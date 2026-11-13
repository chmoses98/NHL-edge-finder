## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-13T08:05:35Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 109743 across 175 games. Settled: 34244 (void/DNP 1367, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 334 (10) | 0.400 | +0.052 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 356 (10) | 0.374 | +0.040 | 0.185 | 82% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 334 (10) | 0.264 | +0.041 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 356 (10) | 0.262 | +0.022 | 0.127 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 334 (10) | 0.492 | +0.093 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 356 (10) | 0.475 | +0.062 | 0.252 | 83% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 15 (10) | 4.865 | +1.473 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 20 (10) | 5.072 | -0.063 | 3.672 | 75% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 334 (10) | 0.989 | +0.027 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 356 (10) | 1.016 | +0.063 | 0.681 | 79% | — |
| team_goals | pf-nhl-F_stack (challenger) | 20 (10) | 1.040 | +0.350 | 0.733 | 100% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 334 (10) | 1.641 | -0.093 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 356 (10) | 1.646 | +0.236 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 20 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 20 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 334 (10) | -0.0029 [-0.0154, +0.0116] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 334 (10) | -0.0008 [-0.0030, +0.0013] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 189 (10) | +0.0018 [-0.0024, +0.0058] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 190 (10) | -0.0025 [-0.0093, +0.0053] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 15 (10) | -0.0109 [-0.0227, +0.0001] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 334 (10) | +0.0120 [-0.0496, +0.0673] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 28 projected goalie-games, named goalie started 71.4% (mean published P(start) 0.9081).
- participation CONFIRMED_ACTIVE: n=16, started 100.0%
- participation LIKELY_ACTIVE: n=12, started 33.3%

**Skater lineup check**: 369 projected skaters, 96.5% dressed.
- participation CONFIRMED_ACTIVE: n=55, dressed 98.2%
- participation LIKELY_ACTIVE: n=305, dressed 97.0%
- participation UNCERTAIN: n=9, dressed 66.7%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
