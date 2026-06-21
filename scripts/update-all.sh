#!/usr/bin/env bash
# update-all.sh — Master update script (called by cron job)
# Runs the full pipeline: fetch → build agent → make diffs → build index → git commit
#
# Usage:
#   cd /path/to/collective-docs && bash scripts/update-all.sh
#   bash scripts/update-all.sh --no-git   # skip git commit/push

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Parse flags
NO_GIT=false
for arg in "$@"; do
    case "$arg" in
        --no-git) NO_GIT=true ;;
    esac
done

echo "============================================"
echo "  collective-docs — Daily Update"
echo "  $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
echo "============================================"

# Step 1: Fetch new content from all sources
echo ""
echo "=== Step 1: Fetch ==="
python3 scripts/fetch.py --all

# Step 2: Build agent-optimized copies
echo ""
echo "=== Step 2: Build Agent Copies ==="
python3 scripts/build-agent.py

# Step 3: Generate diffs for new versions
echo ""
echo "=== Step 3: Generate Diffs ==="
python3 scripts/make-diffs.py

# Step 4: Rebuild search indexes
echo ""
echo "=== Step 4: Build Search Indexes ==="
python3 scripts/build-index.py

# Step 5: Git commit and push
if [ "$NO_GIT" = false ]; then
    echo ""
    echo "=== Step 5: Git Commit & Push ==="
    git add -A
    if git diff --cached --quiet; then
        echo "  No changes to commit."
    else
        git commit -m "📚 daily update $(date -u '+%Y-%m-%d')"
        git push origin main 2>/dev/null || git push origin master 2>/dev/null || echo "  Push skipped (no remote or branch mismatch)"
        echo "  Committed and pushed."
    fi
else
    echo ""
    echo "=== Step 5: Git — SKIPPED ==="
fi

echo ""
echo "============================================"
echo "  Update complete."
echo "============================================"
