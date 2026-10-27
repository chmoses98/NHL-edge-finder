## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-27T00:44:33Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 34091 across 53 games. Settled: 13340 (void/DNP 508, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1119 (33) | 0.427 | -0.011 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1166 (33) | 0.411 | -0.013 | 0.223 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1119 (33) | 0.281 | -0.003 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1166 (33) | 0.276 | -0.002 | 0.142 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1119 (33) | 0.545 | -0.014 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1166 (33) | 0.531 | -0.016 | 0.306 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 60 (33) | 5.322 | -1.397 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 64 (33) | 5.062 | -1.305 | 3.558 | 81% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1119 (33) | 1.007 | -0.102 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1166 (33) | 1.005 | +0.004 | 0.683 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 66 (33) | 1.411 | -0.059 | 0.973 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1119 (33) | 1.867 | -0.429 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1166 (33) | 1.735 | +0.026 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 1119 (33) | -0.0113 [-0.0181, -0.0050] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1119 (33) | -0.0008 [-0.0020, +0.0003] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 787 (33) | -0.0002 [-0.0052, +0.0047] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 785 (33) | +0.0000 [-0.0063, +0.0061] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 60 (33) | -0.0089 [-0.0241, +0.0039] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1119 (33) | -0.1307 [-0.1856, -0.0686] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 85 projected goalie-games, named goalie started 75.3% (mean published P(start) 0.9172).
- participation CONFIRMED_ACTIVE: n=48, started 100.0%
- participation LIKELY_ACTIVE: n=37, started 43.2%

**Skater lineup check**: 1219 projected skaters, 95.7% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1002, dressed 96.4%
- participation UNCERTAIN: n=14, dressed 21.4%

**Availability capture**: mean coverage 1.0, newest capture age 10.7 min (median over recent runs), runs summarised: 12.
