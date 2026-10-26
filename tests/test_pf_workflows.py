from __future__ import annotations

from pathlib import Path

import yaml

WF = Path(__file__).resolve().parents[1] / ".github" / "workflows"


def _load(name):
    d = yaml.safe_load((WF / name).read_text())
    d["on"] = d.pop(True, d.get("on"))          # PyYAML reads the key `on` as boolean True
    return d


def test_projection_foundation_is_a_single_runner_request_with_the_gate_inside_the_job():
    d = _load("projection-foundation.yml")
    assert "gate" not in d["jobs"]                                         # the separate gate job doubled the exposure to runner queues
    live = d["jobs"]["live"]
    assert "needs" not in live and live["if"] == "github.event_name != 'pull_request'"
    assert live["permissions"] == {"contents": "write", "actions": "write"}                 # actions: write only to cancel its own gated-out run
    names = [s.get("name", "") for s in live["steps"]]
    gate_i = next(i for i, n in enumerate(names) if n.startswith("Gate"))
    install_i = next(i for i, s in enumerate(live["steps"]) if "pip install" in str(s.get("run", "")))
    assert gate_i < install_i                                              # a no-op cron run must not pay for the install
    heavy = [s for s in live["steps"][install_i:] if "uses" not in s or "cache/save" in s["uses"] or "upload-artifact" in s["uses"]]
    assert all("steps.gate.outputs" in str(s.get("if", "")) or "steps.chain.outputs" in str(s.get("if", "")) for s in heavy)
    full_view = next(i for i, s in enumerate(live["steps"]) if "ci_data_archive.sh" in str(s.get("run", "")))
    assert full_view > gate_i and live["steps"][full_view]["if"] == "steps.gate.outputs.run == 'true'"       # the heavy input view only if the chain runs
    cancel = next(s for s in live["steps"] if "gh run cancel" in str(s.get("run", "")))
    assert cancel["if"] == "steps.gate.outputs.run != 'true'"                                               # a no-op must not conclude `success`


def test_cron_is_a_fallback_with_its_own_concurrency_group_and_no_dst_duplicates():
    d = _load("projection-foundation.yml")
    crons = [c["cron"] for c in d["on"]["schedule"]]
    assert len(crons) == 3 and all(len(c.split()) == 5 for c in crons)
    group = d["concurrency"]["group"]
    # the three event classes resolve to three groups: a cron run can never take the pending slot of a worker-requested run
    assert "projection-foundation-nhl-cron" in group and "projection-foundation-nhl-pr-" in group and "'projection-foundation-nhl')" in group
    assert d["concurrency"]["cancel-in-progress"] == "${{ github.event_name == 'pull_request' }}"
    assert "stages" in d["on"]["workflow_dispatch"]["inputs"] and "dry_run" in d["on"]["workflow_dispatch"]["inputs"]


def test_the_gate_step_fails_open_and_reads_nothing_secret():
    live = _load("projection-foundation.yml")["jobs"]["live"]
    gate = next(s for s in live["steps"] if s.get("id") == "gate")
    assert "pf_dispatch gate" in gate["run"] and "running the chain" in gate["run"]
    assert set(gate["env"]) == {"EVENT_NAME", "STAGES_INPUT", "RUN_ID", "GITHUB_TOKEN"}
    assert gate["env"]["GITHUB_TOKEN"] == "${{ github.token }}"


def test_slate_watch_can_dispatch_and_nothing_else_beyond_issues():
    d = _load("slate_watch.yml")
    assert d["permissions"] == {"contents": "read", "issues": "write", "actions": "write"}
    text = (WF / "slate_watch.yml").read_text()
    assert "pf_dispatch dispatch" in text and "NHL projection delivery late" in text
    assert 'RECOVERED" = "true"' in text                                                                     # the alert closes only on a real recent success
    for forbidden in ("contents: write", "git push", "--force"):
        assert forbidden not in text


def test_worker_workflow_keeps_the_permission_the_dispatcher_needs():
    d = _load("capture_worker.yml")
    assert d["permissions"]["actions"] == "write" and d["permissions"]["contents"] == "write"


def test_slate_watch_judges_forecast_delivery_by_evaluation_not_by_unchanged_values():
    text = (WF / "slate_watch.yml").read_text()
    assert "delivery_monitor" in text and "NHL pregame forecast missing or stale" in text
    assert 'ALERT" = "true"' in text and 'RECOVERED" = "true"' in text
    assert "did not change is not a problem" in text           # the issue body says so, so a reader is not sent chasing an unchanged value
    assert "contents: write" not in text


def test_research_weekly_records_the_daily_delivery_timeline_read_only():
    d = _load("research_weekly.yml")
    text = (WF / "research_weekly.yml").read_text()
    assert d["permissions"] == {"contents": "read", "issues": "write", "actions": "read"}
    assert "delivery_timeline" in text and "context/schedule" in text and "git push" not in text


def test_slate_watch_asks_for_the_lc_collection_and_alerts_only_on_a_missing_record():
    text = (WF / "slate_watch.yml").read_text()
    assert "lc_dispatch dispatch" in text and "NHL workload shadow collection gap" in text
    assert 'GAP" = "true"' in text and 'RECOVERED" = "true"' in text and "never back-filled" in text.lower().replace("**", "")
    steps = {s.get("id") for s in _load("slate_watch.yml")["jobs"]["check"]["steps"]}
    assert {"pf", "lc"} <= steps


def test_workload_shadow_workflow_cannot_touch_anything_but_its_own_branch_and_refuses_immutable_changes():
    d = _load("workload_shadow.yml")
    text = (WF / "workload_shadow.yml").read_text()
    assert d["permissions"] == {"contents": "write"} and "workflow_dispatch" in d["on"] and "schedule" in d["on"]
    assert "HEAD:workload-shadow-data" in text and "--force" not in text and "push origin main" not in text
    assert "--diff-filter=DMRTC" in text and "--no-renames" in text and "only be appended" in text


def test_player_minutes_runs_in_its_own_workflow_and_writes_only_its_own_branch():
    lc = _load("workload_shadow.yml")
    d = _load("player_minutes.yml")
    text = (WF / "player_minutes.yml").read_text()
    assert set(lc["jobs"]) == {"run"} and "player-minutes" not in (WF / "workload_shadow.yml").read_text()      # the LC run record the dispatcher reads is untouched
    assert d["permissions"] == {"contents": "write"} and "workflow_dispatch" in d["on"] and "schedule" in d["on"]
    assert "HEAD:player-minutes-data" in text and "workload-shadow-data" not in text and "--force" not in text and "push origin main" not in text
    run = "\n".join(str(s.get("run", "")) for s in d["jobs"]["run"]["steps"])
    assert "set +e" in run and "player_minutes_shadow predict" in run and "player_minutes_shadow settle" in run and "player_minutes_shadow score" in run
    assert "(records|outcomes|coverage|looks|activation)" in run and "--diff-filter=DMRTC" in run and "only be appended" in run


def test_lc_run_step_publishes_what_was_written_even_when_a_day_failed():
    d = _load("workload_shadow.yml")
    step = next(s for s in d["jobs"]["run"]["steps"] if s.get("id") == "run")
    assert step["run"].lstrip().startswith("set +e")          # bash -e would otherwise exit at `predict | tee` (rc 3) before the commit step could publish the other days
    assert "predict_rc" in step["run"] and "score_rc" in step["run"]


def test_lineup_probe_workflow_writes_only_its_own_branch_and_cannot_poll_nhl_com_sheets():
    d = _load("nhl_lineup_probe.yml")
    text = (WF / "nhl_lineup_probe.yml").read_text()
    assert set(d["on"]) == {"workflow_dispatch"} and d["permissions"] == {"contents": "write"}
    assert "HEAD:lineup-probe-data" in text and "--force" not in text and "push origin main" not in text
    assert "sheets" not in d["on"]["workflow_dispatch"]["inputs"] and "--sheets" not in text and "htmlreports" not in text
    assert "(obs|raw)" in text and "--diff-filter=DMRTC" in text and "only be appended" in text
    assert d["jobs"]["probe"]["timeout-minutes"] <= 355 and "--max-minutes 330" in text and "from_utc" in d["on"]["workflow_dispatch"]["inputs"]       # hosted runners stop a job at 6 h
    assert "github.run_id" in d["concurrency"]["group"] and "MANIFEST.*.jsonl" in text and "did not complete" in text


def test_source_audit_workflow_is_manual_read_only_and_makes_no_repository_change():
    d = _load("source_audit.yml")
    text = (WF / "source_audit.yml").read_text()
    assert set(d["on"]) == {"workflow_dispatch"} and d["permissions"] == {"contents": "read"}
    assert "git push" not in text and "contents: write" not in text


def test_dispatch_drill_workflow_is_manual_and_only_needs_the_dispatch_permission():
    d = _load("lc_dispatch_drill.yml")
    text = (WF / "lc_dispatch_drill.yml").read_text()
    assert set(d["on"]) == {"workflow_dispatch"} and d["permissions"] == {"contents": "read", "actions": "write"}
    assert "--drill" in text and "git push" not in text and "contents: write" not in text
