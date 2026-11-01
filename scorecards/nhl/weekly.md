## NHL projection scorecard (weekly) — last 28 days

Generated 2026-11-01T22:15:59Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 62040 across 97 games. Settled: 24111 (void/DNP 1027, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 2317 (69) | 0.425 | -0.002 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 2428 (69) | 0.406 | -0.009 | 0.219 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 2317 (69) | 0.282 | -0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 2428 (69) | 0.275 | -0.002 | 0.142 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 2317 (69) | 0.546 | -0.004 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 2428 (69) | 0.528 | -0.011 | 0.303 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 114 (66) | 5.029 | -0.804 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 134 (69) | 4.938 | -0.453 | 3.588 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 2317 (69) | 1.009 | -0.085 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 2428 (69) | 1.005 | +0.028 | 0.677 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 138 (69) | 1.370 | -0.027 | 0.931 | 80% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 2317 (69) | 1.881 | -0.413 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 2428 (69) | 1.773 | +0.041 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **OK** — within expectations
- shots: **OK** — within expectations
- team_goals: **OK** — within expectations
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 2316 (69) | -0.0095 [-0.0135, -0.0051] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 2316 (69) | -0.0009 [-0.0017, -0.0002] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 1553 (69) | -0.0026 [-0.0059, +0.0006] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 1551 (69) | -0.0031 [-0.0070, +0.0009] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 114 (66) | -0.0084 [-0.0188, +0.0011] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 2316 (69) | -0.1084 [-0.1569, -0.0603] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 181 projected goalie-games, named goalie started 74.0% (mean published P(start) 0.9102).
- participation CONFIRMED_ACTIVE: n=99, started 100.0%
- participation LIKELY_ACTIVE: n=82, started 42.7%

**Skater lineup check**: 2552 projected skaters, 95.1% dressed.
- participation CONFIRMED_ACTIVE: n=313, dressed 96.8%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2195, dressed 96.0%
- participation UNCERTAIN: n=38, dressed 44.7%

**Availability capture**: mean coverage 1.0, newest capture age 17.9 min (median over recent runs), runs summarised: 12.
