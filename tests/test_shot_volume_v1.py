"""Unit tests for NHL_SHOT_VOLUME_V1 (research challenger): shot-volume layer, coherent SOG allocation, scoring helpers,
PURE sidecar validity and the negative control. No network, no market input in the PURE path."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

import numpy as np
import pandas as pd

from nhl_edge.players.engine import TeamDraws
from nhl_edge.research import shot_volume_v1 as sv

GATE = Path(__file__).resolve().parents[1] / "tools" / "pure_gate" / "pure_gate.py"


def _tg(n_days: int = 60, level_drop: bool = False) -> pd.DataFrame:
    """Synthetic team-games: 4 teams, round robin; team 1 generates 20% more shots, team 2 suppresses 20%."""
    rows = []
    gid = 0
    pairs = [(1, 2), (3, 4), (1, 3), (2, 4), (1, 4), (2, 3)]
    for day in range(n_days):
        h, a = pairs[day % len(pairs)]
        lvl = 30.0 - (5.0 if (level_drop and day >= n_days // 2) else 0.0)
        gen = {1: 1.2, 2: 1.0, 3: 1.0, 4: 1.0}
        sup = {1: 1.0, 2: 0.8, 3: 1.0, 4: 1.0}
        sf_h = lvl * gen[h] * sup[a]
        sf_a = lvl * gen[a] * sup[h]
        di = int((pd.Timestamp("2024-10-01") + pd.Timedelta(days=day)).strftime("%Y%m%d"))
        gid += 1
        rows.append({"game_id": gid, "team_id": h, "opp_id": a, "sf": sf_h, "sa": sf_a, "date_int": di})
        rows.append({"game_id": gid, "team_id": a, "opp_id": h, "sf": sf_a, "sa": sf_h, "date_int": di})
    return pd.DataFrame(rows)


def test_relative_rates_are_strictly_before_the_date():
    tg = _tg()
    r = sv.RelativeShotRates(tg, prior_games=0.0)
    first = int(tg["date_int"].min())
    assert r.ratings(first) == {t: (1.0, 1.0) for t in (1, 2, 3, 4)}
    d = int(tg["date_int"].iloc[40])
    before = r.expected_faced(2, 1, d, True)
    tg2 = tg.copy()
    tg2.loc[tg2["date_int"] >= d, ["sf", "sa"]] *= 3.0  # the future must not move the forecast
    assert np.isclose(sv.RelativeShotRates(tg2, prior_games=0.0).expected_faced(2, 1, d, True), before)


def test_opponent_adjustment_corrects_an_unbalanced_schedule():
    """Team 3 keeps meeting the strong suppressor (team 2); team 4 never does. Both generate shots equally."""
    rows, gid = [], 0
    pairs = [(3, 2), (3, 2), (4, 1), (3, 2), (4, 1), (1, 2)]
    sup = {1: 1.0, 2: 0.7, 3: 1.0, 4: 1.0}
    for day in range(120):
        h, a = pairs[day % len(pairs)]
        di = int((pd.Timestamp("2024-10-01") + pd.Timedelta(days=day)).strftime("%Y%m%d"))
        gid += 1
        rows.append({"game_id": gid, "team_id": h, "opp_id": a, "sf": 30.0 * sup[a], "sa": 30.0 * sup[h], "date_int": di})
        rows.append({"game_id": gid, "team_id": a, "opp_id": h, "sf": 30.0 * sup[h], "sa": 30.0 * sup[a], "date_int": di})
    tg = pd.DataFrame(rows)
    d = int(tg["date_int"].max())
    kw = {"prior_games": 0.0, "half_life": 1e9, "max_games": 200}
    adj = sv.RelativeShotRates(tg, **kw).ratings(d)
    raw = sv.RelativeShotRates(tg, opp_adjust=False, **kw).ratings(d)
    assert abs(adj[3][0] / adj[4][0] - 1.0) < abs(raw[3][0] / raw[4][0] - 1.0)
    assert adj[2][1] < adj[4][1]


def test_level_drift_does_not_inflate_expected_shots():
    tg = _tg(120, level_drop=True)
    d = int(tg["date_int"].max())
    rel = sv.RelativeShotRates(tg, league_window=40)
    from nhl_edge.players.params import ShotRates

    inc = ShotRates(float(tg["sa"].mean()), tg.copy(), league_window=40)
    truth = 25.0  # neutral pair (3 vs 4) at the new level, venue aside
    e_rel = rel.expected_faced(3, 4, d, True) / 0.985
    e_inc = inc.expected_faced(3, 4, d, True) / 0.985
    assert abs(e_rel - truth) < abs(e_inc - truth)


def _draws(n_sims: int, n: int, rng: np.random.Generator) -> TeamDraws:
    goals = rng.poisson(0.2, (n_sims, n)).astype(np.int16)
    a1 = rng.poisson(0.1, (n_sims, n)).astype(np.int16)
    a2 = rng.poisson(0.05, (n_sims, n)).astype(np.int16)
    mult = np.exp(rng.normal(0, 0.15, (n_sims, n))).astype(np.float32)
    return TeamDraws(goals, a1, a2, mult, {})


def test_sog_allocation_is_coherent():
    rng = np.random.default_rng(3)
    d = _draws(500, 18, rng)
    w = rng.uniform(0.2, 3.0, 18)
    ng = rng.poisson(25, 500)
    sog = sv.allocate_sog(np.random.default_rng(5), d, w, ng)
    assert (sog >= d.goals).all()
    assert np.array_equal(sog.sum(axis=1), d.goals.sum(axis=1) + ng)
    # heavier weight -> more shots on average
    assert np.corrcoef(w, (sog - d.goals).mean(axis=0))[0, 1] > 0.9


def test_coherence_violations_flags_a_broken_draw():
    rng = np.random.default_rng(1)
    d = _draws(50, 5, rng)

    class PS:  # minimal stand-in
        home = d
        away = d

    ng = np.full(50, 10)
    ok = sv.allocate_sog(np.random.default_rng(2), d, np.ones(5), ng)
    assert sv.coherence_violations(PS(), {"home": ok}, {"home": ng}) == []
    bad = ok.copy()
    bad[:, 0] = 0
    bad[:, 1] += d.goals[:, 0] + 11
    assert sv.coherence_violations(PS(), {"home": bad}, {"home": ng})


def test_scoring_helpers():
    x = np.array([0, 0, 1, 1, 1, 2, 3, 3, 4, 6])
    assert np.isclose(sv.crps_draws(np.full(100, 2.0), 2.0), 0.0)
    assert sv.crps_draws(x, 10.0) > sv.crps_draws(x, 2.0)
    assert np.isclose(sv.log_score_draws(x, 1), -np.log(0.3))
    assert np.isclose(sv.log_score_draws(x, 5), -np.log(1 / 20))  # floored at 1/(2n)
    assert np.isclose(sv.pit_mid(x, 1), 0.2 + 0.15)
    s = sv.summarize(x, [1, 2, 3], True)
    assert s["thr"] == sorted(s["thr"], reverse=True) and s["q"] == sorted(s["q"])


def _row(stat: str = "shots_on_goal") -> dict:
    x = np.random.default_rng(0).poisson(2.0, 4000)
    t = datetime(2026, 1, 10, 23, 0, tzinfo=UTC)
    common = {"game_id": 2025020600, "player_id": 8478402, "team_id": 22, "pos": "F", "season": 2025, "date_int": 20260110,
              "kickoff": t, "as_of": datetime(2026, 1, 10, 22, 0, tzinfo=UTC), "src_max": datetime(2026, 1, 10, 8, 0, tzinfo=UTC),
              "lineage": {"prior_games": 40.0, "expected_sog_incumbent": 2.0}}
    return sv._row(common, stat, x, 3.0)


def test_pure_sidecar_validates_with_the_vendored_gate(tmp_path):
    rows = [sv.to_pure(_row(), sv.MODEL_VERSION, "sha256:" + "a" * 64)]
    f = tmp_path / "f.jsonl"
    sv.write_jsonl(f, rows)
    p = subprocess.run([sys.executable, "-I", str(GATE), "validate", "--forecasts", str(f), "--require-v1"], capture_output=True, text=True)
    assert p.returncode == 0, p.stdout + p.stderr


def test_negative_control_reads_the_market_file_and_pure_rows_do_not_change():
    pure = [sv.to_pure(_row(), sv.MODEL_VERSION, "sha256:" + "a" * 64)]
    before = json.dumps(pure, sort_keys=True)
    q = pd.DataFrame([{"game_id": 2025020600, "player_id": 8478402, "statistic": "shots_on_goal", "at_least": 3.0, "mid": 0.9}])
    ctl = sv.market_centered(pure, q)
    assert json.dumps(pure, sort_keys=True) == before  # the input rows are not mutated
    p_model = [t for t in pure[0]["projection"]["thresholds"] if t["at_least"] == 3.0][0]["probability"]
    p_ctl = [t for t in ctl[0]["projection"]["thresholds"] if t["at_least"] == 3.0][0]["probability"]
    assert p_ctl > p_model
    th = ctl[0]["projection"]["thresholds"]
    assert all(th[i]["probability"] <= th[i - 1]["probability"] for i in range(1, len(th)))
