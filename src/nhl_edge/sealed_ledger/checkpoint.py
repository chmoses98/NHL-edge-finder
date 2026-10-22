"""Signed head checkpoints and the owner's witness log.

The manifest's hash chain proves that nothing BEFORE a given head was edited, reordered or removed in the middle. It cannot, by itself, show that the newest
entries were not cut off, that the whole chain was not replaced by a freshly built consistent one, or that the branch was not deleted and recreated: all of those
leave a perfectly valid chain. A checkpoint is a small signed statement ``(ledger_id, seq, head_hash, n_entries, time)`` held OUTSIDE the place an attacker can
rewrite. Verification then asks: does the current manifest still contain the checkpointed head at the checkpointed position?

Two signer roles (see the design document for what each does and does not buy):

* ``WITNESS``: the owner, on a local machine, after reading and verifying the public ledger. The strong anchor: the key and the log never touch GitHub.
* ``RUNNER``: optional attestation by the workflow with a signing key from a protected environment. Defends against someone who can push a branch but not read
  that environment's secrets; it does nothing against whoever controls the workflow or the secret. This is a SIGNING key, unrelated to the decryption key.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey

from nhl_edge.sealed_ledger.core import ZERO, canon, read_manifest, sha256_hex

DOM_CP = b"sift-sealed-ledger/v1/checkpoint\n"
DOM_WITNESS = b"sift-sealed-ledger/v1/witness-chain\n"
SCHEMA = "sift-ledger-checkpoint/1"


def make_checkpoint(entries: list[dict[str, Any]], signer: str, *, now: datetime | None = None) -> dict[str, Any]:
    if not entries:
        raise ValueError("empty manifest")
    if signer not in ("WITNESS", "RUNNER"):
        raise ValueError(signer)
    return {"schema": SCHEMA, "ledger_id": entries[0]["ledger_id"], "seq": len(entries) - 1, "head_hash": entries[-1]["entry_hash"], "n_entries": len(entries),
            "signer": signer, "issued_utc": (now or datetime.now(UTC)).strftime("%Y-%m-%dT%H:%M:%SZ")}


def sign(cp: dict[str, Any], key: Ed25519PrivateKey) -> dict[str, Any]:
    return {"checkpoint": cp, "sig_hex": key.sign(DOM_CP + canon(cp)).hex()}


def verify_signature(signed: dict[str, Any], pub: Ed25519PublicKey) -> bool:
    try:
        pub.verify(bytes.fromhex(signed["sig_hex"]), DOM_CP + canon(signed["checkpoint"]))
        return True
    except (InvalidSignature, ValueError, KeyError, TypeError):
        return False


def generate_key() -> Ed25519PrivateKey:
    return Ed25519PrivateKey.generate()


def private_pem(key: Ed25519PrivateKey, passphrase: bytes | None) -> bytes:
    enc = serialization.BestAvailableEncryption(passphrase) if passphrase else serialization.NoEncryption()
    return key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, enc)


def public_pem(key: Ed25519PrivateKey | Ed25519PublicKey) -> bytes:
    pub = key.public_key() if isinstance(key, Ed25519PrivateKey) else key
    return pub.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)


def load_private(pem: bytes, passphrase: bytes | None) -> Ed25519PrivateKey:
    k = serialization.load_pem_private_key(pem, password=passphrase)
    if not isinstance(k, Ed25519PrivateKey):
        raise ValueError("not an Ed25519 key")
    return k


def load_public(pem: bytes) -> Ed25519PublicKey:
    k = serialization.load_pem_public_key(pem)
    if not isinstance(k, Ed25519PublicKey):
        raise ValueError("not an Ed25519 key")
    return k


# ---- the owner's local witness log: JSON lines, each carrying the hash of the previous line so the log itself is tamper-evident --------------------------------

def witness_append(log: Path, signed: dict[str, Any]) -> dict[str, Any]:
    lines = [json.loads(x) for x in log.read_text().splitlines() if x.strip()] if log.exists() else []
    prev = lines[-1]["line_hash"] if lines else ZERO
    body = {"seq": len(lines), "signed": signed, "prev_line_hash": prev}
    body["line_hash"] = sha256_hex(DOM_WITNESS + canon(body))
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a") as fh:
        fh.write(json.dumps(body, sort_keys=True) + "\n")
    return body


def witness_read(log: Path, pub: Ed25519PublicKey) -> tuple[list[dict[str, Any]], list[str]]:
    """Read and authenticate the witness log. Returns (signed checkpoints, problems)."""
    problems: list[str] = []
    out: list[dict[str, Any]] = []
    if not log.exists():
        return out, problems
    prev = ZERO
    for i, ln in enumerate(x for x in log.read_text().splitlines() if x.strip()):
        e = json.loads(ln)
        body = {k: v for k, v in e.items() if k != "line_hash"}
        if e.get("seq") != i or e.get("prev_line_hash") != prev or e.get("line_hash") != sha256_hex(DOM_WITNESS + canon(body)):
            problems.append(f"witness log line {i} does not chain (the owner's own log was edited or lines removed)")
        if not verify_signature(e["signed"], pub):
            problems.append(f"witness log line {i}: bad signature")
        prev = e.get("line_hash", "")
        out.append(e["signed"])
    return out, problems


def check_against_checkpoints(entries: list[dict[str, Any]], signed: list[dict[str, Any]]) -> list[str]:
    """Every checkpointed head must still be present, unchanged and at the same position."""
    problems: list[str] = []
    for s in signed:
        cp = s["checkpoint"]
        if not entries or entries[0].get("ledger_id") != cp["ledger_id"]:
            problems.append(f"checkpoint {cp['signer']}@{cp['issued_utc']} is for a different ledger: the ledger was REPLACED or recreated")
            continue
        if len(entries) - 1 < cp["seq"]:
            problems.append(f"checkpoint {cp['signer']}@{cp['issued_utc']} is at seq {cp['seq']} but the ledger now ends at seq {len(entries) - 1}: TRUNCATED / ROLLED BACK")
        elif entries[cp["seq"]]["entry_hash"] != cp["head_hash"]:
            problems.append(f"checkpoint {cp['signer']}@{cp['issued_utc']}: entry {cp['seq']} no longer matches the checkpointed head hash: REWRITTEN")
    return problems


def check_store(root: Path, signed: list[dict[str, Any]]) -> list[str]:
    return check_against_checkpoints(read_manifest(root), signed)
