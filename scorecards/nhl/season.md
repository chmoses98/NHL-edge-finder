## NHL projection scorecard (season) — season to date

Generated 2026-10-30T23:03:59Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 52429 across 82 games. Settled: 19666 (void/DNP 761, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1889 (56) | 0.424 | +0.000 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1980 (56) | 0.407 | -0.007 | 0.219 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1889 (56) | 0.279 | +0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1980 (56) | 0.272 | +0.003 | 0.140 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1889 (56) | 0.541 | +0.003 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1980 (56) | 0.525 | -0.004 | 0.301 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 100 (56) | 5.095 | -0.940 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 109 (56) | 4.972 | -0.571 | 3.583 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1889 (56) | 1.002 | -0.086 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1980 (56) | 0.996 | +0.027 | 0.670 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 112 (56) | 1.352 | +0.040 | 0.921 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1889 (56) | 1.880 | -0.416 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1980 (56) | 1.771 | +0.025 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 1888 (56) | -0.0109 [-0.0155, -0.0061] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1888 (56) | -0.0009 [-0.0018, -0.0001] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 1290 (56) | -0.0009 [-0.0045, +0.0025] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 1288 (56) | -0.0008 [-0.0054, +0.0037] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 100 (56) | -0.0081 [-0.0190, +0.0024] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1888 (56) | -0.1109 [-0.1658, -0.0575] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 145 projected goalie-games, named goalie started 75.2% (mean published P(start) 0.9183).
- participation CONFIRMED_ACTIVE: n=84, started 100.0%
- participation LIKELY_ACTIVE: n=61, started 41.0%

**Skater lineup check**: 2074 projected skaters, 95.5% dressed.
- participation CONFIRMED_ACTIVE: n=237, dressed 98.3%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1802, dressed 96.1%
- participation UNCERTAIN: n=31, dressed 48.4%

**Availability capture**: mean coverage 1.0, newest capture age 15.4 min (median over recent runs), runs summarised: 12.
