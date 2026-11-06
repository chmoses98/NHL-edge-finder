## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-06T01:41:52Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 79384 across 127 games. Settled: 30739 (void/DNP 1274, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1063 (32) | 0.436 | -0.023 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1117 (32) | 0.413 | -0.027 | 0.226 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1063 (32) | 0.294 | -0.010 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1117 (32) | 0.286 | -0.012 | 0.152 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1063 (32) | 0.569 | -0.033 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1117 (32) | 0.546 | -0.039 | 0.320 | 79% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 46 (29) | 4.882 | +0.613 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 63 (32) | 4.872 | +0.650 | 3.629 | 86% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1063 (32) | 1.015 | -0.043 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1117 (32) | 1.019 | +0.057 | 0.678 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 64 (32) | 1.384 | -0.209 | 0.942 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1063 (32) | 1.853 | -0.352 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1117 (32) | 1.744 | +0.108 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **WATCH** — CRPS 111% of historical holdout
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 63 settled forecasts (< 100)
- shots: **ALERT** — challenger worse than incumbent on identical forecasts (MAE): +0.0082 [+0.0003, +0.0182]
- team_goals: **INSUFFICIENT** — 64 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1061 (32) | -0.0021 [-0.0073, +0.0034] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 1061 (32) | -0.0008 [-0.0019, +0.0002] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 679 (32) | -0.0071 [-0.0106, -0.0039] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 680 (32) | -0.0083 [-0.0124, -0.0046] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 46 (29) | -0.0008 [-0.0161, +0.0174] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1061 (32) | -0.1078 [-0.1655, -0.0477] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 81 projected goalie-games, named goalie started 77.8% (mean published P(start) 0.9031).
- participation CONFIRMED_ACTIVE: n=44, started 100.0%
- participation LIKELY_ACTIVE: n=37, started 51.3%

**Skater lineup check**: 1178 projected skaters, 94.8% dressed.
- participation CONFIRMED_ACTIVE: n=150, dressed 94.7%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1010, dressed 95.8%
- participation UNCERTAIN: n=16, dressed 31.2%

**Availability capture**: mean coverage 1.0, newest capture age 4.4 min (median over recent runs), runs summarised: 12.
