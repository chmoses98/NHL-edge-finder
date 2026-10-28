## NHL projection scorecard (weekly) — last 28 days

Generated 2026-10-28T23:08:02Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 43594 across 68 games. Settled: 16516 (void/DNP 639, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1587 (47) | 0.422 | +0.002 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1662 (47) | 0.404 | -0.001 | 0.216 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1587 (47) | 0.276 | +0.006 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1662 (47) | 0.270 | +0.006 | 0.137 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1587 (47) | 0.539 | +0.008 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1662 (47) | 0.522 | +0.004 | 0.297 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 85 (47) | 5.203 | -1.397 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 92 (47) | 5.118 | -0.942 | 3.704 | 82% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1587 (47) | 1.006 | -0.097 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1662 (47) | 0.999 | +0.017 | 0.675 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 94 (47) | 1.395 | +0.093 | 0.951 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1587 (47) | 1.875 | -0.432 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1662 (47) | 1.772 | +0.026 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 92 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 94 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1586 (47) | -0.0116 [-0.0170, -0.0067] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1586 (47) | -0.0008 [-0.0017, +0.0001] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 1116 (47) | -0.0005 [-0.0045, +0.0033] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 1114 (47) | +0.0001 [-0.0048, +0.0050] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 85 (47) | -0.0101 [-0.0222, +0.0017] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1586 (47) | -0.1069 [-0.1669, -0.0536] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 126 projected goalie-games, named goalie started 73.0% (mean published P(start) 0.9119).
- participation CONFIRMED_ACTIVE: n=70, started 100.0%
- participation LIKELY_ACTIVE: n=56, started 39.3%

**Skater lineup check**: 1742 projected skaters, 95.4% dressed.
- participation CONFIRMED_ACTIVE: n=237, dressed 98.3%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1477, dressed 96.1%
- participation UNCERTAIN: n=24, dressed 41.7%

**Availability capture**: mean coverage 1.0, newest capture age 17.9 min (median over recent runs), runs summarised: 12.
