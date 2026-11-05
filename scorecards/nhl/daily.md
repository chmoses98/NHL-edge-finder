## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-05T15:21:52Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 76612 across 127 games. Settled: 30739 (void/DNP 1274, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1333 (40) | 0.434 | -0.020 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1400 (40) | 0.414 | -0.028 | 0.227 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1333 (40) | 0.294 | -0.011 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1400 (40) | 0.285 | -0.012 | 0.152 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1333 (40) | 0.564 | -0.031 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1400 (40) | 0.544 | -0.041 | 0.319 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 60 (37) | 4.840 | +0.907 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 78 (40) | 4.808 | +0.876 | 3.527 | 85% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1333 (40) | 1.012 | -0.038 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1400 (40) | 1.015 | +0.065 | 0.673 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 80 (40) | 1.329 | -0.210 | 0.907 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1333 (40) | 1.876 | -0.358 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1400 (40) | 1.755 | +0.084 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **WATCH** — CRPS 111% of historical holdout
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 78 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 80 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1331 (40) | -0.0037 [-0.0089, +0.0011] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 1331 (40) | -0.0010 [-0.0020, +0.0001] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 822 (40) | -0.0064 [-0.0102, -0.0029] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 823 (40) | -0.0075 [-0.0117, -0.0036] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 60 (37) | +0.0004 [-0.0125, +0.0149] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1331 (40) | -0.1161 [-0.1717, -0.0606] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 98 projected goalie-games, named goalie started 79.6% (mean published P(start) 0.9124).
- participation CONFIRMED_ACTIVE: n=56, started 100.0%
- participation LIKELY_ACTIVE: n=42, started 52.4%

**Skater lineup check**: 1474 projected skaters, 95.0% dressed.
- participation CONFIRMED_ACTIVE: n=150, dressed 94.7%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1299, dressed 95.9%
- participation UNCERTAIN: n=23, dressed 43.5%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
