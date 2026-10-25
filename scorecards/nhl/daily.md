## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-25T22:07:26Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 32194 across 50 games. Settled: 11933 (void/DNP 471, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1114 (33) | 0.425 | -0.003 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1164 (33) | 0.408 | -0.003 | 0.219 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1114 (33) | 0.279 | +0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1164 (33) | 0.276 | +0.002 | 0.142 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1114 (33) | 0.544 | -0.001 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1164 (33) | 0.530 | -0.002 | 0.303 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 62 (33) | 5.104 | -1.681 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 64 (33) | 4.884 | -1.613 | 3.490 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1114 (33) | 1.008 | -0.124 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1164 (33) | 1.005 | -0.011 | 0.683 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 66 (33) | 1.355 | +0.011 | 0.931 | 86% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1114 (33) | 1.859 | -0.470 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1164 (33) | 1.744 | -0.006 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 64 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 66 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1113 (33) | -0.0108 [-0.0172, -0.0045] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1113 (33) | -0.0002 [-0.0012, +0.0010] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 788 (33) | +0.0002 [-0.0044, +0.0053] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 786 (33) | +0.0010 [-0.0051, +0.0074] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 62 (33) | -0.0079 [-0.0234, +0.0051] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1113 (33) | -0.1173 [-0.1729, -0.0539] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 89 projected goalie-games, named goalie started 71.9% (mean published P(start) 0.9251).
- participation CONFIRMED_ACTIVE: n=54, started 100.0%
- participation LIKELY_ACTIVE: n=35, started 28.6%

**Skater lineup check**: 1222 projected skaters, 95.2% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1004, dressed 95.9%
- participation UNCERTAIN: n=15, dressed 26.7%

**Availability capture**: mean coverage 1.0, newest capture age 12.6 min (median over recent runs), runs summarised: 12.
