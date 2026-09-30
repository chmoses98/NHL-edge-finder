# HANDOFF: PLAYER_SIM_V1 — deep player / event simulation (overnight build, 2026-09-30)

## A. VERDICT

**PLAYER_SIM_V1 READY FOR PROSPECTIVE SHADOW** — with a calibration caveat that the evidence below states plainly:
goals, saves and first-goal are validated and calibrated against simple baselines; assists and points are coherent and
competitive on log loss but carry a measurable calibration error (compressed toward the middle) and do **not** beat a
simple role-adjusted rate baseline on assists. Nothing here is edge evidence; the market benchmark is in R.

ALL NHL MODEL FAMILIES REMAIN RESEARCH_ONLY. NO AUTOMATIC BETTING AUTHORITY WAS CREATED. NO BETS WERE PLACED.

## B. SHAs

| repo / ref | start | end |
|---|---|---|
| NHL-edge-finder `main` | `c555c1c` (PR #7 merge) | TBD_MAIN_END |
| NHL-edge-finder `claude/nhl-player-prop-sim-l0ovd5` | branched from `c555c1c` | TBD_BRANCH_END |
| NHL-edge-finder `data-archive` | `fae4ca7` (capture 05:07Z) at session start | still advancing (worker); never written by this session except through the merged code's own jobs |
| NHL-edge-finder `accounting-data` / `kalshi-router/NHL` | `4a0e769` / `a80b586` | untouched (read only, for the opening-night ledger) |
| kalshi-bet-router `main` | `984c7c1` | `984c7c1` (read only; no defect required a change) |

## C. PRs

TBD_PRS

## D. OPENING-NIGHT ROOT CAUSE

**What was actually wagered** (the router's delivery on `kalshi-router/NHL`, `a80b586`; the only authoritative record):

| wager (all YES except the last) | executed | price | stake | PLAYER_SIM_V1 at bet time* | Kalshi mid then | result | game facts (official) |
|---|---|---:|---:|---:|---:|---|---|
| Brady Tkachuk 1+ point (FLA @ CAR) | 20:52Z | 0.550 | $50.00 | **0.363** (DEGRADED_ROLE, NEW_TEAM) | 0.540 | lost | 16.6 min incl. 6.1 PP; 4 attempts, 0.19 xG; FLA won **1-0 in OT**; on ice for the only goal, no point |
| Nick Suzuki 1+ point (MTL @ TOR) | 23:00Z | 0.708 | $75.00 | **0.614** | 0.660 | lost | 18.7 min incl. 2.4 PP; 4 attempts, 0.01 xG; MTL won 3-2 with Suzuki **on the ice for none** of the 3 goals |
| David Pastrnak 1+ point (NYR @ BOS) | 23:01Z | 0.670 | $50.00 | **0.682** | 0.660 | lost | 17.5 min incl. 1.5 PP; 8 attempts, 0.32 xG; BOS won 3-0 (all in the 3rd), on ice for one without a point |
| Mark Stone 1+ point (CHI @ VGK) | 22:59Z | 0.639 | $100.00 | **0.644** | 0.605 | won | (settled YES) |
| Nick Suzuki 1+ point, **NO**, 1 contract | 01:40Z | 0.640 | $0.66 | n/a (in-game) | | won | a post-start hedge-sized order |
| Kevin Lankinen 29+ saves | — | — | **not wagered** | 0.354 | 0.39 | (hit) | discussed only; no ledger row |

\* PLAYER_SIM_V1 re-run on a copy of the production archive at the bet instant (context, rosters, market board observed
before it; no lines archive existed yet, so deployment came from last season's shifts: `RECENT_SHIFTS`). Suzuki's and
Pastrnak's rows are from 22:58Z (their bets were placed at 23:00-23:01Z, at or just after the scheduled start).

**Classification**

- **B. MISSING MODEL (primary cause).** 834 of 1,089 joined opening-night contracts (77%) had no model at all. The
  four point bets were priced by hand from hit rates and role. Stated as fair probabilities they had no validated chain
  underneath them.
- **C. MANUAL HANDICAP OVERCONFIDENCE (material on 2 of 4).** Every wager was bought at or above the market midpoint
  (Suzuki at 0.708 against a 0.66 mid). The final event model is ~19 points below the price paid for Tkachuk (a new-team
  player whose role the model could not see: treat that gap as role uncertainty, not a precise number) and ~9 below for
  Suzuki; it is at the price for Stone (0.644 vs 0.639) and slightly above it for Pastrnak (0.682 vs 0.670). The model is
  still mildly biased DOWN for the highest-probability players (Q), so its gaps in the 55-70% range lean conservative.
  MARKET_ANCHORED_PLAYER_V1 (0.8 weight on the market) is below the price paid on all four.
- **D. NORMAL VARIANCE (large).** 3 losses in 4 bets priced ~0.55-0.71 is not informative: if the prices paid had been
  exactly fair, losing 3+ of 4 has probability 0.13; at the final model's probabilities, 0.20. Two of the losing games were 1-0 OT and 3-0 shutouts; Suzuki was on the ice
  for none of his team's goals. These outcomes do not show the props were negative EV; four bets cannot.
- **E. DATA / ROLE MISS (Tkachuk).** A player on a new team with no NHL games for it: the archived context had no line
  source at all. From today the context job archives DailyFaceoff lines (PP1 membership is exactly the information
  that was missing), and the packet flags `NEW_TEAM` / `DEGRADED_ROLE` / `ROLE_FROM_RECENT_SHIFTS`.
- **A. MODEL DEFECT: none in the game models** (moneyline / totals were not involved). Two defects in the new
  player arm were found and fixed before merge (co-ice for newcomers read as "never together"; a non-player contract
  ended the pricing loop).
- **F. MARKET PRICING.** Kalshi's mids were close to the event model on Pastrnak and Stone; nothing here says the
  market was wrong.

What can be concluded: the process bought four prices at or above the market midpoint with no model underneath; the
losses themselves prove nothing about EV. What cannot be concluded: that any of these props were -EV or +EV.

## E. ORIGINAL SUPPORT GAP

Production slate 2026-09-29 18:05:53Z (run 36603459518): 2,900 NHL markets on the board, 1,089 joined to the five
games, 1,484 unjoined (futures, awards, next-team, later dates).

| family | series | joined contracts | V1 gate before | state before |
|---|---|---:|---|---|
| player_goals | KXNHLGOAL | 297 | UNSUPPORTED 297 | DISCOVERED_UNMODELLED |
| player_points | KXNHLPTS | 207 | UNSUPPORTED 207 | DISCOVERED_UNMODELLED |
| first_goal | KXNHLFIRSTGOAL | 165 | UNSUPPORTED 165 | DISCOVERED_UNMODELLED |
| player_assists | KXNHLAST | 155 | UNSUPPORTED 155 | DISCOVERED_UNMODELLED |
| goalie_saves | KXNHLSAVE | 10 | UNSUPPORTED 10 | DISCOVERED_UNMODELLED |
| period_winner / total / spread | KXNHL{1,2,3}P, …PTOTAL, …PSPREAD | 45 / 45 / 30 | UNSUPPORTED 120 | PARTIAL (V2 prices, no settlement) |
| game_overtime | KXNHLOT | 5 | UNSUPPORTED 5 | PARTIAL (V2 prices P(OT)) |
| game_early_goal | KXNHLF10G | 5 | UNSUPPORTED 5 | DISCOVERED_UNMODELLED |
| game_winner / spread / total / team_total | KXNHLGAME / SPREAD / TOTAL / TEAMTOTAL | 10 / 20 / 45 / 50 | priced | SUPPORTED_MODELLED_SETTLED |

834 of 1,089 (77%) were player-driven and unpriced.

## F. NEW PLAYER ARCHITECTURE

`docs/research/PLAYER_SIM_V1.md` section 2 has the full chain. In one line per layer:

1. **Team** — DATA_ONLY_V2's lambdas (xG ratings, special teams, goalie true talent), unchanged.
2. **When goals happen** — the nhl-sim-2.0 draw with the V2 seed, now recording which half-minute step each goal falls in
   (no extra random numbers: V2 is bit-identical, tested).
3. **Strength of each goal** — EN / EA from an estimated (time bucket x score differential) table; PP / SH from this
   matchup's special-teams share; OT = 3-on-3.
4. **Deployment** — each skater's share of his team's EV / PP / SH / empty-net / extra-attacker / OT time: tonight's
   DailyFaceoff lines and PP units when archived, else recent shift charts; per-draw TOI noise + early exit.
5. **Scorer** — share x shrunk xG/60 (own shot-quality model) x shrunk finishing x shrunk on-ice goals-for ratio.
6. **Primary / secondary assist** — co-ice with the scorer (and A1) x shrunk involvement rates; league unassisted rates.
7. **Points** — goals + A1 + A2 in the same draw. **First goal** — earliest simulated goal. **Saves** — negative
   binomial on expected non-goal shots faced, moved by the simulated score and goals against, thinned by a pull hazard.
8. **Kalshi** — ticker -> NHL player id (fail-closed), probability from the same draws, executable asks, fees, edges,
   market-anchored blend, correlation matrix, uncertainty metadata -> `predictions_player` + packet `player_shadow`.
9. **Settlement / evaluation** — official boxscore / play-by-play -> `settlements` (player + period engines) ->
   `evaluations_player`, `eval/report_player.{json,md}`.

## G. DATA SOURCES

See `docs/research/PLAYER_SIM_V1.md` section 3 for the full audit table. Point-in-time limits in brief:
- Official boxscore / play-by-play / shift charts: history pulled for 2021-22 .. 2026-27-to-date (6,996 games; 6,939 with
  shifts; 0 assist or goal reconciliation failures). Live: ingested by the settle job only after a game is final.
- DailyFaceoff lines/PP units: live only (no history); archived from today; never used in any backtest.
- ESPN injuries: live, name-matched; used only to drop "Out"/IR players from a fallback lineup.
- Kalshi player-prop history: 2025-26 settled markets + hourly candle midpoints (not executable depth).
- Not used: MoneyPuck player/line summaries (season aggregates, not point-in-time per game), Rotowire (HTML only;
  sampled as a future fallback in `docs/probe/samples/player_sources/`), referee data (not robust / not PIT).

## H. PLAYER STATE / TOI

Built: `PlayerBook` profiles (deployment shares by state, talent rates, on-ice ratio, assist involvement, sample-size
flags), line/PP/PK templates from DailyFaceoff, per-draw TOI multiplier (log-sd 0.16 estimated) and early exit (0.35%
estimated), uncertainty metadata (`projection_quality` FULL / STANDARD / DEGRADED_ROLE / PRIOR_HEAVY, `role_confidence`,
`uncertainty_flags` NO_HISTORY / SMALL_SAMPLE / NEW_TEAM / NO_CURRENT_SEASON_GAMES / ROLE_FROM_RECENT_SHIFTS /
NOT_IN_TONIGHTS_LINES / PRIOR_HEAVY, `toi_p10_p50_p90_min`). Validation: see P (TOI MAE).

## I. SHOT MODEL

Own xG on official play-by-play (distance, angle, shot type, rebound, behind-net, strength), logistic by IRLS, fit on
2021-23: held-out 2023-24 log loss 0.2204 vs 0.2448 constant; xG total 8,158 vs 8,105 goals; player-season ixG
correlation with MoneyPuck 0.994. Player shot creation = shrunk ixG/60 by strength state (EV prior 300 min, PP/SH 60).
Expected shots on goal per player are reported in the packet (not a Kalshi market today).

## J. GOAL MODEL

Goals are allocated from simulated team goals to scorers in proportion to deployment share x shrunk xG/60 x shrunk
finishing x shrunk on-ice GF ratio, by strength state. Finishing persistence is weak (removing it costs 0.005 nats per
goal; heavy 40-xG prior). Walk-forward 1+ goal Brier 0.11805 / 0.11988 vs role baseline 0.11922 / 0.12087, log loss
0.3867 / 0.3919 vs 0.3917 / 0.3963, ECE 0.004 / 0.002. 2+ goals also better. Ladders from one draw.

## K. ASSIST MODEL

Primary and secondary modelled separately (different shrinkage: 25 vs 45 opportunities; different league
unassisted / no-A2 rates by state). Given the scorer, assist opportunity = co-ice with the scorer, blended toward who was
actually on the ice at his goals; x shrunk P(A | on ice for a teammate's goal). Evidence: line/co-ice effects are the
single largest assist signal (per-goal A1 log-lik -2.672 -> -2.368; player-game assists 1+ Brier 0.1706/0.1730 ->
0.1687/0.1711 with co-ice). Result vs baselines: better than both in 2024-25; ~tied with (marginally behind) the role
baseline in held-out 2025-26. Secondary-assist involvement adds little beyond position rates (validated gain ~0.004 nats).

## L. POINT MODEL

Points = goals + A1 + A2 of each player in the same draw (never modelled separately). 1+ point Brier 0.20201 / 0.20351
vs role baseline 0.20314 / 0.20405 (better in both seasons), log loss 0.5907 / 0.5942 vs 0.5934 / 0.5956. 2+/3+ points:
better in 2024-25, marginally behind the role baseline in 2025-26.

## M. GOALIE SAVES

Negative binomial on point-in-time expected non-goal shots faced, moved by the simulated regulation margin, goals
against and OT; goalie-pull hazard with time-thinning; EN goals excluded; OT included. Full ladders 14+..40+ for every
net. Pooled ladder Brier 0.1722 / 0.1712 vs Poisson-shots 0.1774 / 0.1744, ECE 0.017 / 0.009 vs 0.062 / 0.052; mean
predicted saves 25.10 / 24.08 vs 24.68 / 24.16 actual. The game script helps at common thresholds (<= 24+), neutral at 28+.

## N. CORRELATION

Structural: one draw produces team goals, each goal's strength / scorer / assisters, the goalie's goals against and
saves, and the first goal. Tested invariants: player goals == team non-shootout goals in every draw; A2 <= A1 <= goals;
nobody credited twice; points = G + A; ladders monotone; saves + GA = shots faced; EN goals never against a goalie.
Each packet game block has a correlation matrix (YES indicators of up to 40 priced contracts + team goals + moneyline)
for exposure research.

## P. HISTORICAL VALIDATION

Walk-forward, realistic point-in-time, 2024-25 and 2025-26 (2,624 games, 94,456 skater-games, 5,248 goalie starts); all
league parameters refit on prior seasons; team lambdas = V2's own walk-forward lambdas; deployment from recent shifts
only. Hyper-parameters chosen on 2023-24 (and one switch on 2024-25, see K); 2025-26 never used for a choice.
Summary: **goals and saves beat simple baselines and are calibrated; first-goal scorer calibrated; 1+ point better than
baselines; assists roughly tied with a role-rate baseline; TOI projection no better than a recent mean.** Full tables:
`docs/research/PLAYER_SIM_V1.md` section 5, `docs/research/player_sim_v1/eval.json`.

## Q. CALIBRATION

1+ point by 5-point bucket (2025-26, held out): 20-25% -> 0.201 observed; 30-35% -> 0.296; 40-45% -> 0.421; 50-55% ->
0.546; 55-60% -> 0.616; 60-65% -> 0.650; 65-70% -> 0.726. So "model says 68% for a point" historically hit ~73%, and
"25%" hit ~22-25%: mild compression, ~1 point high on average. 1+ goal: within ~2 points in every populated bucket. Saves
ladder pooled: within ~2 points in every bucket. Full bucket tables in the research doc.

## O. KALSHI MARKET COVERAGE

Opening-night board (5 games) re-run on a copy of the production archive at 20:51:30Z with the merged code (no lines
archive existed then, so every lineup came from the RECENT_SHIFTS fallback; with archived lines the unpriced count
should fall further).

| family | contracts | before: priced / state | after: priced by | after: state |
|---|---:|---|---|---|
| game_winner / game_spread / game_total / team_total | 10 / 20 / 45 / 50 | V1 (+V2 shadow) / SUPPORTED_MODELLED_SETTLED | unchanged (V1 and V2 byte-identical, tested) | SUPPORTED_MODELLED_SETTLED |
| player_goals | 297 | 0 / DISCOVERED_UNMODELLED | PLAYER_SIM_V1: **283** (14 players not in the projected lineup) | MODELLED_RESEARCH_ONLY, settled |
| player_points | 207 | 0 | **202** (5) | MODELLED_RESEARCH_ONLY, settled |
| player_assists | 155 | 0 | **151** (4) | MODELLED_RESEARCH_ONLY, settled |
| first_goal | 165 | 0 | **154** (11) | MODELLED_RESEARCH_ONLY, settled (no-goal-before-SO unsettleable) |
| goalie_saves | 10 | 0 | **10** | MODELLED_RESEARCH_ONLY, settled |
| period_winner / spread / total | 45 / 30 / 45 | V2 shadow prices / PARTIAL (no settlement) | V2 shadow (unchanged) | MODELLED_RESEARCH_ONLY, **settled** (new period engine) |
| game_overtime | 5 | V2 shadow P(OT) / PARTIAL | unchanged | PARTIAL (settles as a game event in V1's engine: BUILDABLE) |
| game_early_goal (KXNHLF10G) | 5 | 0 | none (the event order exists in the draw, but no rule-verified pricer / settlement was built) | DISCOVERED_UNMODELLED |
| futures / awards / season player totals | (unjoined) | 0 | none | UNSUPPORTED |

Player-driven contracts with a model probability: **0 of 834 -> 800 of 834 (96%)**. Contracts with no model at all on the
opening-night card: 964 -> 44 (34 players missing from the fallback lineup, 5 first-10-minutes, 5 OT in V1's view).

## S. SETTLEMENT

New engines, both append-only, idempotent, Kalshi result compared but never allowed to override:
- `nhl-player-settle-1.0` (`settlement/player.py`): goals / assists / points / saves from the official boxscore line
  (OT counts, shootout never); first goal from the official play-by-play (first non-shootout goal). Player absent from
  the boxscore or dressed with 00:00 TOI -> UNSETTLEABLE (Kalshi settles "active but never enters" at the pre-game fair
  price; we never invent it); no goal before the shootout -> UNSETTLEABLE for first-goal (rules silent). Postponed /
  not final -> UNSETTLEABLE. Identity: team + jersey + name, falling back to team + initial + full last name.
- `nhl-period-settle-1.0` (`settlement/period.py`): period winner (incl. TIE), period spread, period total from official
  play-by-play goals of periods 1-3 (third period excludes OT); refuses when play-by-play goals do not reconcile with the
  boxscore. This moves the V2 period families from PARTIAL to MODELLED_RESEARCH_ONLY + settled.
- The settle job now ingests each final game's official player events once (`player_events/*`) and never refetches a
  game whose player/period contracts all have records (tested). Stat corrections: a new FinalResult correction version
  produces new records; old ones stay.
- Opening-night player contracts (archived in `contracts` since 2026-09-29) settle on the first settle run after merge.

## U. PERFORMANCE

- Historical pull (runner): 6 seasons in parallel, 3-4 minutes each (3 requests per game, 6 workers).
- `nhl simulate`, 5-game opening-night slate on a copy of the production archive, this container (4 vCPU, shared with
  three backtests): **19 s with the player arm vs 5 s without**; peak RSS 1.4 GB vs 0.8 GB. 10,000 draws per game.
  (Loading 5 seasons of official history and building the player-game table is ~6 s of that and is independent of the
  slate size; per-game simulation + pricing ~2 s.)
- Archive growth: `predictions_player` ~75-95 KB gzip per simulate run for 5 games (~800 contracts); packet.json grows to
  ~3.7 MB (all player contracts + correlation matrices); slate.md adds ~6 lines per game. `player_events/*` ~0.2 MB per
  game-day. Repository: `data/history/players/` 20 MB (5 seasons, zstd Parquet), params 20 KB.
- Walk-forward: ~0.15 s per game at 4,000 draws (2,624 games ~7 min per configuration).

## W. AUTHORITY

ALL NHL MODEL FAMILIES REMAIN RESEARCH_ONLY.
NO AUTOMATIC BETTING AUTHORITY WAS CREATED.
NO BETS WERE PLACED.

PLAYER_SIM_V1 and MARKET_ANCHORED_PLAYER_V1 rows carry `authority = RESEARCH_ONLY`, `role = SHADOW`; nothing reads
them to gate, size, route or place anything. kalshi-bet-router was not modified. No order-placement code exists.

## X. REMAINING LIMITATIONS

1. **Compression of assists / points.** Predictions are pulled toward the middle: elite playmakers' assists and points
   are under-predicted and fringe players over-predicted (Q). Goals and saves do not show this. Expect PLAYER_SIM_V1 to
   sit BELOW the market on stars' assist/point props and above it on depth players; treat those gaps as model error until
   prospective evidence says otherwise.
2. **Team layer inherited.** Player probabilities inherit V2's lambdas (total-goals bias ~+0.07/game; the market beats
   V2 on game lines). A player model cannot be better than the team scoring environment it allocates.
3. **Deployment history.** DailyFaceoff lines exist only from today. Backtests use recent shift deployment only, so the
   value of confirmed lines is untested historically; it will be measured prospectively (`deployment_source` is on every
   row). Opening-night-style role changes (new team, new line) remain the weakest case (`DEGRADED_ROLE`).
4. **TOI projection** is not better than a simple recent-mean baseline (P); it matters for the packet, less for the
   allocation (which uses shares).
5. **Opponent matchup effects** beyond the team lambdas (line matching, shutdown pairs, home last change) are not
   modelled: no point-in-time matchup data, and team-level suppression is already in the lambdas. Goalie-specific
   shot-location splits are not used (V2's goalie true talent is; splits are unstable).
6. **Scratches.** P(player plays) is not modelled; probabilities are conditional on playing (Kalshi's fair-price rule
   makes that the right target), and a player missing from the projected lineup is left unpriced.
7. **First goal / team-to-score-first**: calibrated but with little skill; "no goal before the shootout" is unsettleable.
8. **Market benchmark** covers 2025-26 only, from candle midpoints (not executable), hourly granularity (R).
9. **Prospective evidence**: none yet. Nothing here should be read as edge.

## Y. NEXT RUN NHL

When the owner says "Run NHL" (conductor `force: context,capture,simulate`, or the worker's own cadence):
1. `nhl context` also archives DailyFaceoff line combinations for tonight's teams (`context/lines`: EV lines, D pairs,
   PP1/PP2, PK1/PK2, IR, source + updated time, resolved to NHL ids).
2. `nhl simulate` runs V1 (unchanged), DATA_ONLY_V2 (unchanged), then PLAYER_SIM_V1 on V2's own draw. `slates/latest/`:
   - `slate.md` gains a short PLAYER_SIM_V1 section per game: each net's projected starter with expected shots /
     saves / pull risk, and the six player contracts with the largest model-market gaps (with quality flags);
   - `packet.json` gains `player_shadow`: every player contract (P(model), P(market mid), P(market-anchored), yes/no
     asks, fee-adjusted EV both sides, expected TOI / PP TOI / TOI p10-p90 / shots / goals / assists / points, projection
     quality, role confidence, uncertainty flags, deployment source, PP unit, line slot), per-net saves ladders 15+..40+,
     P(home scores first), the top players per team, and a correlation matrix of the game's main contracts + team
     goals + moneyline;
   - archive kind `predictions_player` (append-only).
3. The same game can now be compared across ML / puck line / totals / team totals / periods / player goals / assists /
   points / saves with model evidence instead of guesses. Read the player numbers with X.1 in mind.
4. After the games, `nhl settle` settles player props and period markets from official data and ingests the game's
   player events (tomorrow's projections then include tonight's usage); `nhl evaluate` now actually evaluates (it had
   been pointed at an empty sub-ledger) and writes `eval/report_player.md`.

## Z. OWNER ACTION

**NONE.**
(Optional, unchanged from the router handoff: the router token's pull-request scope on this repository, for accounting
deliveries. Not needed for anything in this build.)
