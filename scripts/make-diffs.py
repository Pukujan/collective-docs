#!/usr/bin/env python3
"""
make-diffs.py — Compare version snapshots and generate diffs.

For each source, compares the latest version with the previous version.
Diffs are stored in diffs/<source>/ and kept forever.
"""

import difflib
import json
import os
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def generate_diff(old_content, new_content, old_version, new_version):
    """Generate a unified diff string."""
    old_lines = old_content.splitlines(keepends=True)
    new_lines = new_content.splitlines(keepends=True)

    diff = difflib.unified_diff(
        old_lines, new_lines,
        fromfile=f'v{old_version}',
        tofile=f'v{new_version}',
        n=3  # Context lines
    )
    return ''.join(diff)


def get_versions(source_name):
    """Get sorted list of version timestamps for a source."""
    versions_dir = ROOT / 'versions' / source_name
    if not versions_dir.exists():
        return []
    return sorted([d.name for d in versions_dir.iterdir() if d.is_dir()])


def process_source(source_name):
    """Generate diffs for the latest two versions if not already diffed."""
    versions = get_versions(source_name)
    if len(versions) < 2:
        print(f"  SKIP: Need at least 2 versions, have {len(versions)}")
        return

    diffs_dir = ROOT / 'diffs' / source_name
    diffs_dir.mkdir(parents=True, exist_ok=True)

    old_ver = versions[-2]
    new_ver = versions[-1]
    diff_key = f"{old_ver}-{new_ver}"

    # Skip if diff already exists
    diff_path = diffs_dir / f"{diff_key}.diff"
    if diff_path.exists():
        print(f"  Diff already exists: {diff_key}")
        return

    old_dir = ROOT / 'versions' / source_name / old_ver
    new_dir = ROOT / 'versions' / source_name / new_ver

    diff_parts = []
    total_changes = 0
    changed_files = []

    # Get all pages that exist in either version
    all_files = set()
    if old_dir.exists():
        all_files.update(old_dir.glob('*.md'))
    if new_dir.exists():
        all_files.update(new_dir.glob('*.md'))

    for f in sorted(all_files):
        fname = f.name
        old_path = old_dir / fname
        new_path = new_dir / fname

        old_content = old_path.read_text(encoding='utf-8') if old_path.exists() else ''
        new_content = new_path.read_text(encoding='utf-8') if new_path.exists() else ''

        if old_content == new_content:
            continue

        diff = generate_diff(old_content, new_content, old_ver, new_ver)
        if diff.strip():
            diff_parts.append(f"=== {fname} ===\n{diff}")
            total_changes += diff.count('\n-') + diff.count('\n+')
            changed_files.append(fname)

    if diff_parts:
        header = (
            f"# Diff: {source_name} ({old_ver} -> {new_ver})\n"
            f"# Generated: {datetime.utcnow().isoformat()}\n"
            f"# Files changed: {len(changed_files)}\n"
            f"# Total changes: {total_changes} lines\n"
            f"# Changed files: {', '.join(changed_files)}\n\n"
        )
        diff_content = header + '\n\n'.join(diff_parts)
        diff_path.write_text(diff_content, encoding='utf-8')
        print(f"  Diff written: {diff_key} ({len(changed_files)} files, {total_changes} changes)")
    else:
        print(f"  No changes between {old_ver} and {new_ver}")


def main():
    sources = sys.argv[1:]
    if not sources:
        versions_root = ROOT / 'versions'
        if versions_root.exists():
            sources = [d.name for d in versions_root.iterdir() if d.is_dir()]

    if not sources:
        print("No sources found")
        sys.exit(0)

    for source in sources:
        print(f"\n=== Diffs: {source} ===")
        process_source(source)

    print("\nDone.")


if __name__ == '__main__':
    main()
