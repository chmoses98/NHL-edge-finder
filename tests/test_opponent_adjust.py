"""Opponent adjustment (nhl-oppadj-1.0): recovers known effects on a synthetic schedule, never reads future games, keeps
raw numbers, regularises thin samples, and the walk-forward check runs on the committed history."""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pytest

from nhl_edge.features.opponent_adjust import MIN_ROWS, OPP_ADJ_VERSION, fit

REPO_DATA = Path(__file__).resolve().parents[1] / "data"


def synth_schedule(n_days: int = 150, seed: int = 1, teams: int = 12, season: int = 2025) -> tuple[list[dict], dict[int, float], dict[int, float]]:
    """Every day every team plays one game; true offense / defense effects known. Strong teams play weak teams more early
    (an unbalanced schedule), so raw rates are biased and the adjustment has something to remove."""
    rng = np.random.default_rng(seed)
    off = {t: float(v) for t, v in enumerate(rng.normal(0, 0.35, teams))}
    dfn = {t: float(v) for t, v in enumerate(rng.normal(0, 0.35, teams))}
    rows = []
    d0 = date(2025, 10, 1)
    order = sorted(range(teams), key=lambda t: -off[t])
    for k in range(n_days):
        day = (d0 + timedelta(days=k)).isoformat()
        perm = list(order) if k < 40 else list(rng.permutation(teams))
        if k < 40:  # unbalanced: best offense vs worst defense etc.
            perm = order[: teams // 2] + order[teams // 2:][::-1]
        for i in range(0, teams, 2):
            h, a = int(perm[i]), int(perm[i + 1])
            for t, o, home in ((h, a, True), (a, h, False)):
                rate = 2.5 + off[t] + dfn[o] + (0.05 if home else -0.05)
                toi = 2880.0
                xgf = max(0.05, rng.normal(rate, 0.6)) * toi / 3600.0
                orate = 2.5 + off[o] + dfn[t] + (0.05 if not home else -0.05)
                xga = max(0.05, rng.normal(orate, 0.6)) * toi / 3600.0
                rows.append({"team_id": t, "opp_team_id": o, "home": home, "date": day, "season": season, "situation": "5on5", "toi": toi,
                             "xgf": xgf, "xga": xga})
    return rows, off, dfn


def test_recovers_true_offense_and_defense_better_than_raw():
    rows, off, dfn = synth_schedule()
    f = fit(rows, as_of="2026-03-01", season=2025, metric="xg", ridge_hours=2.0, half_life_days=1e6)
    assert f.version == OPP_ADJ_VERSION and f.mu == pytest.approx(2.5, abs=0.1)
    adj_o = np.array([f.teams[t].off_adj - f.mu for t in off])
    raw_o = np.array([f.teams[t].off_raw - f.mu for t in off])
    true_o = np.array(list(off.values()))
    assert np.corrcoef(adj_o, true_o)[0, 1] > 0.93
    assert np.abs(adj_o - true_o).mean() < np.abs(raw_o - true_o).mean()
    adj_d = np.array([f.teams[t].def_adj - f.mu for t in dfn])
    assert np.corrcoef(adj_d, np.array(list(dfn.values())))[0, 1] > 0.93
    for a in f.teams.values():  # raw is kept beside adjusted and the schedule effect is their difference
        assert a.off_raw is not None and a.schedule_off == pytest.approx(a.off_raw - a.off_adj)


def test_point_in_time_future_games_never_change_the_fit():
    rows, _, _ = synth_schedule()
    cut = "2025-12-15"
    past = [r for r in rows if r["date"] < cut]
    a = fit(rows, as_of=cut, season=2025)
    b = fit(past, as_of=cut, season=2025)
    assert a.n_rows == b.n_rows == len(past)
    for t in a.teams:
        assert a.teams[t].off_adj == pytest.approx(b.teams[t].off_adj, abs=1e-12) and a.teams[t].def_adj == pytest.approx(b.teams[t].def_adj, abs=1e-12)
    # a game ON the cutoff date is not "before" it
    same_day = [r for r in rows if r["date"] == cut]
    assert same_day and fit(past + same_day, as_of=cut, season=2025).n_rows == len(past)


def test_ridge_shrinks_thin_samples_and_insufficient_teams_are_not_rated():
    rows, _, _ = synth_schedule(n_days=12)
    loose = fit(rows, as_of="2026-01-01", season=2025, ridge_hours=0.1)
    tight = fit(rows, as_of="2026-01-01", season=2025, ridge_hours=200.0)
    spread = lambda f: np.std([a.off_adj for a in f.teams.values() if a.off_adj is not None])  # noqa: E731
    assert spread(tight) < spread(loose)
    few, _, _ = synth_schedule(n_days=MIN_ROWS - 2)
    f = fit(few * 3, as_of="2026-01-01", season=2025)  # enough rows overall, but each team below MIN_ROWS distinct games is still rows-based
    assert all(a.status in ("OK", "PRIOR_HEAVY", "INSUFFICIENT") for a in f.teams.values())
    tiny = fit(few[:10], as_of="2026-01-01", season=2025)
    assert tiny.mu is None and not tiny.teams


def test_previous_seasons_outside_the_window_are_ignored():
    rows, _, _ = synth_schedule(season=2023)
    assert fit(rows, as_of="2026-03-01", season=2025).mu is None


@pytest.mark.skipif(not (REPO_DATA / "history" / "moneypuck").exists(), reason="history not present")
def test_walk_forward_check_runs_on_committed_history_and_beats_raw():
    from nhl_edge.research.opponent_adjust_eval import evaluate, load_rows

    rows = load_rows(REPO_DATA / "history")
    res = evaluate(rows, [2025], "xg", step_days=28)
    assert res["n_team_games"] > 1000 and res["checkpoints"] >= 5
    assert res["rate_wmse"]["adj"] < res["rate_wmse"]["league"]
    assert res["rate_wmse"]["adj"] <= res["rate_wmse"]["raw_mult"] * 1.01
