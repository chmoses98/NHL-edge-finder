## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-06T22:19:53Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 80985 across 130 games. Settled: 30739 (void/DNP 1274, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1030 (31) | 0.438 | -0.028 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1081 (31) | 0.415 | -0.032 | 0.228 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1030 (31) | 0.294 | -0.009 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1081 (31) | 0.286 | -0.012 | 0.152 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1030 (31) | 0.571 | -0.037 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1081 (31) | 0.549 | -0.044 | 0.323 | 79% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 46 (29) | 4.882 | +0.613 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 61 (31) | 4.872 | +0.652 | 3.653 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1030 (31) | 1.010 | -0.048 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1081 (31) | 1.015 | +0.055 | 0.675 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 62 (31) | 1.374 | -0.202 | 0.939 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1030 (31) | 1.863 | -0.361 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1081 (31) | 1.755 | +0.109 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **WATCH** — CRPS 111% of historical holdout
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 61 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 62 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1028 (31) | -0.0023 [-0.0079, +0.0031] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 1028 (31) | -0.0007 [-0.0019, +0.0004] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 660 (31) | -0.0072 [-0.0112, -0.0037] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 661 (31) | -0.0082 [-0.0128, -0.0042] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 46 (29) | -0.0008 [-0.0161, +0.0174] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1028 (31) | -0.1075 [-0.1646, -0.0467] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 79 projected goalie-games, named goalie started 77.2% (mean published P(start) 0.9033).
- participation CONFIRMED_ACTIVE: n=43, started 100.0%
- participation LIKELY_ACTIVE: n=36, started 50.0%

**Skater lineup check**: 1139 projected skaters, 94.9% dressed.
- participation CONFIRMED_ACTIVE: n=112, dressed 95.5%
- participation CONFIRMED_OUT: n=1, dressed 100.0%
- participation LIKELY_ACTIVE: n=1010, dressed 95.8%
- participation UNCERTAIN: n=16, dressed 31.2%

**Availability capture**: mean coverage 1.0, newest capture age 4.3 min (median over recent runs), runs summarised: 12.
