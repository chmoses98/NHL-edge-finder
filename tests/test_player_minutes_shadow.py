"""player-minutes-1.0: the prospective ice-time records, their write-once guarantees and the registered scoring."""

from __future__ import annotations

import gzip
import json
from datetime import UTC, datetime
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

from nhl_edge.research import player_minutes_shadow as M
from nhl_edge.research import workload_shadow as S
from nhl_edge.research import workload_shadow_run as LCR

NOW = datetime(2026, 10, 24, 15, 0, tzinfo=UTC)
ROOT = Path(__file__).resolve().parents[1]


def test_frozen_params_match_the_registration():
    prm = M.load_params(ROOT / "data/params/minutes-v1.json")
    assert prm["usage_coef"] == 0.23 and prm["multiplier_clip"] == [-1.0, 1.0] and prm["registration"] == M.REGISTRATION
    text = (ROOT / M.REGISTRATION).read_text()
    assert "0.23" in text and "player-minutes-data" in text and "−2%" in text and "−3%" in text and "−0.5%" in text


def test_usage_term_only_moves_players_with_three_known_games_and_is_clipped():
    m0 = np.array([18.0, 18.0, 18.0, 18.0])
    last3 = np.array([22.0, 14.0, 22.0, np.nan])
    nk = np.array([3, 3, 2, 0])
    m1 = M.usage_adjusted(m0, last3, nk, 0.23)
    assert m1[0] > 18.0 > m1[1] and m1[2] == 18.0 and m1[3] == 18.0
    assert m1[0] == pytest.approx(18.0 * np.exp(0.23 * np.log(23.0 / 19.0)))
    assert M.usage_adjusted(np.array([10.0]), np.array([1000.0]), np.array([3]), 5.0, clip=1.0)[0] == pytest.approx(10.0 * np.e)


def test_last3_minutes_use_only_earlier_dates_and_games_with_ice_time():
    pl = pd.DataFrame({"player_id": [1] * 6, "game_id": [1, 2, 3, 4, 5, 6], "game_type": [2] * 6, "game_date": ["2026-10-01", "2026-10-03", "2026-10-05", "2026-10-07", "2026-10-09", "2026-10-24"],
                       "toi_s": [600.0, 1200.0, 0.0, 1260.0, 1320.0, 3000.0]})
    got = M.last3_minutes(pl, 20261024)
    assert got[1][1] == 3 and got[1][0] == pytest.approx((1200 + 1260 + 1320) / 3 / 60)        # the 0-second game and the same-day game are excluded
    assert M.last3_minutes(pd.DataFrame(), 20261024) == {}


# ------------------------------------------------------------------------------------------------------------------------ predict / settle
def _sched():
    base = {"season_type": "regular", "status": "not_started", "home_team_id": "1", "away_team_id": "2", "game_date_et": "2026-10-24"}
    return [{**base, "game_id": "10", "start_time_utc": "2026-10-24T23:00:00Z"}, {**base, "game_id": "11", "start_time_utc": "2026-10-24T14:00:00Z"},
            {**base, "game_id": "12", "start_time_utc": "2026-10-26T23:00:00Z"}]


def _players():
    return pd.DataFrame({"player_id": [5] * 3, "game_id": [1, 2, 3], "game_type": [2] * 3, "game_date": ["2026-10-18", "2026-10-20", "2026-10-22"], "toi_s": [1200.0, 1260.0, 1320.0]})


def _stub(monkeypatch, sha="sha-A"):
    monkeypatch.setattr(LCR, "read_archive", lambda archive, now: ({k: [] for k in S.TABLES}, _sched()))
    monkeypatch.setattr(S, "load_tables", lambda h, live: {**{k: pd.DataFrame() for k in S.TABLES}, "players": _players()})
    monkeypatch.setattr(S, "build_tables", lambda t: (pd.DataFrame(), pd.DataFrame()))
    monkeypatch.setattr(M, "read_inputs", lambda archive, now: {"lines": [{"player_id": 5, "category": "pp", "unit": "pp1", "slot": None, "lines_updated_at_utc": "2026-10-24T13:00:00Z",
                                                                            "lines_source": "Practice", "observed_at_utc": "2026-10-24T14:00:00Z", "injury_status": None, "game_time_decision": False,
                                                                            "resolution": "jersey+name"}],
                                                                "injuries": [{"team_id": 1, "player_name": "Ann Skater", "status": "Day-To-Day", "type": "lower body", "source": "espn_injuries"}],
                                                                "lines_meta": {"observed_at_utc": "2026-10-24T14:00:00Z"}, "injuries_meta": {"observed_at_utc": "2026-10-24T14:00:00Z"}})
    monkeypatch.setattr(M, "incumbent_capture", lambda archive, now, ids: {(10, 5): {"toi_min": 19.0, "pp_min": 2.5, "at": "2026-10-24T12:00:00Z"}})

    def fake(sk, tg, games, players, goalies, params_path, season=2026, cand=None, constants=None, dispersion_season=2025):
        pred = pd.DataFrame({"game_id": [10, 10], "player_id": [5, 6], "name": ["Ann Skater", "Bob"], "pos": ["F", "D"], "team_id": [1, 1], "opp_id": [2, 2], "is_home": [True, True],
                             "wl_toi": [18.0, 22.0], "wl_toi_pp": [2.0, 1.0], "wl_toi_sh": [0.5, 1.5], "wl_toi_evreg": [15.0, 19.0], "wl_toi_ot": [0.5, 0.5]})
        return pred, S.Fit(SimpleNamespace(to_dict=lambda: {"c": 1, "sha": sha}), None, 0.1, "x")      # type: ignore[arg-type]
    monkeypatch.setattr(S, "predict_day", fake)


def test_predict_writes_one_record_per_player_with_inputs_and_is_write_once(tmp_path, monkeypatch):
    _stub(monkeypatch)
    rep = M.predict(tmp_path / "a", tmp_path / "h", tmp_path / "out", now=NOW, code_commit="abc", params_path=ROOT / "data/params/minutes-v1.json")
    assert rep["games_written"] == [10] and rep["games_missed_started"] == [11] and rep["rows"] == 2 and rep["guard"] == [] and rep["errors"] == []
    rec = M.load_dir(tmp_path / "out", "records")
    r = rec[rec["player_id"] == 5].iloc[0]
    assert r["schema"] == "player-minutes-1.0" and bool(r["pregame"]) and r["conditional_on"] == "dressing" and r["usage_coef"] == 0.23
    assert r["predictions"]["M0_toi_min"] == 18.0 and r["predictions"]["M1_toi_min"] > 18.0 and r["predictions"]["pp_min"] == 2.0
    inp = r["inputs"]
    assert inp["n_known_recent_games"] == 3 and inp["last3_toi_min"] == pytest.approx(21.0, abs=1e-3)
    assert inp["lines"][0]["unit"] == "pp1" and inp["lines"][0]["lines_updated_at_utc"] == "2026-10-24T13:00:00Z"
    assert inp["injury"][0]["status"] == "Day-To-Day" and inp["incumbent_pp_min"] == 2.5 and inp["incumbent_at_utc"] == "2026-10-24T12:00:00Z"
    other = rec[rec["player_id"] == 6].iloc[0]["inputs"]
    assert other["lines"] == [] and other["injury"] == [] and other["incumbent_pp_min"] is None and other["n_known_recent_games"] == 0
    assert json.loads((tmp_path / "out" / "activation.json").read_text())["activation_utc"] == "2026-10-24T15:00:00Z"
    # same game again: nothing new, nothing touched
    rep2 = M.predict(tmp_path / "a", tmp_path / "h", tmp_path / "out", now=datetime(2026, 10, 24, 17, 0, tzinfo=UTC), params_path=ROOT / "data/params/minutes-v1.json")
    assert rep2["games_written"] == [] and rep2["games_already_recorded"] == [10]


def test_a_model_that_differs_from_the_frozen_one_is_refused(tmp_path, monkeypatch):
    _stub(monkeypatch, sha="sha-A")
    M.predict(tmp_path / "a", tmp_path / "h", tmp_path / "out", now=NOW, params_path=ROOT / "data/params/minutes-v1.json")
    sched = _sched()
    sched[2]["start_time_utc"] = "2026-10-25T01:00:00Z"                     # a second, later game now enters the horizon
    _stub(monkeypatch, sha="sha-B")                                         # the fitted model now fingerprints differently
    monkeypatch.setattr(LCR, "read_archive", lambda archive, now: ({k: [] for k in S.TABLES}, sched))
    rep = M.predict(tmp_path / "a", tmp_path / "h", tmp_path / "out", now=datetime(2026, 10, 24, 20, 0, tzinfo=UTC), params_path=ROOT / "data/params/minutes-v1.json")
    assert rep["games_written"] == [] and "differs from the one frozen" in rep["errors"][0]


def test_settle_writes_each_games_outcomes_once_and_the_guard_catches_unlisted_files(tmp_path, monkeypatch):
    _stub(monkeypatch)
    M.predict(tmp_path / "a", tmp_path / "h", tmp_path / "out", now=NOW, params_path=ROOT / "data/params/minutes-v1.json")
    live = {k: [] for k in S.TABLES}
    live["players"] = [{"game_id": 10, "player_id": 5, "team_id": 1, "game_type": 2, "game_date": "2026-10-24", "toi_s": 1100, "toi_ev_s": 900, "toi_pp_s": 150, "toi_sh_s": 50, "sog": 3,
                        "shifts_ok": True, "_observed_at_utc": "2026-10-25T05:00:00Z"},
                       {"game_id": 10, "player_id": 6, "team_id": 1, "game_type": 2, "game_date": "2026-10-24", "toi_s": 0, "toi_ev_s": 0, "toi_pp_s": 0, "toi_sh_s": 0, "sog": 0,
                        "shifts_ok": True, "_observed_at_utc": "2026-10-25T05:00:00Z"},
                       {"game_id": 99, "player_id": 7, "team_id": 1, "game_type": 2, "game_date": "2026-10-24", "toi_s": 900, "_observed_at_utc": "2026-10-25T05:00:00Z"}]
    later = datetime(2026, 10, 25, 6, 0, tzinfo=UTC)
    monkeypatch.setattr(LCR, "read_archive", lambda archive, now: (live, _sched()))
    rep = M.settle(tmp_path / "a", tmp_path / "out", now=later)
    assert rep["games_with_outcomes_written"] == [10] and rep["pending"] == [] and rep["guard"] == []
    outc = M.load_dir(tmp_path / "out", "outcomes")
    assert set(outc["player_id"]) == {5, 6} and outc.loc[outc["player_id"] == 5, "toi_pp_s"].iloc[0] == 150 and set(outc["settled_at_utc"]) == {"2026-10-25T06:00:00Z"}
    assert M.settle(tmp_path / "a", tmp_path / "out", now=later)["games_with_outcomes_written"] == []          # already settled
    (tmp_path / "out" / "outcomes" / "dt=2026-10-24" / "extra.jsonl.gz").write_bytes(gzip.compress(b"{}\n"))
    assert any(x.startswith("unlisted: outcomes/") for x in M.guard(tmp_path / "out"))


# ------------------------------------------------------------------------------------------------------------------------ scoring
def _synthetic(n_games: int = 60, per: int = 40, seed: int = 1, better: bool = True):
    rng = np.random.default_rng(seed)
    rows, outs, inc = [], [], []
    for g in range(n_games):
        for p in range(per):
            true = rng.uniform(10, 24)
            y = max(1.0, true + rng.normal(0, 2.0))
            m0 = true + rng.normal(0, 0.4) if better else true + rng.normal(0, 3.0)
            incv = true + rng.normal(0, 3.0) - 0.3
            m1 = m0 + (0.05 if better else 0.0)
            ypp = max(0.0, rng.normal(2.0, 0.8))
            rows.append({"game_id": g, "player_id": p, "game_start_utc": f"2026-11-{1 + g // 10:02d}T00:00:00Z", "pregame": True, "model_sha256": "m",
                         "predictions": {"M0_toi_min": m0, "M1_toi_min": m1, "pp_min": ypp + rng.normal(0, 0.2) if better else ypp + rng.normal(0, 1.5)},
                         "inputs": {"incumbent_pp_min": ypp + rng.normal(0, 0.7)}})
            outs.append({"game_id": g, "player_id": p, "toi_s": y * 60, "toi_pp_s": ypp * 60, "shifts_ok": True})
            inc.append({"game_id": g, "player_id": p, "inc_toi": incv})
    return pd.DataFrame(rows), pd.DataFrame(outs), pd.DataFrame(inc)


def test_paired_sample_keeps_only_pregame_frozen_model_rows_of_players_who_played():
    rec, outc, inc = _synthetic(3, 5)
    rec.loc[0, "pregame"] = False
    rec.loc[1, "model_sha256"] = "other"
    outc.loc[2, "toi_s"] = 0
    m = M.paired_sample(rec, outc, inc, "m")
    assert len(m) == 15 - 3 and not ((m["game_id"] == 0) & (m["player_id"].isin([0, 1, 2]))).any()
    assert list(m["game_start_utc"]) == sorted(m["game_start_utc"])
    assert M.paired_sample(pd.DataFrame(), outc, inc).empty


def test_scoring_applies_the_registered_thresholds_and_a_look_uses_its_own_sample():
    rec, outc, inc = _synthetic(60, 40)
    m = M.paired_sample(rec, outc, inc, "m")
    res = M.score_frame(m)
    h = res["hypotheses"]
    assert res["n_paired"] == 2400 and h["H1"]["pass"] and h["H1"]["relative_change"] < -0.02
    assert "verdict" in h["H2"] and "INCONCLUSIVE" in h["H2"]["verdict"]                   # fewer than 10,000 pairs with an incumbent PP value
    assert h["H3"]["required_relative_change"] == -0.005
    sub = M.score_frame(m, 1000)
    assert sub["n_paired"] == 1000 and sub["hypotheses"]["H1"]["n"] == 1000
    assert M.score_frame(m, 100)["verdict"].startswith("INCONCLUSIVE AT n=100")


def test_a_challenger_that_is_not_better_does_not_pass(monkeypatch):
    rec, outc, inc = _synthetic(60, 40, better=False)
    res = M.score_frame(M.paired_sample(rec, outc, inc, "m"))
    assert not res["hypotheses"]["H1"]["pass"] and not res["hypotheses"]["H3"]["pass"]


def test_pp_hypothesis_is_judged_once_enough_pairs_have_an_incumbent_value(monkeypatch):
    monkeypatch.setattr(M, "MIN_PP_PAIRS", 500)
    rec, outc, inc = _synthetic(60, 40)
    res = M.score_frame(M.paired_sample(rec, outc, inc, "m"))
    assert res["hypotheses"]["H2"]["pass"] and res["hypotheses"]["H2"]["n"] == 2400 and res["pp"]["mse_M0"] < res["pp"]["mse_incumbent"]


def test_score_writes_the_registered_looks_once_and_never_rewrites_them(tmp_path, monkeypatch):
    rec, outc, inc = _synthetic(60, 40)
    out = tmp_path / "out"
    (out / "records" / "dt=2026-11-01").mkdir(parents=True)
    (out / "outcomes" / "dt=2026-11-01").mkdir(parents=True)
    for name, df in (("records", rec), ("outcomes", outc)):
        with gzip.open(out / name / "dt=2026-11-01" / "x.jsonl.gz", "wt") as f:
            for r in df.to_dict("records"):
                f.write(json.dumps(r, default=float) + "\n")
    (out / "activation.json").write_text(json.dumps({"activation_utc": "2026-10-24T15:00:00Z", "model_sha256": "m"}))
    monkeypatch.setattr(M, "incumbent_toi", lambda pf: inc)
    monkeypatch.setattr(M, "LOOKS", (1000, 5000))
    r1 = M.score(tmp_path / "a", tmp_path / "pf", out, now=NOW)
    assert r1["looks"] == [1000] and (out / "looks" / "look_1000.json").exists() and not (out / "looks" / "look_5000.json").exists()
    first = (out / "looks" / "look_1000.json").read_text()
    assert "relative_change" in first and (out / "scoreboard" / "latest.md").exists()
    M.score(tmp_path / "a", tmp_path / "pf", out, now=datetime(2026, 12, 1, tzinfo=UTC))
    assert (out / "looks" / "look_1000.json").read_text() == first                     # computed once, on its own sample


def test_incumbent_toi_takes_the_last_forecast_before_the_drop(tmp_path):
    d = tmp_path / "forecasts" / "nhl" / "2026-10-25"
    d.mkdir(parents=True)
    base = {"family": "toi_minutes", "model_id": "PLAYER_SIM_V1", "game_id": "7", "entity_id": "5", "game_start_utc": "2026-10-25T00:00:00Z"}
    rows = [{**base, "archived_utc": "2026-10-24T10:00:00Z", "mean": 17.0}, {**base, "archived_utc": "2026-10-24T20:00:00Z", "mean": 18.5},
            {**base, "archived_utc": "2026-10-25T00:05:00Z", "mean": 25.0}, {**base, "family": "shots", "archived_utc": "2026-10-24T21:00:00Z", "mean": 3.0}]
    with gzip.open(d / "a.jsonl.gz", "wt") as f:
        f.write("\n".join(json.dumps(r) for r in rows))
    got = M.incumbent_toi(tmp_path)
    assert len(got) == 1 and got.iloc[0]["inc_toi"] == 18.5


def test_unreadable_context_partitions_do_not_block_the_projections(tmp_path, monkeypatch):
    import nhl_edge.workflows.simulate as sim

    def boom(led, kind, now):
        raise FileNotFoundError("sparse checkout does not hold it")
    monkeypatch.setattr(sim, "_read_latest", boom)
    monkeypatch.setattr("nhl_edge.archive.ledger.Ledger", lambda root: SimpleNamespace())
    got = M.read_inputs(tmp_path, NOW)
    assert got["lines"] == [] and got["injuries"] == [] and "FileNotFoundError" in got["lines_meta"]["error"]
