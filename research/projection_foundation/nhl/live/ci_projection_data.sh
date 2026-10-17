#!/usr/bin/env bash
# Check the `projection-data` archive branch out into <target dir>.
#   existing branch -> its tip; missing branch -> a fresh orphan checkout (only when MODE=live; PR/dry-run uses an empty git dir)
# usage: ci_projection_data.sh <target dir> <live|readonly>
set -euo pipefail
DEST="${1:?target dir}"; MODE="${2:-readonly}"
rm -rf "$DEST"
if git ls-remote --exit-code --heads origin projection-data >/dev/null 2>&1; then
  git fetch --depth=1 origin projection-data
  git worktree add -f --detach "$DEST" FETCH_HEAD
  if [ "$MODE" = live ]; then git -C "$DEST" checkout -q -B projection-data; fi
else
  echo "projection-data does not exist yet"
  if [ "$MODE" = live ]; then
    git worktree add --detach -f "$DEST" HEAD
    git -C "$DEST" checkout -q --orphan projection-data
    git -C "$DEST" rm -rfq . || true
    git -C "$DEST" clean -fdxq
  else
    mkdir -p "$DEST" && git init -q "$DEST"
  fi
fi
