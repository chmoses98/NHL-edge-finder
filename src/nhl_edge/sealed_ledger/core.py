"""Manifest format, hashing and read-only verification of a sealed store. No decryption, no key material.

Store layout (everything published is one of these)::

    manifest.jsonl          one canonical-JSON entry per line, hash-chained (GENESIS, RECORD, DAY)
    sealed/NNNNNN.age       age ciphertext of one game record; NNNNNN is the manifest sequence number (opaque: not a game id, not a date)
    checkpoints/*.json      optional signed head checkpoints

Entries carry NO outcome-derived number. A RECORD entry holds the game id and date (public schedule facts), a version, a ciphertext hash and fixed size, and two
PREGAME data-quality measures. Every PLAINTEXT is padded to the same fixed length before encryption, so ciphertext length carries no information about the record. (``age`` adds a random-length
"grease" header, so ciphertext lengths differ by about a hundred bytes from run to run; that jitter is independent of the content and is bounded by ``size_band``.)
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from nhl_edge.sealed_ledger import SCHEMA, protocol_rules_sha256

ZERO = "0" * 64
DOM_ENTRY = b"sift-sealed-ledger/v1/entry\n"
PAD_BYTES = 4096  # fixed plaintext size before encryption (real records are ~0.9 KB); a larger record fails closed instead of leaking its size
MANIFEST = "manifest.jsonl"
SEALED_DIR = "sealed"
CHECKPOINT_DIR = "checkpoints"
CORRECTION_REASONS = ("SOURCE_SCORE_REVISED", "PIPELINE_DEFECT_FIXED", "OTHER_DOCUMENTED")
AGE_HEADER = b"age-encryption.org/v1\n"
ALLOWED_TOP = {MANIFEST, SEALED_DIR, CHECKPOINT_DIR, "README.md"}
_CT_NAME = re.compile(r"^\d{6}\.age$")
_CP_NAME = re.compile(r"^[A-Za-z0-9_.-]+\.json$")


def canon(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False).encode()


def sha256_hex(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def entry_hash(body: dict[str, Any]) -> str:
    return sha256_hex(DOM_ENTRY + canon({k: v for k, v in body.items() if k != "entry_hash"}))


def finish_entry(body: dict[str, Any]) -> dict[str, Any]:
    out = dict(body)
    out["entry_hash"] = entry_hash(out)
    return out


class TornManifest(Exception):
    """The last manifest line is not a complete entry (an interrupted append)."""


def read_manifest(root: Path, *, allow_torn_tail: bool = False) -> list[dict[str, Any]]:
    p = root / MANIFEST
    if not p.exists():
        return []
    raw = p.read_bytes()
    lines = raw.split(b"\n")
    torn = raw != b"" and not raw.endswith(b"\n")
    out: list[dict[str, Any]] = []
    for i, ln in enumerate(lines):
        if not ln.strip():
            continue
        try:
            out.append(json.loads(ln))
        except json.JSONDecodeError:
            if i == len(lines) - 1 and allow_torn_tail:
                break
            raise TornManifest(f"manifest line {i} is not valid JSON") from None
    if torn and not allow_torn_tail:
        raise TornManifest("manifest does not end with a newline (interrupted append)")
    return out


def size_band(recipient_count: int) -> tuple[int, int]:
    """Plausible ciphertext length for a fixed-size plaintext: payload + age header (+ one stanza per recipient) + random grease. Outside it => not our padding."""
    return PAD_BYTES, PAD_BYTES + 600 + 250 * max(1, recipient_count)


def ct_path(root: Path, seq: int) -> Path:
    return root / SEALED_DIR / f"{seq:06d}.age"


@dataclass
class Report:
    problems: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    n_entries: int = 0
    head_seq: int = -1
    head_hash: str = ""
    ledger_id: str = ""
    n_games: int = 0
    n_corrections: int = 0
    days: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.problems

    def summary(self) -> dict[str, Any]:
        return {"ok": self.ok, "problems": self.problems, "warnings": self.warnings, "n_entries": self.n_entries, "head_seq": self.head_seq, "head_hash": self.head_hash,
                "ledger_id": self.ledger_id, "n_games": self.n_games, "n_corrections": self.n_corrections}


def verify_store(root: Path, *, recipients_sha256: str | None = None) -> Report:
    """Structural verification that needs no secret: chain, hashes, fixed ciphertext size, version discipline, no stray (possibly plaintext) files."""
    rep = Report()
    try:
        entries = read_manifest(root)
    except TornManifest as e:
        rep.problems.append(f"torn manifest: {e}")
        return rep
    rep.n_entries = len(entries)
    if not entries:
        rep.problems.append("empty or missing manifest")
        return rep
    prev = ZERO
    first_ver: dict[str, int] = {}
    last_ver: dict[str, tuple[int, int]] = {}  # game_id -> (version, seq)
    days: set[str] = set()
    band = (0, 0)
    referenced: set[int] = set()
    for i, e in enumerate(entries):
        if e.get("seq") != i:
            rep.problems.append(f"entry {i}: seq is {e.get('seq')!r}")
        if e.get("prev_hash") != prev:
            rep.problems.append(f"entry {i}: prev_hash does not match the previous entry (history rewritten, reordered or truncated in the middle)")
        if e.get("entry_hash") != entry_hash(e):
            rep.problems.append(f"entry {i}: entry_hash does not match its contents (entry edited)")
        prev = e.get("entry_hash", "")
        kind = e.get("kind")
        if i == 0:
            if kind != "GENESIS":
                rep.problems.append("entry 0 is not GENESIS")
                continue
            rep.ledger_id = str(e.get("ledger_id", ""))
            band = size_band(int(e.get("recipient_count", 1)))
            if e.get("schema") != SCHEMA:
                rep.problems.append(f"unknown schema {e.get('schema')!r}")
            if e.get("pad_bytes") != PAD_BYTES:
                rep.problems.append("genesis pad_bytes differs from this code (ciphertext sizes would vary)")
            if e.get("protocol_rules_sha256") != protocol_rules_sha256():
                rep.problems.append("genesis protocol_rules_sha256 differs from the frozen prospective protocol in this code")
            if recipients_sha256 is not None and e.get("recipients_sha256") != recipients_sha256:
                rep.problems.append("recipients file does not match the recipients committed in the genesis entry")
            continue
        if kind == "GENESIS":
            rep.problems.append(f"entry {i}: second GENESIS")
        elif kind == "RECORD":
            gid, ver, sup = e.get("game_id"), e.get("version"), e.get("supersedes")
            if not isinstance(gid, str) or not isinstance(ver, int):
                rep.problems.append(f"entry {i}: malformed RECORD")
                continue
            referenced.add(i)
            if gid not in last_ver:
                if ver != 1 or sup is not None or e.get("reason") is not None:
                    rep.problems.append(f"entry {i}: first record of game {gid} must be version 1 with no supersedes/reason")
                first_ver[gid] = i
                rep.n_games += 1
            else:
                pv, ps = last_ver[gid]
                rep.n_corrections += 1
                if ver != pv + 1 or sup != ps:
                    rep.problems.append(f"entry {i}: correction of game {gid} must be version {pv + 1} superseding seq {ps}")
                if e.get("reason") not in CORRECTION_REASONS:
                    rep.problems.append(f"entry {i}: correction reason {e.get('reason')!r} not in {CORRECTION_REASONS}")
            last_ver[gid] = (ver, i)
            if not band[0] <= int(e.get("ct_bytes", -1)) <= band[1]:
                rep.problems.append(f"entry {i}: ciphertext size {e.get('ct_bytes')} is outside the fixed-padding band {band}")
            p = ct_path(root, i)
            if not p.exists():
                rep.problems.append(f"entry {i}: ciphertext file {p.name} is missing (deleted)")
            else:
                data = p.read_bytes()
                if not data.startswith(AGE_HEADER):
                    rep.problems.append(f"entry {i}: file {p.name} is not an age ciphertext (possible plaintext!)")
                if sha256_hex(data) != e.get("ct_sha256") or len(data) != e.get("ct_bytes"):
                    rep.problems.append(f"entry {i}: ciphertext {p.name} does not match the manifest hash/size (replaced or modified)")
        elif kind == "DAY":
            d = e.get("game_date_et")
            if d in days:
                rep.problems.append(f"entry {i}: second DAY entry for {d}")
            days.add(d)
            for gid in e.get("sealed_game_ids", []):
                if gid not in last_ver:
                    rep.problems.append(f"entry {i}: DAY {d} lists game {gid} that has no earlier RECORD")
            if sorted(set(e.get("sealed_game_ids", [])) | set(e.get("missing_pregame_game_ids", []))) != sorted(e.get("scheduled_game_ids", [])):
                rep.problems.append(f"entry {i}: DAY {d} does not account for every scheduled game")
        else:
            rep.problems.append(f"entry {i}: unknown kind {kind!r}")
    rep.head_seq, rep.head_hash = len(entries) - 1, entries[-1].get("entry_hash", "")
    rep.days = sorted(days)
    sd = root / SEALED_DIR
    if sd.exists():
        for f in sorted(sd.iterdir()):
            if not _CT_NAME.match(f.name):
                rep.problems.append(f"unexpected file in {SEALED_DIR}/: {f.name}")
            elif int(f.name[:6]) not in referenced:
                rep.warnings.append(f"orphan ciphertext {f.name} (an interrupted run; overwritten by the next seal at that sequence number)")
    for f in sorted(root.iterdir()):
        if f.name not in ALLOWED_TOP and not f.name.startswith(".git"):
            rep.problems.append(f"unexpected top-level file {f.name!r}: only ciphertext, the manifest and checkpoints may be published")
    cd = root / CHECKPOINT_DIR
    if cd.exists():
        for f in sorted(cd.iterdir()):
            if not _CP_NAME.match(f.name):
                rep.problems.append(f"unexpected file in {CHECKPOINT_DIR}/: {f.name}")
    return rep


def is_extension(old: list[dict[str, Any]], new: list[dict[str, Any]]) -> list[str]:
    """``new`` must contain every entry of ``old`` unchanged and in place (append-only)."""
    problems = []
    if len(new) < len(old):
        problems.append(f"new manifest has {len(new)} entries, previous had {len(old)} (truncation / rollback)")
    for i, e in enumerate(old[: len(new)]):
        if new[i].get("entry_hash") != e.get("entry_hash"):
            problems.append(f"entry {i} differs from the previous manifest (history rewritten)")
            break
    return problems
