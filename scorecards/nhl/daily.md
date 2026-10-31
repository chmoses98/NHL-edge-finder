## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-31T17:04:12Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 58433 across 92 games. Settled: 20719 (void/DNP 812, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1117 (33) | 0.427 | -0.002 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1172 (33) | 0.409 | -0.014 | 0.221 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1117 (33) | 0.286 | -0.006 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1172 (33) | 0.275 | -0.005 | 0.143 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1117 (33) | 0.545 | -0.008 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1172 (33) | 0.525 | -0.019 | 0.303 | 82% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 52 (32) | 4.837 | +0.016 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 63 (33) | 4.785 | +0.322 | 3.456 | 86% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1117 (33) | 1.004 | -0.039 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1172 (33) | 1.001 | +0.057 | 0.667 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 66 (33) | 1.419 | -0.086 | 0.967 | 80% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1117 (33) | 1.839 | -0.380 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1172 (33) | 1.758 | +0.045 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 63 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 66 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1117 (33) | -0.0097 [-0.0148, -0.0044] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1117 (33) | -0.0018 [-0.0027, -0.0009] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 730 (33) | -0.0034 [-0.0072, +0.0003] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 730 (33) | -0.0049 [-0.0091, -0.0006] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 52 (32) | -0.0118 [-0.0273, +0.0034] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1117 (33) | -0.0824 [-0.1631, -0.0123] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 78 projected goalie-games, named goalie started 80.8% (mean published P(start) 0.9111).
- participation CONFIRMED_ACTIVE: n=44, started 100.0%
- participation LIKELY_ACTIVE: n=34, started 55.9%

**Skater lineup check**: 1223 projected skaters, 95.8% dressed.
- participation CONFIRMED_ACTIVE: n=114, dressed 93.9%
- participation CONFIRMED_OUT: n=1, dressed 100.0%
- participation LIKELY_ACTIVE: n=1088, dressed 96.7%
- participation UNCERTAIN: n=20, dressed 60.0%

**Availability capture**: mean coverage 1.0, newest capture age 11.9 min (median over recent runs), runs summarised: 12.
