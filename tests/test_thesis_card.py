"""Thesis card engine + completion gate on synthetic draws; outcome vectors from a real (small) joint simulation."""

from __future__ import annotations

import copy

import numpy as np
import pytest

from nhl_edge.kalshi.fees import DEFAULT_SCHEDULE, fee_per_contract_dollars
from nhl_edge.thesis.card import REQUIRED_FIELDS, gate_entry, joint_card_check, run_gate
from nhl_edge.thesis.engine import GameDistribution, analyze_game, finalize_slate
from nhl_edge.thesis.mapping import Bet
from nhl_edge.thesis.portfolio import PortfolioConfig
from nhl_edge.thesis.reliability import label_family, reliability_table
from tests.test_thesis_core import synth_features


def _bets_from(y: np.ndarray, ticker: str, family: str, mid_yes: float, team: str | None = None, contract_team: str | None = None) -> list[Bet]:
    out = []
    for side, ys, mid in (("yes", y, mid_yes), ("no", ~y, 1 - mid_yes)):
        ask = int(round(100 * mid)) + 1
        out.append(Bet(f"{ticker}|{side}", ticker, side, f"{ticker} {side}", family, "G1", ys.astype(bool), float(ys.mean()), ask,
                       fee_per_contract_dollars(ask, DEFAULT_SCHEDULE), mid, team, None, {"contract_team": contract_team}))
    return out


def synth_game(n: int = 10000, edge: float = 0.07) -> GameDistribution:
    f = synth_features(n)
    rng = np.random.default_rng(11)
    home_win = f.winner == 1
    over = f.total >= 7
    tt = f.home_goals >= 4
    star_goal = (rng.random(n) < 0.12 + 0.06 * np.minimum(f.home_goals, 5)) & (f.home_goals > 0)
    low_vol = f.away_net_faced <= 25
    bets = []
    bets += _bets_from(home_win, "ML-HOM", "game_winner", home_win.mean() - edge, "HOM", "HOM")
    bets += _bets_from(over, "TOT-6.5", "game_total", over.mean() + 0.01)
    bets += _bets_from(tt, "TT-HOM-3.5", "team_total", tt.mean() - edge, "HOM")
    bets += _bets_from(star_goal, "GOAL-STAR", "player_goals", star_goal.mean() - edge, "HOM")
    bets += _bets_from(low_vol, "SAVE-AWYG-26", "goalie_saves", low_vol.mean() - edge, "AWY")
    return GameDistribution("G1", "HOM", "AWY", 1, 2, f, bets, [{"ticker": "PERIOD-X", "reason": "fail closed"}])


REL = {fam: {"label": "EVIDENCE_MIXED"} for fam in ("game_winner", "game_total", "team_total", "player_goals", "goalie_saves")}


def test_engine_produces_a_complete_gated_card_with_joint_check():
    cfg = PortfolioConfig()
    a = analyze_game(synth_game(), REL, None, cfg)
    out = finalize_slate([a], cfg, REL)
    g = out["games"][0]
    assert out["gate"]["status"] == "PASS", out["gate"]["failures"]
    assert out["status"] == "COMPLETE" and out["card_emitted"]
    assert len(g["card"]) >= 2  # several +EV theses in one game
    assert g["joint_card_check"]["pairs"]
    for e in g["card"]:
        for k, _ in REQUIRED_FIELDS:
            assert e.get(k) is not None
        assert e["estimated_edge"]["ev_raw_per_contract"] > 0 and e["estimated_edge"]["ev_adjusted_per_contract"] > 0
    # exposure caps hold
    assert sum(e["recommended_stake"]["dollars"] for e in g["card"]) <= cfg.max_game_frac * cfg.bankroll + 1e-6
    # full board covers every contract, unpriced ones are reported with a reason (no hidden markets)
    assert len(g["full_board"]) == 5 and g["unpriced_contracts"][0]["reason"]
    # B (joint) has at least the log growth of C (subset) under the same constraints
    assert g["portfolios"]["B"]["expected_log_growth_bp"] >= g["portfolios"]["C"]["expected_log_growth_bp"] - 1e-6


def test_no_negative_ev_bet_reaches_the_card():
    cfg = PortfolioConfig()
    out = finalize_slate([analyze_game(synth_game(), REL, None, cfg)], cfg, REL)
    for e in out["games"][0]["card"]:
        assert "|no" not in e["bet_id"] or e["estimated_edge"]["ev_raw_per_contract"] > 0
    # with no edge anywhere the card is empty but the run is still a valid (NO_BETS) result
    out2 = finalize_slate([analyze_game(synth_game(edge=0.0), REL, None, cfg)], cfg, REL)  # fair market, 1c spread each side
    assert out2["status"] == "NO_BETS" and out2["games"][0]["card"] == []


def test_gate_fails_when_joint_analysis_is_missing_for_multi_bet_game():
    cfg = PortfolioConfig()
    out = finalize_slate([analyze_game(synth_game(), REL, None, cfg)], cfg, REL)
    entries = out["games"][0]["card"]
    assert len(entries) >= 2
    assert joint_card_check("G1", entries, None)  # no joint matrix -> failure
    assert run_gate({"G1": entries}, {})["status"] == "FAIL"
    broken = copy.deepcopy(entries)
    broken[0]["same_game_relationships"] = {}
    assert run_gate({"G1": broken}, {"G1": out["games"][0]["joint_card_check"]})["status"] == "FAIL"


def test_gate_fails_on_missing_field_and_accepts_explained_unknown():
    cfg = PortfolioConfig()
    out = finalize_slate([analyze_game(synth_game(), REL, None, cfg)], cfg, REL)
    e = copy.deepcopy(out["games"][0]["card"][0])
    e["primary_thesis"] = None
    assert gate_entry(e)[0]
    e["primary_thesis"] = {"status": "UNKNOWN", "reason": "test"}
    fails, unk = gate_entry(e)
    assert not fails and unk
    e["primary_thesis"] = {"status": "UNKNOWN", "reason": ""}
    assert gate_entry(e)[0]
    e["recommended_stake"] = {"status": "NOT_APPLICABLE", "reason": "x"}
    assert gate_entry(e)[0]


def test_single_bet_game_passes_without_pairwise_relationships():
    cfg = PortfolioConfig()
    out = finalize_slate([analyze_game(synth_game(), REL, None, cfg)], cfg, REL)
    e = copy.deepcopy(out["games"][0]["card"][0])
    e["same_game_relationships"] = {"status": "NOT_APPLICABLE", "reason": "only recommended bet in this game"}
    assert run_gate({"G1": [e]}, {})["status"] == "PASS"


def test_reliability_labels_come_from_artifacts():
    t = reliability_table()
    assert t["player_goals"]["label"] == "EVIDENCE_STRONGER"
    assert t["player_points"]["label"] == "CALIBRATION_WARNING"
    assert t["game_winner"]["label"] == "EVIDENCE_MIXED"
    assert label_family(None, None)["label"] == "EVIDENCE_THIN"
    small = label_family({"wf_n": 50000, "wf_ece": 0.002, "wf_beats_baseline": True, "mkt_n": 5000, "mkt_delta": -0.001}, {"n_games": 3, "n_rows": 40, "ece": 0.4})
    assert small["label"] == "EVIDENCE_STRONGER" and "SMALL_PROSPECTIVE_SAMPLE" in small["flags"]  # tiny prospective sample never flips the label


# ------------------------------------------------------------------------------------------------ real joint draw
def test_outcome_vectors_reproduce_prices_and_unsupported_contracts_fail_closed():
    from nhl_edge.players.engine import StrengthTable, TeamRoster, simulate_players
    from nhl_edge.players.params import SavesModel
    from nhl_edge.players.pricing import price_player
    from nhl_edge.players.saves import simulate_saves
    from nhl_edge.pricing.price_v2 import price_contract_v2
    from nhl_edge.schemas.market import Contract
    from nhl_edge.sim.engine import TeamParams
    from nhl_edge.sim.engine_v2 import DIFFS, TIME_EDGES, load_params, simulate_game_v2
    from nhl_edge.thesis.features import DrawFeatures
    from nhl_edge.thesis.outcomes import capture_view, contract_outcome

    res = simulate_game_v2(TeamParams(1, "HOM", 3.2), TeamParams(2, "AWY", 2.9), seed=123, n_sims=3000, params=load_params(), record_steps=True)

    def roster(tid: int, ab: str, base: int) -> TeamRoster:
        n = 18
        w = np.tile(np.linspace(2.0, 0.3, n), (6, 1))
        F = np.full((3, n, n), 1.0 / (n - 1))
        for k in range(3):
            np.fill_diagonal(F[k], 0.0)
        return TeamRoster(tid, ab, np.arange(base, base + n), [f"P{i}" for i in range(n)], ["C"] * 12 + ["D"] * 6, w, np.ones((6, n)), np.ones((6, n)), F,
                          np.full(n, 0.16), np.full(n, 0.0035), 0.2, 0.03, np.full(6, 0.08), np.full(6, 0.3))

    nb = len(TIME_EDGES) - 1
    st = StrengthTable(TIME_EDGES, DIFFS, np.zeros((nb, len(DIFFS))), np.zeros((nb, len(DIFFS))))
    ps = simulate_players(res, roster(1, "HOM", 100), roster(2, "AWY", 200), st, 5)
    sm = SavesModel(np.array([0.0, 1.0, 0.017, 0.0, 0.016]), 0.017, {1: 0.005, 2: 0.01, 3: 0.03}, 1)
    sh, sa = simulate_saves(res, ps, True, sm, 28.0, 7), simulate_saves(res, ps, False, sm, 30.0, 8)
    saves = {1: sh, 2: sa}
    gt = {900: 1, 901: 2}
    cap = capture_view(res)
    games = [Contract(ticker="W", family="game_winner", scope="game", stat="winner", period="FULL", team_id=1, support="MODELABLE"),
             Contract(ticker="T", family="game_total", scope="game", stat="total", period="FULL", threshold=6.5, comparator="gt", support="MODELABLE"),
             Contract(ticker="S", family="game_spread", scope="game", stat="margin", period="FULL", team_id=2, threshold=1.5, comparator="gt", support="MODELABLE"),
             Contract(ticker="P1", family="period_total", scope="game", stat="total", period="P1", threshold=1.5, comparator="gt", support="RESEARCH")]
    for c in games:
        y, p, _ = contract_outcome(c, None, cap, ps, saves, gt, 1, 2)
        pr, _ = price_contract_v2(c, res, 1, 2)
        assert y is not None and p == pytest.approx(pr.p, abs=1e-12) and y.mean() == pytest.approx(pr.p, abs=1e-12)
    for fam, pid, thr in (("player_goals", 100, 0.5), ("player_points", 201, 1.5), ("goalie_saves", 901, 24.5), ("first_goal", 100, None)):
        c = Contract(ticker="X", family=fam, scope="player", stat=None, period="FULL", threshold=thr, comparator="gt" if thr is not None else None, support="MODELABLE")
        y, p, _ = contract_outcome(c, pid, cap, ps, saves, gt, 1, 2)
        pp = price_player(fam, c.comparator, thr, pid, ps, saves, gt)
        assert y is not None and p == pytest.approx(pp.p, abs=1e-12)
    # unsupported / unresolvable contracts never get an invented outcome vector
    bad = [(Contract(ticker="F", family="futures", scope="season", stat=None, period="FULL", support="UNSUPPORTED"), None),
           (Contract(ticker="G", family="player_goals", scope="player", stat=None, period="FULL", threshold=0.5, comparator="gt", support="MODELABLE"), None),
           (Contract(ticker="G2", family="player_goals", scope="player", stat=None, period="FULL", threshold=0.5, comparator="gt", support="MODELABLE"), 999999),
           (Contract(ticker="E", family="game_early_goal", scope="game", stat="early_goal", period="FULL", support="UNSUPPORTED"), None)]
    for c, pid in bad:
        y, p, reason = contract_outcome(c, pid, cap, ps, saves, gt, 1, 2)
        assert y is None and p is None and reason
    # features from the joint draw reconcile with the team draw; seed reproducibility
    f = DrawFeatures.from_simulation(res, ps, sh, sa, "HOM", "AWY")
    assert np.array_equal(f.home_final, res.home_final) and np.array_equal(f.home_goals, ps.home.goals.sum(axis=1))
    assert np.all(f.home_net_faced >= f.away_goals - f.away_en)
    ps2 = simulate_players(res, roster(1, "HOM", 100), roster(2, "AWY", 200), st, 5)
    assert np.array_equal(ps2.home.state_goals, ps.home.state_goals) and np.array_equal(ps2.home.goals, ps.home.goals)
    assert np.array_equal(simulate_saves(res, ps, True, sm, 28.0, 7).net_shots_faced, sh.net_shots_faced)


def test_audit_flags_negative_ev_and_unknown_proposals():
    from nhl_edge.thesis.engine import audit_card

    cfg = PortfolioConfig()
    a = analyze_game(synth_game(), REL, None, cfg)
    ml_yes = next(b for b in a["bets"] if b.bet_id == "ML-HOM|yes")
    good = audit_card([a], [{"bet_id": "ML-HOM|yes", "stake_dollars": 10.0}], cfg, REL)
    assert good["gate"]["status"] == "PASS" and not good["negative_ev_bets"]
    overpay = audit_card([a], [{"bet_id": "ML-HOM|yes", "stake_dollars": 10.0, "price_cents": round(100 * ml_yes.p) + 5},
                               {"bet_id": "TOT-6.5|yes", "stake_dollars": 10.0}], cfg, REL)
    assert overpay["verdict"].startswith("FAILS") and "ML-HOM|yes" in overpay["negative_ev_bets"]
    assert overpay["games"][0]["joint_matrix"]["pairs"]  # two same-game proposals get a joint card check
    unk = audit_card([a], [{"bet_id": "NOPE|yes", "stake_dollars": 5.0}], cfg, REL)
    assert unk["missing"] and unk["missing"][0]["bet_id"] == "NOPE|yes"
