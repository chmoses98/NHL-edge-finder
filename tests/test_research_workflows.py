"""Static guards for the research workflows: manual-only, no schedule, publish defaults to false, no relative artifact paths (upload-artifact rejects '..'), write
permission only in a separate publish job, no force push, and -- for the daily loop -- the sealed-ledger activation gate, the absence of any decryption material or path,
and that the default artifact never contains anything but the blinded scorecard, the outcome-free summary and the synthetic self-test result."""

from __future__ import annotations

import re
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


def test_daily_loop_default_artifact_excludes_the_store_and_write_is_isolated():
    d = load("model_research_daily.yml")
    settle, publish = d["jobs"]["settle"], d["jobs"]["publish"]
    assert settle["permissions"] == {"contents": "read"} and publish["permissions"] == {"contents": "write"}
    uploads = [st for st in settle["steps"] if str(st.get("uses", "")).startswith("actions/upload-artifact")]
    default = [st for st in uploads if "if" not in st]
    assert len(default) == 1 and str(default[0]["with"]["path"]).rstrip("/").endswith("rd/out")
    gated = [st for st in uploads if "if" in st]
    assert len(gated) == 1 and "publish == 'true'" in gated[0]["if"] and str(gated[0]["with"]["path"]).rstrip("/").endswith("rd/store")  # ciphertext + manifest only
    assert publish["if"].count("publish == 'true'") == 1


def test_write_permission_is_confined_to_a_publish_job_and_nothing_is_force_pushed():
    for n in RESEARCH:
        d = load(n)
        assert d["permissions"] == {"contents": "read"}, n  # workflow-level default is read-only
        writers = [k for k, j in d["jobs"].items() if (j.get("permissions") or {}).get("contents") == "write"]
        assert writers == ["publish"], (n, writers)
        text = (WF / n).read_text()
        assert "--force" not in text.replace("never forced", "") and "push -f" not in text, n
    alerts = [k for k, j in load("model_research_daily.yml")["jobs"].items() if "issues" in (j.get("permissions") or {})]
    assert alerts == ["alert"]  # the only other grant: one issue per failed date, contents stay read-only
    assert load("model_research_daily.yml")["jobs"]["alert"]["permissions"] == {"contents": "read", "issues": "write"}


def test_daily_publish_is_gated_by_an_owner_activation_in_both_jobs_and_fails_closed():
    d = load("model_research_daily.yml")
    for job in ("settle", "publish"):
        gates = [st for st in d["jobs"][job]["steps"] if "Activation gate" in str(st.get("name", ""))]
        assert len(gates) == 1, job
        run = gates[0]["run"]
        assert "SEALED_LEDGER_ACTIVATION_SHA" in str(gates[0]["env"]) and "exit 1" in run and "sha256sum" in run and "age1" in run
        if job == "settle":
            assert "publish == 'true'" in gates[0]["if"]
    # the gate must precede anything that fetches the archive, restores the ledger or seals
    names = [str(st.get("name", st.get("uses", ""))) for st in d["jobs"]["settle"]["steps"]]
    assert names.index(next(n for n in names if n.startswith("Activation gate"))) < names.index("Fetch a sparse read-only copy of the archive")


def test_daily_workflow_has_no_decryption_path_or_key_material():
    text = yaml.safe_dump(load("model_research_daily.yml"))  # parsed content: comments (which explain what is NOT done) are not part of it
    for banned in ("sealed_ledger.owner", "pyrage.decrypt", "age -d", "--identity", "SEALED_LEDGER_PRIVATE", "decrypt"):
        assert banned not in text, banned
    secrets_used = set(re.findall(r"secrets\.([A-Z0-9_]+)", text))
    assert secrets_used <= {"LEDGER_ATTEST_KEY_PEM"}, secrets_used  # an optional SIGNING key only; no decryption key exists on GitHub
    d = load("model_research_daily.yml")
    assert "secrets." not in yaml.safe_dump(d["jobs"]["settle"]) and "secrets." not in yaml.safe_dump(d["jobs"]["alert"])  # the signing secret is only reachable in the publish job
    raw = (WF / "model_research_daily.yml").read_text()
    assert text.count("--seal") == 1  # sealing happens only under the PUBLISH=true branch
    assert 'if [ "$PUBLISH" = true ]; then\n            args+=(--seal)' in raw


def test_inputs_are_only_used_through_env_vars():
    text = (WF / "model_research_daily.yml").read_text()
    for m in re.finditer(r"run: \|\n((?:[ ]{10,}.*\n)+)", text):
        assert "github.event.inputs" not in m.group(1) and "steps.plan.outputs" not in m.group(1), m.group(1)[:80]


def test_bounded_resources_and_serialised_runs():
    d = load("model_research_daily.yml")
    assert d["concurrency"] == {"group": "model-research-daily", "cancel-in-progress": False}
    for name, j in d["jobs"].items():
        assert j["timeout-minutes"] <= 30, name
    assert all(st["with"].get("retention-days", 99) <= 14 for j in d["jobs"].values() for st in j["steps"] if str(st.get("uses", "")).startswith("actions/upload-artifact"))


def test_publish_runs_only_from_main_in_a_protected_environment_with_a_token_free_checkout():
    d = load("model_research_daily.yml")
    raw = (WF / "model_research_daily.yml").read_text()
    assert d["jobs"]["publish"]["environment"] == "sealed-ledger"
    assert raw.count('refs/heads/main') >= 3  # the plan step and the publish-job gate both refuse any other ref
    co = d["jobs"]["publish"]["steps"][0]
    assert str(co["uses"]).startswith("actions/checkout") and co["with"]["persist-credentials"] is False
    # the write token appears in exactly one step (push), after dependencies are installed and verification has run
    token_steps = [st["name"] for st in d["jobs"]["publish"]["steps"] if "github.token" in yaml.safe_dump(st)]
    assert len(token_steps) == 1 and token_steps[0].startswith("Push the ledger branch")
    names = [st.get("name", st.get("uses")) for st in d["jobs"]["publish"]["steps"]]
    assert names.index(token_steps[0]) > max(i for i, n in enumerate(names) if str(n).startswith(("Build the ledger commit", "pip", "Optional runner")) or n is None)


def test_selftest_step_can_fail_the_job_and_no_readme_or_extra_files_are_published():
    d = load("model_research_daily.yml")
    st = next(s for s in d["jobs"]["settle"]["steps"] if "selftest" in str(s.get("run", "")))
    assert "|" not in st["run"].replace("||", "")  # no pipeline: a failing self-test fails the step
    assert "README" not in (WF / "model_research_daily.yml").read_text().replace("README is", "")
