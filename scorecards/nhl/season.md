## NHL projection scorecard (season) — season to date

Generated 2026-10-31T23:05:38Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 59193 across 92 games. Settled: 22069 (void/DNP 915, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 2121 (63) | 0.425 | -0.003 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 2222 (63) | 0.407 | -0.009 | 0.220 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 2121 (63) | 0.282 | -0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 2222 (63) | 0.275 | -0.002 | 0.143 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 2121 (63) | 0.543 | -0.004 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 2222 (63) | 0.526 | -0.011 | 0.303 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 106 (61) | 5.165 | -0.808 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 122 (63) | 5.016 | -0.529 | 3.612 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 2121 (63) | 1.003 | -0.086 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 2222 (63) | 0.996 | +0.029 | 0.671 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 126 (63) | 1.369 | -0.037 | 0.931 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 2121 (63) | 1.880 | -0.428 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 2222 (63) | 1.771 | +0.020 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 2120 (63) | -0.0106 [-0.0152, -0.0062] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 2120 (63) | -0.0010 [-0.0018, -0.0002] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 1410 (63) | -0.0018 [-0.0052, +0.0017] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 1408 (63) | -0.0021 [-0.0067, +0.0023] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 106 (61) | -0.0090 [-0.0200, +0.0017] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 2120 (63) | -0.1094 [-0.1585, -0.0616] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 162 projected goalie-games, named goalie started 75.3% (mean published P(start) 0.914).
- participation CONFIRMED_ACTIVE: n=91, started 100.0%
- participation LIKELY_ACTIVE: n=71, started 43.7%

**Skater lineup check**: 2333 projected skaters, 95.2% dressed.
- participation CONFIRMED_ACTIVE: n=313, dressed 96.8%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=1981, dressed 96.0%
- participation UNCERTAIN: n=33, dressed 45.5%

**Availability capture**: mean coverage 1.0, newest capture age 9.4 min (median over recent runs), runs summarised: 12.
