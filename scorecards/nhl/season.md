## NHL projection scorecard (season) — season to date

Generated 2026-10-28T00:39:32Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 40372 across 64 games. Settled: 14051 (void/DNP 539, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1352 (40) | 0.426 | -0.007 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1412 (40) | 0.409 | -0.008 | 0.221 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1352 (40) | 0.279 | +0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1412 (40) | 0.275 | +0.000 | 0.142 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1352 (40) | 0.541 | -0.006 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1412 (40) | 0.527 | -0.008 | 0.303 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 73 (40) | 5.192 | -1.559 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 78 (40) | 5.110 | -1.189 | 3.657 | 81% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1352 (40) | 1.009 | -0.116 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1412 (40) | 1.001 | -0.001 | 0.682 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 80 (40) | 1.388 | -0.007 | 0.949 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1352 (40) | 1.852 | -0.425 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1412 (40) | 1.745 | +0.032 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 78 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 80 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1351 (40) | -0.0122 [-0.0176, -0.0066] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1351 (40) | -0.0006 [-0.0016, +0.0005] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 938 (40) | +0.0001 [-0.0046, +0.0042] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 936 (40) | +0.0010 [-0.0047, +0.0065] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 73 (40) | -0.0106 [-0.0238, +0.0020] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1351 (40) | -0.1044 [-0.1544, -0.0441] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 107 projected goalie-games, named goalie started 72.9% (mean published P(start) 0.9122).
- participation CONFIRMED_ACTIVE: n=59, started 100.0%
- participation LIKELY_ACTIVE: n=48, started 39.6%

**Skater lineup check**: 1480 projected skaters, 95.4% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1257, dressed 96.1%
- participation UNCERTAIN: n=20, dressed 35.0%

**Availability capture**: mean coverage 1.0, newest capture age 12.4 min (median over recent runs), runs summarised: 12.
