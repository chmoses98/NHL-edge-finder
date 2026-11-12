## NHL projection scorecard (weekly) — last 28 days

Generated 2026-11-12T22:05:09Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 109743 across 175 games. Settled: 34244 (void/DNP 1367, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 3286 (98) | 0.425 | -0.002 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 3453 (98) | 0.406 | -0.008 | 0.218 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 3286 (98) | 0.283 | +0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 3453 (98) | 0.276 | -0.000 | 0.142 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 3286 (98) | 0.545 | +0.000 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 3453 (98) | 0.527 | -0.009 | 0.302 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 161 (95) | 5.013 | -0.271 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 192 (98) | 4.949 | -0.118 | 3.608 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 3286 (98) | 1.005 | -0.060 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 3453 (98) | 1.005 | +0.041 | 0.674 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 196 (98) | 1.330 | -0.010 | 0.909 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 3286 (98) | 1.847 | -0.362 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 3453 (98) | 1.749 | +0.074 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 3283 (98) | -0.0073 [-0.0108, -0.0038] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 3283 (98) | -0.0009 [-0.0015, -0.0002] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 2158 (98) | -0.0026 [-0.0052, -0.0001] | **better** | SHADOW VALIDATION |
| points | rung RPS | 2158 (98) | -0.0033 [-0.0066, -0.0002] | **better** | SHADOW VALIDATION |
| saves | rung RPS | 161 (95) | -0.0063 [-0.0145, +0.0020] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 3283 (98) | -0.0974 [-0.1352, -0.0599] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 254 projected goalie-games, named goalie started 75.6% (mean published P(start) 0.9123).
- participation CONFIRMED_ACTIVE: n=144, started 100.0%
- participation LIKELY_ACTIVE: n=110, started 43.6%

**Skater lineup check**: 3621 projected skaters, 95.4% dressed.
- participation CONFIRMED_ACTIVE: n=442, dressed 97.1%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=3117, dressed 96.1%
- participation UNCERTAIN: n=56, dressed 46.4%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
