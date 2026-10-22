# Automated research and monitoring plan (Phase J)

> Implemented but **disabled by default**: `.github/workflows/market_audit.yml` has `workflow_dispatch` only; the daily schedule is commented out and needs an explicit decision.

## What runs

| stage | module | bounded / idempotent / resumable |
|---|---|---|
| ingest new captures, reconstruct boards | `pipeline` -> `streams` | reads a COPY of `data-archive`; steps skip when the manifest digest and their modules are unchanged |
| update market / outcome joins, settle research decisions | `tables` (taxonomy -> outcomes) | pure functions; same inputs, same outputs |
| track routed wagers separately | `wagers`, `case_oct20` | accounting-data ledger only; cross-checks each settlement against the independent resolver |
| prediction calibration vs market | `model_audit` | same games/instant for every forecaster |
| strategy performance | `registry` (frozen hypotheses), `thesis_replay`, `shadow` | one decision horizon; LIVE tier closed, PROSPECTIVE read at fixed looks |
| data-quality / degradation alarms | `quality`, `scorecard.alarms` | CRITICAL on ledger-integrity, broken chains, resolver-vs-production or ledger-vs-resolver disagreement |
| daily scorecard + evidence ledger | `scorecard` | one JSONL line per distinct archive snapshot; re-running appends nothing |

## Five groups, never mixed

`ACTUAL_WAGERS` (real fills), `MODEL_RESEARCH_SELECTIONS` (thesis workflow, research stakes), `INDEPENDENT_HANDICAPPING` (**not measurable** - the ledger has no provenance field), `BACKTEST_SELECTIONS` (frozen registry on HIST and the one-shot LIVE tier), `PROSPECTIVE_SHADOW` (games that started after the registry freeze). The scorecard has no cross-group total by construction (tested).

## Cost control

* Runtime ~25 minutes cold (the 5-minute streaming step and a 4-minute integrity pass dominate), a few minutes warm. One run a day is ~25 Actions-minutes; weekly is plenty while the sample is this small.
* The workflow checks out the code, fetches `data-archive` / `accounting-data` at depth 1 and extracts them to the runner's disk (about 1 GB of content). No paid vendor, no new dependency beyond scipy and statsmodels (research extras).
* Archive growth: **zero**. Large derived tables stay on the runner or in a 14-day artifact; the only persisted output is one ~2 KB line per day on the orphan `market-audit-ledger` branch, written only when `publish=true`. It never writes to `main`, `data-archive` or `accounting-data`.

## Prospective protocol (the only route to a VALIDATED claim)

* Freeze: registry `nhl-hypotheses-1.0` at 2026-10-21T17:13:05Z. Games that START after it are PROSPECTIVE.
* Looks at 150 / 300 / 450 independent games; one-sided alpha spent 0.005 / 0.015 / 0.05; BH across the family at each look. Between looks the scorecard reports counts only and flags `ACCUMULATING`.
* A changed idea is a NEW id registered before it sees data. The LIVE window (2026-09-29..10-20) is spent: it is never re-tested for a modified hypothesis.

## Alarms and who acts

CRITICAL (integrity, resolver disagreement): fix before trusting any number. WARN (capture gap > 60 min, unproven contract semantics, reconciliation failure): investigate. INFO (new unmapped season series): decide whether to add an ontology entry. The scorecard writes them at the top of `SCORECARD.md`.

## Recommended capture changes (NOT applied - production capture code is outside this research PR)

1. Record settled `result` for live contracts (a periodic `finalized`-status sweep) so Kalshi settlement can be audited on live data, not only on history.
2. Widen the order-book sample (or add a second pass) to period markets, overtime, first-10-minutes and goalie saves so executability is observable beyond four families.
3. Stamp both the request START and the response COMPLETION time of each tick.
4. Add "New York I", "New York R", "Utah" aliases to `data/identity/teams.csv`.
5. Archive trades (the public trade tape) to make maker-fill probability measurable.
