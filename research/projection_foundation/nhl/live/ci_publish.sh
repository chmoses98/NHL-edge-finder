#!/usr/bin/env bash
# Commit new archive content to `projection-data` (additions to immutable dirs, rewrites of the latest views) and push.
# Runs only after every stage succeeded. archive_guard runs before the commit and again after any pull. usage: ci_publish.sh <dir>
set -euo pipefail
DIR="${1:?archive dir}"; PF="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$DIR"
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git add -A
if git diff --cached --quiet; then echo "no change; nothing to publish"; exit 0; fi
(cd "$PF" && python -m pf_core.archive_guard "$DIR")
git commit -qm "NHL live shadow $(date -u +%Y-%m-%dT%H:%MZ) (research_only)"
for i in 1 2 3 4; do
  if git push origin HEAD:projection-data; then echo "pushed"; exit 0; fi
  echo "push rejected; retry $i"; sleep $((2 ** i))
  git pull --rebase -q origin projection-data || { git rebase --abort 2>/dev/null || true; }
  (cd "$PF" && python -m pf_core.archive_guard "$DIR")
done
echo "::error::could not push projection-data after 4 attempts"; exit 1
