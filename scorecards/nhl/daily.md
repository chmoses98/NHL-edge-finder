## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-01T14:04:50Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 61413 across 97 games. Settled: 23766 (void/DNP 1016, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1136 (34) | 0.426 | -0.005 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1194 (34) | 0.407 | -0.018 | 0.220 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1136 (34) | 0.287 | -0.007 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1194 (34) | 0.276 | -0.007 | 0.145 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1136 (34) | 0.549 | -0.012 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1194 (34) | 0.528 | -0.025 | 0.305 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 49 (31) | 4.722 | +0.279 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 66 (34) | 4.688 | +0.427 | 3.485 | 86% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1136 (34) | 1.008 | -0.051 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1194 (34) | 1.004 | +0.059 | 0.671 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 68 (34) | 1.330 | -0.096 | 0.899 | 85% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1136 (34) | 1.909 | -0.356 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1194 (34) | 1.812 | +0.073 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 66 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 68 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1136 (34) | -0.0082 [-0.0145, -0.0021] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1136 (34) | -0.0016 [-0.0026, -0.0006] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 723 (34) | -0.0051 [-0.0088, -0.0013] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 723 (34) | -0.0072 [-0.0116, -0.0027] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 49 (31) | -0.0083 [-0.0238, +0.0081] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1136 (34) | -0.0979 [-0.1787, -0.0251] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 86 projected goalie-games, named goalie started 76.7% (mean published P(start) 0.8984).
- participation CONFIRMED_ACTIVE: n=43, started 100.0%
- participation LIKELY_ACTIVE: n=43, started 53.5%

**Skater lineup check**: 1258 projected skaters, 94.9% dressed.
- participation CONFIRMED_ACTIVE: n=114, dressed 93.0%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1119, dressed 95.9%
- participation UNCERTAIN: n=23, dressed 56.5%

**Availability capture**: mean coverage 1.0, newest capture age 18.7 min (median over recent runs), runs summarised: 12.
