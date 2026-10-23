"""Prospective-test plumbing: write-once immutable records, coverage, pregame/late split, and the frozen rule applied to synthetic data."""

from __future__ import annotations

import gzip
import json
from datetime import UTC, datetime

import numpy as np
import pandas as pd
import pytest

from nhl_edge.research import workload_eval as E
from nhl_edge.research import workload_shadow as S
from nhl_edge.research import workload_shadow_run as R
from nhl_edge.research import workload_v1 as W

NOW = datetime(2026, 10, 24, 15, 0, tzinfo=UTC)


def test_write_once_refuses_to_overwrite_and_guard_detects_tampering(tmp_path):
    R.write_once(tmp_path, "records/dt=2026-10-24/a.jsonl.gz", [{"game_id": 1}])
    with pytest.raises(FileExistsError):
        R.write_once(tmp_path, "records/dt=2026-10-24/a.jsonl.gz", [{"game_id": 2}])
    assert R.guard(tmp_path) == []
    p = tmp_path / "records/dt=2026-10-24/a.jsonl.gz"
    with gzip.open(p, "wt") as f:
        f.write('{"game_id": 99}\n')
    assert R.guard(tmp_path) == ["modified: records/dt=2026-10-24/a.jsonl.gz"]
    R.write_once(tmp_path, "records/dt=2026-10-24/b.jsonl.gz", [{"game_id": 3}])
    (tmp_path / "records/dt=2026-10-24/c.jsonl.gz").write_bytes(gzip.compress(b"{}\n"))
    assert "unlisted: records/dt=2026-10-24/c.jsonl.gz" in R.guard(tmp_path)
    (tmp_path / "records/dt=2026-10-24/b.jsonl.gz").unlink()
    assert "missing: records/dt=2026-10-24/b.jsonl.gz" in R.guard(tmp_path)


def _sched():
    base = {"season_type": "regular", "status": "not_started", "home_team_id": "1", "away_team_id": "2", "game_date_et": "2026-10-24"}
    return [{**base, "game_id": "10", "start_time_utc": "2026-10-24T23:00:00Z"},          # in horizon -> written
            {**base, "game_id": "11", "start_time_utc": "2026-10-24T14:00:00Z"},          # already started at NOW -> missed, nothing written
            {**base, "game_id": "12", "start_time_utc": "2026-10-26T23:00:00Z"},          # beyond the horizon
            {**base, "game_id": "13", "start_time_utc": "2026-10-24T23:30:00Z", "season_type": "preseason"},
            {**base, "game_id": "14", "start_time_utc": "2026-10-24T23:30:00Z", "status": "final"}]


def _stub_pipeline(monkeypatch, written: list):
    monkeypatch.setattr(R, "read_archive", lambda archive, now: ({k: [] for k in S.TABLES}, _sched()))
    monkeypatch.setattr(S, "load_tables", lambda h, live: {k: pd.DataFrame() for k in S.TABLES})
    monkeypatch.setattr(S, "build_tables", lambda t: (pd.DataFrame(), pd.DataFrame()))

    def fake_predict_day(sk, tg, games, players, goalies, params_path, season=2026, cand=None, constants=None, dispersion_season=2025):
        written.append([int(g["game_id"]) for g in games])
        pred = pd.DataFrame({"game_id": [int(games[0]["game_id"])] * 2, "player_id": [5, 6], "name": ["a", "b"], "pos": ["F", "D"], "team_id": [1, 1], "opp_id": [2, 2], "is_home": [True, True],
                             "raw_mean": [2.0, 1.0], "base_sog": [1.9, 1.1], "level_factor": [0.97, 0.97], "lc_mean": [1.94, 0.97], "pmf": [np.full(S.PMF_K, 1 / S.PMF_K)] * 2})
        return pred, S.Fit(None, None, 0.1, "sha")                                          # type: ignore[arg-type]
    monkeypatch.setattr(S, "predict_day", fake_predict_day)


def test_predict_writes_pregame_games_once_and_reports_coverage(tmp_path, monkeypatch):
    written: list = []
    _stub_pipeline(monkeypatch, written)
    rep = R.predict(tmp_path / "arch", tmp_path / "hist", tmp_path / "out", now=NOW, code_commit="abc")
    assert rep["games_written"] == [10] and rep["games_missed_started"] == [11] and rep["rows"] == 2 and rep["guard"] == []
    assert written == [[10]]
    act = json.loads((tmp_path / "out" / "activation.json").read_text())
    assert act["activation_utc"] == "2026-10-24T15:00:00Z" and act["code_commit"] == "abc"
    # a second run the same day: the game already has a record -> nothing new, activation untouched
    rep2 = R.predict(tmp_path / "arch", tmp_path / "hist", tmp_path / "out", now=datetime(2026, 10, 24, 17, 0, tzinfo=UTC), code_commit="def")
    assert rep2["games_written"] == [] and rep2["games_already_recorded"] == [10]
    assert json.loads((tmp_path / "out" / "activation.json").read_text())["code_commit"] == "abc"
    recs = R.load_records(tmp_path / "out")
    assert len(recs) == 2 and bool(recs["pregame"].all()) and set(recs["conditional_on"]) == {"dressing"}
    assert len(list((tmp_path / "out" / "coverage").glob("*.json"))) == 2


def _synthetic(n: int, bias: float = 0.0, champ_bias: float = 0.15, late: int = 5, seed: int = 0):
    rng = np.random.default_rng(seed)
    mu = rng.uniform(0.6, 3.0, n)
    y = rng.poisson(mu)
    alpha = 0.05
    pm = E.nb_pmf(mu * (1 + bias), alpha, W.SOG_K)
    rec = pd.DataFrame({"game_id": np.arange(n) // 20, "player_id": np.arange(n), "pregame": True, "pos": np.where(np.arange(n) % 3 == 0, "D", "F"), "raw_mean": mu * 1.03,
                        "base_mean": np.full(n, mu.mean()), "alpha": alpha, "pmf": list(pm)})
    late_rows = rec.iloc[:late].copy()
    late_rows["pregame"] = False
    late_rows["player_id"] += 10_000_000
    rec = pd.concat([rec, late_rows], ignore_index=True)
    act = pd.DataFrame({"game_id": np.arange(n) // 20, "player_id": np.arange(n), "y_sog": y.astype(float)}).iloc[: n - 7]           # 7 candidates did not dress
    inc = pd.DataFrame({"game_id": np.arange(n) // 20, "player_id": np.arange(n), "champ_mean": mu * (1 + champ_bias), "archived_utc": "x"})
    return rec, act, inc


def test_score_frame_counts_coverage_and_excludes_late_and_non_dressing():
    rec, act, inc = _synthetic(1000)
    sc = R.score_frame(rec, act, inc, {"alpha_champion_nb": 0.08}, n_boot=300)
    assert sc["n_late_records_excluded"] == 5 and sc["n_candidates_not_dressing"] == 7 and sc["n_scored_dressed"] == 993 and sc["n_paired_with_incumbent"] == 993
    assert sc["verdict"].startswith("INCONCLUSIVE") and sc["look_reached"] is None
    assert set(sc["original_rule_checks"]) >= {"crps_vs_champion_ci_upper_lt_0", "abs_bias_le_0.05", "coverage80_in_band", "crps_vs_champion_nb_ci_upper_lt_0"}


def test_decision_look_applies_the_frozen_rule_and_early_failure_stops():
    rec, act, inc = _synthetic(31_000, bias=0.0, champ_bias=0.10, late=0)
    sc = R.score_frame(rec, act, inc, {"alpha_champion_nb": 0.05}, n_boot=200)
    assert sc["look_reached"] == 30_000 and sc["verdict"].startswith(("MEETS FROZEN RULE", "FAILS FROZEN RULE"))
    # a model that is far too high triggers the early-failure criterion at any reached look
    rec2, act2, inc2 = _synthetic(10_500, bias=0.4, late=0)
    sc2 = R.score_frame(rec2, act2, inc2, {"alpha_champion_nb": 0.05}, n_boot=200)
    assert sc2["look_reached"] == 10_000 and sc2["verdict"].startswith("FAILS FROZEN RULE")


def test_without_the_frozen_champion_dispersion_the_decision_stays_open():
    rec, act, inc = _synthetic(31_000, late=0)
    sc = R.score_frame(rec, act, inc, {}, n_boot=100)
    assert sc["original_rule_complete"] is False and sc["verdict"].startswith("INCONCLUSIVE")


def test_decision_look_is_inconclusive_when_too_few_scored_rows_have_an_incumbent_forecast():
    rec, act, inc = _synthetic(45_000, late=0)
    inc = inc.iloc[: int(0.70 * len(inc))]                       # Amendment 1: coverage below 80% at a decision look
    sc = R.score_frame(rec, act, inc, {"alpha_champion_nb": 0.05}, n_boot=100)
    assert sc["look_reached"] == 30_000 and sc["verdict"].startswith("INCONCLUSIVE (comparator coverage")
    full = R.score_frame(rec, act, _synthetic(45_000, late=0)[2], {"alpha_champion_nb": 0.05}, n_boot=100)
    assert full["verdict"].startswith(("MEETS FROZEN RULE", "FAILS FROZEN RULE"))


def test_incumbent_forecasts_take_the_last_pre_drop_row(tmp_path):
    d = tmp_path / "forecasts" / "nhl" / "2026-10-24"
    d.mkdir(parents=True)

    def row(arch, mean, model="PLAYER_SIM_V1", fam="shots"):
        return {"family": fam, "model_id": model, "game_id": "10", "entity_id": "5", "mean": mean, "archived_utc": arch, "game_start_utc": "2026-10-24T23:00:00Z"}
    with gzip.open(d / "a.jsonl.gz", "wt") as f:
        for r in (row("2026-10-24T12:00:00Z", 1.0), row("2026-10-24T20:00:00Z", 2.0), row("2026-10-24T23:10:00Z", 9.0), row("2026-10-24T21:00:00Z", 5.0, model="pf-nhl-F_stack"),
                  row("2026-10-24T21:00:00Z", 7.0, fam="goals")):
            f.write(json.dumps(r) + "\n")
    inc = R.incumbent_forecasts(tmp_path)
    assert len(inc) == 1 and float(inc["champ_mean"].iloc[0]) == 2.0                 # the 23:10 forecast is after the drop; other models/families are ignored
