## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-19T17:09:39Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 1835 across 6 games. Settled: 692 (void/DNP 33, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 67 (2) | 0.357 | +0.106 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 69 (2) | 0.333 | +0.111 | 0.144 | 84% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 67 (2) | 0.235 | +0.056 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 69 (2) | 0.228 | +0.053 | 0.099 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 67 (2) | 0.451 | +0.162 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 69 (2) | 0.437 | +0.166 | 0.213 | 84% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 4 (2) | 8.995 | -2.870 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 4 (2) | 8.500 | -2.629 | 5.683 | 50% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 67 (2) | 1.018 | -0.230 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 69 (2) | 0.980 | -0.050 | 0.707 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 4 (2) | 1.202 | +1.051 | 0.707 | 100% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 67 (2) | 1.659 | -0.667 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 69 (2) | 1.584 | -0.237 | — | — | — |

**Drift checks**

- assists: **INSUFFICIENT** — 69 settled forecasts (< 100)
- goals: **INSUFFICIENT** — 69 settled forecasts (< 100)
- points: **INSUFFICIENT** — 69 settled forecasts (< 100)
- saves: **INSUFFICIENT** — 4 settled forecasts (< 100)
- shots: **INSUFFICIENT** — 69 settled forecasts (< 100)
- team_goals: **INSUFFICIENT** — 4 settled forecasts (< 100)
- toi_minutes: **INSUFFICIENT** — 69 settled forecasts (< 100)

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 66 (2) | -0.0080 [-0.0144, -0.0011] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 66 (2) | +0.0007 [-0.0037, +0.0053] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 44 (2) | -0.0012 [-0.0025, -0.0001] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 44 (2) | +0.0082 [+0.0061, +0.0101] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 4 (2) | -0.0247 [-0.0755, +0.0261] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 66 (2) | -0.0798 [-0.2710, +0.1234] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 7 projected goalie-games, named goalie started 57.1% (mean published P(start) 0.8775).
- participation CONFIRMED_ACTIVE: n=3, started 100.0%
- participation LIKELY_ACTIVE: n=4, started 25.0%

**Skater lineup check**: 72 projected skaters, 95.8% dressed.
- participation LIKELY_ACTIVE: n=72, dressed 95.8%

**Availability capture**: mean coverage 1.0, newest capture age 3.1 min (median over recent runs), runs summarised: 4.
