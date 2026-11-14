## NHL projection scorecard (season) — season to date

Generated 2026-11-14T07:42:31Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 109743 across 175 games. Settled: 35596 (void/DNP 1451, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 3414 (102) | 0.426 | -0.001 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 3592 (102) | 0.406 | -0.008 | 0.218 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 3414 (102) | 0.282 | +0.003 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 3592 (102) | 0.276 | +0.000 | 0.142 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 3414 (102) | 0.546 | +0.002 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 3592 (102) | 0.528 | -0.008 | 0.303 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 162 (96) | 5.047 | -0.204 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 200 (102) | 4.912 | -0.112 | 3.579 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 3414 (102) | 1.006 | -0.063 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 3592 (102) | 1.007 | +0.039 | 0.675 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 204 (102) | 1.334 | -0.006 | 0.907 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 3414 (102) | 1.846 | -0.366 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 3592 (102) | 1.744 | +0.071 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 3411 (102) | -0.0075 [-0.0109, -0.0037] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 3411 (102) | -0.0009 [-0.0015, -0.0003] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 2216 (102) | -0.0026 [-0.0049, -0.0001] | **better** | SHADOW VALIDATION |
| points | rung RPS | 2216 (102) | -0.0036 [-0.0068, -0.0004] | **better** | SHADOW VALIDATION |
| saves | rung RPS | 162 (96) | -0.0065 [-0.0148, +0.0014] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 3411 (102) | -0.0997 [-0.1389, -0.0655] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 266 projected goalie-games, named goalie started 75.2% (mean published P(start) 0.9104).
- participation CONFIRMED_ACTIVE: n=149, started 100.0%
- participation LIKELY_ACTIVE: n=117, started 43.6%

**Skater lineup check**: 3769 projected skaters, 95.3% dressed.
- participation CONFIRMED_ACTIVE: n=442, dressed 97.1%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=3263, dressed 96.1%
- participation UNCERTAIN: n=58, dressed 44.8%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
