#!/usr/bin/env bash
# OWNER-LOCAL (macOS). Runs `owner weekly-check`: fetch the public ledger (fast-forward only), verify it against everything you registered, sign a witness checkpoint, and raise a
# macOS notification if anything is wrong or the ledger stopped growing. Schedule it with launchd (see SEALED_LEDGER_UNATTENDED.md). It decrypts nothing and never runs a look.
# The witness-key passphrase comes from your login Keychain: `security add-generic-password -a "$USER" -s sift-witness -w` (prompts; never put it in a file).
set -euo pipefail
HOME_DIR="${SIFT_LEDGER_HOME:-$HOME/sift-ledger}"
LEDGER_URL="${SIFT_LEDGER_URL:?set SIFT_LEDGER_URL=https://github.com/<owner>/<ledger repo>.git}"
export PYTHONPATH="$HOME_DIR/repo/src"
set +e
"$HOME_DIR/venv/bin/python" -m nhl_edge.sealed_ledger.owner weekly-check \
      --store "$HOME_DIR/ledger" --dir "$HOME_DIR/witness" \
      --recipients "$HOME_DIR/repo/research/sealed_ledger/recipients.txt" \
      --ledger-url "$LEDGER_URL" --passphrase-cmd "security find-generic-password -s sift-witness -w" > "$HOME_DIR/last_check.json"
rc=$?
set -e
case "$rc" in
  0) exit 0 ;;
  2) osascript -e 'display notification "Ledger verified and witnessed, but no day has closed for a while. See ~/sift-ledger/last_check.json" with title "SIFT research ledger"' || true; exit 0 ;;
  *) osascript -e 'display notification "Sealed-ledger check FAILED. Do not witness. See ~/sift-ledger/last_check.json" with title "SIFT research ledger"' || true; exit 1 ;;
esac
