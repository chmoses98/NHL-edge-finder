"""WORKLOAD_V1 replication harness: which seasons can be held out, the stand-in context, no market inputs. No network."""

from __future__ import annotations

import ast
import inspect

import numpy as np
import pandas as pd

from nhl_edge.research import workload_experiment as X
from nhl_edge.research import workload_replication as R


def test_only_seasons_with_two_prior_seasons_and_a_champion_dispersion_season_are_feasible():
    f = R.feasible_holdouts()
    assert [s for s, v in f.items() if v["feasible"]] == [2023, 2024, 2025]
    assert f[2023]["train_seasons"] == [2021, 2022] and f[2023]["dispersion_season"] == 2022
    assert not f[2022]["feasible"] and not f[2021]["feasible"]


def test_replication_module_takes_no_market_inputs():
    names = [n.module or "" for n in ast.walk(ast.parse(inspect.getsource(R))) if isinstance(n, ast.ImportFrom)]
    names += [a.name for n in ast.walk(ast.parse(inspect.getsource(R))) if isinstance(n, ast.Import) for a in n.names]
    assert not any(k in nm for nm in names for k in ("kalshi", "execution", "pricing", "economics", "market"))


def test_derived_wf_check_is_zero_on_identical_rows_and_detects_a_difference():
    cols = R.DERIVED_WF_COLS
    a = pd.DataFrame({c: [1.0, 2.0] for c in cols})
    assert max(v for k, v in R.check_derived_matches_committed(a, a).items() if k != "n_overlap") == 0.0
    b = a.copy()
    b["ppmin_home"] = [1.0, 2.5]
    assert R.check_derived_matches_committed(a, b)["ppmin_home"] == 0.5


def test_default_evaluate_path_is_still_pinned_to_the_preregistered_season():
    assert "evaluate runs only on the preregistered held-out season" in inspect.getsource(X.main)


def test_stable_league_rates_agree_with_the_research_function_when_dates_are_unique():
    from nhl_edge.research import workload_v1 as W

    n = 40
    rng = np.random.default_rng(3)
    sk = pd.DataFrame({"pos": ["F"] * n, "date_int": np.arange(n) + 20240101, "game_id": np.arange(n), "player_id": np.arange(n)})
    for s in W.STATES_W:
        sk[f"s_{s}"] = rng.integers(0, 4, n).astype(float)
        sk[f"t_{s}"] = rng.random(n) * 600 + 60
    a, b = W.league_rates(sk, 10), R._league_rates_stable(sk, 10)
    assert np.allclose(a.to_numpy(), b.to_numpy(), equal_nan=True)
