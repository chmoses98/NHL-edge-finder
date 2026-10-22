"""Static guards for the research workflows: manual-only, no schedule, publish defaults to false, no relative artifact paths (upload-artifact rejects '..'),
and the daily loop's default artifact never contains the outcome-bearing ledger."""

from __future__ import annotations

from pathlib import Path

import yaml

WF = Path(__file__).resolve().parents[1] / ".github" / "workflows"
RESEARCH = ("market_audit.yml", "model_research_daily.yml")


def load(name: str) -> dict:
    return yaml.safe_load((WF / name).read_text())


def test_research_workflows_are_manual_only_with_publish_false_by_default():
    for n in RESEARCH:
        d = load(n)
        on = d[True] if True in d else d["on"]
        assert list(on) == ["workflow_dispatch"], (n, list(on))
        assert on["workflow_dispatch"]["inputs"]["publish"]["default"] == "false"


def test_no_relative_artifact_or_download_paths():
    for n in RESEARCH:
        for job in load(n)["jobs"].values():
            for st in job["steps"]:
                if str(st.get("uses", "")).startswith(("actions/upload-artifact", "actions/download-artifact")):
                    p = str(st["with"].get("path", ""))
                    assert ".." not in p.replace("${{", "").replace("}}", ""), (n, p)


def test_daily_loop_default_artifact_excludes_the_ledger_and_write_is_isolated():
    d = load("model_research_daily.yml")
    settle, publish = d["jobs"]["settle"], d["jobs"]["publish"]
    assert settle["permissions"] == {"contents": "read"} and publish["permissions"] == {"contents": "write"}
    default_uploads = [st for st in settle["steps"] if str(st.get("uses", "")).startswith("actions/upload-artifact") and "if" not in st]
    assert len(default_uploads) == 1
    assert "ledger" not in str(default_uploads[0]["with"]["path"])
    private = [st for st in settle["steps"] if str(st.get("uses", "")).startswith("actions/upload-artifact") and "if" in st]
    assert all("publish == 'true'" in st["if"] for st in private)
    assert publish["if"].count("publish == 'true'") == 1


def test_write_permission_is_confined_to_a_publish_job_and_nothing_is_force_pushed():
    for n in RESEARCH:
        d = load(n)
        assert d["permissions"] == {"contents": "read"}, n  # workflow-level default is read-only
        writers = [k for k, j in d["jobs"].items() if (j.get("permissions") or {}).get("contents") == "write"]
        assert writers == ["publish"], (n, writers)
        assert d["jobs"]["publish"]["if"].count("publish == 'true'") == 1
        assert "--force" not in (WF / n).read_text().replace("never forced", ""), n


def test_daily_publish_is_refused_while_the_repository_is_public_and_the_ledger_is_not_isolated():
    d = load("model_research_daily.yml")
    guards = [st for st in d["jobs"]["settle"]["steps"] if "Refuse publish" in str(st.get("name", ""))]
    assert len(guards) == 1 and "publish == 'true'" in guards[0]["if"] and "exit 1" in guards[0]["run"]
    # the guard must come before anything is fetched, restored or ingested
    names = [str(st.get("name", st.get("uses", ""))) for st in d["jobs"]["settle"]["steps"]]
    assert names.index(guards[0]["name"]) <= 2
