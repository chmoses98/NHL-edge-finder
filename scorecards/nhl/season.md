## NHL projection scorecard (season) — season to date

Generated 2026-10-25T23:02:50Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 32212 across 50 games. Settled: 12293 (void/DNP 481, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1183 (35) | 0.420 | +0.003 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1235 (35) | 0.404 | +0.003 | 0.215 | 82% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1183 (35) | 0.276 | +0.005 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1235 (35) | 0.272 | +0.005 | 0.139 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1183 (35) | 0.536 | +0.008 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1235 (35) | 0.522 | +0.007 | 0.297 | 82% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 65 (35) | 5.208 | -1.500 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 68 (35) | 4.925 | -1.471 | 3.517 | 82% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1183 (35) | 1.003 | -0.117 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1235 (35) | 0.998 | -0.001 | 0.679 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 70 (35) | 1.338 | +0.071 | 0.914 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1183 (35) | 1.871 | -0.456 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1235 (35) | 1.747 | +0.005 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 68 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 70 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1182 (35) | -0.0113 [-0.0172, -0.0051] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1182 (35) | -0.0004 [-0.0014, +0.0007] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 829 (35) | -0.0003 [-0.0050, +0.0043] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 827 (35) | +0.0005 [-0.0055, +0.0068] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 65 (35) | -0.0110 [-0.0267, +0.0024] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1182 (35) | -0.1247 [-0.1848, -0.0699] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 94 projected goalie-games, named goalie started 72.3% (mean published P(start) 0.9222).
- participation CONFIRMED_ACTIVE: n=56, started 100.0%
- participation LIKELY_ACTIVE: n=38, started 31.6%

**Skater lineup check**: 1295 projected skaters, 95.4% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1076, dressed 96.0%
- participation UNCERTAIN: n=16, dressed 31.2%

**Availability capture**: mean coverage 1.0, newest capture age 9.2 min (median over recent runs), runs summarised: 12.
