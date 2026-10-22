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
