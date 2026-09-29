#!/usr/bin/env bash
# Commit research outputs to the branch this workflow ran on. Refuses the default branch and data-archive.
# usage: research_commit.sh "<message>" <path>...
set -uo pipefail
msg="$1"; shift
if [ "${GITHUB_REF_NAME}" = "${DEFAULT_BRANCH:-main}" ] || [ "${GITHUB_REF_NAME}" = "data-archive" ]; then
  echo "::warning title=Refusing to push::ran on ${GITHUB_REF_NAME}; outputs stay in the workspace"
  exit 0
fi
git config user.name "nhl-edge-bot"
git config user.email "nhl-edge-bot@users.noreply.github.com"
for p in "$@"; do git add -f $p 2>/dev/null || true; done
if git diff --cached --quiet; then echo "nothing to commit"; exit 0; fi
git commit -qm "$msg"
for i in 1 2 3 4 5; do
  # binary research files from separate jobs never overlap; on a conflicting path this run's copy wins
  git pull --rebase -X theirs origin "${GITHUB_REF_NAME}" && git push origin HEAD:"${GITHUB_REF_NAME}" && exit 0
  sleep $((2**i))
done
echo "::error::could not push research outputs"; exit 1
