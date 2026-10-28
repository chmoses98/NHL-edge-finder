## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-28T03:03:12Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 41208 across 68 games. Settled: 14397 (void/DNP 550, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 914 (27) | 0.437 | -0.020 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 957 (27) | 0.417 | -0.021 | 0.228 | 79% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 914 (27) | 0.284 | -0.007 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 957 (27) | 0.277 | -0.007 | 0.145 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 914 (27) | 0.553 | -0.027 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 957 (27) | 0.534 | -0.029 | 0.312 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 47 (27) | 5.158 | -1.160 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 52 (27) | 5.003 | -0.753 | 3.644 | 87% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 914 (27) | 1.003 | -0.089 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 957 (27) | 1.000 | +0.007 | 0.677 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 54 (27) | 1.516 | -0.137 | 1.055 | 74% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 914 (27) | 1.790 | -0.432 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 957 (27) | 1.695 | +0.041 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 52 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 54 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 914 (27) | -0.0124 [-0.0194, -0.0052] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 914 (27) | -0.0008 [-0.0019, +0.0003] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 652 (27) | -0.0003 [-0.0065, +0.0058] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 652 (27) | +0.0001 [-0.0073, +0.0072] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 47 (27) | -0.0197 [-0.0376, -0.0022] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 914 (27) | -0.0906 [-0.1581, -0.0276] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 69 projected goalie-games, named goalie started 75.4% (mean published P(start) 0.9085).
- participation CONFIRMED_ACTIVE: n=37, started 100.0%
- participation LIKELY_ACTIVE: n=32, started 46.9%

**Skater lineup check**: 995 projected skaters, 96.2% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=778, dressed 97.0%
- participation UNCERTAIN: n=14, dressed 35.7%

**Availability capture**: mean coverage 1.0, newest capture age 9.6 min (median over recent runs), runs summarised: 12.
