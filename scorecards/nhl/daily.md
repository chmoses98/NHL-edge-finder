## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-05T00:44:21Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 72723 across 116 games. Settled: 30037 (void/DNP 1229, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1266 (38) | 0.435 | -0.024 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1329 (38) | 0.415 | -0.032 | 0.229 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1266 (38) | 0.294 | -0.012 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1329 (38) | 0.286 | -0.014 | 0.153 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1266 (38) | 0.565 | -0.036 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1329 (38) | 0.545 | -0.046 | 0.321 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 56 (35) | 5.025 | +0.970 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 74 (38) | 4.951 | +0.918 | 3.616 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1266 (38) | 1.013 | -0.041 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1329 (38) | 1.016 | +0.064 | 0.675 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 76 (38) | 1.328 | -0.243 | 0.910 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1266 (38) | 1.873 | -0.357 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1329 (38) | 1.746 | +0.101 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **WATCH** — CRPS 112% of historical holdout
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 74 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 76 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1264 (38) | -0.0030 [-0.0082, +0.0019] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 1264 (38) | -0.0009 [-0.0018, +0.0002] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 776 (38) | -0.0064 [-0.0100, -0.0026] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 777 (38) | -0.0075 [-0.0118, -0.0036] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 56 (35) | +0.0021 [-0.0126, +0.0164] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1264 (38) | -0.1194 [-0.1712, -0.0582] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 94 projected goalie-games, named goalie started 78.7% (mean published P(start) 0.9114).
- participation CONFIRMED_ACTIVE: n=54, started 100.0%
- participation LIKELY_ACTIVE: n=40, started 50.0%

**Skater lineup check**: 1398 projected skaters, 95.1% dressed.
- participation CONFIRMED_ACTIVE: n=150, dressed 94.7%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1224, dressed 96.0%
- participation UNCERTAIN: n=22, dressed 45.5%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
