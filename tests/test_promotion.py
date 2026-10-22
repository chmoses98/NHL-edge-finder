from __future__ import annotations

import numpy as np

from nhl_edge.research.oa_evaluate import compare, evaluate_run
from nhl_edge.research.promotion import score_challenger


def _row(delta, lo, hi, slo=None, shi=None, metric="brier_win", challenger="C"):
    slo = lo if slo is None else slo
    shi = hi if shi is None else shi
    return {"challenger": challenger, "metric": metric, "delta": delta, "lo95": lo, "hi95": hi, "lo95_slate": slo, "hi95_slate": shi,
            "better_game_ci": hi < 0, "worse_game_ci": lo > 0, "better_slate_ci": shi < 0, "worse_slate_ci": slo > 0}


def _card(pooled, seasons, exposed=None, **kw):
    return score_challenger(target="win", challenger="C", incumbent="V1", primary_metric="brier_win", pooled_unexposed=pooled, by_season_unexposed=seasons,
                            exposed=exposed or {}, n_unexposed_games=kw.pop("n", 6000), **kw)


def test_clear_win_is_only_a_candidate_until_live_gates_clear():
    good = [_row(-0.0020, -0.0030, -0.0010)]
    seasons = {str(s): [_row(-0.002, -0.004, 0.0)] for s in (2021, 2022, 2023)}
    sc = _card(good, seasons, inference_seconds=30, reproducible=True, contract_compatible=True)
    assert sc.verdict == "SHADOW_MORE"   # G10 needs live shadow games
    sc = _card(good, seasons, inference_seconds=30, reproducible=True, contract_compatible=True, live_non_inferior=True)
    assert sc.verdict == "PROMOTE_CANDIDATE"


def test_small_or_insignificant_gain_is_retained():
    seasons = {str(s): [_row(-0.001, -0.004, 0.002)] for s in (2021, 2022, 2023)}
    assert _card([_row(-0.0004, -0.0012, 0.0004)], seasons).verdict == "RETAIN_INCUMBENT"          # CI spans zero
    assert _card([_row(-0.0006, -0.0010, -0.0002)], seasons).verdict == "RETAIN_INCUMBENT"          # significant but below the practical threshold


def test_date_cluster_interval_must_also_exclude_zero():
    pooled = [_row(-0.002, -0.003, -0.001, slo=-0.004, shi=0.0005)]
    seasons = {str(s): [_row(-0.002, -0.004, 0.0)] for s in (2021, 2022, 2023)}
    sc = _card(pooled, seasons)
    assert next(g for g in sc.gates if g.gate == "G1_primary_improvement").passed is False


def test_regression_elsewhere_and_unstable_seasons_block_promotion():
    pooled = [_row(-0.002, -0.003, -0.001), _row(0.004, 0.001, 0.009, metric="rps_total")]
    seasons = {str(s): [_row(-0.002, -0.004, 0.0)] for s in (2021, 2022, 2023)}
    sc = _card(pooled, seasons, secondary_metrics=("rps_total",))
    assert next(g for g in sc.gates if g.gate == "G3_no_material_regression").passed is False
    seasons["2022"] = [_row(0.003, 0.001, 0.005)]
    sc = _card(pooled[:1], seasons)
    assert next(g for g in sc.gates if g.gate == "G6_season_stability").passed is False


def test_too_little_evidence_is_retained():
    assert _card([_row(-0.002, -0.003, -0.001)], {"2023": [_row(-0.002, -0.004, 0.0)]}).verdict == "RETAIN_INCUMBENT"


def test_contradicting_exposed_season_blocks():
    seasons = {str(s): [_row(-0.002, -0.004, 0.0)] for s in (2021, 2022, 2023)}
    sc = _card([_row(-0.002, -0.003, -0.001)], seasons, exposed={"2025": [_row(0.003, 0.001, 0.005)]})
    assert next(g for g in sc.gates if g.gate == "G6b_exposed_not_contradicting").passed is False


def test_compare_detects_a_planted_effect_and_not_noise():
    rng = np.random.default_rng(1)
    n = 2000
    base = rng.normal(0.25, 0.05, n)
    clusters = np.repeat(np.arange(n // 5), 5)
    losses = {"V1": {"brier_win": base}, "good": {"brier_win": base - 0.003 + rng.normal(0, 0.001, n)}, "noise": {"brier_win": base + rng.normal(0, 0.02, n)}}
    rows = {r["challenger"]: r for r in compare(losses, "V1", ["good", "noise"], clusters, ("brier_win",), n_boot=500)}
    assert rows["good"]["better_game_ci"] and rows["good"]["practically_meaningful"]
    assert not rows["noise"]["better_game_ci"] and not rows["noise"]["practically_meaningful"]


def test_evaluate_run_end_to_end_on_tiny_synthetic_run(tmp_path):
    import pandas as pd

    rng = np.random.default_rng(2)
    n, k = 60, 20
    arms = ["V1", "A", "LEAGUE"]
    rows = {"game_id": range(n), "season": [2023] * 30 + [2024] * 30, "game_date": [f"2023-11-{1 + i // 3:02d}" for i in range(n)],
            "y_home_win": rng.integers(0, 2, n), "y_overtime": rng.integers(0, 2, n), "home_score": rng.integers(0, 6, n), "away_score": rng.integers(0, 6, n)}
    rows["y_total"] = rows["home_score"] + rows["away_score"]
    for a in arms:
        rows[f"{a}_p_home_win"] = rng.uniform(0.3, 0.7, n)
        rows[f"{a}_p_overtime"] = rng.uniform(0.1, 0.3, n)
        rows[f"{a}_expected_total"] = rng.uniform(5, 7, n)
        rows[f"{a}_p_over_5.5"] = rng.uniform(0.3, 0.7, n)
        rows[f"{a}_p_over_6.5"] = rng.uniform(0.3, 0.7, n)
    pd.DataFrame(rows).to_csv(tmp_path / "g.csv", index=False)
    tot = rng.dirichlet(np.ones(k), size=(n, len(arms)))
    mar = rng.dirichlet(np.ones(21), size=(n, len(arms)))
    np.savez(tmp_path / "p.npz", total=tot, margin=mar, arms=np.array(arms))
    res = evaluate_run(tmp_path / "g.csv", tmp_path / "p.npz")
    assert res["n_games"] == n and set(res["by_season"]) == {"2023", "2024"} and len(res["pooled"]["paired_vs_incumbent"]) == 2 * 8
