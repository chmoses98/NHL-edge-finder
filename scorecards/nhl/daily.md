## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-28T22:07:10Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 43495 across 68 games. Settled: 16516 (void/DNP 639, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1117 (33) | 0.429 | -0.001 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1171 (33) | 0.409 | -0.006 | 0.220 | 79% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1117 (33) | 0.278 | +0.004 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1171 (33) | 0.270 | +0.003 | 0.138 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1117 (33) | 0.546 | +0.003 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1171 (33) | 0.526 | -0.003 | 0.302 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 57 (33) | 5.029 | -1.167 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 64 (33) | 4.950 | -0.643 | 3.658 | 88% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1117 (33) | 1.002 | -0.073 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1171 (33) | 1.002 | +0.024 | 0.673 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 66 (33) | 1.527 | +0.044 | 1.050 | 71% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1117 (33) | 1.833 | -0.422 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1171 (33) | 1.751 | +0.036 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 64 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 66 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1117 (33) | -0.0108 [-0.0173, -0.0044] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1117 (33) | -0.0009 [-0.0018, +0.0000] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 805 (33) | -0.0004 [-0.0051, +0.0044] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 805 (33) | -0.0006 [-0.0063, +0.0056] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 57 (33) | -0.0143 [-0.0303, +0.0012] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1117 (33) | -0.0877 [-0.1601, -0.0192] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 85 projected goalie-games, named goalie started 75.3% (mean published P(start) 0.9082).
- participation CONFIRMED_ACTIVE: n=46, started 100.0%
- participation LIKELY_ACTIVE: n=39, started 46.2%

**Skater lineup check**: 1220 projected skaters, 96.0% dressed.
- participation CONFIRMED_ACTIVE: n=237, dressed 98.3%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=962, dressed 96.8%
- participation UNCERTAIN: n=17, dressed 41.2%

**Availability capture**: mean coverage 1.0, newest capture age 17.9 min (median over recent runs), runs summarised: 12.
