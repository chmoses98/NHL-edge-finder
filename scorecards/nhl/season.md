## NHL projection scorecard (season) — season to date

Generated 2026-10-20T18:26:47Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 8755 across 17 games. Settled: 2066 (void/DNP 114, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 198 (6) | 0.414 | +0.019 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 208 (6) | 0.393 | +0.024 | 0.204 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 198 (6) | 0.269 | +0.027 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 208 (6) | 0.269 | +0.022 | 0.133 | 78% | — |
| points | PLAYER_SIM_V1 (incumbent) | 198 (6) | 0.521 | +0.045 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 208 (6) | 0.510 | +0.046 | 0.284 | 83% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 12 (6) | 5.407 | -1.602 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 12 (6) | 5.001 | -1.291 | 3.642 | 75% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 198 (6) | 0.961 | -0.154 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 208 (6) | 0.938 | +0.017 | 0.639 | 84% | — |
| team_goals | pf-nhl-F_stack (challenger) | 12 (6) | 1.160 | +0.408 | 0.723 | 92% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 198 (6) | 1.820 | -0.439 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 208 (6) | 1.752 | +0.046 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 12 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 12 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 197 (6) | -0.0077 [-0.0156, +0.0008] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 197 (6) | +0.0005 [-0.0018, +0.0027] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 136 (6) | +0.0024 [-0.0025, +0.0078] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 136 (6) | +0.0095 [+0.0013, +0.0172] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 12 (6) | -0.0237 [-0.0516, +0.0024] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 197 (6) | -0.0573 [-0.2094, +0.0824] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 21 projected goalie-games, named goalie started 57.1% (mean published P(start) 0.8967).
- participation CONFIRMED_ACTIVE: n=11, started 100.0%
- participation LIKELY_ACTIVE: n=10, started 10.0%

**Skater lineup check**: 223 projected skaters, 93.3% dressed.
- participation LIKELY_ACTIVE: n=217, dressed 94.5%
- participation UNCERTAIN: n=6, dressed 50.0%

**Availability capture**: mean coverage 1.0, newest capture age 3.2 min (median over recent runs), runs summarised: 8.
