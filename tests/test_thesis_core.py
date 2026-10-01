"""Game-script / thesis / joint / portfolio core math on synthetic draws (no network, no live slate)."""

from __future__ import annotations

import numpy as np
import pytest

from nhl_edge.execution.economics import kelly_fraction
from nhl_edge.kalshi.fees import DEFAULT_SCHEDULE, fee_per_contract_dollars
from nhl_edge.thesis.events import thesis_events
from nhl_edge.thesis.features import DrawFeatures
from nhl_edge.thesis.joint import (
    DUPLICATIVE,
    MOSTLY_INDEPENDENT,
    PARTIALLY_CONTRADICTORY,
    REINFORCING,
    check_identities,
    joint_matrix,
)
from nhl_edge.thesis.mapping import Bet, EventMatrix, associations, concentration, script_counts, thesis_profile
from nhl_edge.thesis.portfolio import (
    PortfolioConfig,
    independent_stakes,
    kelly_optimize,
    metrics,
    optimize_game,
    pair_is_diversifier,
    pnl,
    returns,
)
from nhl_edge.thesis.scripts import (
    N_PRIMARY,
    build_distribution,
    control_labels,
    env_labels,
    margin_labels,
    overlay_tags,
    primary_labels,
)


def synth_features(n: int = 4000, seed: int = 7) -> DrawFeatures:
    rng = np.random.default_rng(seed)
    hg = rng.poisson(3.1, n)
    ag = rng.poisson(2.8, n)
    tie = hg == ag
    ot_goal = tie & (rng.random(n) < 0.6)
    so = tie & ~ot_goal
    home_extra = tie & (rng.random(n) < 0.52)
    hg_ns = hg + (ot_goal & home_extra)
    ag_ns = ag + (ot_goal & ~home_extra)
    hf = hg + (tie & home_extra)
    af = ag + (tie & ~home_extra)
    hnet = rng.poisson(27, n) + ag
    anet = rng.poisson(29, n) + hg
    hpp = rng.binomial(hg_ns, 0.2)
    app = rng.binomial(ag_ns, 0.2)
    hen = rng.binomial(hg_ns, 0.05)
    aen = rng.binomial(ag_ns, 0.05)
    first = np.where(hg_ns + ag_ns == 0, 0, np.where(rng.random(n) < 0.52, 1, -1)).astype(np.int8)
    return DrawFeatures("HOM", "AWY", 1, 2, hg_ns, ag_ns, hf, af, hg, ag, tie, so, hnet, anet, hpp, app, hen, aen, first,
                        rng.integers(0, 3, n), rng.integers(0, 3, n), rng.random(n) < 0.5, hnet - ag, anet - hg)


def mk_bet(bid: str, y: np.ndarray, price: int, family: str = "game_winner", team: str | None = None) -> Bet:
    return Bet(bid, bid.split("|")[0], bid.split("|")[-1] if "|" in bid else "yes", bid, family, "G1", y.astype(bool), float(y.mean()), price,
               fee_per_contract_dollars(price, DEFAULT_SCHEDULE), price / 100.0, team)


# ------------------------------------------------------------------------------------------------ scripts
def test_script_assignment_is_deterministic_and_partitions_draws():
    f = synth_features()
    a, b = primary_labels(f), primary_labels(f)
    assert np.array_equal(a, b)
    assert a.min() >= 0 and a.max() < N_PRIMARY
    d = build_distribution(f)
    assert d.freq.sum() == pytest.approx(1.0, abs=1e-12)
    assert sum(s["frequency"] for s in d.summaries) == pytest.approx(1.0, abs=1e-3)
    for dim in ("shot_control", "environment", "margin", "shape"):
        assert sum(d.dims[dim].values()) == pytest.approx(1.0, abs=1e-3)


def test_script_rules_on_hand_built_games():
    # one draw per row: (home goals, away goals, home net faced, away net faced, ot)
    rows = [(2, 1, 20, 35, False), (5, 4, 30, 30, False), (1, 1, 34, 22, True), (6, 0, 25, 25, False)]
    n = len(rows)
    hg = np.array([r[0] for r in rows])
    ag = np.array([r[1] for r in rows])
    ot = np.array([r[4] for r in rows])
    hf = hg + ot
    z = np.zeros(n, dtype=np.int64)
    f = DrawFeatures("H", "A", 1, 2, hg + ot, ag, hf, ag, hg, ag, ot, np.zeros(n, bool), np.array([r[2] for r in rows]), np.array([r[3] for r in rows]),
                     z, z, z, z, np.ones(n, np.int8), z, z, np.ones(n, bool))
    # row 0: home shots 35 vs away 20 -> home control; 3 goals -> low; 1-goal -> tight
    assert control_labels(f).tolist() == [0, 1, 2, 1]
    assert env_labels(f).tolist() == [0, 2, 0, 1]
    assert margin_labels(f).tolist() == [0, 0, 0, 1]
    tags = overlay_tags(f)
    assert tags["GOALIE_STEAL_H"].tolist() == [False, False, True, False]  # row 2: home wins in OT while out-shot 22-34
    assert tags["NET_VOLUME_HIGH_H"].tolist() == [False, False, True, False]


def test_actual_game_features_match_simulation_semantics():
    res = {"home_team_id": 1, "away_team_id": 2, "home_final": 3, "away_final": 2, "home_reg": 2, "away_reg": 2, "last_period_type": "OT"}
    goals = [{"team_id": 2, "period": 1, "period_type": "REG", "t_s": 300, "strength": "EV", "empty_net": False},
             {"team_id": 2, "period": 2, "period_type": "REG", "t_s": 1500, "strength": "PP", "empty_net": False},
             {"team_id": 1, "period": 3, "period_type": "REG", "t_s": 3000, "strength": "EV", "empty_net": False},
             {"team_id": 1, "period": 3, "period_type": "REG", "t_s": 3550, "strength": "EV", "empty_net": False},
             {"team_id": 1, "period": 4, "period_type": "OT", "t_s": 3700, "strength": "EV", "empty_net": False}]
    goalies = [{"team_id": 1, "shots_against": 30, "saves": 28, "starter": True}, {"team_id": 2, "shots_against": 25, "saves": 22, "starter": True}]
    f = DrawFeatures.from_actual(res, goals, goalies, "H", "A")
    assert f.home_goals[0] == 3 and f.away_goals[0] == 2 and f.ot[0] and not f.so[0]
    assert f.home_max_deficit[0] == 2 and f.away_max_deficit[0] == 0
    assert f.first_team[0] == -1 and f.away_pp[0] == 1
    assert bool(f.tight_late[0])  # 1-2 at 55:00
    ev = {e.key: bool(e.mask[0]) for e in thesis_events(f)}
    assert ev["H:WINS"] and ev["H:COMEBACK"] and ev["GAME:OVERTIME"] and ev["GAME:TIGHT"] and not ev["A:WINS"]


# ------------------------------------------------------------------------------------------------ mapping
def test_bet_to_script_contributions_reconcile_to_unconditional_probability():
    f = synth_features()
    d = build_distribution(f)
    events = thesis_events(f)
    em = EventMatrix.build(events)
    Y = np.stack([f.winner == 1, f.total >= 7, f.home_goals >= 4, f.away_net_faced <= 25])
    C = script_counts(Y, d)
    for i in range(len(Y)):
        assert C[i].sum() == int(Y[i].sum())  # exact integer reconciliation
    PHI, PAB, PB = associations(Y, em)
    bets = [mk_bet(f"b{i}|yes", Y[i], 50) for i in range(len(Y))]
    prof = thesis_profile(0, bets[0], C, d, em, PHI, PAB)
    assert prof["primary_thesis"]["key"] == "HOM:WINS" and prof["primary_thesis"]["phi"] == pytest.approx(1.0)
    pt = prof["primary_thesis"]
    assert pt["p_bet_given_thesis"] == pytest.approx(1.0)
    c = concentration(C[0], d.freq)
    assert 0 < c["top1"] <= c["top2"] <= 1 and c["breadth_eff"] >= 1


def test_script_neutral_bet_has_relative_breadth_near_one_and_narrow_bet_below():
    f = synth_features(20000)
    d = build_distribution(f)
    rng = np.random.default_rng(1)
    neutral = rng.random(f.n) < 0.4  # independent of the game
    narrow = (f.total >= 8) & (f.home_goals >= 5)
    C = script_counts(np.stack([neutral, narrow]), d)
    assert concentration(C[0], d.freq)["breadth_rel"] == pytest.approx(1.0, abs=0.05)
    assert concentration(C[1], d.freq)["breadth_rel"] < 0.5


# ------------------------------------------------------------------------------------------------ joint
def test_joint_identities_and_labels():
    f = synth_features(20000)
    rng = np.random.default_rng(3)
    ml = f.winner == 1
    pl = f.final_margin >= 2  # nested inside ml
    away = f.winner == -1  # mutually exclusive with ml
    noise = rng.random(f.n) < 0.3
    jm = joint_matrix([mk_bet("ml|yes", ml, 50), mk_bet("pl|yes", pl, 30), mk_bet("away|yes", away, 50), mk_bet("noise|yes", noise, 25)])
    lab = {(p["a"], p["b"]): p["relationship"] for p in jm["pairs"]}
    for p in jm["pairs"]:
        assert not check_identities(p), p
        assert p["p_a_and_b"] <= min(p["p_a"], p["p_b"]) + 1e-9
    assert lab[("ml|yes", "pl|yes")] == DUPLICATIVE  # P(ml | pl) = 1
    assert lab[("ml|yes", "away|yes")] == PARTIALLY_CONTRADICTORY
    assert lab[("ml|yes", "noise|yes")] == MOSTLY_INDEPENDENT
    over = f.total >= 7
    team_over = f.home_goals >= 4
    jm2 = joint_matrix([mk_bet("over|yes", over, 50), mk_bet("tt|yes", team_over, 40)])
    assert jm2["pairs"][0]["relationship"] in (REINFORCING, DUPLICATIVE)


# ------------------------------------------------------------------------------------------------ portfolio
def test_portfolio_profit_is_computed_exactly_on_synthetic_draws():
    y1 = np.array([1, 0, 1, 0], bool)
    y2 = np.array([0, 0, 1, 1], bool)
    b1, b2 = mk_bet("a|yes", y1, 40), mk_bet("b|yes", y2, 60)
    f = np.array([0.01, 0.02])
    x = pnl([b1, b2], f, 1000.0)
    exp = 10 * (y1 - b1.cost) / b1.cost + 20 * (y2 - b2.cost) / b2.cost
    assert np.allclose(x, exp)


def test_single_bet_optimizer_matches_closed_form_kelly():
    rng = np.random.default_rng(5)
    y = rng.random(200000) < 0.55
    b = mk_bet("x|yes", y, 50)
    R = returns([b])
    f = kelly_optimize(R, 1.0, [], 600)
    assert f[0] == pytest.approx(kelly_fraction(b.p, 50, DEFAULT_SCHEDULE), abs=2e-3)


def test_duplicative_bets_share_budget_and_diversifiers_are_kept():
    f = synth_features(20000)
    cfg = PortfolioConfig()
    ml = f.winner == 1
    pl = f.final_margin >= 2
    # duplicative pair priced +EV: joint stake respects the shared thesis budget
    bml, bpl = mk_bet("ml|yes", ml, int(ml.mean() * 100) - 6), mk_bet("pl|yes", pl, int(pl.mean() * 100) - 6)
    padj = {bml.bet_id: bml.p, bpl.bet_id: bpl.p}
    st = optimize_game([bml, bpl], padj, {bml.bet_id: "HOM:WINS", bpl.bet_id: "HOM:WINS"}, [], cfg)
    assert st.sum() <= cfg.max_thesis_frac + 1e-9
    # two +EV bets on disjoint scripts (home wins / away wins big): intentional diversifier
    away_big = f.final_margin <= -2
    a = mk_bet("hw|yes", ml, int(ml.mean() * 100) - 6)
    b = mk_bet("ab|yes", away_big, max(int(away_big.mean() * 100) - 6, 2))
    ok, info = pair_is_diversifier(a, b, {a.bet_id: a.p, b.bet_id: b.p}, cfg)
    assert ok, info


def test_no_negative_ev_hedge_is_ever_staked():
    f = synth_features(20000)
    cfg = PortfolioConfig()
    ml = f.winner == 1
    away = f.winner == -1
    good = mk_bet("ml|yes", ml, int(ml.mean() * 100) - 6)  # +EV
    hedge = mk_bet("away|yes", away, int(away.mean() * 100) + 4)  # -EV insurance that would raise P(profit)
    st = optimize_game([good, hedge], {good.bet_id: good.p, hedge.bet_id: hedge.p}, {}, [], cfg)
    assert st[1] == 0.0 and st[0] > 0
    m = metrics([good, hedge], st, cfg)
    assert m["expected_profit"] > 0


def test_confidence_haircut_reduces_stake_and_can_zero_it():
    f = synth_features(20000)
    cfg = PortfolioConfig()
    ml = f.winner == 1
    b = mk_bet("ml|yes", ml, int(ml.mean() * 100) - 3)
    full = optimize_game([b], {b.bet_id: b.p}, {}, [], cfg)
    half = optimize_game([b], {b.bet_id: b.p - 0.015}, {}, [], cfg)
    none = optimize_game([b], {b.bet_id: b.p - 0.05}, {}, [], cfg)
    assert full[0] >= half[0] and none[0] == 0.0


def test_independent_baseline_ignores_joint_structure():
    f = synth_features(20000)
    cfg = PortfolioConfig()
    ml = f.winner == 1
    bets = [mk_bet(f"ml{i}|yes", ml, int(ml.mean() * 100) - 6) for i in range(3)]  # the same event three times
    naive = independent_stakes(bets, cfg)
    joint = optimize_game(bets, {b.bet_id: b.p for b in bets}, {b.bet_id: "HOM:WINS" for b in bets}, [], cfg)
    assert naive.sum() > joint.sum()  # the naive card triples the same risk; the joint one shares one budget


def test_model_audit_attribution_reconciles_on_the_held_out_file():
    from nhl_edge.research.thesis_model_audit import WF, attribution_walk_forward

    if not (WF / "skaters_2025.parquet").exists():
        pytest.skip("walk-forward skater file not present")
    a = attribution_walk_forward()
    exp = sum(r["goals_expected_given_G"] for r in a["by_predicted_share"])
    act = sum(r["goals_actual"] for r in a["by_predicted_share"])
    assert exp == pytest.approx(act, rel=1e-3)  # allocation given realised team goals conserves goals by construction
    assert 0.8 < a["high_share_ratio"] < 1.25
