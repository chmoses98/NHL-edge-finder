from __future__ import annotations

from datetime import UTC, datetime, timedelta

from nhl_edge.worker import pf_dispatch as P
from nhl_edge.worker.run import Worker

NOW = datetime(2026, 10, 22, 17, 0, tzinfo=UTC)
TIP = datetime(2026, 10, 22, 23, 0, tzinfo=UTC)     # 19:00 ET


def _run(i, created, *, status="completed", conclusion="success", event="workflow_dispatch", minutes=10.0, title=""):
    done = created + timedelta(minutes=minutes) if status == "completed" else None
    return P.RunInfo(i, status, conclusion, event, created, done, title)


def test_far_from_the_slate_nothing_is_wanted():
    d = P.decide(TIP - timedelta(hours=12), [TIP], [])
    assert (d.action, d.code) == ("idle", "OUTSIDE_WINDOW")


def test_no_games_means_idle():
    assert P.decide(NOW, [], []).code == "NO_UPCOMING_GAME"


def test_dispatches_when_nothing_has_ever_run_inside_the_window():
    d = P.decide(TIP - timedelta(hours=5), [TIP], [])
    assert (d.action, d.code, d.stages) == ("dispatch", "REFRESH_DUE", "all")


def test_a_fresh_run_suppresses_a_request_and_an_old_one_triggers_it():
    now = TIP - timedelta(hours=2)                                   # wanted interval 45 min
    fresh = _run(1, now - timedelta(minutes=40), minutes=10)         # data as of ~ now-38 min
    assert P.decide(now, [TIP], [fresh]).code == "FRESH_ENOUGH"
    old = _run(1, now - timedelta(minutes=120), minutes=10)
    d = P.decide(now, [TIP], [old])
    assert d.action == "dispatch" and d.last_success_age_min is not None and d.last_success_age_min > 100


def test_never_dispatches_while_a_run_is_queued_or_running_because_a_second_pending_run_replaces_the_first():
    now = TIP - timedelta(hours=2)
    for status in ("queued", "in_progress", "waiting", "pending", "requested"):
        d = P.decide(now, [TIP], [_run(2, now - timedelta(minutes=30), status=status, conclusion=None)])
        assert (d.action, d.code) == ("wait", "IN_FLIGHT"), status


def test_a_run_stuck_for_hours_does_not_block_forever():
    now = TIP - timedelta(hours=2)
    stuck = _run(3, now - timedelta(hours=P.STUCK_HOURS + 1), status="queued", conclusion=None)
    assert P.decide(now, [TIP], [stuck]).action == "dispatch"


def test_too_close_to_puck_drop_the_previous_run_is_final():
    now = TIP - timedelta(minutes=10)
    old = _run(1, now - timedelta(hours=3))
    d = P.decide(now, [TIP], [old])
    assert (d.action, d.code) == ("idle", "TOO_LATE_FOR_PREGAME")
    # but with no run at all a late attempt is still made (better a late file than none)
    assert P.decide(now, [TIP], []).action == "dispatch"


def test_observed_queue_latency_moves_the_last_useful_request_earlier():
    now = TIP - timedelta(minutes=35)
    slow = [_run(i, now - timedelta(hours=3 + i), minutes=80) for i in range(4)]       # runs take ~80 min end to end
    old = _run(9, now - timedelta(hours=3), minutes=10)
    # lead = 8 + min(median, 20) = 28 min < 35 min -> still allowed; at 20 min it is not
    assert P.decide(now, [TIP], [old] + slow).action in ("dispatch", "idle")
    assert P.decide(TIP - timedelta(minutes=20), [TIP], [old] + slow).code == "TOO_LATE_FOR_PREGAME"
    assert P.median_e2e_minutes(slow) == 80


def test_spacing_and_daily_cap_bound_the_request_rate():
    now = TIP - timedelta(hours=4)
    d = P.decide(now, [TIP], [], last_dispatch_at=now - timedelta(minutes=3))
    assert (d.action, d.code) == ("wait", "SPACING")
    d = P.decide(now, [TIP], [], dispatched_today=P.MAX_DISPATCHES_PER_DAY)
    assert (d.action, d.code) == ("wait", "DAILY_CAP")


def test_one_settle_run_after_the_slate_has_finished_and_then_no_repeat():
    last_tip = datetime(2026, 10, 23, 2, 0, tzinfo=UTC)               # 22:00 ET start
    tips = [TIP, last_tip, TIP + timedelta(hours=24)]
    before = last_tip + timedelta(hours=P.SETTLE_AFTER_LAST_TIP_HOURS) - timedelta(minutes=5)
    # the last successful run was shortly before the last start
    pre = _run(1, last_tip - timedelta(hours=1))
    assert P.decide(before, tips, [pre]).code != "SETTLE_DUE"
    due = last_tip + timedelta(hours=P.SETTLE_AFTER_LAST_TIP_HOURS) + timedelta(minutes=5)
    d = P.decide(due, tips, [pre])
    assert (d.action, d.code, d.stages) == ("dispatch", "SETTLE_DUE", P.SETTLE_STAGES)
    # a pregame/'all' run that started after the due instant also settles, so no second request
    after = _run(2, due + timedelta(minutes=1))
    d2 = P.decide(due + timedelta(minutes=30), tips, [after, pre])
    assert d2.code != "SETTLE_DUE"
    # and while it is in flight we wait
    flying = _run(3, due, status="in_progress", conclusion=None)
    assert P.decide(due + timedelta(minutes=2), tips, [flying, pre]).code == "SETTLE_WAIT_IN_FLIGHT"


def test_parse_runs_drops_malformed_rows_and_sorts_newest_first():
    payload = {"workflow_runs": [
        {"id": 1, "status": "completed", "conclusion": "success", "event": "schedule", "created_at": "2026-10-22T10:00:00Z", "updated_at": "2026-10-22T10:05:00Z"},
        {"id": 2, "status": "queued", "event": "workflow_dispatch", "created_at": "2026-10-22T11:00:00Z", "updated_at": "2026-10-22T11:00:00Z"},
        {"id": "x", "created_at": None},
        {"status": "queued"},
        {"id": 3, "status": "in_progress", "event": "pull_request", "created_at": "2026-10-22T11:30:00Z", "updated_at": "2026-10-22T11:30:00Z"},
        {"id": 4, "status": "completed", "conclusion": "success", "event": "workflow_dispatch", "display_title": "projection-foundation workflow_dispatch [all] dry-run",
         "created_at": "2026-10-22T11:40:00Z", "updated_at": "2026-10-22T11:45:00Z"},
    ]}
    runs = P.parse_runs(payload)
    assert [r.id for r in runs] == [2, 1] and runs[0].in_flight and runs[1].succeeded
    assert runs[1].e2e_minutes() == 5.0


def test_dispatcher_dispatches_once_then_waits_and_survives_failures():
    sent = []
    runs = []
    disp = P.PfDispatcher("o/r", "main", "t", list_fn=lambda: list(runs), dispatch_fn=lambda stages: sent.append(stages) or True)
    now = TIP - timedelta(hours=4)
    a = disp.step(now, [TIP])
    assert a["action"] == "dispatch" and a["dispatched"] and sent == ["all"]
    b = disp.step(now + timedelta(minutes=2), [TIP])                      # the API has not listed the new run yet: our own memory throttles
    assert (b["action"], b["code"]) == ("wait", "SPACING") and sent == ["all"]
    runs.append(_run(7, now + timedelta(minutes=1), status="queued", conclusion=None))
    c = disp.step(now + timedelta(minutes=30), [TIP])
    assert (c["action"], c["code"]) == ("wait", "IN_FLIGHT") and sent == ["all"]
    # an unreadable run list never produces a blind dispatch
    d = P.PfDispatcher("o/r", "main", "t", list_fn=lambda: None, dispatch_fn=lambda s: sent.append(s) or True).step(now, [TIP])
    assert d["code"] == "API_UNREADABLE" and sent == ["all"]
    # a refused dispatch is reported, not raised
    e = P.PfDispatcher("o/r", "main", "t", list_fn=lambda: [], dispatch_fn=lambda s: False).step(now, [TIP])
    assert e["code"] == "DISPATCH_REFUSED" and e["action"] == "wait"
    # any exception becomes a recorded wait
    def boom():
        raise RuntimeError("net")
    f = P.PfDispatcher("o/r", "main", "t", list_fn=boom).step(now, [TIP])
    assert f["code"] == "DISPATCHER_ERROR"


def test_recent_dispatches_are_counted_from_the_platforms_record():
    runs = [_run(i, NOW - timedelta(hours=i)) for i in range(1, 5)] + [_run(9, NOW - timedelta(hours=30))] + [_run(10, NOW - timedelta(hours=2), event="schedule")]
    n, last = P.count_recent_dispatches(runs, NOW)
    assert n == 4 and last == NOW - timedelta(hours=1)


def test_tips_from_schedule_files_reads_jsonl_and_gz(tmp_path):
    import gzip
    import json

    rows = [{"season_type": "regular", "start_time_utc": "2026-10-22T23:00:00Z"}, {"season_type": "preseason", "start_time_utc": "2026-10-22T20:00:00Z"}, {"start_time_utc": "bad"},
            {"season_type": "playoffs", "start_time_utc": "2026-10-23T00:00:00Z"}]
    p = tmp_path / "s.jsonl.gz"
    with gzip.open(p, "wt") as f:
        f.write("\n".join(json.dumps(r) for r in rows) + "\n\nnot json\n")
    q = tmp_path / "t.jsonl"
    q.write_text(json.dumps({"season_type": "regular", "start_time_utc": "2026-10-22T23:00:00Z"}) + "\n")
    tips = P.tips_from_schedule_files([p, q, tmp_path / "missing.jsonl"])
    assert tips == [datetime(2026, 10, 22, 23, 0, tzinfo=UTC), datetime(2026, 10, 23, 0, 0, tzinfo=UTC)]


class _Clock:
    def __init__(self, t):
        self.t = t

    def now(self):
        return self.t

    def sleep(self, s):
        self.t += timedelta(seconds=s)


def _worker(tmp_path, clock, pf_fn):
    return Worker(data_root=tmp_path / "d", archive_root=tmp_path / "a", worker_id="w", now_fn=clock.now, sleep_fn=clock.sleep,
                  run_fn=lambda cmd, t: (0, ""), schedule_fn=lambda: [{"start_time_utc": "2026-10-22T23:00:00Z"}], decide_fn=lambda: {},
                  lifetime_minutes=300.0, pf_fn=pf_fn)


def test_the_worker_records_the_dispatch_decision_without_changing_its_own_cycle(tmp_path):
    seen = []
    c = _Clock(NOW)
    w = _worker(tmp_path, c, lambda now, tips: seen.append((now, tips)) or {"action": "idle", "code": "FRESH_ENOUGH", "reason": "x", "hours_to_next_tip": 6.0})
    w._push = lambda msg: True
    rec = w._one_cycle(NOW)
    assert rec.pf == {"action": "idle", "code": "FRESH_ENOUGH", "hours_to_next_tip": 6.0}      # routine decisions drop the sentence
    assert seen and seen[0][1] == [TIP]
    assert rec.capture_ok is True and rec.push_ok is True


def test_a_crashing_dispatcher_never_breaks_a_capture_cycle(tmp_path):
    c = _Clock(NOW)

    def boom(now, tips):
        raise RuntimeError("api down")

    w = _worker(tmp_path, c, boom)
    w._push = lambda msg: True
    rec = w._one_cycle(NOW)
    assert rec.pf["code"] == "DISPATCHER_ERROR" and rec.capture_ok and rec.push_ok


def test_no_dispatcher_means_no_field(tmp_path):
    w = _worker(tmp_path, _Clock(NOW), None)
    w._push = lambda msg: True
    assert w._one_cycle(NOW).pf is None


def test_stale_flag_marks_a_late_delivery_only_when_nothing_is_on_its_way():
    now = TIP - timedelta(minutes=60)
    old = _run(1, now - timedelta(hours=6))
    assert P.decide(now, [TIP], [old]).stale is True
    assert P.decide(now, [TIP], []).stale is True
    assert P.decide(now, [TIP], [_run(2, now - timedelta(minutes=30), status="queued", conclusion=None), old]).stale is False
    assert P.decide(now, [TIP], [_run(3, now - timedelta(minutes=30))]).stale is False
    assert P.decide(TIP - timedelta(hours=5), [TIP], [old]).stale is False          # not close enough to matter


def _main(monkeypatch, tmp_path, runs, argv, now="2026-10-22T20:00:00Z"):
    import json

    sched = tmp_path / "s.jsonl"
    sched.write_text(json.dumps({"season_type": "regular", "start_time_utc": "2026-10-22T23:00:00Z"}) + "\n")
    out = tmp_path / "out.txt"
    monkeypatch.setenv("GITHUB_TOKEN", "t")
    monkeypatch.setattr(P, "list_runs_via_api", lambda repo, token, workflow=P.PF_WORKFLOW, per_page=30: runs)
    rc = P.main([*argv, "--schedule", str(sched), "--repo", "o/r", "--now", now, "--github-output", str(out)])
    return rc, dict(line.split("=", 1) for line in out.read_text().split())


def test_gate_runs_explicit_requests_unconditionally_and_policy_gates_cron(monkeypatch, tmp_path, capsys):
    for event in ("workflow_dispatch", "pull_request"):
        rc, o = _main(monkeypatch, tmp_path, [], ["gate", "--event", event, "--stages-input", "capture,project"])
        assert rc == 0 and o["run"] == "true" and o["stages"] == "capture,project"
    rc, o = _main(monkeypatch, tmp_path, [], ["gate", "--event", "workflow_dispatch"])
    assert o["stages"] == "all"
    # cron at T-3h with a fresh run on record: a no-op
    fresh = [_run(1, datetime(2026, 10, 22, 19, 40, tzinfo=UTC), minutes=6)]
    rc, o = _main(monkeypatch, tmp_path, fresh, ["gate", "--event", "schedule"])
    assert o["run"] == "false" and o["code"] == "FRESH_ENOUGH"
    # cron with nothing on record: it IS the fallback, so it runs
    rc, o = _main(monkeypatch, tmp_path, [], ["gate", "--event", "schedule"])
    assert o["run"] == "true" and o["code"] == "REFRESH_DUE"
    # the run asking must not count itself as in flight; another in-flight run does stop it
    me = _run(42, datetime(2026, 10, 22, 19, 59, tzinfo=UTC), status="in_progress", conclusion=None, event="schedule")
    rc, o = _main(monkeypatch, tmp_path, [me], ["gate", "--event", "schedule", "--exclude-run", "42"])
    assert o["run"] == "true"
    other = _run(43, datetime(2026, 10, 22, 19, 30, tzinfo=UTC), status="queued", conclusion=None)
    rc, o = _main(monkeypatch, tmp_path, [me, other], ["gate", "--event", "schedule", "--exclude-run", "42"])
    assert o["run"] == "false" and o["code"] == "IN_FLIGHT"


def test_gate_runs_when_the_run_list_cannot_be_read(monkeypatch, tmp_path):
    rc, o = _main(monkeypatch, tmp_path, None, ["gate", "--event", "schedule"])
    assert rc == 0 and o["run"] == "true" and o["code"] == "API_UNREADABLE"
    rc, o = _main(monkeypatch, tmp_path, None, ["decide"])
    assert o["run"] == "false"


def test_pull_request_runs_and_dry_runs_are_invisible_to_the_policy():
    runs = P.parse_runs({"workflow_runs": [
        {"id": 1, "status": "in_progress", "event": "pull_request", "created_at": "2026-10-22T20:30:00Z", "updated_at": "2026-10-22T20:30:00Z"},
        {"id": 2, "status": "completed", "conclusion": "success", "event": "workflow_dispatch", "display_title": "projection-foundation workflow_dispatch [all] dry-run",
         "created_at": "2026-10-22T20:40:00Z", "updated_at": "2026-10-22T20:45:00Z"}]})
    assert runs == []
    now = TIP - timedelta(hours=2)
    assert P.decide(now, [TIP], runs).code == "REFRESH_DUE"


def test_a_cancelled_gate_noop_is_neither_fresh_nor_a_failure():
    now = TIP - timedelta(hours=1)
    stale_real = _run(1, now - timedelta(hours=6))
    noop = _run(2, now - timedelta(minutes=3), conclusion="cancelled", minutes=1)
    d = P.decide(now, [TIP], [noop, stale_real])
    assert d.action == "dispatch" and d.stale is True and d.recovered is False


def test_only_projection_refreshing_runs_make_the_slate_fresh_but_any_success_counts_as_settled():
    now = TIP - timedelta(hours=2)
    settle_only = _run(5, now - timedelta(minutes=10), title="projection-foundation workflow_dispatch [capture,results,settle,score,guard]")
    full = _run(1, now - timedelta(hours=5), title="projection-foundation workflow_dispatch [all]")
    assert settle_only.projects is False and full.projects is True and _run(9, now, title="projection-foundation schedule").projects is True
    d = P.decide(now, [TIP], [settle_only, full])
    assert d.action == "dispatch" and d.code == "REFRESH_DUE"                           # the settle-only run did not refresh projections
    last_tip = datetime(2026, 10, 23, 2, 0, tzinfo=UTC)
    due = last_tip + timedelta(hours=P.SETTLE_AFTER_LAST_TIP_HOURS) + timedelta(minutes=5)
    only_settle = _run(6, due - timedelta(minutes=2), title="projection-foundation workflow_dispatch [capture,results,settle,score,guard]")
    assert P.decide(due + timedelta(minutes=30), [TIP, last_tip], [only_settle]).code != "SETTLE_DUE"      # settle already covered


def test_recovered_requires_a_recent_projection_success_not_merely_an_empty_queue():
    now = TIP - timedelta(minutes=60)
    queued = _run(2, now - timedelta(minutes=20), status="queued", conclusion=None)
    d = P.decide(now, [TIP], [queued, _run(1, now - timedelta(hours=7))])
    assert d.stale is False and d.recovered is False                                      # in flight: not stale, but also NOT recovered
    ok = _run(3, now - timedelta(minutes=30))
    assert P.decide(now, [TIP], [ok]).recovered is True


def test_repeated_failures_back_off_instead_of_burning_the_daily_cap():
    now = TIP - timedelta(hours=4)
    fails = [_run(i, now - timedelta(minutes=10 + 20 * i), conclusion="failure", minutes=5) for i in range(3)]
    d = P.decide(now, [TIP], fails)
    assert (d.action, d.code) == ("wait", "FAILURE_BACKOFF")
    later = P.decide(now + timedelta(minutes=120), [TIP], fails)
    assert later.action == "dispatch"
    cancelled_between = [fails[0], _run(8, now - timedelta(minutes=15), conclusion="cancelled"), fails[1], fails[2]]
    assert P.decide(now, [TIP], cancelled_between).code == "FAILURE_BACKOFF"             # cancelled runs are skipped, not counted as successes
    assert P.decide(now, [TIP], [fails[0], fails[1], _run(4, now - timedelta(hours=2)), fails[2]]).code != "FAILURE_BACKOFF"


def test_gate_always_runs_the_full_chain_for_cron_even_when_a_settle_is_due(monkeypatch, tmp_path):
    import json

    sched = tmp_path / "s.jsonl"
    sched.write_text("\n".join(json.dumps({"season_type": "regular", "start_time_utc": t}) for t in ("2026-10-22T23:00:00Z", "2026-10-23T02:00:00Z", "2026-10-24T23:00:00Z")) + "\n")
    out = tmp_path / "o.txt"
    monkeypatch.setenv("GITHUB_TOKEN", "t")
    monkeypatch.setattr(P, "list_runs_via_api", lambda repo, token, workflow=P.PF_WORKFLOW, per_page=100: [_run(1, datetime(2026, 10, 23, 1, 0, tzinfo=UTC))])
    P.main(["gate", "--event", "schedule", "--schedule", str(sched), "--repo", "o/r", "--now", "2026-10-23T06:00:00Z", "--github-output", str(out)])
    o = dict(line.split("=", 1) for line in out.read_text().split())
    assert o["run"] == "true" and o["code"] == "SETTLE_DUE" and o["stages"] == "all" and o["recovered"] in ("true", "false")
