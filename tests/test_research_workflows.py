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


def test_daily_publish_is_gated_by_owner_environment_variables_and_fails_closed():
    d = load("model_research_daily.yml")
    gates = [st for st in d["jobs"]["publish"]["steps"] if "Activation gate" in str(st.get("name", ""))]
    assert len(gates) == 1
    run, env = gates[0]["run"], yaml.safe_dump(gates[0]["env"])
    assert "vars.SEALED_LEDGER_ACTIVATION_SHA" in env and "vars.SEALED_LEDGER_GENESIS_HASH" in env  # ENVIRONMENT variables (the job references the environment)
    assert "exit 1" in run and "sha256sum" in run and "age1" in run and "[0-9a-f]{64}" in run
    assert 'if [ "$INIT" != true ]' in run  # only the one-time init may run before the owner has registered a genesis hash
    # the settle job holds no activation secret/variable at all: its precheck only refuses an unconfigured ledger
    settle = yaml.safe_dump(d["jobs"]["settle"])
    assert "SEALED_LEDGER_ACTIVATION_SHA" not in settle and "SEALED_LEDGER_GENESIS_HASH" not in settle
    # the gate precedes everything in the publish job that installs or runs code or fetches the artifact
    names = [str(st.get("name", st.get("uses", ""))) for st in d["jobs"]["publish"]["steps"]]
    assert names.index(gates[0]["name"]) < min(i for i, n in enumerate(names) if n.startswith(("actions/setup-python", "Install hash-locked", "actions/download-artifact", "Build the ledger")))


def test_genesis_hash_is_checked_against_the_owner_registered_value_before_any_append_is_committed():
    d = load("model_research_daily.yml")
    build = next(st for st in d["jobs"]["publish"]["steps"] if str(st.get("name", "")).startswith("Build the ledger commit"))
    assert build["run"].count('"${gen[@]}"') == 3 and "--expect-genesis-hash" in build["run"] and 'GENESIS' in yaml.safe_dump(build["env"])


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
    assert names.index(token_steps[0]) > max(i for i, n in enumerate(names) if str(n).startswith(("Build the ledger commit", "Install hash-locked", "Optional runner")) or n is None)


def test_selftest_step_can_fail_the_job_and_no_readme_or_extra_files_are_published():
    d = load("model_research_daily.yml")
    st = next(s for s in d["jobs"]["settle"]["steps"] if "selftest" in str(s.get("run", "")))
    assert "|" not in st["run"].replace("||", "")  # no pipeline: a failing self-test fails the step
    assert "README" not in (WF / "model_research_daily.yml").read_text().replace("README is", "")


def test_init_mode_exists_requires_publish_and_skips_the_archive():
    d = load("model_research_daily.yml")
    on = d[True] if True in d else d["on"]
    assert on["workflow_dispatch"]["inputs"]["init_ledger"]["default"] == "false"
    plan = next(st for st in d["jobs"]["settle"]["steps"] if st.get("id") == "plan")
    assert "init_ledger needs publish=true" in plan["run"] and "not allowed with init_ledger" in plan["run"]
    fetch = next(st for st in d["jobs"]["settle"]["steps"] if str(st.get("name", "")).startswith("Fetch a sparse"))
    assert "init != 'true'" in fetch["if"]
    audit = next(st for st in d["jobs"]["settle"]["steps"] if str(st.get("name", "")).startswith("Completeness audit"))
    assert "init != 'true'" in audit["if"] and "sealed_ledger.audit" in audit["run"]


# ---------------------------------------------------------------- supply chain: pinned actions and hash-locked dependencies ------------------------------------

REQ = Path(__file__).resolve().parents[1] / "requirements"


def test_every_action_in_the_research_workflows_is_pinned_to_a_full_commit_sha_with_a_version_comment():
    for n in RESEARCH:
        uses = re.findall(r"^\s*-?\s*uses:\s*(\S+)(.*)$", (WF / n).read_text(), flags=re.M)
        assert uses, n
        for ref, rest in uses:
            assert re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_./-]+@[0-9a-f]{40}", ref), (n, ref)
            assert re.search(r"#\s*v\d+\.\d+\.\d+", rest), (n, ref, "pin needs a '# vX.Y.Z' comment so a reviewer can tell what it is")


def test_research_workflows_install_only_from_hash_locked_requirements():
    for n in RESEARCH:
        text = (WF / n).read_text()
        installs = re.findall(r"pip install[^\n]*", text)
        for line in installs:
            assert "--require-hashes" in line and "--only-binary=:all:" in line and "--no-deps" in line and re.search(r"-r requirements/[a-z-]+\.lock", line), (n, line)
        assert "pip install -e" not in text and "uv pip" not in text and "poetry" not in text, n


def test_lock_files_are_complete_hashed_and_consistent():
    locks = sorted(REQ.glob("*.lock"))
    assert {p.name for p in locks} == {"research-runtime.lock", "sealed-publish.lock"}
    parsed = {}
    for lock in locks:
        assert (REQ / lock.name.replace(".lock", ".in")).exists(), lock.name
        pkgs, cur = {}, None
        for ln in lock.read_text().splitlines():
            if not ln.strip() or ln.lstrip().startswith("#"):
                continue
            m = re.match(r"^([A-Za-z0-9_.-]+)==([^\s;\\]+)", ln)
            if m:
                cur = m.group(1).lower()
                pkgs[cur] = {"version": m.group(2), "hashes": 0}
            else:
                assert re.match(r"^\s+--hash=sha256:[0-9a-f]{64}( \\)?$", ln), (lock.name, ln)
                pkgs[cur]["hashes"] += 1
        assert pkgs and all(v["hashes"] >= 1 for v in pkgs.values()), lock.name
        text = lock.read_text()
        assert not re.search(r"git\+|https?://|^-e |file:", text, flags=re.M), lock.name
        parsed[lock.name] = pkgs
    for name, v in parsed["sealed-publish.lock"].items():  # the small lock must agree with the big one wherever they overlap
        assert parsed["research-runtime.lock"][name]["version"] == v["version"], name
    for crypto in ("pyrage", "cryptography"):
        assert crypto in parsed["sealed-publish.lock"] and crypto in parsed["research-runtime.lock"]


# ---------------------------------------------------------------- the publication path cannot be reached by ordinary development workflows ------------------------

def test_no_other_workflow_touches_the_ledger_environment_variables_secrets_or_branch():
    for f in sorted(WF.glob("*.yml")):
        if f.name == "model_research_daily.yml":
            continue
        text = f.read_text()
        for needle in ("model-research-sealed-ledger", "sealed-ledger", "SEALED_LEDGER", "LEDGER_ATTEST", "sealed_ledger", "model_research_daily"):
            assert needle not in text, (f.name, needle)


def test_pull_request_workflows_are_read_only_and_use_no_environment_or_secret():
    for f in sorted(WF.glob("*.yml")):
        d = yaml.safe_load(f.read_text())
        on = d[True] if True in d else d["on"]
        triggers = on if isinstance(on, (list, dict)) else [on]
        if "pull_request" not in triggers and "pull_request_target" not in triggers:
            continue
        assert "pull_request_target" not in triggers, f.name  # that trigger would run with secrets on untrusted code
        assert d.get("permissions") is None or "write" not in yaml.safe_dump(d["permissions"]), f.name
        for name, j in d["jobs"].items():  # a write-permitted job in a PR-triggered workflow must be excluded from pull_request events
            if "write" in yaml.safe_dump(j.get("permissions")):
                assert "github.event_name != 'pull_request'" in str(j.get("if")), (f.name, name)
        assert all("environment" not in j for j in d["jobs"].values()), f.name
        assert "secrets." not in yaml.safe_dump(d).replace("secrets.GITHUB_TOKEN", ""), f.name


def test_only_the_publish_job_can_reach_the_environment_and_it_is_the_only_one_with_the_signing_secret():
    d = load("model_research_daily.yml")
    envs = {k: j.get("environment") for k, j in d["jobs"].items()}
    assert envs == {"settle": None, "publish": "sealed-ledger", "alert": None}


# ---------------------------------------------------------------- committed development material holds no prospective data -------------------------------------

def test_committed_research_tables_hold_no_post_freeze_game():
    import pandas as pd

    from nhl_edge.model_research import DEV_LAST_GAME_DATE_ET, PROSPECTIVE_FREEZE_UTC

    root = Path(__file__).resolve().parents[1] / "docs" / "research"
    checked = 0
    for f in sorted(root.glob("*/data/*.csv")):
        df = pd.read_csv(f)
        if "game_date_et" in df.columns:
            assert df["game_date_et"].astype(str).max() <= DEV_LAST_GAME_DATE_ET, (f.name, "contains a game dated after the development window")
            checked += 1
        if "start_time_utc" in df.columns:
            assert (pd.to_datetime(df["start_time_utc"], utc=True) < pd.Timestamp(PROSPECTIVE_FREEZE_UTC)).all(), f.name
    assert checked >= 3


def test_audit_verdict_is_applied_after_the_report_is_uploaded_and_exclusions_are_approval_gated():
    d = load("model_research_daily.yml")
    steps = d["jobs"]["settle"]["steps"]
    audit = next(st for st in steps if st.get("id") == "audit")
    fail = next(st for st in steps if str(st.get("name", "")).startswith("Fail the run if the completeness audit failed"))
    upload = next(i for i, st in enumerate(steps) if str(st.get("uses", "")).startswith("actions/upload-artifact") and "if" not in st)
    assert steps.index(audit) < upload < steps.index(fail)  # the owner can read SCHEDULE_AUDIT.json even when the audit fails the run
    assert "--allow-revised" in audit["run"] and "AUDIT PROBLEM" in audit["run"] and "steps.audit.outputs.rc" in fail["if"]
    plan = next(st for st in steps if st.get("id") == "plan")
    assert "exclusions need publish=true" in plan["run"] and "valid exclusion_reason" in plan["run"]
    on = d[True] if True in d else d["on"]
    assert on["workflow_dispatch"]["inputs"]["exclude_game_ids"]["default"] == ""
    # exclusions only reach the sealing path (publish=true) and, like every publish, run in the approval-gated environment
    ingest = next(st for st in steps if str(st.get("name", "")).startswith("Settle the date"))
    assert ingest["run"].index("--exclude") > ingest["run"].index('if [ "$PUBLISH" = true ]')
    gate = next(st for st in d["jobs"]["publish"]["steps"] if "Activation gate" in str(st.get("name", "")))
    assert "init refused: a genesis hash is already registered" in gate["run"]
