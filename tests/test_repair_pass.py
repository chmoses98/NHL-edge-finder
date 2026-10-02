"""Regression tests for the 2026-10-02 repair pass: final-card snapshot uniqueness, settlement / evaluation completeness,
expression fidelity and preference, player-prop research governance, the market-disagreement gate, opponent-adjustment
labelling and whole-dollar research staking. No network."""

from __future__ import annotations

import ast
import json
import random
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from nhl_edge.archive.ledger import ImmutabilityError, Ledger
from nhl_edge.schemas.core import FinalPeriodType, FinalResult, GameStatus
from nhl_edge.thesis import governance as G
from nhl_edge.thesis.engine import GameDistribution, analyze_game, finalize_slate
from nhl_edge.thesis.fidelity import DIRECT, FRAGILE, NONE, STRUCTURAL, classify, fidelity, relation
from nhl_edge.thesis.portfolio import PortfolioConfig
from nhl_edge.workflows import conductor as C
from nhl_edge.workflows.settle import run_settle
from nhl_edge.workflows.thesis_card import snapshot_id
from nhl_edge.workflows.thesis_postmortem import AMBIGUOUS, build_report, final_snapshots, snapshot_key
from tests.test_thesis_card import REL, _bets_from, synth_game
from tests.test_thesis_core import synth_features

T0 = datetime(2026, 10, 1, 23, 0, tzinfo=UTC)
ISO = lambda t: t.isoformat().replace("+00:00", "Z")  # noqa: E731


# ============================================================================================ 1. snapshot uniqueness
def _decision(gid: str, bet: str, ts: datetime, run: str, chosen: bool, stake: float = 5.0, **over) -> dict:
    d = {"decision_id": f"{gid}|{bet}|{ISO(ts)}|{run}", "decided_at_utc": ISO(ts), "run_id": run, "game_id": gid, "bet_id": bet, "ticker": bet.split("|")[0],
         "side": bet.split("|")[1], "family": "player_goals", "matchup": "AWY @ HOM", "chosen": chosen, "stake_dollars": stake if chosen else 0.0,
         "cost_per_contract": 0.40, "executable_price_cents": 39, "p_model": 0.45, "p_adjusted": 0.42, "p_kalshi_mid": 0.39, "ev_raw": 0.05, "ev_adjusted": 0.02,
         "primary_thesis": {"key": "HOM:OFFENSE_4PLUS", "p_thesis": 0.4, "p_bet_given_thesis": 0.45, "p_bet_given_not_thesis": 0.2}, "card_status": "COMPLETE",
         "start_time_utc": ISO(T0)}
    return d | over


def _game_row(gid: str, ts: datetime, run: str, rec: list[str], status: str = "COMPLETE", **over) -> dict:
    return {"game_id": gid, "decided_at_utc": ISO(ts), "run_id": run, "matchup": "AWY @ HOM", "recommended": rec, "card_status": status,
            "meta": {"start_time_utc": ISO(T0)}, "portfolio_config": {"max_bets_per_game": 4}, "scripts": [], "portfolios": {}} | over


def _pm(d: dict, won: bool) -> dict:
    cost = d["cost_per_contract"]
    return {"decision_id": d["decision_id"], "settlement_key": "k-" + d["ticker"], "game_id": d["game_id"], "bet_id": d["bet_id"], "decided_at_utc": d["decided_at_utc"],
            "family": d["family"], "chosen": d["chosen"], "stake_dollars": d["stake_dollars"], "won": won, "thesis_result": True,
            "expression_result": "THESIS_RIGHT_EXPRESSION_" + ("WON" if won else "LOST"), "price_result_clv": 0.0, "close_prob_yes": 0.4,
            "model_result": {"brier_model": 0.2, "brier_adjusted": 0.2, "brier_kalshi_mid": 0.21, "logloss_model": 0.6, "logloss_adjusted": 0.6},
            "realized_profit": round(d["stake_dollars"] * ((1.0 if won else 0.0) - cost) / cost, 2) if d["stake_dollars"] else None}


def _ctx(gids, final=True):
    sched = {g: {"game_id": g, "game_date_et": "2026-10-01", "start_time_utc": ISO(T0), "status": "final"} for g in gids}
    s = set(gids) if final else set()
    return {"schedule": sched, "finals": s, "events": s, "settled": s, "settlements": {}, "actual": {}}


def test_repeated_generations_under_one_worker_run_cannot_inflate_the_final_card():
    """The 2026-10-01 bug: one worker run_id, two simulate cycles (22:09 and 22:57), 4 chosen bets each. The final card
    is the 22:57 generation only: 4 bets, never 8."""
    run, gid = "36929294204", "G1"
    t1, t2 = T0 - timedelta(minutes=51), T0 - timedelta(minutes=3)
    bets = [f"B{i}|yes" for i in range(4)]
    dec = [_decision(gid, b, t, run, True, stake=5.0 + i) for t in (t1, t2) for i, b in enumerate(bets)]
    games = [_game_row(gid, t1, run, bets), _game_row(gid, t2, run, bets)]
    pms = [_pm(d, won=(i % 2 == 0)) for i, d in enumerate(dec)]
    rep = build_report(pms, games, dec, {gid: T0}, _ctx([gid]), T0 + timedelta(hours=6))
    s = rep["slates"]["2026-10-01"]
    fc = s["FINAL_CARD_UNIQUE"]["PORTFOLIO"]["nominal_card"]
    assert fc["n_bets"] == 4 and s["invariants"]["final_card_n"] == 4
    assert s["games"][gid]["final_snapshot"]["decided_at_utc"] == ISO(t2)
    assert {b["decision_id"] for b in s["games"][gid]["bets"]} == {d["decision_id"] for d in dec if d["decided_at_utc"] == ISO(t2)}
    assert s["label"].startswith("COMPLETE") and s["completeness"]["postmortem_complete"]
    # repeated observations stay available for calibration research, labelled as repeats
    ap = rep["ALL_PROSPECTIVE_DECISIONS"]
    assert ap["n_rows"] == 8 and ap["n_unique_logical_wagers"] == 4 and ap["repeat_factor"] == 2.0


@pytest.mark.parametrize("n_games,n_gen", [(1, 5), (3, 12), (8, 20)])
def test_invariant_final_card_never_exceeds_the_sum_of_game_caps(n_games, n_gen):
    rng = random.Random(n_games * 100 + n_gen)
    dec, games, pms, gids = [], [], [], [f"G{i}" for i in range(n_games)]
    for gen in range(n_gen):
        t = T0 - timedelta(minutes=5 * (n_gen - gen))
        run = f"run{gen // 4}"  # several generations per worker run, as in production
        for g in gids:
            chosen = [f"{g}B{rng.randrange(12)}|yes" for _ in range(4)]
            chosen = list(dict.fromkeys(chosen))
            dec += [_decision(g, b, t, run, True) for b in chosen]
            games.append(_game_row(g, t, run, chosen))
    pms = [_pm(d, True) for d in dec]
    rep = build_report(pms, games, dec, {g: T0 for g in gids}, _ctx(gids), T0 + timedelta(hours=6))
    inv = rep["slates"]["2026-10-01"]["invariants"]
    assert inv["holds"] and inv["final_card_n"] <= 4 * n_games == inv["sum_game_card_caps"]
    assert rep["invariants_hold"]


def test_legacy_rows_reconstruct_the_same_snapshot_id_and_the_final_snapshot_comes_from_thesis_games():
    run, ts = "r1", ISO(T0 - timedelta(minutes=10))
    assert snapshot_key({"run_id": run, "decided_at_utc": ts}) == snapshot_id(run, ts) == snapshot_key({"snapshot_id": snapshot_id(run, ts)})
    # a later generation with NO shortlisted bet is still the final one: the game's final card is empty, not the earlier bets
    early, late = T0 - timedelta(minutes=40), T0 - timedelta(minutes=5)
    dec = [_decision("G1", "B1|yes", early, run, True)]
    games = [_game_row("G1", early, run, ["B1|yes"]), _game_row("G1", late, run, [], status="NO_BETS")]
    fs = final_snapshots(games, dec, {"G1": T0})["G1"]
    assert fs["status"] == "OK" and fs["n_chosen"] == 0 and fs["decided_at_utc"] == ISO(late)


def test_postgame_and_incomplete_generations_are_never_the_final_card():
    run = "r1"
    pre, post = T0 - timedelta(minutes=20), T0 + timedelta(minutes=5)
    dec = [_decision("G1", "A|yes", pre, run, True), _decision("G1", "Z|yes", post, run, True), _decision("G1", "X|yes", T0 - timedelta(minutes=2), run, True)]
    games = [_game_row("G1", pre, run, ["A|yes"]), _game_row("G1", post, run, ["Z|yes"]), _game_row("G1", T0 - timedelta(minutes=2), run, ["X|yes"], status="INCOMPLETE")]
    fs = final_snapshots(games, dec, {"G1": T0})["G1"]
    assert fs["status"] == "OK" and [d["bet_id"] for d in fs["chosen"]] == ["A|yes"] and fs["later_incomplete_snapshots_skipped"]


@pytest.mark.parametrize("problem", ["duplicate_rows", "mismatch", "duplicate_bet", "over_cap"])
def test_ambiguous_final_snapshots_fail_closed_and_are_excluded_from_pl(problem):
    run, t = "r1", T0 - timedelta(minutes=5)
    bets = ["A|yes", "B|yes"]
    dec = [_decision("G1", b, t, run, True) for b in bets]
    games = [_game_row("G1", t, run, bets)]
    if problem == "duplicate_rows":
        games.append(_game_row("G1", t, run, bets))
    elif problem == "mismatch":
        games = [_game_row("G1", t, run, ["A|yes"])]
    elif problem == "duplicate_bet":
        dec.append(dict(dec[0], decision_id="dup"))
        games = [_game_row("G1", t, run, bets + ["A|yes"])]
    else:
        more = [f"C{i}|yes" for i in range(5)]
        dec += [_decision("G1", b, t, run, True) for b in more]
        games = [_game_row("G1", t, run, bets + more)]
    rep = build_report([_pm(d, True) for d in dec], games, dec, {"G1": T0}, _ctx(["G1"]), T0 + timedelta(hours=6))
    s = rep["slates"]["2026-10-01"]
    assert s["games"]["G1"]["state"] == AMBIGUOUS and s["completeness"]["games_ambiguous"] == ["G1"]
    assert s["FINAL_CARD_UNIQUE"]["PORTFOLIO"]["nominal_card"]["n_bets"] == 0
    assert not s["completeness"]["final_card_complete"] and not s["completeness"]["postmortem_complete"] and AMBIGUOUS in s["label"]


def test_partial_slate_is_never_labelled_complete():
    run, t = "r1", T0 - timedelta(minutes=5)
    dec = [_decision("G1", "A|yes", t, run, True), _decision("G2", "B|yes", t, run, True)]
    games = [_game_row("G1", t, run, ["A|yes"]), _game_row("G2", t, run, ["B|yes"])]
    ctx = _ctx(["G1", "G2"])
    ctx["finals"], ctx["events"], ctx["settled"] = {"G1"}, {"G1"}, {"G1"}  # the late game is not settled yet
    rep = build_report([_pm(dec[0], True)], games, dec, {"G1": T0, "G2": T0}, ctx, T0 + timedelta(hours=4))
    s = rep["slates"]["2026-10-01"]
    assert s["label"] == "PARTIAL — 1/2 games evaluated"
    c = s["completeness"]
    assert (c["games_scheduled"], c["games_final"], c["games_thesis_evaluated"]) == (2, 1, 1)
    assert not c["final_card_complete"] and not c["postmortem_complete"] and "G2" in c["games_missing"]
    assert "INTERIM" in s["FINAL_CARD_UNIQUE"]["interpretation"]
    # once the late game is settled and scored, the same slate becomes COMPLETE
    ctx["finals"], ctx["events"], ctx["settled"] = {"G1", "G2"}, {"G1", "G2"}, {"G1", "G2"}
    rep2 = build_report([_pm(d, True) for d in dec], games, dec, {"G1": T0, "G2": T0}, ctx, T0 + timedelta(hours=8))
    assert rep2["slates"]["2026-10-01"]["label"] == "COMPLETE — 2/2 games evaluated"


# ============================================================================== 2. settlement / evaluation completeness
def _final(gid: str, final: bool = True) -> FinalResult:
    return FinalResult(game_id=gid, status=GameStatus.FINAL if final else GameStatus.LIVE, home_team_id=1, away_team_id=2, home_final=3 if final else None,
                       away_final=2 if final else None, home_reg=3 if final else None, away_reg=2 if final else None,
                       last_period_type=FinalPeriodType.REG if final else None, source="test", fetched_at_utc=T0)


def _tables(gid: str) -> dict:
    pl = pd.DataFrame([{"game_id": int(gid), "team_id": 1, "sweater": 9, "name": "A Skater", "goals": 1}])
    gl = pd.DataFrame([{"game_id": int(gid), "team_id": 2, "sweater": 30, "name": "A Goalie", "saves": 25}])
    goals = pd.DataFrame([{"game_id": int(gid), "period_type": "REG", "team_id": 1}])
    return {"players": pl, "goalies": gl, "goals": goals, "shots": pd.DataFrame(), "coice": pd.DataFrame(), "team_states": pd.DataFrame()}


def _settle_archive(root: Path) -> Ledger:
    led = Ledger(root, run_id="w1")
    day1 = [{"game_id": g, "game_date_et": "2026-10-01", "start_time_utc": ISO(t), "status": "not_started", "home_abbrev": "HOM", "away_abbrev": "AWY"}
            for g, t in (("2026020011", T0), ("2026020012", T0 + timedelta(hours=1)), ("2026020016", T0 + timedelta(hours=3)))]
    led.append_rows("context/schedule", day1, observed_at=T0 - timedelta(hours=6))
    # after midnight ET the schedule feed only lists the next day's games
    led.append_rows("context/schedule", [{"game_id": "2026020017", "game_date_et": "2026-10-02", "start_time_utc": ISO(T0 + timedelta(hours=24)),
                                          "status": "not_started"}], observed_at=T0 + timedelta(hours=6))
    led.append_rows("predictions", [{"ticker": f"T{g}", "game_id": g} for g in ("2026020011", "2026020012", "2026020016")], observed_at=T0 - timedelta(hours=1))
    return led


def test_settle_ingests_several_games_in_one_run_without_a_ledger_collision(tmp_path):
    led = _settle_archive(tmp_path)
    now = T0 + timedelta(hours=4, minutes=5)  # the two early games are past the 3h grace, the West Coast game is not
    rc = run_settle(tmp_path, tmp_path, fetch_result=lambda g: (_final(g), []), now=now, fetch_player_events=lambda g, m: (_tables(g), []))
    assert rc == 0
    st = json.loads((tmp_path / "STATUS_settle.json").read_text())
    assert sorted(st["player"]["games_ingested"]) == ["2026020011", "2026020012"] and not st["player"]["errors"]
    assert st["backlog"] == {"2026020011": "COMPLETE", "2026020012": "COMPLETE"} and st["games_pending"] == []
    files = sorted(p.name for p in (tmp_path / "player_events" / "players").rglob("*.jsonl.gz"))
    assert len(files) == 2 and len(set(files)) == 2
    assert not led.verify()


def test_ledger_part_disambiguates_same_instant_writes_and_still_refuses_true_overwrites(tmp_path):
    led = Ledger(tmp_path, run_id="w1")
    led.append_rows("player_events/players", [{"a": 1}], observed_at=T0, part="2026020011")
    led.append_rows("player_events/players", [{"a": 2}], observed_at=T0, part="2026020012")
    with pytest.raises(ImmutabilityError):
        led.append_rows("player_events/players", [{"a": 3}], observed_at=T0, part="2026020012")
    assert sorted(r["a"] for r in led.iter_rows("player_events/players")) == [1, 2]


def test_late_west_coast_game_becomes_due_and_is_settled_automatically(tmp_path):
    _settle_archive(tmp_path)
    fetch = {"n": 0}

    def fetch_result(g):
        fetch["n"] += 1
        return _final(g), []

    run_settle(tmp_path, tmp_path, fetch_result=fetch_result, now=T0 + timedelta(hours=4, minutes=5), fetch_player_events=lambda g, m: (_tables(g), []))
    later = T0 + timedelta(hours=7)  # the late game is past its grace; the newest schedule snapshot no longer lists it
    led = Ledger(tmp_path)
    latest_only = C._latest_schedule(led)
    assert {r["game_id"] for r in latest_only} == {"2026020017"}  # the pre-fix conductor input: the late game is invisible
    union = C._recent_schedule(led, later)
    pending = C.settle_backlog(later, union, C._settle_terminal(tmp_path))
    assert pending == ["2026020016"]
    d = C.decide(later, union, 5, 5, 60, 60, 5, 5, pending)
    assert d["settle"] and d["evaluate"]
    run_settle(tmp_path, tmp_path, fetch_result=fetch_result, now=later, fetch_player_events=lambda g, m: (_tables(g), []))
    st = json.loads((tmp_path / "STATUS_settle.json").read_text())
    assert st["backlog"]["2026020016"] == "COMPLETE" and st["games_pending"] == []
    assert C.settle_backlog(later, union, C._settle_terminal(tmp_path)) == []
    assert not C.decide(later, union, 5, 5, 60, 60, 5, 5, [])["settle"] or C.decide(later, union, 5, 5, 60, 60, 5, 5, [])["n_recent_started"]


def test_a_game_still_live_at_the_first_settle_is_retried_not_dropped(tmp_path):
    _settle_archive(tmp_path)
    live = {"2026020012"}
    run_settle(tmp_path, tmp_path, fetch_result=lambda g: (_final(g, final=g not in live), []), now=T0 + timedelta(hours=4, minutes=5),
               fetch_player_events=lambda g, m: (_tables(g), []))
    st = json.loads((tmp_path / "STATUS_settle.json").read_text())
    assert st["backlog"]["2026020012"] == "PENDING_RESULT" and "2026020012" in st["not_final_yet"] and "2026020012" not in st["games_terminal"]
    assert C.settle_backlog(T0 + timedelta(hours=5), C._recent_schedule(Ledger(tmp_path), T0 + timedelta(hours=5)), C._settle_terminal(tmp_path)) == ["2026020012"]


def test_settle_retry_cadence_and_evaluate_follows_settle():
    now = T0 + timedelta(hours=8)
    rows = [{"game_id": "1", "start_time_utc": ISO(T0), "status": "final"}]
    assert C.decide(now, rows, 5, 5, 50, 40, 5, 5, ["1"])["settle"]  # backlog: retry after 45 min
    assert not C.decide(now, rows, 5, 5, 30, 20, 5, 5, ["1"])["settle"]
    # an evaluate that is older than the last settle is due (a failed evaluate is retried)
    assert C.decide(now, rows, 5, 5, 30, 120, 5, 5, [])["evaluate"]
    assert not C.decide(now, rows, 5, 5, 30, 20, 5, 5, [])["evaluate"] or now.hour == 10


def test_evaluate_status_breadcrumb_is_canonical_and_mirrored(tmp_path):
    from nhl_edge.workflows.evaluate import run_evaluate

    (tmp_path / "eval").mkdir()
    (tmp_path / "eval" / "STATUS_evaluate.json").write_text(json.dumps({"evaluated_at_utc": "2026-09-30T03:23:39Z"}))  # the stale legacy file
    now = datetime(2026, 10, 2, 13, 0, tzinfo=UTC)
    assert run_evaluate(tmp_path, tmp_path, now=now) == 0
    a = json.loads((tmp_path / "STATUS_evaluate.json").read_text())
    b = json.loads((tmp_path / "eval" / "STATUS_evaluate.json").read_text())
    assert a == b and a["evaluated_at_utc"] == "2026-10-02T13:00:00Z" and a["canonical_path"] == "STATUS_evaluate.json"
    assert set(a["steps"]) >= {"v1", "player", "thesis_postmortem"}


# ======================================================================================== 3-4. expression fidelity
def test_fidelity_relations_and_classes_are_logical():
    assert relation(100, 40, 40) == "IMPLIED_BY_THESIS" and relation(40, 40, 40) == "EQUIVALENT"
    assert relation(30, 40, 30) == "IMPLIES_THESIS" and relation(50, 40, 20) == "CORRELATED"
    assert classify(1.0, "IMPLIED_BY_THESIS") == STRUCTURAL and classify(0.62, "CORRELATED") == DIRECT and classify(0.27, "CORRELATED") == FRAGILE
    assert classify(None, None) == NONE
    f = fidelity(10000, 1500, 4000, 1080, "player_goals", "UTA:OFFENSE_4PLUS")
    assert f["fidelity_class"] == FRAGILE and f["thesis_capture"] == 0.27 and f["expression_kind"] == "FRAGILE_PLAYER"
    assert f["thesis_lift"] == round(0.27 - (1500 - 1080) / 6000, 4)
    tt = fidelity(10000, 4000, 4000, 4000, "team_total", "UTA:OFFENSE_4PLUS")
    assert tt["fidelity_class"] == STRUCTURAL and tt["relation"] == "EQUIVALENT" and tt["tracking"] == 1.0 and tt["expression_kind"] == "BROAD"


def _pref_game(tt_edge: float, star_edge: float = 0.09, tt_side_shift: float = 0.0) -> GameDistribution:
    """HOM 4+ thesis: a fragile player prop (cashes 45% of thesis-true draws) and the structural team total."""
    f = synth_features(10000)
    rng = np.random.default_rng(5)
    tt = f.home_goals >= 4
    star = tt & (rng.random(f.n) < 0.45)
    bets = _bets_from(star, "GOAL-STAR", "player_goals", star.mean() - star_edge, "HOM")
    bets += _bets_from(tt, "TT-HOM-3.5", "team_total", tt.mean() - tt_edge + tt_side_shift, "HOM")
    return GameDistribution("G1", "HOM", "AWY", 1, 2, f, bets, [])


def test_broad_structural_expression_replaces_a_fragile_prop_when_adjusted_value_is_similar():
    cfg = PortfolioConfig(max_bets_per_game=1)
    rel = {"player_goals": {"label": "EVIDENCE_MIXED"}, "team_total": {"label": "EVIDENCE_MIXED"}}
    a0 = analyze_game(_pref_game(tt_edge=0.08, star_edge=0.08), rel, None, cfg)
    e = a0["econ"]
    assert a0["selection"][0]["added"] == "GOAL-STAR|yes"  # the optimiser alone picks the fragile prop (higher adjusted growth)
    assert 0 < e["GOAL-STAR|yes"].ev_adj - e["TT-HOM-3.5|yes"].ev_adj <= 0.01  # but the structural team total is within one tick
    ov = [o for o in a0["overrides"] if o["applied"]]
    assert len(ov) == 1 and ov[0]["replaced"] == "GOAL-STAR|yes" and ov[0]["selected"] == "TT-HOM-3.5|yes"
    assert ov[0]["text"].startswith("Broad expression TT-HOM-3.5|yes selected over player prop GOAL-STAR|yes because adjusted EV differs by only")
    assert "thesis capture is 1.00 vs 0.45" in ov[0]["text"] and ov[0]["decided_on"] == "expression fidelity"
    out = finalize_slate([a0], cfg, rel)
    g = out["games"][0]
    assert [x["bet_id"] for x in g["card"]] == ["TT-HOM-3.5|yes"]
    entry = g["card"][0]
    assert entry["expression_fidelity"]["fidelity_class"] == STRUCTURAL and entry["reason_chosen"] == ov[0]["text"]
    assert entry["selection_override"]["replaced"] == "GOAL-STAR|yes"
    assert g["research_status"]["GOAL-STAR|yes"]["status"] == G.REJECTED and g["research_status"]["GOAL-STAR|yes"]["research_stake_dollars"] == 0
    assert out["status"] == "COMPLETE" and out["gate"]["status"] == "PASS"


def test_preference_never_forces_a_broad_market_that_is_not_plus_ev_or_not_similar():
    cfg = PortfolioConfig(max_bets_per_game=1)
    rel = {"player_goals": {"label": "EVIDENCE_MIXED"}, "team_total": {"label": "EVIDENCE_MIXED"}}
    for tt_edge, star_edge in ((-0.02, 0.12), (0.06, 0.09)):  # -EV, or +EV but 1.7 pts (more than a tick) below the prop's adjusted EV
        a = analyze_game(_pref_game(tt_edge=tt_edge, star_edge=star_edge), rel, None, cfg)
        out = finalize_slate([a], cfg, rel)
        assert not [o for o in a["overrides"] if o["applied"]]
        for x in out["games"][0]["card"]:
            assert x["estimated_edge"]["ev_adjusted_per_contract"] > 0


def test_expression_rows_and_review_expose_fidelity_and_the_choice():
    cfg = PortfolioConfig()
    a = analyze_game(synth_game(), REL, None, cfg)
    out = finalize_slate([a], cfg, REL)
    g = out["games"][0]
    ex = g["expressions"]["HOM:OFFENSE_4PLUS"]
    assert {"fidelity_class", "thesis_capture", "thesis_lift", "relation"} <= set(ex["rows"][0])
    assert ex["highest_fidelity"]["fidelity_class"] == STRUCTURAL
    rv = g["review"]
    assert rv["top_scripts"] and rv["theses"] and rv["bets"]
    for b in rv["bets"]:
        assert {"expression_kind", "fidelity_class", "large_disagreement", "family_trust", "status", "fails_even_if_thesis_right", "opposing_evidence",
                "relationships"} <= set(b)
        assert b["family_trust"] in ("TRUSTED", "MIXED", "WARNING")


# ==================================================================================== 5-6. governance and the gate
GOV = G.ResearchGovernance()
CAPS = {"max_bet_frac": 0.02, "max_game_frac": 0.05, "max_thesis_frac": 0.03, "max_slate_frac": 0.15}


def _item(bet_id, game="G1", family="player_goals", frac=0.01, p_adj=0.40, growth=5.0, fid=2, gap=0.02, warning=None, checks=None, order=0, thesis=None):
    return {"bet_id": bet_id, "game_id": game, "game_order": order, "family": family, "thesis": thesis or f"T:{bet_id}", "frac": frac, "p_adj": p_adj, "growth_bp": growth,
            "fidelity_rank": fid, "warning": warning or [], "disagreement": {"large": abs(gap) >= 0.10, "abs_gap_pts": 100 * abs(gap)}, "corroboration": checks or []}


def _ctx_bet(**over):
    base = {"family": "player_assists", "side": "no", "p_model": 0.476, "p_mid": 0.305, "reliability": "EVIDENCE_MIXED", "warning": [], "bucket": None, "bench": "D",
            "p_v1": None, "first_mid": None, "role_confidence": "MEDIUM", "projection_quality": "STANDARD", "deployment_source": "LINES_PROJECTED",
            "uncertainty_flags": [], "pp_unit": "pp1", "expected_toi_min": 21.97}
    return base | over


def test_mcdavid_style_large_disagreement_in_a_warning_family_is_shadow_only():
    ctx = _ctx_bet(warning=G.calibration_warning("player_assists", "EVIDENCE_MIXED", None))
    assert ctx["warning"] and "S-shaped" in ctx["warning"][0]  # known concern documented before the slate
    dis = G.market_disagreement(0.476, 0.305, 31, "player_assists", GOV)
    assert dis["large"] and dis["abs_gap_pts"] == 17.1
    checks = G.corroboration(ctx, GOV)
    st = {c["check"]: c["status"] for c in checks}
    assert st["OPPONENT_ADJUSTED_OPPORTUNITY"] == "UNAVAILABLE" and st["INDEPENDENT_ARM_AGREEMENT"] == "UNAVAILABLE"
    assert st["CONFIRMED_LINEUP_ROLE"] == "NEUTRAL"  # projected, not confirmed: no faked corroboration
    res = G.apply([_item("MCD|no", family="player_assists", gap=-0.171, warning=ctx["warning"], checks=checks)], GOV, CAPS)
    r = res["MCD|no"]
    assert r["status"] == G.SHADOW and r["research_stake_dollars"] == 0
    assert "LARGE_MARKET_DISAGREEMENT_UNCORROBORATED" in r["reasons"] and "CALIBRATION_WARNING_UNCORROBORATED" in r["reasons"]
    assert r["label"].startswith("SHADOW_ONLY — ") and "LARGE_MARKET_DISAGREEMENT_UNCORROBORATED" in r["label"]


def test_large_disagreement_gate_requires_real_strong_corroboration():
    confirmed = _ctx_bet(family="player_goals", side="yes", p_model=0.45, p_mid=0.33, role_confidence="HIGH", deployment_source="LINES_CONFIRMED",
                         projection_quality="FULL", first_mid=0.30)
    checks = G.corroboration(confirmed, GOV)
    s = G.corroboration_summary(checks)
    assert sorted(s["strong_passes"]) == ["CONFIRMED_LINEUP_ROLE", "MARKET_MOVEMENT_TOWARD_MODEL"]
    ok = G.apply([_item("P|yes", gap=0.12, checks=checks)], GOV, CAPS)["P|yes"]
    assert ok["status"] == G.FUNDED and ok["research_stake_dollars"] >= 1
    # the same corroboration is not enough under a calibration warning (stricter: 3 strong passes, no failures)
    warn = G.apply([_item("P|yes", gap=0.12, checks=checks, warning=["reliability label CALIBRATION_WARNING"])], GOV, CAPS)["P|yes"]
    assert warn["status"] == G.SHADOW
    # market moving AWAY from the model is a strong failure
    away = G.corroboration(confirmed | {"first_mid": 0.37}, GOV)
    assert G.apply([_item("P|yes", gap=0.12, checks=away)], GOV, CAPS)["P|yes"]["status"] == G.SHADOW
    # below the threshold the gate does not trigger; the threshold is configurable per family
    assert G.apply([_item("P|yes", gap=0.06)], GOV, CAPS)["P|yes"]["status"] == G.FUNDED
    strict = replace(GOV, disagreement_threshold_by_family={"player_goals": 0.05})
    assert G.market_disagreement(0.45, 0.39, None, "player_goals", strict)["large"]
    assert not G.market_disagreement(0.45, 0.39, None, "player_goals", GOV)["large"]


def test_game_markets_are_not_subject_to_the_player_prop_gate():
    r = G.apply([_item("ML|yes", family="game_winner", gap=0.15)], GOV, CAPS)["ML|yes"]
    assert r["status"] == G.FUNDED and not r["is_player_prop"]


def test_player_prop_tier_limits_per_game_and_low_probability_per_slate():
    items = [_item("P1|yes", growth=9, fid=1, p_adj=0.2), _item("P2|yes", growth=8, fid=2, p_adj=0.25), _item("ML|yes", family="game_winner"),
             _item("Q1|yes", game="G2", order=1, growth=7, p_adj=0.2), _item("R1|yes", game="G3", order=2, growth=6, p_adj=0.1),
             _item("S1|yes", game="G4", order=3, growth=5, p_adj=0.15)]
    res = G.apply(items, GOV, CAPS)
    assert res["P2|yes"]["status"] == G.FUNDED  # higher fidelity wins the game's single funded prop slot
    assert res["P1|yes"]["status"] == G.SHADOW and "PLAYER_PROP_GAME_CAP" in res["P1|yes"]["reasons"][0]
    low = [b for b in ("P2|yes", "Q1|yes", "R1|yes", "S1|yes") if res[b]["status"] == G.FUNDED]
    assert len(low) == 2 and low == ["P2|yes", "Q1|yes"]
    assert any("LOW_PROB_PLAYER_PROP_SLATE_CAP" in x for x in res["S1|yes"]["reasons"])
    assert res["ML|yes"]["status"] == G.FUNDED
    for r in res.values():
        if r["status"] != G.FUNDED:
            assert r["research_stake_dollars"] == 0


def test_governance_limits_are_configurable_and_labelled_as_governance(monkeypatch):
    monkeypatch.setenv("NHL_EDGE_RESEARCH_GOVERNANCE", json.dumps({"max_funded_player_props_per_game": 2, "low_prob_threshold": 0.2}))
    monkeypatch.setenv("NHL_EDGE_RESEARCH_BANKROLL", "500")
    g = G.governance_config()
    assert g.max_funded_player_props_per_game == 2 and g.low_prob_threshold == 0.2 and g.research_bankroll == 500
    assert "not model truth" in g.label
    monkeypatch.setenv("NHL_EDGE_RESEARCH_GOVERNANCE", "{not json")
    assert G.governance_config().max_funded_player_props_per_game == 1


# ================================================================================================ 7. evidence labels
def test_no_statistic_is_labelled_opponent_adjusted_unless_it_is():
    assert not G.OPPONENT_ADJUSTED_AVAILABLE
    for name in G.EVIDENCE_REGISTRY:
        e = G.evidence(name)
        assert e["basis"] != G.OPPONENT_ADJUSTED and e["opponent_adjusted"] in (False, None)
        if e["basis"] == G.RAW:
            assert e["label"] == "RAW / NOT OPPONENT ADJUSTED" and e["authority"] == "WEAK"
    with pytest.raises(KeyError):
        G.evidence("some_unregistered_stat")
    checks = G.corroboration(_ctx_bet(family="player_goals", side="yes"), GOV)
    raw = [c for c in checks if c["basis"] == G.RAW]
    assert raw and all(c["authority"] == "WEAK" for c in raw)
    assert not set(G.corroboration_summary(checks)["strong_passes"]) & {c["check"] for c in raw}


# ================================================================================================ 9. research stakes
def test_research_stake_rounds_up_to_whole_dollars_within_caps():
    B = GOV.research_bankroll
    res = G.research_stakes([{"bet_id": "a", "game_id": "G", "thesis": "t1", "frac": 1.2 / B}, {"bet_id": "b", "game_id": "G2", "thesis": "t", "frac": 0.2 / B},
                             {"bet_id": "c", "game_id": "G3", "thesis": "t", "frac": 5.4 / B}, {"bet_id": "d", "game_id": "G4", "thesis": "t", "frac": 4.3 / B}], GOV, CAPS)
    assert [res[k]["stake_dollars"] for k in "abcd"] == [2, 1, 5, 5]
    assert "breach a cap" in res["c"]["rounding"]


def test_rounding_up_never_breaches_a_game_thesis_or_slate_cap():
    B = GOV.research_bankroll
    # game cap 5% of $250 = $12.50: three $4.50 bets -> 5 + 5 + 2 (2.50 left -> largest whole dollar 2)
    its = [{"bet_id": f"x{i}", "game_id": "G", "thesis": f"t{i}", "frac": 4.5 / B} for i in range(3)]
    assert [G.research_stakes(its, GOV, CAPS)[f"x{i}"]["stake_dollars"] for i in range(3)] == [5, 5, 2]
    # thesis cap 3% = $7.50 shared by two bets on one thesis -> 5 + 2
    its = [{"bet_id": f"y{i}", "game_id": "G", "thesis": "T", "frac": 4.0 / B} for i in range(2)]
    assert [G.research_stakes(its, GOV, CAPS)[f"y{i}"]["stake_dollars"] for i in range(2)] == [4, 3]
    rng = random.Random(7)
    for _ in range(200):
        its = [{"bet_id": f"z{i}", "game_id": f"G{rng.randrange(4)}", "thesis": f"T{rng.randrange(3)}", "frac": rng.random() * 0.03} for i in range(rng.randrange(1, 15))]
        res = G.research_stakes(its, GOV, CAPS)
        st = {k: v["stake_dollars"] for k, v in res.items()}
        assert all(isinstance(v, int) and 0 <= v <= GOV.max_research_stake for v in st.values())
        assert sum(st.values()) <= CAPS["max_slate_frac"] * B + 1e-9
        for g in {i["game_id"] for i in its}:
            assert sum(st[i["bet_id"]] for i in its if i["game_id"] == g) <= CAPS["max_game_frac"] * B + 1e-9
            for t in {i["thesis"] for i in its}:
                assert sum(st[i["bet_id"]] for i in its if i["game_id"] == g and i["thesis"] == t) <= CAPS["max_thesis_frac"] * B + 1e-9


def test_engine_card_shadow_bets_have_zero_stake_and_funded_stakes_are_whole_dollars():
    cfg = PortfolioConfig()
    out = finalize_slate([analyze_game(synth_game(), REL, None, cfg)], cfg, REL)
    for g in out["games"]:
        for e in g["card"]:
            rg = e["research_governance"]
            assert isinstance(rg["research_stake_dollars"], int)
            if rg["status"] != G.FUNDED:
                assert rg["research_stake_dollars"] == 0
            else:
                assert 1 <= rg["research_stake_dollars"] <= GOV.max_research_stake
        for v in g["research_status"].values():
            assert v["status"] in (G.FUNDED, G.SHADOW, G.REJECTED)
            assert v["status"] == G.FUNDED or v["research_stake_dollars"] == 0
    assert out["slate_portfolios"]["R"]["total_stake"] <= CAPS["max_slate_frac"] * GOV.research_bankroll
    assert out["slate_portfolios"]["B"]["total_stake"] == out["slate_portfolios"]["B"]["total_stake"]  # the optimiser card is unchanged by governance


def test_governance_does_not_change_the_optimiser_card_or_model_probabilities():
    cfg = PortfolioConfig()
    a1 = analyze_game(synth_game(), REL, None, cfg)
    p_before = {b.bet_id: (b.p, a1["econ"][b.bet_id].p_adj) for b in a1["bets"]}
    stakes_before = [float(s) for s in a1["portfolios"]["B"][1]]
    strict = replace(GOV, max_funded_player_props_per_game=0, max_research_stake=1.0)
    out = finalize_slate([a1], cfg, REL, gov=strict)
    assert [float(s) for s in a1["portfolios"]["B"][1]] == stakes_before
    assert {b.bet_id: (b.p, a1["econ"][b.bet_id].p_adj) for b in a1["bets"]} == p_before
    assert all(e["research_governance"]["research_stake_dollars"] <= 1 for e in out["games"][0]["card"])


# ============================================================================================ 13. no order placement
def test_no_new_code_can_place_or_route_a_wager():
    src = Path(__file__).resolve().parents[1] / "src" / "nhl_edge"
    new = [src / "thesis" / "fidelity.py", src / "thesis" / "governance.py", src / "thesis" / "research_layer.py", src / "workflows" / "thesis_postmortem.py",
           src / "research" / "rules_replay.py"]
    banned_imports = {"httpx", "requests", "urllib", "socket", "nhl_edge.kalshi.client"}
    for p in new:
        text = p.read_text()
        tree = ast.parse(text)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                assert not {a.name.split(".")[0] for a in node.names} & banned_imports, p
            if isinstance(node, ast.ImportFrom):
                assert (node.module or "") not in banned_imports and not (node.module or "").startswith(("httpx", "requests", "urllib")), p
        for word in ("create_order", "/portfolio/orders", "place_order", "submit_order"):
            assert word not in text, (p, word)
