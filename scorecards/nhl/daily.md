## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-27T23:19:02Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 40313 across 64 games. Settled: 14051 (void/DNP 539, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 988 (29) | 0.428 | -0.009 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1029 (29) | 0.410 | -0.012 | 0.222 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 988 (29) | 0.280 | -0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1029 (29) | 0.274 | -0.002 | 0.142 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 988 (29) | 0.542 | -0.010 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1029 (29) | 0.525 | -0.015 | 0.303 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 51 (29) | 4.844 | -1.464 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 56 (29) | 4.802 | -1.069 | 3.496 | 86% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 988 (29) | 1.021 | -0.100 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1029 (29) | 1.017 | -0.005 | 0.692 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 58 (29) | 1.471 | -0.051 | 1.022 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 988 (29) | 1.803 | -0.424 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1029 (29) | 1.705 | +0.017 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 56 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 58 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 988 (29) | -0.0120 [-0.0194, -0.0056] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 988 (29) | -0.0007 [-0.0018, +0.0003] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 700 (29) | +0.0008 [-0.0049, +0.0060] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 699 (29) | +0.0006 [-0.0070, +0.0072] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 51 (29) | -0.0122 [-0.0279, +0.0031] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 988 (29) | -0.0944 [-0.1579, -0.0323] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 72 projected goalie-games, named goalie started 77.8% (mean published P(start) 0.9122).
- participation CONFIRMED_ACTIVE: n=40, started 100.0%
- participation LIKELY_ACTIVE: n=32, started 50.0%

**Skater lineup check**: 1070 projected skaters, 96.2% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=854, dressed 97.0%
- participation UNCERTAIN: n=13, dressed 30.8%

**Availability capture**: mean coverage 1.0, newest capture age 10.1 min (median over recent runs), runs summarised: 12.
