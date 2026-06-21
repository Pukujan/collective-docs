# collective-docs

A curated, auto-updating documentation collection for all the tools, APIs, and
frameworks I use. Serves as the **primary knowledge base** — local tools check
here first before going online.

## 📚 What's Here

| Tool | Status | Last Updated | Pages |
|------|--------|-------------|-------|
| ✨ [Hermes Agent](hermes/human/) | Active | — | — |
| 🔧 [OpenCode](opencode/human/) | Pending | — | — |
| 🤖 [DeepSeek](deepseek/human/) | Pending | — | — |

## 🏗 Structure

```
collective-docs/
├── <source>/human/      # Full, human-readable markdown
├── <source>/agent/      # Stripped, token-efficient markdown for LLMs
├── <source>/versions/   # Last 5 full snapshots per source
├── <source>/diffs/      # All version-to-version diffs (keep forever)
├── <source>/summaries/  # Per-update changelogs
├── search/              # FTS5 keyword + vector semantic search
├── cross-refs/          # Inter-source relationship links
├── status/              # Health and freshness tracking
├── sources/             # YAML configs driving the updates
└── scripts/             # Fetch, build, index, diff machinery
```

## 🔍 Searching

```bash
# Keyword search (instant, no API calls)
python search/search.py --keyword "rate limit"

# Semantic search (uses embeddings)
python search/search.py --semantic "how do I configure providers"

# Full-text grep
rg -i "api key" */agent/
```

## 🔄 Auto-Updates

A cron job runs daily to:
1. Fetch latest docs from each source
2. Generate agent-optimized copies
3. Create version snapshots and diffs
4. Rebuild FTS5 + vector search indexes
5. Detect cross-references between sources
6. Generate update summaries
7. Commit and push to GitHub

## 🤖 For AI Agents

Drop this repo into any agent's context. The `AGENTS.md`, `CLAUDE.md`, and
`.cursorrules` files tell agents to search local docs before going online.
`llms.txt` provides a standard-compliant index for any LLM-aware tool.
