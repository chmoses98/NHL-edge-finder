# NHL player engine audit (Wave 2, opportunity / efficiency lane) — 2026-10-11

**Authority: RESEARCH_ONLY.** This is a read-only audit of the existing joint player simulation (`PLAYER_SIM_V1`,
`player-sim-1.0`, `player-features-1.0`) on `origin/main` @ `3b8fcde`. Nothing in this document changes code, parameters,
workflows, published results or staking/authority code. It is written before any new evaluation and is the reference for
the decomposition (`docs/research/opportunity_efficiency/`) that follows.

Verification that the audited code is what produced the committed evidence: re-running
`nhl_edge.research.player_walk_forward.simulate` on the first 20 games of 2025-26 with the current code reproduces
`docs/research/player_sim_v1/skaters_2025.parquet` and `goalies_2025.parquet` exactly (max |Δ| = 0 for `p_p1`, `e_g`,
`e_saves`; `exp_toi` within 7e-15).

## 1. Event chain as implemented

| quantity | where | how it enters | simulated per draw? |
|---|---|---|---|
| Team goals and their timing | `sim/engine_v2.py` (nhl-sim-2.0) | DATA_ONLY_V2 lambdas (`lam_st_*`: team xG ratings x special teams, goalie factor 1.0 in the walk-forward arm), score-state x time hazards, OT/SO | yes |
| Strength state of each goal | `players/engine.py`, `players/params.strength_table` | EN/EA from P(state \| time bucket, own differential) fit on training seasons; PP/SH share from `roster.team_pp_shares` (expected PP minutes for/against x PP/PK quality) | yes |
| **TOI** (all situations, by state) | `players/features.PlayerBook.profile` -> `roster.build_roster` | deployment share of team time per state (EW half-life 6 games, 0.5 pseudo-games toward position mean, fringe prior for newcomers) x **fixed team minutes** (`TEAM_MIN` = EV 50.6, PP 4.4, SH 4.4, EA 0.6, EN 0.6, OT 0 in the walk-forward; production `team_min` scales PP by the PP goal-share ratio and adds OT 1.2) | only as a per-draw lognormal multiplier (sd ≈ 0.14–0.16, LOW role x1.5) plus 0.35–0.8 % early exit, applied to scorer weights; TOI itself is not an output distribution |
| Line combinations / role changes | `features.coice_fractions` (last 8 team games, half-life 2), `features.goal_copresence` (last 60 games), `roster._lines_F` (DailyFaceoff, live only) | co-ice matrix F for assist allocation; tonight's DailyFaceoff slots blended into shares with 3 (confirmed) / 1.5 (projected) pseudo-games | used inside allocation |
| PP deployment | share_pp (as above), PP1/PP2 slot templates live only | PP TOI expectation and PP scorer weight | allocation only |
| Shot generation (player) | `PlayerProfile.ixg60` (own xG model, 60-game half-life, prior minutes 300 EV / 60 PP / 60 SH) | scorer weight = share x ixG/60 x finishing x on-ice GF ratio^1.0 | allocation only |
| **Player SOG** | `roster.build_roster` meta `expected_sog` = Σ_{EV,PP,SH} exp_TOI_s x `sog60_s` (EW 60-game half-life, **unshrunk**, fallback ixG60 x 10) | a deterministic packet field (`expected_shots` in `predictions_player` rows); **no SOG distribution, no SOG contract priced, not coupled to goals or to the opposing goalie's saves** | **no** |
| Shot attempts -> SOG | not modelled (attempts are only in the xG training set) | — | no |
| SOG -> goals | not modelled as conversion of SOG; goals are allocated from team goals by xG-rate weights | — | — |
| Goals / A1 / A2 / points | `players/engine.simulate_players` | allocation of each simulated team goal; points = goals + A1 + A2 in the same draw | yes |
| Opponent shot volume / suppression | `players/params.ShotRates.expected_faced` | league level (last 1,200 team-games) x opp SF/lg x own SA/lg (25-game half-life, 15-game prior) x venue (0.985 home / 1.015 road); team-level only, **not opponent-adjusted** (raw shots for/against; the RESEARCH `features/opponent_adjust` layer is not an input) | as the NB mean |
| Goalie saves | `players/saves.simulate_saves` | NegBin(mu, α=0.017), log mu = log(expected non-goal shots) + c·margin + d·GA + e·OT with slope 1 fixed; GA = the draw's non-EN opponent goals; pull hazard after k-th GA before 50:00 then binomial thinning | yes |
| Starting goalie | walk-forward: the **actual** starter (boxscore `starter`), i.e. saves are evaluated conditional on starting; production: `goalies/state.py` status ladder from `context/goalie_observations` (DailyFaceoff), confidence 0.985/0.85/0.70/0 by status, used for the team goalie-factor mixture; saves rows are "conditional on this net's starter playing" | conditioning only | — |

### Correlation preserved
One nhl-sim-2.0 draw drives team goals, every player's goals/assists/points and both goalies' GA, so
goals-assists-points-team total-GA dependence is structural, and saves co-move with GA and margin through the NB mean.
Invariants (tested): player goals = team non-shootout goals; A2 ≤ A1 ≤ goals; points = goals + assists; saves + GA =
shots faced. **Not preserved:** player SOG is not part of the draw, so (i) shots ≥ goals per player is not enforced in
any distribution, (ii) Σ team skater SOG is not tied to the opposing net's shots faced, and (iii) a player's SOG and his
goals/points are not jointly distributed. Team shots on goal in the game-script layer (`thesis/scripts.py`) come from the
saves layer (documented caveat in `scripts_v1/taxonomy.py`).

## 2. Data sources and timestamps

| source | tables | history | timestamps |
|---|---|---|---|
| NHL api-web boxscore | `data/history/players/players_*`, `goalies_*` (official G, A, PTS, SOG, TOI, saves, SA, GA, starter) | 2021-22 .. 2025-26 + 2026-27 opening night | pulled 2026-09-30T05:3xZ (`MANIFEST_*.json`, `pulled_at_utc`); point-in-time use = games on dates strictly before the forecast date |
| NHL api-web play-by-play | `goals_*`, `shots_*` (attempts: GOAL/SOG/MISS/BLOCK with shooter), per-state `sog_*`/`att_*` in players | same | same |
| NHL stats shiftcharts | TOI by state (`toi_ev_s`..`toi_ot_s`), `coice_*`, `team_states_*` | same; games without shifts have `shifts_ok = False` | same |
| DailyFaceoff lines / starting goalies | archive kinds `context/lines`, `context/goalie_observations` | **live only, from 2026-09-29** (data-archive branch) | every observation has `observed_at`; DFO `updatedAt`, `sourceName` |
| V2 team lambdas | `docs/research/walk_forward_v2_wf2_20260929_games.csv` | 2024-25, 2025-26 | point-in-time walk-forward (parameters fit on seasons < test season) |
| Live player events 2026-27 | data-archive `player_events/*` (settle job) | ~40 games to 2026-10-11 | ingest timestamps in file names |

Historical **starter confirmation timing does not exist** before 2026-09-29 (`research/walk_forward_v2.py` states the
goalie arms are oracle-style for this reason). Historical **line combinations do not exist** (DailyFaceoff pages carry no
history); every backtest uses recent shift-derived deployment (`RECENT_SHIFTS`).

## 3. Market dependency audit

| item | type | finding |
|---|---|---|
| Team lambdas (DATA_ONLY_V2) | direct | no market input; `goalies/state.py` explicitly does not read the sportsbook fields on the DailyFaceoff starting-goalie rows |
| Player features / priors / params (`players/*.py`, `data/params/player-sim-1.0.json`) | direct | no market input (grep of `players/`, `sim/`, `features/`, `goalies/`: only contract identity/pricing modules reference Kalshi) |
| Hyper-parameters (share prior 0.5, onice β 1.0, goal co-presence k 10, fringe prior) | indirect (selection) | chosen on 2023-24 sports outcomes (allocation log-lik, player-game Brier/log loss). The doc justifies the player-game criterion as "what the markets price", but the selection used outcomes, not prices: **not market-fitted** |
| Saves model (slope fixed at 1, NB α) | indirect | fit on official boxscores; no price |
| `MARKET_ANCHORED_PLAYER_V1` (`workflows/shadow_player._anchored`, weight 0.80 on the Kalshi mid) | direct, separate arm | market-centred by design; usable as the **negative control** for rerun tests; never an input to PLAYER_SIM_V1 |
| `research/player_market_benchmark.py` population (two-sided quotes, spread ≤ 0.10) | market-selected population | diagnostic only; not used to fit or select anything in PLAYER_SIM_V1 |
| Production player rows (`predictions_player`) | market-selected population | one row per **joined Kalshi contract**: the published player population is the market-listed one. The simulation itself runs on all projected dressed skaters |
| Production game population | market-selected (weak) | `simulate` runs on games with Kalshi contracts (in practice every NHL game) |
| Settlement / outcomes | settlement-sourced data | player outcomes come from the official NHL boxscore (`settlement/player.py`, `data/player_events.py`), not from Kalshi settlement |
| Thesis / script / candidate layers | direct | read Kalshi mids and the quarantined `context/sportsbook_odds` kind; downstream of the player engine, out of scope |

Conclusion: the player engine's forecasting path is market-independent at runtime and in fitting; market dependence
exists only in separate arms (anchored, benchmark, thesis) and in the **population** of published production rows.

## 4. Existing SOG market inventory and prior research (not redone)

* Kalshi discovery 2026-09-29 (`data/catalog/discovery_summary.json`): family `player_shots` = 0 markets, `goalie_saves`
  = 0 at discovery time; the ontology maps `KXNHLSOG` / `KXNHLSHOTS` (`data/catalog/market_ontology.yaml`) but neither
  series was listed.
* Archived market deltas on data-archive (1,509 snapshot files, 2026-09-29 .. 2026-10-11), series counts: KXNHLGOAL
  3,788, KXNHLFIRSTGOAL 2,836, KXNHLPTS 2,676, KXNHLAST 2,104, KXNHLSAVE 161, **no SOG / shots series**. SIFT's NHL page
  states no shots-on-goal prop is published. A SOG forecast therefore has no Kalshi contract to be benchmarked against
  today; it is a sports-only research output.
* Prior research reused, not repeated: PLAYER_SIM_V1 walk-forward (goals/assists/points/saves/first goal, 2024-25 and
  2025-26), the allocation test (line effects are large: A1 log-lik −2.672 → −2.368 with co-ice), the TOI finding
  (expected TOI MAE 1.88/1.94 min vs 1.86/1.89 for a plain recent mean: **not better than a recent mean**), the saves
  model history (free slope biased; slope fixed at 1), the market benchmark (no player-prop edge evidence),
  H4 (score effects on saves), opponent adjustment (`docs/research/opponent_adjustment/eval.json`: 5v5 xG/CF/SF
  opponent adjustment improves forward rate MSE modestly; RESEARCH, not an input), goalie-status measurement harness
  (`research/goalie_status_eval.py`).

## 5. What this lane will test (decided before looking at any new numbers)

Opportunity and efficiency are evaluated separately, on the full eligible population (every dressed skater with shift
data, every starting goalie; regular season), with the 2024-25 season as the development season and 2025-26 as the
untouched holdout, matched player-game rows and game-clustered bootstrap CIs:

1. TOI and PP TOI: incumbent expected TOI (share x fixed team minutes) vs a plain recent mean.
2. Shot attempts → SOG: attempt volume (per game and per 60) and on-net rate given attempts.
3. SOG → goals: conversion given SOG.
4. Team shots-against → goalie saves: expected shots faced vs a plain recent mean, and saves given shots faced; starter
   confirmation can only be studied on the 2026-27 archive sample (historical timing does not exist).

A challenger is preregistered only where this decomposition isolates a model error, and only one.
