#!/usr/bin/env python3
"""
embed.py — Generate vector embeddings for all agent/ docs using DeepSeek API.

This script:
1. Reads all docs from agent/<source>/
2. Chunks each doc into ~512-token segments
3. Calls the DeepSeek embeddings API
4. Saves the vectors as numpy .npy file + updates doc-index.json

Usage:
    export DEEPSEEK_API_KEY="sk-..."
    python scripts/embed.py

Or set the key in your Hermes config / .env:
    python scripts/embed.py --api-key sk-...
"""

import json
import os
import re
import sys
from pathlib import Path

try:
    import numpy as np
except ImportError:
    print("numpy is required. Install with: pip install numpy")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SEARCH_DIR = ROOT / 'search'

# DeepSeek API
EMBEDDING_URL = "https://api.deepseek.ai/v1/embeddings"
EMBEDDING_MODEL = "deepseek-embedding"  # or text-embedding-ada-002 compatible
EMBEDDING_DIM = 1024  # DeepSeek embedding dimension


def chunk_text(text, max_chars=2000):
    """Split text into roughly equal chunks by paragraph."""
    paragraphs = text.split('\n\n')
    chunks = []
    current = []
    current_len = 0

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if current_len + len(para) > max_chars and current:
            chunks.append('\n\n'.join(current))
            current = []
            current_len = 0
        current.append(para)
        current_len += len(para)

    if current:
        chunks.append('\n\n'.join(current))

    return chunks if chunks else [text]


def get_embedding(text, api_key):
    """Call DeepSeek embeddings API for a single text."""
    import urllib.request
    import urllib.error

    data = json.dumps({
        "model": EMBEDDING_MODEL,
        "input": text
    }).encode('utf-8')

    req = urllib.request.Request(
        EMBEDDING_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())
            return result['data'][0]['embedding']
    except urllib.error.HTTPError as e:
        print(f"    API error: {e.code} — {e.read().decode()[:200]}")
        return None
    except Exception as e:
        print(f"    Error: {e}")
        return None


def main():
    api_key = None
    for i, arg in enumerate(sys.argv[1:]):
        if arg == '--api-key' and i + 1 < len(sys.argv):
            api_key = sys.argv[i + 1]

    if not api_key:
        api_key = os.environ.get('DEEPSEEK_API_KEY')

    if not api_key:
        print("ERROR: DeepSeek API key required.")
        print("Set DEEPSEEK_API_KEY env var or pass --api-key <key>")
        sys.exit(1)

    # Collect all docs
    agent_root = ROOT / 'agent'
    if not agent_root.exists():
        print("No agent/ directory found. Run build-agent.py first.")
        sys.exit(1)

    docs = []
    for source_dir in sorted(agent_root.iterdir()):
        if not source_dir.is_dir():
            continue
        for md_file in sorted(source_dir.glob('*.md')):
            content = md_file.read_text(encoding='utf-8')
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else md_file.stem
            docs.append({
                "source": source_dir.name,
                "path": f"{source_dir.name}/{md_file.stem}",
                "title": title,
                "file": str(md_file.relative_to(ROOT)),
                "content": content,
            })

    print(f"Generating embeddings for {len(docs)} documents...")

    # Chunk and embed
    all_vectors = []
    doc_index = []

    for i, doc in enumerate(docs):
        print(f"  [{i+1}/{len(docs)}] {doc['source']}/{doc['title']}...")

        chunks = chunk_text(doc['content'])
        chunk_vectors = []

        for chunk in chunks:
            vec = get_embedding(chunk, api_key)
            if vec:
                chunk_vectors.append(vec)
            # Small delay to avoid rate limits
            import time
            time.sleep(0.1)

        if chunk_vectors:
            # Average chunk vectors to get one doc vector
            avg_vec = np.mean(chunk_vectors, axis=0)
            all_vectors.append(avg_vec)
            doc_index.append({
                "source": doc["source"],
                "path": doc["path"],
                "title": doc["title"],
                "file": doc["file"],
                "chunks": len(chunks),
            })
        else:
            print(f"    SKIP: no embeddings generated")

    if not all_vectors:
        print("No vectors generated. Check API key and connectivity.")
        sys.exit(1)

    # Save vectors
    vectors_array = np.array(all_vectors, dtype=np.float32)
    vectors_path = SEARCH_DIR / 'vectors.npy'
    np.save(str(vectors_path), vectors_array)
    print(f"\nSaved {len(all_vectors)} vectors ({vectors_array.nbytes/1024:.1f} KB)")

    # Save doc index
    index_path = SEARCH_DIR / 'doc-index.json'
    with open(index_path, 'w') as f:
        json.dump(doc_index, f, indent=2)
    print(f"Saved doc-index.json with {len(doc_index)} entries")

    # Update search.py vec search to use this
    print("\nEmbeddings ready! To search:")
    print("  python search/search.py --semantic \"your question\"")


if __name__ == '__main__':
    main()
