from __future__ import annotations

import json
from datetime import UTC, datetime, timedelta

from nhl_edge.worker import lc_dispatch as L
from nhl_edge.worker.pf_dispatch import RunInfo

NOW = datetime(2026, 11, 3, 18, 0, tzinfo=UTC)


def _run(i, created, status="completed", conclusion="success", event="workflow_dispatch", minutes=6):
    return RunInfo(i, status, conclusion, event, created, created + timedelta(minutes=minutes) if status == "completed" else None, "workload-shadow")


def test_nothing_is_requested_when_every_upcoming_game_is_covered_by_a_run_inside_its_horizon():
    tip = NOW + timedelta(hours=3)
    d = L.decide(NOW, [tip], [_run(1, NOW - timedelta(hours=5))])
    assert d.action == "idle" and d.code == "COVERED" and d.gap is False and d.recovered is True


def test_a_game_without_a_covering_run_inside_the_window_triggers_one_request():
    tip = NOW + timedelta(hours=3)
    d = L.decide(NOW, [tip], [_run(1, NOW - timedelta(hours=20))])
    assert d.action == "dispatch" and d.code == "DUE" and d.uncovered == 1 and d.gap is False         # 3 h ahead: not yet an alert


def test_games_outside_the_dispatch_window_wait_and_games_too_close_cannot_be_helped():
    assert L.decide(NOW, [NOW + timedelta(hours=9)], []).code == "OUTSIDE_WINDOW"
    d = L.decide(NOW, [NOW + timedelta(minutes=12)], [])
    assert d.action == "wait" and d.code == "TOO_CLOSE" and d.gap is True                                 # a record is actually about to be missing


def test_never_queues_a_second_request_while_one_is_in_flight_and_that_run_counts_as_covering():
    tip = NOW + timedelta(minutes=60)
    queued = _run(2, NOW - timedelta(minutes=5), status="queued", conclusion=None)
    d = L.decide(NOW, [tip], [queued])
    assert d.action == "idle" and d.code == "COVERED" and d.gap is False                                 # covered by the pending run: no alert, no second request


def test_a_run_that_finished_too_late_for_the_game_does_not_cover_it():
    tip = NOW + timedelta(minutes=40)
    late = _run(3, NOW - timedelta(minutes=2), minutes=1)                  # created and finished at ~17:59, i.e. < 40 min ago... but it is before the tip by > 10 min
    assert L._covered(tip, NOW, [late]) is True
    after = _run(4, tip + timedelta(minutes=1), minutes=1)
    assert L._covered(tip, NOW, [after]) is False                           # a run created after the drop never covers it


def test_a_lost_in_flight_run_stops_blocking_and_stops_covering():
    tip = NOW + timedelta(minutes=80)
    lost = _run(5, NOW - timedelta(hours=5), status="in_progress", conclusion=None)
    d = L.decide(NOW, [tip], [lost])
    assert d.action == "dispatch" and d.gap is True


def test_spacing_daily_cap_and_failure_backoff():
    tip = NOW + timedelta(hours=2)
    assert L.decide(NOW, [tip], [], last_dispatch_at=NOW - timedelta(minutes=5)).code == "SPACING"
    assert L.decide(NOW, [tip], [], dispatched_today=L.MAX_DISPATCHES_PER_DAY).code == "DAILY_CAP"
    fails = [_run(10 + i, NOW - timedelta(minutes=40 + 10 * i), conclusion="failure", minutes=2) for i in range(3)]
    d = L.decide(NOW, [tip], fails)
    assert d.action == "wait" and d.code == "BACKOFF"


def test_the_gap_alert_is_about_missing_records_only():
    tip = NOW + timedelta(minutes=60)
    gap = L.decide(NOW, [tip], [])
    assert gap.gap is True and gap.recovered is False
    ok = L.decide(NOW, [tip], [_run(1, NOW - timedelta(hours=1))])
    assert ok.gap is False and ok.recovered is True


def test_the_dispatcher_dispatches_once_and_respects_spacing_and_never_raises():
    calls = []
    d = L.LcDispatcher("o/r", "main", "t", list_fn=lambda: [], dispatch_fn=lambda: calls.append(1) or True)
    tip = NOW + timedelta(hours=2)
    assert d.step(NOW, [tip])["dispatched"] is True
    assert d.step(NOW + timedelta(minutes=3), [tip])["code"] == "SPACING" and len(calls) == 1
    assert L.LcDispatcher("o/r", "main", "t", list_fn=lambda: None).step(NOW, [tip])["code"] == "API_UNREADABLE"

    def boom():
        raise RuntimeError("x")
    assert L.LcDispatcher("o/r", "main", "t", list_fn=boom).step(NOW, [tip])["code"] == "DISPATCHER_ERROR"
    refused = L.LcDispatcher("o/r", "main", "t", list_fn=lambda: [], dispatch_fn=lambda: False).step(NOW, [tip])
    assert refused["action"] == "wait" and refused["code"] == "DISPATCH_REFUSED"


def test_schedule_tips_keep_regular_season_games_that_have_not_started(tmp_path):
    import json

    p = tmp_path / "s.jsonl"
    rows = [{"season_type": "regular", "status": "not_started", "start_time_utc": "2026-11-03T23:00:00Z"}, {"season_type": "preseason", "status": "not_started", "start_time_utc": "2026-11-03T22:00:00Z"},
            {"season_type": "regular", "status": "final", "start_time_utc": "2026-11-03T20:00:00Z"}, {"season_type": "regular", "status": "not_started", "start_time_utc": "bad"}]
    p.write_text("\n".join(json.dumps(r) for r in rows))
    assert L.regular_tips_from_schedule([p]) == [datetime(2026, 11, 3, 23, 0, tzinfo=UTC)]


# ---------------------------------------------------------------------------------------------- worker integration
class _Clock:
    def __init__(self, t):
        self.t = t

    def now(self):
        return self.t

    def sleep(self, s):
        self.t += timedelta(seconds=s)


def _worker(tmp_path, lc_fn):
    from nhl_edge.worker.run import Worker

    c = _Clock(NOW)
    w = Worker(data_root=tmp_path / "d", archive_root=tmp_path / "a", worker_id="w", now_fn=c.now, sleep_fn=c.sleep, run_fn=lambda cmd, t: (0, ""),
               schedule_fn=lambda: [{"start_time_utc": "2026-11-03T22:00:00Z"}], decide_fn=lambda: {}, lifetime_minutes=300.0, lc_fn=lc_fn)
    w._push = lambda msg: True
    return w


def test_the_worker_records_the_lc_decision_and_a_crashing_dispatcher_never_breaks_capture(tmp_path):
    seen = []
    rec = _worker(tmp_path, lambda now, tips: seen.append(tips) or {"action": "dispatch", "code": "DUE", "dispatched": True, "uncovered": 1, "next_uncovered_in_min": 240.0, "gap": False,
                                                                    "reason": "x"})._one_cycle(NOW)
    assert rec.lc == {"action": "dispatch", "code": "DUE", "dispatched": True, "uncovered": 1, "next_uncovered_in_min": 240.0, "gap": False} and seen
    assert rec.capture_ok and rec.push_ok

    def boom(now, tips):
        raise RuntimeError("api down")
    rec2 = _worker(tmp_path, boom)._one_cycle(NOW)
    assert rec2.lc["code"] == "DISPATCHER_ERROR" and rec2.capture_ok and rec2.push_ok
    assert _worker(tmp_path, None)._one_cycle(NOW).lc is None


def test_the_cli_main_dispatches_from_a_schedule_snapshot(monkeypatch, tmp_path):
    import json

    sched = tmp_path / "s.jsonl"
    sched.write_text(json.dumps({"season_type": "regular", "status": "not_started", "start_time_utc": "2026-11-03T20:00:00Z"}) + "\n")
    out = tmp_path / "o.txt"
    monkeypatch.setenv("GITHUB_TOKEN", "t")
    sent = []
    monkeypatch.setattr(L, "list_runs_via_api", lambda repo, token, workflow=L.WORKFLOW, per_page=100: [])
    monkeypatch.setattr(L, "dispatch_via_api", lambda repo, ref, token, workflow=L.WORKFLOW: sent.append(workflow) or True)
    assert L.main(["dispatch", "--schedule", str(sched), "--repo", "o/r", "--now", "2026-11-03T18:00:00Z", "--github-output", str(out)]) == 0
    o = dict(line.split("=", 1) for line in out.read_text().split())
    assert sent == ["workload_shadow.yml", "player_minutes.yml"] and o["lc_action"] == "dispatch" and o["lc_gap"] == "false"


def test_the_minutes_request_is_best_effort_and_never_changes_the_lc_result(monkeypatch):
    sent = []
    monkeypatch.setattr(L, "dispatch_via_api", lambda repo, ref, token, workflow=L.WORKFLOW: sent.append(workflow) or workflow == L.WORKFLOW)
    assert L._dispatch_both("o/r", "main", "t") is True and sent == ["workload_shadow.yml", "player_minutes.yml"]
    sent.clear()
    monkeypatch.setattr(L, "dispatch_via_api", lambda repo, ref, token, workflow=L.WORKFLOW: sent.append(workflow) or False)
    assert L._dispatch_both("o/r", "main", "t") is False and sent == ["workload_shadow.yml"]       # LC refused: nothing else is asked for


def test_drill_ignores_existing_runs_but_uses_the_real_dispatch_function(tmp_path, monkeypatch):
    sched = tmp_path / "s.jsonl"
    sched.write_text(json.dumps({"season_type": "regular", "status": "not_started", "start_time_utc": "2026-11-03T20:00:00Z"}) + "\n")
    monkeypatch.setenv("GITHUB_TOKEN", "t")
    sent = []
    # a covering run exists on the platform; without --drill the game would be COVERED and nothing would be sent
    covering = [RunInfo(id=1, status="completed", conclusion="success", event="schedule", created_at=datetime(2026, 11, 3, 10, 0, tzinfo=UTC), updated_at=datetime(2026, 11, 3, 10, 5, tzinfo=UTC))]
    monkeypatch.setattr(L, "list_runs_via_api", lambda repo, token, workflow=L.WORKFLOW, per_page=100: covering)
    monkeypatch.setattr(L, "dispatch_via_api", lambda repo, ref, token, workflow=L.WORKFLOW: sent.append(workflow) or True)
    args = ["dispatch", "--schedule", str(sched), "--repo", "o/r", "--now", "2026-11-03T18:00:00Z"]
    assert L.main(args) == 0 and sent == []
    assert L.main([*args, "--drill"]) == 0 and sent == ["workload_shadow.yml", "player_minutes.yml"]
    assert L.main(["decide", "--schedule", str(sched), "--repo", "o/r", "--drill"]) == 2
