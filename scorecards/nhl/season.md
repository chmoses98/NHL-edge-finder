## NHL projection scorecard (season) — season to date

Generated 2026-10-21T15:35:43Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 9298 across 17 games. Settled: 4889 (void/DNP 223, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 470 (14) | 0.408 | +0.010 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 491 (14) | 0.392 | +0.011 | 0.207 | 82% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 470 (14) | 0.273 | +0.012 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 491 (14) | 0.271 | +0.012 | 0.136 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 470 (14) | 0.523 | +0.021 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 491 (14) | 0.513 | +0.023 | 0.286 | 82% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 28 (14) | 5.558 | -1.865 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 28 (14) | 5.503 | -1.626 | 3.810 | 75% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 470 (14) | 1.014 | -0.154 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 491 (14) | 0.992 | +0.001 | 0.681 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 28 (14) | 1.085 | +0.209 | 0.716 | 93% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 470 (14) | 1.973 | -0.455 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 491 (14) | 1.823 | +0.003 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 28 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 28 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 469 (14) | -0.0135 [-0.0224, -0.0051] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 469 (14) | -0.0003 [-0.0025, +0.0017] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 311 (14) | -0.0006 [-0.0055, +0.0031] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 309 (14) | +0.0021 [-0.0068, +0.0091] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 28 (14) | -0.0013 [-0.0196, +0.0142] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 469 (14) | -0.1527 [-0.2549, -0.0547] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 41 projected goalie-games, named goalie started 68.3% (mean published P(start) 0.9195).
- participation CONFIRMED_ACTIVE: n=24, started 100.0%
- participation LIKELY_ACTIVE: n=17, started 23.5%

**Skater lineup check**: 522 projected skaters, 94.1% dressed.
- participation LIKELY_ACTIVE: n=515, dressed 94.8%
- participation UNCERTAIN: n=7, dressed 42.9%

**Availability capture**: mean coverage 1.0, newest capture age 3.6 min (median over recent runs), runs summarised: 10.
