## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-01T21:48:03Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 62040 across 97 games. Settled: 24111 (void/DNP 1027, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1134 (34) | 0.429 | -0.008 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1193 (34) | 0.409 | -0.021 | 0.222 | 79% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1134 (34) | 0.289 | -0.009 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1193 (34) | 0.277 | -0.009 | 0.146 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1134 (34) | 0.556 | -0.017 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1193 (34) | 0.534 | -0.030 | 0.310 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 49 (31) | 4.793 | +0.120 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 66 (34) | 4.950 | +0.595 | 3.660 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1134 (34) | 1.014 | -0.053 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1193 (34) | 1.012 | +0.058 | 0.675 | 79% | — |
| team_goals | pf-nhl-F_stack (challenger) | 68 (34) | 1.403 | -0.127 | 0.949 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1134 (34) | 1.891 | -0.368 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1193 (34) | 1.799 | +0.078 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 66 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 68 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1134 (34) | -0.0076 [-0.0135, -0.0013] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1134 (34) | -0.0015 [-0.0025, -0.0005] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 724 (34) | -0.0053 [-0.0092, -0.0016] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 724 (34) | -0.0072 [-0.0116, -0.0029] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 49 (31) | -0.0049 [-0.0204, +0.0104] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1134 (34) | -0.0913 [-0.1734, -0.0083] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 87 projected goalie-games, named goalie started 75.9% (mean published P(start) 0.8973).
- participation CONFIRMED_ACTIVE: n=43, started 100.0%
- participation LIKELY_ACTIVE: n=44, started 52.3%

**Skater lineup check**: 1257 projected skaters, 94.9% dressed.
- participation CONFIRMED_ACTIVE: n=114, dressed 93.0%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1119, dressed 95.9%
- participation UNCERTAIN: n=22, dressed 54.5%

**Availability capture**: mean coverage 1.0, newest capture age 16.7 min (median over recent runs), runs summarised: 12.
