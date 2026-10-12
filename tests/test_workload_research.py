"""WORKLOAD_V1 research: point-in-time feature sums, OT timeline repair, count-forecast scoring, decomposition
identities, starter heuristic, fidelity to the production template, and the sports-only input guarantee. No network."""

from __future__ import annotations

import ast
import inspect
from pathlib import Path

import numpy as np
import pandas as pd

from nhl_edge.research import workload_audit as A
from nhl_edge.research import workload_eval as E
from nhl_edge.research import workload_experiment as X
from nhl_edge.research import workload_v1 as W

SRC = Path(__file__).resolve().parents[1] / "src" / "nhl_edge"


def test_ew_prior_sums_never_include_the_row_itself_and_reset_by_group():
    g = np.array([1, 1, 1, 2, 2])
    x = np.array([[1.0], [2.0], [4.0], [8.0], [16.0]])
    s = W.ew_prior_sums(g, x, half_life=1.0)  # decay 0.5 per game
    assert s[:, 0].tolist() == [0.0, 1.0, 0.5 * 1.0 + 2.0, 0.0, 8.0]


def test_ew_prior_sums_nan_contributes_nothing_but_decay_advances():
    s = W.ew_prior_sums(np.array([1, 1, 1]), np.array([[1.0], [np.nan], [0.0]]), half_life=1.0)
    assert s[:, 0].tolist() == [0.0, 1.0, 0.5]


def test_ew_prior_sums_vectorised_matches_the_reference_loop():
    rng = np.random.default_rng(7)
    g = np.sort(rng.integers(0, 40, 3000))
    x = rng.random((3000, 3))
    x[rng.random((3000, 3)) < 0.1] = np.nan
    for hl in (1.0, 4.0, 60.0):
        d = 0.5 ** (1.0 / hl)
        ref = np.zeros_like(x)
        acc = np.zeros(3)
        for i in range(len(x)):
            if i == 0 or g[i] != g[i - 1]:
                acc[:] = 0.0
            ref[i] = acc
            acc = d * acc + np.nan_to_num(x[i])
        assert np.allclose(W.ew_prior_sums(g, x, hl), ref, rtol=1e-10, atol=1e-12)


def test_league_prior_mean_is_strictly_before_the_date():
    d = np.array([1, 1, 2, 3])
    v = np.array([10.0, 20.0, 30.0, 40.0])
    m = W.league_prior_mean(d, v, np.array([1, 2, 3, 4]), window=2)
    assert np.isnan(m[0])
    assert m[1:].tolist() == [15.0, 25.0, 35.0]


def test_ot_lengths_use_winner_clock_or_shootout():
    ts = pd.DataFrame({"game_id": [1, 1, 2, 2, 3, 3], "game_type": 2, "n_seconds": [4800, 4800, 4800, 4800, 3600, 3600]})
    goals = pd.DataFrame({"game_id": [1, 3], "period": [4, 2], "t_s": [3600 + 125, 2000], "game_type": 2})
    L = W.ot_lengths(goals, ts)
    assert L.to_dict() == {1: 125.0, 2: 300.0}


def _toy_team_states():
    # game 10 regulation, game 11 went to OT and its timeline was stretched to 80:00 with phantom PP time
    return pd.DataFrame({"game_id": [10, 10, 11, 11], "home_team_id": [1, 1, 1, 1], "away_team_id": [2, 2, 2, 2], "season": 2024, "game_type": 2,
                         "game_date": ["2024-10-10", "2024-10-10", "2024-10-12", "2024-10-12"], "team_id": [1, 2, 1, 2], "is_home": [True, False, True, False],
                         "sec_ev": [3000, 3000, 3000, 3000], "sec_pp": [300, 240, 1500, 240], "sec_sh": [240, 300, 240, 1500], "sec_ea": [30, 30, 30, 30],
                         "sec_en": [30, 30, 30, 30], "sec_unknown": 0, "n_seconds": [3600, 3600, 4800, 4800]})


def test_repair_ot_timeline_removes_the_phantom_from_the_inflated_state():
    ts = pd.DataFrame({"game_id": [11], "team_id": [1], "game_type": [2], "n_seconds": [4800], "ot_len": [100.0], "sec_ev": [3000], "sec_pp": [1500],
                       "sec_sh": [240], "sec_ea": [30], "sec_en": [30]})
    pres = pd.DataFrame({"game_id": [11], "team_id": [1], "p_ev": [5 * 2950.0], "p_pp": [5 * 400.0], "p_sh": [4 * 240.0], "p_ea": [6 * 30.0], "p_en": [5 * 30.0]})
    r = W.repair_ot_timeline(ts, pres).iloc[0]
    assert r["repaired"] and r["sec_pp"] == 400 and r["sec_ev"] == 3000
    assert r[["sec_ev", "sec_pp", "sec_sh", "sec_ea", "sec_en"]].sum() == 3600 + 100


def test_skater_table_splits_overtime_minutes_and_shots():
    ts = _toy_team_states()
    shots = pd.DataFrame({"game_id": [11], "home_team_id": [1], "away_team_id": [2], "season": 2024, "game_type": 2, "period": [4], "t_s": [3650], "team_id": [1],
                          "is_home": [True], "shooter_id": [7], "kind": ["SOG"], "strength": ["EV"]})
    goals = pd.DataFrame({"game_id": [11], "period": [4], "t_s": [3700], "game_type": 2})
    pl = pd.DataFrame({"game_id": [10, 11], "season": 2024, "game_type": 2, "game_date": ["2024-10-10", "2024-10-12"], "player_id": 7, "team_id": 1, "is_home": True,
                       "position": "C", "sog": [2, 3], "toi_s": [1100, 1300], "toi_ev_s": [900.0, 1000.0], "toi_pp_s": [150.0, 200.0], "toi_sh_s": [50.0, 0.0],
                       "toi_ea_s": [0.0, 0.0], "toi_en_s": [0.0, 0.0], "toi_ot_s": [0.0, 60.0], "sog_ev": [2, 3], "sog_pp": [0, 0], "sog_sh": [0, 0], "sog_ea": [0, 0],
                       "sog_en": [0, 0], "shifts_ok": True})
    tg = W.team_games(pl, ts, shots, goals)
    sk = W.skater_table(pl, tg, shots)
    r10, r11 = sk.iloc[0], sk.iloc[1]
    assert r10["share_ok"] and r10["T_pp"] == 300
    assert r11["T_ot"] == 100.0 and r11["t_ot"] == 60.0
    assert r11["t_evreg"] == 940.0 and r11["s_evreg"] == 2 and r11["s_ot"] == 1


def test_pmfs_sum_to_one_and_have_the_right_mean():
    mu = np.array([0.3, 1.7, 4.0])
    for p in (E.poisson_pmf(mu, 40), E.nb_pmf(mu, 0.2, 60)):
        assert np.allclose(p.sum(axis=1), 1.0)
        assert np.allclose(E.pmf_mean(p), mu, atol=1e-3)
    sa = E.nb_pmf(np.array([28.0]), 0.02, 90)
    sv = E.binomial_mixture_pmf(sa, np.array([0.9]), 80)
    assert abs(sv.sum() - 1) < 1e-9
    assert abs(E.pmf_mean(sv)[0] - 0.9 * E.pmf_mean(sa)[0]) < 1e-3


def test_crps_matches_brute_force_and_coverage_is_nominal_when_calibrated():
    rng = np.random.default_rng(0)
    p = E.poisson_pmf(np.full(20000, 1.6), 20)
    y = rng.poisson(1.6, 20000)
    F = np.cumsum(p[0])
    brute = sum((F[k] - (y[0] <= k)) ** 2 for k in range(20))
    assert abs(E.crps_rows(p[:1], y[:1])[0] - brute) < 1e-12
    assert abs(E.pit_coverage_rows(p, y, 0.8).mean() - 0.8) < 0.01
    assert abs(E.pit_coverage_rows(p, y, 0.5).mean() - 0.5) < 0.01
    # an over-confident forecast under-covers
    narrow = E.poisson_pmf(np.full(20000, 1.6), 20)
    y_wide = rng.negative_binomial(1.0, 1.0 / (1.0 + 1.6), 20000)
    assert E.pit_coverage_rows(narrow, y_wide, 0.8).mean() < 0.75


def test_bootstrap_of_identical_arms_is_zero_and_detects_a_real_gain():
    rng = np.random.default_rng(1)
    gid = np.repeat(np.arange(200), 10)
    y = rng.poisson(2.0, len(gid))
    good = E.score_arm(E.poisson_pmf(np.full(len(y), 2.0), 20), y, [1, 2, 3])
    bad = E.score_arm(E.poisson_pmf(np.full(len(y), 3.0), 20), y, [1, 2, 3])
    same = E.bootstrap_diff(gid, good, good, n_boot=200)
    assert same["crps"]["diff"] == 0 and same["crps"]["ci95"] == [0.0, 0.0]
    d = E.bootstrap_diff(gid, good, bad, n_boot=200)
    assert d["crps"]["ci95"][1] < 0 and d["rmse"]["ci95"][1] < 0 and d["n_games"] == 200


def _toy_champion_skaters(n=50, seed=3):
    rng = np.random.default_rng(seed)
    d = pd.DataFrame({"game_id": np.repeat(np.arange(n // 5), 5), "team_id": 1, "pos": "F", "shifts_ok": True, "game_ot": False})
    for s in A.SOG_STATES:
        d[f"y_toi_{s}"] = rng.uniform(1, 15, n)
        d[f"ch_toi_{s}"] = d[f"y_toi_{s}"] + rng.normal(0, 1, n)
        d[f"ch_rate_{s}"] = rng.uniform(3, 9, n)
        d[f"sog_{s}"] = rng.poisson(1.0, n)
    d["y_toi_ot"] = 0.0
    d["ch_toi_ot"] = 0.0
    d["sog_ot"] = 0
    d["sog_ea"] = rng.poisson(0.1, n)
    d["sog_en"] = 0
    d["y_sog"] = (d["sog_ev"] + d["sog_pp"] + d["sog_sh"] + d["sog_ea"]).astype(float)
    d["ch_sog"] = sum(d[f"ch_toi_{s}"] * d[f"ch_rate_{s}"] for s in A.SOG_STATES) / 60.0
    d["ch_toi"] = d[[f"ch_toi_{s}" for s in A.SOG_STATES]].sum(axis=1)
    d["y_toi"] = d[[f"y_toi_{s}" for s in A.SOG_STATES]].sum(axis=1)
    d["team_pp_min"] = 4.4
    return d


def test_skater_decomposition_components_add_up_to_the_total_error():
    d = _toy_champion_skaters()
    r = A.skater_decomposition(d)
    assert abs(r["total"]["bias"] - (r["workload_component"]["bias"] + r["efficiency_component"]["bias"] + r["omitted_states_component"]["bias"])) < 1e-12
    # oracle minutes remove exactly the workload component
    assert abs(r["oracle_toi_total_error"]["bias"] - (r["total"]["bias"] - r["workload_component"]["bias"])) < 1e-12


def test_goalie_decomposition_components_add_up():
    rng = np.random.default_rng(4)
    n = 40
    g = pd.DataFrame({"game_id": np.repeat(np.arange(n // 2), 2), "ch_faced_starter": rng.uniform(22, 34, n), "y_sa": rng.integers(15, 40, n),
                      "expected_faced": 29.0, "y_net_sa": rng.integers(15, 40, n), "y_replaced": False, "ch_p_replaced": 0.05, "game_ot": False, "p_ot": 0.22})
    g["ch_saves"] = g["ch_faced_starter"] * 0.9
    g["y_saves"] = (g["y_sa"] * 0.9).round()
    r = A.goalie_decomposition(g)
    assert abs(r["total"]["bias"] - (r["workload_component"]["bias"] + r["efficiency_component"]["bias"])) < 1e-12


def test_starter_heuristic_uses_only_earlier_games():
    rows = []
    for i, (pid, day) in enumerate([(30, 1), (30, 3), (30, 5), (31, 6), (30, 8)]):
        rows.append({"game_id": 100 + i, "team_id": 1, "season": 2024, "game_type": 2, "game_date": f"2024-10-{day:02d}", "player_id": pid, "starter": True})
    h = A.starter_heuristic(pd.DataFrame(rows), 2024, window=10)
    # game on day 6 is the 2nd night of a back-to-back after 30 started day 5: the rule rotates only if another goalie
    # has appeared before, which he has not -> picks 30 (wrong); day 8: leader 30 (right)
    assert h["heuristic_id"].tolist() == [30, 30, 30, 30]
    assert h["actual_id"].tolist() == [30, 30, 31, 30]
    assert h.loc[h["game_id"] == 103, "b2b"].item()


def test_production_team_minutes_match_the_shadow_workflow_verbatim():
    src = (SRC / "workflows" / "shadow_player.py").read_text()
    assert 'team_min = {"ev": 50.6, "pp": 4.4 * p_pp / 0.215, "sh": 4.4, "ea": 0.6, "en": 0.6, "ot": 1.2}' in src
    assert A.production_team_minutes(0.215) == {"ev": 50.6, "pp": 4.4, "sh": 4.4, "ea": 0.6, "en": 0.6, "ot": 1.2}


def test_workload_modules_take_no_market_inputs():
    """Sports-only: none of the research modules may import Kalshi / execution / pricing code or read market fields."""
    for mod in (W, E, A, X):
        tree = ast.parse(inspect.getsource(mod))
        names = [n.module or "" for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)] + \
                [a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names]
        assert not any(k in nm for nm in names for k in ("kalshi", "execution", "pricing", "economics", "market")), (mod.__name__, names)
    for mod in (W, E):
        src = inspect.getsource(mod).lower()
        for tok in ("yes_ask", "yes_bid", "p_market", "moneyline", "odds"):
            assert tok not in src, (mod.__name__, tok)


def test_acceptance_rule_requires_every_check():
    good = {"diff": -0.01, "ci95": [-0.02, -0.001]}
    rep = {"diffs": {"WORKLOAD_V1_minus_CHAMPION": {"crps": good, "rmse": good, "ladder_brier": good},
                     "WORKLOAD_V1_minus_CHAMPION_NB": {"crps": good, "rmse": good, "ladder_brier": good}},
           "arms": {"WORKLOAD_V1": {"bias": 0.01, "coverage80": 0.80}},
           "subgroups": {"F": {"WORKLOAD_V1": {"crps": 1.0}, "CHAMPION_NB": {"crps": 1.1}}, "D": {"WORKLOAD_V1": {"crps": 1.0}, "CHAMPION_NB": {"crps": 1.1}}}}
    rule = {"max_abs_bias_sog": 0.05, "coverage80_band": [0.77, 0.83], "max_abs_bias_saves": 0.5}
    assert X.accept_skaters(rep, rule)["verdict"] == "ACCEPTED"
    rep["diffs"]["WORKLOAD_V1_minus_CHAMPION_NB"]["crps"] = {"diff": -0.01, "ci95": [-0.02, 0.0001]}
    assert X.accept_skaters(rep, rule)["verdict"] == "REJECTED"
