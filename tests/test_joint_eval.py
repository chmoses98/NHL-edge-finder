from __future__ import annotations

import numpy as np
import pytest

from nhl_edge.research import joint_eval as J
from nhl_edge.sim.engine import SimConfig, TeamParams, simulate_game


def test_cells_from_draws_follow_the_result_and_margin_definitions():
    # draws: reg home win by 1 | reg away win by 4 | OT home | OT away | SO home | SO away | reg home win by 2 with a high total
    hr = np.array([3, 1, 2, 2, 3, 3, 5])
    ar = np.array([2, 5, 2, 2, 3, 3, 3])
    ot = np.array([0, 0, 1, 1, 1, 1, 0])
    so = np.array([0, 0, 0, 0, 1, 1, 0])
    hf = np.array([3, 1, 3, 2, 4, 3, 5])
    af = np.array([2, 5, 2, 3, 3, 4, 3])
    pm, pt = J.cells_from_draws(hr, ar, ot, so, hf, af)
    names = list(J.MARGIN_CELLS)
    assert pm.sum() == pytest.approx(1.0) and pt.sum() == pytest.approx(1.0)
    for cell in ("REG_H_1", "REG_A_3+", "OT_H", "OT_A", "SO_H", "SO_A", "REG_H_2"):
        assert pm[names.index(cell)] == pytest.approx(1 / 7), cell
    # total cells: result type x bucket; the 8-goal regulation home win is REG_H|8+
    tn = list(J.total_cell_names())
    assert pt[tn.index("REG_H|8+")] == pytest.approx(1 / 7) and pt[tn.index("REG_A|6")] == pytest.approx(1 / 7)


def test_observed_cells_match_the_same_definitions():
    names, tn = list(J.MARGIN_CELLS), list(J.total_cell_names())
    assert names[J.observed_cells(4, 3, "REG")[0]] == "REG_H_1"
    assert names[J.observed_cells(1, 5, "REG")[0]] == "REG_A_3+"
    assert names[J.observed_cells(3, 2, "OT")[0]] == "OT_H" and names[J.observed_cells(2, 3, "OT")[0]] == "OT_A"
    assert names[J.observed_cells(3, 2, "SO")[0]] == "SO_H" and names[J.observed_cells(2, 3, "SO")[0]] == "SO_A"
    assert tn[J.observed_cells(3, 2, "OT")[1]] == "OT_H|5" and tn[J.observed_cells(1, 0, "REG")[1]] == "REG_H|<=3" and tn[J.observed_cells(6, 4, "REG")[1]] == "REG_H|8+"


def test_simulator_cells_are_coherent_with_the_marginals():
    res = simulate_game(TeamParams(0, "H", 3.2), TeamParams(0, "A", 2.9), seed=11, config=SimConfig(n_sims=20000))
    pm, pt = J.cells_from_result(res)
    names = list(J.MARGIN_CELLS)
    assert pm[names.index("OT_H"):].sum() == pytest.approx(res.p_overtime()[0], abs=1e-12)           # OT + SO mass == P(overtime)
    assert pm[names.index("SO_H"):].sum() == pytest.approx(res.p_shootout()[0], abs=1e-12)
    assert pm[:3].sum() + pm[names.index("OT_H")] + pm[names.index("SO_H")] == pytest.approx(res.p_win(True)[0], abs=1e-12)
    assert pt.reshape(6, 6).sum(axis=1)[0] == pytest.approx(res.p_reg_win(True)[0], abs=1e-12)


def test_scoring_rules_are_proper_and_floor_is_applied():
    p = np.array([[0.7, 0.2, 0.1], [0.1, 0.1, 0.8]])
    k = np.array([0, 2])
    assert J.brier_cat(p, k) == pytest.approx([0.09 + 0.04 + 0.01, 0.01 + 0.01 + 0.04])
    assert J.logscore_cat(p, k) == pytest.approx([-np.log(0.7), -np.log(0.8)])
    z = np.array([[1.0, 0.0, 0.0]])
    assert J.logscore_cat(z, np.array([1]))[0] == pytest.approx(-np.log(J.FLOOR))                         # never infinite
    # a calibrated forecast beats a miscalibrated one in expectation
    rng = np.random.default_rng(0)
    true = np.array([0.5, 0.3, 0.2])
    draw = rng.choice(3, size=20000, p=true)
    good = np.tile(true, (20000, 1))
    bad = np.tile([0.2, 0.3, 0.5], (20000, 1))
    assert J.brier_cat(good, draw).mean() < J.brier_cat(bad, draw).mean()
    assert J.logscore_cat(good, draw).mean() < J.logscore_cat(bad, draw).mean()


def test_reliability_and_ot_conditionals():
    p = np.tile(np.array([0.25, 0.25, 0.25, 0.25]), (400, 1))
    k = np.repeat(np.arange(4), 100)
    rel = J.cell_reliability(p, k, ("a", "b", "c", "d"))
    assert all(abs(r["z"]) < 1e-9 and r["expected"] == pytest.approx(100.0) for r in rel)
    pm = np.zeros((10, 10))
    pm[:, 0] = 0.7
    pm[:, 6] = 0.1
    pm[:, 7] = 0.1
    pm[:, 8] = 0.05
    pm[:, 9] = 0.05
    k_m = np.array([0, 0, 0, 0, 0, 0, 6, 8, 7, 0])
    c = J.overtime_conditionals(pm, k_m)
    assert c["pred_p_ot_or_so"] == pytest.approx(0.3) and c["obs_p_ot_or_so"] == pytest.approx(0.3)
    assert c["pred_p_so_given_tie"] == pytest.approx(1 / 3) and c["obs_p_so_given_tie"] == pytest.approx(1 / 3)


def test_walk_forward_v2_defaults_still_reproduce_the_published_season_ranges():
    from nhl_edge.research import walk_forward_v2 as W2

    assert W2.FIRST_SHOTS_SEASON == 2021 and W2.TRAIN_WINDOW is None
    assert W2.hazard_seasons(2025) == [2021, 2022, 2023, 2024] and W2.hazard_seasons(2023) == [2021, 2022]
    assert W2.hazard_seasons(2025, W2.FIRST_SHOTS_SEASON + 1) == [2022, 2023, 2024]            # the goalie back-to-back estimate used range(2022, S)
    assert W2.hazard_seasons(2015, first=2008, window=4) == [2011, 2012, 2013, 2014]            # the rolling window used by the joint study
    assert W2.hazard_seasons(2010, first=2008, window=4) == [2008, 2009]


def test_the_research_shot_seasons_are_not_where_production_reads_them():
    from pathlib import Path

    import nhl_edge.data.shots as S

    hist = Path(__file__).resolve().parents[1] / "data" / "history"
    prod = {int(p.stem.split("_")[1]) for p in (hist / "moneypuck").glob("shots_*.parquet")}
    assert prod <= {2021, 2022, 2023, 2024, 2025}                                              # production load_shots globs this folder only
    assert "shots_extension" not in str(S.load_shots.__code__.co_consts)
