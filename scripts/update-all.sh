#!/usr/bin/env bash
# update-all.sh — Master update script (manual or cron)
# Runs the full pipeline: fetch -> build agent -> make diffs -> build index -> storage check -> git commit
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

PYTHON="python3"

echo "============================================"
echo "  collective-docs — Daily Update"
echo "  $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
echo "============================================"

# Step 1: Fetch new content from all sources
echo ""
echo "=== Step 1: Fetch ==="
$PYTHON scripts/fetch.py --all || echo "  Warning: fetch had errors"

# Step 2: Build agent-optimized copies
echo ""
echo "=== Step 2: Build Agent Copies ==="
$PYTHON scripts/build-agent.py

# Step 3: Generate diffs for new versions
echo ""
echo "=== Step 3: Generate Diffs ==="
$PYTHON scripts/make-diffs.py

# Step 4: Rebuild search indexes
echo ""
echo "=== Step 4: Build Search Indexes ==="
$PYTHON scripts/build-index.py

# Step 5: Storage check & auto-shard
echo ""
echo "=== Step 5: Storage Check & Auto-Shard ==="
$PYTHON scripts/shard-manager.py check 2>&1 | tail -3

# If over 500MB hard limit, auto-shard into next repo
SIZE_MB=$($PYTHON -c "
import subprocess as sp
r = sp.run(['du', '-sm', '--exclude=.git', '.'], capture_output=True, text=True)
print(int(r.stdout.split()[0]))
" 2>/dev/null || echo "0")
if [ "$SIZE_MB" -ge 500 ]; then
  echo "  Over 500MB threshold — creating shard..."
  $PYTHON scripts/shard-manager.py apply
  echo "  Shard created. Continuing update on primary repo."
fi

# Step 6: Git commit and push
echo ""
echo "=== Step 6: Git Commit & Push ==="
if [ "$NO_GIT" = false ]; then
    git add -A
    if git diff --cached --quiet; then
        echo "  No changes to commit."
    else
        git commit -m "docs: daily update $(date -u '+%Y-%m-%d')"
        git push origin main 2>/dev/null || git push origin master 2>/dev/null || echo "  Push skipped (no remote or branch mismatch)"
        echo "  Committed and pushed."
    fi
else
    echo "  Git — SKIPPED (--no-git flag)"
fi

echo ""
echo "============================================"
echo "  Update complete."
echo "============================================"
