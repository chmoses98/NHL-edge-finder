## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-03T23:28:51Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 70439 across 112 games. Settled: 26530 (void/DNP 1116, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1162 (35) | 0.427 | +0.001 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1227 (35) | 0.406 | -0.011 | 0.218 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1162 (35) | 0.288 | -0.003 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1227 (35) | 0.278 | -0.005 | 0.146 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1162 (35) | 0.552 | -0.002 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1227 (35) | 0.530 | -0.017 | 0.306 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 50 (32) | 4.200 | +0.574 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 68 (35) | 4.316 | +0.555 | 3.192 | 90% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1162 (35) | 0.996 | -0.031 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1227 (35) | 1.002 | +0.075 | 0.665 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 70 (35) | 1.384 | -0.085 | 0.930 | 80% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1162 (35) | 1.875 | -0.336 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1227 (35) | 1.777 | +0.092 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 68 settled forecasts (< 100)
- shots: **ALERT** — bias +0.075 (95% CI +0.003..+0.128) exceeds 5% of the mean
- team_goals: **INSUFFICIENT** — 70 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1162 (35) | -0.0021 [-0.0081, +0.0034] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 1162 (35) | -0.0014 [-0.0022, -0.0003] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 728 (35) | -0.0067 [-0.0107, -0.0033] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 728 (35) | -0.0095 [-0.0141, -0.0052] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 50 (32) | -0.0016 [-0.0165, +0.0154] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1162 (35) | -0.1043 [-0.1803, -0.0258] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 89 projected goalie-games, named goalie started 76.4% (mean published P(start) 0.9103).
- participation CONFIRMED_ACTIVE: n=50, started 100.0%
- participation LIKELY_ACTIVE: n=39, started 46.2%

**Skater lineup check**: 1293 projected skaters, 94.9% dressed.
- participation CONFIRMED_ACTIVE: n=150, dressed 94.7%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1120, dressed 95.7%
- participation UNCERTAIN: n=21, dressed 52.4%

**Availability capture**: mean coverage 1.0, newest capture age 10.1 min (median over recent runs), runs summarised: 12.
