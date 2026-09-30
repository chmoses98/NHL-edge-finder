# Point-in-time discipline

> Every input to a simulation must answer: what did the system know at that exact instant?

## Mechanisms

- **Every observation is a ledger partition** with `observed_at_utc` (partition) and `_observed_at_utc` (row).
  `Ledger.append_rows` refuses to overwrite; the manifest is append-only with sha256 per file.
- **Reads are "latest at or before the cutoff"**: `workflows/simulate._read_latest(kind, cutoff)` picks the newest
  partition whose observation time is <= `now`, never a later one. `_read_all` (goalie observations) filters
  partitions the same way, and `goalies/state.latest_state` filters rows by `observed_at_utc <= cutoff` again.
- **Market board at the cutoff**: `archive/reconstruct.reconstruct_at(root, now)` rebuilds the board as of the latest
  tick at or before `now` from checkpoint + deltas; a broken chain refuses rather than guesses.
- **Frozen prediction rows** (`schemas/prediction.ContractPrediction`) record `predicted_at_utc`, `data_cutoff_utc`,
  `market_observed_at_utc`, the four quotes used, `input_snapshot_ids` (partition paths / board provenance), seed,
  model/sim/feature versions, and both goalie statuses at the cutoff.
- **Game-start gate**: only games with `status == not_started` and `start_time_utc > now` are simulated; later
  starts are listed under `coverage.games_skipped`. `pregame` on a row is `start > now` and market observation
  before start; evaluation recomputes it from the schedule and excludes post-start rows from every metric.
- **Closing line** is the last market observation strictly before the scheduled start (`evaluation/clv`).
- **Goalies**: a CONFIRMED observation at 17:00 does not exist for a 15:00 simulation. Tests:
  `tests/test_goalies.py`, `tests/test_simulate_e2e.py::test_run_nhl_on_opening_night_fixture`.
- **Sportsbook prices** embedded in the NHL schedule feed are written to `context/sportsbook_odds` only; nothing in
  DATA_ONLY reads that kind. DailyFaceoff rows carry sportsbook lines; `data/goalies.strip_market_fields` removes
  them before archiving, and the parser never reads them.
- **History**: `features/ratings` uses only rows dated strictly before `as_of`; `research/walk_forward` proves the
  cutoff with poisoned-future-row tests.

## What is not yet enforced

- Injury rows are archived and shown in the packet but do not change the model in V1.
- Goalie factors come from season aggregates (previous + current season to date), not from a per-date snapshot of
  the goalie's own history; the aggregate is itself captured at the context refresh instant, so it cannot contain
  future games, but it is coarser than a true daily curve.


## PLAYER_SIM_V1 (2026-09-30)

- **Player history** at date D uses official player-game rows with game date < D only (`PlayerBook.profile` slices by
  date with `searchsorted`; a poisoned-future-row test proves it). Team co-ice uses the team's games before D only.
- **Live history** grows through the settle job: `player_events/*` partitions are written only after a game is final,
  so a simulation at time t sees exactly the games whose partitions were observed at or before t.
- **Lines**: `context/lines` rows are read with the same "latest partition at or before now" rule; DailyFaceoff's own
  `updatedAt` must be within 72 h (and within 12 h + a warmups/morning-skate source to count as CONFIRMED). DailyFaceoff
  keeps no history, so backtests NEVER use lines: they use the previous games' shift-derived deployment
  (`REALISTIC_PIT`). A retrospective-oracle deployment exists only as a labelled diagnostic, never in reported skill.
- **Dressed lineup in backtests**: the actual dressed skaters. In production they are known from warmups, and Kalshi
  settles a non-entering player's contract at the pre-game fair price, so the modelled quantity is P(event | plays).
- **Parameters** used by the live arm (`data/params/player-sim-1.0.json`) were fit on completed seasons 2021-22 .. 2025-26;
  the walk-forward evidence refits every league-level parameter on seasons strictly before each test season.
- **League shot level** for saves is itself point-in-time (the last 1,200 team-games before the date): shots on goal per
  team-game fell from 31.6 (2021-22) to 27.7 (2025-26), and an all-seasons constant both leaked and biased saves.
