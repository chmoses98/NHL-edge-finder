"""Edge Finder app export (edge_finder.app.v1): contract intact, end-to-end on a synthetic archive built from the
repository's own record shapes, determinism, failure safety, stale health, naive-timestamp refusal, routed-wager
cross references, no secrets, and a real-data smoke test when the data-archive branch is checked out."""

from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import timedelta
from pathlib import Path

import pytest
from edge_finder_contract import publish, sync, timeutil

from nhl_edge import app_export
from nhl_edge.accounting import ledger as acct
from nhl_edge.archive.ledger import Ledger
from nhl_edge.config import REPO_ROOT
from tests.archive_fixture import NOW, build_archive

GAME = "2026020001"  # FLA @ CAR, opening night 2026-09-29 (real schedule sample; real sample markets re-labelled onto it)
TICKER_YES = "KXNHLGAME-26SEP29FLACAR-FLA"
TICKER_NO = "KXNHLGAME-26SEP29FLACAR-CAR"
TICKER_TOTAL = "KXNHLTOTAL-26SEP29FLACAR-6"
TICKER_GONE = "KXNHLGAME-26SEP28BUFOTT-OTT"  # a settled wager whose market left the board -> stub
KEY_LINKED = "kalshi:0:KXNHLGAME-26SEP29FLACAR-FLA:order-abc123"
KEY_GONE = "kalshi:0:KXNHLGAME-26SEP28BUFOTT-OTT:order-def456"
EXPORT_NOW = NOW + timedelta(minutes=12)


def _iso(dt) -> str:
    return dt.isoformat().replace("+00:00", "Z")


def _slate_contract(ticker: str, p: float | None, gate: str, *, family: str = "game_winner", bid: int = 53, ask: int = 54) -> dict:
    """The exact shape ``slates/latest/slate.json`` ``contracts[]`` rows have in production (2026-10-02)."""
    return {
        "prediction_id": hashlib.sha256(ticker.encode()).hexdigest()[:32], "ticker": ticker, "game_id": GAME, "family": family,
        "predicted_at_utc": _iso(NOW - timedelta(minutes=10)) .replace("Z", ".965127Z"), "data_cutoff_utc": _iso(NOW - timedelta(minutes=10)),
        "model_version": "DATA_ONLY_V1", "sim_version": "nhl-sim-1.1", "feature_version": "nhl-features-1.0", "n_sims": 20000, "seed": 1,
        "p_data_only": p, "p_market": (bid + ask) / 200.0, "p_market_anchored": None if p is None else round(0.8 * (bid + ask) / 200.0 + 0.2 * p, 6),
        "p_data_only_se": None if p is None else 0.0035, "market_observed_at_utc": _iso(NOW - timedelta(minutes=5)),
        "market_yes_bid": bid, "market_yes_ask": ask, "market_no_bid": 100 - ask, "market_no_ask": 100 - bid,
        "executable_p_yes": ask / 100.0, "executable_p_no": (100 - bid) / 100.0,
        "edge_yes_raw": None if p is None else round(p - ask / 100.0, 6), "edge_yes_after_fee": None if p is None else round(p - ask / 100.0 - 0.007, 6),
        "edge_no_raw": None, "edge_no_after_fee": None, "gate": gate, "gate_reasons": [] if gate == "OK" else [gate.lower()],
        "authority": "RESEARCH_ONLY", "support": "MODELABLE" if p is not None else "RESEARCH", "pregame": True, "minutes_to_start": 350.0,
        "horizon_label": "T-3h", "home_goalie_status": "PROBABLE", "away_goalie_status": "PROJECTED", "best_side": "yes" if gate == "OK" else None,
        "title": f"YES on {ticker}", "stat": "winner", "period": "FULL", "threshold": 0.0, "comparator": "gt", "team_id": 13,
    }


def _card_entry() -> dict:
    """One ``thesis_card.games[].card[]`` entry, field for field as the production packet writes it."""
    return {
        "bet_id": f"{TICKER_YES}|yes", "game_id": GAME,
        "contract": {"ticker": TICKER_YES, "title": "Florida wins", "side": "YES", "family": "game_winner"},
        "team_opponent": {"team": "FLA", "opponent": "CAR", "matchup": "FLA @ CAR"},
        "executable_price": {"ask_cents": 57, "fee_per_contract": 0.0098, "cost_per_contract": 0.5798, "observed_at_utc": _iso(NOW - timedelta(minutes=5))},
        "fair_probability": {"p_model_joint_draw": 0.61, "p_confidence_adjusted": 0.6, "confidence_k": 0.75, "confidence_notes": [],
                             "projection": {"projection_quality": "STANDARD", "uncertainty_flags": ["NO_CURRENT_SEASON_GAMES"],
                                            "role_confidence": "MEDIUM", "deployment_source": "LINES_PROJECTED"},
                             "p_kalshi_mid": 0.555, "p_v1": 0.6, "p_sportsbook": None},
        "estimated_edge": {"ev_raw_per_contract": 0.0302, "ev_adjusted_per_contract": 0.0202, "roi_adjusted": 0.0348, "growth_bp": 3.1},
        "bet_up_to_price": {"cents_raw": 60, "cents_adjusted": 59},
        "recommended_stake": {"dollars": 12.5, "fraction_of_bankroll": 0.0125, "contracts": 21.6, "nominal_bankroll": 1000.0,
                              "authority": "RESEARCH_ONLY (suggestion; never placed or routed)"},
        "family_reliability": {"label": "EVIDENCE_STRONGER", "family_label": "EVIDENCE_STRONGER", "family_evidence": "held-out n 1200, ECE 0.01",
                               "flags": ["SMALL_PROSPECTIVE_SAMPLE"], "bucket_calibration": {"bucket": "55-65%", "n": 300, "gap": 0.01},
                               "benchmark_category": "D", "benchmark_meaning": "no external benchmark available"},
        "primary_thesis": {"key": "FLA:WINS", "label": "FLA wins (incl. OT/SO)", "category": "result", "phi": 1.0, "p_thesis": 0.61,
                           "p_bet_given_thesis": 1.0, "p_thesis_given_bet": 1.0, "p_bet_given_not_thesis": 0.0},
        "secondary_thesis": {"key": "FLA:SHOT_CONTROL", "label": "FLA controls shots (share >= 0.55)", "category": "control", "phi": 0.3,
                             "p_thesis": 0.4, "p_bet_given_thesis": 0.8, "p_thesis_given_bet": 0.52, "p_bet_given_not_thesis": 0.48},
        "best_alternative": {"bet_id": f"{TICKER_TOTAL}|yes", "title": "Over 5.5 goals", "price_cents": 50, "p_model": 0.52, "p_adjusted": 0.5,
                             "ev_raw": 0.02, "ev_adjusted": 0.0, "growth_bp": 0.0, "thesis_fit_phi": 0.1, "reliability": "EVIDENCE_THIN",
                             "breadth_rel": 0.7, "eligible": False, "reasons": ["confidence-adjusted EV <= 0"]},
        "reason_chosen": "higher confidence-adjusted growth (3.10 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN",
        "failure_case": {"p_lose": 0.39, "failure_thesis": {"key": "CAR:WINS", "label": "CAR wins (incl. OT/SO)", "category": "result", "phi": -1.0},
                         "worst_major_script": {"script": "CAR shot control · low event (<=4) · tight (1-goal/OT)", "p_win_in_script": 0.3, "script_frequency": 0.05},
                         "scripts_needed": ["balanced shots · normal event (5-7) · decided (2+)"],
                         "note": "conditional on the goalie starting; loses 39% of simulated games"},
        "thesis_concentration": {"top1": 0.2, "top2": 0.35, "breadth_eff": 9.0, "breadth_rel": 0.8,
                                 "main_scripts": [{"script": "balanced shots · normal event (5-7) · decided (2+)", "key": "CB|EN|MD", "contribution_pp": 2.0,
                                                   "share": 0.2, "p_win_in_script": 0.7, "script_frequency": 0.11}]},
        "same_game_relationships": [], "same_game_exposure": {"dollars": 12.5}, "thesis_exposure": {"dollars": 12.5},
        "portfolio_impact": {"marginal_expected_profit": 0.4, "marginal_log_growth_bp": 3.0, "delta_p_profit": 0.01, "delta_p10": 1.0},
    }


def _wager_row(key: str, ticker: str, executed_at: str, **kw) -> dict:
    """Exactly what the router delivers (``tests/test_accounting.py`` shape); ids minted by the ledger's own code."""
    row = {"source_bet_key": key, "import_batch_id": "kalshi-router-v1", "entry_method": "IMPORTED_RECEIPT", "game_date": "2026-09-29",
           "market_ticker": ticker, "side": "YES", "executed_at": executed_at, "contracts": 25.0, "execution_price": 0.57, "stake": 14.61,
           "fees_paid": 0.36, "fees_are_estimated": False, "venue": "kalshi"}
    row.update(kw)
    return acct.build_wager(row)


def _settlement_row(key: str, ticker: str, **kw) -> dict:
    row = {"source_bet_key": key, "market_ticker": ticker, "side": "YES", "settlement_status": "SETTLED", "settled_at": _iso(NOW - timedelta(hours=20)),
           "result": "WON", "gross_return": 25.0, "net_profit_loss": 10.39, "refusals": [], "venue": "kalshi",
           "economics_version": "router-settlement-economics.v2"}
    row.update(kw)
    return acct.build_settlement(row)


def make_root(tmp_path: Path, *, with_accounting: bool = True) -> tuple[Path, Path | None]:
    """A synthetic archive: the real probe schedule + real sample markets (``tests/archive_fixture``), the STATUS/LEASE
    breadcrumbs, a slate + packet in the production shape, and a routed-wager ledger written by the ledger's own code."""
    root = tmp_path / "archive"
    build_archive(root, now=NOW)
    sim_at = _iso(NOW - timedelta(minutes=10))
    (root / "STATUS_capture.json").write_text(json.dumps({"last_capture_utc": _iso(NOW - timedelta(minutes=5)), "n_markets": 38, "run_id": "test-run", "alarms": []}))
    (root / "STATUS_simulate.json").write_text(json.dumps({"simulated_at_utc": sim_at, "date_et": "2026-09-29", "n_games": 5, "n_contracts": 3,
                                                           "out_dir": "slates/dt=2026-09-29/20260929T145000Z_test-run", "run_id": "test-run",
                                                           "by_gate": {"OK": 1, "NO_EDGE": 1, "UNSUPPORTED": 1}}))
    (root / "STATUS_context.json").write_text(json.dumps({"refreshed_at_utc": _iso(NOW - timedelta(minutes=20)), "date_et": "2026-09-29", "run_id": "test-run"}))
    (root / "LEASE_capture.json").write_text(json.dumps({"worker_id": "test-run", "heartbeat_at": _iso(NOW - timedelta(minutes=5)),
                                                         "expected_next_capture_at": _iso(NOW + timedelta(minutes=10)), "generation": 1}))
    contracts = [_slate_contract(TICKER_YES, 0.61, "OK", bid=56, ask=57), _slate_contract(TICKER_NO, 0.39, "NO_EDGE", bid=43, ask=44),
                 _slate_contract(TICKER_TOTAL, None, "UNSUPPORTED", family="game_total", bid=49, ask=51)]
    card = _card_entry()
    thesis_card = {"thesis_version": "nhl-thesis-1.0", "card_version": "nhl-card-1.0", "portfolio_version": "nhl-portfolio-1.0", "authority": "RESEARCH_ONLY",
                   "status": "COMPLETE", "card_emitted": True, "gate": {"status": "PASS"}, "portfolio_config": {"bankroll": 1000.0, "kelly_multiplier": 0.25},
                   "recommended_portfolio": "B", "generated_at_utc": sim_at, "run_id": "test-run",
                   "recommended": [{"bet_id": card["bet_id"], "title": "Florida wins", "side": "YES", "stake": 12.5, "p": 0.61, "p_adj": 0.6, "ask": 57,
                                    "primary_thesis": "FLA:WINS"}]}
    slate = {"sport": "NHL", "generated_at_utc": sim_at, "date_et": "2026-09-29", "authority": "RESEARCH_ONLY", "run_id": "test-run",
             "model_version": "DATA_ONLY_V1", "market_anchored_model_version": "MARKET_ANCHORED_V1", "sim_version": "nhl-sim-1.1",
             "feature_version": "nhl-features-1.0", "n_sims": 20000,
             "games": [{"game_id": GAME, "date_et": "2026-09-29", "start_time_utc": "2026-09-29T21:00:00Z", "home": "CAR", "away": "FLA", "home_team_id": 12,
                        "away_team_id": 13, "p_home_win": 0.39, "p_away_win": 0.61, "p_overtime": 0.2, "exp_total": 5.9, "inputs_trusted": True, "input_reasons": []}],
             "contracts": contracts, "thesis_card": thesis_card}
    packet = {"slate": {k: v for k, v in slate.items() if k not in ("contracts", "games")},
              "games": [{"identity": {"game_id": GAME, "sport": "NHL", "league": "NHL", "event_id": GAME, "season": "2026-27", "season_type": "regular",
                                      "date_et": "2026-09-29", "start_time_utc": "2026-09-29T21:00:00Z", "home": "CAR", "away": "FLA",
                                      "home_team_id": 12, "away_team_id": 13, "venue": "Lenovo Center"},
                         "context": {"home_rest_days": 170, "away_rest_days": 170, "home_b2b": False, "away_b2b": False,
                                     "injuries": [{"team_name": "Florida Panthers", "team_id": 13, "player_name": "Matthew Tkachuk", "position": "LW",
                                                   "status": "Out", "type": "out", "detail": "Groin", "return_date": None}]},
                         "goaltending": {"home": {"team_id": 12, "status": "PROJECTED", "player_id": 8480382, "player_name": "Frederik Andersen", "confidence": 0.7},
                                         "away": {"team_id": 13, "status": "CONFIRMED", "player_id": 8475683, "player_name": "Sergei Bobrovsky", "confidence": 0.985}},
                         "authority": "RESEARCH_ONLY"}],
              "player_shadow": {"contracts": []},
              "thesis_card": thesis_card | {"games": [{"game_id": GAME, "matchup": "FLA @ CAR", "meta": {"source": "PLAYER_SIM_V1 joint draw"},
                                                       "scripts": [{"name": "balanced shots · normal event (5-7) · decided (2+)", "frequency": 0.11, "major": True},
                                                                   {"name": "CAR shot control · low event (<=4) · tight (1-goal/OT)", "frequency": 0.05, "major": False}],
                                                       "thesis_events": [{"key": "FLA:WINS", "label": "FLA wins (incl. OT/SO)", "category": "result", "p": 0.61}],
                                                       "card": [card]}]}}
    latest = root / "slates" / "latest"
    latest.mkdir(parents=True)
    (latest / "slate.json").write_text(json.dumps(slate, indent=1))
    (latest / "packet.json").write_text(json.dumps(packet, indent=1))
    acc = None
    if with_accounting:
        acc = tmp_path / "accounting-data" / "data" / "accounting"
        acc.mkdir(parents=True)
        wagers = [_wager_row(KEY_LINKED, TICKER_YES, _iso(NOW - timedelta(minutes=2))),
                  _wager_row(KEY_GONE, TICKER_GONE, _iso(NOW - timedelta(hours=26)), game_date="2026-09-28")]
        (acc / "wagers.jsonl").write_text("".join(json.dumps(w, sort_keys=True) + "\n" for w in wagers))
        (acc / "settlements.jsonl").write_text(json.dumps(_settlement_row(KEY_GONE, TICKER_GONE), sort_keys=True) + "\n")
        acc = tmp_path / "accounting-data"
    return root, acc


def _export(root: Path, out: Path, acc: Path | None, now=EXPORT_NOW, **kw) -> dict:
    return app_export.export(root, out, accounting_dir=acc, now=now, commit_sha="abc1234", workflow_run_id="1", **kw)


def _load(out: Path, name: str) -> dict:
    return json.loads((out / f"{name}.json").read_text())


def _tree(out: Path) -> dict[str, str]:
    return {str(p.relative_to(out)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.rglob("*.json"))}


# ------------------------------------------------------------------------------------------------- 1. contract
def test_vendored_contract_is_intact():
    assert sync.check() == []


# --------------------------------------------------------------------------------------------- 2. end to end
def test_export_end_to_end_on_a_synthetic_archive(tmp_path):
    root, acc = make_root(tmp_path)
    out = tmp_path / "app"
    res = _export(root, out, acc)
    assert res["ok"], res.get("error")
    assert publish.verify_published(out) == []
    counts = res["counts"]
    events, markets = _load(out, "events")["items"], _load(out, "markets")["items"]
    assert counts["events"] == 5 and len(events) == 5  # the five opening-night games of 2026-09-29
    by_game = {e["source_ids"]["nhl_game_id"]: e for e in events}
    ev = by_game[GAME]
    assert ev["status"] == "SCHEDULED" and ev["start_time_confidence"] == "SCHEDULED" and ev["league"] == "NHL" and ev["season"] == "2026-27"
    assert {p["short_name"] for p in ev["participants"]} == {"FLA", "CAR"}
    assert ev["home_participant"] != ev["away_participant"] and ev["source_ids"]["kalshi_event_ticker"] == "KXNHLGAME-26SEP29FLACAR"
    joined = [m for m in markets if m["event_id"] == ev["event_id"]]
    assert len(joined) == 14 and all(m["source"] == "kalshi" and m["market_status"] == "OPEN" for m in joined)
    winner = next(m for m in joined if m["kalshi_ticker"] == TICKER_YES)
    assert winner["market_family"] == "game_winner" and winner["side"] == "AWAY" and winner["yes_bid"] == 0.1 and winner["yes_ask"] == 0.57
    assert winner["participant_id"] and winner["extensions"]["nhl_game_id"] == GAME and winner["extensions"]["support"] == "MODELABLE"
    assert all(len(json.dumps(m["extensions"])) < 600 for m in markets), "markets carry compact extensions, not raw Kalshi blobs"
    # one model price per priced slate row of the PRODUCTION model; the UNSUPPORTED row (p_data_only null) is counted, not invented
    prices = _load(out, "model_prices")["items"]
    assert counts["model_prices"] == 2 == len(prices) and counts["slate_unpriced_skipped"] == 1
    yes = next(p for p in prices if p["market_id"] == f"mkt_kalshi_{TICKER_YES}")
    assert yes["fair_probability"] == 0.61 and yes["uncertainty"] == 0.0035 and yes["model_version"] == "DATA_ONLY_V1"
    assert yes["data_quality_status"] == "OK" and yes["support_status"] == "OK" and yes["extensions"]["p_market_anchored"] is not None
    assert next(p for p in prices if p["market_id"] == f"mkt_kalshi_{TICKER_NO}")["data_quality_status"] == "OK"  # NO_EDGE -> OK
    assert yes["edge"] == round(0.61 - 0.565, 6) and yes["inputs_as_of"] == _iso(NOW - timedelta(minutes=5))
    # recommendations: RESEARCH_CANDIDATE / RESEARCH_ONLY, selection-side prices, the card's own stake and bankroll
    recs = _load(out, "recommendations")["items"]
    assert counts["recommendations"] == 1 and len(recs) == 1
    r = recs[0]
    assert r["status"] == "RESEARCH_CANDIDATE" and r["authority"] == "RESEARCH_ONLY" and r["research_only"] is True
    assert r["selection"] == "YES" and r["current_price"] == 0.57 and r["fair_probability"] == 0.6 and r["edge"] == 0.0202
    assert r["stake_dollars"] == 12.5 and r["bankroll_basis"] == 1000.0 and r["bet_up_to_price"] == 0.59 and r["event_id"] == ev["event_id"]
    assert r["source_ids"]["bet_id"] == f"{TICKER_YES}|yes" and r["created_at"] == _iso(NOW - timedelta(minutes=10))
    theses = {t["thesis_id"]: t for t in _load(out, "theses")["items"]}
    assert r["thesis_id"] in theses and counts["theses"] == 2  # one per recommendation + one per slate game with a card
    th = theses[r["thesis_id"]]
    assert th["summary"] == "FLA wins (incl. OT/SO)" and th["opposing_factors"][0] == "CAR wins (incl. OT/SO)"
    assert th["supporting_factors"][0].startswith("higher confidence-adjusted growth") and th["confidence_label"] == "EVIDENCE_STRONGER"
    game_thesis = next(t for t in theses.values() if t["thesis_id"] != r["thesis_id"])
    assert game_thesis["summary"] is None and game_thesis["primary_game_script"].startswith("balanced shots")
    assert "Matthew Tkachuk (Out: Groin)" in game_thesis["context_notes"]["injuries"]
    # board + detail + run + health
    board = _load(out, "board")
    assert board["bet_authority"] == "RESEARCH_ONLY" and board["overall_status"] == "RESEARCH_ONLY"
    row = next(b for b in board["items"] if b["event_id"] == ev["event_id"])
    assert row["markets_available"] == 14 and row["markets_priced"] == 2 and row["recommendations_count"] == 1 and row["wagers_count"] == 1
    assert row["data_freshness"] == "FRESH" and row["health_flags"] == []
    detail = json.loads((out / row["detail_path"]).read_text())
    assert len(detail["markets"]) == 14 and len(detail["recommendations"]) == 1 and len(detail["theses"]) == 2 and len(detail["wagers"]) == 1
    assert detail["context"]["goaltending"]["away"]["player_name"] == "Sergei Bobrovsky" and detail["context"]["authority"] == "RESEARCH_ONLY"
    assert {p.name for p in out.glob("*.json")} == {"manifest.json", "events.json", "markets.json", "model_prices.json", "recommendations.json", "theses.json",
                                                    "wagers.json", "settlements.json", "runs.json", "board.json", "performance.json", "health.json"}
    assert len(list((out / "event_detail").glob("*.json"))) == 5
    run = _load(out, "runs")["items"][0]
    assert run["status"] == "SUCCESS" and run["native_run_id" if "native_run_id" in run else "source_ids"]["native_run_id"].startswith("test-run:")
    assert run["model_version"] == "DATA_ONLY_V1" and run["commit_sha"] == "abc1234" and run["markets_priced"] == 2 and run["events_processed"] == 5
    health = _load(out, "health")
    assert health["overall_status"] == "RESEARCH_ONLY" and health["bet_authority"] == "RESEARCH_ONLY" and health["export_failed" if "export_failed" in health else "overall_status"]
    assert health["thresholds"]["market_data"] == {"fresh_after_seconds": 1200, "stale_after_seconds": 3600}
    assert health["next_scheduled_run"] == _iso(NOW + timedelta(minutes=10)) and health["payload_run_id"] == run["run_id"]
    manifest = _load(out, "manifest")
    assert manifest["source_repo"] == "chmoses98/NHL-edge-finder" and manifest["source_branch"] == "data-archive"
    assert manifest["freshness"]["kalshi"]["status"] == "FRESH" and manifest["freshness"]["model"]["status"] == "FRESH"


# ---------------------------------------------------------------------------------- 9. wagers <-> settlements
def test_routed_wagers_settlements_and_pnl_match_the_ledger(tmp_path):
    root, acc = make_root(tmp_path)
    out = tmp_path / "app"
    assert _export(root, out, acc)["ok"]
    wagers = {w["source_bet_key"]: w for w in _load(out, "wagers")["items"]}
    settlements = {s["settlement_id"]: s for s in _load(out, "settlements")["items"]}
    markets = {m["market_id"]: m for m in _load(out, "markets")["items"]}
    assert set(wagers) == {KEY_LINKED, KEY_GONE} and len(settlements) == 1
    linked, gone = wagers[KEY_LINKED], wagers[KEY_GONE]
    assert all(w["source"] == "KALSHI_ROUTER" and w["destination_repo"] == "chmoses98/NHL-edge-finder" and w["market_id"] in markets for w in wagers.values())
    assert linked["source_ids"]["wager_id"].startswith("nhlw-") and linked["side"] == "BUY" and linked["fees"] == 0.36 and linked["stake"] == 14.61
    # temporal linkage: the recommendation (T-10m) and model price predate the wager (T-2m), so both link; never by hand
    recs = _load(out, "recommendations")["items"]
    assert linked["recommendation_id"] == recs[0]["recommendation_id"] and linked["model_price_id"] and linked["event_id"]
    assert linked["linkage"]["recommendation_generated_at"] == recs[0]["created_at"] and linked["settlement_status"] == "PENDING"
    # the settled wager's market left the board: a stub keeps the reference intact
    stub = markets[gone["market_id"]]
    assert stub["source"] == "accounting_ledger" and stub["market_status"] == "SETTLED" and stub["yes_bid"] is None
    assert gone["settlement_status"] == "SETTLED" and gone["settlement_id"] in settlements and gone["recommendation_id"] is None
    st = settlements[gone["settlement_id"]]
    assert st["wager_id"] == gone["wager_id"] and st["market_id"] == gone["market_id"] and st["result"] == "WON" and st["winning_side"] == "YES"
    assert st["verification_status"] == "EXCHANGE_CONFIRMED" and st["net_pnl"] == 10.39 and st["gross_payout"] == 25.0
    assert gone["payout"] == 25.0 and gone["profit_loss"] == 10.39
    ledger_rows = acct.read_jsonl(acc / "data" / "accounting" / "settlements.jsonl")
    wager_rows = acct.read_jsonl(acc / "data" / "accounting" / "wagers.jsonl")
    perf = _load(out, "performance")
    assert perf["totals"]["wagers"] == 2 and perf["totals"]["settled"] == 1 and perf["totals"]["pending"] == 1
    assert perf["totals"]["net_pnl"] == round(sum(r["net_profit_loss"] for r in ledger_rows), 4)
    assert perf["totals"]["stake"] == round(sum(r["stake"] for r in wager_rows), 4)
    assert perf["totals"]["open_exposure"] == 14.61 and perf["recommended_vs_wagered"]["wagers_linked_to_recommendation"] == 1


def test_an_empty_or_absent_ledger_is_a_valid_state(tmp_path):
    """The committed accounting-data ledger is currently empty; the export must publish zero wagers, not fail."""
    root, _ = make_root(tmp_path, with_accounting=False)
    out = tmp_path / "app"
    res = _export(root, out, None)
    assert res["ok"] and res["counts"]["wagers"] == 0 and res["counts"]["settlements"] == 0 and publish.verify_published(out) == []
    assert any("accounting" in w for w in res["warnings"])
    empty = tmp_path / "empty-ledger"
    empty.mkdir()
    (empty / "wagers.jsonl").write_text("")
    (empty / "settlements.jsonl").write_text("")
    res = _export(root, out, empty)
    assert res["ok"] and res["counts"]["wagers"] == 0 and _load(out, "performance")["totals"]["wagers"] == 0


# ------------------------------------------------------------------------------------------- 3. determinism
def test_two_runs_on_the_same_inputs_are_byte_identical(tmp_path):
    root, acc = make_root(tmp_path)
    a, b = tmp_path / "a", tmp_path / "b"
    assert _export(root, a, acc)["ok"] and _export(root, b, acc)["ok"]
    assert _tree(a) == _tree(b)
    ma, mb = _load(a, "manifest"), _load(b, "manifest")
    assert {k: v["sha256"] for k, v in ma["files"].items()} == {k: v["sha256"] for k, v in mb["files"].items()} and ma["run_id"] == mb["run_id"]


# ---------------------------------------------------------------------------------------- 4. failure safety
def test_a_failed_build_rewrites_only_health_and_keeps_the_payload(tmp_path):
    root, acc = make_root(tmp_path)
    out = tmp_path / "app"
    assert _export(root, out, acc)["ok"]
    before = _tree(out)
    good_run = _load(out, "manifest")["run_id"]
    (root / "slates" / "latest" / "slate.json").write_text("{not json")
    res = _export(root, out, acc, now=EXPORT_NOW + timedelta(minutes=5))
    assert res["ok"] is False and "slate.json" in res["error"]
    after = _tree(out)
    assert {k: v for k, v in after.items() if k != "health.json"} == {k: v for k, v in before.items() if k != "health.json"}
    assert after["health.json"] != before["health.json"]
    health = _load(out, "health")
    assert health["overall_status"] == "DEGRADED" and health["payload_run_id"] == good_run and health["errors"]
    assert health["components"]["export"]["status"] == "DEGRADED" and "last-known-good" in health["components"]["export"]["detail"]
    assert publish.verify_published(out) == [], "the last-known-good payload is still a consistent publication"
    # nothing published yet + failure -> UNAVAILABLE, and exit code 1 through the CLI
    fresh = tmp_path / "fresh"
    rc = app_export.main(["--data-root", str(root), "--out", str(fresh), "--now", _iso(EXPORT_NOW)])
    assert rc == 1 and _load(fresh, "health")["overall_status"] == "UNAVAILABLE" and not (fresh / "manifest.json").exists()


# --------------------------------------------------------------------------------------------- 5. stale data
def test_stale_inputs_make_health_stale(tmp_path):
    root, acc = make_root(tmp_path)
    out = tmp_path / "app"
    res = _export(root, out, acc, now=NOW + timedelta(days=3))
    assert res["ok"]
    health = _load(out, "health")
    assert health["overall_status"] == "STALE" and health["market_data_status"] == "STALE" and health["model_status"] == "STALE"
    assert health["freshness_status"] == "STALE" and _load(out, "board")["items"][0]["data_freshness"] == "STALE"
    assert "STALE_DATA" in _load(out, "board")["items"][0]["health_flags"]


# ------------------------------------------------------------------------------------- 6. naive timestamps
def test_a_naive_timestamp_in_the_inputs_is_refused_and_nothing_naive_is_emitted(tmp_path):
    root, acc = make_root(tmp_path)
    out = tmp_path / "app"
    slate_path = root / "slates" / "latest" / "slate.json"
    slate = json.loads(slate_path.read_text())
    slate["contracts"][0]["predicted_at_utc"] = "2026-09-29T14:50:00"  # no zone
    slate_path.write_text(json.dumps(slate))
    res = _export(root, out, acc)
    assert res["ok"] is False and "zone" in res["error"] and not (out / "manifest.json").exists()
    # and a good export never emits a naive stamp anywhere
    root2, acc2 = make_root(tmp_path / "second")
    out2 = tmp_path / "app2"
    assert _export(root2, out2, acc2)["ok"]
    naive = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(?![\dZ+\-.])")
    for p in out2.rglob("*.json"):
        text = p.read_text()
        assert not naive.search(text), f"{p.name} carries a timestamp without a zone"
        for m in re.finditer(r'"[a-z_]*(?:_at|_utc|as_of)":"([^"]+)"', text):
            assert timeutil.is_canonical(m.group(1)), (p.name, m.group(0))


# ------------------------------------------------------------------------------------------- 8. no secrets
def test_no_secret_shaped_strings_in_any_output(tmp_path):
    root, acc = make_root(tmp_path)
    out = tmp_path / "app"
    assert _export(root, out, acc)["ok"]
    bad = re.compile(r"PRIVATE KEY|ghp_|github_pat_|Bearer |AIRTABLE")
    for p in out.rglob("*.json"):
        assert not bad.search(p.read_text()), p


# ----------------------------------------------------------------------------- worker / workflow / archive
def test_the_worker_exports_after_a_capture_and_the_archive_verifier_ignores_app_latest(tmp_path):
    from nhl_edge.worker.run import Worker

    names = [n for n, _, _ in Worker.SLOW_JOBS]
    assert names.index("app_export") == names.index("evaluate") + 1 and "app_export" in Worker.DERIVED_JOBS
    tmpl = dict((n, t) for n, t, _ in Worker.SLOW_JOBS)["app_export"]
    assert tmpl[:2] == ["nhl", "app-export"] and "ARCHIVE/app/latest" in tmpl
    root, acc = make_root(tmp_path)
    out = root / "app" / "latest"
    assert _export(root, out, acc)["ok"]
    assert Ledger(root).verify() == [], "app/latest is not a ledger kind and must not break archive immutability verification"
    # the derived job is due after a successful capture, or after any slow job, and never when the cycle was idle
    calls: list[list[str]] = []
    w = Worker.__new__(Worker)
    w.archive_root, w.data_root, w.decide_fn = root, tmp_path, lambda: {}
    w.run_cmd = lambda cmd, timeout: (calls.append(cmd), (0, ""))[1]
    assert w._run_due_jobs({}, capture_ok=False) == []
    assert w._run_due_jobs({}, capture_ok=True) == ["app_export"] and calls[-1][:2] == ["nhl", "app-export"]
    assert w._run_due_jobs({"evaluate": True}, capture_ok=False) == ["evaluate", "app_export"]
    assert w._run_due_jobs({"app_export": False}, capture_ok=True) == []


def test_the_cli_exposes_app_export_and_the_workflows_carry_the_step():
    import yaml

    from nhl_edge.cli import build_parser

    args = build_parser().parse_args(["app-export", "--data-root", "x", "--out", "y"])
    assert args.fn.__name__ == "cmd_app_export" and args.data_root == "x"
    wf = yaml.safe_load((REPO_ROOT / ".github" / "workflows" / "conductor.yml").read_text())
    steps = wf["jobs"]["run"]["steps"]
    names = [s.get("name", "") for s in steps]
    export_i = next(i for i, n in enumerate(names) if n.startswith("App export"))
    push_i = next(i for i, n in enumerate(names) if n.startswith("Verify archive immutability and push"))
    assert names.index("Evaluate") < export_i < push_i, "the export reads what evaluate wrote and must precede the push"
    assert steps[export_i].get("continue-on-error") is True and "nhl app-export" in steps[export_i]["run"]
    fail_i = next(i for i, n in enumerate(names) if n.startswith("Fail the job if the app export failed"))
    assert fail_i > push_i and "app_export.outcome" in steps[fail_i]["if"], "the job goes red only after production outputs were pushed"
    registry = json.loads((REPO_ROOT / "contract" / "edge_finder_contract" / "registry.json").read_text())["sports"]["NHL"]
    assert registry["repo"] == app_export.SOURCE_REPO and registry["branch"] == app_export.SOURCE_BRANCH and registry["app_root"] == "app/latest"


# ------------------------------------------------------------------------------------- 7. real data proof
def test_real_data_smoke(tmp_path):
    """Runs against the production archive when it is checked out (data/archive, or NHL_EDGE_ARCHIVE_ROOT)."""
    root = Path(os.environ.get("NHL_EDGE_ARCHIVE_ROOT") or (REPO_ROOT / "data" / "archive"))
    if not (root / "manifest.jsonl").exists() or not (root / "slates" / "latest" / "slate.json").exists():
        pytest.skip("production data lives on the data-archive branch; check it out at data/archive (or set NHL_EDGE_ARCHIVE_ROOT) to run this")
    acc_env = os.environ.get("NHL_EDGE_ACCOUNTING_ROOT")
    acc = Path(acc_env) if acc_env else (REPO_ROOT / "data" / "accounting" if (REPO_ROOT / "data" / "accounting").exists() else None)
    out = tmp_path / "app"
    res = app_export.export(root, out, accounting_dir=acc, now=timeutil.now_utc())
    assert res["ok"], res.get("error")
    assert publish.verify_published(out) == []
    counts = res["counts"]
    assert counts["events"] >= 1 and counts["markets"] >= counts["events"] and counts["model_prices"] >= 0
    health = _load(out, "health")
    assert health["bet_authority"] == "RESEARCH_ONLY" and health["overall_status"] in ("RESEARCH_ONLY", "DEGRADED", "STALE")
    for r in _load(out, "recommendations")["items"]:
        assert r["status"] == "RESEARCH_CANDIDATE" and r["authority"] == "RESEARCH_ONLY" and r["research_only"]
    for p in _load(out, "model_prices")["items"]:
        assert p["model_version"] == "DATA_ONLY_V1" and 0.0 <= p["fair_probability"] <= 1.0
