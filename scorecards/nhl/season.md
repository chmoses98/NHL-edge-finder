## NHL projection scorecard (season) — season to date

Generated 2026-11-03T22:36:09Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 70425 across 112 games. Settled: 26530 (void/DNP 1116, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 2546 (76) | 0.427 | -0.005 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 2675 (76) | 0.407 | -0.011 | 0.220 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 2546 (76) | 0.284 | -0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 2675 (76) | 0.276 | -0.003 | 0.144 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 2546 (76) | 0.547 | -0.007 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 2675 (76) | 0.528 | -0.014 | 0.304 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 125 (73) | 4.865 | -0.624 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 148 (76) | 4.782 | -0.317 | 3.468 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 2546 (76) | 1.002 | -0.074 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 2675 (76) | 1.000 | +0.037 | 0.672 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 152 (76) | 1.376 | -0.049 | 0.935 | 79% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 2546 (76) | 1.863 | -0.393 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 2675 (76) | 1.756 | +0.058 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **OK** — within expectations
- shots: **OK** — within expectations
- team_goals: **OK** — within expectations
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 2545 (76) | -0.0079 [-0.0122, -0.0035] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 2545 (76) | -0.0010 [-0.0017, -0.0002] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 1691 (76) | -0.0031 [-0.0061, +0.0001] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 1689 (76) | -0.0037 [-0.0076, +0.0005] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 125 (73) | -0.0083 [-0.0180, +0.0016] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 2545 (76) | -0.1083 [-0.1547, -0.0625] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 199 projected goalie-games, named goalie started 74.4% (mean published P(start) 0.9116).
- participation CONFIRMED_ACTIVE: n=111, started 100.0%
- participation LIKELY_ACTIVE: n=88, started 42.0%

**Skater lineup check**: 2810 projected skaters, 95.2% dressed.
- participation CONFIRMED_ACTIVE: n=349, dressed 97.1%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2413, dressed 95.9%
- participation UNCERTAIN: n=42, dressed 45.2%

**Availability capture**: mean coverage 1.0, newest capture age 5.2 min (median over recent runs), runs summarised: 12.
