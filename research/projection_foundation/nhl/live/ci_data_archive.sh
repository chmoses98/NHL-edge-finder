#!/usr/bin/env bash
# Sparse, blobless view of the multi-GB `data-archive` branch holding only what the NHL live pipeline reads:
#   player_events/ (all: final-game history)        context/schedule + goalie_observations (36 days: P(start), results look-back)
#   context/lines, injuries, predictions_player (4 days: availability look-back + incumbent forecasts)
# usage: ci_data_archive.sh <target dir>
set -euo pipefail
DEST="${1:?target dir}"
git fetch --depth=1 --filter=blob:none origin data-archive
rm -rf "$DEST" && git worktree add --no-checkout -f "$DEST" FETCH_HEAD
git -C "$DEST" sparse-checkout init --no-cone
pats=(/player_events/)
for i in $(seq -1 36); do
  d=$(date -u -d "-$i days" +%F)
  pats+=("/context/schedule/dt=$d/" "/context/goalie_observations/dt=$d/")
  if [ "$i" -le 4 ]; then pats+=("/context/lines/dt=$d/" "/context/injuries/dt=$d/" "/predictions_player/dt=$d/"); fi
done
git -C "$DEST" sparse-checkout set --no-cone "${pats[@]}"
git -C "$DEST" checkout -q
du -sh "$DEST" || true
