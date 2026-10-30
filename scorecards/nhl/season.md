## NHL projection scorecard (season) — season to date

Generated 2026-10-30T00:37:57Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 50088 across 79 games. Settled: 16856 (void/DNP 649, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1619 (48) | 0.423 | +0.002 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1697 (48) | 0.405 | -0.002 | 0.217 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1619 (48) | 0.277 | +0.005 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1697 (48) | 0.271 | +0.005 | 0.138 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1619 (48) | 0.540 | +0.007 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1697 (48) | 0.524 | +0.003 | 0.298 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 86 (48) | 5.159 | -1.397 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 94 (48) | 5.041 | -0.954 | 3.661 | 82% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1619 (48) | 1.002 | -0.097 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1697 (48) | 0.996 | +0.016 | 0.673 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 96 (48) | 1.392 | +0.082 | 0.947 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1619 (48) | 1.867 | -0.421 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1697 (48) | 1.766 | +0.032 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 94 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 96 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1618 (48) | -0.0110 [-0.0162, -0.0058] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1618 (48) | -0.0008 [-0.0017, +0.0001] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 1147 (48) | -0.0006 [-0.0044, +0.0032] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 1145 (48) | -0.0005 [-0.0052, +0.0043] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 86 (48) | -0.0102 [-0.0224, +0.0010] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1618 (48) | -0.1045 [-0.1697, -0.0479] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 128 projected goalie-games, named goalie started 73.4% (mean published P(start) 0.9132).
- participation CONFIRMED_ACTIVE: n=72, started 100.0%
- participation LIKELY_ACTIVE: n=56, started 39.3%

**Skater lineup check**: 1778 projected skaters, 95.4% dressed.
- participation CONFIRMED_ACTIVE: n=237, dressed 98.3%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1513, dressed 96.1%
- participation UNCERTAIN: n=24, dressed 41.7%

**Availability capture**: mean coverage 1.0, newest capture age 4.7 min (median over recent runs), runs summarised: 12.
