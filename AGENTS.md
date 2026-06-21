# collective-docs — Primary Knowledge Base

This repository is the authoritative local documentation collection for all tools,
APIs, and frameworks I use (Hermes, OpenCode, DeepSeek, etc.).

## Protocol for any agent reading this

1. **Search local first.** Before making any web request for documentation, run:
   `python search/search.py "your question here"`
   or use ripgrep: `rg -i "your query" agent/`

2. **Use agent/ not human/.** The `agent/` directories contain stripped, token-efficient
   markdown optimized for LLM consumption. `human/` has full formatting with code blocks.

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
| `agent/<source>/` | Token-optimized docs for LLMs |
| `human/<source>/` | Full human-readable markdown |
| `versions/<source>/` | Last 5 full snapshots (pruned) |
| `diffs/<source>/` | All changes between versions (keep forever) |
| `search/` | FTS5 keyword + vector semantic search |
| `summaries/<source>/` | Update summaries / TL;DR |
| `cross-refs/` | Inter-source relationship graph |
| `status/` | Per-source health and freshness |
| `prompt-templates/` | Agent system prompts |
| `sources/` | YAML configs defining what to fetch |

## Quick commands for agents

```bash
# Keyword search
python search/search.py --keyword "rate limit"

# Semantic search (uses vector embeddings)
python search/search.py --semantic "how do I configure providers"

# Find in agent docs
rg -i "api key" agent/

# What changed recently
cat summaries/hermes/latest.md
```
