# Edge Finder app export (`edge_finder.app.v1`)

The app-facing publication of this repository's current state. It is an **adapter only**: it reads what the
production jobs already wrote and maps every record onto the vendored contract (`contract/edge_finder_contract`,
byte-identical across the sport repositories; `tests/test_app_contract_v1.py::test_vendored_contract_is_intact`
fails if the copy drifts). Nothing in it prices, simulates, stakes, promotes or places anything. Every
recommendation is `RESEARCH_CANDIDATE` with authority `RESEARCH_ONLY`; `health.bet_authority` is `RESEARCH_ONLY`.

| | |
|---|---|
| Adapter | `src/nhl_edge/app_export.py` (`build_documents()` pure, `export()` publishes) |
| Entry points | `nhl app-export ...` and `python scripts/app_export.py ...` (same options) |
| Options | `--data-root` (archive root, default `data/archive`), `--out` (default `<data-root>/app/latest`), `--accounting-dir` (checkout of `accounting-data`, optional), `--now`, `--commit-sha` (default `$GITHUB_SHA`), `--workflow-run-id` (default `$GITHUB_RUN_ID`), `--source-branch` |
| Where the app reads it | branch **`data-archive`**, path **`app/latest`** (`contract/edge_finder_contract/registry.json` -> `sports.NHL`), i.e. `https://raw.githubusercontent.com/chmoses98/NHL-edge-finder/data-archive/app/latest/<file>` |
| Who writes it | the capture worker (`app_export` in `Worker.SLOW_JOBS`, after `evaluate`) and the conductor workflow step "App export"; both publish into the archive worktree, and `scripts/archive_push.sh` (`git add -A`) carries it with the next archive commit |
| Contract version | `edge_finder.app.v1`, contract `1.0.0` |

## Files

`manifest.json`, `events.json`, `markets.json`, `model_prices.json`, `recommendations.json`, `theses.json`,
`wagers.json`, `settlements.json`, `runs.json`, `board.json`, `performance.json`, `health.json`,
`event_detail/<event_id>.json` (one per event on the board). Written atomically by `publish.publish` (manifest last),
validated against the schemas and the cross-reference checks before a byte is moved.

## What is exported, from where

| Document | Source in the archive (`--data-root`) | Notes |
|---|---|---|
| events | newest `context/schedule` partition (`Ledger.latest("context/schedule")`), the games of the slate's ET date (`STATUS_simulate.date_et`) plus any game a model price, recommendation or wager refers to | status: `not_started` -> `SCHEDULED`, `live`/`in_progress`/`critical` -> `LIVE`, `final`/`off` -> `FINAL`, `postponed` -> `POSTPONED`, `canceled` -> `CANCELLED`. `start_time_confidence="SCHEDULED"` (NHL API, never a Kalshi placeholder). `schedule_updated_at`/`last_updated_at` = the snapshot's `_observed_at_utc`. |
| participants | `nhl_edge.identity.teams.registry()` | `TEAM`, source `nhl_team_id`, `short_name` = abbrev. Players: `PLAYER`, source `nhl_player_id`, only when `packet.json` `player_shadow.contracts[]` resolved the market's player (`player_id`); otherwise the market carries `kalshi_entity_uuid` + `entity_name` in `extensions`. |
| markets | the reconstructed current board, `reconstruct.latest_board(Ledger(root)).rows` (checkpoint + deltas), every market Kalshi had `active` at capture | semantics via `kalshi.contracts.build_contract` (family, scope, period, settles_on, team, threshold, comparator, support). Joined to a game by `contracts.game_key` (game date + the two team ids) against the schedule, falling back to the slate's `ticker -> game_id`. Markets of games outside the exported day keep `extensions.nhl_game_id` but `event_id` is null (their event is not on the board). Prices from `_quote_cents` via `build.from_cents`. Status: `active`/`open` -> `OPEN`, `closed` -> `CLOSED`, `settled`/`finalized` -> `SETTLED`, `unopened` -> `UNOPENED`. `captured_at` = the row's `_observed_at_utc`. |
| model_prices | `slates/latest/slate.json` `contracts[]` | **one per market for the production model `DATA_ONLY_V1`**: `fair_probability = p_data_only`, `uncertainty = p_data_only_se`, `market_probability = p_market`, `generated_at = predicted_at_utc`, `inputs_as_of = market_observed_at_utc`. `data_quality_status` from `gate`: `OK`/`NO_EDGE` -> `OK`, `CANNOT_TRUST_INPUTS` -> `CANNOT_TRUST_INPUTS`, `UNSUPPORTED` -> `UNSUPPORTED`, `NOT_PREGAME` -> `DEGRADED`; `support_status = gate` verbatim. `extensions`: `p_market_anchored`, `executable_p_yes/no`, `edge_yes/no_after_fee`, `best_side`, `gate_reasons`, `prediction_id`, `support`, `sim_version`, `feature_version`. Rows with a null `p_data_only` (gate `UNSUPPORTED`) have no fair probability and are skipped (counted in the run as `slate_unpriced_skipped`); rows whose ticker left the board are skipped with a warning. |
| theses | `slates/latest/packet.json` `thesis_card.games[].card[]` (one per recommendation, `scope = bet_id`) and `thesis_card.games[]` (one per slate game, `scope = "event"`) | **only text the thesis layer already wrote**: `summary = primary_thesis.label`, `supporting_factors = [reason_chosen, secondary_thesis.label]`, `opposing_factors = [failure_case.failure_thesis.label, failure_case.worst_major_script.script, failure_case.note]`, `key_dependencies = failure_case.scripts_needed`, `primary_game_script` = the bet's main script (`thesis_concentration.main_scripts[0]`) / the game's most frequent major script, `confidence_label = family_reliability.label`; numbers go in `evidence`. The game thesis has `summary = null` (no prose exists) and carries the injury list and goalie statuses from the packet's game context. |
| recommendations | `thesis_card.recommended[]` (the bet ids the portfolio optimiser kept) with the full card entry from `packet.json` | `status=RESEARCH_CANDIDATE`, `authority=RESEARCH_ONLY`, `research_only=true`. `native_id = "<bet_id>|<thesis run_id>|<card generated_at>"`. Prices are for the **selection**: `current_price = executable_price.ask_cents/100`, `fair_probability = fair_probability.p_confidence_adjusted` (the card's own conservative number; `p_model_joint_draw` in extensions), `edge = estimated_edge.ev_adjusted_per_contract`, `bet_up_to_price = bet_up_to_price.cents_adjusted/100`, `current_probability` = Kalshi mid for the selection (`1 - p_kalshi_mid` for NO). `stake_dollars = recommended_stake.dollars`, `bankroll_basis = recommended_stake.nominal_bankroll` ($1,000 nominal research bankroll). `expires_at` = the game's start. If `packet.json` is missing, the thinner `slate.thesis_card.recommended[]` rows are used (warning recorded). |
| wagers | `--accounting-dir` -> `data/accounting/wagers.jsonl` (`nhl_accounted_wager.v1`, read with `accounting.ledger.read_jsonl`) | `source=KALSHI_ROUTER`, `source_bet_key` = the router key (the wager identity), `native_id = wager_id` (`nhlw-...`) in `source_ids`, `side=BUY`, `average_price = execution_price`, `fees = fees_paid`, `placed_at = executed_at`. Event via the market's game join. A market no longer on the board gets a `market_stub` (prices null) so every wager's `market_id` exists. Model/recommendation links come from `linkage.apply_links` (only records that predate `placed_at`), never by hand. |
| settlements | `data/accounting/settlements.jsonl` (`nhl_wager_settlement.v1`) | `result` WON/LOST (else `UNKNOWN`), `gross_payout = gross_return`, `net_pnl = net_profit_loss`, `verification_status = EXCHANGE_CONFIRMED` when both are established, `REFUSED` (with the router's `refusals`) otherwise; `settlement_id` derived from the wager id; the wager gets `settlement_status=SETTLED`, `payout`, `profit_loss`. |
| runs | `STATUS_simulate.json` + `slate.json` | `native_run_id = "<simulate run_id>:<simulated_at_utc>"`, `completed_at = --now`, `model_version` from the slate, `commit_sha`/`workflow_run_id` from the CLI (no commit is recorded anywhere in the archive), `data_sources` = board provenance (checkpoint + deltas + board hash), schedule partition, slate directory, accounting dir; `input_freshness` = kalshi / schedule / model / context / accounting. |
| health | `STATUS_capture.json`, `STATUS_simulate.json`, `STATUS_context.json`, `LEASE_capture.json` | `last_market_capture` = the board's observed instant, `last_model_generated` = slate `generated_at_utc`, `next_scheduled_run = LEASE_capture.expected_next_capture_at`, `settlement_as_of` = newest settlement, `router_as_of` = null (the router reports to its own app-data branch). |
| board / performance / event_detail | derived | `event_detail.context`: `nhl_game_id`, matchup, goaltending (status / player / confidence per side), rest days & back-to-backs, injuries, the slate's game-level model numbers (`p_home_win`, `exp_total`, `inputs_trusted` ...). |

## Ids

All deterministic (`edge_finder_contract.ids`): `event_id` from (`NHL`, `nhl_game_id`, game id);
`participant_id` from (`NHL`, `TEAM`/`PLAYER`, `nhl_team_id`/`nhl_player_id`, id); `market_id = mkt_kalshi_<TICKER>`;
`run_id` from (`NHL`, repo, `native_run_id`, `--now`); `model_price_id` from (run, market, model version);
`thesis_id` from (`NHL`, run, event, scope); `recommendation_id` from (`NHL`, repo, `native_id`); `wager_id` from the
router `source_bet_key`; `settlement_id` from the wager id. Two exports of the same inputs with the same `--now` are
byte-identical (tested).

## Freshness thresholds and authority

`market_data`: fresh 20 min / stale 60 min (capture runs every 5-15 min while games are near, `plan.py`).
`model`: fresh 60 min / stale 6 h (the slate is re-priced at most hourly while a game is within 26 h).
Other components use the contract defaults. `bet_authority = RESEARCH_ONLY`, so `overall_status` is
`RESEARCH_ONLY` when everything is fresh, `STALE` when market or model data is past its stale threshold,
`DEGRADED` when the last export failed but a good payload stands, `UNAVAILABLE` when there is no payload.

## Failure policy

`export()` never raises for a data problem. If the build or the publication fails, only `health.json` is
rewritten (`export_failed=true`, `errors=[...]`, `payload_run_id` = the standing manifest's run), the previous
payload is untouched and still verifies, and the process exits 1. The worker treats a failed `app_export` like any
other failed job (logged, never ends the cycle); the conductor step is `continue-on-error: true` so the archive is
still verified and pushed, after which a dedicated step fails the job.

`app/latest` is not a ledger kind: it is never listed in `manifest.jsonl`, so `Ledger.verify()` (the immutability
check before every push) ignores it, and `publish` writes it atomically with its own manifest.

## Running it locally

```
git fetch --depth=1 origin data-archive accounting-data
mkdir -p /tmp/nhl-archive /tmp/nhl-accounting
git archive origin/data-archive | tar -x -C /tmp/nhl-archive
git archive origin/accounting-data | tar -x -C /tmp/nhl-accounting
nhl app-export --data-root /tmp/nhl-archive --accounting-dir /tmp/nhl-accounting --out /tmp/nhl-app --now 2026-10-02T17:30:00Z
PYTHONPATH=contract python -m edge_finder_contract validate /tmp/nhl-app
NHL_EDGE_ARCHIVE_ROOT=/tmp/nhl-archive NHL_EDGE_ACCOUNTING_ROOT=/tmp/nhl-accounting pytest -q tests/test_app_contract_v1.py -k real_data
```

Real-data proof on 2026-10-02 (archive at 17:21:44Z, slate at 16:40:42Z): 5 events (games 2026020017-2026020021,
NYR@DET, WSH@CAR, BOS@WPG, STL@DAL, ANA@VGK), 3,204 markets (890 joined to those games), 125 model prices (82 `OK`
+ 43 `NO_EDGE`; 761 `UNSUPPORTED` rows skipped), 19 recommendations, 24 theses, 0 wagers, 0 settlements,
health `RESEARCH_ONLY`, `verify_published == []`.

## Known gaps

- **The committed accounting ledger is empty.** `accounting-data` holds no rows yet: the 17 real wagers sit on the
  router's unmerged `kalshi-router/NHL` branch, so `wagers.json`/`settlements.json` publish with `count: 0` and
  `performance.json` notes it. The export handles an empty or absent ledger as a valid state (tested); the rows
  appear automatically once the router's PR merges, because the workflows read the branch on every run.
- `UNSUPPORTED` slate rows (761 of 886 on 2026-10-02) carry no `p_data_only` and therefore no model price; the
  contract requires a fair probability. Their market rows are still on the board with `extensions.support`.
- One slate day per export: `events.json` is the slate's ET date (plus games referenced by prices/wagers). The
  schedule snapshot carries ~8 days and the board carries their markets (1,680 game-joined markets on 2026-10-02);
  the other days' markets are exported with `event_id = null` and `extensions.nhl_game_id` set.
- `recommendation.current_probability` is the Kalshi mid for the selection as the card recorded it, not a
  re-read of the board; `current_price` is the card's executable ask. Both are as-of the card's generation.
- Player participants exist only for markets the player shadow model resolved to an NHL player id; other player
  markets expose Kalshi's entity uuid and the parsed name in `extensions`.
- Every export is a new run (`run_id` depends on `--now`), so each worker cycle that captured or ran a job
  rewrites `app/latest` (~3.6 MB, mostly `markets.json`). Git delta compression keeps the branch growth small, but
  an "inputs unchanged -> skip" short-circuit would be a reasonable follow-up.
- `router_as_of` is null: this repository never sees the router's health; the app reads that from the router's
  own `app-data` publication.
- No CLV, bankroll history or P&L is derived here; `performance.json` aggregates ledger settlements only.

## Contract feedback

- `model_price.fair_probability` is required, so a model that explicitly declines to price a market (gate
  `UNSUPPORTED`) cannot be represented as a model-price row; a nullable probability with
  `data_quality_status="UNSUPPORTED"` would let the app show "the model declined" rather than "no row".
- `event.source_ids` is flat string/int; a per-event list of Kalshi event tickers (NHL has ~70 per game across
  period/player series) does not fit, so only the game-level `KXNHLGAME-...` ticker is recorded there.
- `thesis` has one `scope` string; bet-level theses use the bet id as scope, which works but is implicit.
