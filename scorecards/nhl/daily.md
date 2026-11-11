## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-11T15:24:53Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 100813 across 164 games. Settled: 33883 (void/DNP 1361, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 366 (11) | 0.403 | +0.048 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 391 (11) | 0.377 | +0.036 | 0.189 | 83% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 366 (11) | 0.268 | +0.034 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 391 (11) | 0.263 | +0.021 | 0.128 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 366 (11) | 0.498 | +0.082 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 391 (11) | 0.479 | +0.057 | 0.259 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 17 (11) | 4.265 | +0.746 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 22 (11) | 4.630 | -0.413 | 3.392 | 82% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 366 (11) | 0.998 | -0.012 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 391 (11) | 1.019 | +0.040 | 0.683 | 78% | — |
| team_goals | pf-nhl-F_stack (challenger) | 22 (11) | 1.091 | +0.335 | 0.754 | 86% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 366 (11) | 1.737 | -0.119 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 391 (11) | 1.742 | +0.169 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 22 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 22 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 366 (11) | -0.0029 [-0.0148, +0.0096] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 366 (11) | -0.0006 [-0.0025, +0.0014] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 211 (11) | -0.0003 [-0.0047, +0.0038] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 212 (11) | -0.0018 [-0.0083, +0.0042] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 17 (11) | -0.0098 [-0.0181, -0.0015] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 366 (11) | +0.0027 [-0.0923, +0.0804] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 29 projected goalie-games, named goalie started 75.9% (mean published P(start) 0.9099).
- participation CONFIRMED_ACTIVE: n=16, started 100.0%
- participation LIKELY_ACTIVE: n=13, started 46.2%

**Skater lineup check**: 408 projected skaters, 95.8% dressed.
- participation CONFIRMED_ACTIVE: n=19, dressed 94.7%
- participation LIKELY_ACTIVE: n=379, dressed 96.8%
- participation UNCERTAIN: n=10, dressed 60.0%

**Availability capture**: mean coverage 1.0, newest capture age 16.6 min (median over recent runs), runs summarised: 12.
