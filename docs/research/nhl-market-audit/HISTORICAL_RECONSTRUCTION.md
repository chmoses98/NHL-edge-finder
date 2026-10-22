# Historical reconstruction: method, lineage, point-in-time rules

> RESEARCH ONLY. The archive and the accounting ledger are read-only inputs; nothing here rewrites a source record.

## Pipeline

```
python -m nhl_edge.market_audit.pipeline --archive <data-archive checkout> --accounting <accounting-data checkout> \
    --history data/history --repo . --work <derived dir> --out docs/research/nhl-market-audit/data [--force] [--only step,step]
```

Twenty steps, each resumable and idempotent: a step records a fingerprint (archive manifest digest + ledger digest + the step's own modules + the fingerprints of every earlier step) and is skipped when unchanged, so a re-run after new
captures redoes only what depends on them and a crash resumes at the failed step. `lineage.json` binds every output to the archive manifest SHA-256, the git commit and the package versions; derived parquet tables carry their own SHA-256 (they are
reproducible from the archive bytes and are not committed because of size).

## Reconstructing delta-compressed boards

Reuses `nhl_edge.archive.reconstruct.iter_board_ticks` - the path the production archive already trusts: a full checkpoint, then field-level deltas applied in order. Each delta carries the hash of the board it must produce and the path of the checkpoint it descends from;
any gap, reordering, duplicate or hash mismatch raises (fail-closed). All 128 market chains and 128 order-book chains verify. The reconstructed row of a delta tick equals the real one field-for-field, including the ledger stamps.

`streams.py` turns the 2,870 ticks into change logs (`quote_events`, `book_events`) plus a static contract table. A change log is not a panel: as-of lookups carry the last event forward and bound staleness by the tick table, not by the event time (a quiet market is not stale).

## Four different things, kept apart

| object | source | meaning |
|---|---|---|
| **quote** | board `yes_bid/yes_ask` (cents), `*_size_fp` | the displayed best prices at a tick |
| **liquidity** | order-book ladder (10 levels, 4 families only) | what could be taken at what prices |
| **hypothetical execution** | `execution.walk()` over the ladder + `0.07 p (1-p)` fee | a modelled taker fill |
| **real fill** | accounting-data ledger | what the owner actually paid, with fees |

## Point-in-time rules (enforced in code, covered by assertions)

1. A tick is stamped with the capture START. The market board is fully written ~30-40 s later, the books ~91-100 s later. Every quote carries `available_at = stamp + 45 s` (markets) or `+ 105 s` (books). Nothing is used before it is available.
2. The as-of state is taken from ALL events first, and only then tested for two-sidedness / `active`: a one-sided or inactive state at the cut is a missing quote, never an older two-sided one.
3. The contract must still be on the board at the cut (`last_seen + 45 s >= cut`).
4. Model outputs are the last production rows with `predicted_at <= cut` (asserted); production inputs were verified to equal the archived board (100% of 15,553 sampled rows).
5. No closing price, final score, or post-start quote is ever an input. Settlement outcomes enter only as labels.
6. Tiers are chronological. The LIVE tier is closed at the registry freeze (2026-10-21T17:13:05Z); later games are PROSPECTIVE and read only at predeclared looks.

## Immutability and lineage

* Source: `data-archive` (append-only ledger, 14,214 manifest entries with SHA-256) and `accounting-data` (append-only). Verified, never modified.
* Derived: written only under `--work` and `--out`. A different manifest digest means a different snapshot, and nothing is reused across digests.
* Every output JSON is reproducible by re-running the pipeline against the same two branches at the digest recorded in `data/lineage.json`.

## Known reconstruction limits

* The capture saw only live statuses, so Kalshi's own settlement is absent for live contracts (validated separately on 2025-26 history).
* Quotes between ticks (median 10 min apart) are not observed; the carried-forward state can be up to one cadence stale (max observed gap 55 min; none over an hour).
* Trade tape / fills are not archived, so maker fill probabilities, queue position and market impact cannot be estimated.
* Starting-goalie, lineup and injury information is timestamped by the context snapshot, not by when the market learned it.
