#!/usr/bin/env python3
"""Import a kalshi-bet-router NHL wager payload into data/accounting/wagers.jsonl. COUNTS ONLY.

    python scripts/accounting/import_routed_wagers.py --payload NHL.json --base-dir <accounting-data checkout> \
        --receipts-out receipts.json

The payload is the router's envelope ``{"importBatchId": ..., "rows": [...]}`` built by ``to_nhl_import_row``.
Identity (``wager_id``) is minted here from ``source_bet_key``; an identical re-delivery is DUPLICATE_NOOP and changes
zero bytes; a re-delivery with different economics is CONFLICT and exits 1 so the router's merge gate fails.

This repository's Actions logs are public: stdout carries counts and refusal REASONS by row position, never a
ticker, price, stake, contract count or key. Per-row receipts (source key + minted id + verdict) go only to the
--receipts-out file the router's gate reads.

Recording is not endorsing: a row says the owner placed an NHL bet. The NHL model (RESEARCH_ONLY) is not involved.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src"))

from nhl_edge.accounting.ledger import RowRefused, import_wagers  # noqa: E402

EXIT_OK, EXIT_REFUSED, EXIT_BAD_INPUT = 0, 1, 2


def read_payload(path: str) -> tuple[str, list]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("payload is not an object")
    batch = payload.get("importBatchId")
    if not isinstance(batch, str) or not batch.strip():
        raise ValueError("payload carries no importBatchId")
    rows = payload.get("rows")
    if not isinstance(rows, list):
        raise ValueError("payload carries no rows list")
    return batch, rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--payload", required=True)
    ap.add_argument("--base-dir", required=True, help="a checkout of the accounting-data branch")
    ap.add_argument("--receipts-out", default=None)
    a = ap.parse_args(argv)
    try:
        batch, rows = read_payload(a.payload)
        result = import_wagers(Path(a.base_dir), rows, import_batch_id=batch)
    except (OSError, ValueError, RowRefused) as exc:
        print(f"unreadable payload or ledger: {type(exc).__name__}", file=sys.stderr)
        return EXIT_BAD_INPUT
    print(f"rows in payload: {len(rows)}")
    print(f"  written:         {result.written}")
    print(f"  already present: {result.duplicate}")
    print(f"  refused:         {result.refused}")
    for r in result.rows:
        if not r["success"]:
            fields = f" fields={r['conflicting_fields']}" if r.get("conflicting_fields") else ""
            print(f"    row {r['row']}: {r['status']}: {r.get('reason')}{fields}")
    if a.receipts_out:
        Path(a.receipts_out).write_text(json.dumps(result.receipts("wagers") | {"importBatchId": batch}, indent=2, sort_keys=True) + "\n")
    return EXIT_REFUSED if result.conflicted else EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
