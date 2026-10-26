# Team-minute recalibration for the PLAYER_SIM_V1 ice-time projection (RESEARCH_ONLY)

Prepared for a controlled promotion decision. **Nothing here is activated**: the published allocation is still the hard-coded template (`team-minutes-0`); the candidate (`team-minutes-1.0`) runs in shadow only. Evidence on the exposed seasons 2022-2025 is *development* evidence (it fits and selects a specification); the current-games shadow (`SHADOW_CURRENT_GAMES.md`) and its prospective accumulation are the validation.

Code: `src/nhl_edge/players/team_minutes.py` (allocation, shared by research and production), `src/nhl_edge/research/team_minutes_recal.py` (derivation, fit, walk-forward scoring), `src/nhl_edge/research/team_minutes_shadow.py` (current-game scoring). Raw output: `recalibration.json`. Parameters: `data/params/team-minutes-1.0.json` (fingerprint `84aaf65e0f3b3ea3`; the fit reproduces bit for bit).

## 1. What the constants are supposed to be
`build_roster` projects a player's minutes in a strength state as `share[state] x team_minutes[state]`. The share is the player's recency-weighted fraction of his team's **clock** time in the state; `team_minutes` therefore must be the **team's clock minutes** in that state (not skater-minutes, which are ~5x larger). The published template is EV 50.6, PP 4.4 x p_pp/0.215, SH 4.4, EA 0.6, EN 0.6, OT 1.2 (sum 61.8). Measured on the history it is inconsistent in four ways:

| defect | evidence |
|---|---|
| **PP and SH are ~14% too small.** League clock PP = SH = 5.16 min per team-game (regulation games, 2022-25). | `identities` + `skater_budget` |
| **SH ignores the opponent.** One team's short-handed time *is* the other team's power-play time (identical in 100% of 5,103 regulation games; EA of one team equals EN of the other in 99.98%), but the template gives every team SH = 4.4 whatever the matchup, and scales PP by a *goal-share* (`p_pp`, which mixes PP time with PP efficiency). | `identities` |
| **Overtime is added on top of minutes that already contain it.** In the player tables a skater's EV/PP/SH seconds include overtime seconds (total = EV+PP+SH+EA+EN exactly; the overtime column is a subset memo), yet the template adds 1.2 min of OT. | `skater_budget` |
| **States do not partition the game.** The template sums to 61.8 and has EV unrelated to penalty time; in the data the five states sum to exactly 60:00 for both teams in every regulation game, and penalty time comes out of even strength. | `identities` |

**Erratum to the Sprint 6 trace (`docs/research/player_minutes/PROPAGATION_TRACE.md`).** That document quoted league team minutes EA 0.54, EN 2.98, total 64.4. Those three figures are artefacts: the recorded team-state seconds of an **overtime game are padded to a 20:00 overtime grid** (80:00 recorded; the state in force at the last event is held to the end of the grid), which inflated EN to 11.3 min in overtime games. Regulation games (exactly 60:00 recorded) give EA = EN = 0.571 and total 60.0. The 14% PP/SH finding and the fitted state factors (which use player ice time, not team seconds) are unaffected. The original JSON is left untouched.

## 2. The physical allocation (`team-minutes-1.0`)
All values are clock minutes of ONE team in one game; both teams of a game are computed by the same function with the roles swapped.

* `PP_A = c x ppmin_A`, `SH_A = c x ppmin_B`. `ppmin` is V2's own expected PP minutes (already in `components`, the same quantity that drives the PP goal expectation); `c = 1.104` converts V2's 5-on-4 minutes to total power-play clock (fitted: regulation games only). So `PP_A = SH_B` and `SH_A = PP_B` **exactly**.
* `EA_A = EN_B = 0.580` (symmetric league mean).
* `EV = 60 + E[OT] - (PP_A + PP_B) - (EA + EN)` with `E[OT] = 0.713` min (unconditional expected overtime clock per game; 22% of games reach overtime, 33% of those end in a shootout after the full 5:00): the five states **sum to 60 + E[OT]**, penalty time reduces even strength, and both teams get the bit-identical EV clock.
* `team_minutes[s] = kappa_s x clock_s`, `ot = 0`. The overtime state is a memo (its seconds are already inside EV/PP/SH), so it is no longer added.
* `kappa` is the share-normalisation: the dressed skaters' shares sum to *less* than the number of skaters on the ice (EV 4.88 vs 4.99, PP 4.95 vs 5.00, SH 4.00 vs 4.07, EN 3.55 vs 4.89), because the recorded denominators of overtime games are padded and shares are shrunk. `kappa` = observed skater-minutes / (sum of shares x clock) over the training team-games: **EV 1.020, PP 1.006, SH 1.015, EA 0.855, EN 1.150**. Shares themselves are **not** touched (they drive scorer and assist weights), so goals, assists and points cannot change.

Clock vs skater-minutes (regulation games with shift charts, 8,078 team-games): skaters on the ice per clock minute are EV 4.99, PP 5.00, SH 4.07, EA 5.98 (goalie out), EN 4.89; a team-game holds 295.0 skater-minutes in regulation, 304.7 in games that reach overtime, 297.2 on average. The summed projections of a team's dressed skaters are checked against that budget below.

Fallbacks: if V2's `ppmin` is missing/non-positive/outside 2-9 clock minutes for either team, **both** teams get the league clock (`fallback = true` is recorded; PP_A = SH_B still holds). If the candidate cannot be computed or its parameter file cannot be read, the published template is used for that game (tested).

## 3. Fit (training seasons only) and walk-forward scoring
Each test season (2023, 2024, 2025) is scored with parameters fitted on the **earlier** seasons only (2023: 2022; 2024: 2022-23; 2025: 2022-24); the 2022-2025 fit is the proposed constant set. 2026 games are never in a fit. The champion's own per-skater frames (shares, shot rates, actual ice time by state, shots) are used unchanged; only the team-minute dictionary differs between arms. Pooled over 2023-25 (139,628 skater-games; paired, game-clustered 95% intervals, 2,000 resamples):

| arm | TOI bias | PP bias | SH bias | shots bias | TOI MSE | PP MSE | SH MSE | shots deviance | calibration slope TOI / PP / shots |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L0 published template | -0.281 | -0.224 | -0.170 | -0.062 | 6.402 | 1.423 | 1.018 | 1.2502 | 1.042 / 1.167 / 1.074 |
| L1 level refit (same form, constants refitted) | +0.047 | +0.035 | +0.044 | -0.030 | 6.275 | 1.349 | 0.983 | 1.2455 | 0.993 / 0.956 / 1.020 |
| L2 = L1 with overtime as a memo (not added) | -0.073 | +0.035 | +0.044 | -0.030 | 6.291 | 1.349 | 0.983 | 1.2455 | 1.010 / 0.956 / 1.020 |
| L3 = clock budget, league-mean PP/SH (no matchup) | -0.046 | +0.059 | +0.042 | -0.026 | 6.263 | 1.351 | 0.983 | 1.2454 | 1.010 / 0.954 / 1.020 |
| **L4 candidate `team-minutes-1.0`** (matchup PP/SH from V2, EV from the partition) | -0.029 | -0.024 | -0.025 | -0.027 | 6.258 | 1.320 | 0.961 | 1.2460 | 1.018 / 1.016 / 1.032 |

Isolated effect of the candidate against the published template (change in MSE / deviance, negative = better):
* total TOI MSE -0.1439 [-0.1546, -0.1334] (-2.2%)
* power-play TOI MSE -0.1034 [-0.1165, -0.0901] (-7.3%)
* short-handed TOI MSE -0.0568 [-0.0648, -0.0488] (-5.6%)
* even-strength TOI MSE -0.0407 [-0.0559, -0.0251] (-0.7%)
* expected-shots Poisson deviance -0.0043 [-0.0047, -0.0038]

Where the gain comes from (the ladder): the **level** refit (L1) delivers most of the PP/SH/shots gain; **removing the overtime double count** (L2) is neutral for PP/SH but exposes that L1's near-zero total bias (+0.05) was an accident: the additive OT term (+0.12 min) was offsetting an even-strength under-prediction (-0.12), so L2's total is -0.07; the **clock budget with matchup coupling** (L4 vs L3) adds a further PP/SH/EV gain (PP MSE 1.351 -> 1.320, SH 0.983 -> 0.961, EV 5.715 -> 5.669) that a league-constant clock cannot. Calibration: the published template's power-play slope is 1.17 (it under-predicts the busy PP players most: top predicted decile 3.05 predicted vs 3.41 actual) and the candidate's is 1.02 (top decile 3.47 vs 3.45); the largest decile bias falls from 0.52 to 0.08 min for PP and from 0.51 to 0.13 for total TOI.

Stability by season (candidate vs published, change in MSE; every season's intervals except 2025 EV exclude zero and agree in sign):
* 2023 (fit on [2022]): TOI -0.130 [-0.147, -0.113], PP -0.126 [-0.153, -0.102], SH -0.086 [-0.104, -0.070], shots deviance -0.0048 [-0.0056, -0.0039]
* 2024 (fit on [2022, 2023]): TOI -0.119 [-0.139, -0.100], PP -0.080 [-0.101, -0.059], SH -0.032 [-0.043, -0.021], shots deviance -0.0025 [-0.0033, -0.0017]
* 2025 (fit on [2022, 2023, 2024]): TOI -0.181 [-0.199, -0.164], PP -0.103 [-0.124, -0.082], SH -0.051 [-0.064, -0.038], shots deviance -0.0054 [-0.0061, -0.0046]

**Team-level coherence** (sum of the dressed skaters' projected minutes per team-game; actual mean 297.2): published template 292.2 (bias -5.1, RMSE 10.9); candidate 296.7 (bias -0.5, RMSE 9.6); share of team-games with an impossible total (<270 or >330 skater-minutes) 0.77% -> 0.44%. Refitting each state independently (L1) overshoots the budget (298.1); the partition keeps it on target.

## 4. What this does not show
* It is development evidence on seasons that were also used to design the shares and rates; the parameters are nine numbers fitted on 186,841 skater-games, so over-fitting risk is small, but the independent check is the prospective shadow.
* Shots stay under-predicted (-0.027 per skater-game): minutes explain about a tenth of the shots bias; the rest is the shot-rate level (the LC level calibration's job).
* The matchup term has weak individual information (the correlation of V2's `ppmin` with actual PP clock is ~0.16) but unbiased scale (slope 1.02); its gain over a league-constant clock is small but significant (above).
* Usage (last-three-games) and WORKLOAD_V1 minutes are **separate** research tracks and are not part of this change.
