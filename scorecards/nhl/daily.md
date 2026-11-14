## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-14T07:42:31Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 109743 across 175 games. Settled: 35596 (void/DNP 1451, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 462 (14) | 0.412 | +0.041 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 495 (14) | 0.389 | +0.032 | 0.197 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 462 (14) | 0.268 | +0.036 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 495 (14) | 0.268 | +0.019 | 0.132 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 462 (14) | 0.516 | +0.077 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 495 (14) | 0.500 | +0.050 | 0.271 | 83% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 16 (11) | 5.222 | +2.042 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 28 (14) | 4.766 | -0.039 | 3.448 | 79% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 462 (14) | 1.006 | -0.016 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 495 (14) | 1.024 | +0.044 | 0.686 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 28 (14) | 1.147 | +0.275 | 0.768 | 100% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 462 (14) | 1.689 | -0.198 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 495 (14) | 1.634 | +0.171 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 462 (14) | -0.0059 [-0.0159, +0.0050] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 462 (14) | -0.0007 [-0.0024, +0.0009] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 247 (14) | +0.0008 [-0.0051, +0.0056] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 248 (14) | -0.0050 [-0.0143, +0.0034] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 16 (11) | -0.0132 [-0.0254, -0.0017] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 462 (14) | -0.0352 [-0.1252, +0.0362] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 40 projected goalie-games, named goalie started 70.0% (mean published P(start) 0.8963).
- participation CONFIRMED_ACTIVE: n=21, started 100.0%
- participation LIKELY_ACTIVE: n=19, started 36.8%

**Skater lineup check**: 517 projected skaters, 95.7% dressed.
- participation CONFIRMED_ACTIVE: n=55, dressed 98.2%
- participation LIKELY_ACTIVE: n=451, dressed 96.5%
- participation UNCERTAIN: n=11, dressed 54.5%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
