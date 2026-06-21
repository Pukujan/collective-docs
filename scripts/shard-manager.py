#!/usr/bin/env python3
"""
shard-manager.py — Automatic repo sharding for collective-docs.

When the working tree exceeds a configurable threshold, creates new
repo(s) (collective-docs-2, -3, ...) and distributes source categories.

Helps keep each GitHub repo well under the 1GB soft limit (5GB hard).

Usage:
    python scripts/shard-manager.py check      # Check status
    python scripts/shard-manager.py plan       # Show what would happen
    python scripts/shard-manager.py apply      # Actually shard (creates repos, moves dirs)
    python scripts/shard-manager.py refresh-toc # Regenerate table-of-contents only
"""

import json, os, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "shard-config.json"
TOC = ROOT / "SHARD-INDEX.md"

# Categories grouped by affinity — each lives in one repo
CATEGORIES = {
    "ai": {
        "label": "AI Models & Agent Frameworks",
        "sources": ["hermes", "deepseek", "opencode", "codex", "claude"],
    },
    "devops": {
        "label": "Deployment & Infrastructure",
        "sources": ["vercel", "railway", "docker", "github-actions", "nixpacks"],
    },
    "platform": {
        "label": "Platform APIs & CLIs",
        "sources": ["github", "supabase", "npm", "python", "git"],
    },
    "reference": {
        "label": "Language & Database Reference",
        "sources": ["postgresql", "nodejs", "python-lang", "sqlite"],
    },
}

DEFAULT_THRESHOLD_MB = 100  # Start warning at 100MB, hard action at 500MB

def get_repo_size_mb():
    """Get working tree size (excluding .git) in MB."""
    result = subprocess.run(
        ["du", "-sm", "--exclude=.git", "."], capture_output=True, text=True, cwd=ROOT
    )
    try:
        return int(result.stdout.split()[0])
    except (ValueError, IndexError):
        return 0

def get_shard_number():
    """Return the next shard index (2 for collective-docs-2)."""
    cfg = load_config()
    return cfg.get("next_shard", 2)

def load_config():
    if CONFIG.exists():
        return json.loads(CONFIG.read_text())
    return {
        "next_shard": 2,
        "threshold_mb": DEFAULT_THRESHOLD_MB,
        "shards": {
            "1": {
                "repo": "Pukujan/collective-docs",
                "categories": [],  # empty = all (primary)
                "created": "2026-06-21",
            }
        },
        "source_to_shard": {},
    }

def save_config(cfg):
    CONFIG.write_text(json.dumps(cfg, indent=2))

def get_categories_for_source(source_name):
    """Return which category a source belongs to."""
    for cat, info in CATEGORIES.items():
        if source_name in info["sources"]:
            return cat
    return "other"


def cmd_check():
    """Report current size and shard status."""
    cfg = load_config()
    size_mb = get_repo_size_mb()
    threshold = cfg.get("threshold_mb", DEFAULT_THRESHOLD_MB)

    print(f"collective-docs — Storage Report")
    print(f"{'='*40}")
    print(f"Working tree size:  {size_mb} MB")
    print(f"Shard threshold:    {threshold} MB (soft)")
    print(f"Hard limit:         500 MB (auto-shard)")
    print(f"Active shard:       1 — Pukujan/collective-docs")
    print(f"Next shard index:   {cfg.get('next_shard', 2)}")

    if size_mb >= 500:
        print(f"\n⚠ OVER THRESHOLD — sharding required")
    elif size_mb >= threshold:
        print(f"\n⚠ Over soft threshold — consider sharding")
    else:
        print(f"\n✓ Well under limits ({size_mb}/{threshold} MB)")

    if cfg.get("source_to_shard"):
        print(f"\nExisting shards:")
        for src, shard_num in sorted(cfg["source_to_shard"].items()):
            shard_key = f"collective-docs-{shard_num}" if shard_num > 1 else "collective-docs"
            print(f"  {src:<20} → {shard_key}")

    return size_mb, threshold


def cmd_plan():
    """Show what would happen on shard."""
    cfg = load_config()
    size_mb, threshold = cmd_check()

    if size_mb < 500 and size_mb < threshold * 2:
        print(f"\nNo shard needed ({size_mb} MB). To force: shard-manager.py apply --force")
        return

    next_num = cfg["next_shard"]
    print(f"\nWould create: {cfg.get('repo_template', 'Pukujan/collective-docs-{n}').format(n=next_num)}")
    print(f"Would move: saturated source categories")

    # Check which sources have the most versions
    src_sizes = {}
    for d in ROOT.iterdir():
        if d.is_dir() and (d / 'versions').exists() and not d.name.startswith('.'):
            size = sum(f.stat().st_size for f in d.rglob("*") if f.is_file())
            src_sizes[d.name] = format(size / (1024*1024), ".2f")

    print(f"\nVersion snapshot sizes (MB):")
    for src, sz in sorted(src_sizes.items(), key=lambda x: -float(x[1])):
        print(f"  {src:<20} {sz} MB")


def cmd_apply(force=False):
    """Actually perform sharding: create new repo, move directories."""
    cfg = load_config()
    size_mb = get_repo_size_mb()

    if size_mb < 500 and not force:
        print(f"Only {size_mb} MB — not yet at 500MB hard limit. Use --force to shard anyway.")
        return

    next_num = cfg["next_shard"]
    repo_name = f"collective-docs-{next_num}"
    repo_full = f"Pukujan/{repo_name}"
    repo_path = ROOT.parent / repo_name

    print(f"Sharding to {repo_full}...")

    # Create the new repo directory
    repo_path.mkdir(exist_ok=True)

    # Find which sources are the largest (the ones to move)
    src_sizes = []
    for d in ROOT.iterdir():
        if d.is_dir() and (d / 'versions').exists() and not d.name.startswith('.'):
            total = sum(f.stat().st_size for f in d.rglob("*") if f.is_file())
            src_sizes.append((total, d.name))

    src_sizes.sort(reverse=True)

    # Move half the biggest source categories
    moved_dirs = []
    half_point = len(src_sizes) // 2
    for _, src_name in src_sizes[:max(half_point, 2)]:
        src_path = ROOT / src_name / "human"
        if src_path.exists():
            dest = repo_path / "human" / src_name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src_path), str(dest))
            moved_dirs.append(src_name)

            cfg["source_to_shard"][src_name] = next_num

    # Also copy the scripts and search layer
    for item in ["scripts", "search", "sources", "AGENTS.md", "CLAUDE.md", "llms.txt", "README.md"]:
        src = ROOT / item
        dst = repo_path / item
        if src.is_dir():
            shutil.copytree(str(src), str(dst), dirs_exist_ok=True)
        elif src.is_file():
            shutil.copy2(str(src), str(dst))

    # Initialize git in new repo
    subprocess.run(["git", "init"], cwd=repo_path, capture_output=True)
    subprocess.run(["git", "add", "-A"], cwd=repo_path, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", f"init: shard {next_num} — {', '.join(moved_dirs)}"],
        cwd=repo_path, capture_output=True,
    )

    # Add remote and push
    result = subprocess.run(
        ["gh", "repo", "create", repo_full, "--public", "--push", "--source", "."],
        cwd=repo_path, capture_output=True, text=True,
    )
    if result.returncode == 0:
        print(f"  Created and pushed: https://github.com/{repo_full}")
    else:
        print(f"  Could not create remote: {result.stderr.strip()}")
        print(f"  Local repo at: {repo_path}")

    # Update config
    cfg["next_shard"] = next_num + 1
    cfg["shards"][str(next_num)] = {
        "repo": repo_full,
        "categories": moved_dirs,
        "created": subprocess.run(
            ["date", "-u", "+%Y-%m-%d"], capture_output=True, text=True
        ).stdout.strip(),
    }
    save_config(cfg)

    # Regenerate the table of contents
    cmd_refresh_toc()

    print(f"\n✓ Shard {next_num} created. Sources moved: {', '.join(moved_dirs)}")
    print(f"  Update your agent configs to point to {repo_full} for {', '.join(moved_dirs)} docs.")


def cmd_refresh_toc():
    """Regenerate SHARD-INDEX.md — the master table of contents."""
    cfg = load_config()

    lines = [
        "# collective-docs — Shard Index",
        "",
        "This index maps every doc source to its repo shard. Your agent can use this",
        "to find docs without searching all repos.",
        "",
        f"_(Generated by shard-manager.py on {subprocess.run(['date', '-u', '+%Y-%m-%d'], capture_output=True, text=True).stdout.strip()})_",
        "",
        "---",
        "",
        "## Repositories",
        "",
    ]

    # List all shards
    for num in sorted(cfg["shards"].keys(), key=int):
        info = cfg["shards"][num]
        repo_name = info["repo"]
        if info.get("categories"):
            cats = ", ".join(CATEGORIES.get(c, {}).get("label", c) for c in info["categories"])
            lines.append(f"### [{repo_name}](https://github.com/{repo_name}) — {cats}")
        else:
            lines.append(f"### [{repo_name}](https://github.com/{repo_name}) — Primary (all categories)")

        lines.append("")
        try:
            readme_path = ROOT if num == "1" else (ROOT.parent / f"collective-docs-{num}" / "README.md")
            if readme_path.exists():
                desc = readme_path.read_text().split("\n")[0].lstrip("#").strip()
                lines.append(f"  _{desc}_")
        except Exception:
            pass
        lines.append("")

    lines.extend([
        "---",
        "",
        "## Source-to-Repo Mapping",
        "",
        "| Source | Category | Repo |",
        "|--------|----------|------|",
    ])

    # Build mapping from all shards
    src_map = cfg.get("source_to_shard", {})
    all_sources = set()
    for cat_info in CATEGORIES.values():
        all_sources.update(cat_info["sources"])

    for src in sorted(all_sources):
        shard_num = src_map.get(src, 1)
        repo_name = cfg["shards"].get(str(shard_num), {}).get("repo", "Pukujan/collective-docs")
        cat = get_categories_for_source(src)
        cat_label = CATEGORIES.get(cat, {}).get("label", "Other")
        lines.append(f"| {src:<20} | {cat_label:<30} | [{repo_name}](https://github.com/{repo_name}) |")

    lines.extend([
        "",
        "---",
        "",
        "## How Agents Use This",
        "",
        "1. **Direct lookup**: read SHARD-INDEX.md, find the source's repo",
        "2. **Search script**: `python search/search.py --keyword \"...\"` from the correct repo",
        "3. **Git clone**: `gh repo clone Pukujan/collective-docs-{n}` to pull the right shard locally",
        "",
        "## How Humans Navigate",
        "",
        "Click any repo link above to browse its full human-readable doc collection on GitHub.",
        "Each repo has its own README, AGENTS.md, and file tree organized by source.",
    ])

    TOC.write_text("\n".join(lines) + "\n")
    print(f"  Regenerated: {TOC}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/shard-manager.py <command> [--force]")
        print("  check         — Show storage usage and shard status")
        print("  plan          — Show what a shard would do")
        print("  apply         — Actually create a new shard repo")
        print("  apply --force — Force shard even under threshold")
        print("  refresh-toc   — Regenerate SHARD-INDEX.md")
        sys.exit(1)

    cmd = sys.argv[1]
    force = "--force" in sys.argv

    if cmd == "check":
        cmd_check()
    elif cmd == "plan":
        cmd_plan()
    elif cmd == "apply":
        cmd_apply(force=force)
    elif cmd == "refresh-toc":
        cmd_refresh_toc()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
