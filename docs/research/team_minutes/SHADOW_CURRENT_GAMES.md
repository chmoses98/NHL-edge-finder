# Team-minute allocation shadow on current games (2026-10-24 and 2026-10-25 slates)

RESEARCH_ONLY. Descriptive; no pass/fail; nothing here promotes anything. The candidate `team-minutes-1.0` (parameters fitted on 2022-2025 only; no 2026 game is in the fit) was run **beside** the published `team-minutes-0` template, from the same shares, the same lineups and the same V2 components, at real production run instants.

## Method
* **Replay of real instants.** Ten production run instants (the last pregame run for each settled game, 28-51 minutes before the drop) were replayed through the current code (`run_simulate(..., now=<instant>)` against the archive as it stood). Each replay computes BOTH allocations in the same run, so the two arms have identical pregame timestamps and lineups by construction.
* **Replay fidelity.** At each instant the replay's *published* rows were compared field by field with the rows production archived at that instant: 9,608 contract rows, 531,348 field comparisons, **zero differences in any model quantity** (ice time, power-play time, shots, goals, assists, points, prices, edges, roles). The only differences are `minutes_to_start` (production's clock seconds vs the rounded instant) and 90 `p_market_anchored` values that differ in the 16th significant digit (1 ulp of floating-point arithmetic). The replay is therefore a faithful stand-in for what production computed.
* **Outcomes.** Settled `player_events/players` rows (final TOI by state, shots on goal). For each (game, player) the newest shadow row before the puck drop is used; players who did not play are excluded for both arms.

## Result (591 paired skater-games, 17 games; lead time median 39 min, range 28-51)
| | published (`team-minutes-0`) | candidate (`team-minutes-1.0`) | candidate - published (95% game-clustered interval) |
|---|---:|---:|---:|
| mean actual total TOI (min) | 16.63 | | |
| total TOI bias | -0.357 | -0.025 | |
| total TOI MSE | 5.002 | 4.800 | -0.202 [-0.377, -0.044] |
| power-play TOI bias | -0.201 | +0.009 | |
| power-play TOI MSE | 1.485 | 1.333 | -0.152 [-0.404, +0.072] |
| short-handed TOI bias | -0.100 | +0.014 | |
| short-handed TOI MSE | 0.979 | 0.914 | -0.065 [-0.173, +0.031] |
| even-strength TOI MSE | 5.152 | 5.134 | -0.018 [-0.155, +0.129] |
| expected-shots bias | -0.112 | -0.068 | |
| expected-shots Poisson deviance | 1.2498 | 1.2459 | -0.0039 [-0.0093, +0.0029] |
| calibration slope, total TOI (actual on predicted; 1 = calibrated) | 1.045 | 1.016 | |
| calibration slope, PP TOI | 1.232 | 1.062 | |

Reading. The direction and size match the walk-forward result (`RECALIBRATION.md`): the published template under-predicts ice time (total -0.36 min, PP -0.20, SH -0.10), the candidate removes that bias, and total-TOI MSE falls with an interval that excludes zero. With 17 games the PP, SH and shots intervals are wide and include zero: **this sample confirms the direction, it does not add independent precision**. Shots stay under-predicted by the candidate too (-0.068): the remaining shots error is the shot-rate level, not minutes.

By position, total-TOI bias (published -> candidate): forwards -0.319 -> +0.011 (n=393), defence -0.432 -> -0.098 (n=198).

## Representative players (rules fixed in `team_minutes_shadow.representatives`; minutes: published / candidate / actual)
| archetype | player | TOI | PP | SH | shots (exp. / exp. / actual) |
|---|---|---|---|---|---|
| top-line forward (most ice time) | Connor McDavid (EDM, F) | 22.4 / 22.9 / 22.4 | 2.93 / 3.34 / 3.87 | 1.53 / 1.60 / 0.23 | 2.92 / 3.05 / 3 |
| top-six forward (75th percentile of ice time) | Pavel Dorofeyev (NYR, F) | 17.3 / 17.4 / 19.1 | 2.75 / 2.99 / 1.92 | 0.12 / 0.15 / 0.05 | 2.75 / 2.80 / 4 |
| fourth-line forward (nearest 10 min) | Kirby Dach (MTL, F) | 10.0 / 10.1 / 13.2 | 0.50 / 0.57 / 0.00 | 0.23 / 0.26 / 1.57 | 0.91 / 0.91 / 2 |
| top-pair defenceman (most ice time) | Quinn Hughes (MIN, D) | 26.4 / 26.9 / 22.8 | 2.55 / 2.93 / 2.63 | 0.21 / 0.23 / 0.33 | 2.22 / 2.30 / 1 |
| third-pair defenceman (nearest 15 min) | William Wallinder (DET, D, PRIOR_HEAVY) | 15.0 / 15.1 / 13.4 | 0.07 / 0.09 / 0.00 | 0.78 / 0.79 / 0.35 | 1.05 / 1.06 / 1 |
| power-play forward (most PP minutes) | Ryan Nugent-Hopkins (EDM, F) | 18.0 / 18.4 / 18.9 | 3.22 / 3.67 / 3.73 | 0.78 / 0.81 / 0.00 | 1.76 / 1.85 / 1 |
| power-play defenceman (most PP minutes) | Evan Bouchard (EDM, D) | 24.8 / 25.3 / 26.2 | 3.01 / 3.43 / 3.78 | 1.41 / 1.47 / 0.00 | 2.46 / 2.55 / 3 |
| penalty-kill defenceman (most SH minutes) | Zach Whitecloud (CGY, D) | 20.3 / 20.8 / 20.5 | 0.09 / 0.10 / 0.00 | 2.65 / 3.11 / 2.77 | 0.89 / 0.91 / 2 |
| largest PP increase under the candidate | Cale Makar (COL, D) | 22.6 / 23.5 / 23.3 | 2.73 / 3.57 / 4.53 | 1.77 / 2.00 / 2.65 | 2.41 / 2.55 / 1 |
| prior-heavy (little NHL history) skater | Hunter McDonald (PHI, D, PRIOR_HEAVY) | 14.7 / 14.9 / 10.1 | 0.10 / 0.12 / 0.00 | 1.49 / 1.81 / 0.00 | 0.01 / 0.01 / 1 |

Single games say little (one player-game is mostly noise); the table shows the *mechanics*. Across all 1,882 pregame player rows the candidate moves expected minutes as follows (percent change from the published value, 5th / 50th / 95th percentile): total ice time +0.5 / +2.0 / +3.5, power-play time +8.9 / +18.6 / +30.6, short-handed time +2.4 / +11.3 / +19.4, even-strength time -0.5 / +0.3 / +1.9, expected shots +0.2 / +2.2 / +5.9. No row moves in an implausible direction and no row used the league-clock fallback (every game had its V2 power-play-minute inputs). Goals, assists and points for the same players are bit-identical under both allocations (below).

## What is being compared, and what is not
* Published-field equivalents only: `expected_toi_min`, `expected_pp_toi_min`, `expected_shots` (and through them the `toi_p10_p50_p90_min` band and `top_players` minutes). Goals, assists, points, saves and every price are computed from shares and rates, not minutes, and are **identical to the last bit** under both allocations (`tests/test_team_minutes.py::test_goals_assists_points_and_every_price_are_bit_identical_under_either_allocation`).
* Selection: the 17 games are every game that had settled when this was run; no game was dropped. The sample is small and covers one weekend, so the intervals above are wide.
* The prospective accumulation continues automatically once this change is merged (archive kind `player_tm_shadow`, one row per dressed skater per run); `python -m nhl_edge.research.team_minutes_shadow --archive <archive> --out ...` re-scores it at any time.
