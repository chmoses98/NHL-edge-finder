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

## Research explorer (`app/latest/explorer`, contract 1.1.0)

The research graph the app navigates (teams -> players -> games -> opponents -> metrics -> rankings -> trends ->
markets), published beside the v1 files by a second adapter, `src/nhl_edge/research_export.py`
(`build_explorer()` pure, `export_explorer()` publishes through `research.publish_explorer`: validated, graph- and
capability-checked, staged, swapped in with `index.json` last; any problem leaves the previous tree untouched).

| | |
|---|---|
| Entry points | `nhl research-export --data-root data/archive --out data/archive/app/latest [--now] [--history-root] [--commit-sha]`, `python scripts/research_export.py ...` |
| Runs | after every app export: the conductor step `research_export` (own command, `continue-on-error`, step summary, then "Fail the job if the research export failed" after the push) and the capture worker (`Worker._run_research_export`, after every successful `app_export`; a failure is recorded on the cycle as a non-critical job) |
| Why after every app export | `publish.publish` removes every file under `app/latest` its manifest does not list, `explorer/` included, so the explorer must be re-published after each v1 publication |
| Identity | `run_id` = the v1 manifest's `run_id`; `generated_at` = the v1 manifest's `generated_at` (or `--now`); `as_of` = the newest data timestamp read. Team / player / event ids are the v1 `prt_` / `evt_` ids (same `build.participant` / `ids.event_id` sources: `nhl_team_id`, `nhl_player_id`, `nhl_game_id`) |
| Inputs | the v1 publication (events, markets, model prices, wagers); `data/history` on `main` (MoneyPuck team game logs, official results, official player / goalie game logs: last complete season, plus the previous season and the current partial file for players); the archive (`context/team_games`, `team_games_st`, `team_summary`, `schedule`, `rosters`, `lines`, `injuries`, `goalie_observations`, `results`, `player_events/*`, `predictions`, `eval/report*.json`, `kalshi/markets` checkpoints + deltas via `archive/reconstruct.iter_board_ticks`, `slates/latest/packet.json`) |

### What it publishes

- **Team profiles** (all 32 active clubs): 2025-26 (history) and 2026-27 (live) regular-season xGF%, xGF/60, xGA/60,
  CF%, FF%, HDxGF%, score/venue-adjusted xGF%, GF/GP, GA/GP; L10 (each team's last 10 stored games, computed by the
  export); official points %, PP %, PK % (NHL team summary); point-in-time DATA_ONLY_V1 ratings (off/def xG60, finish,
  stop) and the model's expected goals (lambda, RESEARCH) from the latest packet. Every value carries its league
  rank / universe / average / best / worst from a published ranking. Splits: situation (5on5 / 5on4 / 4on5) and home/away.
  Last-82-game log (`extensions.game_log`), game refs with official results, opponents, roster, injuries, the team's
  markets and model prices for its next game.
- **Player profiles** (every rostered skater and goalie of the teams in the v1 events): official season totals for
  the last complete and the current season, L10, TOI per game by strength state, goalie save % / EV save % / GAA;
  season rankings over skaters with >= 20 GP / goalies with >= 15 starts (current-season rankings only once 50
  players reach 10 games); last-82-game official log; injury status (ESPN, name-matched) and goalie-start status.
- **Event research** (one per v1 event): matchup rows (primary season, L10, run), every v1 market as a market ref,
  DATA_ONLY_V1 model prices as projections (`research_only`, `RESEARCH_ONLY`), total-goals and margin quantiles from
  the latest simulation, goalie status timeline and line combinations / PP-PK units (`context.lineups`), injuries,
  venue, rest notes, per-family calibration and CLV, the simulation ladders and lambda decomposition (`extensions`).
- **Market history** (one per v1 event): every ticker's quote-change series (bid / ask / last, volume and open
  interest at the change) from checkpoints + deltas, plus the last observation; thinned to the most recent change
  points only if a document would exceed 380 KB (none did on 2026-10-03).
- **Time series**: per-game xGF% and CF% (last 82 games, rolling L10) for the teams on the slate; DATA_ONLY_V1
  probability per run (x_axis RUN) for every priced ticker of the published events. Because `explorer/index.json`
  cannot be sharded, probability series are dropped lowest-priority first (team totals, then game totals, spreads;
  moneylines last) when the index would pass 295 KB; the run's warnings and the `raw_projections` limitations say how
  many.
- **Rankings, metric registry (33 metrics), capability manifest, search index** (teams, players, events, metrics,
  rankings).

### Capabilities (audit 2026-10-03, `scratchpad/phase2/audit_nhl.md` §4/§10)

A mixed audit rating publishes the lower status unless only the higher-rated part is published. A capability whose
source is absent from the archive being exported is downgraded to UNAVAILABLE with the reason.

| status | capabilities | why |
|---|---|---|
| VERIFIED | usage, raw_projections, market_prices, market_price_history, player_props, team_props, game_markets, calibration, historical_accuracy, clv, search | production kinds on a cadence (actual TOI from shift charts, `predictions`, board captures, `eval/report.json`); player props are VERIFIED as captures only |
| PARTIAL | team_profiles, player_profiles, event_research, team_metrics, player_metrics, team_game_logs, player_game_logs, historical_results, opponents, recent_form_windows, lineups, injuries, projection_distributions, advanced_stats, situational_splits, rankings, time_series, comparisons | history parquet is a one-off manual pull; ratings not opponent-adjusted; lines/injuries 4-5 days deep, injuries name-only; L10 and rankings are export arithmetic, not stored by the repository |
| RESEARCH | matchup_metrics | lambda decomposition / expected goals per run (`model_expected_goals` stays RESEARCH inside profiles, matchup rows and packets) |
| UNAVAILABLE | opponent_adjustment, schedule_strength, play_by_play, weather, venue_effects, wager_history | none computed (audit §6); shots/goals not exposed per play; indoor; constant home factor only; accounting ledger empty (PARTIAL automatically once wagers exist) |

### Sizes (real archive, 2026-10-03T06:30Z: 13 events, 26 teams on the slate)

`research.tree_bytes`: players 13.74 MB (620 files, ~25 KB each), market_history 4.38 MB (13, max 365 KB), teams
3.24 MB (32, max 111 KB), series 2.06 MB (358), events 1.48 MB (13, max 115 KB), rankings 1.37 MB (58, max 157 KB),
index.json 295 KB, search_index.json 234 KB, metrics.json 86 KB, capabilities.json 23 KB; total 26.9 MB. Build ~50 s
(~25 s of it is replaying the 520 board ticks). Every file carries the run id, so every publication rewrites the tree.

### Deliberately not published

Opponent- or schedule-adjusted anything (none exists); per-play shots/goals rows; order-book depth; historical Kalshi
candles (2025-26); DATA_ONLY_V2 and PLAYER_SIM_V1 per-contract probabilities and projected TOI (RESEARCH shadow arms;
PLAYER_SIM_V1 calibration is in the registry as RESEARCH); thesis scripts / portfolios / postmortems; sportsbook
consensus (quarantined); historical walk-forward datasets under `docs/research`; player time series (game logs are
tables in the profiles); team series for teams not on the slate.
