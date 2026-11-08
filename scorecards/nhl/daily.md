## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-08T21:32:49Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 93602 across 148 games. Settled: 31785 (void/DNP 1296, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 674 (20) | 0.425 | -0.011 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 707 (20) | 0.405 | -0.017 | 0.219 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 674 (20) | 0.287 | +0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 707 (20) | 0.282 | -0.003 | 0.147 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 674 (20) | 0.553 | -0.009 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 707 (20) | 0.534 | -0.022 | 0.309 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 32 (20) | 5.282 | +0.774 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 40 (20) | 5.106 | +0.856 | 3.798 | 85% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 674 (20) | 1.002 | -0.045 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 707 (20) | 1.005 | +0.044 | 0.664 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 40 (20) | 1.184 | -0.051 | 0.834 | 85% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 674 (20) | 1.914 | -0.338 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 707 (20) | 1.809 | +0.074 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 40 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 40 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 672 (20) | -0.0014 [-0.0076, +0.0041] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 672 (20) | -0.0003 [-0.0017, +0.0013] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 437 (20) | -0.0044 [-0.0082, -0.0006] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 438 (20) | -0.0044 [-0.0089, +0.0001] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 32 (20) | +0.0089 [-0.0044, +0.0254] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 672 (20) | -0.0986 [-0.1652, -0.0322] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 48 projected goalie-games, named goalie started 83.3% (mean published P(start) 0.9196).
- participation CONFIRMED_ACTIVE: n=30, started 100.0%
- participation LIKELY_ACTIVE: n=18, started 55.6%

**Skater lineup check**: 736 projected skaters, 96.1% dressed.
- participation CONFIRMED_ACTIVE: n=74, dressed 97.3%
- participation LIKELY_ACTIVE: n=653, dressed 96.9%
- participation UNCERTAIN: n=9, dressed 22.2%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
