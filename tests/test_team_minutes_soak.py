"""The soak evaluator: every NO-GO trigger of GO_NO_GO.md with its stated threshold, on a synthetic archive."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta

import numpy as np

from nhl_edge.archive.ledger import Ledger
from nhl_edge.research import team_minutes_soak as K

T0 = datetime(2026, 11, 1, 20, 0, tzinfo=UTC)
SINCE = "2026-10-28T00:11:43Z"


def _iso(t):
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


def _build(tmp_path, n_games, cand_better=True, fallback=False, error_runs=0, pin_published=False, mismatch=False, many_runs=20):
    led = Ledger(tmp_path / "arch", run_id="r")
    rng = np.random.default_rng(1)
    shadow, pred, act = [], [], []
    now = T0
    for g in range(n_games):
        gid = f"2026021{g:03d}"
        for i in range(2):
            pid = g * 10 + i
            actual_toi = 17.0 + rng.normal(0, 1)
            legacy = 16.2
            cand = 16.9 if cand_better else 15.0
            row = {"game_id": gid, "side": "home", "team": "AAA", "team_id": 1, "player_id": pid, "name": f"P{pid}", "pos": "F" if i == 0 else "D", "predicted_at_utc": _iso(now),
                   "minutes_to_start": 40.0, "horizon_label": "T-30m", "pregame": True, "run_id": "r", "published_allocation": "team-minutes-0", "candidate_version": "team-minutes-1.0",
                   "candidate_fingerprint": "x", "clock_fallback": bool(fallback and g == 0), "projection_quality": "STANDARD", "deployment_source": "LINES_PROJECTED", "role": "SHADOW"}
            for k, (a, b, _y) in {"toi": (legacy, cand, actual_toi), "ev": (13.0, 13.3, 13.5), "pp": (1.2, 1.6 if cand_better else 0.5, 1.6), "sh": (1.0, 1.1, 1.1), "sog": (2.0, 2.1, 2.0)}.items():
                row[f"legacy_{k}"], row[f"cand_{k}"] = a, b
            shadow.append(row)
            p = {"game_id": gid, "player_id": pid, "ticker": f"T{pid}", "predicted_at_utc": _iso(now), "meta_expected_toi_min": 99.0 if mismatch and g == 0 and i == 0 else legacy,
                 "meta_expected_pp_toi_min": 1.2, "meta_expected_shots": 2.0}
            if pin_published and g == 0:
                p["meta_team_minutes_version"] = "team-minutes-1.0"
            pred.append(p)
            act.append({"game_id": gid, "game_type": 2, "shifts_ok": True, "player_id": pid, "toi_s": actual_toi * 60, "toi_pp_s": 96, "toi_sh_s": 66, "toi_ev_s": 810, "sog": int(rng.poisson(2))})
        now += timedelta(seconds=1)
    led.append_rows("player_tm_shadow", shadow, observed_at=T0 - timedelta(seconds=1), meta={"published_allocation": "team-minutes-0", "n_errors": 0})
    led.append_rows("predictions_player", pred, observed_at=T0, meta={})
    led.append_rows("player_events/players", act, observed_at=T0 + timedelta(hours=6), meta={})
    # extra runs (manifest entries only matter for the error-run fraction)
    for k in range(many_runs):
        Ledger(tmp_path / "arch", run_id=f"x{k}").append_rows("player_tm_shadow", [dict(shadow[0], player_id=None, marker=True)] if k < error_runs else [], observed_at=T0 + timedelta(minutes=k + 1),
                                                                meta={"published_allocation": "team-minutes-0", "n_errors": 1 if k < error_runs else 0})
    return tmp_path / "arch"


def test_nothing_accumulated_yet_is_reported_as_undetermined_not_as_a_pass(tmp_path):
    (tmp_path / "arch").mkdir()
    res = K.evaluate(tmp_path / "arch", SINCE, n_boot=50)
    assert res["settled_games"] == 0 and res["soak_complete"] is False and res["activation_evidence_complete"] is False
    assert "T1_mse_upper_bound_above_zero" in res["triggers_undetermined"]


def test_a_complete_clean_soak_reports_complete_evidence(tmp_path):
    arch = _build(tmp_path, 100)
    res = K.evaluate(arch, SINCE, n_boot=100)
    assert res["settled_games"] == 100 and res["soak_complete"] is True
    assert res["triggers_failed"] == [] and res["triggers_undetermined"] == [] and res["activation_evidence_complete"] is True
    assert res["triggers"]["T4_published_surface_changed"]["published_vs_shadow_template_arm"]["mismatches"] == 0
    assert "activation evidence complete: True" in K.markdown(res)


def test_fewer_than_100_games_is_never_complete_even_when_clean(tmp_path):
    res = K.evaluate(_build(tmp_path, 40), SINCE, n_boot=100)
    assert res["soak_complete"] is False and res["activation_evidence_complete"] is False and res["triggers_failed"] == []
    assert res["triggers"]["T1_mse_upper_bound_above_zero"]["final"] is False


def test_t1_and_t2_fire_when_the_candidate_is_worse(tmp_path):
    res = K.evaluate(_build(tmp_path, 100, cand_better=False), SINCE, n_boot=100)
    assert "T1_mse_upper_bound_above_zero" in res["triggers_failed"] or "T2_candidate_bias_larger_in_magnitude" in res["triggers_failed"]
    assert res["activation_evidence_complete"] is False


def test_t3a_fallback_share_above_two_percent_fires_and_at_two_percent_does_not(tmp_path):
    res = K.evaluate(_build(tmp_path, 30, fallback=True), SINCE, n_boot=50)            # 2 of 60 rows = 3.3% > 2%
    assert res["triggers"]["T3a_clock_fallback_share_above_2pct"]["fails"] is True
    res = K.evaluate(_build(tmp_path / "b", 100, fallback=True), SINCE, n_boot=50)     # 2 of 200 rows = 1% <= 2%
    assert res["triggers"]["T3a_clock_fallback_share_above_2pct"]["fails"] is False


def test_t3b_more_than_one_run_in_ten_fires(tmp_path):
    ok = K.evaluate(_build(tmp_path, 30, error_runs=2, many_runs=20), SINCE, n_boot=50)           # 2 error runs of 21 = 9.5% (not more than one in ten)
    assert ok["triggers"]["T3b_error_runs_above_one_in_ten"]["fails"] is False
    bad = K.evaluate(_build(tmp_path / "b", 30, error_runs=4, many_runs=20), SINCE, n_boot=50)    # 4 of 21 = 19%
    assert bad["triggers"]["T3b_error_runs_above_one_in_ten"]["fails"] is True


def test_t4_fires_when_a_published_row_carries_allocation_fields_or_differs_from_the_template_arm(tmp_path):
    a = K.evaluate(_build(tmp_path, 30, pin_published=True), SINCE, n_boot=50)
    assert a["triggers"]["T4_published_surface_changed"]["fails"] is True and a["triggers"]["T4_published_surface_changed"]["rows_with_allocation_or_legacy_fields"] > 0
    b = K.evaluate(_build(tmp_path / "b", 30, mismatch=True), SINCE, n_boot=50)
    assert b["triggers"]["T4_published_surface_changed"]["fails"] is True and b["triggers"]["T4_published_surface_changed"]["published_vs_shadow_template_arm"]["mismatches"] == 1


def test_thresholds_are_the_ones_written_in_go_no_go():
    text = (K.Path(__file__).resolve().parents[1] / "docs" / "research" / "team_minutes" / "GO_NO_GO.md").read_text()
    assert "more than 2% of shadow rows" in text and "one run in ten" in text and "100 settled games" in text
    assert K.SOAK_GAMES == 100 and K.MAX_FALLBACK_SHARE == 0.02 and K.MAX_ERROR_RUN_FRACTION == 0.10
