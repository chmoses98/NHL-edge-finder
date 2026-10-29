## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-29T00:39:29Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 43884 across 68 games. Settled: 16516 (void/DNP 639, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1050 (31) | 0.432 | -0.004 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1100 (31) | 0.412 | -0.010 | 0.223 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1050 (31) | 0.281 | +0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1100 (31) | 0.271 | +0.001 | 0.139 | 82% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1050 (31) | 0.551 | -0.004 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1100 (31) | 0.530 | -0.009 | 0.306 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 53 (31) | 5.200 | -1.250 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 60 (31) | 5.067 | -0.693 | 3.743 | 87% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1050 (31) | 1.007 | -0.080 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1100 (31) | 1.008 | +0.021 | 0.678 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 62 (31) | 1.526 | +0.006 | 1.053 | 77% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1050 (31) | 1.828 | -0.440 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1100 (31) | 1.745 | +0.011 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 60 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 62 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1050 (31) | -0.0108 [-0.0176, -0.0044] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1050 (31) | -0.0012 [-0.0021, -0.0004] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 752 (31) | -0.0005 [-0.0057, +0.0045] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 751 (31) | -0.0008 [-0.0074, +0.0053] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 53 (31) | -0.0180 [-0.0350, -0.0015] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1050 (31) | -0.0869 [-0.1609, -0.0152] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 81 projected goalie-games, named goalie started 74.1% (mean published P(start) 0.904).
- participation CONFIRMED_ACTIVE: n=43, started 100.0%
- participation LIKELY_ACTIVE: n=38, started 44.7%

**Skater lineup check**: 1147 projected skaters, 95.9% dressed.
- participation CONFIRMED_ACTIVE: n=237, dressed 98.3%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=889, dressed 96.7%
- participation UNCERTAIN: n=17, dressed 41.2%

**Availability capture**: mean coverage 1.0, newest capture age 10.6 min (median over recent runs), runs summarised: 12.
