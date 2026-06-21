#!/usr/bin/env python3
"""
lazy-refresh.py — On-demand doc freshness check.

When an agent or user looks up a source, call this first:
    python scripts/lazy-refresh.py --source hermes

It checks:
  1. Was the doc fetched within the last 24h? If yes → skip (still fresh)
  2. If stale → re-fetch from web (via fetch.py for that source)
  3. If fetch changed content → rebuild indexes for that source only

Returns: "FRESH", "REFRESHED", "CHANGED", or "ERROR:..."

Integration: add this to the search.py invocation so every search
auto-freshens before returning results.

Usage:
    python scripts/lazy-refresh.py --source hermes
    python scripts/lazy-refresh.py --source deepseek --force
    python scripts/lazy-refresh.py --all          # check all stale sources
"""

import json, os, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATUS_DIR = ROOT / "status"
SOURCES_DIR = ROOT / "sources"
FRESHNESS_FILE = STATUS_DIR / "_freshness.json"
MAX_AGE_HOURS = 24  # Re-fetch after this many hours

PYTHON = sys.executable or "python3"
FETCH_SCRIPT = str(ROOT / "scripts" / "fetch.py")
BUILD_INDEX = str(ROOT / "scripts" / "build-index.py")


def load_freshness():
    if FRESHNESS_FILE.exists():
        return json.loads(FRESHNESS_FILE.read_text())
    return {}


def save_freshness(data):
    FRESHNESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    FRESHNESS_FILE.write_text(json.dumps(data, indent=2))


def is_stale(source_name, freshness, force=False):
    """Check if a source needs refresh. Returns True if stale or never fetched."""
    if force:
        return True
    entry = freshness.get(source_name)
    if not entry:
        return True  # Never fetched
    fetched_at = datetime.fromisoformat(entry.get("fetched_at", "2000-01-01"))
    age_hours = (datetime.now(timezone.utc) - fetched_at).total_seconds() / 3600
    return age_hours > MAX_AGE_HOURS


def get_source_names():
    """Get all configured source names (even with empty pages)."""
    import yaml
    names = []
    for f in sorted(SOURCES_DIR.glob("*.yaml")):
        cfg = yaml.safe_load(f.read_text())
        if cfg and cfg.get("name"):
            names.append(cfg["name"])
    return names


def refresh_source(source_name, force=False):
    """Fetch a single source and rebuild its index if content changed."""
    freshness = load_freshness()
    stale = is_stale(source_name, freshness, force=force)

    if not stale:
        last = freshness.get(source_name, {}).get("fetched_at", "?")
        return f"FRESH (last fetched: {last})"

    # Check if source has a config
    config_path = SOURCES_DIR / f"{source_name}.yaml"
    if not config_path.exists():
        return f"ERROR: no config for {source_name}"

    import yaml
    cfg = yaml.safe_load(config_path.read_text())
    if not cfg or not cfg.get("pages"):
        return f"SKIP: no pages configured for {source_name}"

    print(f"  Refreshing {source_name}...", flush=True)

    # Run fetch
    result = subprocess.run(
        [PYTHON, FETCH_SCRIPT, str(config_path)],
        capture_output=True, text=True, timeout=120,
    )

    if result.returncode != 0:
        return f"ERROR: fetch failed — {result.stderr.strip() or result.stdout.strip()[:200]}"

    # Check if content actually changed (compare to previous status)
    status_path = STATUS_DIR / source_name / "status.json"
    prev_hash = freshness.get(source_name, {}).get("content_hash")

    # Simple hash: sum of file sizes in <source>/human/
    human_dir = ROOT / source_name / "human"
    current_hash = ""
    if human_dir.exists():
        total = 0
        count = 0
        for f in human_dir.glob("*.md"):
            total += f.stat().st_size
            count += 1
        current_hash = f"{count}:{total}"

    changed = current_hash != prev_hash

    # Update freshness record
    freshness[source_name] = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "content_hash": current_hash,
        "page_count": count if human_dir.exists() else 0,
    }
    save_freshness(freshness)

    # Rebuild search index if content changed
    if changed and current_hash:
        print(f"  Content changed — rebuilding index...", flush=True)
        subprocess.run(
            [PYTHON, BUILD_INDEX, "--source", source_name],
            capture_output=True, text=True, timeout=60,
        )

    status = "CHANGED" if changed else "UNCHANGED"
    return f"REFRESHED ({status})"


def refresh_all(force=False):
    """Check all sources, refresh stale ones."""
    names = get_source_names()
    results = {}
    for name in names:
        results[name] = refresh_source(name, force=force)
    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Lazy-refresh doc sources")
    parser.add_argument("--source", help="Single source to check")
    parser.add_argument("--all", action="store_true", help="Check all sources")
    parser.add_argument("--force", action="store_true", help="Force refresh even if fresh")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--status", action="store_true", help="Show freshness status of all sources")

    args = parser.parse_args()

    if args.status:
        freshness = load_freshness()
        results = {}
        for name in get_source_names():
            entry = freshness.get(name)
            if entry:
                age = (datetime.now(timezone.utc) - datetime.fromisoformat(entry["fetched_at"])).total_seconds()
                results[name] = {
                    "status": "fresh" if age < MAX_AGE_HOURS * 3600 else "stale",
                    "last_fetched": entry["fetched_at"],
                    "pages": entry.get("page_count", 0),
                    "age_hours": round(age / 3600, 1),
                }
            else:
                results[name] = {"status": "never_fetched"}
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            for name, info in sorted(results.items()):
                emoji = {"fresh": "✓", "stale": "⚠", "never_fetched": "○"}
                print(f"  {emoji.get(info['status'], '?')} {name:<15} {info['status']:<15} last: {info.get('last_fetched', 'never')[:19]}")
        return

    if args.all:
        results = refresh_all(force=args.force)
    elif args.source:
        results = {args.source: refresh_source(args.source, force=args.force)}
    else:
        parser.print_help()
        sys.exit(1)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for name, status in results.items():
            icon = "✓" if status.startswith("FRESH") else "↻" if "REFRESHED" in status else "⚠"
            print(f"  {icon} {name:<15} {status}")


if __name__ == "__main__":
    main()
