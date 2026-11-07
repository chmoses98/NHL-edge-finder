## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-07T23:07:23Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 89284 across 142 games. Settled: 31434 (void/DNP 1285, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 768 (23) | 0.433 | -0.017 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 810 (23) | 0.410 | -0.021 | 0.223 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 768 (23) | 0.289 | +0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 810 (23) | 0.282 | -0.002 | 0.148 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 768 (23) | 0.561 | -0.015 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 810 (23) | 0.539 | -0.023 | 0.313 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 37 (23) | 4.945 | +0.592 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 46 (23) | 5.039 | +1.007 | 3.719 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 768 (23) | 0.996 | -0.017 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 810 (23) | 0.997 | +0.073 | 0.656 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 46 (23) | 1.345 | -0.058 | 0.934 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 768 (23) | 1.877 | -0.285 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 810 (23) | 1.780 | +0.151 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 46 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 46 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 766 (23) | -0.0014 [-0.0067, +0.0046] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 766 (23) | -0.0006 [-0.0019, +0.0009] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 494 (23) | -0.0059 [-0.0096, -0.0022] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 495 (23) | -0.0062 [-0.0102, -0.0021] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 37 (23) | +0.0050 [-0.0102, +0.0228] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 766 (23) | -0.0913 [-0.1488, -0.0386] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 55 projected goalie-games, named goalie started 83.6% (mean published P(start) 0.9211).
- participation CONFIRMED_ACTIVE: n=35, started 100.0%
- participation LIKELY_ACTIVE: n=20, started 55.0%

**Skater lineup check**: 845 projected skaters, 95.9% dressed.
- participation CONFIRMED_ACTIVE: n=74, dressed 97.3%
- participation LIKELY_ACTIVE: n=759, dressed 96.6%
- participation UNCERTAIN: n=12, dressed 41.7%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
