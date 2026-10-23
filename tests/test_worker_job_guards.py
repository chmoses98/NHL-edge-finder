from __future__ import annotations

from datetime import UTC, datetime, timedelta

from nhl_edge.timeutil import iso
from nhl_edge.worker.run import Worker

T0 = datetime(2026, 10, 22, 18, 0, tzinfo=UTC)


class Clock:
    def __init__(self, t):
        self.t = t

    def now(self):
        return self.t

    def sleep(self, s):
        self.t += timedelta(seconds=s)


def _worker(tmp_path, clock, rc_by_job=None, exit_in_min=300.0):
    calls = []

    def run_fn(cmd, timeout):
        calls.append((cmd[1], timeout))
        clock.t += timedelta(seconds=30)
        return (rc_by_job or {}).get(cmd[1], 0), ""

    w = Worker(data_root=tmp_path / "d", archive_root=tmp_path / "a", worker_id="w", now_fn=clock.now, sleep_fn=clock.sleep, run_fn=run_fn,
               schedule_fn=lambda: [], decide_fn=lambda: {}, lifetime_minutes=exit_in_min)
    w._exit_at = clock.t + timedelta(minutes=exit_in_min)
    w._calls = calls
    return w


def _decision(next_h, now):
    return {"now_utc": iso(now), "next_start_hours": next_h, "evaluate": True, "settle": False, "simulate": False, "context": False, "discover": False}


def test_evaluate_runs_when_it_can_finish_before_the_quiet_window(tmp_path):
    c = Clock(T0)
    w = _worker(tmp_path, c)
    done, failed = w._run_jobs(_decision(8.0, c.t))
    assert "evaluate" in done and not failed


def test_evaluate_does_not_start_if_its_budget_would_run_into_the_quiet_window(tmp_path):
    c = Clock(T0)
    w = _worker(tmp_path, c)
    # 3 h 20 min to puck drop at decision time: the conductor allows it (>3 h) but a 40 min budget would end inside the window
    done, _ = w._run_jobs(_decision(3.33, c.t))
    assert "evaluate" not in done and not any(n == "evaluate" for n, _ in w._calls)
    # time spent on earlier jobs in the same cycle counts: 8 h at decision time, but the decision is 6 h stale
    c.t += timedelta(hours=6)
    assert w._skip_reason("evaluate", 2400.0, _decision(8.0, c.t - timedelta(hours=6)), c.t)


def test_a_failed_speculative_job_backs_off_for_three_hours(tmp_path):
    c = Clock(T0)
    w = _worker(tmp_path, c, rc_by_job={"evaluate": 124})
    _, failed = w._run_jobs(_decision(10.0, c.t))
    assert failed == ["evaluate"]
    c.t += timedelta(minutes=20)
    done, failed = w._run_jobs(_decision(10.0, c.t))
    assert "evaluate" not in done and not failed
    assert sum(1 for n, _ in w._calls if n == "evaluate") == 1
    c.t += timedelta(hours=3)
    w._run_jobs(_decision(10.0, c.t))
    assert sum(1 for n, _ in w._calls if n == "evaluate") == 2


def test_speculative_jobs_never_start_if_they_could_overrun_the_planned_exit(tmp_path):
    c = Clock(T0)
    w = _worker(tmp_path, c, exit_in_min=45.0)           # 45 min left, evaluate budget 40 min + 8 min reserve
    done, _ = w._run_jobs(_decision(10.0, c.t))
    assert "evaluate" not in done
    w2 = _worker(tmp_path, c, exit_in_min=120.0)
    assert "evaluate" in w2._run_jobs(_decision(10.0, c.t))[0]


def test_core_jobs_are_not_subject_to_the_speculative_guards(tmp_path):
    c = Clock(T0)
    w = _worker(tmp_path, c, rc_by_job={"simulate": 1}, exit_in_min=10.0)
    d = _decision(1.0, c.t) | {"simulate": True, "evaluate": False}
    _, failed = w._run_jobs(d)
    assert failed == ["simulate"]
    _, failed = w._run_jobs(d)
    assert failed == ["simulate"]                         # simulate is retried every cycle: it feeds the slate
