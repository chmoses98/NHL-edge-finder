"""Sealed (encrypted, tamper-evident) prospective research ledger (RESEARCH_ONLY, shadow).

The prospective evaluation tier holds outcome-bearing records that must stay unread until the preregistered look (150 games). The repository is public, so the
records are encrypted on the GitHub Actions runner with ``age`` (X25519 key agreement, ChaCha20-Poly1305 payload; implemented by ``pyrage``) to PUBLIC keys that
are committed to the repository. The matching private key is held by the owner, outside the research infrastructure, and is never uploaded, read or used by any
workflow or development tool. Only ciphertext, a plaintext hash-chained manifest of non-outcome metadata and optional signed checkpoints are published.

Module map (the trust boundary is the file ``owner.py``):

* ``core``       canonical JSON, hashing, manifest entries, ``verify_store`` (no cryptography beyond SHA-256; read-only).
* ``seal``       ``SealedStore``: encrypt-only append (genesis / record / correction / day-close). Cannot decrypt.
* ``checkpoint`` Ed25519 signed checkpoints and the owner's witness log (rollback / truncation / replacement detection).
* ``runner``     CLI used by the daily workflow: ingest-and-seal, blinded scorecard, verify, attest. Imports ``seal`` and ``core`` only.
* ``owner``      OWNER-LOCAL tool: key generation, key check, decryption, witness, the single look. Refuses to run in CI. Imported by nothing else.
* ``selftest``   synthetic-outcome end-to-end exercise with a THROWAWAY key. Never reads the archive or a real store.

See ``docs/research/nhl-model-improvement/SEALED_LEDGER_DESIGN.md`` for the threat model and ``SEALED_LEDGER_KEY_SETUP.md`` for the owner's procedure.
"""

from __future__ import annotations

import hashlib
import json

from nhl_edge.model_research import PROSPECTIVE_FREEZE_UTC

SCHEMA = "sift-sealed-ledger/1"
RECORD_SCHEMA = "sift-sealed-record/1"

# The preregistered, frozen prospective rules (docs/research/nhl-model-improvement/PROSPECTIVE_PROTOCOL.md). The sealed ledger commits to their hash in its genesis
# entry and refuses to append if they differ, so a change to the threshold or the spending schedule cannot happen unnoticed. ``tests`` pin the hash literally.
PROTOCOL_RULES = {
    "freeze_utc": PROSPECTIVE_FREEZE_UTC,
    "looks_games": [150, 300, 450],
    "alpha_spending_cumulative_one_sided": [0.0007, 0.0164, 0.05],
    "max_primary_hypotheses": 3,
    "independent_unit": "game",
}


def protocol_rules_sha256() -> str:
    return hashlib.sha256(json.dumps(PROTOCOL_RULES, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
