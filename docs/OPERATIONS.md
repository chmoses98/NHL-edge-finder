# Operations

## Day one (opening night)

1. Confirm `capture_worker.yml` has a live run (Actions tab) or dispatch it once; it re-dispatches itself.
2. Or dispatch `conductor.yml` with `force: context,capture,simulate` for an immediate RUN NHL.
3. Read `slates/latest/slate.md` on the `data-archive` branch; `packet.json` next to it is the machine-readable
   packet for a thesis builder.
4. After games: settlement runs automatically ~3h after each start; `eval/report.md` follows.

## Reading the outputs

- `slate.md`: one row per game (P(home), P(OT), expected total, goalie statuses, contract counts) and a contract
  table sorted by fee-adjusted EV of the best executable side. `gate` values: `OK` (evaluable), `NO_EDGE`,
  `CANNOT_TRUST_INPUTS` (stale market, thin history, crossed book), `UNSUPPORTED`, `NOT_PREGAME`.
- `packet.json`: per game `identity`, `context` (rest, back-to-back, injuries), `goaltending` (status, confidence,
  factor, mixture detail), `team_state` (ratings, league rates), `model` (components, full sim summary with ladders
  and pmfs), `kalshi` (every joined contract with quotes, model/market/anchored probabilities, both edges), `authority`.
- `STATUS_*.json` on the archive: pointers the conductor reads (`refreshed_at_utc`, `last_capture_utc`,
  `simulated_at_utc`, `settled_at_utc`, `evaluated_at_utc`).

## Alarms

- Coverage alarm (capture): an UNRESOLVED market, an unknown series, or pagination truncation. Fix by adding the
  series to `data/catalog/market_ontology.yaml`.
- `calendar_known=false` (conductor): add the new season to `SEASON_CALENDAR` in `workflows/conductor.py`.
- Archive push failed: the run's archive is uploaded as an artifact; nothing is lost.

## Adding a market family

Add an entry under `families:` in `data/catalog/market_ontology.yaml` with `scope`, `stat`, `period`, `settles_on`,
`support` (start at BUILDABLE or RESEARCH), `series_tickers`/`series_patterns`. Promote to MODELABLE only with a
pricing path in `pricing/price.py`, a settlement path in `settlement/engine.py`, and tests against a real market.

## Archive hygiene

Never rewrite `data-archive`. Never delete partitions. Corrections are new rows (settlement records carry
`stat_correction_version`). `scripts/archive_push.sh` is the only push path.
