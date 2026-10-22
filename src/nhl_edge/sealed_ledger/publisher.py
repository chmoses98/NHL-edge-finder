"""Publish a staged sealed store to the ledger REPOSITORY (ciphertext + manifest only). Encrypt-only: no decrypt, no identity.

The ledger lives in its own public repository (``SEALED_LEDGER_REPO``) that contains no code, no workflow and no secret, so the only credential the automated publisher
holds -- a deploy key with write access to THAT repository alone -- can write nothing else on GitHub: not the code repository, not ``data-archive``, not a model file.
Every publish is a plain fast-forward push: the staged manifest must extend the remote one, share the owner's registered genesis hash and pass ``verify_store``; there is no
force, no delete, no rewrite. A rejected push is never "fixed" by rewriting: the next run starts again from the remote head (everything is idempotent).
"""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

from nhl_edge.sealed_ledger.core import MANIFEST, genesis_hash, is_extension, read_manifest, verify_store
from nhl_edge.sealed_ledger.seal import SealError, load_recipients

# GitHub's published ED25519 SSH host key (https://docs.github.com/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints),
# fingerprint SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU (a test recomputes it). Pinned so a deploy-key push can never go to a man-in-the-middle.
GITHUB_HOST_KEY = "github.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOMqqnkVzrm0SdG6UOoqKLsabgH5C9okWi0dh2l9GKJl"
GITHUB_HOST_FINGERPRINT = "SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU"
BOT = ("nhl-edge-bot", "nhl-edge-bot@users.noreply.github.com")


class PublishError(Exception):
    pass


def _git(args: list[str], cwd: Path | None = None, env: dict[str, str] | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    e = {**os.environ, "GIT_TERMINAL_PROMPT": "0", "GIT_CONFIG_NOSYSTEM": "1", **(env or {})}
    r = subprocess.run(["git", "-c", f"user.name={BOT[0]}", "-c", f"user.email={BOT[1]}", "-c", "commit.gpgsign=false", *args], cwd=cwd, env=e, capture_output=True, text=True, check=False)
    if check and r.returncode != 0:
        # git's stderr can contain URLs; never the key (it is read from a file path by ssh, not passed on the command line)
        raise PublishError(f"git {' '.join(a for a in args if not a.startswith('-c'))[:60]} failed (exit {r.returncode}): {r.stderr.strip()[:300]}")
    return r


def ssh_env(key: Path | None, known_hosts: Path | None) -> dict[str, str]:
    if key is None:
        return {}
    kh = known_hosts
    cmd = f"ssh -i {key} -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes -o BatchMode=yes"
    if kh is not None:
        cmd += f" -o UserKnownHostsFile={kh}"
    return {"GIT_SSH_COMMAND": cmd}


def write_known_hosts(path: Path) -> Path:
    path.write_text(GITHUB_HOST_KEY + "\n")
    path.chmod(0o644)
    return path


def _remote_has_branch(url: str, branch: str, env: dict[str, str]) -> str | None:
    r = _git(["ls-remote", "--heads", url, branch], env=env, check=False)
    if r.returncode != 0:
        raise PublishError(f"cannot read the ledger repository: {r.stderr.strip()[:200]}")
    return r.stdout.split()[0] if r.stdout.strip() else None


def publish(staged: Path, *, read_url: str, push_url: str, recipients: Path, init: bool = False, expect_genesis: str | None = None, branch: str = "main",
            ssh_key: Path | None = None, known_hosts: Path | None = None, message: str = "sealed-ledger: update", forbid_url_substring: str | None = None,
            attempts: int = 3, sleep: float = 5.0) -> dict[str, Any]:
    """Verify the staged store against the remote and push it (fast-forward only). Returns an outcome-free summary."""
    staged = Path(staged)
    if forbid_url_substring and forbid_url_substring.lower() in (read_url + " " + push_url).lower():
        raise PublishError("the ledger destination is the code repository; refusing (the ledger lives in its own repository)")
    rec_sha = load_recipients(recipients)[1]
    rep = verify_store(staged, recipients_sha256=rec_sha)
    if not rep.ok:
        raise PublishError("staged store fails verification: " + "; ".join(rep.problems[:5]))
    new = read_manifest(staged)
    if not init and (expect_genesis is None or genesis_hash(new) != expect_genesis):
        raise PublishError("the staged ledger's genesis hash is not the one the owner registered (a different ledger): refusing")
    work = Path(tempfile.mkdtemp(prefix="ledger_publish_"))
    try:
        wt = work / "ledger"
        read_env: dict[str, str] = {}
        head = _remote_has_branch(read_url, branch, read_env)
        if head is None:  # empty remote: only the owner-approved init may create the first commit
            if not init:
                raise PublishError("the ledger repository is empty: the ledger must be created by the approved init procedure first")
            _git(["init", "-q", "-b", branch, str(wt)])
            _git(["remote", "add", "origin", read_url], cwd=wt)
            old: list[dict[str, Any]] = []
        else:
            if init:
                raise PublishError("init refused: the ledger repository already holds a ledger")
            _git(["clone", "-q", "--branch", branch, "--single-branch", read_url, str(wt)])
            problems = verify_store(wt, recipients_sha256=rec_sha).problems
            if problems:
                raise PublishError("the REMOTE ledger fails verification: " + "; ".join(problems[:5]))
            old = read_manifest(wt)
            if genesis_hash(old) != genesis_hash(new) and not init:
                raise PublishError("remote and staged ledgers have different genesis hashes")
            ext = is_extension(old, new)
            if ext:
                raise PublishError("the staged manifest does not extend the remote one (append-only): " + "; ".join(ext[:3]))
        _git(["remote", "set-url", "--push", "origin", push_url], cwd=wt)
        for item in sorted(staged.iterdir()):
            if item.name == ".git":
                continue
            dest = wt / item.name
            if item.is_dir():
                shutil.copytree(item, dest, dirs_exist_ok=True)
            else:
                shutil.copy2(item, dest)
        after = verify_store(wt, recipients_sha256=rec_sha)
        if not after.ok:
            raise PublishError("merged ledger fails verification: " + "; ".join(after.problems[:5]))
        _git(["add", "-A"], cwd=wt)
        if _git(["diff", "--cached", "--quiet"], cwd=wt, check=False).returncode == 0 and head is not None:
            return {"pushed": False, "note": "nothing new to publish", "head_seq": after.head_seq, "head_hash": after.head_hash}
        _git(["commit", "-q", "-m", f"{message} (head seq {after.head_seq})"], cwd=wt)
        penv = ssh_env(ssh_key, known_hosts)
        local_head = _git(["rev-parse", "HEAD"], cwd=wt).stdout.strip()
        for i in range(attempts):
            r = _git(["push", "origin", f"HEAD:refs/heads/{branch}"], cwd=wt, env=penv, check=False)  # never --force
            if r.returncode == 0:
                break
            remote_now = _remote_has_branch(read_url, branch, read_env)
            if remote_now == local_head:  # the push landed but the reply was lost
                break
            if "non-fast-forward" in r.stderr or "rejected" in r.stderr:
                raise PublishError("push rejected (the remote moved): not rewriting; the next run starts again from the remote head")
            if i == attempts - 1:
                raise PublishError(f"push failed after {attempts} attempts: {r.stderr.strip()[:200]}")
            time.sleep(sleep * (3**i))
        tag = f"sealed-ledger-head-{after.head_seq}"
        if not _git(["ls-remote", "--tags", read_url, f"refs/tags/{tag}"], check=False).stdout.strip():  # re-runs create a missing tag instead of skipping it
            _git(["tag", "-a", tag, "-m", f"head {after.head_seq} {after.head_hash}"], cwd=wt)
            _git(["push", "origin", f"refs/tags/{tag}"], cwd=wt, env=penv)
        return {"pushed": True, "head_seq": after.head_seq, "head_hash": after.head_hash, "genesis_hash": genesis_hash(read_manifest(wt)), "tag": tag, "manifest": MANIFEST}
    finally:
        shutil.rmtree(work, ignore_errors=True)


__all__ = ["BOT", "GITHUB_HOST_FINGERPRINT", "GITHUB_HOST_KEY", "PublishError", "SealError", "publish", "ssh_env", "write_known_hosts"]
