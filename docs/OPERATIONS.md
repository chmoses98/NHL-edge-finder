# Operations

## Day one (opening night)

1. Confirm `capture_worker.yml` has a live run (Actions tab) or dispatch it once; it re-dispatches itself.
2. Or dispatch `conductor.yml` with `force: context,capture,simulate` for an immediate RUN NHL.
3. Read `slates/latest/slate.md` on the `data-archive` branch; `packet.json` next to it is the machine-readable
   packet for a thesis builder.
4. After games: settlement runs automatically ~3h after each start; `eval/report.md` follows. Any game that started
   3-72h ago and is not yet COMPLETE in `STATUS_settle.json` (`backlog`, `games_pending`) keeps settlement due every
   45 min, so late (West Coast) games and games still live at an earlier settle run are retried with no manual action.
   The conductor reads the UNION of the last 4 days of schedule snapshots (the newest snapshot alone drops a slate's
   games once the ET date rolls over). Evaluate runs after every settle and whenever it is older than the last settle.

## Reading the outputs

- `slate.md`: one row per game (P(home), P(OT), expected total, goalie statuses, contract counts) and a contract
  table sorted by fee-adjusted EV of the best executable side. `gate` values: `OK` (evaluable), `NO_EDGE`,
  `CANNOT_TRUST_INPUTS` (stale market, thin history, crossed book), `UNSUPPORTED`, `NOT_PREGAME`.
- `packet.json`: per game `identity`, `context` (rest, back-to-back, injuries), `goaltending` (status, confidence,
  factor, mixture detail), `team_state` (ratings, league rates), `model` (components, full sim summary with ladders
  and pmfs), `kalshi` (every joined contract with quotes, model/market/anchored probabilities, both edges), `authority`.
- `STATUS_*.json` on the archive ROOT: pointers the conductor reads (`refreshed_at_utc`, `last_capture_utc`,
  `simulated_at_utc`, `settled_at_utc`, `evaluated_at_utc`). The canonical evaluate breadcrumb is
  `STATUS_evaluate.json` at the root, written LAST by the evaluate job (with per-step status and the thesis postmortem
  completeness per slate). `eval/STATUS_evaluate.json` is a legacy location (it showed 2026-09-30 until 2026-10-02);
  it is now overwritten with the same content plus `canonical_path`.
- `eval/report_thesis.md`: per slate a label `COMPLETE — n/n games evaluated` or `PARTIAL — k/n games evaluated`
  (a PARTIAL slate's numbers are interim, never the slate's final ROI); FINAL_CARD_UNIQUE (the one latest complete
  pregame snapshot per game; all P/L) and ALL_PROSPECTIVE_DECISIONS (calibration research over every generation; no P/L).
- `card.md`: optimiser stake (nominal bankroll) AND research status / research stake per bet. Research execution:
  `NHL_EDGE_RESEARCH_BANKROLL` (default $250), `NHL_EDGE_RESEARCH_MAX_STAKE` (default $5), and any
  `thesis.governance.ResearchGovernance` field as JSON in `NHL_EDGE_RESEARCH_GOVERNANCE`. These are research governance,
  not model truth; nothing is ever placed.

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
