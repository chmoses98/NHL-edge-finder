## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-23T23:20:23Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 19431 across 33 games. Settled: 8442 (void/DNP 332, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 812 (24) | 0.417 | +0.005 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 848 (24) | 0.403 | +0.003 | 0.216 | 83% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 812 (24) | 0.272 | +0.009 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 848 (24) | 0.269 | +0.009 | 0.136 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 812 (24) | 0.536 | +0.014 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 848 (24) | 0.525 | +0.011 | 0.298 | 83% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 47 (24) | 5.444 | -2.060 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 47 (24) | 5.414 | -1.841 | 3.826 | 79% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 812 (24) | 1.000 | -0.149 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 848 (24) | 0.993 | -0.019 | 0.678 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 48 (24) | 1.295 | +0.162 | 0.876 | 85% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 812 (24) | 1.908 | -0.460 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 848 (24) | 1.763 | -0.003 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 47 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 48 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 811 (24) | -0.0112 [-0.0201, -0.0031] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 811 (24) | +0.0001 [-0.0014, +0.0015] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 579 (24) | +0.0015 [-0.0043, +0.0072] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 577 (24) | +0.0028 [-0.0050, +0.0100] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 47 (24) | -0.0018 [-0.0158, +0.0122] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 811 (24) | -0.1415 [-0.2118, -0.0759] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 69 projected goalie-games, named goalie started 68.1% (mean published P(start) 0.9228).
- participation CONFIRMED_ACTIVE: n=40, started 100.0%
- participation LIKELY_ACTIVE: n=29, started 24.1%

**Skater lineup check**: 891 projected skaters, 95.2% dressed.
- participation CONFIRMED_ACTIVE: n=161, dressed 100.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=716, dressed 95.5%
- participation UNCERTAIN: n=10, dressed 30.0%

**Availability capture**: mean coverage 1.0, newest capture age 11.0 min (median over recent runs), runs summarised: 12.
