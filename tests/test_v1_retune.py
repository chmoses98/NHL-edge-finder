"""Retuned-V1 study: grid is the preregistered one, decision rules behave on planted effects, ablation switches default to V1 behaviour."""

from __future__ import annotations

import numpy as np
import pandas as pd

from nhl_edge.features.ratings import HALF_LIFE_GAMES, HOME_ADJ, PRIOR_GAMES
from nhl_edge.research import retune_evaluate as E
from nhl_edge.research import v1_retune as R


def test_grid_is_the_preregistered_one_and_contains_production_constants():
    assert R.GRID_PRIOR == (2.5, 5.0, 10.0, 20.0, 40.0, 80.0, 160.0) and R.GRID_HALF_LIFE == (10.0, 20.0, 40.0, 80.0, 160.0)
    assert min(R.GRID_PRIOR) < 10 and HALF_LIFE_GAMES in R.GRID_HALF_LIFE and PRIOR_GAMES in R.GRID_PRIOR and HOME_ADJ in R.GRID_HOME


def test_boundary_report_flags_a_binding_grid():
    sel = pd.DataFrame({"season": [2017, 2018, 2019], "half_life": [20.0, 160.0, 40.0], "prior": [2.5, 2.5, 10.0], "home_adj": [1.03, 1.03, 1.06]})
    rep = R.boundary_report(sel)
    assert rep["prior"]["at_lower_edge"] == [2017, 2018] and rep["half_life"]["at_upper_edge"] == [2018] and rep["home_adj"]["at_upper_edge"] == [2019]


def _losses(delta: float, n_seasons: int = 9, per: int = 400, seed: int = 0, noise: float = 0.05):
    rng = np.random.default_rng(seed)
    season = np.repeat(np.array(E.ALL_SEASONS[:n_seasons]), per)
    n = len(season)
    dates = np.array([f"{s}-{(i % 150) + 1:03d}" for s, i in zip(season, range(n), strict=True)])
    base = {m: rng.random(n) * 0.3 for m in ("brier_win", "rps_total", "brier_ot")}
    chall = {m: base[m] + (delta if m == "brier_win" else 0.0) + rng.normal(0, noise, n) for m in base}
    return {"inc": base, "chall": chall}, season, dates


def test_decide_marks_a_planted_gain_better_and_no_gain_not_better():
    losses, season, dates = _losses(-0.004)
    r = E.decide(losses, season, dates, "chall", "inc", ("brier_win",), E.PRACTICAL["brier_win"])
    assert r["BETTER"] and r["seasons_favourable"] >= 6 and r["no_primary_worse"]
    losses, season, dates = _losses(0.0)
    assert not E.decide(losses, season, dates, "chall", "inc", ("brier_win",), E.PRACTICAL["brier_win"])["BETTER"]


def test_decide_requires_the_practical_size_even_when_significant():
    losses, season, dates = _losses(-0.0004, per=3000, noise=0.01)
    r = E.decide(losses, season, dates, "chall", "inc", ("brier_win",), E.PRACTICAL["brier_win"])
    assert r["gate_ok"] and not r["size_ok"] and not r["BETTER"]


def test_decide_rejects_a_challenger_that_is_worse_on_a_primary_metric():
    losses, season, dates = _losses(-0.004)
    losses["chall"]["rps_total"] = losses["inc"]["rps_total"] + 0.02
    r = E.decide(losses, season, dates, "chall", "inc", ("brier_win",), E.PRACTICAL["brier_win"])
    assert not r["no_primary_worse"] and not r["BETTER"]


def test_ablation_switches_default_to_unchanged_v1(monkeypatch):
    """_lams(b2b=True, finish=True) must equal the pre-existing behaviour; switching a feature off must move the rate in the expected direction."""
    from nhl_edge.research import v1_tuned_control as T

    rows = []
    for gid, (d, h, a) in enumerate([("2024-10-01", "AAA", "BBB"), ("2024-10-02", "AAA", "CCC"), ("2024-10-03", "BBB", "CCC")], start=1):
        for team, opp, home in ((h, a, 1), (a, h, 0)):
            rows.append({"team": team, "opp": opp, "date_int": int(d.replace("-", "")), "season": 2024, "minutes": 60.0, "xGoalsFor": 3.0 if team == "AAA" else 2.0,
                         "xGoalsAgainst": 2.0, "goalsFor": 4 if team == "AAA" else 1, "goalsAgainst": 2, "home": home, "game_id": gid})
    log = pd.DataFrame(rows)
    logs = {t: d for t, d in log.groupby("team")}
    game = type("G", (), {"game_date": "2024-10-04", "season": 2024, "home_abbrev": "AAA", "away_abbrev": "BBB"})()
    base = T._lams(game, 20.0, 20.0, log, logs, {})
    assert base == T._lams(game, 20.0, 20.0, log, logs, {}, b2b=True, finish=True)
    nofin = T._lams(game, 20.0, 20.0, log, logs, {}, finish=False)
    assert nofin[0] < base[0]              # AAA out-finishes its xG in the log, so dropping the finishing ratio lowers its rate
