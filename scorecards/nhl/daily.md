## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-31T23:05:38Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 59193 across 92 games. Settled: 22069 (void/DNP 915, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 973 (29) | 0.428 | -0.008 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1023 (29) | 0.409 | -0.023 | 0.224 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 973 (29) | 0.289 | -0.008 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1023 (29) | 0.277 | -0.008 | 0.146 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 973 (29) | 0.547 | -0.016 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1023 (29) | 0.526 | -0.031 | 0.307 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 42 (27) | 5.028 | +0.333 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 56 (29) | 5.029 | +0.590 | 3.668 | 86% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 973 (29) | 0.997 | -0.050 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1023 (29) | 0.987 | +0.064 | 0.658 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 58 (29) | 1.379 | -0.146 | 0.934 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 973 (29) | 1.899 | -0.365 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1023 (29) | 1.804 | +0.054 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 56 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 58 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 973 (29) | -0.0103 [-0.0165, -0.0036] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 973 (29) | -0.0018 [-0.0029, -0.0007] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 601 (29) | -0.0045 [-0.0087, +0.0002] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 601 (29) | -0.0065 [-0.0115, -0.0009] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 42 (27) | -0.0075 [-0.0255, +0.0098] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 973 (29) | -0.0947 [-0.1821, -0.0117] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 70 projected goalie-games, named goalie started 80.0% (mean published P(start) 0.9021).
- participation CONFIRMED_ACTIVE: n=36, started 100.0%
- participation LIKELY_ACTIVE: n=34, started 58.8%

**Skater lineup check**: 1075 projected skaters, 95.2% dressed.
- participation CONFIRMED_ACTIVE: n=114, dressed 93.0%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=941, dressed 96.1%
- participation UNCERTAIN: n=18, dressed 61.1%

**Availability capture**: mean coverage 1.0, newest capture age 9.4 min (median over recent runs), runs summarised: 12.
