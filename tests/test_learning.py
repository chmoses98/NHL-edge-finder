"""Learning loop (nhl-learning-1.0): realised-script postmortems are pregame-only, immutable and deduped; scoring math; the
maturity gates never promote on small samples; the SIFT publication layer keeps raw statistics out of betting evidence."""

from __future__ import annotations

import json
from datetime import UTC, datetime

import pytest

from nhl_edge.archive.ledger import Ledger
from nhl_edge.research_sift import EVIDENCE_BASES, learning_extension, matchup_findings, script_notes, scripts_extension
from nhl_edge.scripts_v1.taxonomy import SCRIPTS, base_rates
from nhl_edge.workflows.learning import (
    binary_metrics,
    final_pregame,
    learning_stage,
    mean_ci,
    multiclass_scores,
    run_learning,
)

ORDER = [s.id for s in SCRIPTS]
START = datetime(2026, 10, 6, 23, 0, tzinfo=UTC)


def test_multiclass_scores_and_base_rate():
    p = {k: 0.0 for k in ORDER} | {"OPEN_GAME": 0.6, "BACK_AND_FORTH": 0.4}
    s = multiclass_scores(p, "OPEN_GAME", ORDER)
    assert s["brier"] == pytest.approx(0.4**2 + 0.4**2) and s["top_hit"] == 1.0 and s["top"] == "OPEN_GAME"
    miss = multiclass_scores(p, "TIGHT_LOW_EVENT", ORDER)
    assert miss["top_hit"] == 0.0 and miss["log_loss"] > 10  # zero probability on what happened is punished hard
    br = multiclass_scores(base_rates()["frequency"], "OPEN_GAME", ORDER)
    assert 0 < br["brier"] < 2


def test_final_pregame_never_selects_a_row_at_or_after_the_start():
    rows = [{"game_id": "g", "t": "2026-10-06T21:00:00Z", "v": 1}, {"game_id": "g", "t": "2026-10-06T22:59:00Z", "v": 2},
            {"game_id": "g", "t": "2026-10-06T23:00:00Z", "v": 3}, {"game_id": "g", "t": "2026-10-07T01:00:00Z", "v": 4}]
    out = final_pregame(rows, "game_id", "t", lambda r: START)
    assert out["g"]["v"] == 2


def test_stage_gates_are_conservative_and_ignore_roi():
    small = {"games_settled": 43, "final_pregame_contracts_settled": 7626, "script_forecasts_settled": 0, "candidate_clv_sample": 370}
    st = learning_stage(small, {"brier_close_both_halves": True, "no_family_bias": True})
    assert st["stage"] == "EARLY_LEARNING" and st["next_stage"] == "CALIBRATION_BUILDING"
    mid = small | {"games_settled": 150}
    assert learning_stage(mid, {})["stage"] == "CALIBRATION_BUILDING"
    big = {"games_settled": 900, "final_pregame_contracts_settled": 90000, "script_forecasts_settled": 900, "candidate_clv_sample": 5000}
    all_ok = dict.fromkeys(("brier_close_both_halves", "no_family_bias", "brier_le_market_both_halves", "candidate_clv_positive", "scripts_beat_base_rate"), True)
    assert learning_stage(big, all_ok)["stage"] == "VALIDATED"
    assert learning_stage(big, all_ok | {"candidate_clv_positive": False})["stage"] == "EVIDENCE_EMERGING"
    assert "ROI is never a criterion" in st["note"]


def test_small_sample_metrics_say_so():
    assert mean_ci([0.01, -0.02, 0.03])["small_sample"] is True
    assert binary_metrics([], [])["n"] == 0
    m = binary_metrics([0.6] * 50, [1] * 30 + [0] * 20)
    assert m["n"] == 50 and m["calibration"][0]["observed"] == pytest.approx(0.6)


def _final_row() -> dict:
    return {"game_id": "2026020099", "status": "final", "home_team_id": 1, "away_team_id": 2, "home_final": 4, "away_final": 1, "home_reg": 4,
            "away_reg": 1, "last_period_type": "REG", "source": "nhl_api_boxscore", "fetched_at_utc": "2026-10-07T02:00:00Z", "stat_correction_version": 0}


def test_run_learning_scores_pregame_forecasts_once_and_never_rewrites_them(tmp_path):
    led = Ledger(tmp_path)
    probs = {k: round(1 / len(ORDER), 6) for k in ORDER}
    pre = {"game_id": "2026020099", "decided_at_utc": "2026-10-06T22:30:00Z", "snapshot_id": "snap-a", "script_version": "NHL_SCRIPT_V1",
           "home": "HOM", "away": "AWY", "script_probabilities": probs, "candidates": []}
    late = pre | {"decided_at_utc": "2026-10-06T23:10:00Z", "snapshot_id": "snap-late"}  # after the puck drop: never scored
    led.append_rows("script_forecasts", [pre, late], observed_at=START)
    led.append_rows("results", [_final_row()], observed_at=START)
    goals = [{"game_id": "2026020099", "team_id": 1, "period": p, "period_type": "REG", "t_s": t, "strength": "EV", "empty_net": False}
             for p, t in ((1, 200), (2, 1400), (3, 2700), (3, 3300))] + \
            [{"game_id": "2026020099", "team_id": 2, "period": 2, "period_type": "REG", "t_s": 1900, "strength": "EV", "empty_net": False}]
    goalies = [{"game_id": "2026020099", "team_id": 1, "shots_against": 24, "saves": 23, "starter": True},
               {"game_id": "2026020099", "team_id": 2, "shots_against": 33, "saves": 29, "starter": True}]
    led.append_rows("player_events/goals", goals, observed_at=START)
    led.append_rows("player_events/goalies", goalies, observed_at=START)
    now = datetime(2026, 10, 7, 4, 0, tzinfo=UTC)
    rep = run_learning(led, {}, {"2026020099": START}, obs_loader=lambda t: {}, now=now)
    pm = list(Ledger(tmp_path).iter_rows("script_postmortems"))
    assert len(pm) == 1 and pm[0]["snapshot_id"] == "snap-a" and pm[0]["realized_script"] == "HOME_CONTROL"
    assert pm[0]["base_rate_brier"] is not None and rep["scripts"]["n_games"] == 1
    assert rep["counts"]["script_forecasts"] == 2 and rep["counts"]["script_forecasts_settled"] == 1
    fc = list(Ledger(tmp_path).iter_rows("script_forecasts"))
    assert [f["script_probabilities"] for f in fc] == [probs, probs]  # the forecast rows are untouched
    run_learning(Ledger(tmp_path), {}, {"2026020099": START}, obs_loader=lambda t: {}, now=now)
    assert len(list(Ledger(tmp_path).iter_rows("script_postmortems"))) == 1  # deduped, append-only
    assert json.loads((tmp_path / "eval" / "report_learning.json").read_text())["stage"]["stage"] == "EARLY_LEARNING"


# ------------------------------------------------------------------------------------------------ publication layer
def test_raw_statistics_are_never_betting_evidence():
    obs = lambda mid, v, rank: {"metric_id": mid, "value": v, "context": {"rank": rank, "universe_size": 32}}  # noqa: E731
    mid = lambda s: f"met_nhl.{s}"  # noqa: E731
    team_obs = {1: [obs(mid("oa_xgf60_5v5"), 2.9, 2), obs(mid("oa_xga60_5v5"), 2.4, 3), obs(mid("oa_xgf_pct_5v5"), 0.55, 2), obs(mid("pp_pct"), 0.27, 1),
                    obs(mid("pk_pct"), 0.85, 2)],
                2: [obs(mid("oa_xgf60_5v5"), 2.3, 30), obs(mid("oa_xga60_5v5"), 2.9, 31), obs(mid("oa_xgf_pct_5v5"), 0.45, 31), obs(mid("pp_pct"), 0.15, 30),
                    obs(mid("pk_pct"), 0.75, 31)]}
    pg = {"goaltending": {"home": {"status": "CONFIRMED", "player_name": "A", "factor": 0.9}, "away": {"status": "UNKNOWN"}},
          "context": {"away_b2b": True}, "model": {"sim": {"home_lambda": 3.4, "away_lambda": 2.5, "p_home_win": 0.66, "total_mean": 5.9}}}
    out = matchup_findings(home="HOM", away="AWY", home_tid=1, away_tid=2, team_obs=team_obs, mid=mid, packet_game=pg, injuries={"AWY": 3}, scripts=None)
    by_basis = {}
    for f in out["findings"]:
        by_basis.setdefault(f["basis"], []).append(f)
        assert f["evidence_eligible"] == (f["basis"] in EVIDENCE_BASES)
    assert by_basis["RAW"] and all(not f["evidence_eligible"] and "Not opponent-adjusted" in f["text"] for f in by_basis["RAW"])
    assert by_basis["OPPONENT_ADJUSTED"] and all("opponent-adjusted" in f["text"].lower() for f in by_basis["OPPONENT_ADJUSTED"])
    wm = [f for f in out["findings"] if f["id"] in out["what_matters"]]
    assert 1 <= len(wm) <= 5 and all(f["basis"] != "RAW" for f in wm)
    assert any(f["id"] == "goalie_status_away" for f in out["findings"])


def test_scripts_extension_is_explicit_when_a_game_is_not_simulated_and_notes_are_deterministic():
    x = scripts_extension(None, generated_at=None, start_time_utc="2026-10-07T23:00:00Z", event_tickers=set())
    assert x["status"] == "NOT_SIMULATED" and "game day" in x["reason"]
    assert script_notes(x) == []


def test_learning_extension_reports_a_failed_job_instead_of_looking_healthy():
    rep = {"version": "nhl-learning-1.0", "counts": {"games_settled": 3}, "stage": {"stage": "EARLY_LEARNING"}}
    ok = learning_extension(rep, {"evaluated_at_utc": "x", "steps": {"learning": "OK"}})
    bad = learning_extension(rep, {"evaluated_at_utc": "x", "steps": {"learning": "FAILED: RuntimeError: boom"}})
    assert ok["status"] == "OK" and bad["status"] == "STALE_LAST_RUN_FAILED" and bad["job"]["learning_step"].startswith("FAILED")
    assert learning_extension(None, None)["status"] == "UNAVAILABLE"


def test_health_shows_a_broken_learning_job_as_degraded():
    from nhl_edge.app_export import learning_component

    now = "2026-10-07T00:00:00Z"
    bad = learning_component({"evaluated_at_utc": "2026-10-06T23:28:24Z", "steps": {"v1": "OK", "learning": "FAILED: RuntimeError: boom"}}, now)
    assert bad["status"] == "DEGRADED" and "boom" in bad["detail"]
    assert learning_component({"evaluated_at_utc": "2026-10-06T23:28:24Z", "steps": {"learning": "OK"}}, now)["status"] == "OK"
    assert learning_component({"evaluated_at_utc": "2026-10-01T00:00:00Z", "steps": {"learning": "OK"}}, now)["status"] == "STALE"
    assert learning_component(None, now)["status"] == "UNKNOWN"
