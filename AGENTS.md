# collective-docs — Primary Knowledge Base

This repository is the authoritative local documentation collection for all tools,
APIs, and frameworks I use (Hermes, OpenCode, DeepSeek, etc.).

## Protocol for any agent reading this

1. **Search local first.** Before making any web request for documentation, run:
   `python search/search.py "your question here"`
   or use ripgrep: `rg -i "your query" */agent/`

2. **Use agent/ not human/.** The `<source>/agent/` directories contain stripped, token-efficient
   markdown optimized for LLM consumption. `<source>/human/` has full formatting with code blocks.

3. **Read the llms.txt** at the project root for a structured index of what's available.

4. **Check summaries/** for TL;DR changelogs before diving into full docs.

5. **Cross-references** in `cross-refs/relation-graph.json` map links between sources
   (e.g., "Hermes docs mention OpenRouter → DeepSeek docs explain how to configure it").

6. **Only go online** if:
   - The local search returns nothing relevant, OR
   - You need the absolute latest version (this collection updates daily)

7. **Prompt templates** in `prompt-templates/` give you pre-built system prompts
   for answering questions about specific tools.

## Directory layout

| Path | Purpose |
|------|---------|
| `<source>/agent/` | Token-optimized docs for LLMs |
| `<source>/human/` | Full human-readable markdown |
| `<source>/versions/` | Last 5 full snapshots (pruned) |
| `<source>/diffs/` | All changes between versions (keep forever) |
| `<source>/summaries/` | Update summaries / TL;DR |
| `search/` | FTS5 keyword + vector semantic search |
| `cross-refs/` | Inter-source relationship graph |
| `status/` | Per-source health and freshness |
| `prompt-templates/` | Agent system prompts |
| `sources/` | YAML configs defining what to fetch |

## Lazy Refresh (on-demand, no cron needed)

Docs auto-fresh when you search — no daily cron burn. The system checks each source's freshness (24h stale threshold) at query time:

1. **`scripts/lazy-refresh.py`** — checks if a source needs updating; only fetches from web if >24h old
2. **`search/search.py`** calls `lazy-refresh` automatically before every search
3. **Freshness status**: `python scripts/lazy-refresh.py --status`
4. **No changes? No refetch.** Uses content hashing — if the source hasn't changed on the web, the index isn't rebuilt
5. **Zero extra overhead** on fresh docs — lookup is instant SQLite
6. **SHARD-INDEX.md** at root — when repos exceed 500MB, auto-splits into collective-docs-2, -3, etc.

```bash
# Check what's fresh/stale
python scripts/lazy-refresh.py --status

# Force-refresh a specific source
python scripts/lazy-refresh.py --source hermes --force

# Search auto-freshens as needed (recommended daily use)
python search/search.py --keyword "delegate_task"
```

## Quick commands for agents

```bash
# Keyword search
python search/search.py --keyword "rate limit"

# Semantic search (uses vector embeddings)
python search/search.py --semantic "how do I configure providers"

# Find in agent docs
rg -i "api key" */agent/

# What changed recently
cat summaries/hermes/latest.md
```
