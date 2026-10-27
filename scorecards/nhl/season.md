## NHL projection scorecard (season) — season to date

Generated 2026-10-27T00:08:53Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 34078 across 53 games. Settled: 13340 (void/DNP 508, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1284 (38) | 0.423 | -0.001 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1340 (38) | 0.406 | -0.002 | 0.218 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1284 (38) | 0.277 | +0.003 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1340 (38) | 0.273 | +0.003 | 0.139 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1284 (38) | 0.538 | +0.001 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1340 (38) | 0.524 | +0.000 | 0.299 | 82% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 70 (38) | 5.368 | -1.579 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 74 (38) | 5.075 | -1.447 | 3.578 | 81% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1284 (38) | 1.004 | -0.116 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1340 (38) | 0.998 | -0.000 | 0.679 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 76 (38) | 1.379 | +0.043 | 0.939 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1284 (38) | 1.863 | -0.434 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1340 (38) | 1.743 | +0.024 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 74 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 76 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1283 (38) | -0.0113 [-0.0170, -0.0056] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1283 (38) | -0.0006 [-0.0017, +0.0005] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 898 (38) | +0.0000 [-0.0043, +0.0046] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 896 (38) | +0.0009 [-0.0049, +0.0069] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 70 (38) | -0.0116 [-0.0247, +0.0017] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1283 (38) | -0.1180 [-0.1687, -0.0636] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 102 projected goalie-games, named goalie started 72.5% (mean published P(start) 0.914).
- participation CONFIRMED_ACTIVE: n=57, started 100.0%
- participation LIKELY_ACTIVE: n=45, started 37.8%

**Skater lineup check**: 1404 projected skaters, 95.4% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1183, dressed 96.2%
- participation UNCERTAIN: n=18, dressed 27.8%

**Availability capture**: mean coverage 1.0, newest capture age 9.9 min (median over recent runs), runs summarised: 12.
