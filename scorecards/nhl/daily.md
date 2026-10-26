## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-26T01:18:58Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 32212 across 50 games. Settled: 12628 (void/DNP 496, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1148 (34) | 0.427 | -0.007 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1200 (34) | 0.410 | -0.008 | 0.222 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1148 (34) | 0.280 | -0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1200 (34) | 0.275 | -0.001 | 0.142 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1148 (34) | 0.542 | -0.008 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1200 (34) | 0.527 | -0.009 | 0.303 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 62 (34) | 5.030 | -1.537 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 66 (34) | 4.767 | -1.401 | 3.408 | 85% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1148 (34) | 1.002 | -0.112 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1200 (34) | 0.999 | -0.001 | 0.677 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 68 (34) | 1.353 | -0.035 | 0.933 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1148 (34) | 1.864 | -0.443 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1200 (34) | 1.744 | +0.015 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 1148 (34) | -0.0115 [-0.0177, -0.0056] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1148 (34) | -0.0006 [-0.0017, +0.0005] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 805 (34) | +0.0002 [-0.0048, +0.0054] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 803 (34) | +0.0004 [-0.0065, +0.0072] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 62 (34) | -0.0110 [-0.0255, +0.0019] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1148 (34) | -0.1191 [-0.1771, -0.0627] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 89 projected goalie-games, named goalie started 74.2% (mean published P(start) 0.9228).
- participation CONFIRMED_ACTIVE: n=53, started 100.0%
- participation LIKELY_ACTIVE: n=36, started 36.1%

**Skater lineup check**: 1259 projected skaters, 95.3% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1038, dressed 96.2%
- participation UNCERTAIN: n=18, dressed 27.8%

**Availability capture**: mean coverage 1.0, newest capture age 13.4 min (median over recent runs), runs summarised: 12.
