#!/usr/bin/env python3
"""
search.py — Dual search interface for Collective Docs.

Modes:
  --keyword QUERY   Full-text search via FTS5 (instant, no API calls)
  --semantic QUERY  Vector similarity search via numpy cosine similarity
  --hybrid QUERY    Combines both results

  --json            Output as JSON
  --top N           Results to return (default: 10)
  --source NAME     Filter to a specific source
"""

import argparse
import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent if __file__.endswith("search.py") else Path.cwd()
LAZY_REFRESH = str(ROOT / "scripts" / "lazy-refresh.py")


def auto_fresh(source=None, quiet=True):
    """Check if docs are stale and refresh if needed. Only does work if >24h old."""
    cmd = [sys.executable or "python3", LAZY_REFRESH]
    if source:
        cmd += ["--source", source]
    else:
        cmd += ["--all"]
    if quiet:
        cmd += ["--json"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=130)
    if result.returncode == 0 and not quiet:
        print(result.stdout, file=sys.stderr, end="")
    return result.returncode == 0


def keyword_search(query, top_k=10, source=None):
    """FTS5 full-text search."""
    db_path = ROOT / "search" / "fts5.sqlite"
    if not db_path.exists():
        return {"error": "FTS5 index not found. Run scripts/build-index.py first."}

    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()

    # FTS5 query with ranking
    try:
        if source:
            cursor.execute(
                "SELECT title, source, path, content "
                "FROM docs_fts WHERE docs_fts MATCH ? AND source = ? "
                "ORDER BY rank LIMIT ?",
                (query, source, top_k)
            )
        else:
            cursor.execute(
                "SELECT title, source, path, content "
                "FROM docs_fts WHERE docs_fts MATCH ? "
                "ORDER BY rank LIMIT ?",
                (query, top_k)
            )
    except sqlite3.OperationalError as e:
        conn.close()
        return {"error": f"Query error: {e}"}

    results = []
    for title, src, path, content in cursor.fetchall():
        # Manual snippet: find the match in content
        import re as _re
        snippet = content[:200] + "..." if len(content) > 200 else content
        match = _re.search(_re.escape(query)[:40], content, _re.I)
        if match:
            start = max(0, match.start() - 60)
            end = min(len(content), match.end() + 60)
            snippet = ("..." if start > 0 else "") + content[start:end].replace('\n', ' ') + ("..." if end < len(content) else "")
        results.append({
            "title": title,
            "source": src,
            "path": path,
            "snippet": snippet[:200],
            "relevance": "fts5_ranked"
        })

    conn.close()
    return {"mode": "keyword", "query": query, "count": len(results), "results": results}


def semantic_search(query, top_k=10, source=None):
    """Vector similarity search using numpy embeddings."""
    embeddings_path = ROOT / "search" / "nnp_embeddings.npy"
    chunks_path = ROOT / "search" / "nnp_chunks.json"

    if not embeddings_path.exists():
        return {"error": "Vector embeddings not found. Run scripts/embed.py first."}

    import numpy as np

    # Check for DeepSeek API key
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        # Try reading from Hermes .env
        env_path = Path.home() / ".hermes" / ".env"
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("DEEPSEEK_API_KEY="):
                        api_key = line.split("=", 1)[1].strip().strip("'\"")
                        break

    if not api_key:
        return {"error": "No DEEPSEEK_API_KEY found. Set it in ~/.hermes/.env or export it."}

    # Load chunks
    with open(chunks_path) as f:
        chunks = json.load(f)

    if source:
        filtered = [(i, c) for i, c in enumerate(chunks) if c.get("source") == source]
        indices = [i for i, _ in filtered]
        chunks = [c for _, c in filtered]
    else:
        indices = list(range(len(chunks)))

    if not chunks:
        return {"error": "No matching chunks found."}

    # Generate query embedding via DeepSeek
    import requests

    resp = requests.post(
        "https://api.deepseek.com/v1/embeddings",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={"model": "deepseek-chat", "input": query}
    )

    if resp.status_code != 200:
        return {"error": f"DeepSeek API error: {resp.status_code} {resp.text[:200]}"}

    data = resp.json()
    query_emb = np.array(data["data"][0]["embedding"], dtype=np.float32)

    # Load embeddings (only the chunks we need)
    full_embeddings = np.load(str(embeddings_path))
    if source:
        embeddings = full_embeddings[indices]
    else:
        embeddings = full_embeddings

    # Cosine similarity
    norms = np.linalg.norm(embeddings, axis=1)
    norms[norms == 0] = 1  # Avoid division by zero
    similarities = np.dot(embeddings, query_emb) / norms

    top_indices = np.argsort(similarities)[-top_k:][::-1]

    results = []
    for idx in top_indices:
        actual_idx = indices[idx] if source else idx
        chunk = chunks[idx]
        results.append({
            "title": chunk.get("title", "untitled"),
            "source": chunk.get("source", "unknown"),
            "path": chunk.get("path", chunk.get("page", "unknown")),
            "snippet": chunk.get("text", "")[:200] + "...",
            "score": float(similarities[idx])
        })

    return {"mode": "semantic", "query": query, "count": len(results), "results": results}


def hybrid_search(query, top_k=10, source=None):
    """Combined keyword + semantic search."""
    kw_results = keyword_search(query, top_k=top_k * 2, source=source)
    sem_results = semantic_search(query, top_k=top_k * 2, source=source)

    if "error" in kw_results:
        return kw_results
    if "error" in sem_results:
        return kw_results  # Fall back to keyword-only

    # Merge by averaging ranks
    seen = {}
    for i, r in enumerate(kw_results.get("results", [])):
        key = f"{r['source']}/{r['path']}"
        seen[key] = {"keyword_rank": i, "semantic_rank": None, **r}

    for i, r in enumerate(sem_results.get("results", [])):
        key = f"{r['source']}/{r['path']}"
        if key in seen:
            seen[key]["semantic_rank"] = i
        else:
            seen[key] = {"keyword_rank": None, "semantic_rank": i, **r}

    # Score: average of normalized ranks (lower = better)
    max_k = max(top_k * 2, 1)
    scored = []
    for key, item in seen.items():
        kr = item.pop("keyword_rank", None)
        sr = item.pop("semantic_rank", None)
        if kr is not None and sr is not None:
            score = (kr / max_k + sr / max_k) / 2
        elif kr is not None:
            score = kr / max_k
        else:
            score = sr / max_k
        scored.append((score, item))

    scored.sort(key=lambda x: x[0])

    return {"mode": "hybrid", "query": query, "count": min(len(scored), top_k), "results": [r for _, r in scored[:top_k]]}


def main():
    parser = argparse.ArgumentParser(description="Search Collective Docs")
    parser.add_argument("--keyword", "-k", help="Keyword search query")
    parser.add_argument("--semantic", "-s", help="Semantic search query")
    parser.add_argument("--hybrid", "-b", help="Hybrid search query")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--top", type=int, default=10, help="Number of results")
    parser.add_argument("--source", help="Filter to source")

    args = parser.parse_args()

    # Auto-refresh before searching — only fetches if >24h stale
    if args.keyword or args.semantic or args.hybrid:
        source_arg = args.source if args.source != "all" else None
        auto_fresh(source=source_arg, quiet=not args.json)

    if args.keyword:
        result = keyword_search(args.keyword, args.top, args.source)
    elif args.semantic:
        result = semantic_search(args.semantic, args.top, args.source)
    elif args.hybrid:
        result = hybrid_search(args.hybrid, args.top, args.source)
    else:
        parser.print_help()
        sys.exit(1)

    if args.json or isinstance(result, dict) and "error" in result:
        print(json.dumps(result, indent=2))
        if "error" in result:
            sys.exit(1)
        return

    print(f"Mode: {result.get('mode', '?')} | Query: '{result.get('query', '?')}' | {result.get('count', 0)} results\n")
    for i, r in enumerate(result.get("results", []), 1):
        print(f"{i}. [{r.get('source', '?')}] {r.get('title', '?')}")
        print(f"   Path: {r.get('path', '?')}")
        if "score" in r:
            print(f"   Score: {r['score']:.3f}")
        if "snippet" in r:
            print(f"   {r['snippet']}")
        print()


if __name__ == "__main__":
    main()
