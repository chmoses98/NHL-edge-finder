## NHL projection scorecard (season) — season to date

Generated 2026-10-28T03:03:12Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 41208 across 68 games. Settled: 14397 (void/DNP 550, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1384 (41) | 0.427 | -0.010 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1448 (41) | 0.408 | -0.010 | 0.221 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1384 (41) | 0.280 | -0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1448 (41) | 0.275 | -0.000 | 0.142 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1384 (41) | 0.543 | -0.010 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1448 (41) | 0.527 | -0.012 | 0.303 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 75 (41) | 5.308 | -1.423 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 80 (41) | 5.178 | -1.058 | 3.702 | 80% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1384 (41) | 1.007 | -0.111 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1448 (41) | 0.998 | +0.005 | 0.678 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 82 (41) | 1.369 | -0.019 | 0.939 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1384 (41) | 1.852 | -0.440 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1448 (41) | 1.738 | +0.028 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 80 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 82 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1383 (41) | -0.0128 [-0.0182, -0.0073] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1383 (41) | -0.0006 [-0.0016, +0.0004] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 963 (41) | -0.0004 [-0.0049, +0.0037] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 961 (41) | +0.0007 [-0.0052, +0.0061] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 75 (41) | -0.0128 [-0.0263, +0.0006] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1383 (41) | -0.1116 [-0.1692, -0.0546] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 110 projected goalie-games, named goalie started 72.7% (mean published P(start) 0.9126).
- participation CONFIRMED_ACTIVE: n=61, started 100.0%
- participation LIKELY_ACTIVE: n=49, started 38.8%

**Skater lineup check**: 1517 projected skaters, 95.5% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1293, dressed 96.1%
- participation UNCERTAIN: n=21, dressed 38.1%

**Availability capture**: mean coverage 1.0, newest capture age 9.6 min (median over recent runs), runs summarised: 12.
