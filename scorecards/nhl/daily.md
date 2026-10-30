## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-30T01:27:39Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 50238 across 79 games. Settled: 16856 (void/DNP 649, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 807 (24) | 0.429 | -0.001 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 849 (24) | 0.408 | -0.007 | 0.218 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 807 (24) | 0.283 | +0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 849 (24) | 0.273 | +0.002 | 0.140 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 807 (24) | 0.544 | -0.000 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 849 (24) | 0.522 | -0.005 | 0.299 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 39 (24) | 4.817 | -0.598 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 47 (24) | 4.668 | -0.066 | 3.495 | 87% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 807 (24) | 1.004 | -0.045 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 849 (24) | 0.998 | +0.051 | 0.668 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 48 (24) | 1.490 | +0.002 | 1.018 | 79% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 807 (24) | 1.825 | -0.382 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 849 (24) | 1.769 | +0.066 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 47 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 48 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 807 (24) | -0.0109 [-0.0166, -0.0049] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 807 (24) | -0.0016 [-0.0025, -0.0008] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 568 (24) | -0.0029 [-0.0071, +0.0012] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 568 (24) | -0.0038 [-0.0084, +0.0006] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 39 (24) | -0.0202 [-0.0399, -0.0008] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 807 (24) | -0.0674 [-0.1607, +0.0246] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 59 projected goalie-games, named goalie started 79.7% (mean published P(start) 0.9019).
- participation CONFIRMED_ACTIVE: n=32, started 100.0%
- participation LIKELY_ACTIVE: n=27, started 55.6%

**Skater lineup check**: 887 projected skaters, 95.7% dressed.
- participation CONFIRMED_ACTIVE: n=76, dressed 94.7%
- participation LIKELY_ACTIVE: n=797, dressed 96.6%
- participation UNCERTAIN: n=14, dressed 50.0%

**Availability capture**: mean coverage 1.0, newest capture age 4.7 min (median over recent runs), runs summarised: 12.
