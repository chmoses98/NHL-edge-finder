## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-07T17:28:04Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 88241 across 142 games. Settled: 30739 (void/DNP 1274, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 897 (27) | 0.437 | -0.021 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 943 (27) | 0.414 | -0.025 | 0.226 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 897 (27) | 0.291 | -0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 943 (27) | 0.283 | -0.004 | 0.148 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 897 (27) | 0.570 | -0.022 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 943 (27) | 0.547 | -0.029 | 0.318 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 41 (25) | 4.697 | +0.632 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 54 (27) | 4.735 | +0.947 | 3.515 | 87% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 897 (27) | 1.009 | -0.024 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 943 (27) | 1.016 | +0.070 | 0.672 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 54 (27) | 1.348 | -0.065 | 0.927 | 78% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 897 (27) | 1.873 | -0.332 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 943 (27) | 1.753 | +0.130 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 54 settled forecasts (< 100)
- shots: **ALERT** — challenger worse than incumbent on identical forecasts (MAE): +0.0096 [+0.0007, +0.0176]
- team_goals: **INSUFFICIENT** — 54 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 895 (27) | -0.0007 [-0.0064, +0.0049] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 895 (27) | -0.0008 [-0.0020, +0.0004] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 589 (27) | -0.0070 [-0.0113, -0.0034] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 590 (27) | -0.0074 [-0.0120, -0.0033] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 41 (25) | +0.0018 [-0.0137, +0.0178] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 895 (27) | -0.1182 [-0.1873, -0.0519] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 69 projected goalie-games, named goalie started 78.3% (mean published P(start) 0.9074).
- participation CONFIRMED_ACTIVE: n=39, started 100.0%
- participation LIKELY_ACTIVE: n=30, started 50.0%

**Skater lineup check**: 991 projected skaters, 95.2% dressed.
- participation CONFIRMED_ACTIVE: n=74, dressed 97.3%
- participation LIKELY_ACTIVE: n=902, dressed 96.0%
- participation UNCERTAIN: n=15, dressed 33.3%

**Availability capture**: mean coverage 1.0, newest capture age 4.4 min (median over recent runs), runs summarised: 12.
