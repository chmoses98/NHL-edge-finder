"""Encrypt-only append to a sealed store. This module can seal records; it has no way to read them back (no identity, no decrypt call).

``SealedStore.seal_rows`` is idempotent by ``game_id`` (a game already sealed is skipped, never duplicated or rewritten) and resumable: a ciphertext is written
atomically first and the manifest line is appended (fsync) second, so an interrupted run leaves at worst an orphan ciphertext that the next run overwrites at the
same sequence number. A change to a historical record is only ever a new, explicitly requested, versioned correction (reason code from a closed list); the earlier
ciphertext and its manifest entry stay.
"""

from __future__ import annotations

import os
import secrets
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import pyrage
from pyrage import x25519

from nhl_edge.sealed_ledger import RECORD_SCHEMA, SCHEMA, protocol_rules_sha256
from nhl_edge.sealed_ledger.core import (
    CORRECTION_REASONS,
    EXCLUSION_REASONS,
    PAD_BYTES,
    SEALED_DIR,
    ZERO,
    canon,
    ct_path,
    finish_entry,
    read_manifest,
    sha256_hex,
    verify_store,
)

MAX_GAMES_PER_RUN = 60  # an NHL slate has at most ~16 games; a larger batch is a bug or an abuse and fails closed


class SealError(Exception):
    pass


def load_recipients(path: Path) -> tuple[list[Any], str]:
    """Parse an ``age`` recipients file (public keys only). Returns the recipient objects and the SHA-256 of the file as committed."""
    raw = path.read_bytes()
    recs = []
    for ln in raw.decode().splitlines():
        t = ln.strip()
        if not t or t.startswith("#"):
            continue
        if t.upper().startswith("AGE-SECRET-KEY") or "PRIVATE KEY" in t.upper():
            raise SealError("the recipients file contains a SECRET key; refusing to continue (publish public keys only)")
        try:
            recs.append(x25519.Recipient.from_str(t))
        except Exception as e:  # noqa: BLE001 - library raises its own RecipientError
            raise SealError(f"not an age public key: {t[:12]}...") from e
    if not recs:
        raise SealError("no recipients configured: nothing can be sealed (fail closed)")
    if len({str(r) for r in recs}) != len(recs):
        raise SealError("the same public key is listed more than once; a backup recipient must be a DIFFERENT key")
    return recs, sha256_hex(raw)


def _plaintext(ledger_id: str, seq: int, game_id: str, version: int, record: dict[str, Any]) -> bytes:
    body = canon({"schema": RECORD_SCHEMA, "ledger_id": ledger_id, "seq": seq, "game_id": game_id, "version": version, "record": record})
    if len(body) > PAD_BYTES - 1:
        raise SealError(f"record is {len(body)} bytes; larger than the fixed {PAD_BYTES}-byte slot (refusing: size would leak)")
    return body + b" " * (PAD_BYTES - len(body))


def _canary_plaintext(ledger_id: str) -> bytes:
    body = canon({"schema": RECORD_SCHEMA, "kind": "CANARY", "ledger_id": ledger_id, "seq": 0, "text": "SYNTHETIC CANARY - not a game record; proves the key opens this ledger"})
    return body + b" " * (PAD_BYTES - len(body))


def _pregame(record: dict[str, Any]) -> dict[str, Any]:
    age = record.get("slate_age_min")
    return {"slate_age_min": None if age is None else round(float(age), 3), "sb_present": record.get("sb_p_home") is not None}


def _atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    with tmp.open("wb") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def _append_line(path: Path, entry: dict[str, Any]) -> None:
    line = canon(entry) + b"\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("ab") as fh:
        fh.write(line)
        fh.flush()
        os.fsync(fh.fileno())


class SealedStore:
    def __init__(self, root: Path, recipients_file: Path, *, run_id: str = "", code_sha: str = "", now: datetime | None = None, repair_torn_tail: bool = False, create: bool = True):
        self.root = Path(root)
        self.recips, self.recipients_sha256 = load_recipients(recipients_file)
        self.run_id, self.code_sha = run_id, code_sha
        self._now = now
        if create or (self.root / "manifest.jsonl").exists():
            self.root.mkdir(parents=True, exist_ok=True)
        if repair_torn_tail:
            self._repair_torn_tail()
        if (self.root / "manifest.jsonl").exists():
            rep = verify_store(self.root, recipients_sha256=self.recipients_sha256, allow_orphans=True)
            if not rep.ok:
                raise SealError("existing store failed verification; refusing to append: " + "; ".join(rep.problems[:5]))
        elif not create:
            raise SealError("the sealed ledger is not initialised: run the init procedure (runner init / workflow init_ledger) and have the owner verify and register its genesis hash first")
        else:
            self._genesis()
        self.entries = read_manifest(self.root)
        self.ledger_id = self.entries[0]["ledger_id"]

    def _ts(self) -> str:
        return (self._now or datetime.now(UTC)).strftime("%Y-%m-%dT%H:%M:%SZ")

    def _repair_torn_tail(self) -> None:
        """Drop ONLY an incomplete final manifest line (a crash mid-append). Complete entries are never touched."""
        p = self.root / "manifest.jsonl"
        if not p.exists():
            return
        raw = p.read_bytes()
        if raw and not raw.endswith(b"\n"):
            keep = raw[: raw.rfind(b"\n") + 1]
            if keep:
                p.write_bytes(keep)
            else:
                p.unlink()  # a torn GENESIS: nothing was ever committed, start the chain again

    def _genesis(self) -> None:
        ledger_id = secrets.token_hex(16)
        ct = pyrage.encrypt(_canary_plaintext(ledger_id), self.recips)
        _atomic_write(ct_path(self.root, 0), ct)
        e = finish_entry({"v": 1, "schema": SCHEMA, "seq": 0, "kind": "GENESIS", "ledger_id": ledger_id, "created_utc": self._ts(),
                          "recipients_sha256": self.recipients_sha256, "recipient_count": len(self.recips), "pad_bytes": PAD_BYTES,
                          "protocol_rules_sha256": protocol_rules_sha256(), "canary_ct_sha256": sha256_hex(ct), "canary_ct_bytes": len(ct),
                          "run_id": self.run_id, "code_sha": self.code_sha, "prev_hash": ZERO})
        _append_line(self.root / "manifest.jsonl", e)

    def _head(self) -> dict[str, Any]:
        return self.entries[-1]

    def sealed_versions(self) -> dict[str, tuple[int, int]]:
        out: dict[str, tuple[int, int]] = {}
        for e in self.entries:
            if e["kind"] == "RECORD":
                out[e["game_id"]] = (e["version"], e["seq"])
        return out

    def _seal_one(self, row: dict[str, Any], version: int, supersedes: int | None, reason: str | None, source_asof: str | None = None) -> dict[str, Any]:
        seq = len(self.entries)
        gid = str(row["game_id"])
        ct = pyrage.encrypt(_plaintext(self.ledger_id, seq, gid, version, row), self.recips)
        _atomic_write(ct_path(self.root, seq), ct)  # 1) ciphertext (atomic)   2) manifest line (fsync)
        e = finish_entry({"v": 1, "seq": seq, "kind": "RECORD", "game_id": gid, "game_date_et": str(row["game_date_et"]), "version": version, "supersedes": supersedes,
                          "reason": reason, "ct_sha256": sha256_hex(ct), "ct_bytes": len(ct), "pregame": _pregame(row), "sealed_utc": self._ts(),
                          "source_asof_utc": source_asof or self._ts(), "run_id": self.run_id, "code_sha": self.code_sha, "prev_hash": self._head()["entry_hash"]})
        _append_line(self.root / "manifest.jsonl", e)
        self.entries.append(e)
        return e

    def seal_rows(self, rows: list[dict[str, Any]], *, correct: dict[str, int] | None = None, reason: str | None = None, source_asof: str | None = None) -> dict[str, int]:
        """Seal each row once. ``correct`` maps game id -> the version currently sealed that is to be superseded by this row (a versioned correction). Naming the
        expected version makes a correction idempotent: repeating the same request after it was applied is refused as stale instead of stacking versions."""
        correct = dict(correct or {})
        if len(rows) > MAX_GAMES_PER_RUN:
            raise SealError(f"{len(rows)} rows in one run exceeds the bound of {MAX_GAMES_PER_RUN}")
        if correct and reason not in CORRECTION_REASONS:
            raise SealError(f"a correction needs a reason code from {CORRECTION_REASONS}")
        if len({str(r['game_id']) for r in rows}) != len(rows):
            raise SealError("duplicate game_id within one batch")
        have = self.sealed_versions()
        unknown = {g for g in correct if g not in have}
        if unknown:
            raise SealError(f"cannot correct games that were never sealed: {sorted(unknown)}")
        stale = {g: (v, have[g][0]) for g, v in correct.items() if have[g][0] != v}
        if stale:
            raise SealError(f"stale correction (game: requested-version, current-version): {stale}; nothing was changed")
        missing_rows = {g for g in correct if g not in {str(r['game_id']) for r in rows}}
        if missing_rows:
            raise SealError(f"correction requested but no re-derived row supplied for: {sorted(missing_rows)}")
        n_new = n_skip = n_corr = 0
        for r in rows:
            gid = str(r["game_id"])
            if gid in have:
                if gid in correct:
                    ver, seq = have[gid]
                    self._seal_one(r, ver + 1, seq, reason, source_asof)
                    n_corr += 1
                else:
                    n_skip += 1  # idempotent: already sealed, never rewritten
                continue
            self._seal_one(r, 1, None, None, source_asof)
            n_new += 1
        return {"sealed_new": n_new, "skipped_existing": n_skip, "corrections": n_corr}

    def close_day(self, game_date_et: str, scheduled_game_ids: list[str], missing_pregame_game_ids: list[str], excluded_game_ids: list[str] | None = None,
                  exclusion_reason: str | None = None) -> bool:
        """Commit publicly to which games were eligible on a date (public schedule facts), so a later omission is visible. Idempotent per date. ``excluded_game_ids`` are
        scheduled games that never finished (or whose start moved across the freeze), waived by an explicit, reason-coded owner decision; they can never be sealed."""
        excluded = sorted(set(excluded_game_ids or []))
        if excluded and exclusion_reason not in EXCLUSION_REASONS:
            raise SealError(f"an exclusion needs a reason code from {EXCLUSION_REASONS}")
        if excluded and not set(excluded) <= set(scheduled_game_ids):
            raise SealError("excluded games must be scheduled on that date")
        if any(e["kind"] == "DAY" and e["game_date_et"] == game_date_et for e in self.entries):
            return False
        have = {e["game_id"] for e in self.entries if e["kind"] == "RECORD" and e["game_date_et"] == game_date_et}
        if excluded and set(excluded) & {e["game_id"] for e in self.entries if e["kind"] == "RECORD"}:
            raise SealError("cannot exclude a game that already has a sealed record")
        sealed = sorted((have & set(scheduled_game_ids)) - set(excluded))
        miss = sorted(set(missing_pregame_game_ids) - set(excluded))
        if sorted(set(sealed) | set(miss) | set(excluded)) != sorted(set(scheduled_game_ids)):
            raise SealError("cannot close the day: some scheduled games are neither sealed, nor listed as missing a pregame forecast, nor explicitly excluded")
        e = finish_entry({"v": 1, "seq": len(self.entries), "kind": "DAY", "game_date_et": game_date_et, "scheduled_game_ids": sorted(set(scheduled_game_ids)),
                          "sealed_game_ids": sealed, "missing_pregame_game_ids": miss, "excluded_game_ids": excluded,
                          "exclusion_reason": exclusion_reason if excluded else None, "sealed_utc": self._ts(), "run_id": self.run_id, "code_sha": self.code_sha,
                          "prev_hash": self._head()["entry_hash"]})
        _append_line(self.root / "manifest.jsonl", e)
        self.entries.append(e)
        return True


__all__ = ["MAX_GAMES_PER_RUN", "SEALED_DIR", "SealError", "SealedStore", "load_recipients"]
