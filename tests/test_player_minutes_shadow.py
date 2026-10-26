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
    assert M.usage_adjusted(np.array([10.0]), np.array([1000.0]), np.array([3]), 5.0, clip=(-1.0, 1.0))[0] == pytest.approx(10.0 * np.e)


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
def _stamp(rec: pd.DataFrame) -> pd.DataFrame:
    return rec.assign(written_at_utc="2026-10-25T00:00:00Z")           # written before every synthetic drop (November)


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
    rec = _stamp(rec)
    rec.loc[0, "pregame"] = False
    rec.loc[1, "model_sha256"] = "other"
    outc.loc[2, "toi_s"] = 0
    rec.loc[3, "written_at_utc"] = "2026-11-01T01:00:00Z"                    # written after the drop: never counts
    m = M.paired_sample(rec, outc, inc, "m")
    assert len(m) == 15 - 4 and not ((m["game_id"] == 0) & (m["player_id"].isin([0, 1, 2]))).any()
    assert list(m["game_start_utc"]) == sorted(m["game_start_utc"])
    assert M.paired_sample(pd.DataFrame(), outc, inc).empty


def test_scoring_applies_the_registered_thresholds_and_a_look_uses_its_own_sample():
    rec, outc, inc = _synthetic(60, 40)
    m = M.paired_sample(_stamp(rec), outc, inc, "m")
    assert "pass" not in M.score_frame(m)["hypotheses"]["H1"]                        # nothing but a decision/final look carries a pass flag
    res = M.score_frame(m, with_pass=True)
    h = res["hypotheses"]
    assert res["n_paired"] == 2400 and h["H1"]["pass"] and h["H1"]["relative_change"] < -0.02
    assert "verdict" in h["H2"] and "INCONCLUSIVE" in h["H2"]["verdict"]                   # fewer than 10,000 pairs with an incumbent PP value
    assert h["H3"]["required_relative_change"] == -0.005
    sub = M.score_frame(m, 1000)
    assert sub["sample_sha256"] != M.score_frame(m, 1001)["sample_sha256"] and sub["last_key"]["game_id"] == int(m["game_id"].iloc[999])
    assert sub["n_paired"] == 1000 and sub["hypotheses"]["H1"]["n"] == 1000
    assert M.score_frame(m, 100)["verdict"].startswith("INCONCLUSIVE AT n=100")


def test_a_challenger_that_is_not_better_does_not_pass(monkeypatch):
    rec, outc, inc = _synthetic(60, 40, better=False)
    res = M.score_frame(M.paired_sample(_stamp(rec), outc, inc, "m"), with_pass=True)
    assert not res["hypotheses"]["H1"]["pass"] and not res["hypotheses"]["H3"]["pass"]


def test_pp_hypothesis_is_judged_once_enough_pairs_have_an_incumbent_value(monkeypatch):
    monkeypatch.setattr(M, "MIN_PP_PAIRS", 500)
    rec, outc, inc = _synthetic(60, 40)
    res = M.score_frame(M.paired_sample(_stamp(rec), outc, inc, "m"), with_pass=True)
    assert res["hypotheses"]["H2"]["pass"] and res["hypotheses"]["H2"]["n"] == 2400 and res["pp"]["mse_M0"] < res["pp"]["mse_incumbent"]


def _publish(out: Path, rec: pd.DataFrame, outc: pd.DataFrame, written="2026-10-25T00:00:00Z") -> None:
    """Write records/outcomes the way the runner does (files listed in the append-only manifest), with a fixed write time."""
    entries = []
    for name, df in (("records", rec), ("outcomes", outc)):
        rel = f"{name}/dt=2026-11-01/x.jsonl.gz"
        (out / rel).parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(out / rel, "wt") as f:
            for r in df.to_dict("records"):
                f.write(json.dumps(r, default=float) + "\n")
        entries.append({"path": rel, "rows": len(df), "sha256": "x", "written_at_utc": written})
    (out / "MANIFEST.jsonl").write_text("\n".join(json.dumps(e) for e in entries) + "\n")
    (out / "activation.json").write_text(json.dumps({"activation_utc": "2026-10-24T15:00:00Z", "model_sha256": "m"}))


def test_score_writes_the_registered_looks_once_and_never_rewrites_them(tmp_path, monkeypatch):
    rec, outc, inc = _synthetic(60, 40)
    out = tmp_path / "out"
    _publish(out, rec, outc)
    monkeypatch.setattr(M, "incumbent_toi", lambda pf: inc)
    monkeypatch.setattr(M.LCR, "coverage_audit", lambda archive, out, rec, now: {"activated": True, "games_since_activation": 60, "recorded": 60, "missed": [], "pending": 0,
                                                                                  "coverage_of_started": 1.0, "median_lead_min": 400.0, "min_lead_min": 30.0})
    monkeypatch.setattr(M, "LOOKS", (1000, 5000))
    monkeypatch.setattr(M, "DECISION_LOOK", 1000)
    now = datetime(2026, 12, 1, tzinfo=UTC)
    r1 = M.score(tmp_path / "a", tmp_path / "pf", out, now=now)
    assert r1["looks"] == [1000] and (out / "looks" / "look_1000.json").exists() and not (out / "looks" / "look_5000.json").exists()
    first = (out / "looks" / "look_1000.json").read_text()
    look = json.loads(first)
    assert look["decision_look"] and look["hypotheses"]["H1"]["pass"] and len(look["sample_sha256"]) == 64 and look["last_key"]["game_id"] >= 0
    md = (out / "scoreboard" / "latest.md").read_text()
    assert "descriptive only" in md and "coverage of started games 1.0" in md and "SUPPORTED at the decision look" in md and "PASS" not in md.replace("SUPPORTED", "")
    M.score(tmp_path / "a", tmp_path / "pf", out, now=datetime(2026, 12, 2, tzinfo=UTC))
    assert (out / "looks" / "look_1000.json").read_text() == first                     # computed once, on its own sample


def test_a_look_waits_until_every_earlier_recorded_game_has_its_outcome(tmp_path, monkeypatch):
    rec, outc, inc = _synthetic(60, 40)
    outc = outc[outc["game_id"] != 0]                                                 # game 0 (the earliest) has not settled yet
    out = tmp_path / "out"
    _publish(out, rec, outc)
    monkeypatch.setattr(M, "incumbent_toi", lambda pf: inc)
    monkeypatch.setattr(M.LCR, "coverage_audit", lambda *a: {"activated": False})
    monkeypatch.setattr(M, "LOOKS", (1000,))
    r = M.score(tmp_path / "a", tmp_path / "pf", out, now=datetime(2026, 11, 3, tzinfo=UTC))
    assert r["looks"] == [] and "no outcome yet" in r["looks_waiting"][1000] and not (out / "looks").exists()
    r = M.score(tmp_path / "a", tmp_path / "pf", out, now=datetime(2026, 12, 20, tzinfo=UTC))      # an unsettled game older than 7 days is ignored
    assert r["looks"] == [1000]


def test_registered_verdicts_follow_the_decision_then_final_rule():
    ok, bad = {"hypotheses": {"H1": {"pass": True}, "H2": {"verdict": "INCONCLUSIVE"}, "H3": {"pass": False}}}, {"hypotheses": {"H1": {"pass": True}, "H2": {"pass": True}, "H3": {"pass": True}}}
    assert all(v.startswith("OPEN") for v in M.registered_verdicts({10_000: ok}).values())          # the descriptive look decides nothing
    v = M.registered_verdicts({30_000: ok})
    assert v["H1"].startswith("SUPPORTED at the decision") and v["H3"].startswith("NOT MET") and "carried to the final look" in v["H3"]
    v = M.registered_verdicts({30_000: ok, 60_000: bad})
    assert v["H3"].startswith("SUPPORTED at the final") and v["H2"].startswith("SUPPORTED at the final") and v["H1"].startswith("SUPPORTED at the decision")


def test_non_finite_rows_are_dropped_not_allowed_to_poison_the_intervals():
    rec, outc, inc = _synthetic(30, 40)
    m = M.paired_sample(_stamp(rec), outc, inc, "m")
    m.loc[5, "p_M0_toi_min"] = float("nan")
    res = M.score_frame(m, with_pass=True)
    assert res["n_nonfinite_dropped"] == 1 and np.isfinite(res["hypotheses"]["H1"]["hi95"])


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


def test_a_bad_optional_input_is_recorded_and_does_not_stop_the_projections(tmp_path, monkeypatch):
    _stub(monkeypatch)
    def boom(archive, now, ids):
        raise ValueError("garbage predicted_at_utc")
    monkeypatch.setattr(M, "incumbent_capture", boom)
    rep = M.predict(tmp_path / "a", tmp_path / "h", tmp_path / "out", now=NOW, params_path=ROOT / "data/params/minutes-v1.json")
    assert rep["games_written"] == [10] and rep["errors"] == [] and "garbage" in rep["errors_optional"][0]


def test_incumbent_capture_orders_mixed_timestamp_formats_by_instant(tmp_path, monkeypatch):
    rows = [{"game_id": 7, "player_id": 5, "predicted_at_utc": "2026-10-24T12:00:00+00:00", "meta_expected_toi_min": 18.0, "meta_expected_pp_toi_min": 2.0},
            {"game_id": 7, "player_id": 5, "predicted_at_utc": "2026-10-24T09:00:00Z", "meta_expected_toi_min": 17.0, "meta_expected_pp_toi_min": 1.0}]
    monkeypatch.setattr("nhl_edge.archive.ledger.Ledger", lambda root: SimpleNamespace(iter_rows=lambda kind, dt_from=None: iter(rows)))
    got = M.incumbent_capture(tmp_path, NOW, {7})
    assert got[(7, 5)]["toi_min"] == 18.0


def test_coverage_counts_report_how_many_players_have_each_comparator():
    rec, outc, inc = _synthetic(4, 10)
    rec = _stamp(rec)
    m = M.paired_sample(rec, outc, inc.iloc[5:], "m")                       # the incumbent is missing for 5 players
    c = M.coverage_counts(M.LCR.eligible_records(rec, "m")[0], outc, m)
    assert c["settled_candidates"] == 40 and c["dressed"] == 40 and c["paired"] == 35 and c["paired_with_captured_pp"] == 35
    assert M.coverage_counts(rec.iloc[:0], outc, m)["dressed"] == 0


def test_incumbent_last_predrop_takes_only_rows_made_before_the_drop(tmp_path, monkeypatch):
    rows = [{"game_id": 7, "player_id": 5, "predicted_at_utc": "2026-10-24T20:00:00Z", "meta_expected_toi_min": 17.0, "meta_expected_pp_toi_min": 1.0},
            {"game_id": 7, "player_id": 5, "predicted_at_utc": "2026-10-24T22:30:00Z", "meta_expected_toi_min": 18.0, "meta_expected_pp_toi_min": 2.0},
            {"game_id": 7, "player_id": 5, "predicted_at_utc": "2026-10-24T23:05:00Z", "meta_expected_toi_min": 25.0, "meta_expected_pp_toi_min": 9.0},       # after the drop: never eligible
            {"game_id": 7, "player_id": 6, "predicted_at_utc": "2026-10-24T22:00:00Z", "meta_expected_toi_min": 15.0, "meta_expected_pp_toi_min": None}]
    monkeypatch.setattr("nhl_edge.archive.ledger.Ledger", lambda root: SimpleNamespace(iter_rows=lambda kind, dt_from=None: iter(rows)))
    got = M.incumbent_last_predrop(tmp_path, {7: "2026-10-24T23:00:00Z"}, datetime(2026, 10, 26, tzinfo=UTC))
    assert got[(7, 5)] == {"toi_min": 18.0, "pp_min": 2.0, "at": "2026-10-24T22:30:00Z"} and got[(7, 6)]["pp_min"] is None


def test_capture_incumbent_writes_once_with_explicit_missing_and_the_guard_covers_it(tmp_path, monkeypatch):
    rec, _, _ = _synthetic(2, 3)
    rec = rec.assign(game_start_utc=["2026-10-24T23:00:00Z"] * 3 + ["2026-10-25T01:00:00Z"] * 3)
    out = tmp_path / "out"
    _publish(out, rec, pd.DataFrame([{"game_id": 0, "player_id": 0, "toi_s": 600}]))
    monkeypatch.setattr(M, "incumbent_last_predrop", lambda archive, starts, now: {(0, 1): {"toi_min": 18.0, "pp_min": 2.0, "at": "2026-10-24T22:00:00Z"}})
    r = M.capture_incumbent(tmp_path / "a", out, now=datetime(2026, 10, 25, 12, 0, tzinfo=UTC))
    assert r["games_captured"] == [0, 1]
    inc = M.load_dir(out, "incumbent")
    row = inc[(inc.game_id == 0) & (inc.player_id == 1)].iloc[0]
    assert row["inc_pp_min"] == 2.0 and row["incumbent_lead_min"] == 60.0 and inc[inc.inc_pp_min.notna()].shape[0] == 1 and len(inc) == 6      # missing candidates are rows with nulls
    assert M.capture_incumbent(tmp_path / "a", out, now=datetime(2026, 10, 25, 13, 0, tzinfo=UTC))["games_captured"] == []                   # write-once per game
    (out / "incumbent" / "dt=2026-10-24" / "stray.jsonl.gz").write_bytes(gzip.compress(b"{}\n"))
    assert any(x.startswith("unlisted: incumbent/") for x in M.guard(out))


def test_supplementary_h2_reports_coverage_missingness_and_selection_without_a_pass_flag():
    rec, outc, _ = _synthetic(30, 40)
    rec = _stamp(rec)
    rng = np.random.default_rng(3)
    inc_rows = []
    for g in range(30):
        for p in range(40):
            priced = p < 24                                   # only the first 24 candidates were ever priced by the production engine
            ypp = float(outc[(outc.game_id == g) & (outc.player_id == p)]["toi_pp_s"].iloc[0]) / 60
            inc_rows.append({"game_id": g, "player_id": p, "inc_toi_min": 18.0 if priced else None, "inc_pp_min": (ypp + rng.normal(0, 0.7)) if priced else None, "incumbent_lead_min": 45.0 if priced else None})
    rec["pos"] = ["F" if p % 2 else "D" for g in range(30) for p in range(40)]
    res = M.supplementary_h2(rec, outc, pd.DataFrame(inc_rows), "m")
    assert res["n_dressed"] == 1200 and res["n_pairs"] == 720 and abs(res["coverage_of_dressed"] - 0.6) < 1e-9 and res["missing"]["no_incumbent_row"] == 480
    assert res["registered_captured_coverage_of_dressed"] == 1.0 and res["selection"]["covered"]["n"] == 720 and res["selection"]["not_covered"]["n"] == 480
    assert res["relative_change_M0_vs_incumbent"]["relative_change"] < 0 and "pass" not in res["relative_change_M0_vs_incumbent"] and res["incumbent_lead_min"]["median"] == 45.0
    md = M.render({"n_paired": 0, "verdict": "x"}, {}, None, {"records": 1, "eligible": 1, "outcomes": 1}, None, res)
    assert "Supplementary power-play comparison (not the registered H2" in md and "no pass/fail" in md
    assert M.supplementary_h2(rec, outc, pd.DataFrame(), "m")["n_dressed"] == 0
