#!/usr/bin/env python3
"""Import a kalshi-bet-router NHL settlement payload into data/accounting/settlements.jsonl. COUNTS ONLY.

    python scripts/accounting/import_routed_settlements.py --payload NHL-settlements.json --base-dir <accounting-data> \
        --receipts-out receipts.json

Payload: ``{"settlements": [...]}`` rows under router-settlement-economics.v2 (the only version accepted). A
settlement whose ``source_bet_key`` is not on the NHL wager ledger is refused as ORPHAN. An identical repeat is
DUPLICATE_NOOP (zero bytes change); a different settlement for an already-settled wager is CONFLICT; either refusal
exits 1. stdout never carries a ticker, payout, P&L or key.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src"))

from nhl_edge.accounting.ledger import RowRefused, import_settlements  # noqa: E402

EXIT_OK, EXIT_REFUSED, EXIT_BAD_INPUT = 0, 1, 2


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--payload", required=True)
    ap.add_argument("--base-dir", required=True, help="a checkout of the accounting-data branch")
    ap.add_argument("--receipts-out", default=None)
    a = ap.parse_args(argv)
    try:
        payload = json.loads(Path(a.payload).read_text(encoding="utf-8"))
        rows = payload.get("settlements") if isinstance(payload, dict) else None
        if not isinstance(rows, list):
            raise ValueError("payload carries no settlements list")
        result = import_settlements(Path(a.base_dir), rows)
    except (OSError, ValueError, RowRefused) as exc:
        print(f"unreadable payload or ledger: {type(exc).__name__}", file=sys.stderr)
        return EXIT_BAD_INPUT
    print(f"settlements in payload: {len(rows)}")
    print(f"  written:         {result.written}")
    print(f"  already present: {result.duplicate}")
    print(f"  refused:         {result.refused}")
    for r in result.rows:
        if not r["success"]:
            fields = f" fields={r['conflicting_fields']}" if r.get("conflicting_fields") else ""
            print(f"    row {r['row']}: {r['status']}: {r.get('reason')}{fields}")
    if a.receipts_out:
        Path(a.receipts_out).write_text(json.dumps(result.receipts("settlements"), indent=2, sort_keys=True) + "\n")
    return EXIT_REFUSED if result.conflicted else EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
