"""OWNER-LOCAL tool for the sealed prospective ledger. The ONLY module that can decrypt. Run it on your own machine, never in CI, never from a development session.

    python -m nhl_edge.sealed_ledger.owner keygen         --identity ~/sift-ledger/identity.txt          # prints ONLY the public key
    python -m nhl_edge.sealed_ledger.owner check-key      --identity ~/sift-ledger/identity.txt --recipients <repo>/research/sealed_ledger/recipients.txt
    python -m nhl_edge.sealed_ledger.owner witness-keygen --dir ~/sift-ledger/witness
    python -m nhl_edge.sealed_ledger.owner witness        --store <ledger checkout> --dir ~/sift-ledger/witness
    python -m nhl_edge.sealed_ledger.owner verify         --store <ledger checkout> --dir ~/sift-ledger/witness [--recipients ...] [--attest-pub runner_public.pem]
    python -m nhl_edge.sealed_ledger.owner reproduce      --store <ledger checkout> --identity ~/sift-ledger/identity.txt --archive <data-archive checkout> --repo .
    python -m nhl_edge.sealed_ledger.owner look           --store <ledger checkout> --identity ~/sift-ledger/identity.txt --dir ~/sift-ledger/witness --out ~/sift-ledger/looks

``look`` refuses to decrypt anything before the preregistered 150 distinct games exist, refuses to run twice for the same look, and verifies the whole store (chain,
ciphertext hashes, witness checkpoints) before it touches a key. It never prints a record. The private key is read from a file path you give; it is never taken from
an environment variable, an argument or a prompt-echo, and never leaves this process. Under CI (``GITHUB_ACTIONS``/``CI``) every command refuses to run.
"""

from __future__ import annotations

import argparse
import getpass
import json
import os
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
from nhl_edge.sealed_ledger.core import CHECKPOINT_DIR, ct_path, is_extension, read_manifest, verify_store
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


def latest_rows(root: Path, identities: list[Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Latest version of every game, in first-seal order (= the ledger's chronological order)."""
    entries = read_manifest(root)
    order: list[str] = []
    latest: dict[str, dict[str, Any]] = {}
    corrections: list[dict[str, Any]] = []
    for e in entries:
        if e["kind"] != "RECORD":
            continue
        if e["version"] == 1:
            order.append(e["game_id"])
        else:
            corrections.append({"game_id": e["game_id"], "version": e["version"], "reason": e["reason"], "seq": e["seq"]})
        latest[e["game_id"]] = e
    rows = [decrypt_entry(root, latest[g], identities)["record"] for g in order]
    return rows, {"n_games": len(order), "corrections": corrections}


def reproduce_diff(root: Path, identities: list[Any], archive: Path, repo: Path, tol: float = 1e-9) -> list[str]:
    """Origin check for the CONTENT of the ledger (encryption alone cannot give it: anyone holding the public key can seal a forged record). For every day the ledger
    closed, re-derive the rows from an archive checkout you trust and compare with the decrypted FIRST version of each record. Prints/returns mismatches only as
    ``game_id: field`` names, never values, so a mismatch report is safe to share. Needs the real archive; run it locally, once, before relying on a look."""
    refuse_in_ci()
    entries = read_manifest(root)
    first = {e["game_id"]: e for e in entries if e["kind"] == "RECORD" and e["version"] == 1}
    out: list[str] = []
    for day in sorted({e["game_date_et"] for e in entries if e["kind"] == "DAY"}):
        rows, _info = daily.build_rows(archive, day, repo)
        for r in rows:
            e = first.get(str(r["game_id"]))
            if e is None:
                out.append(f"{r['game_id']}: derivable from the archive but NOT in the ledger (omitted)")
                continue
            sealed = decrypt_entry(root, e, identities)["record"]
            for k in sorted(set(r) | set(sealed)):
                a, b = r.get(k), sealed.get(k)
                same = (abs(a - b) <= tol) if isinstance(a, float) and isinstance(b, float) else a == b
                if not same:
                    out.append(f"{r['game_id']}: field {k} differs")
    return out


def witness_status(root: Path, witness_dir: Path) -> tuple[list[dict[str, Any]], list[str]]:
    pub_p = Path(witness_dir).expanduser() / "witness_public.pem"
    if not pub_p.exists():
        return [], [f"no witness key in {witness_dir}"]
    signed, probs = CP.witness_read(Path(witness_dir).expanduser() / "witness.jsonl", CP.load_public(pub_p.read_bytes()))
    return signed, probs + CP.check_store(root, signed)


def verify_all(root: Path, witness_dir: Path | None, recipients: Path | None, attest_pub: Path | None) -> dict[str, Any]:
    refuse_in_ci()
    rep = verify_store(root, recipients_sha256=load_recipients(recipients)[1] if recipients else None)
    probs = list(rep.problems)
    n_witness = 0
    if witness_dir is not None:
        signed, wp = witness_status(root, witness_dir)
        probs += wp
        n_witness = len(signed)
    if attest_pub is not None and (root / CHECKPOINT_DIR).exists():
        pub = CP.load_public(Path(attest_pub).read_bytes())
        runner = [json.loads(p.read_text()) for p in sorted((root / CHECKPOINT_DIR).glob("runner_*.json"))]
        for s in runner:
            if not CP.verify_signature(s, pub):
                probs.append(f"runner checkpoint at seq {s['checkpoint']['seq']}: bad signature")
        probs += CP.check_against_checkpoints(read_manifest(root), [s for s in runner if CP.verify_signature(s, pub)])
    return {**rep.summary(), "problems": probs, "ok": not probs, "witness_checkpoints": n_witness, "warnings": rep.warnings}


def witness(root: Path, witness_dir: Path, passphrase: str | None = None) -> dict[str, Any]:
    """Verify the public ledger, then record a signed checkpoint of its head in YOUR local witness log. Do this regularly (e.g. weekly)."""
    refuse_in_ci()
    wd = Path(witness_dir).expanduser()
    res = verify_all(root, wd, None, None)
    if not res["ok"]:
        raise SystemExit("not witnessing a ledger that fails verification: " + "; ".join(res["problems"][:5]))
    key = CP.load_private((wd / "witness_private.pem").read_bytes(), (passphrase if passphrase is not None else getpass.getpass("Witness key passphrase: ")).encode())
    signed = CP.sign(CP.make_checkpoint(read_manifest(root), "WITNESS"), key)
    CP.witness_append(wd / "witness.jsonl", signed)
    return signed["checkpoint"]


def witness_keygen(witness_dir: Path, passphrase: str | None = None) -> str:
    refuse_in_ci()
    wd = Path(witness_dir).expanduser()
    if (wd / "witness_private.pem").exists():
        raise SystemExit("witness key already exists")
    pw = passphrase if passphrase is not None else getpass.getpass("New witness key passphrase: ")
    wd.mkdir(parents=True, exist_ok=True, mode=0o700)
    key = CP.generate_key()
    fd = os.open(wd / "witness_private.pem", os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as fh:
        fh.write(CP.private_pem(key, pw.encode()))
    (wd / "witness_public.pem").write_bytes(CP.public_pem(key))
    return CP.public_pem(key).decode()


def take_look(root: Path, identity_path: Path, witness_dir: Path | None, out: Path, passphrase: str | None = None, *, allow_unwitnessed: bool = False) -> dict[str, Any]:
    """The single preregistered look. Order matters: nothing is decrypted until every check that needs no key has passed."""
    refuse_in_ci()
    rep = verify_store(root)
    if not rep.ok:
        raise SystemExit("ledger fails verification; not decrypting: " + "; ".join(rep.problems[:5]))
    if rep.n_games < daily.LOOKS[0]:
        raise SystemExit(f"only {rep.n_games} distinct games sealed; the first look is at {daily.LOOKS[0]}. Nothing was decrypted (the blinding is the point).")
    if witness_dir is not None:
        signed, wp = witness_status(root, witness_dir)
        if wp:
            raise SystemExit("witness check failed (rollback / truncation / replacement?): " + "; ".join(wp[:5]))
        if not signed and not allow_unwitnessed:
            raise SystemExit("your witness log is empty: run `witness` first, or pass --allow-unwitnessed to accept that rollback cannot be ruled out")
    elif not allow_unwitnessed:
        raise SystemExit("--dir (witness) is required, or pass --allow-unwitnessed")
    k = max(x for x in daily.LOOKS if rep.n_games >= x)
    out = Path(out).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    if (out / f"LOOK_{k}.json").exists():
        raise SystemExit(f"LOOK_{k}.json already exists in {out}: a look is taken once and never overwritten")
    rows, meta = latest_rows(root, load_identities(identity_path, passphrase))
    sc = daily.scorecard(rows, out)  # the frozen scoring code, unchanged: writes LOOK_k.json exactly once
    prov = {"look": k, "ledger_id": rep.ledger_id, "head_seq": rep.head_seq, "head_hash": rep.head_hash, "n_games_sealed_at_look": rep.n_games,
            "corrections_in_ledger": meta["corrections"], "taken_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")}
    (out / f"LOOK_{k}.provenance.json").write_text(json.dumps(prov, indent=1))
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
    s = sub.add_parser("verify")
    s.add_argument("--store", type=Path, required=True)
    s.add_argument("--dir", type=Path)
    s.add_argument("--recipients", type=Path)
    s.add_argument("--attest-pub", type=Path)
    s.add_argument("--previous", type=Path, help="an earlier copy of the store (e.g. from your last visit); the current one must extend it")
    s = sub.add_parser("reproduce")
    s.add_argument("--store", type=Path, required=True)
    s.add_argument("--identity", type=Path, required=True)
    s.add_argument("--archive", type=Path, required=True)
    s.add_argument("--repo", type=Path, default=Path("."))
    s = sub.add_parser("look")
    s.add_argument("--store", type=Path, required=True)
    s.add_argument("--identity", type=Path, required=True)
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
        print(json.dumps(witness(a.store, a.dir), indent=1))
    elif a.cmd == "verify":
        res = verify_all(a.store, a.dir, a.recipients, a.attest_pub)
        if a.previous:
            res["problems"] += is_extension(read_manifest(a.previous), read_manifest(a.store))
            res["ok"] = not res["problems"]
        print(json.dumps(res, indent=1))
        return 0 if res["ok"] else 1
    elif a.cmd == "reproduce":
        diffs = reproduce_diff(a.store, load_identities(a.identity), a.archive, a.repo)
        print(json.dumps({"mismatches": diffs, "ok": not diffs}, indent=1))
        return 0 if not diffs else 1
    else:
        print(json.dumps(take_look(a.store, a.identity, a.dir, a.out, allow_unwitnessed=a.allow_unwitnessed), indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SealError as e:
        print(f"REFUSED: {e}", file=sys.stderr)
        sys.exit(3)
