"""Static guards for the research workflows.

Unattended architecture (see docs/research/nhl-model-improvement/SEALED_LEDGER_UNATTENDED.md):
* ``sealed_ledger_daily.yml``: routine, parameter-free, NO write permission on this repository anywhere; its only write capability is a deploy key for the ledger REPOSITORY
  (released to one job through an environment with no reviewers, restricted to ``main`` by the owner); cannot init, correct by hand, exclude by hand or change anything here.
* ``sealed_ledger_admin.yml``: init / hand corrections / hand exclusions; its publish job waits for the owner's approval.
* ``market_audit.yml``: the older research audit (read-only default, write only in a separate publish job, no force push).
Plus supply-chain pins, the publish script, and isolation from every other workflow."""

from __future__ import annotations

import ast
import re
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WF = ROOT / ".github" / "workflows"
REQ = ROOT / "requirements"
DAILY, ADMIN, AUDIT = "sealed_ledger_daily.yml", "sealed_ledger_admin.yml", "market_audit.yml"
RESEARCH = (AUDIT, DAILY, ADMIN)
SEALED = (DAILY, ADMIN)
SCRIPT = ROOT / "scripts" / "sealed_ledger_publish.sh"


def load(name: str) -> dict:
    return yaml.safe_load((WF / name).read_text())


def triggers(d: dict) -> dict:
    return d[True] if True in d else d["on"]


# ---------------------------------------------------------------- manual-only, nothing enabled --------------------------------------------------------------

def test_research_workflows_are_manual_only_and_nothing_is_scheduled():
    for n in RESEARCH:
        assert list(triggers(load(n))) == ["workflow_dispatch"], n
    assert triggers(load(AUDIT))["workflow_dispatch"]["inputs"]["publish"]["default"] == "false"
    # the schedule exists only as a comment, ready for the owner's approval
    assert re.search(r"^\s*#\s*schedule:", (WF / DAILY).read_text(), flags=re.M)
    assert not re.search(r"^\s*schedule:", (WF / DAILY).read_text(), flags=re.M)


def test_the_unattended_workflow_takes_no_input_except_a_dry_run_flag_and_cannot_init_correct_or_exclude():
    d = load(DAILY)
    assert list(triggers(d)["workflow_dispatch"]["inputs"]) == ["dry_run"] and triggers(d)["workflow_dispatch"]["inputs"]["dry_run"]["default"] == "false"
    text = yaml.safe_dump(d)
    for banned in ("--init", "--correct", "init_ledger", "correct_game_ids", "exclude_game_ids", "MODE: init", "sealed-ledger-admin"):
        assert banned not in text, banned
    assert not re.search(r"--exclude(?!-dir)", text)  # (grep's --exclude-dir is not ours)
    adm = triggers(load(ADMIN))["workflow_dispatch"]["inputs"]
    assert set(adm) == {"action", "date", "game_ids", "reason"} and adm["action"]["options"] == ["init", "correct", "exclude", "accept_missing"]


# ---------------------------------------------------------------- permissions: the routine path cannot write this repository ---------------------------------------

def test_no_sealed_workflow_has_any_write_permission_on_this_repository():
    for n in SEALED:
        d = load(n)
        assert d["permissions"] == {"contents": "read"}, n
        for name, j in d["jobs"].items():
            perms = j.get("permissions") or {}
            assert perms.get("contents") == "read", (n, name)
            writers = {k: v for k, v in perms.items() if v != "read"}
            assert writers in ({}, {"issues": "write"}), (n, name, writers)  # the ONLY other grant: one deduplicated issue per exception
    assert [k for k, j in load(DAILY)["jobs"].items() if "issues" in (j.get("permissions") or {})] == ["alert"]
    assert not [k for k, j in load(ADMIN)["jobs"].items() if "issues" in (j.get("permissions") or {})]


def test_market_audit_keeps_write_confined_to_a_publish_job_and_nothing_is_force_pushed():
    d = load(AUDIT)
    assert d["permissions"] == {"contents": "read"}
    assert [k for k, j in d["jobs"].items() if (j.get("permissions") or {}).get("contents") == "write"] == ["publish"]
    assert d["jobs"]["publish"]["if"].count("publish == 'true'") == 1
    text = (WF / AUDIT).read_text()
    assert "--force" not in text.replace("never forced", "") and "push -f" not in text


def test_environments_and_secrets_are_scoped_to_the_publish_jobs_only():
    daily, admin = load(DAILY), load(ADMIN)
    assert {k: j.get("environment") for k, j in daily["jobs"].items()} == {"reconcile": None, "publish": "sealed-ledger-publish", "alert": None}
    assert {k: j.get("environment") for k, j in admin["jobs"].items()} == {"settle": None, "publish": "sealed-ledger-admin"}
    for d in (daily, admin):
        for name, j in d["jobs"].items():
            blob = yaml.safe_dump(j)
            if name != "publish":
                assert "secrets." not in blob.replace("secrets.GITHUB_TOKEN", "") and "SEALED_LEDGER_ACTIVATION_SHA" not in blob and "SEALED_LEDGER_GENESIS_HASH" not in blob, name
    for n in SEALED:
        raw = (WF / n).read_text()
        assert set(re.findall(r"secrets\.([A-Z0-9_]+)", raw)) == {"SEALED_LEDGER_DEPLOY_KEY"}  # no decryption key and no token of any kind exists on GitHub
        assert set(re.findall(r"vars\.([A-Z0-9_]+)", raw)) <= {"SEALED_LEDGER_REPO", "SEALED_LEDGER_ACTIVATION_SHA", "SEALED_LEDGER_GENESIS_HASH"}


def test_the_routine_publish_job_has_no_reviewer_prompt_but_the_admin_one_is_the_only_approval_gate_in_code():
    # approval is configured by the owner on the environments, not in the file; the file just routes the two paths to two different environments
    daily_pub, admin_pub = load(DAILY)["jobs"]["publish"], load(ADMIN)["jobs"]["publish"]
    assert daily_pub["environment"] != admin_pub["environment"]
    assert load(DAILY)["jobs"]["publish"]["steps"][-1]["env"]["MODE"] == "append"  # hard-coded: the routine path can never run init
    assert "init" in str(admin_pub["steps"][-1]["env"]["MODE"])


def test_routine_runs_only_the_sealed_ledger_modules_and_the_publish_script():
    for n in SEALED:
        raw = yaml.safe_dump(load(n))  # parsed content: comments explaining what is NOT done are not part of it
        mods = set(re.findall(r"python -m ([A-Za-z0-9_.]+)", raw))
        assert mods and all(m == "pip" or m.startswith("nhl_edge.sealed_ledger.") for m in mods), (n, mods)  # no production, model, conductor or capture module is ever run
        for banned in ("nhl_edge.workflows", "nhl_edge.cli", "conductor", "capture_worker", "edge_finder", "stake", "recommend"):
            assert banned not in raw.replace("recommendation", ""), (n, banned)
        scripts = set(re.findall(r"run: (scripts/[A-Za-z0-9_./-]+)", (WF / n).read_text()))
        assert scripts <= {"scripts/sealed_ledger_publish.sh"}, scripts


def test_nothing_in_the_routine_workflow_writes_a_file_in_the_checkout():
    raw = (WF / DAILY).read_text()
    assert "git push" not in raw and "git commit" not in raw and "git tag" not in raw  # the only push is inside the audited publisher, to the ledger repository
    assert "GITHUB_WORKSPACE/src" in raw  # PYTHONPATH only; the checkout is read, never written


# ---------------------------------------------------------------- the publish script -----------------------------------------------------------------------------

def test_publish_script_is_syntax_valid_fail_closed_and_never_exposes_the_key():
    assert subprocess.run(["bash", "-n", str(SCRIPT)], capture_output=True).returncode == 0
    text = SCRIPT.read_text()
    code = "\n".join(ln for ln in text.splitlines() if not ln.lstrip().startswith("#"))
    assert "set -euo pipefail" in code and "set -x" not in code and "xtrace" not in code
    assert re.search(r'echo[^\n]*DEPLOY_KEY', code) is None and "cat " not in code and 'printf \'%s\\n\' "$DEPLOY_KEY" > "$key"' in code
    assert "umask 077" in code and "trap 'rm -f \"$key\"' EXIT" in code
    for needle in ("ACTIVATION", "GENESIS", "must be a different repository", "--forbid-repo", "--expect-genesis", "[0-9a-f]{64}", "sha256sum"):
        assert needle in code, needle
    assert "--force" not in code and "--delete" not in code and "push" not in code.replace("--push-url", "")  # the push is inside the audited publisher
    assert '--ssh-key "$key"' in code  # the key reaches ssh by path only
    # mode init requires that NO genesis is registered yet; append requires one
    assert code.index("--init") > code.index("init refused") - 400


def test_genesis_and_activation_gates_are_not_in_the_settle_jobs():
    for n in SEALED:
        d = load(n)
        for name, j in d["jobs"].items():
            if name not in ("publish", "alert"):
                blob = yaml.safe_dump(j)
                assert "DEPLOY_KEY" not in blob and "SEALED_LEDGER_ACTIVATION_SHA" not in blob, (n, name)


# ---------------------------------------------------------------- bounded resources ------------------------------------------------------------------------------

def test_bounded_resources_one_writer_and_short_retention():
    for n in SEALED:
        d = load(n)
        assert d["concurrency"] == {"group": "sealed-ledger-daily" if n == DAILY else "sealed-ledger-admin", "cancel-in-progress": False}, n  # separate groups: a pending owner approval never starves the daily run; a race is a safe non-fast-forward rejection
        for name, j in d["jobs"].items():
            assert j["timeout-minutes"] <= 45, (n, name)
        for j in d["jobs"].values():
            for st in j["steps"]:
                if str(st.get("uses", "")).startswith("actions/upload-artifact"):
                    assert st["with"]["retention-days"] <= 14
    pub_artifacts = [st for st in load(DAILY)["jobs"]["reconcile"]["steps"] if str(st.get("uses", "")).startswith("actions/upload-artifact") and "if" in st]
    assert len(pub_artifacts) == 1 and pub_artifacts[0]["with"]["retention-days"] == 1 and "dry != 'true'" in pub_artifacts[0]["if"]  # the staged store is not kept


def test_alerts_fire_on_failure_or_blocked_only_and_waiting_is_not_an_alert():
    alert = load(DAILY)["jobs"]["alert"]
    assert "BLOCKED" in alert["if"] and "failure" in alert["if"] and "WAITING" not in alert["if"] and "IDLE" not in alert["if"]
    assert "dry != 'true'" in alert["if"]  # a dry run never opens an issue
    run = alert["steps"][0]["run"]
    assert "gh issue list" in run and "gh issue create" in run and "--state open" in run  # deduplicated: one open issue per cause
    assert "needs.reconcile.outputs.codes" in yaml.safe_dump(alert)


def test_the_blinding_check_whitelist_matches_what_reconcile_can_emit():
    raw = (WF / DAILY).read_text()
    lit = re.search(r"ok_summary = (\{.*?\})\n", raw, flags=re.S).group(1)
    allowed = ast.literal_eval(lit.replace("\n", " "))
    from nhl_edge.sealed_ledger import reconcile  # noqa: F401 - the keys below are asserted in tests/test_sealed_reconcile.py::test_the_summary_is_outcome_free

    assert {"mode", "through", "status", "dates_closed", "games_sealed", "corrections", "exclusions", "waiting", "blocked", "reproduction_max_abs_diff", "manifest_entries",
            "head_seq", "head_hash", "changed", "note"} == allowed


# ---------------------------------------------------------------- supply chain: pinned actions and hash-locked dependencies ------------------------------------

def test_no_relative_artifact_or_download_paths():
    for n in RESEARCH:
        for job in load(n)["jobs"].values():
            for st in job["steps"]:
                if str(st.get("uses", "")).startswith(("actions/upload-artifact", "actions/download-artifact")):
                    p = str(st["with"].get("path", ""))
                    assert ".." not in p.replace("${{", "").replace("}}", ""), (n, p)


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
        for line in re.findall(r"pip install[^\n]*", text):
            assert "--require-hashes" in line and "--only-binary=:all:" in line and "--no-deps" in line and re.search(r"-r requirements/[a-z-]+\.lock", line), (n, line)
        assert "pip install -e" not in text and "uv pip" not in text and "poetry" not in text, n
    publish_installs = re.findall(r"requirements/([a-z-]+)\.lock", yaml.safe_dump(load(DAILY)["jobs"]["publish"]) + yaml.safe_dump(load(ADMIN)["jobs"]["publish"]))
    assert set(publish_installs) == {"sealed-publish"}  # the jobs that hold the deploy key install the smallest possible set


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
        assert not re.search(r"git\+|https?://|^-e |file:", lock.read_text(), flags=re.M), lock.name
        parsed[lock.name] = pkgs
    for name, v in parsed["sealed-publish.lock"].items():
        assert parsed["research-runtime.lock"][name]["version"] == v["version"], name
    for crypto in ("pyrage", "cryptography"):
        assert crypto in parsed["sealed-publish.lock"] and crypto in parsed["research-runtime.lock"]


# ---------------------------------------------------------------- isolation from every other workflow ------------------------------------------------------------

def test_no_other_workflow_touches_the_ledger_environments_variables_secrets_or_modules():
    for f in sorted(WF.glob("*.yml")):
        if f.name in SEALED:
            continue
        text = f.read_text()
        for needle in ("sealed-ledger", "SEALED_LEDGER", "sealed_ledger", "LEDGER_DEPLOY", "model_research_daily"):
            assert needle not in text, (f.name, needle)


def test_pull_request_workflows_are_read_only_and_use_no_environment_or_secret():
    for f in sorted(WF.glob("*.yml")):
        d = yaml.safe_load(f.read_text())
        on = d[True] if True in d else d["on"]
        trig = on if isinstance(on, (list, dict)) else [on]
        if "pull_request" not in trig and "pull_request_target" not in trig:
            continue
        assert "pull_request_target" not in trig, f.name  # that trigger would run with secrets on untrusted code
        assert d.get("permissions") is None or "write" not in yaml.safe_dump(d["permissions"]), f.name
        for name, j in d["jobs"].items():  # a write-permitted job in a PR-triggered workflow must be excluded from pull_request events
            if "write" in yaml.safe_dump(j.get("permissions")):
                assert "github.event_name != 'pull_request'" in str(j.get("if")), (f.name, name)
        assert all("environment" not in j for j in d["jobs"].values()), f.name
        assert "secrets." not in yaml.safe_dump(d).replace("secrets.GITHUB_TOKEN", ""), f.name


def test_committed_research_tables_hold_no_post_freeze_game():
    import pandas as pd

    from nhl_edge.model_research import DEV_LAST_GAME_DATE_ET, PROSPECTIVE_FREEZE_UTC

    checked = 0
    for f in sorted((ROOT / "docs" / "research").glob("*/data/*.csv")):
        df = pd.read_csv(f)
        if "game_date_et" in df.columns:
            assert df["game_date_et"].astype(str).max() <= DEV_LAST_GAME_DATE_ET, (f.name, "contains a game dated after the development window")
            checked += 1
        if "start_time_utc" in df.columns:
            assert (pd.to_datetime(df["start_time_utc"], utc=True) < pd.Timestamp(PROSPECTIVE_FREEZE_UTC)).all(), f.name
    assert checked >= 3


def test_owner_weekly_script_is_local_never_prints_the_passphrase_and_decrypts_nothing():
    script = ROOT / "scripts" / "owner_weekly_check.sh"
    assert subprocess.run(["bash", "-n", str(script)], capture_output=True).returncode == 0
    code = "\n".join(ln for ln in script.read_text().splitlines() if not ln.lstrip().startswith("#"))
    assert "weekly-check" in code and "security find-generic-password -s sift-witness -w" in code and "set -x" not in code
    assert "look" not in code.replace("--store", "") and "keygen" not in code and "--identity" not in code  # no key, no decryption, no look
    assert re.search(r"echo[^\n]*(passphrase|PASSPHRASE)", code) is None
