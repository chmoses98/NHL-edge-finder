## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-04T01:31:23Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 70444 across 112 games. Settled: 26530 (void/DNP 1116, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 959 (29) | 0.434 | -0.017 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1013 (29) | 0.413 | -0.028 | 0.226 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 959 (29) | 0.296 | -0.015 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1013 (29) | 0.286 | -0.017 | 0.154 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 959 (29) | 0.560 | -0.032 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1013 (29) | 0.538 | -0.044 | 0.316 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 40 (26) | 4.146 | +1.018 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 56 (29) | 4.229 | +0.710 | 3.080 | 88% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 959 (29) | 0.997 | -0.037 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1013 (29) | 1.001 | +0.069 | 0.667 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 58 (29) | 1.344 | -0.281 | 0.910 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 959 (29) | 1.843 | -0.328 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1013 (29) | 1.730 | +0.109 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **ALERT** — bias -0.017 (95% CI -0.034..-0.001) exceeds 5% of the mean; CRPS 112% of historical holdout
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 56 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 58 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 959 (29) | -0.0019 [-0.0084, +0.0046] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 959 (29) | -0.0013 [-0.0024, -0.0002] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 575 (29) | -0.0083 [-0.0129, -0.0038] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 575 (29) | -0.0111 [-0.0163, -0.0060] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 40 (26) | -0.0046 [-0.0206, +0.0125] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 959 (29) | -0.1106 [-0.1823, -0.0331] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 73 projected goalie-games, named goalie started 76.7% (mean published P(start) 0.9111).
- participation CONFIRMED_ACTIVE: n=41, started 100.0%
- participation LIKELY_ACTIVE: n=32, started 46.9%

**Skater lineup check**: 1068 projected skaters, 94.8% dressed.
- participation CONFIRMED_ACTIVE: n=112, dressed 94.6%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=936, dressed 95.7%
- participation UNCERTAIN: n=18, dressed 50.0%

**Availability capture**: mean coverage 1.0, newest capture age 10.1 min (median over recent runs), runs summarised: 12.
