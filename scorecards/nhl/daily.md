## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-07T16:01:52Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 87463 across 142 games. Settled: 30739 (void/DNP 1274, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 961 (29) | 0.438 | -0.026 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1011 (29) | 0.414 | -0.029 | 0.227 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 961 (29) | 0.294 | -0.007 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1011 (29) | 0.286 | -0.009 | 0.152 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 961 (29) | 0.568 | -0.033 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1011 (29) | 0.545 | -0.038 | 0.320 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 44 (27) | 5.010 | +0.547 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 58 (29) | 4.926 | +0.784 | 3.700 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 961 (29) | 1.015 | -0.039 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1011 (29) | 1.019 | +0.062 | 0.678 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 58 (29) | 1.358 | -0.164 | 0.931 | 86% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 961 (29) | 1.883 | -0.361 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1011 (29) | 1.765 | +0.108 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **WATCH** — CRPS 111% of historical holdout
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 58 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 58 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 959 (29) | -0.0018 [-0.0074, +0.0038] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 959 (29) | -0.0007 [-0.0018, +0.0005] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 625 (29) | -0.0074 [-0.0119, -0.0037] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 626 (29) | -0.0078 [-0.0122, -0.0035] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 44 (27) | +0.0021 [-0.0132, +0.0190] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 959 (29) | -0.1156 [-0.1819, -0.0517] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 75 projected goalie-games, named goalie started 77.3% (mean published P(start) 0.9037).
- participation CONFIRMED_ACTIVE: n=41, started 100.0%
- participation LIKELY_ACTIVE: n=34, started 50.0%

**Skater lineup check**: 1066 projected skaters, 94.8% dressed.
- participation CONFIRMED_ACTIVE: n=112, dressed 95.5%
- participation CONFIRMED_OUT: n=1, dressed 100.0%
- participation LIKELY_ACTIVE: n=938, dressed 95.7%
- participation UNCERTAIN: n=15, dressed 33.3%

**Availability capture**: mean coverage 1.0, newest capture age 4.4 min (median over recent runs), runs summarised: 12.
