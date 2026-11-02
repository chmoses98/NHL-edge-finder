## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-02T23:21:26Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 65017 across 101 games. Settled: 25454 (void/DNP 1079, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1124 (34) | 0.432 | -0.006 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1191 (34) | 0.410 | -0.017 | 0.222 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1124 (34) | 0.289 | -0.005 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1191 (34) | 0.278 | -0.007 | 0.146 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1124 (34) | 0.562 | -0.011 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1191 (34) | 0.537 | -0.024 | 0.311 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 50 (31) | 4.490 | +0.510 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 66 (34) | 4.503 | +0.568 | 3.333 | 88% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1124 (34) | 1.004 | -0.039 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1191 (34) | 1.006 | +0.071 | 0.668 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 68 (34) | 1.392 | -0.108 | 0.939 | 84% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1124 (34) | 1.848 | -0.351 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1191 (34) | 1.747 | +0.098 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 1124 (34) | -0.0057 [-0.0119, +0.0004] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 1124 (34) | -0.0015 [-0.0025, -0.0006] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 703 (34) | -0.0073 [-0.0116, -0.0033] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 703 (34) | -0.0100 [-0.0142, -0.0055] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 50 (31) | -0.0061 [-0.0224, +0.0096] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1124 (34) | -0.1061 [-0.1794, -0.0282] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 86 projected goalie-games, named goalie started 76.7% (mean published P(start) 0.9097).
- participation CONFIRMED_ACTIVE: n=48, started 100.0%
- participation LIKELY_ACTIVE: n=38, started 47.4%

**Skater lineup check**: 1256 projected skaters, 94.8% dressed.
- participation CONFIRMED_ACTIVE: n=150, dressed 94.7%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1081, dressed 95.7%
- participation UNCERTAIN: n=23, dressed 56.5%

**Availability capture**: mean coverage 1.0, newest capture age 5.8 min (median over recent runs), runs summarised: 12.
