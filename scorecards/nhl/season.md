## NHL projection scorecard (season) — season to date

Generated 2026-10-31T11:14:37Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 55314 across 92 games. Settled: 20719 (void/DNP 812, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1991 (59) | 0.423 | +0.001 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 2086 (59) | 0.407 | -0.007 | 0.219 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1991 (59) | 0.280 | +0.000 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 2086 (59) | 0.273 | +0.001 | 0.141 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1991 (59) | 0.543 | +0.001 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 2086 (59) | 0.527 | -0.007 | 0.302 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 102 (58) | 5.036 | -0.880 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 114 (59) | 4.940 | -0.586 | 3.549 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1991 (59) | 1.002 | -0.085 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 2086 (59) | 0.997 | +0.027 | 0.671 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 118 (59) | 1.366 | +0.005 | 0.927 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1991 (59) | 1.865 | -0.408 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 2086 (59) | 1.759 | +0.030 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 1990 (59) | -0.0106 [-0.0150, -0.0061] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1990 (59) | -0.0010 [-0.0019, -0.0001] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 1344 (59) | -0.0010 [-0.0045, +0.0021] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 1342 (59) | -0.0014 [-0.0059, +0.0028] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 102 (58) | -0.0092 [-0.0206, +0.0017] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1990 (59) | -0.1069 [-0.1576, -0.0551] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 151 projected goalie-games, named goalie started 75.5% (mean published P(start) 0.9174).
- participation CONFIRMED_ACTIVE: n=87, started 100.0%
- participation LIKELY_ACTIVE: n=64, started 42.2%

**Skater lineup check**: 2186 projected skaters, 95.4% dressed.
- participation CONFIRMED_ACTIVE: n=275, dressed 97.5%
- participation CONFIRMED_OUT: n=5, dressed 20.0%
- participation LIKELY_ACTIVE: n=1874, dressed 96.2%
- participation UNCERTAIN: n=32, dressed 46.9%

**Availability capture**: mean coverage 1.0, newest capture age 15.4 min (median over recent runs), runs summarised: 12.
