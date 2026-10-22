"""End-to-end exercise of the sealed ledger with SYNTHETIC outcomes and a THROWAWAY key (generated in memory, never written). It never reads the archive, a real store
or the real recipients file, so it can run anywhere (including CI) without touching the prospective tier.

    python -m nhl_edge.sealed_ledger.selftest [--out DIR]

It seals synthetic games whose outcome fields carry unmistakable sentinels, then checks that: (1) no sentinel appears in any published file or in the captured console
output, (2) the store verifies, (3) the throwaway key round-trips every record, (4) tampering, replacement, deletion, truncation, rollback and duplicate ingestion are
detected or refused. Exit code 0 only if every check passes.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import shutil
import sys
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from pyrage import x25519

from nhl_edge.model_research import daily
from nhl_edge.sealed_ledger import checkpoint as CP
from nhl_edge.sealed_ledger.core import ct_path, is_extension, read_manifest, verify_store
from nhl_edge.sealed_ledger.owner import decrypt_entry
from nhl_edge.sealed_ledger.runner import blinded_scorecard
from nhl_edge.sealed_ledger.seal import SealedStore, SealError

SENTINEL = "SYNTHETIC-OUTCOME-SENTINEL"


def synthetic_rows(day: str, start: int, n: int) -> list[dict[str, Any]]:
    rows = []
    for i in range(start, start + n):
        r: dict[str, Any] = {k: None for k in daily.LEDGER_FIELDS}
        r.update({"game_id": f"SYN{i:05d}", "game_date_et": day, "slate_age_min": 20.0 + i, "sb_p_home": 0.5, "v1_p_home_win": 0.51, "v2_p_home_win": 0.52, "c1_p_home_win": 0.5, "y_home_win": i % 2, "y_total": 5 + i % 3,
                  "home_final": 3 + i % 4, "away_final": 2, "attribution_class": "E_normal_variance", "attribution_evidence": f"{SENTINEL}-{i}"})
        rows.append(r)
    return rows


def _files_text(root: Path) -> bytes:
    return b"".join(p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file())


def run(out: Path | None = None) -> list[str]:
    results: list[str] = []

    def check(name: str, cond: bool) -> None:
        results.append(("PASS " if cond else "FAIL ") + name)

    tmp = Path(tempfile.mkdtemp(prefix="sealed_selftest_"))
    try:
        ident = x25519.Identity.generate()  # throwaway, in memory only
        rec = tmp / "recipients.txt"
        rec.write_text(f"# THROWAWAY SELF-TEST KEY\n{ident.to_public()}\n")
        store = tmp / "store"
        console = io.StringIO()
        with contextlib.redirect_stdout(console), contextlib.redirect_stderr(console):
            s = SealedStore(store, rec, run_id="selftest", code_sha="selftest", now=datetime(2026, 10, 22, 12, 0, tzinfo=UTC))
            s.seal_rows(synthetic_rows("2026-10-22", 0, 4))
            s.close_day("2026-10-22", [f"SYN{i:05d}" for i in range(4)], [])
            s.seal_rows(synthetic_rows("2026-10-23", 4, 4))
            s.close_day("2026-10-23", [f"SYN{i:05d}" for i in range(4, 8)], [])
        wit_key = CP.generate_key()
        witnessed = CP.sign(CP.make_checkpoint(read_manifest(store), "WITNESS"), wit_key)
        blob = _files_text(store) + console.getvalue().encode()
        check("no synthetic outcome sentinel in any published file or console output", SENTINEL.encode() not in blob and b"y_home_win" not in blob and b"home_final" not in blob)
        check("store verifies", verify_store(store).ok)
        sc = blinded_scorecard(read_manifest(store))
        check("runner scorecard is blinded (counts + pregame quality only)", set(sc) == {"n_prospective_games", "tier", "looks", "next_look_at_games", "data_quality", "alarms", "status", "note"}
              and sc["n_prospective_games"] == 8 and sc["status"] == "ACCUMULATING_BLINDED")
        ents = [e for e in read_manifest(store) if e["kind"] == "RECORD"]
        check("throwaway key round-trips every record", all(SENTINEL in decrypt_entry(store, e, [ident])["record"]["attribution_evidence"] for e in ents))
        s2 = SealedStore(store, rec)
        before = (store / "manifest.jsonl").read_bytes()
        s2.seal_rows(synthetic_rows("2026-10-22", 0, 4))
        check("duplicate ingestion is a no-op", (store / "manifest.jsonl").read_bytes() == before)
        # tamper / delete / replace / rollback on copies
        for name, mutate in {
            "ciphertext bit flip": lambda r: ct_path(r, 1).write_bytes(ct_path(r, 1).read_bytes()[:-1] + bytes([ct_path(r, 1).read_bytes()[-1] ^ 1])),
            "ciphertext deleted": lambda r: ct_path(r, 2).unlink(),
            "ciphertexts swapped": lambda r: (ct_path(r, 1).write_bytes(ct_path(r, 2).read_bytes())),
            "manifest entry edited": lambda r: (r / "manifest.jsonl").write_text((r / "manifest.jsonl").read_text().replace("SYN00001", "SYN09999", 1)),
            "plaintext file planted": lambda r: (r / "leak.json").write_text("{}"),
        }.items():
            cp = tmp / "mut"
            shutil.rmtree(cp, ignore_errors=True)
            shutil.copytree(store, cp)
            mutate(cp)
            check(f"detected: {name}", not verify_store(cp).ok)
        cp = tmp / "trunc"
        shutil.copytree(store, cp)
        lines = (cp / "manifest.jsonl").read_text().splitlines(keepends=True)
        (cp / "manifest.jsonl").write_text("".join(lines[:-2]))
        for f in (cp / "sealed").iterdir():  # a careful attacker removes the matching ciphertexts too
            if int(f.name[:6]) > len(lines) - 3:
                f.unlink()
        check("truncation passes the chain check by itself (as designed: it needs an external anchor)", verify_store(cp).ok)
        check("... but detected by a witnessed checkpoint", bool(CP.check_against_checkpoints(read_manifest(cp), [witnessed])))
        check("... and by the extension check against the previous copy", bool(is_extension(read_manifest(store), read_manifest(cp))))
        try:
            SealedStore(tmp / "empty", tmp / "none.txt")
            check("sealing with no recipients is refused", False)
        except (SealError, FileNotFoundError):
            check("sealing with no recipients is refused", True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if out is not None:
        out.mkdir(parents=True, exist_ok=True)
        (out / "SEALED_LEDGER_SELFTEST.json").write_text(json.dumps({"synthetic": True, "checks": results, "all_passed": all(r.startswith("PASS") for r in results)}, indent=1))
    return results


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path)
    res = run(ap.parse_args().out)
    print("\n".join(res))
    return 0 if all(r.startswith("PASS") for r in res) else 1


if __name__ == "__main__":
    sys.exit(main())
