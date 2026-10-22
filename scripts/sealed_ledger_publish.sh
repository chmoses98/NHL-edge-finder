#!/usr/bin/env bash
# Publish a staged sealed store (ciphertext + manifest only) to the ledger REPOSITORY with a deploy key that can write that repository and nothing else.
# Called by the publish jobs of sealed_ledger_daily.yml (mode `append`, unattended) and sealed_ledger_admin.yml (mode `init` or `append`, owner-approved).
#
#   env: MODE (append|init)  STAGED  LEDGER_REPO (owner/name)  CODE_REPO (owner/name of THIS repository)  ACTIVATION  GENESIS (append only)  DEPLOY_KEY  MESSAGE
#
# Fails closed: the owner's activation hash must equal the SHA-256 of research/sealed_ledger/recipients.txt (a key change or a protocol change in code invalidates it until the
# owner re-registers), an append needs the owner's registered genesis hash, the destination must be a different repository than the code repository, and the push is a plain
# fast-forward (no force, no delete). The key is written to a 0600 temp file, handed to ssh by PATH and removed on exit; it is never echoed or put on a command line.
set -euo pipefail
: "${MODE:?}" "${STAGED:?}" "${LEDGER_REPO:?}" "${CODE_REPO:?}" "${DEPLOY_KEY:?the owner has not stored the ledger deploy key in this environment}" "${MESSAGE:?}"
[[ "$MODE" == append || "$MODE" == init ]] || { echo "::error::bad mode"; exit 1; }
[[ "$LEDGER_REPO" =~ ^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$ ]] || { echo "::error::SEALED_LEDGER_REPO is not an owner/name"; exit 1; }
[ "${LEDGER_REPO,,}" != "${CODE_REPO,,}" ] || { echo "::error::the ledger repository must be a different repository than the code repository"; exit 1; }

rec=research/sealed_ledger/recipients.txt
grep -qE '^age1[0-9a-z]{50,}$' "$rec" || { echo "::error::no owner public key in $rec (the sealed ledger is not set up)"; exit 1; }
actual=$(sha256sum "$rec" | cut -d' ' -f1)
[ -n "${ACTIVATION:-}" ] && [ "$ACTIVATION" = "$actual" ] || { echo "::error::not activated for this exact recipients file (environment variable SEALED_LEDGER_ACTIVATION_SHA)"; exit 1; }
args=()
if [ "$MODE" = append ]; then
  [[ "${GENESIS:-}" =~ ^[0-9a-f]{64}$ ]] || { echo "::error::the owner has not registered the verified genesis hash (environment variable SEALED_LEDGER_GENESIS_HASH)"; exit 1; }
  args+=(--expect-genesis "$GENESIS")
else
  [ -z "${GENESIS:-}" ] || { echo "::error::init refused: a genesis hash is already registered (a ledger was already initialised and verified)"; exit 1; }
  args+=(--init)
fi

umask 077
key=$(mktemp)
trap 'rm -f "$key"' EXIT
printf '%s\n' "$DEPLOY_KEY" > "$key"
python -m nhl_edge.sealed_ledger.runner publish --staged "$STAGED" --recipients "$rec" \
  --read-url "https://github.com/${LEDGER_REPO}.git" --push-url "git@github.com:${LEDGER_REPO}.git" \
  --ssh-key "$key" --forbid-repo "$CODE_REPO" --message "$MESSAGE" "${args[@]}"
