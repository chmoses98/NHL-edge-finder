"""OWNER-LOCAL tool for the sealed prospective ledger. The ONLY module that can decrypt. Run it on your own machine, never in CI, never from a development session.

    python -m nhl_edge.sealed_ledger.owner keygen         --identity ~/sift-ledger/identity.txt          # prints ONLY the public key
    python -m nhl_edge.sealed_ledger.owner check-key      --identity ~/sift-ledger/identity.txt --recipients <repo>/research/sealed_ledger/recipients.txt
    python -m nhl_edge.sealed_ledger.owner drill          --store <ledger checkout> --identity primary.txt --identity backup.txt --recipients <repo>/research/sealed_ledger/recipients.txt
    python -m nhl_edge.sealed_ledger.owner first-checkpoint --store <ledger checkout> --identity primary.txt --identity backup.txt --dir ~/sift-ledger/witness --recipients <...>
    python -m nhl_edge.sealed_ledger.owner witness-keygen --dir ~/sift-ledger/witness
    python -m nhl_edge.sealed_ledger.owner witness        --store <ledger checkout> --dir ~/sift-ledger/witness --recipients <repo>/research/sealed_ledger/recipients.txt
    python -m nhl_edge.sealed_ledger.owner weekly-check   --store ~/sift-ledger/ledger --dir ~/sift-ledger/witness --recipients <repo>/research/sealed_ledger/recipients.txt --ledger-url https://github.com/<owner>/<ledger repo>.git --passphrase-cmd '...'
    python -m nhl_edge.sealed_ledger.owner verify         --store <ledger checkout> --dir ~/sift-ledger/witness [--recipients ...] [--attest-pub runner_public.pem]
    python -m nhl_edge.sealed_ledger.owner reproduce      --store <ledger checkout> --identity ~/sift-ledger/identity.txt --archive <data-archive checkout> --repo .
    python -m nhl_edge.sealed_ledger.owner look           --store <ledger checkout> --identity ~/sift-ledger/identity.txt --dir ~/sift-ledger/witness --recipients <repo>/research/sealed_ledger/recipients.txt --out ~/sift-ledger/looks

``look`` refuses to decrypt anything before the preregistered 150 distinct games exist, refuses to run twice for the same look, and verifies the whole store (chain,
ciphertext hashes, witness checkpoints) before it touches a key. It never prints a record. The private key is read from a file path you give; it is never taken from
an environment variable, an argument or a prompt-echo, and never leaves this process. Under CI (``GITHUB_ACTIONS``/``CI``) every command refuses to run.
"""

from __future__ import annotations

import argparse
import getpass
import json
import os
import shlex
import shutil
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import pyrage
from pyrage import passphrase as _pw
from pyrage import x25519

from nhl_edge.model_research import daily
from nhl_edge.sealed_ledger import RECORD_SCHEMA
from nhl_edge.sealed_ledger import checkpoint as CP
from nhl_edge.sealed_ledger.core import (
    CHECKPOINT_DIR,
    closed_games,
    ct_path,
    genesis_hash,
    is_extension,
    read_manifest,
    verify_store,
)
from nhl_edge.sealed_ledger.seal import SealError, load_recipients

_SECRET_PREFIX = "AGE-SECRET-KEY-"


def refuse_in_ci() -> None:
    if os.environ.get("GITHUB_ACTIONS") or os.environ.get("CI", "").lower() == "true":
        raise SystemExit("owner.py decrypts prospective results and must not run in CI or any automated environment")


# ---- keys ------------------------------------------------------------------------------------------------------------------------------------------------

def generate_identity(path: Path) -> str:
    """Write an ``age-keygen``-format identity file (mode 0600, never overwritten) and return the PUBLIC key."""
    refuse_in_ci()
    path = Path(path).expanduser()
    if path.exists():
        raise SystemExit(f"{path} already exists; refusing to overwrite a private key")
    ident = x25519.Identity.generate()
    pub = str(ident.to_public())
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w") as fh:
        fh.write(f"# created: {datetime.now(UTC).strftime('%Y-%m-%dT%H:%M:%SZ')}\n# public key: {pub}\n{ident}\n")
    return pub


def load_identities(path: Path, passphrase: str | None = None) -> list[Any]:
    path = Path(path).expanduser()
    raw = path.read_bytes()
    if path.suffix == ".age":  # a passphrase-protected backup of the identity file
        raw = _pw.decrypt(raw, passphrase if passphrase is not None else getpass.getpass("Identity passphrase: "))
    ids = [x25519.Identity.from_str(ln.strip()) for ln in raw.decode().splitlines() if ln.strip().startswith(_SECRET_PREFIX)]
    if not ids:
        raise SystemExit(f"no age secret key found in {path}")
    return ids


def check_key(identity_path: Path, recipients_file: Path, passphrase: str | None = None) -> dict[str, Any]:
    """Prove the key you hold is the one the ledger encrypts to: derive its public key, find it among the recipients, and round-trip a canary."""
    refuse_in_ci()
    idents = load_identities(identity_path, passphrase)
    recips, sha = load_recipients(recipients_file)
    pubs = [str(r) for r in recips]
    mine = [str(i.to_public()) for i in idents]
    matched = [m for m in mine if m in pubs]
    canary = os.urandom(32)
    ok = pyrage.decrypt(pyrage.encrypt(canary, recips), idents) == canary if matched else False
    return {"identity_matches_recipient": bool(matched), "canary_roundtrip": ok, "recipient_count": len(pubs), "recipients_sha256": sha,
            "warning": None if len(pubs) >= 2 else "only one recipient: if this one key is lost the ledger is unrecoverable; add a backup key"}


# ---- reading the ledger ------------------------------------------------------------------------------------------------------------------------------------

def decrypt_entry(root: Path, entry: dict[str, Any], identities: list[Any]) -> dict[str, Any]:
    pt = pyrage.decrypt(ct_path(root, entry["seq"]).read_bytes(), identities)
    obj = json.loads(pt.rstrip(b" "))
    ok = (obj.get("schema") == RECORD_SCHEMA and obj.get("seq") == entry["seq"] and obj.get("game_id") == entry["game_id"] and obj.get("version") == entry["version"])
    if not ok:
        raise SystemExit(f"entry {entry['seq']}: decrypted record does not match its manifest slot (ciphertexts swapped or forged)")
    return obj


def decrypt_canary(root: Path, identities: list[Any]) -> dict[str, Any]:
    entries = read_manifest(root)
    obj = json.loads(pyrage.decrypt(ct_path(root, 0).read_bytes(), identities).rstrip(b" "))
    if obj.get("kind") != "CANARY" or obj.get("ledger_id") != entries[0]["ledger_id"] or obj.get("seq") != 0:
        raise SystemExit("the canary does not match this ledger's genesis")
    return obj


def drill(root: Path, identity_paths: list[Path], recipients: Path | None = None, passphrases: list[str | None] | None = None) -> dict[str, Any]:
    """Recovery drill on the REAL published ciphertext, before any game exists: every identity you list must, on its own, open the genesis canary (a synthetic record
    sealed to all recipients). Proves each key (primary, backup, a restored copy) really opens this ledger. Decrypts nothing but the synthetic canary."""
    refuse_in_ci()
    rep = verify_store(root, recipients_sha256=load_recipients(recipients)[1] if recipients else None)
    if not rep.ok:
        raise SystemExit("ledger fails verification: " + "; ".join(rep.problems[:5]))
    out = []
    for i, p in enumerate(identity_paths):
        pw = passphrases[i] if passphrases else None
        try:
            decrypt_canary(root, load_identities(p, pw))
            out.append({"identity": str(p), "opens_this_ledger": True})
        except (pyrage.DecryptError, ValueError):
            out.append({"identity": str(p), "opens_this_ledger": False})
    return {"ledger_id": rep.ledger_id, "all_identities_open_the_ledger": all(x["opens_this_ledger"] for x in out), "results": out,
            "warning": None if len(identity_paths) >= 2 else "drill only one identity: a backup that was never tested is not a backup"}


def first_checkpoint(root: Path, identity_paths: list[Path], witness_dir: Path, recipients: Path, passphrase: str | None = None, identity_passphrases: list[str | None] | None = None) -> dict[str, Any]:
    """The owner's initial verification, to be done right after `init` and BEFORE any real game is sealed: structural verification against the committed recipients
    file, the recovery drill with every identity, then a signed WITNESS checkpoint of the initial head. Prints the genesis hash, the head hash and the recipients hash:
    write them down offline and compare them with the Actions run summary and the `sealed-ledger-head-0` tag. Refuses a ledger that holds anything beyond the genesis."""
    refuse_in_ci()
    entries = read_manifest(root)
    if len(entries) != 1:
        raise SystemExit(f"this ledger has {len(entries)} entries; first-checkpoint is only for the freshly initialised ledger (genesis only)")
    d = drill(root, identity_paths, recipients, identity_passphrases)
    if not d["all_identities_open_the_ledger"]:
        raise SystemExit("NOT witnessing: at least one identity cannot open the ledger's canary: " + json.dumps(d["results"]))
    cp = witness(root, witness_dir, passphrase, recipients)
    rep = verify_store(root)
    (Path(witness_dir).expanduser() / "state.json").write_text(json.dumps({"genesis_hash": genesis_hash(entries), "recipients_sha256": load_recipients(recipients)[1],
                                                                          "witness_log_head": cp["witness_log_head"]}))
    return {"genesis_hash": genesis_hash(entries), "head_seq": rep.head_seq, "head_hash": rep.head_hash, "ledger_id": rep.ledger_id,
            "recipients_sha256": load_recipients(recipients)[1], "witness_log_head": cp["witness_log_head"], "drill": d,
            "write_down": "genesis_hash, recipients_sha256 and witness_log_head, offline, and compare genesis_hash with the Actions run summary and the sealed-ledger-head-0 tag"}


def weekly_check(store: Path, witness_dir: Path, recipients: Path, *, ledger_url: str | None = None, passphrase: str | None = None, passphrase_cmd: str | None = None,
                 max_stale_days: int = 14) -> dict[str, Any]:
    """The owner's unattended routine (e.g. a weekly launchd job): fetch the public ledger (fast-forward only), verify it against everything you registered (genesis hash, the
    previous local copy, your witness log head, the recipients hash), and only then sign a new witness checkpoint. Exits non-zero (-> a macOS notification) on any problem, on a
    ledger that stopped growing, or on anything that is not a clean fast-forward. It decrypts nothing and never runs a look."""
    refuse_in_ci()
    store, wd = Path(store).expanduser(), Path(witness_dir).expanduser()
    state_p = wd / "state.json"
    if not state_p.exists():
        raise SystemExit("no state.json: run `first-checkpoint` once first")
    state = json.loads(state_p.read_text())
    prev = wd / "ledger_prev"
    if ledger_url:
        if not (store / ".git").exists():
            subprocess.run(["git", "clone", "-q", ledger_url, str(store)], check=True, capture_output=True)
        else:
            shutil.rmtree(prev, ignore_errors=True)
            shutil.copytree(store, prev, ignore=shutil.ignore_patterns(".git"))
            def git(*args: str) -> subprocess.CompletedProcess[str]:
                return subprocess.run(["git", "-C", str(store), *args], capture_output=True, text=True)

            if git("fetch", "-q", "origin").returncode != 0:
                return {"ok": False, "problems": ["cannot fetch the ledger repository (offline? deleted?)"], "witnessed": False}
            local_head, remote_head = git("rev-parse", "HEAD").stdout.strip(), git("rev-parse", "@{u}").stdout.strip()
            if local_head != remote_head:
                if git("merge-base", "--is-ancestor", local_head, remote_head).returncode == 0:
                    git("merge", "-q", "--ff-only", "@{u}")  # a clean fast-forward: the ledger grew
                elif git("merge-base", "--is-ancestor", remote_head, local_head).returncode == 0:
                    return {"ok": False, "witnessed": False, "problems": ["the ledger repository is BEHIND your last copy: it was rolled back or truncated (do NOT witness; keep your copies)"]}
                else:
                    return {"ok": False, "witnessed": False, "problems": ["the ledger repository DIVERGED from your last copy: history was rewritten or replaced (do NOT witness; keep your copies)"]}
    res = verify_all(store, wd, recipients, None, state.get("witness_log_head"), state.get("genesis_hash"))
    if prev.exists() and (prev / "manifest.jsonl").exists():
        res["problems"] += is_extension(read_manifest(prev), read_manifest(store))
    res["ok"] = not res["problems"]  # integrity only: a quiet ledger is NOT a reason to refuse to witness
    stale = res.get("days_since_latest_closed_date")
    res["attention"] = []
    in_season = datetime.now(UTC).month in (10, 11, 12, 1, 2, 3, 4)  # regular season only; the off-season is legitimately quiet
    if stale is not None and stale > max_stale_days and in_season:
        res["attention"].append(f"the ledger has not closed a day for {stale} days (normal during a long wait or a break; if it persists, collection may have stopped: scheduled "
                                "workflows are disabled after 60 days of repository inactivity)")
    res["witnessed"] = False
    if res["ok"]:
        pw = passphrase if passphrase is not None else passphrase_from_command(passphrase_cmd) if passphrase_cmd else None
        cp = witness(store, wd, pw, recipients)
        state["witness_log_head"] = cp["witness_log_head"]
        state_p.write_text(json.dumps(state))
        res["witnessed"] = True
        res["witness_log_head"] = cp["witness_log_head"]
    return res


def latest_rows(root: Path, identities: list[Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Latest version of every CLOSED game (one that a DAY entry accounts for), in first-seal order (= the ledger's chronological order)."""
    entries = read_manifest(root)
    order = closed_games(entries)
    latest: dict[str, dict[str, Any]] = {}
    corrections: list[dict[str, Any]] = []
    for e in entries:
        if e["kind"] != "RECORD":
            continue
        if e["version"] > 1:
            corrections.append({"game_id": e["game_id"], "version": e["version"], "reason": e["reason"], "seq": e["seq"]})
        latest[e["game_id"]] = e
    rows = [decrypt_entry(root, latest[g], identities)["record"] for g in order]
    return rows, {"n_games": len(order), "corrections": corrections}


def reproduce_diff(root: Path, identities: list[Any], archive: Path, repo: Path, tol: float = 1e-9) -> list[str]:
    """Origin check for the CONTENT of the ledger (encryption alone cannot give it: anyone holding the public key can seal a forged record). For every date that has
    a sealed record or a DAY entry, re-derive the rows from an archive checkout you trust and compare them with the decrypted LATEST version of each game; also flag
    sealed ids the archive cannot derive and derivable games that were never sealed. Reports ``game_id: field`` names only, never values, so a report is safe to
    share. Needs the real archive; run it locally before relying on a look."""
    refuse_in_ci()
    entries = read_manifest(root)
    latest: dict[str, dict[str, Any]] = {}
    for e in entries:
        if e["kind"] == "RECORD":
            latest[e["game_id"]] = e
    out: list[str] = []
    for day in sorted({e["game_date_et"] for e in entries if e["kind"] in ("RECORD", "DAY")}):
        rows, _info = daily.build_rows(archive, day, repo)
        derived = {str(r["game_id"]): r for r in rows}
        sealed_ids = {g for g, e in latest.items() if e["game_date_et"] == day}
        out += [f"{g}: sealed for {day} but not derivable from the archive (extra or forged id)" for g in sorted(sealed_ids - set(derived))]
        out += [f"{g}: derivable from the archive but NOT in the ledger (omitted)" for g in sorted(set(derived) - sealed_ids)]
        for gid in sorted(sealed_ids & set(derived)):
            sealed = decrypt_entry(root, latest[gid], identities)["record"]
            for k in sorted(set(derived[gid]) | set(sealed)):
                a, b = derived[gid].get(k), sealed.get(k)
                same = (abs(a - b) <= tol) if isinstance(a, float) and isinstance(b, float) else a == b
                if not same:
                    out.append(f"{gid}: field {k} differs (version {latest[gid]['version']})")
    return out


def witness_status(root: Path, witness_dir: Path) -> tuple[list[dict[str, Any]], list[str]]:
    pub_p = Path(witness_dir).expanduser() / "witness_public.pem"
    if not pub_p.exists():
        return [], [f"no witness key in {witness_dir}"]
    signed, probs = CP.witness_read(Path(witness_dir).expanduser() / "witness.jsonl", CP.load_public(pub_p.read_bytes()))
    return signed, probs + CP.check_store(root, signed)


def witness_log_head(witness_dir: Path) -> tuple[int, str]:
    log = Path(witness_dir).expanduser() / "witness.jsonl"
    lines = [json.loads(x) for x in log.read_text().splitlines() if x.strip()] if log.exists() else []
    return len(lines), (lines[-1]["line_hash"] if lines else "")


def verify_all(root: Path, witness_dir: Path | None, recipients: Path | None, attest_pub: Path | None, expect_witness_head: str | None = None,
               expect_genesis: str | None = None) -> dict[str, Any]:
    refuse_in_ci()
    rep = verify_store(root, recipients_sha256=load_recipients(recipients)[1] if recipients else None)
    probs = list(rep.problems)
    if expect_genesis is not None and genesis_hash(read_manifest(root)) != expect_genesis:
        probs.append("the genesis hash differs from the one you registered: this is a different (replaced or recreated) ledger")
    n_witness = 0
    if witness_dir is not None:
        signed, wp = witness_status(root, witness_dir)
        probs += wp
        n_witness = len(signed)
        if expect_witness_head is not None and witness_log_head(witness_dir)[1] != expect_witness_head:
            probs.append("the witness log head differs from the value you recorded elsewhere: lines were removed from (or added to) your local log")
    if attest_pub is not None and (root / CHECKPOINT_DIR).exists():
        pub = CP.load_public(Path(attest_pub).read_bytes())
        good = []
        for f in sorted((root / CHECKPOINT_DIR).glob("runner_*.json")):
            try:
                s = json.loads(f.read_text())
                if CP.verify_signature(s, pub):
                    good.append(s)
                else:
                    probs.append(f"{f.name}: bad signature")
            except (ValueError, KeyError, TypeError):
                probs.append(f"{f.name}: malformed runner checkpoint")
        probs += CP.check_against_checkpoints(read_manifest(root), good)
    days = sorted(e["game_date_et"] for e in read_manifest(root) if e.get("kind") == "DAY")
    stale_days = None
    if days:
        stale_days = (datetime.now(UTC).date() - datetime.fromisoformat(days[-1]).date()).days
    return {**rep.summary(), "problems": probs, "ok": not probs, "witness_checkpoints": n_witness, "warnings": rep.warnings, "latest_closed_date": days[-1] if days else None,
            "days_since_latest_closed_date": stale_days}


def passphrase_from_command(cmd: str) -> str:
    """Run a local command that prints the passphrase (e.g. ``security find-generic-password -s sift-witness -w`` on macOS) so a scheduled check needs no typing. The
    command is the owner's, runs only on the owner's machine, and its output is never printed."""
    out = subprocess.run(shlex.split(cmd), capture_output=True, text=True, check=True).stdout.strip()
    if len(out) < 8:
        raise SystemExit("the passphrase command returned no usable passphrase")
    return out


def witness(root: Path, witness_dir: Path, passphrase: str | None = None, recipients: Path | None = None) -> dict[str, Any]:
    """Verify the public ledger, then record a signed checkpoint of its head in YOUR local witness log. Do this regularly (e.g. weekly).
    Pass ``recipients`` (the committed file) so that a replacement ledger encrypted to someone else's key cannot be witnessed."""
    refuse_in_ci()
    wd = Path(witness_dir).expanduser()
    res = verify_all(root, wd, recipients, None)
    if not res["ok"]:
        raise SystemExit("not witnessing a ledger that fails verification: " + "; ".join(res["problems"][:5]))
    key = CP.load_private((wd / "witness_private.pem").read_bytes(), (passphrase if passphrase is not None else getpass.getpass("Witness key passphrase: ")).encode())
    signed = CP.sign(CP.make_checkpoint(read_manifest(root), "WITNESS"), key)
    line = CP.witness_append(wd / "witness.jsonl", signed)
    state_p = wd / "state.json"
    if state_p.exists():  # a manual `witness` must not make the next weekly-check fail: keep the recorded log head current
        state = json.loads(state_p.read_text())
        state["witness_log_head"] = line["line_hash"]
        state_p.write_text(json.dumps(state))
    return {**signed["checkpoint"], "witness_entries": line["seq"] + 1, "witness_log_head": line["line_hash"],
            "note": "write witness_log_head down somewhere OTHER than this folder; `verify --expect-witness-head` uses it to detect a truncated log"}


def witness_keygen(witness_dir: Path, passphrase: str | None = None) -> str:
    refuse_in_ci()
    wd = Path(witness_dir).expanduser()
    if (wd / "witness_private.pem").exists():
        raise SystemExit("witness key already exists")
    pw = passphrase if passphrase is not None else getpass.getpass("New witness key passphrase (>= 8 characters): ")
    if len(pw) < 8:
        raise SystemExit("passphrase must be at least 8 characters (an empty one would leave the key unencrypted)")
    wd.mkdir(parents=True, exist_ok=True, mode=0o700)
    key = CP.generate_key()
    fd = os.open(wd / "witness_private.pem", os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as fh:
        fh.write(CP.private_pem(key, pw.encode()))
    (wd / "witness_public.pem").write_bytes(CP.public_pem(key))
    return CP.public_pem(key).decode()


def _looks_taken(root_ledger_id: str, witness_dir: Path | None, out: Path) -> set[int]:
    taken = {k for k in daily.LOOKS if (out / f"LOOK_{k}.json").exists()}
    if witness_dir is not None:
        m = Path(witness_dir).expanduser() / "looks_taken.json"
        if m.exists():
            taken |= set(json.loads(m.read_text()).get(root_ledger_id, []))
    return taken


def take_look(root: Path, identity_path: Path, witness_dir: Path | None, out: Path, passphrase: str | None = None, *, allow_unwitnessed: bool = False,
              recipients: Path | None = None) -> dict[str, Any]:
    """The preregistered looks. Order matters: nothing is decrypted until every check that needs no key has passed. Each look (150, 300, 450) is taken once per ledger:
    a marker in the witness directory (and the LOOK file itself) refuses a repeat even with a different ``--out``. The look taken is the SMALLEST untaken level the
    closed-game count has reached, evaluated on exactly the first k games, so a late first look still reports the preregistered 150-game look."""
    refuse_in_ci()
    rep = verify_store(root, recipients_sha256=load_recipients(recipients)[1] if recipients else None)
    if not rep.ok:
        raise SystemExit("ledger fails verification; not decrypting: " + "; ".join(rep.problems[:5]))
    if rep.n_games_closed < daily.LOOKS[0]:
        raise SystemExit(f"only {rep.n_games_closed} closed-day games sealed; the first look is at {daily.LOOKS[0]}. Nothing was decrypted (the blinding is the point).")
    if witness_dir is not None:
        signed, wp = witness_status(root, witness_dir)
        if wp:
            raise SystemExit("witness check failed (rollback / truncation / replacement?): " + "; ".join(wp[:5]))
        if not signed and not allow_unwitnessed:
            raise SystemExit("your witness log is empty: run `witness` first, or pass --allow-unwitnessed to accept that rollback cannot be ruled out")
    elif not allow_unwitnessed:
        raise SystemExit("--dir (witness) is required, or pass --allow-unwitnessed")
    out = Path(out).expanduser()
    taken = _looks_taken(rep.ledger_id, witness_dir, out)
    todo = [x for x in daily.LOOKS if rep.n_games_closed >= x and x not in taken]
    if not todo:
        raise SystemExit(f"every look reached so far ({sorted(taken)}) was already taken for this ledger: a look is taken once and never repeated")
    k = todo[0]
    out.mkdir(parents=True, exist_ok=True)
    rows, meta = latest_rows(root, load_identities(identity_path, passphrase))
    sc = daily.scorecard(rows[:k], out)  # the frozen scoring code, unchanged, on exactly the first k games: writes LOOK_k.json exactly once
    prov = {"look": k, "ledger_id": rep.ledger_id, "head_seq": rep.head_seq, "head_hash": rep.head_hash, "n_games_closed_at_look": rep.n_games_closed,
            "corrections_in_ledger": meta["corrections"], "taken_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")}
    (out / f"LOOK_{k}.provenance.json").write_text(json.dumps(prov, indent=1))
    if witness_dir is not None:
        m = Path(witness_dir).expanduser() / "looks_taken.json"
        d = json.loads(m.read_text()) if m.exists() else {}
        d.setdefault(rep.ledger_id, []).append(k)
        m.write_text(json.dumps(d))
    return {"status": sc["status"], "look_file": str(out / f"LOOK_{k}.json"), "provenance": prov}


def main(argv: list[str] | None = None) -> int:
    refuse_in_ci()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("keygen")
    s.add_argument("--identity", type=Path, required=True)
    s = sub.add_parser("check-key")
    s.add_argument("--identity", type=Path, required=True)
    s.add_argument("--recipients", type=Path, required=True)
    s = sub.add_parser("witness-keygen")
    s.add_argument("--dir", type=Path, required=True)
    s = sub.add_parser("witness")
    s.add_argument("--store", type=Path, required=True)
    s.add_argument("--dir", type=Path, required=True)
    s.add_argument("--recipients", type=Path, required=True)
    s = sub.add_parser("weekly-check")
    s.add_argument("--store", type=Path, required=True, help="your local clone of the ledger repository")
    s.add_argument("--dir", type=Path, required=True)
    s.add_argument("--recipients", type=Path, required=True)
    s.add_argument("--ledger-url", help="clone/pull this URL first (https://github.com/<owner>/<ledger repo>.git)")
    s.add_argument("--passphrase-cmd", help="command that prints the witness-key passphrase, e.g. 'security find-generic-password -s sift-witness -w'")
    s.add_argument("--max-stale-days", type=int, default=14)
    s = sub.add_parser("verify")
    s.add_argument("--store", type=Path, required=True)
    s.add_argument("--dir", type=Path)
    s.add_argument("--recipients", type=Path)
    s.add_argument("--attest-pub", type=Path)
    s.add_argument("--previous", type=Path, help="an earlier copy of the store (e.g. from your last visit); the current one must extend it")
    s.add_argument("--expect-witness-head", help="the witness_log_head you recorded elsewhere at your last `witness`")
    s.add_argument("--expect-genesis", help="the genesis_hash you wrote down at first-checkpoint")
    s = sub.add_parser("drill")
    s.add_argument("--store", type=Path, required=True)
    s.add_argument("--identity", type=Path, action="append", required=True, help="repeat for primary, backup and any restored copy")
    s.add_argument("--recipients", type=Path, required=True)
    s = sub.add_parser("first-checkpoint")
    s.add_argument("--store", type=Path, required=True)
    s.add_argument("--identity", type=Path, action="append", required=True)
    s.add_argument("--dir", type=Path, required=True)
    s.add_argument("--recipients", type=Path, required=True)
    s = sub.add_parser("reproduce")
    s.add_argument("--store", type=Path, required=True)
    s.add_argument("--identity", type=Path, required=True)
    s.add_argument("--archive", type=Path, required=True)
    s.add_argument("--repo", type=Path, default=Path("."))
    s = sub.add_parser("look")
    s.add_argument("--store", type=Path, required=True)
    s.add_argument("--identity", type=Path, required=True)
    s.add_argument("--recipients", type=Path, required=True)
    s.add_argument("--dir", type=Path)
    s.add_argument("--out", type=Path, required=True)
    s.add_argument("--allow-unwitnessed", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "keygen":
        print("PUBLIC KEY (safe to share and to commit):", generate_identity(a.identity))
        print(f"private key written to {a.identity} (mode 0600). Back it up now (see SEALED_LEDGER_KEY_SETUP.md). Never paste it anywhere.")
    elif a.cmd == "check-key":
        print(json.dumps(check_key(a.identity, a.recipients), indent=1))
    elif a.cmd == "witness-keygen":
        print(witness_keygen(a.dir))
    elif a.cmd == "witness":
        print(json.dumps(witness(a.store, a.dir, recipients=a.recipients), indent=1))
    elif a.cmd == "weekly-check":
        res = weekly_check(a.store, a.dir, a.recipients, ledger_url=a.ledger_url, passphrase_cmd=a.passphrase_cmd, max_stale_days=a.max_stale_days)
        print(json.dumps(res, indent=1))
        return 1 if not res["ok"] else 2 if res.get("attention") else 0  # 1 = integrity problem (do not witness), 2 = verified and witnessed but needs attention
    elif a.cmd == "verify":
        res = verify_all(a.store, a.dir, a.recipients, a.attest_pub, a.expect_witness_head, a.expect_genesis)
        if a.previous:
            if not a.previous.is_dir():
                res["problems"].append(f"--previous {a.previous} is not a directory")
            else:
                res["problems"] += is_extension(read_manifest(a.previous), read_manifest(a.store))
            res["ok"] = not res["problems"]
        print(json.dumps(res, indent=1))
        return 0 if res["ok"] else 1
    elif a.cmd == "drill":
        res = drill(a.store, a.identity, a.recipients)
        print(json.dumps(res, indent=1))
        return 0 if res["all_identities_open_the_ledger"] else 1
    elif a.cmd == "first-checkpoint":
        print(json.dumps(first_checkpoint(a.store, a.identity, a.dir, a.recipients), indent=1))
    elif a.cmd == "reproduce":
        diffs = reproduce_diff(a.store, load_identities(a.identity), a.archive, a.repo)
        print(json.dumps({"mismatches": diffs, "ok": not diffs}, indent=1))
        return 0 if not diffs else 1
    else:
        print(json.dumps(take_look(a.store, a.identity, a.dir, a.out, allow_unwitnessed=a.allow_unwitnessed, recipients=a.recipients), indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SealError as e:
        print(f"REFUSED: {e}", file=sys.stderr)
        sys.exit(3)
