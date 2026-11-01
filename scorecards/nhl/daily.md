## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-01T01:08:04Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 59197 across 92 games. Settled: 22744 (void/DNP 963, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1039 (31) | 0.427 | -0.006 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1090 (31) | 0.408 | -0.020 | 0.222 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1039 (31) | 0.287 | -0.006 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1090 (31) | 0.276 | -0.007 | 0.145 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1039 (31) | 0.548 | -0.012 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1090 (31) | 0.526 | -0.027 | 0.305 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 44 (28) | 4.936 | +0.197 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 60 (31) | 4.901 | +0.343 | 3.585 | 87% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1039 (31) | 1.015 | -0.061 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1090 (31) | 1.004 | +0.055 | 0.671 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 62 (31) | 1.363 | -0.113 | 0.921 | 84% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1039 (31) | 1.908 | -0.353 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1090 (31) | 1.820 | +0.069 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 60 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 62 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1039 (31) | -0.0104 [-0.0165, -0.0039] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1039 (31) | -0.0018 [-0.0027, -0.0008] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 654 (31) | -0.0048 [-0.0089, -0.0006] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 654 (31) | -0.0069 [-0.0118, -0.0020] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 44 (28) | -0.0106 [-0.0280, +0.0079] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1039 (31) | -0.0895 [-0.1673, -0.0062] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 77 projected goalie-games, named goalie started 77.9% (mean published P(start) 0.8977).
- participation CONFIRMED_ACTIVE: n=38, started 100.0%
- participation LIKELY_ACTIVE: n=39, started 56.4%

**Skater lineup check**: 1148 projected skaters, 95.0% dressed.
- participation CONFIRMED_ACTIVE: n=114, dressed 93.0%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1012, dressed 96.0%
- participation UNCERTAIN: n=20, dressed 55.0%

**Availability capture**: mean coverage 1.0, newest capture age 16.2 min (median over recent runs), runs summarised: 12.
