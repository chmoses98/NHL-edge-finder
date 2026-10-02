"""Failure semantics of the capture worker: green for no-work, yellow for nonfatal degradation, red only when
something is actionably broken after the in-shift retries.

Before this, ``nhl worker`` returned 0 unconditionally. Run 36955011158 (2026-10-02) was a green check while
``nhl settle`` crashed twice and settlement silently stopped. Every test here is deterministic: a fake clock,
injected commands, no network, no committed archive data and no dependence on today's date.
"""

from __future__ import annotations

import json
from datetime import timedelta
from pathlib import Path

import yaml

from nhl_edge.worker import health as H
from tests.test_worker_race import T0, FakeClock, make_worker


def _cycle(captured=True, capture_ok=True, push_ok=True, jobs_run=(), jobs_failed=(), decision_ok=True):
    return {
        "captured": captured,
        "capture_ok": capture_ok,
        "push_ok": push_ok,
        "jobs_run": list(jobs_run),
        "jobs_failed": list(jobs_failed),
        "decision_ok": decision_ok,
    }


def _status(cycles, **kw):
    d = {"worker_id": "w", "generation": 1, "exit_reason": "planned retirement", "fail_closed": False,
         "successor_expected": True, "successor_dispatched": True, "final_push_ok": True, "capture_alarms": [],
         "cycles": cycles}
    d.update(kw)
    return d


# -- pure classification --------------------------------------------------------------------------------


def test_fail_closed_standdown_is_not_applicable():
    h = H.assess(_status([], fail_closed=True, exit_reason="fail-closed: lease held by run-1"))
    assert h["state"] == H.NOT_APPLICABLE


def test_no_work_due_with_a_valid_decision_is_not_applicable():
    h = H.assess(_status([_cycle(captured=False, capture_ok=False)] * 4))
    assert h["state"] == H.NOT_APPLICABLE
    assert not h["failures"] and not h["warnings"]


def test_missing_decision_on_every_cycle_is_never_read_as_no_work():
    """An absent decision is missing evidence, not an off-day: fail closed."""
    h = H.assess(_status([_cycle(captured=False, capture_ok=False, decision_ok=False)] * 4))
    assert h["state"] == H.FAILED
    assert "decision unavailable" in h["reason"]


def test_missing_decision_on_some_cycles_is_degraded():
    cycles = [_cycle(decision_ok=False)] + [_cycle()] * 3
    assert H.assess(_status(cycles))["state"] == H.DEGRADED


def test_a_clean_shift_is_healthy():
    cycles = [_cycle(jobs_run=["simulate"]), _cycle(), _cycle(jobs_run=["settle", "evaluate"])]
    h = H.assess(_status(cycles))
    assert h["state"] == H.HEALTHY
    assert h["components"]["jobs"]["settle"]["disposition"] == "OK"


def test_replay_of_run_36955011158_settle_failing_at_retirement_is_red():
    """settle failed 02:20Z, succeeded 02:35Z (one game), failed 04:20Z and was never recovered."""
    cycles = [_cycle(jobs_failed=["settle"]), _cycle(jobs_run=["settle"])] + [_cycle()] * 7
    cycles += [_cycle(jobs_failed=["settle"])] + [_cycle()] * 10
    h = H.assess(_status(cycles))
    assert h["state"] == H.FAILED
    assert h["components"]["jobs"]["settle"]["disposition"] == "FAILING_AT_RETIREMENT"


def test_a_single_unretried_critical_failure_is_degraded_not_red():
    h = H.assess(_status([_cycle(), _cycle(jobs_failed=["simulate"])]))
    assert h["state"] == H.DEGRADED


def test_a_critical_job_recovered_within_the_shift_is_healthy_with_a_disposition():
    h = H.assess(_status([_cycle(jobs_failed=["simulate"]), _cycle(jobs_run=["simulate"])]))
    assert h["state"] == H.HEALTHY
    assert h["components"]["jobs"]["simulate"]["disposition"] == "RECOVERED_AFTER_RETRY"
    assert any("recovered" in n for n in h["notes"])


def test_research_jobs_failing_every_attempt_are_degraded_never_red():
    cycles = [_cycle(jobs_failed=["evaluate", "discover", "context"])] * 5
    h = H.assess(_status(cycles))
    assert h["state"] == H.DEGRADED
    assert h["failures"] == []


def test_a_capture_outage_at_the_end_of_the_shift_is_red():
    cycles = [_cycle()] * 5 + [_cycle(capture_ok=False)] * H.CAPTURE_TRAILING_FAILURES_FOR_FAILED
    assert H.assess(_status(cycles))["state"] == H.FAILED


def test_every_capture_failing_is_red():
    assert H.assess(_status([_cycle(capture_ok=False)] * 6))["state"] == H.FAILED


def test_short_capture_blips_are_degraded():
    cycles = [_cycle(), _cycle(capture_ok=False), _cycle(), _cycle(capture_ok=False), _cycle(capture_ok=False)]
    h = H.assess(_status(cycles))
    assert h["state"] == H.DEGRADED, "two trailing failures are below the bounded-retry threshold"


def test_final_push_failure_is_red_and_recovered_cycle_pushes_are_not():
    assert H.assess(_status([_cycle()], final_push_ok=False))["state"] == H.FAILED
    h = H.assess(_status([_cycle(push_ok=False), _cycle()], final_push_ok=True))
    assert h["state"] == H.HEALTHY
    assert h["notes"]


def test_status_written_before_the_final_push_does_not_claim_a_push_failure():
    h = H.assess(_status([_cycle()], final_push_ok=None))
    assert h["state"] == H.HEALTHY


def test_missing_successor_and_coverage_alarms_are_degraded_not_red():
    assert H.assess(_status([_cycle()], successor_dispatched=False))["state"] == H.DEGRADED
    assert H.assess(_status([_cycle()], successor_expected=False, successor_dispatched=False))["state"] == H.HEALTHY
    h = H.assess(_status([_cycle()], capture_alarms=["series on the board with no ontology entry: ['KXNEW']"]))
    assert h["state"] == H.DEGRADED and "coverage alarm" in h["reason"]


# -- the worker records what the verdict needs ----------------------------------------------------------


def _with_jobs(w, clock, failing: set[str], push_fail_on: str | None = None):
    def run_fn(cmd, timeout):
        w._calls.append(cmd)
        if cmd[:2] == ["nhl", "capture"]:
            clock.t += timedelta(seconds=180)
            return 0, ""
        if cmd[0] == "nhl" and cmd[1] in failing:
            return 1, f"{cmd[1]} blew up"
        if cmd[0] == "bash" and push_fail_on and push_fail_on in cmd[-1]:
            return 4, "archive-push: FAILED after 5 attempts"
        return 0, ""

    w.run_cmd = run_fn
    return w


def test_a_shift_whose_settle_keeps_failing_is_recorded_as_failed(tmp_path):
    clock = FakeClock(T0)
    w = _with_jobs(make_worker(tmp_path, clock, "run-1", lifetime=45.0), clock, {"settle"})
    w.decide_fn = lambda: {"settle": True}
    res = w.run()
    assert all(c.jobs_failed == ["settle"] for c in res.cycles)
    status = json.loads((tmp_path / "archive" / "STATUS_worker.json").read_text())
    assert status["health"]["state"] == H.FAILED
    assert status["n_jobs_failed"] == len(res.cycles)


def test_a_failing_research_job_leaves_the_shift_green_but_degraded(tmp_path):
    clock = FakeClock(T0)
    w = _with_jobs(make_worker(tmp_path, clock, "run-1", lifetime=45.0), clock, {"evaluate"})
    w.decide_fn = lambda: {"evaluate": True, "simulate": True}
    res = w.run()
    assert res.as_dict()["health"]["state"] == H.DEGRADED


def test_an_off_day_shift_is_not_applicable(tmp_path):
    clock = FakeClock(T0)
    w = make_worker(tmp_path, clock, "run-1", schedule=[], lifetime=30.0)
    w.decide_fn = lambda: {"capture": False, "context": False}
    res = w.run()
    assert res.as_dict()["health"]["state"] == H.NOT_APPLICABLE


def test_a_decision_that_raises_is_recorded_and_fails_closed(tmp_path, monkeypatch):
    import nhl_edge.workflows.conductor as conductor

    def boom(data_root, now=None):
        raise ValueError("corrupt breadcrumb")

    monkeypatch.setattr(conductor, "decide_now", boom)
    clock = FakeClock(T0)
    res = make_worker(tmp_path, clock, "run-1", schedule=[], lifetime=30.0).run()
    assert res.cycles and all(c.decision_ok is False for c in res.cycles)
    assert res.as_dict()["health"]["state"] == H.FAILED


def test_the_final_push_outcome_reaches_the_report(tmp_path):
    clock = FakeClock(T0)
    w = _with_jobs(make_worker(tmp_path, clock, "run-1", lifetime=30.0), clock, set(), push_fail_on="retired after")
    res = w.run()
    assert res.final_push_ok is False
    assert res.as_dict()["health"]["state"] == H.FAILED
    on_branch = json.loads((tmp_path / "archive" / "STATUS_worker.json").read_text())
    assert on_branch["final_push_ok"] is None, "the archived status is written before that push"


def test_coverage_alarms_of_the_last_capture_are_carried_as_degraded(tmp_path):
    clock = FakeClock(T0)
    w = make_worker(tmp_path, clock, "run-1", lifetime=30.0)
    (tmp_path / "archive" / "STATUS_capture.json").write_text(json.dumps({"alarms": ["pagination stopped"]}))
    res = w.run()
    assert res.capture_alarms == ["pagination stopped"]
    assert res.as_dict()["health"]["state"] == H.DEGRADED


# -- the workflow report step -----------------------------------------------------------------------------


def _run_report(tmp_path, payload):
    rep = tmp_path / "report.json"
    if payload is not None:
        rep.write_text(json.dumps(payload))
    summary, out = tmp_path / "summary.md", tmp_path / "out.txt"
    rc = H.main(["--report", str(rep), "--summary", str(summary), "--github-output", str(out)])
    outputs = dict(line.split("=", 1) for line in out.read_text().splitlines())
    return rc, outputs, summary.read_text()


def test_report_step_degraded_warns_in_summary_and_exits_zero(tmp_path, capsys):
    st = _status([_cycle(jobs_failed=["evaluate"])])
    st["health"] = H.assess(st)
    rc, outputs, summary = _run_report(tmp_path, st)
    assert rc == 0
    assert outputs["state"] == H.DEGRADED and outputs["final_push_ok"] == "true"
    assert "::warning title=capture-worker DEGRADED::" in capsys.readouterr().out
    assert "DEGRADED" in summary


def test_report_step_failed_sets_state_and_flags_the_unpushed_archive(tmp_path, capsys):
    st = _status([_cycle()], final_push_ok=False)
    st["health"] = H.assess(st)
    rc, outputs, _ = _run_report(tmp_path, st)
    assert rc == 0, "the report step never fails; the single enforcement step does"
    assert outputs == {"state": H.FAILED, "final_push_ok": "false"}
    assert "::error title=capture-worker FAILED::" in capsys.readouterr().out


def test_report_step_with_no_report_fails_closed(tmp_path):
    rc, outputs, summary = _run_report(tmp_path, None)
    assert rc == 0 and outputs["state"] == H.FAILED
    assert "did not finish" in summary


def test_cli_writes_the_final_report(tmp_path, monkeypatch):
    from nhl_edge import cli
    from nhl_edge.worker import run as run_mod

    class FakeWorker:
        def __init__(self, **kw):
            pass

        def run(self):
            return run_mod.WorkerResult(worker_id="x", generation=1, exit_reason="planned", final_push_ok=False)

    monkeypatch.setattr(run_mod, "Worker", FakeWorker)
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    rep = tmp_path / "r.json"
    assert cli.main(["worker", "--out", str(tmp_path / "a"), "--report", str(rep)]) == 0
    assert json.loads(rep.read_text())["health"]["state"] == H.FAILED


# -- workflow shape ---------------------------------------------------------------------------------------


def test_capture_worker_has_one_enforcement_step_after_report_and_preserve():
    wf = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "capture_worker.yml"
    steps = yaml.safe_load(wf.read_text())["jobs"]["worker"]["steps"]
    names = [s.get("name", "") for s in steps]
    report = names.index("Report shift health")
    preserve = names.index("Preserve the archive if the final push failed")
    enforce = names.index("Enforce (red only for FAILED)")
    assert report < preserve < enforce == len(steps) - 1
    assert steps[report]["if"] == "always()"
    assert "final_push_ok == 'false'" in steps[preserve]["if"]
    assert "if" not in steps[enforce], "enforcement must not run (and fail twice) after a crashed worker step"
    exits = [s for s in steps if "exit 1" in (s.get("run") or "")]
    assert exits == [steps[enforce]], "exactly one step may turn the run red on purpose"
    assert not any(s.get("continue-on-error") for s in steps), "no failure may be hidden in the worker job"
    worker_step = steps[names.index("Run the worker")]
    assert "--report" in worker_step["run"] and worker_step["env"]["PYTHONUNBUFFERED"] == "1"


# -- settlement progress: `nhl settle` exits 0 while recording fetch errors and pending games ------------------------


def _snap(pending=(), result_errors=0, player_errors=0, fresh=True):
    if not fresh:
        return {"fresh": False}
    return {"fresh": True, "games_pending": list(pending), "n_result_errors": result_errors, "n_player_errors": player_errors}


def _settle_cycles(*snaps):
    return [_cycle(jobs_run=["settle"]) | {"settle": sn} for sn in snaps]


def test_a_game_pending_within_the_retry_grace_is_degraded():
    h = H.assess(_status(_settle_cycles(_snap(["2026020001"]), _snap(["2026020001"]))))
    assert h["state"] == H.DEGRADED
    assert h["components"]["settlement"]["games_pending"] == ["2026020001"]


def test_a_game_pending_across_consecutive_settle_runs_is_red_although_settle_exited_zero():
    snaps = [_snap(["2026020001", "2026020002"])] + [_snap(["2026020001"])] * (H.SETTLE_STALL_ATTEMPTS - 1)
    h = H.assess(_status(_settle_cycles(*snaps)))
    assert h["state"] == H.FAILED
    assert h["components"]["settlement"]["stalled_games"] == ["2026020001"]
    assert h["components"]["jobs"]["settle"]["disposition"] == "OK", "the exit code alone says everything is fine"


def test_a_backlog_that_moves_is_not_a_stall():
    """Different games pending in consecutive runs = settlement is progressing (new games entering the window)."""
    snaps = [_snap(["a"]), _snap(["b"]), _snap(["c"])]
    assert H.assess(_status(_settle_cycles(*snaps)))["state"] == H.DEGRADED
    assert H.assess(_status(_settle_cycles(_snap(["a"]), _snap(["a"]), _snap([]))))["state"] == H.HEALTHY


def test_player_phase_errors_are_degraded_then_red_once_the_grace_is_spent():
    assert H.assess(_status(_settle_cycles(_snap(), _snap(player_errors=1))))["state"] == H.DEGRADED
    snaps = [_snap(player_errors=1), _snap(result_errors=1), _snap(player_errors=2)]
    assert H.assess(_status(_settle_cycles(*snaps)))["state"] == H.FAILED
    recovered = [_snap(player_errors=1), _snap(player_errors=1), _snap()]
    assert H.assess(_status(_settle_cycles(*recovered)))["state"] == H.HEALTHY


def test_a_settle_run_that_did_not_refresh_its_status_is_degraded():
    assert H.assess(_status(_settle_cycles(_snap(), _snap(fresh=False))))["state"] == H.DEGRADED


def _settle_writer(w, clock, statuses, stale_by=None):
    """settle exits 0 every time (as on main) and writes the next STATUS_settle.json in ``statuses``."""
    it = iter(statuses)

    def run_fn(cmd, timeout):
        w._calls.append(cmd)
        if cmd[:2] == ["nhl", "capture"]:
            clock.t += timedelta(seconds=180)
        elif cmd[:2] == ["nhl", "settle"]:
            body = next(it)
            at = clock.now() - (stale_by or timedelta(0))
            body = {"settled_at_utc": at.isoformat().replace("+00:00", "Z"), **body}
            (w.archive_root / "STATUS_settle.json").write_text(json.dumps(body))
        return 0, ""

    w.run_cmd = run_fn
    return w


def test_worker_reads_the_settle_status_it_produced_and_turns_a_stall_red(tmp_path):
    clock = FakeClock(T0)
    stuck = {"errors": [], "player": {"errors": ["2026020001: boom"]}, "games_pending": ["2026020001"]}
    w = _settle_writer(make_worker(tmp_path, clock, "run-1", lifetime=60.0), clock, [stuck] * 50)
    w.decide_fn = lambda: {"settle": True}
    res = w.run()
    assert len([c for c in res.cycles if c.settle]) >= H.SETTLE_STALL_ATTEMPTS
    assert res.cycles[0].settle == {"fresh": True, "games_pending": ["2026020001"], "n_result_errors": 0, "n_player_errors": 1}
    h = json.loads((tmp_path / "archive" / "STATUS_worker.json").read_text())["health"]
    assert h["state"] == H.FAILED and h["components"]["jobs"]["settle"]["failed"] == 0


def test_a_stale_settle_status_from_another_run_is_never_attributed_to_this_shift(tmp_path):
    clock = FakeClock(T0)
    stuck = {"errors": ["x"], "player": {"errors": ["y"]}, "games_pending": ["2026020001"]}
    w = _settle_writer(make_worker(tmp_path, clock, "run-1", lifetime=60.0), clock, [stuck] * 50, stale_by=timedelta(hours=2))
    w.decide_fn = lambda: {"settle": True}
    res = w.run()
    assert all(c.settle == {"fresh": False} for c in res.cycles)
    h = res.as_dict()["health"]
    assert h["state"] == H.DEGRADED, "stale breadcrumb: flagged as not refreshed, its pending games/errors ignored"
    assert h["components"]["settlement"]["stalled_games"] == []
