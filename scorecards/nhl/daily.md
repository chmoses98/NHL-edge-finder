## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-04T21:06:49Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 72374 across 116 games. Settled: 30037 (void/DNP 1229, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1298 (39) | 0.436 | -0.024 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1364 (39) | 0.417 | -0.032 | 0.230 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1298 (39) | 0.295 | -0.013 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1364 (39) | 0.286 | -0.014 | 0.153 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1298 (39) | 0.566 | -0.037 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1364 (39) | 0.546 | -0.047 | 0.321 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 57 (36) | 4.962 | +0.928 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 76 (39) | 4.860 | +0.855 | 3.565 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1298 (39) | 1.009 | -0.043 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1364 (39) | 1.012 | +0.061 | 0.672 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 78 (39) | 1.326 | -0.248 | 0.907 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1298 (39) | 1.862 | -0.345 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1364 (39) | 1.739 | +0.106 | — | — | — |

**Drift checks**

- assists: **ALERT** — bias -0.032 (95% CI -0.068..-0.000) exceeds 5% of the mean
- goals: **WATCH** — CRPS 112% of historical holdout
- points: **ALERT** — bias -0.047 (95% CI -0.097..-0.000) exceeds 5% of the mean
- saves: **INSUFFICIENT** — 76 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 78 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1296 (39) | -0.0026 [-0.0076, +0.0023] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 1296 (39) | -0.0009 [-0.0019, +0.0002] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 807 (39) | -0.0064 [-0.0099, -0.0030] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 808 (39) | -0.0081 [-0.0121, -0.0043] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 57 (36) | +0.0017 [-0.0122, +0.0167] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1296 (39) | -0.1161 [-0.1695, -0.0631] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 96 projected goalie-games, named goalie started 79.2% (mean published P(start) 0.9132).
- participation CONFIRMED_ACTIVE: n=56, started 100.0%
- participation LIKELY_ACTIVE: n=40, started 50.0%

**Skater lineup check**: 1434 projected skaters, 95.1% dressed.
- participation CONFIRMED_ACTIVE: n=150, dressed 94.7%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1260, dressed 96.0%
- participation UNCERTAIN: n=22, dressed 45.5%

**Availability capture**: mean coverage 1.0, newest capture age 10.1 min (median over recent runs), runs summarised: 12.
