#!/usr/bin/env python3
"""
build-agent.py — Create stripped, token-efficient copies of docs for LLM consumption.

Strips frontmatter, fluff paragraphs, nav references, and excessive whitespace.
Files are saved to <source>/agent/ — typically ~40-60% smaller than <source>/human/ versions.
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def strip_for_agent(content):
    """Reduce content to essential LLM-friendly text."""
    # Remove YAML frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

    lines = content.split('\n')
    output = []
    skip_until_content = True

    for line in lines:
        stripped = line.strip()

        # Skip very short or empty lines at the top (fluff before first heading)
        if skip_until_content:
            if stripped.startswith('#') or len(stripped) > 20:
                skip_until_content = False
                output.append(line)
            continue

        # Skip common noise
        if re.search(r'(skip to content|edit this page|was this helpful|on this page|sidebar|table of contents)', stripped, re.I):
            continue

        # Skip single-word lines that aren't headings
        if len(stripped) < 3 and not stripped.startswith('#'):
            continue

        output.append(line)

    text = '\n'.join(output)

    # Normalize whitespace
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    return text.strip()


def process_source(source_name):
    """Process all pages for a source."""
    source_dir = ROOT / source_name
    human_dir = source_dir / 'human'
    agent_dir = source_dir / 'agent'
    agent_dir.mkdir(parents=True, exist_ok=True)

    if not human_dir.exists():
        print(f"  SKIP: {human_dir} does not exist")
        return 0, 0

    total_before = 0
    total_after = 0
    count = 0

    for md_file in sorted(human_dir.glob('*.md')):
        content = md_file.read_text(encoding='utf-8')
        original_size = len(content)
        total_before += original_size

        stripped = strip_for_agent(content)
        total_after += len(stripped)

        agent_path = agent_dir / md_file.name
        agent_path.write_text(stripped, encoding='utf-8')
        count += 1

    savings = 0
    if count > 0:
        savings = (1 - total_after / total_before) * 100 if total_before > 0 else 0
        print(f"  {count} pages: {total_before:,} -> {total_after:,} chars ({savings:.0f}% reduction)")
    else:
        print(f"  No markdown files in {human_dir}")
    return count, savings


def main():
    sources = sys.argv[1:]
    if not sources:
        # Process all sources that have human/ content
        sources = [
            d.name for d in ROOT.iterdir()
            if d.is_dir() and (d / 'human').exists() and not d.name.startswith('.')
        ]

    if not sources:
        print("No sources found to process")
        sys.exit(0)

    total_pages = 0
    for source in sources:
        print(f"\n=== Agent-ifying: {source} ===")
        pages, _ = process_source(source)
        total_pages += pages

    print(f"\nDone. {total_pages} pages processed.")


if __name__ == '__main__':
    main()
