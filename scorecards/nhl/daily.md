## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-06T23:59:28Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 81044 across 130 games. Settled: 30739 (void/DNP 1274, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 996 (30) | 0.439 | -0.029 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1046 (30) | 0.415 | -0.032 | 0.229 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 996 (30) | 0.293 | -0.008 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1046 (30) | 0.286 | -0.011 | 0.152 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 996 (30) | 0.570 | -0.037 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1046 (30) | 0.548 | -0.043 | 0.322 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 45 (28) | 4.983 | +0.619 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 59 (30) | 4.892 | +0.820 | 3.668 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 996 (30) | 1.010 | -0.039 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1046 (30) | 1.015 | +0.064 | 0.674 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 60 (30) | 1.377 | -0.193 | 0.943 | 75% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 996 (30) | 1.878 | -0.370 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1046 (30) | 1.770 | +0.104 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **WATCH** — CRPS 111% of historical holdout
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 59 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 60 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 994 (30) | -0.0022 [-0.0082, +0.0035] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 994 (30) | -0.0005 [-0.0017, +0.0006] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 643 (30) | -0.0073 [-0.0114, -0.0035] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 644 (30) | -0.0076 [-0.0121, -0.0035] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 45 (28) | +0.0012 [-0.0148, +0.0182] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 994 (30) | -0.1053 [-0.1657, -0.0409] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 77 projected goalie-games, named goalie started 76.6% (mean published P(start) 0.9035).
- participation CONFIRMED_ACTIVE: n=42, started 100.0%
- participation LIKELY_ACTIVE: n=35, started 48.6%

**Skater lineup check**: 1103 projected skaters, 94.8% dressed.
- participation CONFIRMED_ACTIVE: n=112, dressed 95.5%
- participation CONFIRMED_OUT: n=1, dressed 100.0%
- participation LIKELY_ACTIVE: n=974, dressed 95.8%
- participation UNCERTAIN: n=16, dressed 31.2%

**Availability capture**: mean coverage 1.0, newest capture age 4.3 min (median over recent runs), runs summarised: 12.
