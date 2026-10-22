"""Sealed prospective ledger: encryption, authentication, tamper evidence, ordering, idempotence, versioned corrections, rollback detection, crash recovery, the
frozen protocol commitment, the owner-only decryption boundary and the guarantee that the real prospective path emits no plaintext. All outcomes are SYNTHETIC and all
keys are throwaway; nothing here reads the archive or a real store."""

from __future__ import annotations

import ast
import json
import re
import shutil
import subprocess
from datetime import UTC, datetime
from pathlib import Path

import pyrage
import pytest
from pyrage import x25519

from nhl_edge.model_research import daily
from nhl_edge.sealed_ledger import checkpoint as CP
from nhl_edge.sealed_ledger import owner, protocol_rules_sha256, runner, seal
from nhl_edge.sealed_ledger.core import PAD_BYTES, ct_path, is_extension, read_manifest, size_band, verify_store
from nhl_edge.sealed_ledger.selftest import SENTINEL, synthetic_rows

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "nhl_edge"
T0 = datetime(2026, 10, 22, 12, 0, tzinfo=UTC)


@pytest.fixture(autouse=True)
def _not_ci(monkeypatch):
    for k in ("GITHUB_ACTIONS", "CI"):
        monkeypatch.delenv(k, raising=False)


@pytest.fixture()
def keys(tmp_path):
    a, b = x25519.Identity.generate(), x25519.Identity.generate()
    rec = tmp_path / "recipients.txt"
    rec.write_text(f"# test keys\n{a.to_public()}\n{b.to_public()}\n")
    return a, b, rec


def make_store(tmp_path, keys, days=((("2026-10-22"), 0, 4), (("2026-10-23"), 4, 4)), name="store"):
    a, _b, rec = keys
    st = seal.SealedStore(tmp_path / name, rec, run_id="t", code_sha="abc", now=T0)
    for day, start, n in days:
        st.seal_rows(synthetic_rows(day, start, n))
        st.close_day(day, [f"SYN{i:05d}" for i in range(start, start + n)], [])
    return st


# ---------------------------------------------------------------- encryption / authentication -----------------------------------------------------------------

def test_roundtrip_with_either_recipient_and_not_with_a_stranger(tmp_path, keys):
    a, b, _ = keys
    st = make_store(tmp_path, keys)
    e = next(x for x in st.entries if x["kind"] == "RECORD")
    for ident in (a, b):  # a backup recipient can recover the ledger on its own
        assert decrypt_ok(st.root, e, ident)
    with pytest.raises(pyrage.DecryptError):
        owner.decrypt_entry(st.root, e, [x25519.Identity.generate()])


def decrypt_ok(root, e, ident):
    rec = owner.decrypt_entry(root, e, [ident])["record"]
    return rec["game_id"] == e["game_id"] and SENTINEL in rec["attribution_evidence"]


def test_encryption_is_randomised_and_authenticated(tmp_path, keys):
    a, _b, rec = keys
    recips, _ = seal.load_recipients(rec)
    pt = b"x" * PAD_BYTES
    c1, c2 = pyrage.encrypt(pt, recips), pyrage.encrypt(pt, recips)
    assert c1 != c2  # fresh file key each time: equal plaintexts do not reveal themselves
    flipped = c1[:-1] + bytes([c1[-1] ^ 1])
    with pytest.raises(pyrage.DecryptError):
        pyrage.decrypt(flipped, [a])  # AEAD tag failure
    with pytest.raises(pyrage.DecryptError):
        pyrage.decrypt(c1[: len(c1) // 2], [a])  # truncation


def test_plaintext_is_padded_to_a_fixed_size_and_oversize_fails_closed(tmp_path, keys):
    st = make_store(tmp_path, keys)
    small, big = synthetic_rows("2026-10-24", 100, 1)[0], synthetic_rows("2026-10-24", 101, 1)[0]
    big["attribution_evidence"] = "z" * 2500  # a record ~3x larger ...
    st.seal_rows([small, big])
    lo, hi = size_band(2)
    sizes = [e["ct_bytes"] for e in st.entries if e["kind"] == "RECORD"]
    assert all(lo <= s <= hi for s in sizes)  # ... same ciphertext band: length carries no information
    huge = synthetic_rows("2026-10-24", 102, 1)[0]
    huge["attribution_evidence"] = "z" * PAD_BYTES
    with pytest.raises(seal.SealError, match="larger than the fixed"):
        st.seal_rows([huge])
    assert "SYN00102" not in {e.get("game_id") for e in read_manifest(st.root)}


def test_manifest_and_files_contain_no_outcome_field_or_sentinel(tmp_path, keys):
    st = make_store(tmp_path, keys)
    blob = b"".join(p.read_bytes() for p in st.root.rglob("*") if p.is_file())
    for banned in (SENTINEL.encode(), b"y_home_win", b"home_final", b"brier", b"pit_", b"attribution", b"roi"):
        assert banned not in blob
    for e in st.entries:
        if e["kind"] == "RECORD":
            assert set(e) == {"v", "seq", "kind", "game_id", "game_date_et", "version", "supersedes", "reason", "ct_sha256", "ct_bytes", "pregame", "sealed_utc", "run_id",
                              "code_sha", "prev_hash", "entry_hash"}
            assert set(e["pregame"]) == {"slate_age_min", "sb_present"}
    assert all(re.fullmatch(r"\d{6}\.age", p.name) for p in (st.root / "sealed").iterdir())  # opaque names: no game id, no date


# ---------------------------------------------------------------- tamper evidence --------------------------------------------------------------------------

def _copy(st, tmp_path, name="mut"):
    d = tmp_path / name
    shutil.rmtree(d, ignore_errors=True)
    shutil.copytree(st.root, d)
    return d


def test_edit_reorder_delete_insert_in_the_manifest_are_detected(tmp_path, keys):
    st = make_store(tmp_path, keys)
    assert verify_store(st.root).ok
    lines = (st.root / "manifest.jsonl").read_text().splitlines(keepends=True)
    cases = {
        "edit": lambda ls: [ls[0]] + [ls[1].replace("SYN00000", "SYN99999")] + ls[2:],
        "reorder": lambda ls: [ls[0], ls[2], ls[1]] + ls[3:],
        "delete_middle": lambda ls: ls[:2] + ls[3:],
        "insert_duplicate": lambda ls: ls[:3] + [ls[2]] + ls[3:],
    }
    for name, f in cases.items():
        d = _copy(st, tmp_path, name)
        (d / "manifest.jsonl").write_text("".join(f(lines)))
        assert not verify_store(d).ok, name


def test_ciphertext_modified_deleted_swapped_or_replaced_by_plaintext_are_detected(tmp_path, keys):
    st = make_store(tmp_path, keys)
    for name, mut in {
        "bitflip": lambda r: ct_path(r, 1).write_bytes(ct_path(r, 1).read_bytes()[:-1] + b"\x00"),
        "delete": lambda r: ct_path(r, 2).unlink(),
        "swap": lambda r: ct_path(r, 1).write_bytes(ct_path(r, 2).read_bytes()),
        "plaintext_json_in_place": lambda r: ct_path(r, 3).write_text(json.dumps({"y_home_win": 1})),
        "stray_file": lambda r: (r / "sealed" / "notes.txt").write_text("x"),
        "stray_top_level": lambda r: (r / "ledger.jsonl").write_text("{}"),
    }.items():
        d = _copy(st, tmp_path, name)
        mut(d)
        assert not verify_store(d).ok, name


def test_a_fresh_valid_looking_replacement_is_caught_by_a_witness_checkpoint_not_by_the_chain(tmp_path, keys):
    st = make_store(tmp_path, keys)
    key = CP.generate_key()
    signed = CP.sign(CP.make_checkpoint(st.entries, "WITNESS", now=T0), key)
    assert CP.verify_signature(signed, key.public_key())
    forged = make_store(tmp_path, keys, name="forged")  # an attacker rebuilds a perfectly consistent ledger
    assert verify_store(forged.root).ok  # the chain alone cannot tell
    probs = CP.check_against_checkpoints(read_manifest(forged.root), [signed])
    assert probs and "REPLACED" in probs[0]


def test_truncation_and_rollback_are_detected_by_checkpoints_and_by_extension(tmp_path, keys):
    st = make_store(tmp_path, keys)
    before = read_manifest(st.root)
    signed = CP.sign(CP.make_checkpoint(before, "WITNESS", now=T0), CP.generate_key())
    d = _copy(st, tmp_path, "trunc")
    lines = (d / "manifest.jsonl").read_text().splitlines(keepends=True)
    (d / "manifest.jsonl").write_text("".join(lines[:-3]))
    assert verify_store(d).ok  # structurally fine: that is exactly why an external anchor exists
    assert any("TRUNCATED" in p for p in CP.check_against_checkpoints(read_manifest(d), [signed]))
    assert is_extension(before, read_manifest(d))
    # rewrite of an old entry, same length
    st2 = make_store(tmp_path, keys, name="alt")
    assert any("REPLACED" in p or "REWRITTEN" in p for p in CP.check_against_checkpoints(read_manifest(st2.root), [signed]))


def test_signature_and_witness_log_authentication(tmp_path, keys):
    st = make_store(tmp_path, keys)
    k, other = CP.generate_key(), CP.generate_key()
    signed = CP.sign(CP.make_checkpoint(st.entries, "WITNESS", now=T0), k)
    assert not CP.verify_signature(signed, other.public_key())
    signed2 = json.loads(json.dumps(signed))
    signed2["checkpoint"]["seq"] += 1
    assert not CP.verify_signature(signed2, k.public_key())
    log = tmp_path / "witness.jsonl"
    CP.witness_append(log, signed)
    CP.witness_append(log, CP.sign(CP.make_checkpoint(st.entries, "WITNESS", now=T0), k))
    _, probs = CP.witness_read(log, k.public_key())
    assert not probs
    lines = log.read_text().splitlines(keepends=True)
    log.write_text(lines[1])  # the owner's own log with the first line removed
    assert CP.witness_read(log, k.public_key())[1]
    pem = CP.private_pem(k, b"pw")
    assert CP.load_private(pem, b"pw").public_key().public_bytes_raw() == k.public_key().public_bytes_raw()
    with pytest.raises(TypeError):
        CP.load_private(pem, None)


# ---------------------------------------------------------------- ordering / idempotence / corrections / missing -----------------------------------------------

def test_records_are_sealed_in_the_given_order_with_contiguous_sequence_numbers(tmp_path, keys):
    st = make_store(tmp_path, keys)
    es = read_manifest(st.root)
    assert [e["seq"] for e in es] == list(range(len(es)))
    assert [e["game_id"] for e in es if e["kind"] == "RECORD"] == [f"SYN{i:05d}" for i in range(8)]
    assert es[0]["kind"] == "GENESIS" and [e["kind"] for e in es].count("DAY") == 2


def test_reprocessing_a_game_never_duplicates_and_resumes_after_new_games(tmp_path, keys):
    st = make_store(tmp_path, keys)
    before = (st.root / "manifest.jsonl").read_bytes()
    st2 = seal.SealedStore(st.root, keys[2], now=T0)
    changed = synthetic_rows("2026-10-22", 0, 4)
    changed[0]["home_final"] = 99  # a DIFFERENT row for an existing game must not overwrite silently
    res = st2.seal_rows(changed)
    assert res == {"sealed_new": 0, "skipped_existing": 4, "corrections": 0}
    assert (st.root / "manifest.jsonl").read_bytes() == before
    res = st2.seal_rows(synthetic_rows("2026-10-22", 0, 4) + synthetic_rows("2026-10-22", 20, 2))  # late-finishing games are added; the first four are skipped
    assert res == {"sealed_new": 2, "skipped_existing": 4, "corrections": 0}
    assert verify_store(st.root).ok
    assert st2.close_day("2026-10-22", [], []) is False  # day already closed (idempotent)
    with pytest.raises(seal.SealError, match="duplicate game_id"):
        st2.seal_rows(synthetic_rows("2026-10-25", 50, 1) * 2)


def test_a_correction_is_a_new_version_and_never_overwrites(tmp_path, keys):
    a, _b, rec = keys
    st = make_store(tmp_path, keys)
    old_ct = ct_path(st.root, 1).read_bytes()
    fixed = synthetic_rows("2026-10-22", 0, 1)
    fixed[0]["home_final"] = 7
    with pytest.raises(seal.SealError, match="reason code"):
        st.seal_rows(fixed, correct={"SYN00000"})
    with pytest.raises(seal.SealError, match="never sealed"):
        st.seal_rows(fixed, correct={"NOPE"}, reason="OTHER_DOCUMENTED")
    with pytest.raises(seal.SealError, match="no re-derived row"):
        st.seal_rows([], correct={"SYN00000"}, reason="OTHER_DOCUMENTED")
    assert st.seal_rows(fixed, correct={"SYN00000"}, reason="SOURCE_SCORE_REVISED") == {"sealed_new": 0, "skipped_existing": 0, "corrections": 1}
    assert ct_path(st.root, 1).read_bytes() == old_ct  # the original ciphertext and entry are untouched
    es = [e for e in read_manifest(st.root) if e["kind"] == "RECORD" and e["game_id"] == "SYN00000"]
    assert [(e["version"], e["supersedes"], e["reason"]) for e in es] == [(1, None, None), (2, 1, "SOURCE_SCORE_REVISED")]
    assert verify_store(st.root).ok and verify_store(st.root).n_games == 8 and verify_store(st.root).n_corrections == 1
    rows, meta = owner.latest_rows(st.root, [a])
    assert rows[0]["home_final"] == 7 and meta["corrections"][0]["reason"] == "SOURCE_SCORE_REVISED"
    # a forged / out-of-sequence correction entry is detected
    d = _copy(st, tmp_path, "forge")
    lines = (d / "manifest.jsonl").read_text().splitlines(keepends=True)
    assert "SOURCE_SCORE_REVISED" in lines[-1]
    (d / "manifest.jsonl").write_text("".join(lines[:-1] + [lines[-1].replace('"version":2', '"version":5')]))
    assert not verify_store(d).ok


def test_missing_games_must_be_accounted_for_in_the_day_entry(tmp_path, keys):
    st = seal.SealedStore(tmp_path / "s", keys[2], now=T0)
    st.seal_rows(synthetic_rows("2026-10-22", 0, 2))
    with pytest.raises(seal.SealError, match="neither sealed nor listed"):
        st.close_day("2026-10-22", ["SYN00000", "SYN00001", "SYN00002"], [])
    assert st.close_day("2026-10-22", ["SYN00000", "SYN00001", "SYN00002"], ["SYN00002"])
    d = _copy(st, tmp_path, "m")
    ct_path(d, 1).unlink()
    assert any("deleted" in p for p in verify_store(d).problems)


# ---------------------------------------------------------------- failure recovery -----------------------------------------------------------------------

def test_crash_between_ciphertext_and_manifest_leaves_an_orphan_that_the_next_run_overwrites(tmp_path, keys, monkeypatch):
    st = make_store(tmp_path, keys)
    n0 = len(st.entries)
    real = seal._append_line
    calls = {"n": 0}

    def boom(path, entry):
        calls["n"] += 1
        raise OSError("simulated crash after the ciphertext was written")

    monkeypatch.setattr(seal, "_append_line", boom)
    with pytest.raises(OSError):
        st.seal_rows(synthetic_rows("2026-10-24", 20, 1))
    monkeypatch.setattr(seal, "_append_line", real)
    assert ct_path(st.root, n0).exists() and len(read_manifest(st.root)) == n0
    rep = verify_store(st.root)
    assert rep.ok and any("orphan" in w for w in rep.warnings)
    st2 = seal.SealedStore(st.root, keys[2], now=T0)  # a fresh process resumes
    assert st2.seal_rows(synthetic_rows("2026-10-24", 20, 1))["sealed_new"] == 1
    rep = verify_store(st.root)
    assert rep.ok and not rep.warnings and rep.n_games == 9


def test_a_torn_manifest_tail_blocks_appends_until_explicitly_repaired(tmp_path, keys):
    st = make_store(tmp_path, keys)
    p = st.root / "manifest.jsonl"
    good = p.read_bytes()
    p.write_bytes(good + b'{"v":1,"seq":99,"kind":"REC')  # crash mid-write
    assert not verify_store(st.root).ok
    with pytest.raises(seal.SealError):
        seal.SealedStore(st.root, keys[2], now=T0)
    st2 = seal.SealedStore(st.root, keys[2], now=T0, repair_torn_tail=True)  # drops ONLY the incomplete last line
    assert p.read_bytes() == good and st2.seal_rows(synthetic_rows("2026-10-24", 30, 1))["sealed_new"] == 1


# ---------------------------------------------------------------- recipients, key hygiene, frozen protocol --------------------------------------------------

def test_recipients_file_must_hold_only_public_keys_and_not_change_after_genesis(tmp_path, keys):
    secret = tmp_path / "bad.txt"
    secret.write_text(str(x25519.Identity.generate()) + "\n")
    with pytest.raises(seal.SealError, match="SECRET key"):
        seal.load_recipients(secret)
    empty = tmp_path / "empty.txt"
    empty.write_text("# nothing configured\n")
    with pytest.raises(seal.SealError, match="fail closed"):
        seal.load_recipients(empty)
    junk = tmp_path / "junk.txt"
    junk.write_text("not-a-key\n")
    with pytest.raises(seal.SealError):
        seal.load_recipients(junk)
    st = make_store(tmp_path, keys)
    other = tmp_path / "other.txt"
    other.write_text(f"{x25519.Identity.generate().to_public()}\n")
    with pytest.raises(seal.SealError, match="recipients"):
        seal.SealedStore(st.root, other, now=T0)  # an attacker (or mistake) swapping the public key is refused


def test_the_frozen_protocol_commitment_is_pinned():
    # Changing the 150/300/450 looks, the freeze instant or the spending schedule changes this hash and fails here AND on every existing ledger.
    assert protocol_rules_sha256() == "527508ce7e3cf1c0e677b7a022f22a176f62903f31a04788f9a5160969b7376d"
    assert daily.LOOKS == runner.LOOKS == (150, 300, 450)


def test_genesis_with_other_rules_is_rejected(tmp_path, keys, monkeypatch):
    st = make_store(tmp_path, keys)
    from nhl_edge import sealed_ledger as SL
    from nhl_edge.sealed_ledger import core

    monkeypatch.setattr(SL, "PROTOCOL_RULES", {**SL.PROTOCOL_RULES, "looks_games": [100, 300, 450]})
    monkeypatch.setattr(core, "protocol_rules_sha256", SL.protocol_rules_sha256)
    assert any("frozen prospective protocol" in p for p in verify_store(st.root).problems)


def test_owner_keygen_modes_and_no_overwrite(tmp_path):
    p = tmp_path / "id" / "identity.txt"
    pub = owner.generate_identity(p)
    assert pub.startswith("age1") and oct(p.stat().st_mode & 0o777) == "0o600"
    assert str(pub) in p.read_text() and "AGE-SECRET-KEY-" in p.read_text()
    with pytest.raises(SystemExit, match="already exists"):
        owner.generate_identity(p)


def test_check_key_confirms_the_held_key_is_a_recipient(tmp_path, keys):
    a, _b, rec = keys
    idf = tmp_path / "identity.txt"
    idf.write_text(f"{a}\n")
    ok = owner.check_key(idf, rec)
    assert ok["identity_matches_recipient"] and ok["canary_roundtrip"] and ok["recipient_count"] == 2 and ok["warning"] is None
    stranger = tmp_path / "stranger.txt"
    stranger.write_text(f"{x25519.Identity.generate()}\n")
    bad = owner.check_key(stranger, rec)
    assert not bad["identity_matches_recipient"] and not bad["canary_roundtrip"]
    one = tmp_path / "one.txt"
    one.write_text(f"{a.to_public()}\n")
    assert owner.check_key(idf, one)["warning"]


# ---------------------------------------------------------------- the single look --------------------------------------------------------------------------

def _owner_setup(tmp_path, keys, n_games):
    a, _b, rec = keys
    st = seal.SealedStore(tmp_path / "ledger", rec, now=T0)
    ids = []
    for i in range(0, n_games, 10):
        rows = synthetic_rows(f"2026-11-{1 + i // 10:02d}", i, min(10, n_games - i))
        st.seal_rows(rows)
        st.close_day(rows[0]["game_date_et"], [r["game_id"] for r in rows], [])
        ids += [r["game_id"] for r in rows]
    idf = tmp_path / "identity.txt"
    idf.write_text(f"{a}\n")
    wd = tmp_path / "witness"
    owner.witness_keygen(wd, passphrase="pw")
    return st, idf, wd


def test_look_refuses_before_150_games_and_never_decrypts(tmp_path, keys, monkeypatch):
    st, idf, wd = _owner_setup(tmp_path, keys, 149)
    monkeypatch.setattr(pyrage, "decrypt", lambda *a, **k: pytest.fail("decrypted before the threshold"))
    with pytest.raises(SystemExit, match="Nothing was decrypted"):
        owner.take_look(st.root, idf, wd, tmp_path / "out", allow_unwitnessed=True)
    assert not (tmp_path / "out").exists()


def test_look_at_150_is_written_once_with_provenance_and_requires_a_witness(tmp_path, keys):
    st, idf, wd = _owner_setup(tmp_path, keys, 150)
    out = tmp_path / "looks"
    with pytest.raises(SystemExit, match="witness log is empty"):
        owner.take_look(st.root, idf, wd, out)
    cp = owner.witness(st.root, wd, passphrase="pw")
    assert cp["seq"] == len(st.entries) - 1
    res = owner.take_look(st.root, idf, wd, out)
    assert res["status"] == "AT_LOOK_150" and (out / "LOOK_150.json").exists() and (out / "LOOK_150.provenance.json").exists()
    look = json.loads((out / "LOOK_150.json").read_text())
    assert look["games"] == 150 and "brier" in look
    with pytest.raises(SystemExit, match="already exists"):
        owner.take_look(st.root, idf, wd, out)


def test_look_refuses_a_rolled_back_ledger_and_a_tampered_one(tmp_path, keys):
    st, idf, wd = _owner_setup(tmp_path, keys, 150)
    owner.witness(st.root, wd, passphrase="pw")
    full = _copy(st, tmp_path, "full")
    st.seal_rows(synthetic_rows("2026-12-01", 500, 3))
    st.close_day("2026-12-01", ["SYN00500", "SYN00501", "SYN00502"], [])
    owner.witness(st.root, wd, passphrase="pw")  # witnessed the longer ledger
    rolled = full  # the shorter, older, internally valid copy
    assert verify_store(rolled).ok
    with pytest.raises(SystemExit, match="TRUNCATED"):
        owner.take_look(rolled, idf, wd, tmp_path / "o1")
    bad = _copy(st, tmp_path, "bad")
    ct_path(bad, 5).write_bytes(ct_path(bad, 5).read_bytes()[:-1] + b"\x01")
    with pytest.raises(SystemExit, match="fails verification"):
        owner.take_look(bad, idf, wd, tmp_path / "o2")


def test_reproduce_diff_flags_forged_or_omitted_records_without_printing_values(tmp_path, keys, monkeypatch):
    a, _b, rec = keys
    st = seal.SealedStore(tmp_path / "s", rec, now=T0)
    real = synthetic_rows("2026-11-01", 0, 3)
    forged = [dict(r) for r in real]
    forged[1]["home_final"] = 8  # the sealed copy of game 1 was forged
    st.seal_rows(forged[:2])  # and game 2 was omitted
    st.close_day("2026-11-01", ["SYN00000", "SYN00001"], [])
    monkeypatch.setattr(daily, "build_rows", lambda *a, **k: (real, {}))
    diffs = owner.reproduce_diff(st.root, [a], tmp_path, tmp_path)
    assert diffs == ["SYN00001: field home_final differs", "SYN00002: derivable from the archive but NOT in the ledger (omitted)"]
    assert owner.reproduce_diff(make_store(tmp_path, keys, name="ok", days=(("2026-11-01", 0, 3),)).root, [a], tmp_path, tmp_path) == []


def test_verify_all_with_witness_and_previous_copy(tmp_path, keys):
    st, _idf, wd = _owner_setup(tmp_path, keys, 20)
    owner.witness(st.root, wd, passphrase="pw")
    res = owner.verify_all(st.root, wd, keys[2], None)
    assert res["ok"] and res["witness_checkpoints"] == 1
    d = _copy(st, tmp_path, "t")
    lines = (d / "manifest.jsonl").read_text().splitlines(keepends=True)
    (d / "manifest.jsonl").write_text("".join(lines[:-1]))
    assert not owner.verify_all(d, wd, keys[2], None)["ok"]


def test_runner_attestation_roundtrip(tmp_path, keys, monkeypatch, capsys):
    st = make_store(tmp_path, keys)
    k = CP.generate_key()
    monkeypatch.setenv("LEDGER_ATTEST_KEY_PEM", CP.private_pem(k, None).decode())
    assert runner.main(["attest", "--store", str(st.root)]) == 0
    pub = tmp_path / "runner_pub.pem"
    pub.write_bytes(CP.public_pem(k))
    assert owner.verify_all(st.root, None, None, pub)["ok"]
    f = next((st.root / "checkpoints").glob("runner_*.json"))
    d = json.loads(f.read_text())
    d["checkpoint"]["head_hash"] = "0" * 64
    f.write_text(json.dumps(d))
    assert not owner.verify_all(st.root, None, None, pub)["ok"]
    assert verify_store(st.root).ok  # checkpoints/ files are an allowed, non-secret part of the store


# ---------------------------------------------------------------- the real prospective path emits no plaintext ----------------------------------------------

def _fake_build_rows(monkeypatch, rows, scheduled=None, missing=()):
    ids = scheduled or [r["game_id"] for r in rows]
    info = {"date": "2026-10-22", "games_scheduled": len(ids), "games_final": len(rows), "scheduled_game_ids": sorted(ids), "all_scheduled_final": True,
            "games_with_pregame_forecast": len(rows), "missing_pregame_forecast": list(missing), "reproduction_max_abs_diff": 0.0}
    monkeypatch.setattr(daily, "build_rows", lambda *a, **k: (rows, info))


def _forbid_plaintext_writers(monkeypatch):
    def nope(*a, **k):
        raise AssertionError("the prospective path called a plaintext ledger/look writer")

    monkeypatch.setattr(daily, "append_rows", nope)
    monkeypatch.setattr(daily, "scorecard", nope)


def test_real_path_ingest_seal_emits_no_plaintext_anywhere(tmp_path, keys, monkeypatch, capsys):
    _a, _b, rec = keys
    rows = synthetic_rows("2026-10-22", 0, 6)
    _fake_build_rows(monkeypatch, rows)
    _forbid_plaintext_writers(monkeypatch)
    work = tmp_path / "work"
    work.mkdir()
    monkeypatch.chdir(work)
    summary = tmp_path / "out" / "ingest_summary.json"
    argv = ["ingest", "--archive", str(tmp_path / "archive"), "--date", "2026-10-22", "--repo", ".", "--store", str(tmp_path / "store"), "--recipients", str(rec), "--seal",
            "--summary-out", str(summary)]
    assert runner.main(argv) == 0
    assert runner.main(["scorecard", "--store", str(tmp_path / "store"), "--out", str(tmp_path / "out")]) == 0
    assert runner.main(["verify", "--store", str(tmp_path / "store"), "--recipients", str(rec)]) == 0
    seen = capsys.readouterr()
    blob = (seen.out + seen.err).encode() + b"".join(p.read_bytes() for p in tmp_path.rglob("*") if p.is_file() and p.name != "recipients.txt")
    for banned in (SENTINEL.encode(), b"y_home_win", b"home_final", b"y_total", b"v1_p_home_win", b"brier_v1", b"pit_total", b"attribution_class"):
        assert banned not in blob, banned
    out = json.loads(summary.read_text())
    assert out["sealed_new"] == 6 and out["day_closed"] is True and out["integrity_ok"] is True
    assert set(out) <= {"date", "mode", "games_scheduled", "games_final", "games_with_pregame_forecast", "missing_pregame_forecast", "reproduction_max_abs_diff",
                        "all_scheduled_final", "sealed_new", "skipped_existing", "corrections", "day_closed", "integrity_ok", "manifest_entries", "head_seq", "head_hash"}
    # re-running the same date is idempotent
    assert runner.main(argv) == 0
    assert json.loads(summary.read_text())["sealed_new"] == 0
    assert list(work.iterdir()) == []  # nothing was written into the working directory either


def test_real_path_dry_run_writes_nothing(tmp_path, keys, monkeypatch):
    _a, _b, rec = keys
    _fake_build_rows(monkeypatch, synthetic_rows("2026-10-22", 0, 3))
    _forbid_plaintext_writers(monkeypatch)
    res = runner.run_ingest(tmp_path / "a", "2026-10-22", Path("."), tmp_path / "store", rec, seal=False, correct=set(), reason=None)
    assert res["mode"] == "DRY_RUN" and res["sealed_new"] == 0 and not (tmp_path / "store").exists()


def test_real_path_fails_closed_without_recipients(tmp_path, monkeypatch):
    _fake_build_rows(monkeypatch, synthetic_rows("2026-10-22", 0, 3))
    rec = tmp_path / "recipients.txt"
    rec.write_text("# no key configured yet\n")
    with pytest.raises(seal.SealError, match="fail closed"):
        runner.main(["ingest", "--archive", str(tmp_path), "--date", "2026-10-22", "--store", str(tmp_path / "s"), "--recipients", str(rec), "--seal"])
    assert not (tmp_path / "s").exists()
    with pytest.raises(SystemExit):  # file missing entirely
        runner.main(["ingest", "--archive", str(tmp_path), "--date", "2026-10-22", "--store", str(tmp_path / "s"), "--recipients", str(tmp_path / "nope.txt"), "--seal"])


def test_plaintext_ingest_is_refused_for_prospective_dates():
    with pytest.raises(daily.PlaintextProspectiveLedgerForbidden):
        daily.ingest(Path("."), "2026-10-22", Path("."), Path("ledger.jsonl"), dev_dry_run=False)


def test_runner_scorecard_equals_the_frozen_blinded_scorecard_and_never_computes_a_look(tmp_path, keys):
    _a, _b, rec = keys
    st = seal.SealedStore(tmp_path / "s", rec, now=T0)
    rows = synthetic_rows("2026-11-01", 0, 10)
    rows[3]["sb_p_home"] = None
    st.seal_rows(rows)
    mine = runner.blinded_scorecard(st.entries)
    ref = daily.scorecard([{**r, "y_home_win": 1} for r in rows])
    assert set(mine) == set(ref) and mine["status"] == ref["status"] == "ACCUMULATING_BLINDED" and mine["n_prospective_games"] == 10
    assert mine["data_quality"]["missing_sportsbook_share"] == ref["data_quality"]["missing_sportsbook_share"] == 0.1
    assert mine["data_quality"]["mean_slate_age_min"] == pytest.approx(ref["data_quality"]["mean_slate_age_min"])
    big = seal.SealedStore(tmp_path / "b", rec, now=T0)
    for i in range(0, 150, 15):
        big.seal_rows(synthetic_rows(f"2026-12-{1 + i // 15:02d}", i, 15))
    sc = runner.blinded_scorecard(big.entries)
    assert sc["status"] == "LOOK_150_DUE_OWNER_LOCAL" and "look" not in sc and not list((tmp_path / "b").glob("LOOK_*"))


def test_bounded_batch_size(tmp_path, keys):
    st = seal.SealedStore(tmp_path / "s", keys[2], now=T0)
    with pytest.raises(seal.SealError, match="exceeds the bound"):
        st.seal_rows(synthetic_rows("2026-11-01", 0, seal.MAX_GAMES_PER_RUN + 1))


# ---------------------------------------------------------------- development tools cannot decrypt ---------------------------------------------------------------

def _py_files():
    return [p for p in SRC.rglob("*.py")]


def test_only_owner_py_can_decrypt_and_nothing_imports_it():
    allowed_decrypt = {SRC / "sealed_ledger" / "owner.py", SRC / "sealed_ledger" / "selftest.py"}
    for p in _py_files():
        tree = ast.parse(p.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute) and node.attr in {"decrypt", "decrypt_file", "decrypt_io"}:
                assert p in allowed_decrypt | {SRC / "sealed_ledger" / "owner.py"}, f"{p} calls .{node.attr}"
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                names = [a.name for a in node.names] + [getattr(node, "module", "") or ""]
                if any(n.endswith("sealed_ledger.owner") or n == "owner" for n in names) or (
                    isinstance(node, ast.ImportFrom) and node.module == "nhl_edge.sealed_ledger" and any(a.name in ("owner", "selftest") for a in node.names)
                ):
                    assert p in allowed_decrypt, f"{p} imports the owner-only module"
    # every model / challenger module is free of the sealed ledger altogether
    for p in (SRC / "model_research").glob("*.py"):
        for node in ast.walk(ast.parse(p.read_text())):
            mods = [node.module or ""] + [a.name for a in node.names] if isinstance(node, ast.ImportFrom) else [a.name for a in node.names] if isinstance(node, ast.Import) else []
            assert not any("sealed_ledger" in m for m in mods), f"{p.name}: challenger/model code must not import the sealed ledger"


def test_runner_and_seal_have_no_identity_handling():
    for name in ("seal.py", "runner.py", "core.py"):
        tree = ast.parse((SRC / "sealed_ledger" / name).read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                assert node.attr not in {"decrypt", "Identity", "from_str_identity"}, (name, node.attr)


def test_owner_refuses_to_run_in_ci(monkeypatch, tmp_path):
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    with pytest.raises(SystemExit, match="must not run in CI"):
        owner.generate_identity(tmp_path / "k.txt")
    with pytest.raises(SystemExit, match="must not run in CI"):
        owner.main(["keygen", "--identity", str(tmp_path / "k2.txt")])


def test_no_private_key_material_is_committed_anywhere():
    files = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=False).stdout.split()
    if not files:
        files = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file() and ".venv" not in p.parts and ".git" not in p.parts]
    pat = re.compile(r"AGE-SECRET-KEY-1[0-9A-Z]{50,}|-----BEGIN (?:ENCRYPTED |EC |RSA |OPENSSH )?PRIVATE KEY-----")
    for f in files:
        p = ROOT / f
        if p.is_file() and p.stat().st_size < 5_000_000:
            try:
                txt = p.read_text(errors="ignore")
            except OSError:
                continue
            assert not pat.search(txt), f"private key material in {f}"


def test_recipients_file_in_the_repo_holds_public_keys_only():
    p = ROOT / "research" / "sealed_ledger" / "recipients.txt"
    assert p.exists()
    for ln in p.read_text().splitlines():
        t = ln.strip()
        assert not t or t.startswith("#") or (t.startswith("age1") and "SECRET" not in t.upper())


def test_registry_note_for_the_sealed_ledger_design_chains():
    from nhl_edge.model_research import registry

    assert registry.verify(ROOT / "docs/research/nhl-model-improvement/experiment_registry.jsonl") == []
