"""Workflow-side CLI of the sealed prospective ledger. Encrypt-only: it imports ``seal``/``core``/``checkpoint`` and NEVER ``owner`` (no decryption path exists here).

    python -m nhl_edge.sealed_ledger.runner reconcile --archive A --repo . --store S --recipients R --through D [--dry-run] [--summary-out F]   # the unattended daily pass
    python -m nhl_edge.sealed_ledger.runner init      --store S --recipients R [--summary-out F]            # creates GENESIS + a synthetic canary; no game
    python -m nhl_edge.sealed_ledger.runner ingest    --archive A --date D --repo . --store S --recipients R [--seal] [--correct IDS --reason CODE | --exclude IDS --exclude-reason CODE | --accept-missing-forecasts] [--summary-out F]
    python -m nhl_edge.sealed_ledger.runner scorecard --store S --out DIR
    python -m nhl_edge.sealed_ledger.runner verify    --store S [--recipients R] [--previous PREV_STORE]
    python -m nhl_edge.sealed_ledger.runner attest    --store S [--out F]       # optional RUNNER signature, key from $LEDGER_ATTEST_KEY_PEM

Without ``--seal`` the ingest is a DRY RUN: rows are derived in memory, validated, counted and discarded. Whatever the mode, stdout, the summary file and the scorecard
contain only outcome-free metadata: counts, ids of scheduled games, data-quality and integrity flags.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from statistics import fmean
from typing import Any

from nhl_edge.sealed_ledger import PROTOCOL_RULES
from nhl_edge.sealed_ledger.core import closed_games, genesis_hash, is_extension, read_manifest, verify_store
from nhl_edge.sealed_ledger.seal import SealedStore, SealError, load_recipients

LOOKS = tuple(PROTOCOL_RULES["looks_games"])  # the frozen 150 / 300 / 450 (a test pins equality with daily.LOOKS)
_ID = re.compile(r"^[0-9A-Za-z_-]{1,40}$")


def blinded_scorecard(entries: list[dict[str, Any]]) -> dict[str, Any]:
    """The blinded scorecard computed from the PUBLIC manifest alone, over games a DAY entry accounts for. It carries the same keys as the document ``daily.scorecard`` prints before the first look (``mean_slate_age_min`` is computed from values rounded to 3 decimals). At >= 150 games the
    runner does NOT compute a look (it cannot: it has no key); it reports that the owner's look is due."""
    closed = set(closed_games(entries))
    first = {e["game_id"]: e for e in entries if e["kind"] == "RECORD" and e["version"] == 1 and e["game_id"] in closed}
    n = len(first)
    sc: dict[str, Any] = {"n_prospective_games": n, "tier": "PROSPECTIVE", "looks": list(LOOKS)}
    sc["next_look_at_games"] = next((k for k in LOOKS if k > n), None)
    ages = [e["pregame"]["slate_age_min"] for e in first.values() if e["pregame"]["slate_age_min"] is not None]
    miss = sum(1 for e in first.values() if not e["pregame"]["sb_present"]) / n if n else None
    sc["data_quality"] = {"missing_sportsbook_share": miss, "mean_slate_age_min": float(fmean(ages)) if n and ages else None}
    sc["alarms"] = ["WARN: more than 20% of games lack a sportsbook consensus"] if n and miss is not None and miss > 0.2 else []
    reached = [k for k in LOOKS if n >= k]
    if not reached:
        sc["status"] = "ACCUMULATING_BLINDED"
        sc["note"] = "Outcome-derived and model-vs-market measures on the prospective tier are withheld until the first predeclared look (150 games)."
    else:
        sc["status"] = f"LOOK_{max(reached)}_DUE_OWNER_LOCAL"
        sc["note"] = "The preregistered threshold is reached. The look is computed only by the owner, locally, with the private key (owner.py look); the runner never decrypts."
    return sc


def _corrections(s: str | None) -> dict[str, int]:
    """``GAME_ID@VERSION,...``: VERSION is the version currently sealed (the one being superseded)."""
    out: dict[str, int] = {}
    for x in (t.strip() for t in (s or "").split(",") if t.strip()):
        m = re.fullmatch(r"([0-9A-Za-z_-]{1,40})@([1-9][0-9]{0,2})", x)
        if not m:
            raise SystemExit(f"invalid correction {x!r}: use GAME_ID@CURRENT_VERSION")
        out[m.group(1)] = int(m.group(2))
    return out


def _id_list(s: str | None) -> set[str]:
    out = {x.strip() for x in (s or "").split(",") if x.strip()}
    bad = [x for x in out if not re.fullmatch(r"[0-9A-Za-z_-]{1,40}", x)]
    if bad:
        raise SystemExit(f"invalid game id(s): {bad}")
    return out


def run_ingest(archive: Path, date: str, repo: Path, store: Path, recipients: Path, *, seal: bool, correct: dict[str, int], reason: str | None,
               run_id: str = "", code_sha: str = "", exclude: set[str] | None = None, exclude_reason: str | None = None, accept_no_forecast: bool = False) -> dict[str, Any]:
    from nhl_edge.model_research import daily  # heavy imports only on the ingest path

    exclude = set(exclude or ())
    rows, info = daily.build_rows(archive, date, repo)
    out: dict[str, Any] = {"date": date, "mode": "SEAL" if seal else "DRY_RUN", "games_scheduled": info["games_scheduled"], "games_final": info["games_final"],
                           "games_with_pregame_forecast": info["games_with_pregame_forecast"], "missing_pregame_forecast": info["missing_pregame_forecast"],
                           "reproduction_max_abs_diff": info["reproduction_max_abs_diff"], "all_scheduled_final": info["all_scheduled_final"]}
    if not seal:
        out.update({"sealed_new": 0, "skipped_existing": 0, "corrections": 0, "day_closed": False, "note": "dry run: nothing was sealed or written"})
        return out
    st = SealedStore(store, recipients, run_id=run_id, code_sha=code_sha, create=False)  # a ledger is only ever created by `init`, which the owner verifies first
    from nhl_edge.market_audit.games import build_games, read_kind
    from nhl_edge.sealed_ledger import audit
    from nhl_edge.sealed_ledger.core import EXCLUSION_REASONS

    # fail closed: no day may be skipped, left incomplete, drifted or revised, and no orphan result may exist, before a later day is sealed
    results = read_kind(archive, "results")
    gaps = audit.open_days_before(archive, date, store, results=results, ignore_revised=bool(correct))
    if gaps:
        raise SealError(f"refusing to seal {date}: earlier day(s) are not cleanly closed: " + "; ".join(gaps[:5]))
    if exclude:  # an owner decision, public and reason-coded: only a game that did not finish (or a genuine boundary game) may be waived, never a finished game
        if exclude_reason not in EXCLUSION_REASONS:
            raise SealError(f"an exclusion needs a reason code from {EXCLUSION_REASONS}")
        if correct:
            raise SealError("exclusions and corrections are separate runs")
        if not exclude <= set(info["scheduled_game_ids"]):
            raise SealError(f"excluded game(s) are not scheduled on {date}: {sorted(exclude - set(info['scheduled_game_ids']))}")
        finished = exclude & set(info["final_game_ids"])
        if finished and (exclude_reason != "START_TIME_BOUNDARY" or not finished <= audit.boundary_games(build_games(archive))):
            raise SealError(f"cannot exclude finished game(s) {sorted(finished)} (only an unfinished game, or a genuine start-time boundary game with reason START_TIME_BOUNDARY)")
        rows = [r for r in rows if str(r["game_id"]) not in exclude]
    out["excluded_game_ids"] = sorted(exclude)
    out.update(st.seal_rows(rows, correct=correct, reason=reason, source_asof=audit.results_asof(results)))
    # never close a day whose every game lacks a pregame forecast: that is the signature of an incomplete archive fetch, and a DAY entry cannot be undone
    suspicious = bool(info["scheduled_game_ids"]) and info["games_with_pregame_forecast"] == 0 and not accept_no_forecast  # the owner may accept a whole day without forecasts (admin)
    complete = bool(info["scheduled_game_ids"]) and set(info["scheduled_game_ids"]) <= set(info["final_game_ids"]) | exclude
    out["day_closed"] = bool(complete and not suspicious and st.close_day(date, info["scheduled_game_ids"], info["missing_pregame_forecast"], sorted(exclude), exclude_reason))
    if suspicious:
        out["note"] = "day NOT closed: no scheduled game has a pregame forecast (check the archive fetch)"
    rep = verify_store(store, recipients_sha256=load_recipients(recipients)[1])
    out["integrity_ok"] = rep.ok
    out["manifest_entries"], out["head_seq"], out["head_hash"] = rep.n_entries, rep.head_seq, rep.head_hash
    if not rep.ok:
        raise SealError("store failed verification after sealing: " + "; ".join(rep.problems[:5]))
    return out


def run_init(store: Path, recipients: Path, *, run_id: str = "", code_sha: str = "") -> dict[str, Any]:
    """Create the ledger: GENESIS (recipients hash, frozen-protocol hash) + a SYNTHETIC canary ciphertext. Refuses if a ledger already exists. Seals no game."""
    if (store / "manifest.jsonl").exists():
        raise SealError("a ledger already exists at this location; init refuses to touch it")
    st = SealedStore(store, recipients, run_id=run_id, code_sha=code_sha, create=True)
    rep = verify_store(store, recipients_sha256=st.recipients_sha256)
    if not rep.ok:
        raise SealError("fresh ledger failed verification: " + "; ".join(rep.problems[:5]))
    return {"date": "n/a", "mode": "INIT", "initialised": True, "ledger_id": st.ledger_id, "genesis_hash": genesis_hash(st.entries), "recipients_sha256": st.recipients_sha256,
            "recipient_count": len(st.recips), "manifest_entries": rep.n_entries, "head_seq": rep.head_seq, "head_hash": rep.head_hash, "integrity_ok": True,
            "note": "owner: verify and register this genesis hash (SEALED_LEDGER_OWNER_CHECKLIST.md) BEFORE any game is sealed"}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("ingest")
    a.add_argument("--archive", type=Path, required=True)
    a.add_argument("--date", required=True)
    a.add_argument("--repo", type=Path, default=Path("."))
    a.add_argument("--store", type=Path, required=True)
    a.add_argument("--recipients", type=Path, required=True)
    a.add_argument("--seal", action="store_true", help="seal into --store (default: dry run, nothing written)")
    a.add_argument("--correct", help="comma-separated GAME_ID@CURRENT_VERSION whose sealed record is to be superseded by a versioned correction")
    a.add_argument("--reason", help="correction reason code")
    a.add_argument("--exclude", help="comma-separated game ids waived from this day because they never finished (owner decision; needs --exclude-reason)")
    a.add_argument("--exclude-reason", help="POSTPONED_OR_CANCELLED | START_TIME_BOUNDARY | OTHER_DOCUMENTED")
    a.add_argument("--accept-missing-forecasts", action="store_true", help="owner decision: close a day in which no final game has a pregame forecast, declaring them all missing (a public data gap)")
    a.add_argument("--summary-out", type=Path)
    rc = sub.add_parser("reconcile")
    rc.add_argument("--archive", type=Path, required=True)
    rc.add_argument("--repo", type=Path, default=Path("."))
    rc.add_argument("--store", type=Path, required=True)
    rc.add_argument("--recipients", type=Path, required=True)
    rc.add_argument("--through", required=True, help="last ET date to settle (normally yesterday)")
    rc.add_argument("--dry-run", action="store_true", help="work on a throw-away copy of the store and report what would be sealed")
    rc.add_argument("--summary-out", type=Path)
    pb = sub.add_parser("publish")
    pb.add_argument("--staged", type=Path, required=True)
    pb.add_argument("--read-url", required=True)
    pb.add_argument("--push-url", required=True)
    pb.add_argument("--recipients", type=Path, required=True)
    pb.add_argument("--init", action="store_true")
    pb.add_argument("--expect-genesis")
    pb.add_argument("--ssh-key", type=Path, help="path of the deploy key file (never the key itself)")
    pb.add_argument("--forbid-repo", help="owner/name that must NOT be the destination (the code repository); compared exactly")
    pb.add_argument("--message", default="sealed-ledger: update")
    pb.add_argument("--summary-out", type=Path)
    i = sub.add_parser("init")
    i.add_argument("--store", type=Path, required=True)
    i.add_argument("--recipients", type=Path, required=True)
    i.add_argument("--summary-out", type=Path)
    b = sub.add_parser("scorecard")
    b.add_argument("--store", type=Path, required=True)
    b.add_argument("--out", type=Path, required=True)
    c = sub.add_parser("verify")
    c.add_argument("--store", type=Path, required=True)
    c.add_argument("--recipients", type=Path)
    c.add_argument("--previous", type=Path, help="the store as it was before this run: the new manifest must extend it")
    c.add_argument("--expect-genesis-hash", help="the genesis entry hash the owner registered after verifying the initial ledger; a different ledger is refused")
    d = sub.add_parser("attest")
    d.add_argument("--store", type=Path, required=True)
    d.add_argument("--out", type=Path)
    ns = ap.parse_args(argv)
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", getattr(ns, "date", "2000-01-01")):
        raise SystemExit("bad date")
    if ns.cmd == "ingest":
        if not ns.recipients.exists():
            raise SystemExit(f"no recipients file at {ns.recipients}: configure the owner's PUBLIC key(s) first (fail closed)")
        if ns.seal:
            load_recipients(ns.recipients)  # fail closed on an empty / secret-bearing file BEFORE any data is derived
        res = run_ingest(ns.archive, ns.date, ns.repo, ns.store, ns.recipients, seal=ns.seal, correct=_corrections(ns.correct), reason=ns.reason, exclude=_id_list(ns.exclude), exclude_reason=ns.exclude_reason, accept_no_forecast=ns.accept_missing_forecasts,
                         run_id=os.environ.get("GITHUB_RUN_ID", ""), code_sha=os.environ.get("GITHUB_SHA", ""))
        print(json.dumps(res, indent=1))
        if ns.summary_out:
            ns.summary_out.parent.mkdir(parents=True, exist_ok=True)
            ns.summary_out.write_text(json.dumps(res, indent=1))
        return 0
    if ns.cmd == "reconcile":
        from nhl_edge.sealed_ledger.reconcile import reconcile

        if not re.match(r"^\d{4}-\d{2}-\d{2}$", ns.through):
            raise SystemExit("bad --through date")
        res = reconcile(ns.archive, ns.repo, ns.store, ns.recipients, through=ns.through, dry_run=ns.dry_run, run_id=os.environ.get("GITHUB_RUN_ID", ""),
                        code_sha=os.environ.get("GITHUB_SHA", ""))
        print(json.dumps(res, indent=1))
        if ns.summary_out:
            ns.summary_out.parent.mkdir(parents=True, exist_ok=True)
            ns.summary_out.write_text(json.dumps(res, indent=1))
        return 0
    if ns.cmd == "publish":
        import tempfile

        from nhl_edge.sealed_ledger import publisher

        kh = publisher.write_known_hosts(Path(tempfile.mkdtemp(prefix="kh_")) / "known_hosts") if ns.ssh_key else None
        res = publisher.publish(ns.staged, read_url=ns.read_url, push_url=ns.push_url, recipients=ns.recipients, init=ns.init, expect_genesis=ns.expect_genesis,
                                ssh_key=ns.ssh_key, known_hosts=kh, message=ns.message, forbid_repo=ns.forbid_repo)
        print(json.dumps(res, indent=1))
        if ns.summary_out:
            ns.summary_out.parent.mkdir(parents=True, exist_ok=True)
            ns.summary_out.write_text(json.dumps(res, indent=1))
        return 0
    if ns.cmd == "init":
        if not ns.recipients.exists():
            raise SystemExit(f"no recipients file at {ns.recipients} (fail closed)")
        res = run_init(ns.store, ns.recipients, run_id=os.environ.get("GITHUB_RUN_ID", ""), code_sha=os.environ.get("GITHUB_SHA", ""))
        print(json.dumps(res, indent=1))
        if ns.summary_out:
            ns.summary_out.parent.mkdir(parents=True, exist_ok=True)
            ns.summary_out.write_text(json.dumps(res, indent=1))
        return 0
    if ns.cmd == "scorecard":
        ns.out.mkdir(parents=True, exist_ok=True)
        sc = blinded_scorecard(read_manifest(ns.store))
        (ns.out / "SHADOW_SCORECARD.json").write_text(json.dumps(sc, indent=1))
        print(json.dumps(sc, indent=1))
        return 0
    if ns.cmd == "verify":
        sha = load_recipients(ns.recipients)[1] if ns.recipients else None
        rep = verify_store(ns.store, recipients_sha256=sha)
        probs = list(rep.problems)
        if ns.expect_genesis_hash is not None and genesis_hash(read_manifest(ns.store)) != ns.expect_genesis_hash:
            probs.append("the ledger's genesis hash differs from the one the owner registered: this is a different (replaced or recreated) ledger")
        if ns.previous is not None:
            if not ns.previous.is_dir():
                probs.append(f"--previous {ns.previous} is not a directory (a typo would silently disable the append-only check)")
            else:  # an existing directory without a manifest is the legitimate "first publish" case
                probs += is_extension(read_manifest(ns.previous), read_manifest(ns.store))
        print(json.dumps({**rep.summary(), "problems": probs, "ok": not probs}, indent=1))
        return 0 if not probs else 1
    if ns.cmd == "attest":
        from nhl_edge.sealed_ledger import checkpoint as CP

        pem = os.environ.get("LEDGER_ATTEST_KEY_PEM", "").encode()
        if not pem:
            print(json.dumps({"attested": False, "note": "no LEDGER_ATTEST_KEY_PEM configured (optional hardening); head hash only"}))
            return 0
        signed = CP.sign(CP.make_checkpoint(read_manifest(ns.store), "RUNNER"), CP.load_private(pem, None))
        out = ns.out or (ns.store / "checkpoints" / f"runner_{signed['checkpoint']['seq']:06d}.json")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(signed, indent=1, sort_keys=True))
        print(json.dumps({"attested": True, "seq": signed["checkpoint"]["seq"], "head_hash": signed["checkpoint"]["head_hash"]}))
        return 0
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SealError as e:
        print(f"SEALED LEDGER REFUSED: {e}", file=sys.stderr)
        sys.exit(3)
    except Exception as e:  # noqa: BLE001
        if type(e).__name__ == "PublishError":  # its message carries git's stderr only (no record data, no key)
            print(f"SEALED LEDGER PUBLISH REFUSED: {e}", file=sys.stderr)
            sys.exit(5)
        # a traceback or pandas error message can echo row values; the public log gets the exception TYPE only
        print(f"SEALED LEDGER RUN FAILED: {type(e).__name__} (message and traceback suppressed so no record data reaches a public log; reproduce locally on a development-window date)", file=sys.stderr)
        sys.exit(4)
