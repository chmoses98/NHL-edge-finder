## NHL projection scorecard (weekly) — last 28 days

Generated 2026-10-26T01:18:58Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 32212 across 50 games. Settled: 12628 (void/DNP 496, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1215 (36) | 0.423 | -0.001 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1269 (36) | 0.406 | -0.001 | 0.217 | 82% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1215 (36) | 0.277 | +0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1269 (36) | 0.273 | +0.002 | 0.140 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1215 (36) | 0.537 | +0.001 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1269 (36) | 0.522 | +0.000 | 0.298 | 82% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 66 (36) | 5.270 | -1.618 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 70 (36) | 4.980 | -1.471 | 3.538 | 81% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1215 (36) | 1.003 | -0.119 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1269 (36) | 0.998 | -0.004 | 0.679 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 72 (36) | 1.344 | +0.025 | 0.921 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1215 (36) | 1.852 | -0.456 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1269 (36) | 1.735 | +0.002 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 1214 (36) | -0.0114 [-0.0177, -0.0056] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1214 (36) | -0.0005 [-0.0016, +0.0006] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 849 (36) | +0.0001 [-0.0045, +0.0048] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 847 (36) | +0.0008 [-0.0050, +0.0068] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 66 (36) | -0.0118 [-0.0261, +0.0009] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1214 (36) | -0.1170 [-0.1735, -0.0576] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 96 projected goalie-games, named goalie started 72.9% (mean published P(start) 0.9195).
- participation CONFIRMED_ACTIVE: n=56, started 100.0%
- participation LIKELY_ACTIVE: n=40, started 35.0%

**Skater lineup check**: 1331 projected skaters, 95.3% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1110, dressed 96.1%
- participation UNCERTAIN: n=18, dressed 27.8%

**Availability capture**: mean coverage 1.0, newest capture age 13.4 min (median over recent runs), runs summarised: 12.
