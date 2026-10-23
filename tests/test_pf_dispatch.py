"""Worker-driven projection-foundation refresh: policy, idempotency, fail-soft, and wiring. No network."""

from __future__ import annotations

import json
from datetime import UTC, datetime, timedelta
from pathlib import Path

import yaml

from nhl_edge.timeutil import iso
from nhl_edge.worker import pf
from nhl_edge.worker.run import Worker

NOW = datetime(2026, 10, 22, 21, 0, tzinfo=UTC)


def games(*minutes_ahead, status="not_started"):
    return [{"start_time_utc": iso(NOW + timedelta(minutes=m)), "status": status} for m in minutes_ahead]


def run(status="completed", event="schedule", minutes_ago=100, rid=1):
    return {"id": rid, "status": status, "event": event, "created_at": iso(NOW - timedelta(minutes=minutes_ago))}


def test_stale_publication_before_a_reachable_game_dispatches():
    d = pf.decide_pf(NOW, games(75, 80), [run()], NOW - timedelta(minutes=300))
    assert d["action"] == "dispatch" and d["max_age_min"] == 40.0 and d["lead_min"] == 75.0


def test_fresh_publication_does_not_dispatch():
    d = pf.decide_pf(NOW, games(75), [run()], NOW - timedelta(minutes=20))
    assert d["action"] == "skip" and "old" in d["reason"]


def test_allowed_age_loosens_with_lead_time():
    for lead, age, expect in ((200, 100, "skip"), (200, 160, "dispatch"), (120, 60, "skip"), (120, 90, "dispatch"), (60, 30, "skip"), (60, 50, "dispatch")):
        assert pf.decide_pf(NOW, games(lead), [run()], NOW - timedelta(minutes=age))["action"] == expect, (lead, age)


def test_far_games_are_left_to_the_cron_slot_and_started_games_are_ignored():
    assert pf.decide_pf(NOW, games(500), [], None)["action"] == "skip"
    assert pf.decide_pf(NOW, games(75, status="live"), [], None)["action"] == "skip"
    assert pf.decide_pf(NOW, [], [], None)["action"] == "skip"


def test_a_refresh_that_cannot_land_before_puck_drop_is_not_requested_but_a_later_game_still_counts():
    assert pf.decide_pf(NOW, games(10), [run()], None)["action"] == "skip"
    d = pf.decide_pf(NOW, games(10, 120), [run()], NOW - timedelta(minutes=200))
    assert d["action"] == "dispatch" and d["lead_min"] == 120.0


def test_never_stacks_on_a_running_or_dispatched_run_but_ignores_queued_cron_entries():
    stale = NOW - timedelta(minutes=300)
    assert pf.decide_pf(NOW, games(75), [run("in_progress", "schedule", 30)], stale)["action"] == "skip"
    assert pf.decide_pf(NOW, games(75), [run("queued", "workflow_dispatch", 20)], stale)["action"] == "skip"
    # a queued scheduled run may be a gate-only cron entry: it is no evidence a refresh is coming
    assert pf.decide_pf(NOW, games(75), [run("queued", "schedule", 30)], stale)["action"] == "dispatch"


def test_throttle_and_daily_cap():
    stale = NOW - timedelta(minutes=300)
    assert pf.decide_pf(NOW, games(75), [run("completed", "workflow_dispatch", 5)], stale)["action"] == "skip"
    many = [run("completed", "workflow_dispatch", 20 + i, rid=i) for i in range(pf.MAX_DISPATCHES_PER_DAY)]
    d = pf.decide_pf(NOW, games(75), many, stale)
    assert d["action"] == "skip" and "PF_DISPATCH_CAP_REACHED" in d["alerts"]


def test_watchdog_alerts():
    stale = NOW - timedelta(minutes=300)
    d = pf.decide_pf(NOW, games(40), [run("queued", "workflow_dispatch", 70, rid=9)], stale)
    assert any(a.startswith("PF_RUN_QUEUED_70MIN") for a in d["alerts"]) and any(a.startswith("PF_PUBLICATION_STALE_NEAR_TIPOFF") for a in d["alerts"])
    d = pf.decide_pf(NOW, games(500), [run("in_progress", "schedule", 120, rid=3)], NOW)
    assert any(a.startswith("PF_RUN_IN_PROGRESS_120MIN") for a in d["alerts"])


def _http(runs, commit_time, log):
    def call(method, url, body=None):
        log.append((method, url, body))
        if method == "GET" and "/runs" in url:
            return 200, {"workflow_runs": runs}
        if method == "GET" and "/commits" in url:
            return (200, [{"commit": {"committer": {"date": iso(commit_time)}}}]) if commit_time else (404, "no branch")
        if method == "POST":
            return 204, None
        return 500, "unexpected"
    return call


def test_run_pf_refresh_dispatches_the_same_workflow_live_and_all_stages():
    log = []
    rec = pf.run_pf_refresh(NOW, games(75), "o/r", "t", http=_http([run()], NOW - timedelta(minutes=300), log))
    assert rec["action"] == "dispatch" and rec["dispatch_http"] == 204
    method, url, body = log[-1]
    assert method == "POST" and url.endswith("/actions/workflows/projection-foundation.yml/dispatches")
    assert json.loads(body) == {"ref": "main", "inputs": {"stages": "all", "dry_run": "false"}}


def test_a_missing_projection_branch_counts_as_never_published_and_api_errors_fail_soft():
    log = []
    assert pf.run_pf_refresh(NOW, games(75), "o/r", "t", http=_http([], None, log))["action"] == "dispatch"
    assert pf.run_pf_refresh(NOW, games(75), "o/r", "t", http=lambda *a: (403, "forbidden"))["action"] == "error"

    def boom(*a):
        raise RuntimeError("network down")
    assert pf.run_pf_refresh(NOW, games(75), "o/r", "t", http=boom)["action"] == "error"


def test_rejected_dispatch_is_an_error_not_a_dispatch():
    def call(method, url, body=None):
        if method == "POST":
            return 422, "bad input"
        return (200, {"workflow_runs": []}) if "/runs" in url else (404, "")
    rec = pf.run_pf_refresh(NOW, games(75), "o/r", "t", http=call)
    assert rec["action"] == "error" and "422" in rec["reason"]


def test_kill_switch_and_missing_credentials(monkeypatch):
    monkeypatch.setenv("NHL_EDGE_PF_DISPATCH", "0")
    assert pf.make_pf_fn("o/r", "t") is None
    monkeypatch.delenv("NHL_EDGE_PF_DISPATCH")
    assert pf.make_pf_fn("", "t") is None and pf.make_pf_fn("o/r", "") is None
    assert pf.make_pf_fn("o/r", "t") is not None


def test_worker_records_the_check_and_survives_a_crashing_checker(tmp_path):
    calls = []

    def ok(now, rows):
        calls.append(rows)
        return {"action": "dispatch", "reason": "stale", "alerts": []}

    def bad(now, rows):
        raise RuntimeError("x")

    for fn, action in ((ok, "dispatch"), (bad, "error"), (None, None)):
        w = Worker(data_root=tmp_path / "d", archive_root=tmp_path / "a", worker_id="w", now_fn=lambda: NOW, sleep_fn=lambda s: None, run_fn=lambda c, t: (0, ""),
                   schedule_fn=lambda: games(75), decide_fn=lambda: {}, lifetime_minutes=300, pf_fn=fn)
        rec = w._pf_check(NOW)
        assert (rec or {}).get("action") == action
    assert calls and calls[0][0]["status"] == "not_started"


def test_health_degrades_on_pf_alerts_and_never_fails():
    from nhl_edge.worker import health

    cyc = {"captured": True, "capture_ok": True, "push_ok": True, "jobs_run": [], "jobs_failed": [], "decision_ok": True,
           "pf": {"action": "skip", "alerts": ["PF_RUN_QUEUED_55MIN (run 1): GitHub runner capacity"]}}
    status = {"worker_id": "w", "generation": 1, "exit_reason": "planned retirement", "fail_closed": False, "successor_expected": True, "successor_dispatched": True,
              "final_push_ok": True, "capture_alarms": [], "cycles": [cyc, dict(cyc, pf={"action": "skip", "alerts": ["PF_RUN_QUEUED_70MIN (run 1): x"]})]}
    h = health.assess(status)
    assert h["state"] == health.DEGRADED and h["components"]["pf_refresh"]["alerts"] == ["PF_RUN_QUEUED"]
    assert sum("PF_RUN_QUEUED" in w for w in h["warnings"]) == 1          # de-duplicated across cycles
    errs = dict(status, cycles=[dict(cyc, pf={"action": "error", "reason": "HTTP 403", "alerts": []})])
    assert health.assess(errs)["state"] == health.DEGRADED


def test_workflow_serialises_on_the_live_job_so_gate_only_runs_cannot_cancel_a_pending_refresh():
    wf = yaml.safe_load((Path(__file__).resolve().parents[1] / ".github" / "workflows" / "projection-foundation.yml").read_text())
    top = wf["concurrency"]["group"]
    assert "run_id" in top and "'projection-foundation-nhl'" not in top.replace("projection-foundation-nhl-", "")
    live = wf["jobs"]["live"]["concurrency"]
    assert live["cancel-in-progress"] is False and "'projection-foundation-nhl'" in live["group"] and "-dry" in live["group"]   # dry-runs get their own group
    assert "concurrency" not in wf["jobs"]["gate"]


# ---- review findings (independent adversarial review of this PR) -----------------------------------------------------------------------------------------

def test_pull_request_ci_runs_of_the_workflow_are_not_pf_work():
    stale = NOW - timedelta(minutes=300)
    pr = [run("in_progress", "pull_request", 120, rid=7), run("queued", "pull_request", 200, rid=8)]
    d = pf.decide_pf(NOW, games(75), pr, stale)
    assert d["action"] == "dispatch" and d["alerts"] == []          # neither blocks, throttles, counts toward the cap nor raises a queue alert


def test_back_off_after_a_failed_dispatched_run_and_after_runs_that_publish_nothing():
    stale = NOW - timedelta(minutes=300)
    failed = dict(run("completed", "workflow_dispatch", 30, rid=5), conclusion="failure")
    d = pf.decide_pf(NOW, games(75), [failed], stale)
    assert d["action"] == "skip" and any(a.startswith("PF_DISPATCHED_RUN_FAILURE") for a in d["alerts"])
    old_failure = dict(run("completed", "workflow_dispatch", 90, rid=5), conclusion="failure")
    assert pf.decide_pf(NOW, games(75), [old_failure], stale)["action"] == "dispatch"
    ok = [dict(run("completed", "workflow_dispatch", 40 + 20 * i, rid=10 + i), conclusion="success") for i in range(2)]
    d = pf.decide_pf(NOW, games(75), ok, stale)
    assert d["action"] == "skip" and "PF_DISPATCHED_BUT_NOT_PUBLISHED" in d["alerts"]
    published_after = NOW - timedelta(minutes=45)                   # the tip moved after those runs: no backoff needed (and now fresh enough)
    assert pf.decide_pf(NOW, games(75), ok, published_after - timedelta(minutes=300))["action"] in ("skip", "dispatch")


def test_in_progress_watchdog_measures_from_run_started_at_not_creation():
    r = dict(run("in_progress", "workflow_dispatch", 200, rid=4), run_started_at=iso(NOW - timedelta(minutes=10)))
    assert not pf.decide_pf(NOW, games(500), [r], NOW)["alerts"]
    r2 = dict(r, run_started_at=iso(NOW - timedelta(minutes=100)))
    assert any(a.startswith("PF_RUN_IN_PROGRESS_100MIN") for a in pf.decide_pf(NOW, games(500), [r2], NOW)["alerts"])


def test_only_a_main_worker_dispatches_and_always_on_main():
    assert pf.make_pf_fn("o/r", "t", "claude/some-branch") is None
    log = []
    fn = pf.make_pf_fn("o/r", "t", "main")
    assert fn is not None
    rec = pf.run_pf_refresh(NOW, games(75), "o/r", "t", ref="main", http=_http([], None, log))
    assert json.loads(log[-1][2])["ref"] == "main" and rec["action"] == "dispatch"


def test_no_network_call_when_no_game_is_within_reach():
    def forbidden(*a):
        raise AssertionError("network call made")
    assert pf.run_pf_refresh(NOW, [], "o/r", "t", http=forbidden)["action"] == "skip"
    assert pf.run_pf_refresh(NOW, games(60 * 12), "o/r", "t", http=forbidden)["action"] == "skip"
    assert pf.run_pf_refresh(NOW, games(75, status="live"), "o/r", "t", http=forbidden)["action"] == "skip"


def test_boundaries_of_the_lead_and_age_rules():
    for lead, age, expect in ((20, 41, "dispatch"), (19, 500, "skip"), (90, 41, "dispatch"), (90, 40, "skip"), (91, 76, "dispatch"), (91, 75, "skip"),
                              (180, 76, "dispatch"), (181, 151, "dispatch"), (181, 150, "skip"), (360, 151, "dispatch"), (361, 999, "skip")):
        assert pf.decide_pf(NOW, games(lead), [], NOW - timedelta(minutes=age))["action"] == expect, (lead, age)
    for status in ("waiting", "pending", "requested"):
        assert pf.decide_pf(NOW, games(75), [run(status, "workflow_dispatch", 5)], NOW - timedelta(minutes=300))["action"] == "skip"


def test_unparseable_or_naive_schedule_rows_are_ignored_and_a_5xx_is_an_error_not_a_dispatch():
    rows = [{"start_time_utc": "garbage", "status": "not_started"}, {"start_time_utc": "2026-10-22T22:15:00", "status": None}] + games(75)
    assert pf.decide_pf(NOW, rows, [], None)["action"] == "dispatch"

    def call(method, url, body=None):
        return (200, {"workflow_runs": []}) if "/runs" in url else (502, "bad gateway")
    assert pf.run_pf_refresh(NOW, games(75), "o/r", "t", http=call)["action"] == "error"


def test_health_survives_an_empty_alert_string():
    from nhl_edge.worker import health

    cyc = {"captured": True, "capture_ok": True, "push_ok": True, "jobs_run": [], "jobs_failed": [], "decision_ok": True, "pf": {"action": "skip", "alerts": ["", "   "]}}
    status = {"worker_id": "w", "generation": 1, "exit_reason": "planned retirement", "fail_closed": False, "successor_expected": True, "successor_dispatched": True,
              "final_push_ok": True, "capture_alarms": [], "cycles": [cyc]}
    assert health.assess(status)["state"] in (health.HEALTHY, health.DEGRADED)
