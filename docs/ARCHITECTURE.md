# Architecture

> RESEARCH_ONLY. No betting authority exists anywhere in this repository.

## Modules (`src/nhl_edge/`)

| module | role |
|---|---|
| `identity/teams.py` + `data/identity/teams.csv` | canonical identity keyed by official NHL `team_id`; abbreviations, aliases (MoneyPuck `T.B`, Kalshi `SJ`), history (ARI 53 -> UHC 59 -> UTA 68) |
| `schemas/` | `Game`, `GameStatus` (NOT_STARTED/LIVE/FINAL/POSTPONED/CANCELED), `GoalieObservation`, `FinalResult`, `Contract`, `ContractPrediction` (pydantic, `extra=forbid`) |
| `data/nhl_api.py` | api-web schedule/score/boxscore/roster parsers, stats REST team and goalie summaries |
| `data/moneypuck.py` | season summaries (teams, goalies) and the all-teams game-by-game log |
| `data/goalies.py` + `goalies/state.py` | DailyFaceoff starting-goalie observations; point-in-time status resolution; starter mixture |
| `data/context.py` | `nhl context`: writes every context kind as an append-only ledger partition with provenance |
| `data/history.py` | historical Parquet pull (MoneyPuck 2022+, NHL official results with REG/OT/SO) |
| `features/ratings.py` | exponentially weighted, shrunk xG ratings; goalie factors; expected goals decomposition |
| `features/build.py` | assembles `GameInputs` for one game from snapshot rows at a cutoff |
| `sim/engine.py` | vectorised joint game simulator |
| `pricing/price.py` | contract probability from the joint draws |
| `kalshi/` | public read client, discovery (all series, no cap), ontology (YAML families), ticker parser, contract semantics, fees, normalisation |
| `archive/` | immutable ledger, delta-encoded market boards, capture job, STATUS breadcrumbs |
| `execution/economics.py` | executable-ask economics: EV after fee, bet-up-to, crossed/stale/thin flags (research only) |
| `settlement/engine.py` | deterministic, idempotent settlement against `FinalResult` |
| `evaluation/` | Brier, log loss, ECE, calibration tables, CLV, authority eligibility (informational) |
| `workflows/` | `conductor` (stdlib-only decisions), `simulate` (RUN NHL), `settle`, `evaluate` |
| `worker/` | the self-renewing capture worker (lease, plan, run) ported from nba-edge-finder |
| `research/walk_forward.py` | historical walk-forward evaluation of DATA_ONLY_V1 |
| `cli.py` | `nhl <command>` |

## Data flow per RUN NHL

1. `nhl context` fetches the schedule window (today + 8 days), team game log, goalie stats, rosters, DailyFaceoff
   observations (resolved to NHL game ids by date + team), ESPN injuries. Each becomes a ledger partition
   `context/<kind>/dt=.../<kind>_<ts>_<run>.jsonl.gz` with `_observed_at_utc`. Sportsbook prices embedded in the
   NHL schedule feed are quarantined in `context/sportsbook_odds` and never read by DATA_ONLY.
2. `nhl capture` snapshots every Kalshi NHL market (catalog series + live series rescan) and up to 300 order books,
   delta-encoded with periodic full checkpoints (`kalshi/markets`, `kalshi/markets_delta`).
3. `nhl simulate` reads the latest partition of each kind observed at or before `now`, builds inputs, simulates each
   NOT_STARTED game on the date with a deterministic seed, prices every joined contract from the same draws,
   computes economics at executable asks, freezes `predictions` and `contracts` rows, writes slate/packet.
4. `nhl settle` (3h after start) fetches the boxscore, derives regulation and final scores, settles idempotently,
   records CONFIRMED starters post-start.
5. `nhl evaluate` joins predictions x settlements, recomputes pregame, computes CLV against the last pre-start
   observation, writes `eval/report.{json,md}`.

## Storage

- `main`: code, `data/identity`, `data/catalog` (ontology + reviewed discovery summary), `data/history/*.parquet`
  (compact, manifested), `docs/`.
- `data-archive` (orphan branch): every observation, prediction, settlement, evaluation. Append-only; `manifest.jsonl`
  uses `merge=union`; `Ledger.verify()` re-hashes before every push; a failed push preserves the run as an artifact.

## Scheduling

GitHub cron delivered ~4% of ten-minute wakes on the NBA repository, so cadence is owned by `capture_worker.yml`:
one run holds the `conductor-archive` concurrency group for ~300 minutes, captures on a horizon-aware cadence,
runs due slow jobs via `conductor.decide_now()`, dispatches its successor early (crash insurance) and again at
retirement. The group holds one running and one pending run, so storms collapse; a lease file on the archive makes
ownership auditable and fail-closed. `conductor.yml` is manual and shares the group.

## Model arms

- `DATA_ONLY_V1`: hockey data only (xG rates, finishing, goaltending, home ice, rest). Never sees a price.
- `MARKET_BASELINE`: the Kalshi midpoint at the market observation instant.
- `MARKET_ANCHORED_V1`: logit blend, weight 0.80 on the market (prior; recorded on every row). Not independent evidence.

## Cross-sport compatibility

Slate/packet rows carry `sport`, `league`, `event_id`, `start_time_utc`, `home`, `away`, `model_version`, `ticker`
(market/contract id), `family`, `p_data_only` (model probability), `p_market`, `executable_p_yes/no`,
`edge_*_raw`, `edge_*_after_fee`, `authority`, `predicted_at_utc`, and settlement rows carry the outcome. A future
multi-sport app can consume `packet.json` directly; the standardisation path is to publish a shared JSON schema
(EdgeLab-style `sport`/`platform` discriminators) once a second sport adopts this packet shape.

## DATA_ONLY_V2 shadow arm (2026-09-29)

- `nhl simulate` runs V1 unchanged, then `workflows/shadow_v2.py` from the same snapshot (no extra network):
  `features/special_teams.py`, `features/goalie_talent.py`, `sim/engine_v2.py`, `pricing/price_v2.py`.
- New archive kinds: `predictions_v2` (one row per contract: V1, V2, market and their differences; role SHADOW) and
  `context/team_games_st` (MoneyPuck 5on5/5on4/4on5/all rows, written only when the content hash changes).
  `slate.json` / `packet.json` gain a `v2_shadow` block; `slate.md` a V1-vs-V2 table. `NHL_EDGE_V2_SHADOW=0` disables.
- Research workflows (branch-only commits, never `main`, never `data-archive`): `research_data.yml` (historical Kalshi
  NHL markets/candles, MoneyPuck shots) and `shadow_run.yml` (read-only V1+V2 RUN NHL on a copy of the archive).
