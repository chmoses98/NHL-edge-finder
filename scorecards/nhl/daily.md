## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-31T22:31:38Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 59193 across 92 games. Settled: 22069 (void/DNP 915, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1212 (36) | 0.431 | -0.009 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1272 (36) | 0.411 | -0.020 | 0.224 | 79% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1212 (36) | 0.290 | -0.010 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1272 (36) | 0.279 | -0.010 | 0.147 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1212 (36) | 0.547 | -0.019 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1272 (36) | 0.526 | -0.030 | 0.306 | 82% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 55 (34) | 4.986 | -0.112 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 70 (36) | 4.851 | +0.169 | 3.520 | 87% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1212 (36) | 1.004 | -0.062 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1272 (36) | 1.000 | +0.043 | 0.670 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 72 (36) | 1.433 | -0.178 | 0.976 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1212 (36) | 1.886 | -0.427 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1272 (36) | 1.795 | +0.022 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 70 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 72 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1212 (36) | -0.0100 [-0.0148, -0.0046] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1212 (36) | -0.0018 [-0.0027, -0.0009] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 777 (36) | -0.0044 [-0.0083, -0.0008] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 777 (36) | -0.0061 [-0.0104, -0.0020] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 55 (34) | -0.0107 [-0.0246, +0.0049] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1212 (36) | -0.0895 [-0.1627, -0.0225] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 87 projected goalie-games, named goalie started 80.5% (mean published P(start) 0.906).
- participation CONFIRMED_ACTIVE: n=47, started 100.0%
- participation LIKELY_ACTIVE: n=40, started 57.5%

**Skater lineup check**: 1333 projected skaters, 95.4% dressed.
- participation CONFIRMED_ACTIVE: n=133, dressed 93.2%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1177, dressed 96.4%
- participation UNCERTAIN: n=21, dressed 57.1%

**Availability capture**: mean coverage 1.0, newest capture age 9.4 min (median over recent runs), runs summarised: 12.
