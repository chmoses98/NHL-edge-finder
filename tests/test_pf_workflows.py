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
