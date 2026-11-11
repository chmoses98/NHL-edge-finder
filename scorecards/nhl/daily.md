## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-11T00:07:20Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 99607 across 158 games. Settled: 32495 (void/DNP 1324, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 305 (9) | 0.392 | +0.048 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 318 (9) | 0.371 | +0.036 | 0.185 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 305 (9) | 0.267 | +0.027 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 318 (9) | 0.263 | +0.020 | 0.128 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 305 (9) | 0.506 | +0.075 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 318 (9) | 0.488 | +0.054 | 0.262 | 82% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 13 (9) | 4.397 | -0.066 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 18 (9) | 4.906 | -1.168 | 3.622 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 305 (9) | 1.011 | -0.099 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 318 (9) | 1.012 | -0.032 | 0.680 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 18 (9) | 1.050 | +0.364 | 0.750 | 89% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 305 (9) | 1.916 | -0.304 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 318 (9) | 1.867 | +0.029 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 18 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 18 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 304 (9) | -0.0111 [-0.0201, -0.0025] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 304 (9) | -0.0004 [-0.0027, +0.0021] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 178 (9) | -0.0014 [-0.0062, +0.0041] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 179 (9) | -0.0025 [-0.0099, +0.0050] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 13 (9) | -0.0037 [-0.0171, +0.0142] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 304 (9) | -0.0428 [-0.1477, +0.0644] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 23 projected goalie-games, named goalie started 78.3% (mean published P(start) 0.896).
- participation CONFIRMED_ACTIVE: n=11, started 100.0%
- participation LIKELY_ACTIVE: n=12, started 58.3%

**Skater lineup check**: 332 projected skaters, 95.8% dressed.
- participation CONFIRMED_ACTIVE: n=19, dressed 94.7%
- participation LIKELY_ACTIVE: n=307, dressed 97.1%
- participation UNCERTAIN: n=6, dressed 33.3%

**Availability capture**: mean coverage 1.0, newest capture age 16.1 min (median over recent runs), runs summarised: 12.
