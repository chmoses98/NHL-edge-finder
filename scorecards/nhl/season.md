## NHL projection scorecard (season) — season to date

Generated 2026-11-12T16:13:59Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 108719 across 175 games. Settled: 33883 (void/DNP 1361, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 3251 (97) | 0.425 | -0.003 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 3417 (97) | 0.406 | -0.009 | 0.218 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 3251 (97) | 0.283 | +0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 3417 (97) | 0.276 | -0.001 | 0.143 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 3251 (97) | 0.545 | -0.001 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 3417 (97) | 0.527 | -0.010 | 0.302 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 159 (94) | 5.016 | -0.334 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 190 (97) | 4.958 | -0.162 | 3.612 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 3251 (97) | 1.006 | -0.066 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 3417 (97) | 1.006 | +0.037 | 0.675 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 194 (97) | 1.333 | -0.016 | 0.911 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 3251 (97) | 1.854 | -0.362 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 3417 (97) | 1.755 | +0.074 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **OK** — within expectations
- shots: **OK** — within expectations
- team_goals: **OK** — within expectations
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 3248 (97) | -0.0070 [-0.0107, -0.0032] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 3248 (97) | -0.0008 [-0.0014, -0.0002] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 2134 (97) | -0.0027 [-0.0051, -0.0003] | **better** | SHADOW VALIDATION |
| points | rung RPS | 2134 (97) | -0.0032 [-0.0063, -0.0001] | **better** | SHADOW VALIDATION |
| saves | rung RPS | 159 (94) | -0.0058 [-0.0136, +0.0025] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 3248 (97) | -0.0982 [-0.1360, -0.0586] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 251 projected goalie-games, named goalie started 75.7% (mean published P(start) 0.9122).
- participation CONFIRMED_ACTIVE: n=142, started 100.0%
- participation LIKELY_ACTIVE: n=109, started 44.0%

**Skater lineup check**: 3584 projected skaters, 95.3% dressed.
- participation CONFIRMED_ACTIVE: n=406, dressed 96.8%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=3116, dressed 96.2%
- participation UNCERTAIN: n=56, dressed 46.4%

**Availability capture**: mean coverage 1.0, newest capture age 11.3 min (median over recent runs), runs summarised: 12.
