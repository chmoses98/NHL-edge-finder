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

import pandas as pd
import pyrage
import pytest
from pyrage import x25519

from nhl_edge.model_research import daily
from nhl_edge.sealed_ledger import audit, owner, protocol_rules_sha256, runner, seal
from nhl_edge.sealed_ledger import checkpoint as CP
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
    for banned in (SENTINEL.encode(), b"y_home_win", b"home_final", b"v1_p_home_win"):  # long tokens only: random ciphertext bytes could contain a 3-4 letter word by chance
        assert banned not in blob
    manifest_text = (st.root / "manifest.jsonl").read_text()
    for banned in ("brier", "pit_", "attribution", "roi", "y_total", "away_final", "home_final", "SYN0000" + "0\"" + ",\"y"):
        assert banned not in manifest_text
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
    for f in (d / "sealed").iterdir():  # a careful attacker removes the matching ciphertexts too
        if int(f.name[:6]) > len(lines) - 4:
            f.unlink()
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
    res = st2.seal_rows(synthetic_rows("2026-10-22", 0, 4) + synthetic_rows("2026-10-24", 20, 2))  # games of a later (not yet closed) day are added; the first four are skipped
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
        st.seal_rows(fixed, correct={"SYN00000": 1})
    with pytest.raises(seal.SealError, match="never sealed"):
        st.seal_rows(fixed, correct={"NOPE": 1}, reason="OTHER_DOCUMENTED")
    with pytest.raises(seal.SealError, match="no re-derived row"):
        st.seal_rows([], correct={"SYN00000": 1}, reason="OTHER_DOCUMENTED")
    assert st.seal_rows(fixed, correct={"SYN00000": 1}, reason="SOURCE_SCORE_REVISED") == {"sealed_new": 0, "skipped_existing": 0, "corrections": 1}
    with pytest.raises(seal.SealError, match="stale correction"):  # repeating the same request (e.g. a workflow re-run) cannot stack versions
        st.seal_rows(fixed, correct={"SYN00000": 1}, reason="SOURCE_SCORE_REVISED")
    assert [e["version"] for e in read_manifest(st.root) if e["kind"] == "RECORD" and e["game_id"] == "SYN00000"] == [1, 2]
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
    assert not verify_store(st.root).ok  # a PUBLISHED orphan is a problem (it cannot be told from plaintext behind a fake header) ...
    rep = verify_store(st.root, allow_orphans=True)  # ... but the runner's own working copy may resume after a crash
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
    owner.witness_keygen(wd, passphrase="correct-horse")
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
    cp = owner.witness(st.root, wd, passphrase="correct-horse")
    assert cp["seq"] == len(st.entries) - 1
    res = owner.take_look(st.root, idf, wd, out)
    assert res["status"] == "AT_LOOK_150" and (out / "LOOK_150.json").exists() and (out / "LOOK_150.provenance.json").exists()
    look = json.loads((out / "LOOK_150.json").read_text())
    assert look["games"] == 150 and "brier" in look
    with pytest.raises(SystemExit, match="already taken"):
        owner.take_look(st.root, idf, wd, out)
    with pytest.raises(SystemExit, match="already taken"):  # a different --out directory is no escape: the marker lives in the witness directory
        owner.take_look(st.root, idf, wd, tmp_path / "elsewhere")


def test_look_refuses_a_rolled_back_ledger_and_a_tampered_one(tmp_path, keys):
    st, idf, wd = _owner_setup(tmp_path, keys, 150)
    owner.witness(st.root, wd, passphrase="correct-horse")
    full = _copy(st, tmp_path, "full")
    st.seal_rows(synthetic_rows("2026-12-01", 500, 3))
    st.close_day("2026-12-01", ["SYN00500", "SYN00501", "SYN00502"], [])
    owner.witness(st.root, wd, passphrase="correct-horse")  # witnessed the longer ledger
    rolled = full  # the shorter, older, internally valid copy
    assert verify_store(rolled).ok
    with pytest.raises(SystemExit, match="TRUNCATED"):
        owner.take_look(rolled, idf, wd, tmp_path / "o1")
    bad = _copy(st, tmp_path, "bad")
    ct_path(bad, 5).write_bytes(ct_path(bad, 5).read_bytes()[:-1] + b"\x01")
    with pytest.raises(SystemExit, match="fails verification"):
        owner.take_look(bad, idf, wd, tmp_path / "o2")


def test_reproduce_diff_flags_forged_extra_and_omitted_records_without_printing_values(tmp_path, keys, monkeypatch):
    a, _b, rec = keys
    st = seal.SealedStore(tmp_path / "s", rec, now=T0)
    real = synthetic_rows("2026-11-01", 0, 3)
    forged = [dict(r) for r in real]
    forged[1]["home_final"] = 8  # the sealed copy of game 1 was forged
    st.seal_rows(forged[:2])  # and game 2 was omitted
    st.close_day("2026-11-01", ["SYN00000", "SYN00001"], [])
    st.seal_rows(synthetic_rows("2026-11-01", 90, 1))  # an extra id on a closed day, appended later
    monkeypatch.setattr(daily, "build_rows", lambda *a, **k: (real, {}))
    diffs = owner.reproduce_diff(st.root, [a], tmp_path, tmp_path)
    assert diffs == ["SYN00090: sealed for 2026-11-01 but not derivable from the archive (extra or forged id)",
                     "SYN00002: derivable from the archive but NOT in the ledger (omitted)", "SYN00001: field home_final differs (version 1)"]
    assert owner.reproduce_diff(make_store(tmp_path, keys, name="ok", days=(("2026-11-01", 0, 3),)).root, [a], tmp_path, tmp_path) == []


def test_a_forged_correction_and_forged_extra_games_are_caught_and_never_count_toward_the_threshold(tmp_path, keys, monkeypatch):
    a, _b, rec = keys
    st = seal.SealedStore(tmp_path / "s", rec, now=T0)
    real = synthetic_rows("2026-11-01", 0, 4)
    st.seal_rows(real)
    st.close_day("2026-11-01", [r["game_id"] for r in real], [])
    assert verify_store(st.root).n_games_closed == 4
    flipped = dict(real[1])
    flipped["home_final"] = 9
    # an attacker with write access (the public key is public) appends a forged v2 and extra games for a real date and for an unclosed date
    seal.SealedStore(st.root, rec, now=T0).seal_rows([flipped], correct={"SYN00001": 1}, reason="OTHER_DOCUMENTED")
    seal.SealedStore(st.root, rec, now=T0).seal_rows(synthetic_rows("2026-11-02", 70, 5))
    rep = verify_store(st.root)
    assert rep.ok and rep.n_games == 9 and rep.n_games_closed == 4 and rep.n_corrections == 1  # structurally valid, but only the 4 closed games count
    assert runner.blinded_scorecard(read_manifest(st.root))["n_prospective_games"] == 4
    monkeypatch.setattr(daily, "build_rows", lambda archive, day, *x, **k: (real if day == "2026-11-01" else [], {}))
    diffs = owner.reproduce_diff(st.root, [a], tmp_path, tmp_path)
    assert "SYN00001: field home_final differs (version 2)" in diffs and sum("not derivable" in d for d in diffs) == 5
    rows, meta = owner.latest_rows(st.root, [a])
    assert len(rows) == 4 and meta["n_games"] == 4  # forged extras never enter a look
    # a record that appears for a day that was ALREADY closed is a structural error
    seal.SealedStore(st.root, rec, now=T0).seal_rows(synthetic_rows("2026-11-01", 80, 1))
    assert any("after its day" in p or "does not list exactly" in p for p in verify_store(st.root).problems)


def test_verify_all_with_witness_and_previous_copy(tmp_path, keys):
    st, _idf, wd = _owner_setup(tmp_path, keys, 20)
    owner.witness(st.root, wd, passphrase="correct-horse")
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
    monkeypatch.setattr(audit, "open_days_before", lambda *a, **k: [])  # the completeness audit has its own tests (it needs a real archive)


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
    assert runner.main(["init", "--store", str(tmp_path / "store"), "--recipients", str(rec)]) == 0  # a ledger exists only after the owner-verified init
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
    assert runner.blinded_scorecard(st.entries)["n_prospective_games"] == 0  # records of a day nobody closed do not count
    st.close_day("2026-11-01", [r["game_id"] for r in rows], [])
    mine = runner.blinded_scorecard(st.entries)
    ref = daily.scorecard([{**r, "y_home_win": 1} for r in rows])
    assert set(mine) == set(ref) and mine["status"] == ref["status"] == "ACCUMULATING_BLINDED" and mine["n_prospective_games"] == 10
    assert mine["data_quality"]["missing_sportsbook_share"] == ref["data_quality"]["missing_sportsbook_share"] == 0.1
    assert mine["data_quality"]["mean_slate_age_min"] == pytest.approx(ref["data_quality"]["mean_slate_age_min"])
    big = seal.SealedStore(tmp_path / "b", rec, now=T0)
    for i in range(0, 150, 15):
        rws = synthetic_rows(f"2026-12-{1 + i // 15:02d}", i, 15)
        big.seal_rows(rws)
        big.close_day(rws[0]["game_date_et"], [r["game_id"] for r in rws], [])
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


# ---------------------------------------------------------------- review hardening ---------------------------------------------------------------------

def test_verify_rejects_hidden_channels_in_the_published_tree(tmp_path, keys):
    st = make_store(tmp_path, keys)
    lines = (st.root / "manifest.jsonl").read_text().splitlines()
    cases = {
        "workflow_file": lambda r: ((r / ".github" / "workflows").mkdir(parents=True), (r / ".github" / "workflows" / "x.yml").write_text("on: push")),
        "dotfile": lambda r: (r / ".gitattributes").write_text("x"),
        "readme": lambda r: (r / "README.md").write_text("home_final=3"),
        "plaintext_orphan": lambda r: (r / "sealed" / "000099.age").write_text("home_final=3 plaintext"),
        "fake_header_orphan": lambda r: (r / "sealed" / "000098.age").write_bytes(b"age-encryption.org/v1\n" + b"x" * 4500),
        "extra_manifest_field": lambda r: (r / "manifest.jsonl").write_text("\n".join([lines[0], lines[1][:-1] + ',"leak":"home_final=3"}'] + lines[2:]) + "\n"),
        "non_canonical_json": lambda r: (r / "manifest.jsonl").write_text("\n".join([lines[0], json.dumps(json.loads(lines[1]), indent=1).replace("\n", " ")] + lines[2:]) + "\n"),
        "blank_line": lambda r: (r / "manifest.jsonl").write_text(lines[0] + "\n\n" + "\n".join(lines[1:]) + "\n"),
        "junk_checkpoint": lambda r: ((r / "checkpoints").mkdir(), (r / "checkpoints" / "runner_000001.json").write_text('{"x": "home_final=3"}')),
        "wrongly_named_checkpoint": lambda r: ((r / "checkpoints").mkdir(), (r / "checkpoints" / "notes.json").write_text("{}")),
    }
    for name, mut in cases.items():
        d = _copy(st, tmp_path, name)
        mut(d)
        assert not verify_store(d).ok, name
    (st.root / ".git").mkdir()  # a bare .git (the store as a working tree) is the one allowed dotfile
    assert verify_store(st.root).ok


def test_workflows_pass_previous_strictly_and_close_day_refuses_a_suspicious_archive(tmp_path, keys, monkeypatch, capsys):
    _a, _b, rec = keys
    st = make_store(tmp_path, keys)
    assert runner.main(["verify", "--store", str(st.root), "--recipients", str(rec), "--previous", str(tmp_path / "typo")]) == 1  # a typo can no longer disable the check
    empty = tmp_path / "empty_prev"
    empty.mkdir()
    assert runner.main(["verify", "--store", str(st.root), "--recipients", str(rec), "--previous", str(empty)]) == 0  # first publish: previous exists and is empty
    rows = synthetic_rows("2026-10-30", 40, 2)
    _fake_build_rows(monkeypatch, rows, scheduled=["SYN00040", "SYN00041"], missing=["SYN00040", "SYN00041"])
    monkeypatch.setitem(__import__("sys").modules["nhl_edge.model_research.daily"].__dict__, "build_rows", lambda *a, **k: (rows[:0], {
        "date": "2026-10-30", "games_scheduled": 2, "games_final": 2, "scheduled_game_ids": ["SYN00040", "SYN00041"], "all_scheduled_final": True,
        "games_with_pregame_forecast": 0, "missing_pregame_forecast": ["SYN00040", "SYN00041"], "reproduction_max_abs_diff": None}))
    runner.run_init(tmp_path / "s2", rec)
    res = runner.run_ingest(tmp_path / "a", "2026-10-30", Path("."), tmp_path / "s2", rec, seal=True, correct={}, reason=None)
    assert res["day_closed"] is False and "NOT closed" in res["note"]


def test_look_takes_the_smallest_untaken_level_on_exactly_the_first_k_games_and_each_look_once(tmp_path, keys):
    st, idf, wd = _owner_setup(tmp_path, keys, 300)
    owner.witness(st.root, wd, passphrase="correct-horse")
    out = tmp_path / "looks"
    r1 = owner.take_look(st.root, idf, wd, out)
    assert r1["provenance"]["look"] == 150 and json.loads((out / "LOOK_150.json").read_text())["games"] == 150  # a late first look is still the preregistered 150-game look
    r2 = owner.take_look(st.root, idf, wd, tmp_path / "other")
    assert r2["provenance"]["look"] == 300 and json.loads((tmp_path / "other" / "LOOK_300.json").read_text())["games"] == 300
    with pytest.raises(SystemExit, match="already taken"):
        owner.take_look(st.root, idf, wd, tmp_path / "third")


def test_witness_log_head_detects_removal_of_the_last_lines_and_recipients_are_checked(tmp_path, keys):
    st, _idf, wd = _owner_setup(tmp_path, keys, 20)
    c1 = owner.witness(st.root, wd, passphrase="correct-horse", recipients=keys[2])
    st.seal_rows(synthetic_rows("2026-12-20", 300, 2))
    st.close_day("2026-12-20", ["SYN00300", "SYN00301"], [])
    c2 = owner.witness(st.root, wd, passphrase="correct-horse", recipients=keys[2])
    assert c2["witness_entries"] == 2 and owner.verify_all(st.root, wd, keys[2], None, c2["witness_log_head"])["ok"]
    log = wd / "witness.jsonl"
    log.write_text(log.read_text().splitlines(keepends=True)[0])  # the owner's log loses its last line: still chains and still signs ...
    assert CP.witness_read(log, CP.load_public((wd / "witness_public.pem").read_bytes()))[1] == []
    res = owner.verify_all(st.root, wd, keys[2], None, c2["witness_log_head"])  # ... but the head recorded elsewhere exposes it
    assert not res["ok"] and any("witness log head" in p for p in res["problems"])
    assert c1["witness_entries"] == 1
    other = tmp_path / "other_recipients.txt"
    other.write_text(f"{x25519.Identity.generate().to_public()}\n")
    with pytest.raises(SystemExit, match="recipients"):
        owner.witness(st.root, wd, passphrase="correct-horse", recipients=other)  # a ledger encrypted to someone else's key cannot be witnessed
    idf = tmp_path / "id2.txt"
    idf.write_text(f"{keys[0]}\n")


def test_empty_witness_passphrase_and_duplicate_recipients_and_torn_genesis(tmp_path, keys):
    with pytest.raises(SystemExit, match="at least 8"):
        owner.witness_keygen(tmp_path / "w", passphrase="")
    with pytest.raises(ValueError, match="unencrypted"):
        CP.private_pem(CP.generate_key(), b"")
    a, _b, _rec = keys
    dup = tmp_path / "dup.txt"
    dup.write_text(f"{a.to_public()}\n{a.to_public()}\n")
    with pytest.raises(seal.SealError, match="more than once"):
        seal.load_recipients(dup)
    rec = keys[2]
    st = seal.SealedStore(tmp_path / "g", rec, now=T0)
    (st.root / "manifest.jsonl").write_bytes((st.root / "manifest.jsonl").read_bytes()[:40])  # crash while writing the genesis line
    with pytest.raises(seal.SealError):
        seal.SealedStore(st.root, rec, now=T0)
    st2 = seal.SealedStore(st.root, rec, now=T0, repair_torn_tail=True)
    assert st2.seal_rows(synthetic_rows("2026-11-01", 0, 1))["sealed_new"] == 1 and verify_store(st.root).ok


def test_correction_syntax_names_the_version_being_superseded():
    assert runner._corrections("A1@1, B2@3") == {"A1": 1, "B2": 3}
    for bad in ("A1", "A1@0", "A1@x", "bad id@1", "A1@1@2"):
        with pytest.raises(SystemExit):
            runner._corrections(bad)


# ---------------------------------------------------------------- completeness audit ---------------------------------------------------------------------

def _games(spec):
    """spec: list of (game_id, date, start_utc, final, first_start_utc|None)."""
    return pd.DataFrame([{"game_id": g, "game_date_et": d, "season_type": "regular", "start_time_utc": pd.Timestamp(st, tz="UTC"), "is_final": fin,
                          "first_start_seen": pd.Timestamp(fs or st, tz="UTC")} for g, d, st, fin, fs in spec])


def _results(rows):
    return pd.DataFrame(rows, columns=["game_id", "_observed_at_utc", "home_final", "away_final", "last_period_type", "_file"])


NOW = datetime(2026, 11, 5, 12, 0, tzinfo=UTC)


def test_audit_accepts_a_clean_closed_history(tmp_path, keys):
    st = seal.SealedStore(tmp_path / "s", keys[2], now=T0)
    for day, ids in (("2026-10-21", ["A1", "A2"]), ("2026-10-22", ["B1"])):
        st.seal_rows([r for i, g in enumerate(ids) for r in synthetic_rows(day, 0, 1) if not r.update({"game_id": g})])
        st.close_day(day, ids, [])
    g = _games([("A1", "2026-10-21", "2026-10-21T23:00:00", True, None), ("A2", "2026-10-21", "2026-10-21T23:30:00", True, None), ("B1", "2026-10-22", "2026-10-22T23:00:00", True, None)])
    rep = audit.schedule_audit(tmp_path, "2026-10-22", store=st.root, now=NOW, games=g, results=_results([]))
    assert rep["ok"] and rep["dates"]["2026-10-21"] == {"scheduled": 2, "final": 2, "overdue_not_final": [], "closed": True}


def test_audit_flags_skipped_incomplete_drifted_extra_unsealed_boundary_and_orphan_results(tmp_path, keys):
    st = seal.SealedStore(tmp_path / "s", keys[2], now=T0)
    rows = synthetic_rows("2026-10-21", 0, 2)
    rows[0]["game_id"], rows[1]["game_id"] = "A1", "A2"
    st.seal_rows(rows)
    st.close_day("2026-10-21", ["A1", "A2"], [])
    extra = synthetic_rows("2026-10-21", 9, 1)
    extra[0]["game_id"] = "ZZ9"
    seal.SealedStore(st.root, keys[2], now=T0).seal_rows(extra)  # a forged extra id, after the day closed
    g = _games([("A1", "2026-10-21", "2026-10-21T23:00:00", True, None), ("A2", "2026-10-21", "2026-10-21T23:30:00", True, None),
                ("A3", "2026-10-21", "2026-10-21T23:45:00", True, None),  # added to a CLOSED day -> drift
                ("C1", "2026-10-23", "2026-10-23T23:00:00", True, None),  # a past date nobody closed -> open day
                ("D1", "2026-10-24", "2026-10-24T23:00:00", False, None),  # long overdue, not final -> incomplete
                ("E1", "2026-10-25", "2026-10-25T23:00:00", True, "2026-10-20T23:00:00")])  # start moved across the freeze
    res = _results([("Q9", "2026-10-26T01:00:00Z", 1, 2, "REG", "results/dt=2026-10-24/x.jsonl.gz")])  # a played game the schedule never listed
    rep = audit.schedule_audit(tmp_path, "2026-10-25", store=st.root, now=NOW, games=g, results=res)
    text = " | ".join(rep["problems"])
    for tag in ("OPEN DAY 2026-10-23", "INCOMPLETE 2026-10-24", "DRIFT 2026-10-21", "EXTRA 2026-10-21", "BOUNDARY", "ORPHAN RESULT"):
        assert tag in text, tag
    assert not rep["ok"]
    # a final scheduled game that was neither sealed nor declared missing
    g2 = _games([("A1", "2026-10-21", "2026-10-21T23:00:00", True, None), ("A2", "2026-10-21", "2026-10-21T23:30:00", True, None)])
    st2 = seal.SealedStore(tmp_path / "s2", keys[2], now=T0)
    r2 = synthetic_rows("2026-10-21", 0, 1)
    r2[0]["game_id"] = "A1"
    st2.seal_rows(r2)
    st2._seal_one  # noqa: B018 - the public API refuses to close an unaccounted day, so build the inconsistent DAY by hand
    from nhl_edge.sealed_ledger.core import canon, finish_entry

    day = finish_entry({"v": 1, "seq": len(st2.entries), "kind": "DAY", "game_date_et": "2026-10-21", "scheduled_game_ids": ["A1", "A2"], "sealed_game_ids": ["A1"],
                        "missing_pregame_game_ids": [], "sealed_utc": "2026-10-22T00:00:00Z", "run_id": "", "code_sha": "", "prev_hash": st2.entries[-1]["entry_hash"]})
    with (st2.root / "manifest.jsonl").open("ab") as fh:
        fh.write(canon(day) + b"\n")
    rep2 = audit.schedule_audit(tmp_path, "2026-10-21", store=st2.root, now=NOW, games=g2, results=_results([]))
    assert any(p.startswith("UNSEALED 2026-10-21") for p in rep2["problems"])


def test_a_late_source_revision_of_a_sealed_game_cannot_be_absorbed_silently(tmp_path, keys):
    st = seal.SealedStore(tmp_path / "s", keys[2], now=datetime(2026, 10, 22, 6, 0, tzinfo=UTC))
    rows = synthetic_rows("2026-10-21", 0, 1)
    rows[0]["game_id"] = "A1"
    st.seal_rows(rows)
    st.close_day("2026-10-21", ["A1"], [])
    g = _games([("A1", "2026-10-21", "2026-10-21T23:00:00", True, None)])
    same = _results([("A1", "2026-10-22T05:00:00Z", 3, 2, "REG", "results/dt=2026-10-22/a"), ("A1", "2026-10-22T09:00:00Z", 3, 2, "REG", "results/dt=2026-10-22/b")])
    assert audit.schedule_audit(tmp_path, "2026-10-21", store=st.root, now=NOW, games=g, results=same)["ok"]  # re-observed, unchanged: fine
    revised = _results([("A1", "2026-10-22T05:00:00Z", 3, 2, "REG", "results/dt=2026-10-22/a"), ("A1", "2026-10-22T09:00:00Z", 4, 2, "REG", "results/dt=2026-10-22/b")])
    rep = audit.schedule_audit(tmp_path, "2026-10-21", store=st.root, now=NOW, games=g, results=revised)
    assert not rep["ok"] and any(p.startswith("RESULT REVISED A1") for p in rep["problems"])
    fixed = seal.SealedStore(st.root, keys[2], now=datetime(2026, 10, 22, 10, 0, tzinfo=UTC))  # an explicit, versioned correction resolves it (and is visible)
    fixed.seal_rows(rows, correct={"A1": 1}, reason="SOURCE_SCORE_REVISED")
    assert audit.schedule_audit(tmp_path, "2026-10-21", store=st.root, now=NOW, games=g, results=revised)["ok"]
    # the runner can never overwrite: re-ingesting the same game after the revision is a skip, not a replacement
    assert seal.SealedStore(st.root, keys[2]).seal_rows(rows)["skipped_existing"] == 1


def test_sealing_fails_closed_when_an_earlier_day_is_not_cleanly_closed(tmp_path, keys, monkeypatch):
    _a, _b, rec = keys
    runner.run_init(tmp_path / "s", rec)
    _fake_build_rows(monkeypatch, synthetic_rows("2026-10-22", 0, 2))
    monkeypatch.setattr(audit, "open_days_before", lambda *a, **k: ["OPEN DAY 2026-10-21: 2 scheduled game(s) and no DAY entry (a skipped or incomplete day)"])
    with pytest.raises(seal.SealError, match="not cleanly closed"):
        runner.run_ingest(tmp_path / "a", "2026-10-22", Path("."), tmp_path / "s", rec, seal=True, correct={}, reason=None)
    assert [e["kind"] for e in read_manifest(tmp_path / "s")] == ["GENESIS"]  # nothing sealed
    monkeypatch.undo()
    # the real function: the first prospective date has no predecessor; the next date needs the first one closed
    g = _games([("A1", "2026-10-21", "2026-10-21T23:00:00", True, None), ("B1", "2026-10-22", "2026-10-22T23:00:00", True, None)])
    assert audit.open_days_before(tmp_path, "2026-10-21", tmp_path / "s", now=NOW, games=g) == []
    assert any(p.startswith("OPEN DAY 2026-10-21") for p in audit.open_days_before(tmp_path, "2026-10-22", tmp_path / "s", now=NOW, games=g))


def test_a_ledger_cannot_be_created_by_ingest_only_by_init_and_init_refuses_an_existing_one(tmp_path, keys):
    _a, _b, rec = keys
    with pytest.raises(seal.SealError, match="not initialised"):
        seal.SealedStore(tmp_path / "x", rec, create=False)
    res = runner.run_init(tmp_path / "s", rec)
    assert res["initialised"] and res["manifest_entries"] == 1 and res["genesis_hash"] == res["head_hash"] and not (tmp_path / "x").exists()
    with pytest.raises(seal.SealError, match="already exists"):
        runner.run_init(tmp_path / "s", rec)


# ---------------------------------------------------------------- backup/recovery drill and first checkpoint ------------------------------------------------

def test_primary_and_backup_independently_open_the_real_canary_and_every_record(tmp_path, keys):
    a, b, rec = keys
    st = make_store(tmp_path, keys)
    for ident in (a, b):  # each identity ALONE
        assert "SYNTHETIC CANARY" in owner.decrypt_canary(st.root, [ident])["text"]
        rows = [owner.decrypt_entry(st.root, e, [ident])["record"] for e in st.entries if e["kind"] == "RECORD"]
        assert len(rows) == 8 and all(SENTINEL in r["attribution_evidence"] for r in rows)
    ida, idb = tmp_path / "primary.txt", tmp_path / "backup.txt"
    ida.write_text(f"{a}\n")
    idb.write_text(f"{b}\n")
    res = owner.drill(st.root, [ida, idb], rec)
    assert res["all_identities_open_the_ledger"] and res["warning"] is None
    stranger = tmp_path / "stranger.txt"
    stranger.write_text(f"{x25519.Identity.generate()}\n")
    bad = owner.drill(st.root, [ida, stranger], rec)
    assert not bad["all_identities_open_the_ledger"] and [r["opens_this_ledger"] for r in bad["results"]] == [True, False]
    assert owner.drill(st.root, [ida], rec)["warning"]


def test_recovery_drill_from_a_passphrase_protected_backup_and_with_the_reference_age_tool(tmp_path, keys):
    import shutil as _sh
    import subprocess as _sp

    from pyrage import passphrase as pw

    a, b, rec = keys
    st = make_store(tmp_path, keys)
    backup = tmp_path / "backup-identity.txt.age"  # what `age -p -o backup-identity.txt.age backup-identity.txt` produces
    backup.write_bytes(pw.encrypt(f"# public key: {b.to_public()}\n{b}\n".encode(), "a long backup passphrase"))
    assert "SYNTHETIC CANARY" in owner.decrypt_canary(st.root, owner.load_identities(backup, "a long backup passphrase"))["text"]
    with pytest.raises(pyrage_errors()):
        owner.load_identities(backup, "wrong passphrase")
    age = _sh.which("age")
    if age:  # interoperability with the reference implementation: no code of ours is needed to recover
        ident = tmp_path / "ref-identity.txt"
        ident.write_text(f"{a}\n")
        out = _sp.run([age, "-d", "-i", str(ident), str(ct_path(st.root, 0))], capture_output=True, check=True).stdout
        assert b"SYNTHETIC CANARY" in out
        rec_out = _sp.run([age, "-d", "-i", str(ident), str(ct_path(st.root, 1))], capture_output=True, check=True).stdout
        assert SENTINEL.encode() in rec_out


def pyrage_errors():
    return pyrage.DecryptError


def test_first_checkpoint_is_only_for_the_fresh_ledger_and_registers_a_genesis_the_workflow_can_check(tmp_path, keys):
    a, b, rec = keys
    res = runner.run_init(tmp_path / "ledger", rec)
    ida, idb = tmp_path / "primary.txt", tmp_path / "backup.txt"
    ida.write_text(f"{a}\n")
    idb.write_text(f"{b}\n")
    wd = tmp_path / "witness"
    owner.witness_keygen(wd, passphrase="correct-horse")
    fc = owner.first_checkpoint(tmp_path / "ledger", [ida, idb], wd, rec, passphrase="correct-horse")
    assert fc["genesis_hash"] == res["genesis_hash"] == fc["head_hash"] and fc["drill"]["all_identities_open_the_ledger"] and fc["witness_log_head"]
    assert owner.verify_all(tmp_path / "ledger", wd, rec, None, fc["witness_log_head"], fc["genesis_hash"])["ok"]
    assert not owner.verify_all(tmp_path / "ledger", wd, rec, None, None, "0" * 64)["ok"]  # a different genesis = a replaced ledger
    # an independent, stdlib-only recomputation of the genesis hash (the recipe in the owner checklist) agrees
    import hashlib
    import json as _json

    entry = _json.loads((tmp_path / "ledger" / "manifest.jsonl").read_text().splitlines()[0])
    body = {k: v for k, v in entry.items() if k != "entry_hash"}
    canon_bytes = _json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False).encode()
    assert hashlib.sha256(b"sift-sealed-ledger/v1/entry\n" + canon_bytes).hexdigest() == fc["genesis_hash"]
    # a ledger that already holds games is not a "first checkpoint"
    st = seal.SealedStore(tmp_path / "ledger", rec, now=T0)
    st.seal_rows(synthetic_rows("2026-11-01", 0, 1))
    with pytest.raises(SystemExit, match="only for the freshly initialised"):
        owner.first_checkpoint(tmp_path / "ledger", [ida, idb], wd, rec, passphrase="correct-horse")
    # a stranger key blocks the checkpoint
    bad = tmp_path / "stranger.txt"
    bad.write_text(f"{x25519.Identity.generate()}\n")
    runner.run_init(tmp_path / "ledger2", rec)
    with pytest.raises(SystemExit, match="cannot open the ledger"):
        owner.first_checkpoint(tmp_path / "ledger2", [ida, bad], wd, rec, passphrase="correct-horse")


def test_verify_expect_genesis_hash_refuses_a_different_ledger(tmp_path, keys, capsys):
    _a, _b, rec = keys
    one = runner.run_init(tmp_path / "one", rec)
    runner.run_init(tmp_path / "two", rec)
    assert runner.main(["verify", "--store", str(tmp_path / "one"), "--recipients", str(rec), "--expect-genesis-hash", one["genesis_hash"]]) == 0
    assert runner.main(["verify", "--store", str(tmp_path / "two"), "--recipients", str(rec), "--expect-genesis-hash", one["genesis_hash"]]) == 1
    assert not tmp_path.joinpath("one", "sealed", "000001.age").exists()  # init seals no game


def test_a_tampered_or_missing_canary_is_detected(tmp_path, keys):
    _a, _b, rec = keys
    runner.run_init(tmp_path / "s", rec)
    d1 = tmp_path / "c1"
    shutil.copytree(tmp_path / "s", d1)
    ct_path(d1, 0).write_bytes(ct_path(d1, 0).read_bytes()[:-1] + b"\x00")
    assert not verify_store(d1).ok
    d2 = tmp_path / "c2"
    shutil.copytree(tmp_path / "s", d2)
    ct_path(d2, 0).unlink()
    assert any("canary" in p for p in verify_store(d2).problems)


def test_unexpected_exceptions_print_only_their_type(tmp_path, keys, monkeypatch, capsys):
    import runpy

    _a, _b, rec = keys
    runner.run_init(tmp_path / "s", rec)

    def boom(*a, **k):
        raise ValueError("home_final=7 row=SYN-LEAK-SENTINEL")

    monkeypatch.setattr(daily, "build_rows", boom)
    monkeypatch.setattr("sys.argv", ["runner", "ingest", "--archive", str(tmp_path), "--date", "2026-10-22", "--store", str(tmp_path / "s"), "--recipients", str(rec), "--seal"])
    with pytest.raises(SystemExit) as ei:
        runpy.run_module("nhl_edge.sealed_ledger.runner", run_name="__main__")
    err = capsys.readouterr()
    assert ei.value.code == 4 and "ValueError" in err.err and "SYN-LEAK-SENTINEL" not in err.out + err.err and "home_final" not in err.out + err.err
