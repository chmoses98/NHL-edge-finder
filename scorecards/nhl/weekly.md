## NHL projection scorecard (weekly) — last 28 days

Generated 2026-10-25T20:11:30Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 31988 across 50 games. Settled: 11933 (void/DNP 471, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1148 (34) | 0.422 | +0.002 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1199 (34) | 0.406 | +0.002 | 0.216 | 82% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1148 (34) | 0.277 | +0.004 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1199 (34) | 0.273 | +0.004 | 0.139 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1148 (34) | 0.540 | +0.006 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1199 (34) | 0.526 | +0.005 | 0.299 | 82% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 64 (34) | 5.255 | -1.557 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 66 (34) | 5.005 | -1.477 | 3.565 | 82% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1148 (34) | 1.008 | -0.118 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1199 (34) | 1.005 | -0.002 | 0.683 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 68 (34) | 1.361 | +0.056 | 0.928 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1148 (34) | 1.864 | -0.482 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1199 (34) | 1.742 | -0.008 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 1147 (34) | -0.0109 [-0.0172, -0.0049] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1147 (34) | -0.0003 [-0.0014, +0.0009] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 809 (34) | +0.0002 [-0.0045, +0.0049] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 807 (34) | +0.0011 [-0.0053, +0.0077] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 64 (34) | -0.0100 [-0.0240, +0.0034] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1147 (34) | -0.1219 [-0.1766, -0.0670] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 92 projected goalie-games, named goalie started 71.7% (mean published P(start) 0.923).
- participation CONFIRMED_ACTIVE: n=55, started 100.0%
- participation LIKELY_ACTIVE: n=37, started 29.7%

**Skater lineup check**: 1258 projected skaters, 95.3% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1040, dressed 96.0%
- participation UNCERTAIN: n=15, dressed 26.7%

**Availability capture**: mean coverage 1.0, newest capture age 12.6 min (median over recent runs), runs summarised: 12.
