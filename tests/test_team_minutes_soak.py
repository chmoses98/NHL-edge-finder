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


PER_TEAM = 10


def _build(tmp_path, n_games, cand_better=True, fallback=False, error_runs=0, pin_published=False, mismatch=False, many_runs=20, missing_runs=0, dup=False, unsettled=0,
           incomplete_games=0, nan_outcomes=0, one_team_games=0, extra_run=False):
    """n_games settled games of 2 x 10 skaters each, all in ONE simulate run at T0 (+ optional extras described by the keyword arguments)."""
    led = Ledger(tmp_path / "arch", run_id="r")
    rng = np.random.default_rng(1)
    shadow, pred, act = [], [], []
    at = _iso(T0)
    for g in range(n_games + unsettled):
        gid = f"2026021{g:03d}"
        settled = g < n_games
        for i in range(2 * PER_TEAM):
            pid = g * 100 + i
            team = "AAA" if (i < PER_TEAM or g < one_team_games) else "BBB"
            actual_toi = 17.0 + rng.normal(0, 1)
            legacy = 16.2
            cand = 16.9 if cand_better else 15.0
            fb = bool((fallback and g == 0) or not settled)
            row = {"game_id": gid, "side": "home", "team": team, "team_id": 1, "player_id": pid, "name": f"P{pid}", "pos": "F" if i % 2 == 0 else "D", "predicted_at_utc": at,
                   "minutes_to_start": 40.0, "horizon_label": "T-30m", "pregame": True, "run_id": "r", "published_allocation": "team-minutes-0", "candidate_version": "team-minutes-1.0",
                   "candidate_fingerprint": "84aaf65e0f3b3ea3", "clock_fallback": fb, "projection_quality": "STANDARD", "deployment_source": "LINES_PROJECTED", "role": "SHADOW"}
            for k, (a_, b_) in {"toi": (legacy, cand), "ev": (13.0, 13.3), "pp": (1.2, 1.6 if cand_better else 0.5), "sh": (1.0, 1.1), "sog": (2.0, 2.1)}.items():
                row[f"legacy_{k}"], row[f"cand_{k}"] = a_, b_
            shadow.append(row)
            p = {"game_id": gid, "player_id": pid, "ticker": f"T{pid}", "predicted_at_utc": at, "pregame": True, "minutes_to_start": 40.0,
                 "meta_expected_toi_min": 99.0 if mismatch and g == 0 and i == 0 else legacy, "meta_expected_pp_toi_min": 1.2, "meta_expected_shots": 2.0}
            if pin_published and g == 0:
                p["meta_team_minutes_version"] = "team-minutes-1.0"
            pred.append(p)
            keep = settled and not (g < incomplete_games and i >= 3)                              # an incomplete game: only 3 players have an outcome row
            if keep:
                toi = float("nan") if (nan_outcomes and g < nan_outcomes and i < 18) else actual_toi * 60
                act.append({"game_id": gid, "game_type": 2, "shifts_ok": True, "player_id": pid, "toi_s": toi, "toi_pp_s": 96, "toi_sh_s": 66, "toi_ev_s": 810, "sog": int(rng.poisson(2))})
    led.append_rows("player_tm_shadow", shadow, observed_at=T0, meta={"published_allocation": "team-minutes-0", "n_errors": 0})
    if dup:                                                                                    # the same run recorded twice (different run id, same instant and rows)
        Ledger(tmp_path / "arch", run_id="dup").append_rows("player_tm_shadow", shadow, observed_at=T0, meta={"published_allocation": "team-minutes-0", "n_errors": 0})
    led.append_rows("predictions_player", pred, observed_at=T0, meta={})
    led.append_rows("player_events/players", act, observed_at=T0 + timedelta(hours=6), meta={})
    if extra_run:                                                                              # a LATER run for the same games: more rows, no more games
        t1 = T0 + timedelta(hours=1)
        l2 = Ledger(tmp_path / "arch", run_id="r2")
        l2.append_rows("player_tm_shadow", [dict(r, predicted_at_utc=_iso(t1), minutes_to_start=25.0) for r in shadow], observed_at=t1, meta={"published_allocation": "team-minutes-0", "n_errors": 0})
        l2.append_rows("predictions_player", [dict(r, predicted_at_utc=_iso(t1), minutes_to_start=25.0) for r in pred], observed_at=t1, meta={})
    # runs that EXPECTED shadow records but wrote none (a crash / swallowed failure): published rows inside the window, no shadow entry
    for k in range(missing_runs):
        t = T0 + timedelta(hours=2 + k)
        Ledger(tmp_path / "arch", run_id=f"m{k}").append_rows("predictions_player", [dict(pred[0], predicted_at_utc=_iso(t))], observed_at=t, meta={})
    # extra shadow runs with errors / markers (manifest entries only matter for the failed-run fraction)
    for k in range(many_runs):
        Ledger(tmp_path / "arch", run_id=f"x{k}").append_rows("player_tm_shadow", [dict(shadow[0], player_id=None, marker=True)] if k < error_runs else [], observed_at=T0 + timedelta(days=1, minutes=k),
                                                                meta={"published_allocation": "team-minutes-0", "n_errors": 1 if k < error_runs else 0})
    return tmp_path / "arch"


def test_nothing_accumulated_yet_is_reported_as_undetermined_not_as_a_pass(tmp_path):
    (tmp_path / "arch").mkdir()
    res = K.evaluate(tmp_path / "arch", SINCE, n_boot=50)
    assert res["settled_games"] == 0 and res["soak_complete"] is False and res["activation_evidence_complete"] is False
    assert "T1_mse_upper_bound_above_zero" in res["triggers_undetermined"]


def test_a_complete_clean_soak_reports_complete_evidence(tmp_path):
    arch = _build(tmp_path, 100, many_runs=0)
    res = K.evaluate(arch, SINCE, n_boot=100)
    assert res["settled_games"] == 100 and res["soak_complete"] is True
    assert res["triggers_failed"] == [] and res["triggers_undetermined"] == [] and res["activation_evidence_complete"] is True
    assert res["triggers"]["T4_published_surface_changed"]["published_vs_shadow_template_arm"]["mismatches"] == 0
    assert "activation evidence complete: True" in K.markdown(res)


def test_fewer_than_100_games_is_never_complete_even_when_clean(tmp_path):
    res = K.evaluate(_build(tmp_path, 40, many_runs=0), SINCE, n_boot=100)
    assert res["soak_complete"] is False and res["activation_evidence_complete"] is False and res["triggers_failed"] == []
    assert res["triggers"]["T1_mse_upper_bound_above_zero"]["final"] is False


def test_t1_and_t2_fire_when_the_candidate_is_worse(tmp_path):
    res = K.evaluate(_build(tmp_path, 100, cand_better=False, many_runs=0), SINCE, n_boot=100)
    assert "T1_mse_upper_bound_above_zero" in res["triggers_failed"] or "T2_candidate_bias_larger_in_magnitude" in res["triggers_failed"]
    assert res["activation_evidence_complete"] is False


def test_t3a_fallback_share_above_two_percent_fires_and_at_two_percent_does_not(tmp_path):
    res = K.evaluate(_build(tmp_path, 30, fallback=True), SINCE, n_boot=50)            # 20 of 600 rows = 3.3% > 2%
    assert res["triggers"]["T3a_clock_fallback_share_above_2pct"]["fails"] is True
    res = K.evaluate(_build(tmp_path / "b", 100, fallback=True), SINCE, n_boot=50)     # 20 of 2000 rows = 1% <= 2%
    assert res["triggers"]["T3a_clock_fallback_share_above_2pct"]["fails"] is False


def test_t3b_more_than_one_run_in_ten_fires(tmp_path):
    ok = K.evaluate(_build(tmp_path, 30, error_runs=2, many_runs=20), SINCE, n_boot=50)           # 2 failed runs of 21 = 9.5% (not more than one in ten)
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


def test_missing_expected_runs_count_as_failed_so_failures_cannot_be_understated(tmp_path):
    # 1 run wrote records; 3 further simulate runs had a game in the lead window but left NO shadow record and no marker -> 3 of 4 runs failed
    res = K.evaluate(_build(tmp_path, 30, many_runs=0, missing_runs=3), SINCE, n_boot=50)
    t = res["triggers"]["T3b_error_runs_above_one_in_ten"]
    assert res["run_health"]["expected_runs"] == 4 and t["missing_expected_runs"] == 3 and t["failed_runs"] == 3 and t["error_run_fraction"] == 0.75 and t["fails"] is True
    # a single missing run among eleven expected stays under one in ten only if it is 1 of >= 11: here 1 of 2 fails
    one = K.evaluate(_build(tmp_path / "b", 30, many_runs=0, missing_runs=1), SINCE, n_boot=50)
    assert one["triggers"]["T3b_error_runs_above_one_in_ten"]["fails"] is True


def test_duplicate_rows_and_repeated_runs_never_inflate_games_rows_or_runs(tmp_path):
    base = K.evaluate(_build(tmp_path, 100, many_runs=0), SINCE, n_boot=50)
    dup = K.evaluate(_build(tmp_path / "d", 100, many_runs=0, dup=True), SINCE, n_boot=50)
    rep = K.evaluate(_build(tmp_path / "r", 100, many_runs=0, extra_run=True), SINCE, n_boot=50)
    for r in (dup, rep):
        assert r["settled_games"] == 100 and base["settled_games"] == 100                       # unique games, not rows or runs
    assert dup["n_eligible_shadow_rows"] == base["n_eligible_shadow_rows"] == 2000              # duplicates collapse
    assert dup["comparison"]["n_paired_with_outcome"] == base["comparison"]["n_paired_with_outcome"] == 2000
    assert dup["run_health"]["runs_considered"] == base["run_health"]["runs_considered"] == 1
    assert rep["comparison"]["n_paired_with_outcome"] == 2000 and rep["run_health"]["expected_runs"] == 2   # the later run is a run, not more games


def test_incomplete_outcomes_and_single_team_games_do_not_count(tmp_path):
    res = K.evaluate(_build(tmp_path, 100, many_runs=0, incomplete_games=5), SINCE, n_boot=50)         # 5 games with only 3 outcome rows
    assert res["settled_games"] == 95 and res["soak_complete"] is False
    res = K.evaluate(_build(tmp_path / "n", 100, many_runs=0, nan_outcomes=4), SINCE, n_boot=50)        # 4 games with 18 of 20 outcomes missing / non-finite
    assert res["settled_games"] == 96
    res = K.evaluate(_build(tmp_path / "o", 100, many_runs=0, one_team_games=3), SINCE, n_boot=50)      # 3 games whose paired rows are all one team
    assert res["settled_games"] == 97
    assert res["comparison"]["n_paired_before_game_eligibility"] >= res["comparison"]["n_paired_with_outcome"]


def test_the_fallback_denominator_is_every_eligible_shadow_row_not_only_settled_ones(tmp_path):
    # 30 settled games without fallback + 20 unsettled games whose rows all used the fallback: the settled-only share would be 0%, the all-eligible share is 40%
    res = K.evaluate(_build(tmp_path, 30, many_runs=0, unsettled=20), SINCE, n_boot=50)
    t = res["triggers"]["T3a_clock_fallback_share_above_2pct"]
    assert t["n_eligible_rows"] == 1000 and abs(t["share"] - 0.4) < 1e-12 and t["fails"] is True
    assert res["comparison"]["n_paired_with_outcome"] == 600


def test_the_lead_window_constant_mirrors_the_archive_cap():
    from nhl_edge.research import team_minutes_shadow as S
    from nhl_edge.workflows import shadow_player

    assert S.MAX_LEAD_MIN == shadow_player.TM_SHADOW_MAX_LEAD_MIN
