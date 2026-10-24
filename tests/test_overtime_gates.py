from __future__ import annotations

import gzip
import json
from datetime import UTC, datetime, timedelta

import numpy as np

from nhl_edge.research import overtime_gates as G

T = datetime(2026, 11, 1, 0, 0, tzinfo=UTC)


def _slate(gen, games):
    """games: [(game_id, start, p1, p2)]"""
    return {"generated_at_utc": gen.strftime("%Y-%m-%dT%H:%M:%SZ"), "date_et": "2026-10-31",
            "games": [{"game_id": g, "start_time_utc": s.strftime("%Y-%m-%dT%H:%M:%SZ"), "date_et": s.strftime("%Y-%m-%d")} for g, s, _, _ in games],
            "v2_shadow": {"blocks": [{"game_id": g, "v1": {"p_reg_tie": p1}, "v2": {"p_overtime": p2}} for g, _, p1, p2 in games]}}


def test_pairs_use_the_latest_snapshot_at_least_ten_minutes_before_the_start():
    start = T + timedelta(hours=3)
    slates = [_slate(start - timedelta(hours=5), [("g", start, 0.17, 0.21)]), _slate(start - timedelta(minutes=30), [("g", start, 0.18, 0.22)]),
              _slate(start - timedelta(minutes=5), [("g", start, 0.9, 0.9)])]                                         # too close to the drop: ignored
    pairs, cnt = G.pairs_from_slates(slates)
    assert len(pairs) == 1 and (pairs[0].p1, pairs[0].p2) == (0.18, 0.22) and cnt["games_with_pregame_pair"] == 1


def test_pairs_survive_a_promotion_because_v1_comes_from_the_shadow_block():
    start = T + timedelta(hours=3)
    s = _slate(start - timedelta(hours=1), [("g", start, 0.17, 0.21)])
    s["games"][0]["p_overtime"] = 0.21                                                                           # published field now shows V2
    pairs, _ = G.pairs_from_slates([s])
    assert (pairs[0].p1, pairs[0].p2) == (0.17, 0.21)


def test_outcomes_take_the_latest_final_regular_season_row():
    rows = [{"game_id": "2026020001", "status": "final", "last_period_type": "REG", "_observed_at_utc": "2026-10-01T00:00:00Z"},
            {"game_id": "2026020001", "status": "final", "last_period_type": "OT", "_observed_at_utc": "2026-10-02T00:00:00Z"},      # correction
            {"game_id": "2026020002", "status": "final", "last_period_type": "SO"}, {"game_id": "2026020003", "status": "live", "last_period_type": "REG"},
            {"game_id": "2026030001", "status": "final", "last_period_type": "OT"}]                                                      # playoff game
    assert G.outcomes_from_results(rows) == {"2026020001": 1, "2026020002": 1}


def _synthetic(n, true_gain=0.0022, seed=0):
    rng = np.random.default_rng(seed)
    base = rng.uniform(0.14, 0.26, n)
    y = (rng.random(n) < base * 1.25).astype(int)                                  # real OT rate above what V1 says
    p1 = np.clip(base - 0.03, 0.05, 0.45)
    p2 = np.clip(base + 0.0 * true_gain, 0.05, 0.45)
    pairs = [G.Pair(f"g{i}", f"2026-11-{1 + i // 7:02d}", T + timedelta(hours=i), T + timedelta(hours=i - 2), float(p1[i]), float(p2[i])) for i in range(n)]
    return pairs, {f"g{i}": int(y[i]) for i in range(n)}


def test_the_gate_is_in_progress_until_the_registered_sample_and_can_stop_for_harm_only():
    pairs, out = _synthetic(300)
    rep = G.evaluate_live(pairs, out, t0=T)
    assert rep["status"] in ("IN_PROGRESS", "FAILED_HARM") and "250" in rep["looks"]
    # V2 clearly worse than V1: the harm look (99%) fails the gate
    bad = [G.Pair(p.game_id, p.date_et, p.start, p.snapshot, p.p2, max(p.p2 - 0.14, 0.01)) for p in pairs]
    rep_bad = G.evaluate_live(bad, out, t0=T)
    assert rep_bad["status"] == "FAILED_HARM" and rep_bad["looks"]["250"]["significantly_worse"]


def test_no_interim_look_can_pass_the_gate_and_games_before_t0_do_not_count():
    pairs, out = _synthetic(900)
    assert G.evaluate_live(pairs, out, t0=T)["status"] in ("IN_PROGRESS", "FAILED_HARM")
    assert G.evaluate_live(pairs, out, t0=T + timedelta(days=3650))["status"] == "NO_DATA"


def test_the_primary_look_passes_only_when_every_registered_check_holds():
    pairs, out = _synthetic(1100, seed=3)
    rep = G.evaluate_live(pairs, out, eligible_games=1150, t0=T, fallback_rate=0.0)
    assert rep["status"] in ("PASS", "EXTENSION", "FAILED")
    assert rep["looks"]["primary"]["n"] == G.PRIMARY_N and set(rep["looks"]["primary"]["checks"]) == {"upper95_below_margin", "delta_negative", "calibration_within_tol", "pair_coverage_ok", "fallback_ok"}
    low = G.evaluate_live(pairs, out, eligible_games=2000, t0=T, fallback_rate=0.0)                                # 55% pair coverage can never pass
    assert low["status"] != "PASS" and low["looks"]["primary"]["checks"]["pair_coverage_ok"] is False
    fb = G.evaluate_live(pairs, out, eligible_games=1150, t0=T, fallback_rate=0.2)
    assert fb["status"] != "PASS" and fb["looks"]["primary"]["checks"]["fallback_ok"] is False


def test_worker_runtime_summarises_only_cycles_that_ran_simulate():
    st = {"cycles": [{"jobs_run": ["simulate"], "duration_s": 100.0}, {"jobs_run": ["simulate"], "duration_s": 400.0}, {"jobs_run": [], "duration_s": 999.0}]}
    r = G.worker_runtime(st)
    assert r["n_cycles"] == 2 and r["max_s"] == 400.0 and r["share_over_budget"] == 0.5 and r["pass"] is False


def test_process_determinism_gives_one_hash_across_hash_seeds():
    r = G.process_determinism(("0", "7"))
    assert r["identical"], r


def test_archive_replay_reproduces_a_stored_block_exactly_and_flags_a_tampered_one(tmp_path):
    from nhl_edge.sim.engine import TeamParams
    from nhl_edge.sim.engine_v2 import load_params, simulate_game_v2

    seed, lam_h, lam_a = 4242, 3.1, 2.9
    sm = simulate_game_v2(TeamParams(7, "AAA", lam_h), TeamParams(8, "BBB", lam_a), seed=seed ^ 0x5F3759DF, n_sims=2000, params=load_params()).summary()
    blk = {"game_id": "1", "detail": {"lam_home": lam_h, "lam_away": lam_a}, "v2": {k: sm[k] for k in ("p_home_win", "p_reg_tie", "p_overtime")}}

    def write(name, block):
        d = tmp_path / "slates" / "dt=2026-10-30" / name
        d.mkdir(parents=True)
        (d / "slate.json").write_text(json.dumps({"n_sims": 2000, "games": [{"game_id": "1", "seed": seed, "home": "AAA", "away": "BBB", "home_team_id": 7, "away_team_id": 8}],
                                                  "v2_shadow": {"blocks": [block]}}))
    write("20261030T000000Z_a", blk)
    assert G.archive_replay(tmp_path, limit=10)["mismatches"] == 0
    write("20261030T010000Z_b", {**blk, "v2": {**blk["v2"], "p_overtime": blk["v2"]["p_overtime"] + 1e-9}})
    r = G.archive_replay(tmp_path, limit=10)
    assert r["checked"] == 2 and r["mismatches"] == 1 and r["pass"] is False
    gzip  # noqa: B018  (module kept imported for fixtures that write archives)


def test_g7_inputs_a_late_team_games_st_snapshot_never_reaches_the_v2_run(tmp_path, monkeypatch):
    """The only input V2 reads beyond V1's (special-teams rows) is cut at the run's instant; a snapshot observed after it is invisible."""
    from datetime import timedelta

    from nhl_edge.archive.ledger import Ledger
    from nhl_edge.workflows import shadow_v2, simulate
    from tests.archive_fixture import NOW, build_archive

    root = tmp_path / "a"
    build_archive(root)
    led = Ledger(root)
    led.append_rows("context/team_games_st", [{"team": "AAA", "marker": "early"}], observed_at=NOW - timedelta(hours=1), meta={})
    led.append_rows("context/team_games_st", [{"team": "AAA", "marker": "LATE"}], observed_at=NOW + timedelta(hours=1), meta={})
    seen = {}

    def spy(items, data_root, live_st, *a, **k):
        seen["rows"] = live_st
        raise RuntimeError("stop after capturing the input")

    monkeypatch.setattr(shadow_v2, "run_shadow", spy)
    monkeypatch.setenv("NHL_EDGE_V2_SHADOW", "1")
    simulate._run_v2_shadow(led, [{"gi": None}], tmp_path, 100, NOW, None, None)
    assert [r["marker"] for r in seen["rows"]] == ["early"]
