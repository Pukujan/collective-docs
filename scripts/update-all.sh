#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PY="${PYTHON:-/c/Users/pujan/AppData/Local/hermes/hermes-agent/venv/Scripts/python}"
NO_GIT=false

for arg in "$@"; do
    if [ "$arg" = "--no-git" ]; then NO_GIT=true; fi
done

echo "=== collective-docs update $(date -Iseconds) ==="
echo "Root: $ROOT"

echo ""
echo "=== Step 1: Fetch all sources ==="
cd "$ROOT"
for cfg in sources/*.yaml; do
    # Skip files with no pages
    page_count=$(grep -c '  - path:' "$cfg" 2>/dev/null || echo 0)
    [ "$page_count" -eq 0 ] && echo "  SKIP $cfg (no pages)" && continue
    echo "  Fetching $cfg..."
    $PY scripts/fetch.py "$cfg" 2>&1 | tail -1
done

echo ""
echo "=== Step 2: Build agent docs ==="
$PY scripts/build-agent.py 2>&1

echo ""
echo "=== Step 3: Make diffs ==="
$PY scripts/make-diffs.py 2>&1

echo ""
echo "=== Step 4: Build search index ==="
$PY scripts/build-index.py 2>&1

echo ""
echo "=== Step 5: Storage check ==="
$PY scripts/shard-manager.py check 2>&1

if [ "$NO_GIT" = false ]; then
    echo ""
    echo "=== Step 6: Git commit & push ==="
    git add -A
    if git diff --cached --quiet; then
        echo "  Nothing changed — skipping commit"
    else
        git commit -m "docs: daily update $(date +%Y-%m-%d)"
        git push origin main 2>&1
    fi
fi

echo ""
echo "=== Done at $(date -Iseconds) ==="
