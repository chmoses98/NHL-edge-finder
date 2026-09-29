"""The NHL routed-wager ledger: schema, identity, append-only store, importers and validator.

LAYOUT (on the ``accounting-data`` branch; the code lives on ``main``)
    data/accounting/wagers.jsonl        one line per ORDER the owner placed (nhl_accounted_wager.v1)
    data/accounting/settlements.jsonl   one line per settled wager (nhl_wager_settlement.v1)

No season partition: an NHL season spans two calendar years, and filing a wager must never require guessing one.

IDENTITY
    ``wager_id``      = "nhlw-" + sha256(source_bet_key)[:24]
    ``settlement_id`` = "nhls-" + sha256(source_bet_key)[:24]
Minted HERE (the router never names NHL's records) from the router's deterministic ``source_bet_key`` alone -- no
wall clock, no batch id, no economics -- so the same order delivered twice lands on the same row.

IDEMPOTENCY AND CONFLICTS
    same key, same canonical fields      -> DUPLICATE_NOOP, and the file is not touched (byte-identical)
    same key, different canonical fields -> CONFLICT: nothing written for that row, the field NAMES are reported,
                                            the importer exits non-zero, and the router's merge gate fails.
Existing lines are never rewritten or removed; the validator proves that against a base ref.

PRIVACY
Everything that reaches stdout or a receipt is a count, a reason, a minted id or a router source key (the router's
receipt contract needs the key). Never a ticker, price, stake, contract count or P&L: these run in public logs.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

WAGER_SCHEMA = "nhl_accounted_wager.v1"
SETTLEMENT_SCHEMA = "nhl_wager_settlement.v1"
ECONOMICS_V2 = "router-settlement-economics.v2"
LEDGER_DIR = Path("data") / "accounting"
WAGERS_FILE = LEDGER_DIR / "wagers.jsonl"
SETTLEMENTS_FILE = LEDGER_DIR / "settlements.jsonl"
ENTRY_METHOD = "IMPORTED_RECEIPT"
VENUE = "kalshi"

NEW, DUPLICATE_NOOP, CONFLICT, REFUSED = "NEW", "DUPLICATE_NOOP", "CONFLICT", "REFUSED"

#: Exactly what the router's ``to_nhl_import_row`` sends. Anything else is refused, not dropped: a sender that
#: believes a field was recorded must not be silently contradicted by the ledger.
WAGER_INPUT_FIELDS = ("source_bet_key", "import_batch_id", "entry_method", "game_date", "market_ticker", "side",
                      "executed_at", "contracts", "execution_price", "stake", "fees_paid", "fees_are_estimated",
                      "venue")
#: Compared on re-delivery. ``import_batch_id`` is provenance of a delivery, not a fact about the order.
WAGER_CANONICAL_FIELDS = ("entry_method", "game_date", "market_ticker", "side", "executed_at", "contracts",
                          "execution_price", "stake", "fees_paid", "fees_are_estimated", "venue")

SETTLEMENT_INPUT_FIELDS = ("source_bet_key", "market_ticker", "side", "settlement_status", "settled_at", "result",
                           "gross_return", "net_profit_loss", "refusals", "venue", "economics_version")
SETTLEMENT_CANONICAL_FIELDS = tuple(f for f in SETTLEMENT_INPUT_FIELDS if f != "source_bet_key")

#: Fields that would assert that this repository's research model had something to do with a bet. Refused on sight
#: -- including ``model_supported=False``, which still claims the model had an opinion.
PROVENANCE_FIELDS = frozenset({
    "recommendation_id", "recommendation", "model_version", "model_evaluation_id", "model_fair_probability",
    "model_probability", "model_supported", "p_data_only", "p_data_only_v2", "p_model", "sim_version",
    "feature_version", "projection_id", "prediction_id", "rating", "edge", "expected_value", "ev",
    "qualification", "readiness", "kelly", "stake_recommendation", "gate", "authority",
})

MONEY_TOLERANCE = 1e-9
_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class RowRefused(ValueError):
    """This row cannot be filed, and filing it anyway would be worse."""


# ------------------------------------------------------------------------------------------------------ identity
def _mint(prefix: str, source_bet_key: Any) -> str:
    if not isinstance(source_bet_key, str) or not source_bet_key.strip():
        raise RowRefused("source_bet_key is required")
    return f"{prefix}-{hashlib.sha256(source_bet_key.encode('utf-8')).hexdigest()[:24]}"


def mint_wager_id(source_bet_key: str) -> str:
    return _mint("nhlw", source_bet_key)


def mint_settlement_id(source_bet_key: str) -> str:
    return _mint("nhls", source_bet_key)


# ------------------------------------------------------------------------------------------------------ validation
def _is_number(v: Any) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(float(v))


def _parse_ts(v: Any) -> bool:
    if not isinstance(v, str) or "T" not in v:
        return False
    try:
        dt = datetime.fromisoformat(v.replace("Z", "+00:00"))
    except ValueError:
        return False
    return dt.tzinfo is not None


def _nonempty(v: Any) -> bool:
    return isinstance(v, str) and bool(v.strip())


def validate_wager(rec: dict) -> list[str]:
    """Every reason this wager row may not be written. Empty means it may. Reasons never quote values."""
    p: list[str] = []
    bad = sorted(set(rec) & PROVENANCE_FIELDS)
    if bad:
        p.append(f"model/recommendation provenance field(s) {bad} are not accounting facts")
    for name in ("wager_id", "source_bet_key", "import_batch_id", "market_ticker", "game_date", "executed_at"):
        if not _nonempty(rec.get(name)):
            p.append(f"{name} is required")
    if rec.get("schema_version") != WAGER_SCHEMA:
        p.append(f"schema_version must be {WAGER_SCHEMA}")
    if _nonempty(rec.get("source_bet_key")) and rec.get("wager_id") != mint_wager_id(rec["source_bet_key"]):
        p.append("wager_id is not the id this ledger mints from source_bet_key")
    if rec.get("entry_method") != ENTRY_METHOD:
        p.append(f"entry_method must be {ENTRY_METHOD}")
    if rec.get("side") not in ("YES", "NO"):
        p.append("side must be YES or NO")
    if _nonempty(rec.get("game_date")) and not _DATE.match(rec["game_date"]):
        p.append("game_date must be YYYY-MM-DD")
    if _nonempty(rec.get("executed_at")) and not _parse_ts(rec["executed_at"]):
        p.append("executed_at must be an RFC 3339 timestamp with a zone")
    c = rec.get("contracts")
    if not _is_number(c) or c <= 0:
        p.append("contracts must be a positive number")
    px = rec.get("execution_price")
    if not _is_number(px) or not (0 < px < 1):
        p.append("execution_price must be a number strictly between 0 and 1 (dollars per contract)")
    st = rec.get("stake")
    if not _is_number(st) or st <= 0:
        p.append("stake must be a positive number")
    fee = rec.get("fees_paid")
    if not _is_number(fee) or fee < 0:
        p.append("fees_paid must be a non-negative number")
    if rec.get("fees_are_estimated") is not False:
        p.append("fees_are_estimated must be false: only the exchange's own reported fees are accepted")
    if rec.get("venue") != VENUE:
        p.append("venue must be kalshi")
    if _is_number(c) and _is_number(px) and _is_number(st) and _is_number(fee) and c > 0:
        # stake = contracts x price + fees, as the router computes it from the fills. Recomputed only as a check,
        # never to fill anything in.
        if abs(st - (c * px + fee)) > 1e-6 * max(1.0, st):
            p.append("stake does not equal contracts x execution_price + fees_paid")
    return p


def validate_settlement(rec: dict) -> list[str]:
    p: list[str] = []
    bad = sorted(set(rec) & PROVENANCE_FIELDS)
    if bad:
        p.append(f"model/recommendation provenance field(s) {bad} are not accounting facts")
    for name in ("settlement_id", "source_bet_key", "market_ticker", "settled_at"):
        if not _nonempty(rec.get(name)):
            p.append(f"{name} is required")
    if rec.get("schema_version") != SETTLEMENT_SCHEMA:
        p.append(f"schema_version must be {SETTLEMENT_SCHEMA}")
    if _nonempty(rec.get("source_bet_key")) and rec.get("settlement_id") != mint_settlement_id(rec["source_bet_key"]):
        p.append("settlement_id is not the id this ledger mints from source_bet_key")
    if rec.get("side") not in ("YES", "NO"):
        p.append("side must be YES or NO")
    if rec.get("settlement_status") != "SETTLED":
        p.append("settlement_status must be SETTLED (an unsettled wager simply has no settlement row)")
    if _nonempty(rec.get("settled_at")) and not _parse_ts(rec["settled_at"]):
        p.append("settled_at must be an RFC 3339 timestamp with a zone")
    if rec.get("result") not in ("WON", "LOST", None):
        p.append("result must be WON, LOST or absent")
    if rec.get("economics_version") != ECONOMICS_V2:
        p.append(f"economics_version must be {ECONOMICS_V2}")
    if rec.get("venue") != VENUE:
        p.append("venue must be kalshi")
    refusals = rec.get("refusals")
    if not isinstance(refusals, list) or not all(isinstance(r, str) for r in refusals):
        p.append("refusals must be a list of strings")
        refusals = []
    g, n = rec.get("gross_return"), rec.get("net_profit_loss")
    for name, v in (("gross_return", g), ("net_profit_loss", n)):
        if v is not None and not _is_number(v):
            p.append(f"{name} must be a number or absent")
    if g is not None and _is_number(g) and g < 0:
        p.append("gross_return may not be negative")
    established = g is not None and n is not None
    if established and refusals:
        p.append("a settlement with established money may not also carry refusals")
    if not established and not refusals:
        p.append("a settlement without established money must say why (refusals)")
    return p


# ----------------------------------------------------------------------------------------------------------- store
def read_jsonl(path: Path) -> list[dict]:
    """Rows of a JSONL ledger. Raises on an undecodable line: an unreadable ledger is not an empty one."""
    if not path.exists():
        return []
    out = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise RowRefused(f"{path.name} line {i} is not JSON") from exc
        if not isinstance(row, dict):
            raise RowRefused(f"{path.name} line {i} is not an object")
        out.append(row)
    return out


def _line(rec: dict) -> str:
    return json.dumps(rec, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"


def _append(path: Path, recs: list[dict]) -> None:
    """Append-only. A file that exists is opened for APPEND and nothing before the end is touched."""
    if not recs:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = path.read_bytes() if path.exists() else b""
    with path.open("a", encoding="utf-8") as fh:
        if existing and not existing.endswith(b"\n"):
            fh.write("\n")
        for r in recs:
            fh.write(_line(r))


def _differs(a: Any, b: Any) -> bool:
    if _is_number(a) and _is_number(b):
        return abs(float(a) - float(b)) > MONEY_TOLERANCE
    return a != b


def conflicting_fields(existing: dict, incoming: dict, fields: tuple[str, ...]) -> list[str]:
    return [f for f in fields if _differs(existing.get(f), incoming.get(f))]


# --------------------------------------------------------------------------------------------------------- wagers
def build_wager(row: Any) -> dict:
    if not isinstance(row, dict):
        raise RowRefused("row is not an object")
    prov = sorted(set(row) & PROVENANCE_FIELDS)
    if prov:
        raise RowRefused(f"model/recommendation provenance field(s) {prov} are not accounting facts")
    unknown = sorted(set(row) - set(WAGER_INPUT_FIELDS))
    if unknown:
        raise RowRefused(f"unknown field(s) {unknown}")
    missing = [f for f in WAGER_INPUT_FIELDS if f not in row]
    if missing:
        raise RowRefused(f"missing field(s) {missing}")
    rec = {k: row[k] for k in WAGER_INPUT_FIELDS}
    rec["wager_id"] = mint_wager_id(row.get("source_bet_key"))
    rec["schema_version"] = WAGER_SCHEMA
    problems = validate_wager(rec)
    if problems:
        raise RowRefused("; ".join(problems))
    return rec


@dataclass
class ImportResult:
    rows: list[dict] = field(default_factory=list)
    written: int = 0
    duplicate: int = 0
    refused: int = 0

    @property
    def conflicted(self) -> bool:
        return self.refused > 0

    def receipts(self, kind: str) -> dict:
        return {"kind": kind, "written": self.written, "alreadyPresent": self.duplicate, "refused": self.refused,
                "rows": self.rows}


def _receipt(index: int, key: Any, id_field: str, ident: str | None, status: str, reason: str | None = None,
             fields: list[str] | None = None) -> dict:
    r = {"row": index, "source_bet_key": key if isinstance(key, str) else None, id_field: ident, "status": status,
         "duplicate_status": status, "success": status in (NEW, DUPLICATE_NOOP)}
    if reason:
        r["reason"] = reason
    if fields:
        r["conflicting_fields"] = list(fields)
    return r


def import_wagers(base_dir: Path, rows: list, import_batch_id: str | None = None) -> ImportResult:
    """Write every new wager; DUPLICATE_NOOP identical repeats; CONFLICT/REFUSE the rest, per row."""
    path = Path(base_dir) / WAGERS_FILE
    on_file = {r.get("source_bet_key"): r for r in read_jsonl(path)}
    res = ImportResult()
    new: list[dict] = []
    for i, row in enumerate(rows):
        key = row.get("source_bet_key") if isinstance(row, dict) else None
        try:
            if import_batch_id is not None and isinstance(row, dict) and row.get("import_batch_id") != import_batch_id:
                raise RowRefused("row import_batch_id disagrees with the payload envelope")
            rec = build_wager(row)
        except RowRefused as exc:
            res.refused += 1
            res.rows.append(_receipt(i, key, "wager_id", None, REFUSED, str(exc)))
            continue
        prior = on_file.get(rec["source_bet_key"])
        if prior is not None:
            diff = conflicting_fields(prior, rec, WAGER_CANONICAL_FIELDS)
            if diff:
                res.refused += 1
                res.rows.append(_receipt(i, key, "wager_id", rec["wager_id"], CONFLICT,
                                         "this order is already on the ledger with different economics; "
                                         "an existing row is never rewritten", diff))
            else:
                res.duplicate += 1
                res.rows.append(_receipt(i, key, "wager_id", rec["wager_id"], DUPLICATE_NOOP))
            continue
        on_file[rec["source_bet_key"]] = rec
        new.append(rec)
        res.written += 1
        res.rows.append(_receipt(i, key, "wager_id", rec["wager_id"], NEW))
    _append(path, new)
    return res


# ----------------------------------------------------------------------------------------------------- settlements
def build_settlement(row: Any) -> dict:
    if not isinstance(row, dict):
        raise RowRefused("row is not an object")
    prov = sorted(set(row) & PROVENANCE_FIELDS)
    if prov:
        raise RowRefused(f"model/recommendation provenance field(s) {prov} are not accounting facts")
    unknown = sorted(set(row) - set(SETTLEMENT_INPUT_FIELDS))
    if unknown:
        raise RowRefused(f"unknown field(s) {unknown}")
    missing = [f for f in SETTLEMENT_INPUT_FIELDS if f not in row and f not in ("result", "gross_return", "net_profit_loss")]
    if missing:
        raise RowRefused(f"missing field(s) {missing}")
    rec = {k: row.get(k) for k in SETTLEMENT_INPUT_FIELDS}
    rec["refusals"] = list(rec["refusals"]) if isinstance(rec["refusals"], (list, tuple)) else rec["refusals"]
    rec["settlement_id"] = mint_settlement_id(row.get("source_bet_key"))
    rec["schema_version"] = SETTLEMENT_SCHEMA
    problems = validate_settlement(rec)
    if problems:
        raise RowRefused("; ".join(problems))
    return rec


def import_settlements(base_dir: Path, rows: list) -> ImportResult:
    """Write a settlement only for a wager already on the ledger (else ORPHAN refusal); never rewrite one."""
    wagers = {r.get("source_bet_key"): r for r in read_jsonl(Path(base_dir) / WAGERS_FILE)}
    path = Path(base_dir) / SETTLEMENTS_FILE
    on_file = {r.get("source_bet_key"): r for r in read_jsonl(path)}
    res = ImportResult()
    new: list[dict] = []
    for i, row in enumerate(rows):
        key = row.get("source_bet_key") if isinstance(row, dict) else None
        try:
            rec = build_settlement(row)
            wager = wagers.get(rec["source_bet_key"])
            if wager is None:
                raise RowRefused("ORPHAN: no wager with this source_bet_key is on the NHL wager ledger")
            if wager.get("market_ticker") != rec["market_ticker"] or wager.get("side") != rec["side"]:
                raise RowRefused("settlement market/side disagree with the wager it settles")
        except RowRefused as exc:
            res.refused += 1
            res.rows.append(_receipt(i, key, "settlement_id", None, REFUSED, str(exc)))
            continue
        prior = on_file.get(rec["source_bet_key"])
        if prior is not None:
            diff = conflicting_fields(prior, rec, SETTLEMENT_CANONICAL_FIELDS)
            if diff:
                res.refused += 1
                res.rows.append(_receipt(i, key, "settlement_id", rec["settlement_id"], CONFLICT,
                                         "this wager already has a different settlement; a market settles once "
                                         "and an existing row is never rewritten", diff))
            else:
                res.duplicate += 1
                res.rows.append(_receipt(i, key, "settlement_id", rec["settlement_id"], DUPLICATE_NOOP))
            continue
        on_file[rec["source_bet_key"]] = rec
        new.append(rec)
        res.written += 1
        res.rows.append(_receipt(i, key, "settlement_id", rec["settlement_id"], NEW))
    _append(path, new)
    return res


# ------------------------------------------------------------------------------------------------------ validator
def validate_ledger(base_dir: Path, base_texts: dict[str, str] | None = None) -> dict:
    """Whole-ledger check. Returns counts and failure REASONS only (file + line numbers, never values).

    ``base_texts`` maps the two ledger paths to their content at a base ref; when given, every base line must be
    present, unchanged and in order at the start of the current file (append-only)."""
    failures: list[str] = []
    counts: dict[str, int] = {"wagers": 0, "settlements": 0}
    parsed: dict[str, list[tuple[int, dict]]] = {}
    for label, rel, validator in (("wagers", WAGERS_FILE, validate_wager), ("settlements", SETTLEMENTS_FILE, validate_settlement)):
        path = Path(base_dir) / rel
        rows: list[tuple[int, dict]] = []
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        for i, line in enumerate(text.splitlines(), 1):
            if not line.strip():
                failures.append(f"{rel} line {i}: blank line")
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                failures.append(f"{rel} line {i}: not JSON")
                continue
            if not isinstance(row, dict):
                failures.append(f"{rel} line {i}: not an object")
                continue
            for reason in validator(row):
                failures.append(f"{rel} line {i}: {reason}")
            unknown = sorted(set(row) - set(WAGER_INPUT_FIELDS if label == "wagers" else SETTLEMENT_INPUT_FIELDS)
                             - {"wager_id", "settlement_id", "schema_version"})
            if unknown:
                failures.append(f"{rel} line {i}: unknown field(s) {unknown}")
            rows.append((i, row))
        parsed[label] = rows
        counts[label] = len(rows)
        seen: dict[str, int] = {}
        for i, row in rows:
            k = row.get("source_bet_key")
            if k in seen:
                failures.append(f"{rel} line {i}: duplicate source_bet_key (first at line {seen[k]})")
            else:
                seen[k] = i
        if base_texts is not None:
            base = base_texts.get(str(rel), "")
            base_lines = [x for x in base.splitlines()]
            cur_lines = text.splitlines()
            if len(cur_lines) < len(base_lines) or cur_lines[: len(base_lines)] != base_lines:
                bad = next((n + 1 for n, (a, b) in enumerate(zip(base_lines, cur_lines)) if a != b), min(len(base_lines), len(cur_lines)) + 1)
                failures.append(f"{rel}: not append-only against the base (first difference at line {bad})")
    wagers = {row.get("source_bet_key"): row for _, row in parsed["wagers"]}
    orphans = 0
    for i, row in parsed["settlements"]:
        w = wagers.get(row.get("source_bet_key"))
        if w is None:
            orphans += 1
            failures.append(f"{SETTLEMENTS_FILE} line {i}: orphan settlement (no wager with its source_bet_key)")
        elif w.get("market_ticker") != row.get("market_ticker") or w.get("side") != row.get("side"):
            failures.append(f"{SETTLEMENTS_FILE} line {i}: market/side disagree with its wager")
    counts["orphan_settlements"] = orphans
    return {"passed": not failures, "counts": counts, "failures": failures, "n_failures": len(failures)}
