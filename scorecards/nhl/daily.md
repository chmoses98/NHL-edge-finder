## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-02T15:08:55Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 63887 across 101 games. Settled: 25454 (void/DNP 1079, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1158 (35) | 0.434 | -0.010 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1227 (35) | 0.412 | -0.021 | 0.224 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1158 (35) | 0.291 | -0.008 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1227 (35) | 0.280 | -0.009 | 0.148 | 82% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1158 (35) | 0.564 | -0.017 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1227 (35) | 0.539 | -0.030 | 0.314 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 51 (32) | 4.409 | +0.493 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 68 (35) | 4.655 | +0.818 | 3.479 | 85% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1158 (35) | 1.007 | -0.037 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1227 (35) | 1.007 | +0.071 | 0.669 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 70 (35) | 1.398 | -0.149 | 0.951 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1158 (35) | 1.842 | -0.350 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1227 (35) | 1.751 | +0.101 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 68 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 70 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1158 (35) | -0.0064 [-0.0127, -0.0006] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1158 (35) | -0.0014 [-0.0023, -0.0005] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 722 (35) | -0.0068 [-0.0108, -0.0028] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 722 (35) | -0.0093 [-0.0138, -0.0050] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 51 (32) | -0.0052 [-0.0209, +0.0110] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1158 (35) | -0.0967 [-0.1683, -0.0229] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 89 projected goalie-games, named goalie started 76.4% (mean published P(start) 0.9081).
- participation CONFIRMED_ACTIVE: n=49, started 100.0%
- participation LIKELY_ACTIVE: n=40, started 47.5%

**Skater lineup check**: 1294 projected skaters, 94.8% dressed.
- participation CONFIRMED_ACTIVE: n=150, dressed 94.7%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1118, dressed 95.6%
- participation UNCERTAIN: n=24, dressed 58.3%

**Availability capture**: mean coverage 1.0, newest capture age 16.7 min (median over recent runs), runs summarised: 12.
