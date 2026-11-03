## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-03T18:34:56Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 70067 across 112 games. Settled: 26530 (void/DNP 1116, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1194 (36) | 0.427 | -0.003 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1263 (36) | 0.406 | -0.014 | 0.219 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1194 (36) | 0.289 | -0.004 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1263 (36) | 0.278 | -0.006 | 0.146 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1194 (36) | 0.553 | -0.007 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1263 (36) | 0.530 | -0.020 | 0.306 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 52 (33) | 4.405 | +0.688 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 70 (36) | 4.416 | +0.654 | 3.256 | 87% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1194 (36) | 0.995 | -0.027 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1263 (36) | 0.998 | +0.079 | 0.662 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 72 (36) | 1.363 | -0.097 | 0.920 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1194 (36) | 1.875 | -0.356 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1263 (36) | 1.768 | +0.086 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 70 settled forecasts (< 100)
- shots: **ALERT** — bias +0.079 (95% CI +0.010..+0.140) exceeds 5% of the mean
- team_goals: **INSUFFICIENT** — 72 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1194 (36) | -0.0030 [-0.0091, +0.0027] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 1194 (36) | -0.0014 [-0.0024, -0.0005] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 753 (36) | -0.0072 [-0.0107, -0.0035] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 753 (36) | -0.0095 [-0.0135, -0.0054] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 52 (33) | -0.0051 [-0.0202, +0.0115] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1194 (36) | -0.1127 [-0.1841, -0.0407] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 92 projected goalie-games, named goalie started 76.1% (mean published P(start) 0.9109).
- participation CONFIRMED_ACTIVE: n=52, started 100.0%
- participation LIKELY_ACTIVE: n=40, started 45.0%

**Skater lineup check**: 1330 projected skaters, 95.0% dressed.
- participation CONFIRMED_ACTIVE: n=150, dressed 94.7%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1156, dressed 95.8%
- participation UNCERTAIN: n=22, dressed 54.5%

**Availability capture**: mean coverage 1.0, newest capture age 5.2 min (median over recent runs), runs summarised: 12.
