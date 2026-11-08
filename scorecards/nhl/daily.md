## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-08T00:55:51Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 90096 across 142 games. Settled: 31434 (void/DNP 1285, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 734 (22) | 0.437 | -0.020 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 775 (22) | 0.413 | -0.025 | 0.226 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 734 (22) | 0.291 | -0.000 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 775 (22) | 0.284 | -0.005 | 0.149 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 734 (22) | 0.567 | -0.021 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 775 (22) | 0.545 | -0.030 | 0.318 | 78% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 35 (22) | 4.904 | +0.429 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 44 (22) | 4.996 | +0.848 | 3.692 | 86% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 734 (22) | 1.000 | -0.031 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 775 (22) | 1.002 | +0.059 | 0.660 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 44 (22) | 1.360 | -0.107 | 0.947 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 734 (22) | 1.858 | -0.294 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 775 (22) | 1.761 | +0.134 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 44 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 44 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 732 (22) | -0.0024 [-0.0075, +0.0035] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 732 (22) | -0.0006 [-0.0019, +0.0009] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 471 (22) | -0.0059 [-0.0100, -0.0021] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 472 (22) | -0.0062 [-0.0110, -0.0019] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 35 (22) | +0.0048 [-0.0117, +0.0235] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 732 (22) | -0.0914 [-0.1494, -0.0289] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 53 projected goalie-games, named goalie started 83.0% (mean published P(start) 0.9183).
- participation CONFIRMED_ACTIVE: n=33, started 100.0%
- participation LIKELY_ACTIVE: n=20, started 55.0%

**Skater lineup check**: 808 projected skaters, 95.9% dressed.
- participation CONFIRMED_ACTIVE: n=74, dressed 97.3%
- participation LIKELY_ACTIVE: n=723, dressed 96.7%
- participation UNCERTAIN: n=11, dressed 36.4%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
