## NHL projection scorecard (weekly) — last 28 days

Generated 2026-11-01T00:36:59Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 59197 across 92 games. Settled: 22744 (void/DNP 963, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 2187 (65) | 0.424 | -0.002 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 2289 (65) | 0.407 | -0.008 | 0.219 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 2187 (65) | 0.282 | -0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 2289 (65) | 0.274 | -0.001 | 0.142 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 2187 (65) | 0.544 | -0.003 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 2289 (65) | 0.526 | -0.010 | 0.302 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 108 (62) | 5.125 | -0.842 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 126 (65) | 4.956 | -0.611 | 3.574 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 2187 (65) | 1.011 | -0.091 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 2289 (65) | 1.004 | +0.025 | 0.677 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 130 (65) | 1.362 | -0.025 | 0.925 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 2187 (65) | 1.884 | -0.421 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 2289 (65) | 1.779 | +0.029 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 2186 (65) | -0.0107 [-0.0152, -0.0067] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 2186 (65) | -0.0010 [-0.0018, -0.0002] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 1463 (65) | -0.0021 [-0.0056, +0.0011] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 1461 (65) | -0.0025 [-0.0071, +0.0018] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 108 (62) | -0.0102 [-0.0211, +0.0002] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 2186 (65) | -0.1065 [-0.1610, -0.0552] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 169 projected goalie-games, named goalie started 74.6% (mean published P(start) 0.9115).
- participation CONFIRMED_ACTIVE: n=93, started 100.0%
- participation LIKELY_ACTIVE: n=76, started 43.4%

**Skater lineup check**: 2406 projected skaters, 95.1% dressed.
- participation CONFIRMED_ACTIVE: n=313, dressed 96.8%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2052, dressed 96.0%
- participation UNCERTAIN: n=35, dressed 42.9%

**Availability capture**: mean coverage 1.0, newest capture age 11.9 min (median over recent runs), runs summarised: 12.
