#!/usr/bin/env bash
# Commit new archive content to `projection-data` (additions to immutable dirs, rewrites of the latest views) and push.
# Runs only after every stage succeeded. archive_guard runs before the commit and again after any re-base on a moved remote.
# On a rejected push the remote tip is fetched, OUR added/changed files are re-applied on top of it (nothing existing is ever
# rewritten by the merge itself) and the guard runs again. usage: ci_publish.sh <dir>
set -euo pipefail
DIR="${1:?archive dir}"; PF="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$DIR"
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
guard() { (cd "$PF" && python -m pf_core.archive_guard "$DIR"); }
git add -A
if git diff --cached --quiet; then echo "no change; nothing to publish"; exit 0; fi
guard
git commit -qm "NHL live shadow $(date -u +%Y-%m-%dT%H:%MZ) (research_only)"
SAVE="$(mktemp -d)"
for i in 1 2 3 4; do
  if git push origin HEAD:projection-data; then echo "pushed"; exit 0; fi
  echo "push rejected (remote moved); re-applying our files on the new tip, retry $i"; sleep $((2 ** i))
  git diff-tree --root --no-commit-id -r --name-only --diff-filter=AM HEAD > "$SAVE/files.txt"
  while IFS= read -r f; do mkdir -p "$SAVE/files/$(dirname "$f")"; cp "$f" "$SAVE/files/$f"; done < "$SAVE/files.txt"
  git fetch -q --depth=1 origin projection-data
  git reset -q --hard FETCH_HEAD
  cp -r "$SAVE/files/." .
  git add -A
  if git diff --cached --quiet; then echo "remote already has our content"; exit 0; fi
  guard
  git commit -qm "NHL live shadow $(date -u +%Y-%m-%dT%H:%MZ) (research_only)"
  rm -rf "$SAVE/files"
done
echo "::error::could not push projection-data after 4 attempts"; exit 1
