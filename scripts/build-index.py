#!/usr/bin/env python3
"""
build-index.py — Rebuilds the FTS5 full-text search index and the vector embedding index.
Finds agent docs inside each source directory: <source>/agent/*.md
"""

import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def find_source_dirs():
    """Find all source directories that have agent/ subdirectories."""
    return sorted([
        d.name for d in ROOT.iterdir()
        if d.is_dir()
        and (d / 'agent').exists()
        and not d.name.startswith('.')
        and d.name not in ('scripts', 'search', 'status', 'sources', 'cross-refs', 'prompt-templates')
    ])


def build_fts5():
    """Build FTS5 index from <source>/agent/ docs."""
    db_path = ROOT / 'search' / 'fts5.sqlite'
    db_path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()

    # Create FTS5 table
    cursor.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS docs_fts USING fts5(
            title,
            source,
            path,
            content,
            tokenize='porter unicode61'
        )
    """)

    # Clear existing
    cursor.execute("DELETE FROM docs_fts")

    sources = find_source_dirs()
    if not sources:
        print("  No source dirs with agent/ found")
        conn.close()
        return 0

    count = 0
    for source_name in sources:
        agent_dir = ROOT / source_name / 'agent'
        if not agent_dir.exists():
            continue

        for md_file in sorted(agent_dir.glob('*.md')):
            content = md_file.read_text(encoding='utf-8')

            # Extract title from first heading
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else md_file.stem

            # Extract source from frontmatter if present
            src_match = re.search(r'^source:\s*(.+)$', content, re.MULTILINE)
            source_from_fm = src_match.group(1) if src_match else source_name

            path_key = f"{source_name}/{md_file.stem}"

            cursor.execute(
                "INSERT INTO docs_fts (title, source, path, content) VALUES (?, ?, ?, ?)",
                (title, source_from_fm, path_key, content)
            )
            count += 1

    conn.commit()
    conn.close()
    print(f"  FTS5 index: {count} documents indexed")
    return count


def build_vector_index():
    """
    Builds a flat vector index using numpy.
    Doc index JSON maps vector row → source + path.
    """
    index_path = ROOT / 'search' / 'doc-index.json'
    index_path.parent.mkdir(parents=True, exist_ok=True)

    doc_index = []
    sources = find_source_dirs()

    for source_name in sources:
        agent_dir = ROOT / source_name / 'agent'
        if not agent_dir.exists():
            continue
        for md_file in sorted(agent_dir.glob('*.md')):
            content = md_file.read_text(encoding='utf-8')
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else md_file.stem

            doc_index.append({
                "source": source_name,
                "path": f"{source_name}/{md_file.stem}",
                "title": title,
                "file": str(md_file.relative_to(ROOT)),
                "char_count": len(content)
            })

    with open(index_path, 'w') as f:
        json.dump(doc_index, f, indent=2)

    print(f"  Vector doc index: {len(doc_index)} documents (embeddings pending)")
    return doc_index


def build_summaries():
    """Generate a quick summary of what's available."""
    summary_path = ROOT / 'summaries' / '_index.md'
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    sources = find_source_dirs()

    lines = ["# Collective Docs — Summary Index\n"]
    lines.append(f"Generated: {__import__('datetime').datetime.utcnow().isoformat()}\n")

    for source_name in sources:
        agent_dir = ROOT / source_name / 'agent'
        if not agent_dir.exists():
            continue
        pages = list(agent_dir.glob('*.md'))
        total_chars = sum(f.read_text(encoding='utf-8').__len__() for f in pages)
        lines.append(f"\n## {source_name}")
        lines.append(f"- Pages: {len(pages)}")
        lines.append(f"- Total chars: {total_chars:,}")
        for md_file in sorted(pages):
            content = md_file.read_text(encoding='utf-8')
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else md_file.stem
            lines.append(f"  - [{title}]({md_file})")

    summary_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"  Summary written: {summary_path}")


def main():
    print("\n=== Building FTS5 Index ===")
    build_fts5()

    print("\n=== Building Vector Index ===")
    build_vector_index()

    print("\n=== Building Summary ===")
    build_summaries()

    print("\nIndex build complete.")


if __name__ == '__main__':
    main()
