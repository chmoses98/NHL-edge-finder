## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-26T17:04:02Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 33507 across 53 games. Settled: 13340 (void/DNP 508, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1217 (36) | 0.427 | -0.007 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1271 (36) | 0.410 | -0.008 | 0.222 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1217 (36) | 0.280 | -0.000 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1271 (36) | 0.275 | +0.001 | 0.142 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1217 (36) | 0.543 | -0.007 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1271 (36) | 0.528 | -0.009 | 0.303 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 66 (36) | 5.148 | -1.501 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 70 (36) | 4.879 | -1.379 | 3.458 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1217 (36) | 1.003 | -0.109 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1271 (36) | 0.999 | +0.002 | 0.678 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 72 (36) | 1.389 | -0.013 | 0.952 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1217 (36) | 1.875 | -0.421 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1271 (36) | 1.752 | +0.038 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 70 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 72 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1217 (36) | -0.0115 [-0.0176, -0.0055] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1217 (36) | -0.0007 [-0.0017, +0.0004] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 854 (36) | +0.0001 [-0.0047, +0.0049] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 852 (36) | +0.0006 [-0.0054, +0.0069] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 66 (36) | -0.0108 [-0.0243, +0.0024] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1217 (36) | -0.1200 [-0.1783, -0.0672] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 95 projected goalie-games, named goalie started 73.7% (mean published P(start) 0.9166).
- participation CONFIRMED_ACTIVE: n=54, started 100.0%
- participation LIKELY_ACTIVE: n=41, started 39.0%

**Skater lineup check**: 1332 projected skaters, 95.4% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1111, dressed 96.2%
- participation UNCERTAIN: n=18, dressed 27.8%

**Availability capture**: mean coverage 1.0, newest capture age 11.2 min (median over recent runs), runs summarised: 12.
