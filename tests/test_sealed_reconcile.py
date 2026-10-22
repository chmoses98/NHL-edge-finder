"""Unattended reconciliation and fast-forward publication of the sealed ledger: missed days, retries, postponed games, source revisions, model-drift guard, dry run, and
publication to a (local, bare) ledger repository. All synthetic: no archive, no real key, no network."""

from __future__ import annotations

import base64
import hashlib
import json
import shutil
import subprocess
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pandas as pd
import pytest
from pyrage import x25519

from nhl_edge.sealed_ledger import PROTOCOL_RULES, owner, publisher, runner, seal
from nhl_edge.sealed_ledger import reconcile as R
from nhl_edge.sealed_ledger.core import genesis_hash, read_manifest, verify_store
from nhl_edge.sealed_ledger.selftest import SENTINEL, synthetic_rows

REPO = Path(__file__).resolve().parents[1]
NOW = datetime(2026, 11, 20, 12, 0, tzinfo=UTC)


@pytest.fixture(autouse=True)
def _not_ci(monkeypatch):
    for k in ("GITHUB_ACTIONS", "CI"):
        monkeypatch.delenv(k, raising=False)


@pytest.fixture()
def rec(tmp_path):
    a, b = x25519.Identity.generate(), x25519.Identity.generate()
    p = tmp_path / "recipients.txt"
    p.write_text(f"{a.to_public()}\n{b.to_public()}\n")
    return p


def mkgames(spec):
    """spec: (game_id, date, start 'YYYY-MM-DDTHH:MM:SS' UTC, is_final[, first_start])."""
    rows = []
    for t in spec:
        gid, d, st, fin = t[:4]
        fs = t[4] if len(t) > 4 else st
        rows.append({"game_id": gid, "game_date_et": d, "season_type": "regular", "start_time_utc": pd.Timestamp(st, tz="UTC"), "is_final": fin, "first_start_seen": pd.Timestamp(fs, tz="UTC")})
    return pd.DataFrame(rows)


def mkresults(rows=()):
    return pd.DataFrame(list(rows), columns=["game_id", "_observed_at_utc", "home_final", "away_final", "last_period_type", "_file"])


def fake_build(games, drift=0.0, no_forecast=()):
    def build(archive, date, repo):
        day = games[(games["game_date_et"] == date) & (games["start_time_utc"] >= pd.Timestamp("2026-10-21T17:13:05Z"))]
        sched = sorted(day["game_id"])
        fin = sorted(day[day["is_final"]]["game_id"])
        rows = []
        for i, gid in enumerate(g for g in fin if g not in no_forecast):
            r = synthetic_rows(date, i, 1)[0]
            r["game_id"] = gid
            rows.append(r)
        info = {"date": date, "games_scheduled": len(sched), "games_final": len(fin), "scheduled_game_ids": sched, "final_game_ids": fin, "all_scheduled_final": bool(sched) and set(sched) == set(fin),
                "games_with_pregame_forecast": len(rows), "missing_pregame_forecast": sorted(set(fin) & set(no_forecast)), "reproduction_max_abs_diff": drift}
        return rows, info

    return build


def world(tmp_path, rec, spec, results=()):
    store = tmp_path / "store"
    runner.run_init(store, rec)
    games = mkgames(spec)
    return store, games, mkresults(results)


def run(tmp_path, rec, store, games, results, build=None, through="2026-11-19", **kw):
    return R.reconcile(tmp_path / "archive", REPO, store, rec, through=through, now=kw.pop("now", NOW), games=games, results=results, build_rows_fn=build or fake_build(games), **kw)


THREE_DAYS = [("G1", "2026-10-21", "2026-10-21T23:00:00", True), ("G2", "2026-10-21", "2026-10-21T23:30:00", True), ("G3", "2026-10-22", "2026-10-22T23:00:00", True),
              ("G4", "2026-10-23", "2026-10-23T23:00:00", True), ("G5", "2026-10-23", "2026-10-23T23:30:00", True)]


def test_missed_days_are_reconciled_in_ascending_order_in_one_pass_and_a_rerun_is_a_noop(tmp_path, rec):
    store, games, res = world(tmp_path, rec, THREE_DAYS)
    out = run(tmp_path, rec, store, games, res)
    assert out["status"] == "OK" and out["dates_closed"] == ["2026-10-21", "2026-10-22", "2026-10-23"] and out["games_sealed"] == 5 and out["changed"]
    assert verify_store(store).ok and verify_store(store).n_games_closed == 5
    before = (store / "manifest.jsonl").read_bytes()
    again = run(tmp_path, rec, store, games, res)
    assert again["status"] == "IDLE" and not again["changed"] and (store / "manifest.jsonl").read_bytes() == before  # idempotent: a retry changes nothing


def test_a_bounded_run_continues_where_it_stopped_and_an_interrupted_run_resumes_without_duplicates(tmp_path, rec, monkeypatch):
    store, games, res = world(tmp_path, rec, THREE_DAYS)
    first = run(tmp_path, rec, store, games, res, max_dates=1)
    assert first["status"] == "PARTIAL" and first["dates_closed"] == ["2026-10-21"]
    # a crash while closing the next day: the process dies after sealing its games but before the DAY entry
    real = seal.SealedStore.close_day
    monkeypatch.setattr(seal.SealedStore, "close_day", lambda *a, **k: (_ for _ in ()).throw(OSError("runner lost")))
    with pytest.raises(OSError):
        run(tmp_path, rec, store, games, res)
    monkeypatch.setattr(seal.SealedStore, "close_day", real)
    out = run(tmp_path, rec, store, games, res)
    assert out["status"] == "OK" and out["dates_closed"] == ["2026-10-22", "2026-10-23"]
    ids = [e["game_id"] for e in read_manifest(store) if e["kind"] == "RECORD"]
    assert sorted(ids) == sorted(set(ids)) == ["G1", "G2", "G3", "G4", "G5"]  # no duplicates, nothing lost
    assert verify_store(store).ok


def test_a_game_that_is_merely_late_makes_the_day_wait_without_alert_then_closes(tmp_path, rec):
    spec = [("G1", "2026-11-18", "2026-11-18T23:00:00", True), ("G2", "2026-11-18", "2026-11-18T23:30:00", False), ("G3", "2026-11-19", "2026-11-19T23:00:00", True)]
    store, games, res = world(tmp_path, rec, spec)
    out = run(tmp_path, rec, store, games, res)
    assert out["status"] == "WAITING" and not out["blocked"] and out["waiting"] == [{"date": "2026-11-18", "game_ids": ["G2"]}]
    assert out["dates_closed"] == [] and out["games_sealed"] == 1 and runner.blinded_scorecard(read_manifest(store))["n_prospective_games"] == 0  # sealed but not counted yet
    games.loc[games["game_id"] == "G2", "is_final"] = True
    out = run(tmp_path, rec, store, games, res)
    assert out["status"] == "OK" and out["dates_closed"] == ["2026-11-18", "2026-11-19"]


def test_a_postponed_game_is_excluded_mechanically_after_the_prespecified_wait_and_later_days_proceed(tmp_path, rec):
    spec = [("P1", "2026-10-25", "2026-10-25T23:00:00", False), ("P2", "2026-10-25", "2026-10-25T23:30:00", True), ("P3", "2026-10-26", "2026-10-26T23:00:00", True)]
    store, games, res = world(tmp_path, rec, spec)
    out = run(tmp_path, rec, store, games, res, now=datetime(2026, 11, 5, tzinfo=UTC), through="2026-11-04")  # 11 days: still within the 14-day wait
    assert out["status"] == "WAITING" and out["waiting"][0]["game_ids"] == ["P1"]
    out = run(tmp_path, rec, store, games, res, now=datetime(2026, 11, 10, tzinfo=UTC), through="2026-11-09")  # > 14 days after the start
    assert out["status"] == "OK" and out["exclusions"] == [{"date": "2026-10-25", "game_ids": ["P1"], "reason": "POSTPONED_OR_CANCELLED"}] and out["dates_closed"] == ["2026-10-25", "2026-10-26"]
    day = next(e for e in read_manifest(store) if e["kind"] == "DAY" and e["game_date_et"] == "2026-10-25")
    assert day["excluded_game_ids"] == ["P1"] and day["sealed_game_ids"] == ["P2"] and verify_store(store).ok
    # if the schedule later lists the excluded game on a new date it stays excluded (never sealed, never drift)
    games.loc[games["game_id"] == "P1", ["game_date_et", "start_time_utc", "is_final"]] = ["2026-11-02", pd.Timestamp("2026-11-02T23:00:00", tz="UTC"), True]
    out = run(tmp_path, rec, store, games, res, now=datetime(2026, 11, 12, tzinfo=UTC), through="2026-11-11")
    assert out["status"] in ("IDLE", "OK") and not out["blocked"] and "P1" not in [e["game_id"] for e in read_manifest(store) if e["kind"] == "RECORD"]


def test_a_freeze_boundary_game_is_excluded_by_rule_not_by_discretion(tmp_path, rec):
    spec = [("B1", "2026-10-21", "2026-10-21T23:00:00", True, "2026-10-21T15:00:00"), ("B2", "2026-10-21", "2026-10-21T23:30:00", True)]  # B1's start moved across the freeze
    store, games, res = world(tmp_path, rec, spec)
    out = run(tmp_path, rec, store, games, res)
    assert out["exclusions"] == [{"date": "2026-10-21", "game_ids": ["B1"], "reason": "START_TIME_BOUNDARY"}] and "B1" not in [e["game_id"] for e in read_manifest(store) if e["kind"] == "RECORD"]
    assert verify_store(store).ok and not out["blocked"]


def test_a_revised_final_score_becomes_the_next_version_and_a_rerun_does_not_stack_more(tmp_path, rec):
    store, games, res0 = world(tmp_path, rec, [("A1", "2026-10-21", "2026-10-21T23:00:00", True)])
    base = [("A1", "2026-10-22T05:00:00Z", 3, 2, "REG", "r/a")]
    run(tmp_path, rec, store, games, mkresults(base))
    revised = base + [("A1", "2026-10-25T05:00:00Z", 4, 2, "REG", "r/b")]
    out = run(tmp_path, rec, store, games, mkresults(revised))
    assert out["status"] == "OK" and out["corrections"] == [{"game_id": "A1", "from_version": 1, "date": "2026-10-21"}]
    vs = [(e["version"], e["supersedes"], e["reason"]) for e in read_manifest(store) if e["kind"] == "RECORD"]
    assert vs == [(1, None, None), (2, 1, "SOURCE_SCORE_REVISED")]
    n = len(read_manifest(store))
    assert run(tmp_path, rec, store, games, mkresults(revised + [("A1", "2026-10-26T05:00:00Z", 4, 2, "REG", "r/c")]))["status"] == "IDLE"  # re-observed unchanged: no new version
    assert len(read_manifest(store)) == n
    again = revised + [("A1", "2026-10-27T05:00:00Z", 5, 2, "REG", "r/d")]
    assert run(tmp_path, rec, store, games, mkresults(again))["corrections"][0]["from_version"] == 2
    third = again + [("A1", "2026-10-29T05:00:00Z", 6, 2, "REG", "r/e")]
    out = run(tmp_path, rec, store, games, mkresults(third))
    assert out["status"] == "BLOCKED" and out["blocked"][0]["code"] == "CORRECTION_LIMIT"  # a fourth value is an exception, not an endless rewrite
    assert verify_store(store).ok


def test_model_drift_and_changed_frozen_parameters_block_before_anything_is_sealed(tmp_path, rec):
    store, games, res = world(tmp_path, rec, THREE_DAYS)
    out = run(tmp_path, rec, store, games, res, build=fake_build(games, drift=1e-3))
    assert out["status"] == "BLOCKED" and out["blocked"][0]["code"] == "MODEL_DRIFT" and out["dates_closed"] == [] and verify_store(store).n_games == 0
    fake_repo = tmp_path / "repo"
    shutil.copytree(REPO / "docs", fake_repo / "docs", ignore=shutil.ignore_patterns("*.md"))
    p = fake_repo / R.C1_PARAMS_FILE
    d = json.loads(p.read_text())
    d["c1_frozen_all_wf"]["b_s"] += 0.01
    p.write_text(json.dumps(d))
    out = R.reconcile(tmp_path / "a", fake_repo, store, rec, through="2026-11-19", now=NOW, games=games, results=res, build_rows_fn=fake_build(games))
    assert out["status"] == "BLOCKED" and out["blocked"][0]["code"] == "C1_PARAMS_CHANGED" and not out["changed"]
    assert R.c1_params_sha256(REPO) == PROTOCOL_RULES["c1_frozen_params_sha256"]  # the real frozen file matches the committed hash


def test_structural_exceptions_block_but_keep_what_was_safely_sealed_and_alert_once_per_cause(tmp_path, rec):
    store, games, res = world(tmp_path, rec, THREE_DAYS)
    run(tmp_path, rec, store, games, res, through="2026-10-22")
    games2 = pd.concat([games, mkgames([("G9", "2026-10-21", "2026-10-21T23:45:00", True)])], ignore_index=True)  # a game appears on a day that was already closed
    out = run(tmp_path, rec, store, games2, res, build=fake_build(games2))
    assert out["status"] == "BLOCKED" and any(b["code"] == "DRIFT" for b in out["blocked"])
    assert out["dates_closed"] == [] and verify_store(store).n_games_closed == 3  # earlier days intact, no later day sealed past the problem
    orphan = mkresults([("Z999", "2026-10-30T05:00:00Z", 1, 0, "REG", "results/dt=2026-10-30/z")])
    out = run(tmp_path, rec, store, games, orphan, through="2026-10-22")
    assert out["status"] == "BLOCKED" and any(b["code"] == "ORPHAN_RESULT" for b in out["blocked"])


def test_a_whole_day_without_pregame_forecasts_is_blocked_not_closed(tmp_path, rec):
    store, games, res = world(tmp_path, rec, [("G1", "2026-10-21", "2026-10-21T23:00:00", True), ("G2", "2026-10-21", "2026-10-21T23:30:00", True)])
    out = run(tmp_path, rec, store, games, res, build=fake_build(games, no_forecast=("G1", "G2")))
    assert out["status"] == "BLOCKED" and out["blocked"][0]["code"] == "NO_PREGAME_FORECAST" and out["dates_closed"] == []
    out = run(tmp_path, rec, store, games, res, build=fake_build(games, no_forecast=("G2",)))  # one game lacking a forecast is a declared data gap, not an exception
    assert out["status"] == "OK" and next(e for e in read_manifest(store) if e["kind"] == "DAY")["missing_pregame_game_ids"] == ["G2"]


def test_dry_run_reports_what_would_happen_and_touches_nothing(tmp_path, rec):
    store, games, res = world(tmp_path, rec, THREE_DAYS)
    before = {p.relative_to(store): p.read_bytes() for p in store.rglob("*") if p.is_file()}
    out = run(tmp_path, rec, store, games, res, dry_run=True)
    assert out["mode"] == "DRY_RUN" and out["status"] == "OK" and out["dates_closed"] == ["2026-10-21", "2026-10-22", "2026-10-23"]
    assert {p.relative_to(store): p.read_bytes() for p in store.rglob("*") if p.is_file()} == before  # the real store is untouched


def test_the_summary_is_outcome_free(tmp_path, rec):
    store, games, res = world(tmp_path, rec, THREE_DAYS)
    out = run(tmp_path, rec, store, games, res)
    text = json.dumps(out)
    for banned in (SENTINEL, "y_home_win", "home_final", "away_final", "brier", "pit_", "attribution"):
        assert banned not in text
    assert set(out) <= {"mode", "through", "status", "dates_closed", "games_sealed", "corrections", "exclusions", "waiting", "blocked", "reproduction_max_abs_diff", "manifest_entries",
                        "head_seq", "head_hash", "changed", "note"}


def test_reconcile_cannot_run_without_an_initialised_ledger(tmp_path, rec):
    games = mkgames(THREE_DAYS)
    with pytest.raises(seal.SealError, match="not initialised"):
        run(tmp_path, rec, tmp_path / "nope", games, mkresults())


def test_runner_reconcile_cli_dry_run(tmp_path, rec, monkeypatch, capsys):
    store, games, res = world(tmp_path, rec, THREE_DAYS)
    import nhl_edge.market_audit.games as MG
    from nhl_edge.model_research import daily

    monkeypatch.setattr(MG, "build_games", lambda *a, **k: games)
    monkeypatch.setattr(MG, "read_kind", lambda *a, **k: res)
    monkeypatch.setattr(daily, "build_rows", fake_build(games))
    monkeypatch.setattr(R, "check_c1", True, raising=False)
    assert runner.main(["reconcile", "--archive", str(tmp_path), "--repo", str(REPO), "--store", str(store), "--recipients", str(rec), "--through", "2026-10-23", "--dry-run",
                        "--summary-out", str(tmp_path / "out" / "s.json")]) == 0
    s = json.loads((tmp_path / "out" / "s.json").read_text())
    assert s["status"] in ("OK", "BLOCKED", "IDLE") and s["mode"] == "DRY_RUN"


# ---------------------------------------------------------------- publication to the ledger repository (local bare repos) -------------------------------------

def git(*a, cwd=None):
    return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True).stdout


@pytest.fixture()
def remote(tmp_path):
    r = tmp_path / "ledger.git"
    git("init", "-q", "--bare", "-b", "main", str(r))
    return r


def staged_store(tmp_path, rec, name="staged", games=None, with_days=True):
    s = tmp_path / name
    runner.run_init(s, rec)
    if with_days:
        g = games if games is not None else mkgames(THREE_DAYS)
        R.reconcile(tmp_path / "a", REPO, s, rec, through="2026-11-19", now=NOW, games=g, results=mkresults(), build_rows_fn=fake_build(g))
    return s


def pub(staged, remote, rec, **kw):
    return publisher.publish(staged, read_url=f"file://{remote}", push_url=f"file://{remote}", recipients=rec, sleep=0, **kw)


def test_init_then_append_then_noop_publication_is_fast_forward_only(tmp_path, rec, remote):
    s0 = staged_store(tmp_path, rec, "s0", with_days=False)
    out = pub(s0, remote, rec, init=True)
    gh = out["genesis_hash"]
    assert out["pushed"] and out["head_seq"] == 0 and out["tag"] == "sealed-ledger-head-0"
    s1 = tmp_path / "s1"
    shutil.copytree(s0, s1)
    g = mkgames(THREE_DAYS)
    R.reconcile(tmp_path / "a", REPO, s1, rec, through="2026-11-19", now=NOW, games=g, results=mkresults(), build_rows_fn=fake_build(g))
    out = pub(s1, remote, rec, expect_genesis=gh)
    assert out["pushed"] and out["head_seq"] > 0 and out["tag"].startswith("sealed-ledger-head-")
    assert pub(s1, remote, rec, expect_genesis=gh)["pushed"] is False  # idempotent retry
    clone = tmp_path / "clone"
    git("clone", "-q", f"file://{remote}", str(clone))
    assert verify_store(clone).ok and verify_store(clone).n_games_closed == 5
    assert {p.name for p in clone.iterdir()} == {".git", "manifest.jsonl", "sealed"}  # only ciphertext + manifest reach the ledger repository
    assert "sealed-ledger-head-0" in git("tag", cwd=clone)


def test_publication_refusals(tmp_path, rec, remote):
    s0 = staged_store(tmp_path, rec, "s0", with_days=False)
    gh0 = genesis_hash(read_manifest(s0))
    with pytest.raises(publisher.PublishError, match="empty"):
        pub(s0, remote, rec, expect_genesis=gh0)  # only the approved init may create the ledger
    gh = pub(s0, remote, rec, init=True)["genesis_hash"]
    assert gh == gh0
    with pytest.raises(publisher.PublishError, match="already holds"):
        pub(s0, remote, rec, init=True)
    other = staged_store(tmp_path, rec, "other", with_days=False)  # a different ledger (different genesis) with the same recipients
    with pytest.raises(publisher.PublishError, match="genesis"):
        pub(other, remote, rec, expect_genesis=gh)
    with pytest.raises(publisher.PublishError, match="registered"):
        pub(s0, remote, rec, expect_genesis="f" * 64)
    with pytest.raises(publisher.PublishError, match="registered"):
        pub(s0, remote, rec)  # no registered genesis at all
    s1 = tmp_path / "s1"
    shutil.copytree(s0, s1)
    g = mkgames(THREE_DAYS)
    R.reconcile(tmp_path / "a", REPO, s1, rec, through="2026-11-19", now=NOW, games=g, results=mkresults(), build_rows_fn=fake_build(g))
    pub(s1, remote, rec, expect_genesis=gh)
    with pytest.raises(publisher.PublishError, match="extend"):  # a rolled-back / shorter staged ledger is refused
        pub(s0, remote, rec, expect_genesis=gh)
    (s1 / "leak.json").write_text("{}")
    with pytest.raises(publisher.PublishError, match="verification"):
        pub(s1, remote, rec, expect_genesis=gh)
    with pytest.raises(publisher.PublishError, match="code repository"):
        publisher.publish(s0, read_url=f"file://{remote}", push_url=f"file://{remote}", recipients=rec, expect_genesis=gh, forbid_url_substring="ledger.git")


def test_a_moved_remote_is_never_overwritten_and_transient_failures_are_retried(tmp_path, rec, remote, monkeypatch):
    s0 = staged_store(tmp_path, rec, "s0", with_days=False)
    gh = pub(s0, remote, rec, init=True)["genesis_hash"]
    s1 = tmp_path / "s1"
    shutil.copytree(s0, s1)
    g = mkgames(THREE_DAYS)
    R.reconcile(tmp_path / "a", REPO, s1, rec, through="2026-11-19", now=NOW, games=g, results=mkresults(), build_rows_fn=fake_build(g))
    calls = []
    real = publisher._git

    def spy(args, cwd=None, env=None, check=True):
        calls.append(list(args))
        if args[:1] == ["push"] and not any(c[:1] == ["push"] and c is not calls[-1] for c in calls):  # first push attempt: a transient network error
            return subprocess.CompletedProcess(args, 1, "", "fatal: unable to access: Connection timed out")
        return real(args, cwd=cwd, env=env, check=check)

    monkeypatch.setattr(publisher, "_git", spy)
    out = pub(s1, remote, rec, expect_genesis=gh)
    assert out["pushed"] and sum(c[:1] == ["push"] for c in calls) >= 2  # retried
    assert not any("--force" in c or "-f" in c or "--delete" in c or "+HEAD" in " ".join(c) for c in calls)  # never forced, never deleted

    def rejecting(args, cwd=None, env=None, check=True):
        if args[:1] == ["push"]:
            return subprocess.CompletedProcess(args, 1, "", " ! [rejected] HEAD -> main (non-fast-forward)")
        return real(args, cwd=cwd, env=env, check=check)

    s2 = tmp_path / "s2"
    shutil.copytree(s1, s2)
    g2 = pd.concat([g, mkgames([("G7", "2026-10-24", "2026-10-24T23:00:00", True)])], ignore_index=True)
    R.reconcile(tmp_path / "a", REPO, s2, rec, through="2026-11-19", now=NOW, games=g2, results=mkresults(), build_rows_fn=fake_build(g2))
    monkeypatch.setattr(publisher, "_git", rejecting)
    with pytest.raises(publisher.PublishError, match="not rewriting"):
        pub(s2, remote, rec, expect_genesis=gh)


def test_the_pinned_github_host_key_matches_its_published_fingerprint_and_ssh_is_strict(tmp_path):
    blob = base64.b64decode(publisher.GITHUB_HOST_KEY.split()[2])
    assert "SHA256:" + base64.b64encode(hashlib.sha256(blob).digest()).decode().rstrip("=") == publisher.GITHUB_HOST_FINGERPRINT
    kh = publisher.write_known_hosts(tmp_path / "kh")
    env = publisher.ssh_env(tmp_path / "deploy_key", kh)["GIT_SSH_COMMAND"]
    assert "StrictHostKeyChecking=yes" in env and "IdentitiesOnly=yes" in env and "BatchMode=yes" in env and f"UserKnownHostsFile={kh}" in env
    assert "AAAA" not in env and "BEGIN" not in env  # only a file path ever appears on a command line
    assert publisher.ssh_env(None, None) == {}


def test_the_publisher_has_no_decryption_no_key_reading_and_no_force():
    import ast

    src = (REPO / "src/nhl_edge/sealed_ledger/publisher.py").read_text()
    attrs = {n.attr for n in ast.walk(ast.parse(src)) if isinstance(n, ast.Attribute)}
    assert not attrs & {"decrypt", "decrypt_file", "decrypt_io", "Identity", "read_bytes"}  # it never opens the deploy key (ssh does, from a path) and cannot decrypt
    code = "\n".join(ln for ln in src.splitlines() if not ln.lstrip().startswith("#"))
    assert "--force" not in code.replace("never --force", "") and "--delete" not in code


def test_unfinished_dates_beyond_the_run_bound_are_not_silently_dropped(tmp_path, rec):
    spec = [(f"X{i}", (datetime(2026, 10, 21) + timedelta(days=i)).strftime("%Y-%m-%d"), (datetime(2026, 10, 21, 23) + timedelta(days=i)).strftime("%Y-%m-%dT%H:%M:%S"), True) for i in range(20)]
    store, games, res = world(tmp_path, rec, spec)
    a = run(tmp_path, rec, store, games, res, through="2026-11-19")
    assert a["status"] == "PARTIAL" and len(a["dates_closed"]) == R.MAX_DATES_PER_RUN
    b = run(tmp_path, rec, store, games, res, through="2026-11-19")
    assert b["status"] == "OK" and len(b["dates_closed"]) == 6 and verify_store(store).n_games_closed == 20


# ---------------------------------------------------------------- the owner's own unattended routine ------------------------------------------------------------

def _owner_world(tmp_path, rec, remote):
    ids = []
    for n in ("primary", "backup"):
        i = x25519.Identity.generate()
        f = tmp_path / f"{n}.txt"
        f.write_text(f"{i}\n")
        ids.append(f)
    # the recipients file must contain exactly these two public keys
    rec.write_text("".join(f"{x25519.Identity.from_str(f.read_text().strip()).to_public()}\n" for f in ids))
    s0 = staged_store(tmp_path, rec, "s0", with_days=False)
    pub(s0, remote, rec, init=True)
    local = tmp_path / "ledger_clone"
    git("clone", "-q", f"file://{remote}", str(local))
    wd = tmp_path / "witness"
    owner.witness_keygen(wd, passphrase="correct-horse")
    fc = owner.first_checkpoint(local, ids, wd, rec, passphrase="correct-horse")
    return s0, local, wd, fc


def test_weekly_check_verifies_everything_then_witnesses_and_a_rewritten_remote_is_refused(tmp_path, rec, remote):
    s0, local, wd, fc = _owner_world(tmp_path, rec, remote)
    gh = fc["genesis_hash"]
    assert json.loads((wd / "state.json").read_text())["genesis_hash"] == gh
    s1 = tmp_path / "s1"
    shutil.copytree(s0, s1)
    g = mkgames(THREE_DAYS)
    R.reconcile(tmp_path / "a", REPO, s1, rec, through="2026-11-19", now=NOW, games=g, results=mkresults(), build_rows_fn=fake_build(g))
    pub(s1, remote, rec, expect_genesis=gh)
    res = owner.weekly_check(local, wd, rec, ledger_url=f"file://{remote}", passphrase="correct-horse", max_stale_days=10_000)
    assert res["ok"] and res["witnessed"] and res["witness_log_head"] != fc["witness_log_head"] and res["witness_checkpoints"] == 1
    again = owner.weekly_check(local, wd, rec, ledger_url=f"file://{remote}", passphrase="correct-horse", max_stale_days=10_000)
    assert again["ok"] and again["witnessed"]  # nothing new: still verifies and re-witnesses
    # an attacker with write access rewinds the ledger repository: the owner's routine refuses to witness it
    attacker = tmp_path / "attacker"
    git("clone", "-q", f"file://{remote}", str(attacker))
    git("reset", "-q", "--hard", "HEAD~1", cwd=attacker)
    git("push", "-q", "--force", "origin", "HEAD:main", cwd=attacker)
    bad = owner.weekly_check(local, wd, rec, ledger_url=f"file://{remote}", passphrase="correct-horse", max_stale_days=10_000)
    assert not bad["ok"] and not bad["witnessed"] and "BEHIND" in bad["problems"][0]
    # ... and so is a diverged (replaced) history
    (attacker / "x.txt").write_text("replacement")
    git("add", "-A", cwd=attacker)
    git("-c", "user.name=a", "-c", "user.email=a@a", "commit", "-q", "-m", "replacement", cwd=attacker)
    git("push", "-q", "--force", "origin", "HEAD:main", cwd=attacker)
    div = owner.weekly_check(local, wd, rec, ledger_url=f"file://{remote}", passphrase="correct-horse", max_stale_days=10_000)
    assert not div["ok"] and not div["witnessed"] and "DIVERGED" in div["problems"][0]


def test_weekly_check_flags_a_ledger_that_stopped_growing_and_a_forged_witness_head(tmp_path, rec, remote):
    s0, local, wd, fc = _owner_world(tmp_path, rec, remote)
    # collection silently stopped long ago: the newest closed day is old
    st = seal.SealedStore(local, rec, now=NOW)
    rows = synthetic_rows("2026-09-01", 0, 1)
    st.seal_rows(rows)
    st.close_day("2026-09-01", [rows[0]["game_id"]], [])
    res = owner.weekly_check(local, wd, rec, passphrase="correct-horse", max_stale_days=4)
    assert not res["ok"] and any("has not closed a day" in p for p in res["problems"]) and not res["witnessed"]
    state = json.loads((wd / "state.json").read_text())
    state["witness_log_head"] = "0" * 64  # the owner's own record of the log head disagrees with the log: removal of lines is detected
    (wd / "state.json").write_text(json.dumps(state))
    res = owner.weekly_check(local, wd, rec, passphrase="correct-horse", max_stale_days=10_000)
    assert not res["ok"] and any("witness log head" in p for p in res["problems"])


def test_passphrase_command_is_local_and_validated(tmp_path):
    assert owner.passphrase_from_command("printf correct-horse") == "correct-horse"
    with pytest.raises(SystemExit, match="no usable passphrase"):
        owner.passphrase_from_command("printf x")
