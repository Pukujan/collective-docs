# Claude Code Instructions for collective-docs

This is a local documentation collection. Before searching the web for any
tool, API, or framework documentation, follow these steps:

1. **Search locally first:**
   `python search/search.py --keyword "your query"`
   or `rg -i "your query" */agent/`

2. If nothing found locally, check `summaries/` for recent updates.

3. Only use web search as a last resort.

4. The `<source>/agent/` directories have token-optimized markdown. Use them over `<source>/human/`.

5. `llms.txt` at the root has a structured index of all available docs.
