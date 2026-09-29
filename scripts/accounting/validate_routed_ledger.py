#!/usr/bin/env python3
"""Validate the NHL routed-wager ledger. The destination's own verdict on its own data. COUNTS AND REASONS ONLY.

    python scripts/accounting/validate_routed_ledger.py --base-dir <accounting-data checkout> [--against origin/accounting-data]
        [--result-out result.json]

Checks: every line decodes; wager and settlement schemas (incl. no model/recommendation provenance field);
source_bet_key unique in each file; every settlement has its wager with the same ticker and side; with --against
(a git ref in --base-dir), both files are APPEND-ONLY relative to that ref (no line removed or rewritten).

accounting-data carries no .github/, so a pull request into it gets no CI; kalshi-bet-router runs this after its
import and the exit status is the verdict (0 pass, 1 fail, 2 unreadable). Failures name a file and LINE NUMBER and
a reason -- never a ticker, stake, price, contract count, P&L or source_bet_key.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src"))

from nhl_edge.accounting.ledger import SETTLEMENTS_FILE, WAGERS_FILE, validate_ledger  # noqa: E402

EXIT_OK, EXIT_INVALID, EXIT_UNREADABLE = 0, 1, 2


def base_texts(base_dir: str, ref: str) -> dict[str, str]:
    out = {}
    for rel in (WAGERS_FILE, SETTLEMENTS_FILE):
        shown = subprocess.run(["git", "-C", base_dir, "show", f"{ref}:{rel.as_posix()}"], capture_output=True, text=True, check=False)
        out[str(rel)] = shown.stdout if shown.returncode == 0 else ""
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base-dir", required=True)
    ap.add_argument("--against", default=None, help="git ref whose ledger the current files must extend")
    ap.add_argument("--result-out", default=None)
    a = ap.parse_args(argv)
    if not Path(a.base_dir).is_dir():
        print("ledger directory not found", file=sys.stderr)
        return EXIT_UNREADABLE
    if a.against:
        ok = subprocess.run(["git", "-C", a.base_dir, "rev-parse", "--verify", "--quiet", a.against], capture_output=True, check=False)
        if ok.returncode != 0:
            print("the --against ref does not resolve", file=sys.stderr)
            return EXIT_UNREADABLE
    try:
        result = validate_ledger(Path(a.base_dir), base_texts(a.base_dir, a.against) if a.against else None)
    except (OSError, UnicodeDecodeError) as exc:
        print(f"ledger unreadable: {type(exc).__name__}", file=sys.stderr)
        return EXIT_UNREADABLE
    c = result["counts"]
    print(f"wagers: {c['wagers']}  settlements: {c['settlements']}  orphan settlements: {c['orphan_settlements']}")
    print(f"append-only check: {'against ' + a.against if a.against else 'not requested'}")
    print(f"failures: {result['n_failures']}")
    for f in result["failures"][:200]:
        print(f"  {f}")
    if a.result_out:
        Path(a.result_out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return EXIT_OK if result["passed"] else EXIT_INVALID


if __name__ == "__main__":
    raise SystemExit(main())
