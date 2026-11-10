## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-10T21:56:07Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 99399 across 158 games. Settled: 32495 (void/DNP 1324, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 575 (17) | 0.423 | -0.002 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 599 (17) | 0.405 | -0.010 | 0.217 | 79% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 575 (17) | 0.281 | +0.007 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 599 (17) | 0.276 | +0.003 | 0.141 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 575 (17) | 0.549 | +0.005 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 599 (17) | 0.532 | -0.009 | 0.303 | 85% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 27 (17) | 5.974 | +0.503 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 34 (17) | 5.948 | +0.031 | 4.463 | 76% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 575 (17) | 1.023 | -0.090 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 599 (17) | 1.024 | -0.008 | 0.683 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 34 (17) | 1.184 | +0.053 | 0.836 | 85% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 575 (17) | 1.905 | -0.304 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 599 (17) | 1.813 | +0.089 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 34 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 34 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 573 (17) | -0.0082 [-0.0138, -0.0030] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 573 (17) | -0.0003 [-0.0019, +0.0013] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 368 (17) | -0.0026 [-0.0062, +0.0014] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 370 (17) | -0.0021 [-0.0065, +0.0023] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 27 (17) | +0.0074 [-0.0070, +0.0253] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 573 (17) | -0.0794 [-0.1386, -0.0146] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 42 projected goalie-games, named goalie started 81.0% (mean published P(start) 0.9049).
- participation CONFIRMED_ACTIVE: n=23, started 100.0%
- participation LIKELY_ACTIVE: n=19, started 57.9%

**Skater lineup check**: 624 projected skaters, 96.0% dressed.
- participation CONFIRMED_ACTIVE: n=38, dressed 94.7%
- participation LIKELY_ACTIVE: n=577, dressed 97.0%
- participation UNCERTAIN: n=9, dressed 33.3%

**Availability capture**: mean coverage 1.0, newest capture age 16.2 min (median over recent runs), runs summarised: 12.
