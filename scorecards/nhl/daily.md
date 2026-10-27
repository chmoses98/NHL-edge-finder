## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-27T17:15:11Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 38798 across 64 games. Settled: 14051 (void/DNP 539, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1154 (34) | 0.428 | -0.011 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1204 (34) | 0.411 | -0.013 | 0.223 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1154 (34) | 0.281 | -0.004 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1204 (34) | 0.276 | -0.003 | 0.143 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1154 (34) | 0.545 | -0.015 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1204 (34) | 0.530 | -0.018 | 0.306 | 82% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 61 (34) | 5.150 | -1.550 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 66 (34) | 5.130 | -1.170 | 3.660 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1154 (34) | 1.017 | -0.110 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1204 (34) | 1.012 | -0.004 | 0.689 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 68 (34) | 1.428 | -0.080 | 0.988 | 78% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1154 (34) | 1.857 | -0.423 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1204 (34) | 1.744 | +0.030 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 1154 (34) | -0.0130 [-0.0196, -0.0067] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1154 (34) | -0.0008 [-0.0019, +0.0003] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 802 (34) | -0.0003 [-0.0052, +0.0043] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 800 (34) | -0.0005 [-0.0065, +0.0052] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 61 (34) | -0.0080 [-0.0220, +0.0050] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1154 (34) | -0.1124 [-0.1733, -0.0552] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 86 projected goalie-games, named goalie started 76.7% (mean published P(start) 0.9159).
- participation CONFIRMED_ACTIVE: n=48, started 100.0%
- participation LIKELY_ACTIVE: n=38, started 47.4%

**Skater lineup check**: 1257 projected skaters, 95.8% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1040, dressed 96.4%
- participation UNCERTAIN: n=14, dressed 28.6%

**Availability capture**: mean coverage 1.0, newest capture age 6.8 min (median over recent runs), runs summarised: 12.
