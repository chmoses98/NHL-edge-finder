"""NHL routed-wager accounting: schema, identity, idempotency, conflicts, orphans, append-only, privacy, isolation."""

import copy
import json
import subprocess
import sys
from pathlib import Path

import pytest

from nhl_edge.accounting import ledger as L

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "scripts" / "accounting"
KEY = "kalshi:0:KXNHLGAME-26OCT01BOSTOR-TOR:order-abc123"
TICKER = "KXNHLGAME-26OCT01BOSTOR-TOR"


def wager_row(**kw) -> dict:
    row = {"source_bet_key": KEY, "import_batch_id": "kalshi-router-v1", "entry_method": "IMPORTED_RECEIPT",
           "game_date": "2026-10-01", "market_ticker": TICKER, "side": "YES", "executed_at": "2026-10-01T22:15:03Z",
           "contracts": 25.0, "execution_price": 0.57, "stake": 14.61, "fees_paid": 0.36, "fees_are_estimated": False,
           "venue": "kalshi"}
    row.update(kw)
    return row


def settlement_row(**kw) -> dict:
    row = {"source_bet_key": KEY, "market_ticker": TICKER, "side": "YES", "settlement_status": "SETTLED",
           "settled_at": "2026-10-02T02:40:00Z", "result": "WON", "gross_return": 25.0, "net_profit_loss": 10.39,
           "refusals": [], "venue": "kalshi", "economics_version": "router-settlement-economics.v2"}
    row.update(kw)
    return row


def ledger_bytes(base: Path) -> tuple[bytes, bytes]:
    w, s = base / L.WAGERS_FILE, base / L.SETTLEMENTS_FILE
    return (w.read_bytes() if w.exists() else b"", s.read_bytes() if s.exists() else b"")


# ------------------------------------------------------------------------------------------------------ wagers
def test_wager_schema_accepts_the_router_row_and_mints_a_deterministic_id(tmp_path):
    rec = L.build_wager(wager_row())
    assert rec["wager_id"] == L.mint_wager_id(KEY) == L.mint_wager_id(KEY)
    assert rec["wager_id"].startswith("nhlw-") and len(rec["wager_id"]) == 5 + 24
    assert rec["schema_version"] == L.WAGER_SCHEMA and L.validate_wager(rec) == []
    assert L.mint_wager_id(KEY + "x") != rec["wager_id"]


@pytest.mark.parametrize("change,needle", [
    ({"source_bet_key": ""}, "source_bet_key"),
    ({"import_batch_id": ""}, "import_batch_id"),
    ({"market_ticker": ""}, "market_ticker"),
    ({"side": "BUY"}, "side"),
    ({"contracts": 0}, "contracts"),
    ({"contracts": -3.0}, "contracts"),
    ({"execution_price": 1.0}, "execution_price"),
    ({"execution_price": 0}, "execution_price"),
    ({"execution_price": "0.5"}, "execution_price"),
    ({"stake": 0}, "stake"),
    ({"stake": 99.0}, "stake does not equal"),
    ({"fees_paid": -0.01}, "fees_paid"),
    ({"fees_are_estimated": True}, "fees_are_estimated"),
    ({"venue": "polymarket"}, "venue"),
    ({"executed_at": "yesterday"}, "executed_at"),
    ({"executed_at": "2026-10-01T22:15:03"}, "executed_at"),
    ({"game_date": "10/01/2026"}, "game_date"),
    ({"entry_method": "MANUAL"}, "entry_method"),
])
def test_wager_validation_refuses_bad_rows(change, needle):
    with pytest.raises(L.RowRefused, match=needle):
        L.build_wager(wager_row(**change))


@pytest.mark.parametrize("field", ["recommendation_id", "model_version", "model_supported", "edge", "p_data_only_v2",
                                   "expected_value", "authority"])
def test_model_provenance_is_refused_even_when_falsy(field):
    with pytest.raises(L.RowRefused, match="provenance"):
        L.build_wager(wager_row(**{field: False}))
    with pytest.raises(L.RowRefused, match="provenance"):
        L.build_settlement(settlement_row(**{field: None}))


def test_unknown_and_missing_fields_are_refused_not_dropped():
    with pytest.raises(L.RowRefused, match="unknown"):
        L.build_wager(wager_row(season=2026))
    row = wager_row()
    del row["fees_paid"]
    with pytest.raises(L.RowRefused, match="missing"):
        L.build_wager(row)


def test_import_then_identical_reimport_is_duplicate_noop_and_byte_identical(tmp_path):
    r1 = L.import_wagers(tmp_path, [wager_row()], import_batch_id="kalshi-router-v1")
    assert [r["status"] for r in r1.rows] == ["NEW"] and r1.written == 1
    before = ledger_bytes(tmp_path)
    r2 = L.import_wagers(tmp_path, [wager_row()], import_batch_id="kalshi-router-v1")
    assert [r["status"] for r in r2.rows] == ["DUPLICATE_NOOP"] and r2.written == 0 and not r2.conflicted
    assert ledger_bytes(tmp_path) == before
    assert r1.rows[0]["wager_id"] == r2.rows[0]["wager_id"] == L.mint_wager_id(KEY)


def test_duplicate_with_different_economics_is_conflict_and_nothing_is_rewritten(tmp_path):
    L.import_wagers(tmp_path, [wager_row()])
    before = ledger_bytes(tmp_path)
    r = L.import_wagers(tmp_path, [wager_row(contracts=26.0, stake=15.18)])
    assert r.rows[0]["status"] == "CONFLICT" and r.rows[0]["success"] is False and r.conflicted
    assert set(r.rows[0]["conflicting_fields"]) == {"contracts", "stake"}
    assert ledger_bytes(tmp_path) == before


def test_conflict_within_one_payload_and_other_rows_still_land(tmp_path):
    other = wager_row(source_bet_key=KEY + "-2")
    r = L.import_wagers(tmp_path, [wager_row(), wager_row(side="NO", execution_price=0.43, stake=11.11), other])
    assert [x["status"] for x in r.rows] == ["NEW", "CONFLICT", "NEW"]
    assert len(L.read_jsonl(tmp_path / L.WAGERS_FILE)) == 2


def test_a_different_import_batch_id_is_not_an_economics_conflict(tmp_path):
    L.import_wagers(tmp_path, [wager_row()])
    r = L.import_wagers(tmp_path, [wager_row(import_batch_id="kalshi-router-backfill-x")])
    assert r.rows[0]["status"] == "DUPLICATE_NOOP"


def test_row_batch_disagreeing_with_envelope_is_refused(tmp_path):
    r = L.import_wagers(tmp_path, [wager_row(import_batch_id="other")], import_batch_id="kalshi-router-v1")
    assert r.rows[0]["status"] == "REFUSED" and not (tmp_path / L.WAGERS_FILE).exists()


# ------------------------------------------------------------------------------------------------- settlements
def test_settlement_import_duplicate_noop_and_deterministic_id(tmp_path):
    L.import_wagers(tmp_path, [wager_row()])
    r1 = L.import_settlements(tmp_path, [settlement_row()])
    assert r1.rows[0]["status"] == "NEW" and r1.rows[0]["settlement_id"] == L.mint_settlement_id(KEY)
    before = ledger_bytes(tmp_path)
    r2 = L.import_settlements(tmp_path, [settlement_row()])
    assert r2.rows[0]["status"] == "DUPLICATE_NOOP" and ledger_bytes(tmp_path) == before


def test_orphan_settlement_is_refused(tmp_path):
    r = L.import_settlements(tmp_path, [settlement_row()])
    assert r.rows[0]["status"] == "REFUSED" and "ORPHAN" in r.rows[0]["reason"] and r.conflicted
    assert not (tmp_path / L.SETTLEMENTS_FILE).exists()


def test_different_settlement_for_a_settled_wager_is_conflict(tmp_path):
    L.import_wagers(tmp_path, [wager_row()])
    L.import_settlements(tmp_path, [settlement_row()])
    before = ledger_bytes(tmp_path)
    r = L.import_settlements(tmp_path, [settlement_row(result="LOST", gross_return=0.0, net_profit_loss=-14.61)])
    assert r.rows[0]["status"] == "CONFLICT" and set(r.rows[0]["conflicting_fields"]) == {"result", "gross_return", "net_profit_loss"}
    assert ledger_bytes(tmp_path) == before


@pytest.mark.parametrize("change,needle", [
    ({"economics_version": "router-settlement-economics.v1"}, "economics_version"),
    ({"settlement_status": "PENDING"}, "settlement_status"),
    ({"result": "PUSH"}, "result"),
    ({"gross_return": None, "net_profit_loss": None, "refusals": []}, "refusals"),
    ({"refusals": ["fee_not_reconciled"]}, "may not also carry refusals"),
    ({"settled_at": "soon"}, "settled_at"),
    ({"import_batch_id": "kalshi-router-v1"}, "unknown"),
])
def test_settlement_validation(change, needle):
    with pytest.raises(L.RowRefused, match=needle):
        L.build_settlement(settlement_row(**change))


def test_unestablished_money_with_a_reason_is_a_valid_settlement(tmp_path):
    L.import_wagers(tmp_path, [wager_row()])
    r = L.import_settlements(tmp_path, [settlement_row(gross_return=None, net_profit_loss=None, refusals=["fee_not_reconciled"])])
    assert r.rows[0]["status"] == "NEW"


def test_settlement_must_match_its_wager_side_and_ticker(tmp_path):
    L.import_wagers(tmp_path, [wager_row()])
    r = L.import_settlements(tmp_path, [settlement_row(side="NO")])
    assert r.rows[0]["status"] == "REFUSED"


# ------------------------------------------------------------------------------------------------- validator
def _git(cwd, *args):
    subprocess.run(["git", "-C", str(cwd), *args], check=True, capture_output=True)


def test_validator_passes_a_clean_ledger_and_is_append_only_against_base(tmp_path):
    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "t@t")
    _git(tmp_path, "config", "user.name", "t")
    L.import_wagers(tmp_path, [wager_row()])
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-qm", "base")
    L.import_settlements(tmp_path, [settlement_row()])
    L.import_wagers(tmp_path, [wager_row(source_bet_key=KEY + "-2")])
    rc = subprocess.run([sys.executable, str(SCRIPTS / "validate_routed_ledger.py"), "--base-dir", str(tmp_path), "--against", "HEAD"],
                        capture_output=True, text=True)
    assert rc.returncode == 0, rc.stdout
    # rewrite line 1 in place: not append-only
    p = tmp_path / L.WAGERS_FILE
    lines = p.read_text().splitlines()
    first = json.loads(lines[0])
    first["stake"] = 14.6100001
    lines[0] = json.dumps(first, sort_keys=True, separators=(",", ":"))
    p.write_text("\n".join(lines) + "\n")
    rc = subprocess.run([sys.executable, str(SCRIPTS / "validate_routed_ledger.py"), "--base-dir", str(tmp_path), "--against", "HEAD"],
                        capture_output=True, text=True)
    assert rc.returncode == 1 and "not append-only" in rc.stdout


def test_validator_catches_duplicates_orphans_provenance_and_bad_json(tmp_path):
    L.import_wagers(tmp_path, [wager_row()])
    w = tmp_path / L.WAGERS_FILE
    row = json.loads(w.read_text().splitlines()[0])
    bad = copy.deepcopy(row)
    bad["model_supported"] = False
    with w.open("a") as fh:
        fh.write(json.dumps(row) + "\n")  # duplicate key
        fh.write(json.dumps(bad) + "\n")
        fh.write("{not json\n")
    s = tmp_path / L.SETTLEMENTS_FILE
    s.parent.mkdir(parents=True, exist_ok=True)
    orphan = L.build_settlement(settlement_row(source_bet_key="nobody", market_ticker=TICKER))
    s.write_text(json.dumps(orphan) + "\n")
    res = L.validate_ledger(tmp_path)
    text = "\n".join(res["failures"])
    assert not res["passed"]
    assert "duplicate source_bet_key" in text and "provenance" in text and "not JSON" in text and "orphan settlement" in text
    assert res["counts"]["orphan_settlements"] == 1


def test_empty_ledger_is_valid(tmp_path):
    assert L.validate_ledger(tmp_path)["passed"]


# ------------------------------------------------------------------------------------------------- CLIs + privacy
def test_cli_round_trip_receipts_and_no_economics_in_stdout(tmp_path):
    payload = tmp_path / "NHL.json"
    payload.write_text(json.dumps({"importBatchId": "kalshi-router-v1", "rows": [wager_row()]}))
    spay = tmp_path / "NHL-settlements.json"
    spay.write_text(json.dumps({"settlements": [settlement_row()]}))
    base = tmp_path / "ledger"
    base.mkdir()
    outs = []
    for script, pay, rec in (("import_routed_wagers.py", payload, "w1.json"), ("import_routed_wagers.py", payload, "w2.json"),
                             ("import_routed_settlements.py", spay, "s1.json"), ("import_routed_settlements.py", spay, "s2.json")):
        p = subprocess.run([sys.executable, str(SCRIPTS / script), "--payload", str(pay), "--base-dir", str(base),
                            "--receipts-out", str(tmp_path / rec)], capture_output=True, text=True)
        assert p.returncode == 0, p.stdout + p.stderr
        outs.append(p.stdout + p.stderr)
    v = subprocess.run([sys.executable, str(SCRIPTS / "validate_routed_ledger.py"), "--base-dir", str(base)], capture_output=True, text=True)
    assert v.returncode == 0
    outs.append(v.stdout + v.stderr)
    blob = "\n".join(outs)
    for secret in (TICKER, KEY, "14.61", "0.57", "25.0", "10.39", "0.36"):
        assert secret not in blob, f"{secret!r} leaked into a public log"
    w1, w2 = (json.loads((tmp_path / f).read_text()) for f in ("w1.json", "w2.json"))
    s1, s2 = (json.loads((tmp_path / f).read_text()) for f in ("s1.json", "s2.json"))
    assert [r["status"] for r in w1["rows"]] == ["NEW"] and [r["status"] for r in w2["rows"]] == ["DUPLICATE_NOOP"]
    assert [r["status"] for r in s1["rows"]] == ["NEW"] and [r["status"] for r in s2["rows"]] == ["DUPLICATE_NOOP"]
    assert w1["rows"][0]["wager_id"] == w2["rows"][0]["wager_id"] and w1["rows"][0]["source_bet_key"] == KEY


def test_cli_conflict_exits_nonzero_and_names_fields_not_values(tmp_path):
    base = tmp_path / "ledger"
    base.mkdir()
    L.import_wagers(base, [wager_row()])
    payload = tmp_path / "NHL.json"
    payload.write_text(json.dumps({"importBatchId": "kalshi-router-v1", "rows": [wager_row(contracts=26.0, stake=15.18)]}))
    p = subprocess.run([sys.executable, str(SCRIPTS / "import_routed_wagers.py"), "--payload", str(payload), "--base-dir", str(base)],
                       capture_output=True, text=True)
    assert p.returncode == 1 and "CONFLICT" in p.stdout and "contracts" in p.stdout
    assert "26.0" not in p.stdout and "15.18" not in p.stdout


def test_router_receipts_normalise_shape():
    """The receipt rows expose exactly what kalshi_router.receipts.normalise reads."""
    res = L.ImportResult()
    res.rows.append(L._receipt(0, KEY, "wager_id", "nhlw-x", "NEW"))
    r = res.receipts("wagers")["rows"][0]
    assert {"source_bet_key", "wager_id", "duplicate_status", "status", "success"} <= set(r)


# ------------------------------------------------------------------------------------------------- isolation
def test_accounting_imports_no_model_code():
    code = ("import sys; import nhl_edge.accounting.ledger; "
            "bad=[m for m in sys.modules if m.startswith('nhl_edge.') and not m.startswith('nhl_edge.accounting')]; "
            "print(bad); raise SystemExit(1 if bad else 0)")
    p = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, cwd=REPO)
    assert p.returncode == 0, p.stdout


def test_model_authority_is_untouched():
    import nhl_edge

    assert nhl_edge.AUTHORITY == "RESEARCH_ONLY"
    assert (nhl_edge.DATA_ONLY_MODEL_VERSION, nhl_edge.DATA_ONLY_V2_MODEL_VERSION) == ("DATA_ONLY_V1", "DATA_ONLY_V2")
    src = (REPO / "src" / "nhl_edge" / "accounting" / "ledger.py").read_text()
    for forbidden in ("httpx", "post(", "orders", "KalshiClient"):
        assert forbidden not in src
