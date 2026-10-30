## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-30T20:09:18Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 52076 across 82 games. Settled: 19666 (void/DNP 761, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1077 (32) | 0.428 | -0.003 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1132 (32) | 0.410 | -0.014 | 0.222 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1077 (32) | 0.285 | -0.003 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1132 (32) | 0.275 | -0.002 | 0.142 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1077 (32) | 0.545 | -0.006 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1132 (32) | 0.525 | -0.016 | 0.303 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 53 (32) | 4.786 | +0.054 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 62 (32) | 4.637 | +0.391 | 3.400 | 87% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1077 (32) | 1.003 | -0.038 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1132 (32) | 0.999 | +0.062 | 0.664 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 64 (32) | 1.394 | -0.052 | 0.956 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1077 (32) | 1.860 | -0.383 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1132 (32) | 1.777 | +0.047 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 62 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 64 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1077 (32) | -0.0107 [-0.0157, -0.0051] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1077 (32) | -0.0017 [-0.0026, -0.0007] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 711 (32) | -0.0029 [-0.0069, +0.0011] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 711 (32) | -0.0037 [-0.0081, +0.0008] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 53 (32) | -0.0138 [-0.0295, +0.0023] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1077 (32) | -0.0878 [-0.1711, -0.0152] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 76 projected goalie-games, named goalie started 81.6% (mean published P(start) 0.9142).
- participation CONFIRMED_ACTIVE: n=44, started 100.0%
- participation LIKELY_ACTIVE: n=32, started 56.2%

**Skater lineup check**: 1183 projected skaters, 95.7% dressed.
- participation CONFIRMED_ACTIVE: n=76, dressed 94.7%
- participation LIKELY_ACTIVE: n=1086, dressed 96.5%
- participation UNCERTAIN: n=21, dressed 57.1%

**Availability capture**: mean coverage 1.0, newest capture age 4.3 min (median over recent runs), runs summarised: 12.
