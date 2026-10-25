## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-25T23:37:16Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 32212 across 50 games. Settled: 12293 (void/DNP 481, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1149 (34) | 0.423 | -0.001 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1200 (34) | 0.406 | -0.002 | 0.217 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1149 (34) | 0.279 | +0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1200 (34) | 0.275 | +0.003 | 0.141 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1149 (34) | 0.540 | +0.001 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1200 (34) | 0.525 | +0.000 | 0.300 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 63 (34) | 5.057 | -1.620 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 66 (34) | 4.806 | -1.602 | 3.443 | 85% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1149 (34) | 1.002 | -0.123 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1200 (34) | 0.998 | -0.010 | 0.679 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 68 (34) | 1.332 | +0.027 | 0.917 | 87% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1149 (34) | 1.867 | -0.443 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1200 (34) | 1.749 | +0.008 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 1148 (34) | -0.0112 [-0.0177, -0.0048] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1148 (34) | -0.0003 [-0.0013, +0.0008] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 808 (34) | -0.0002 [-0.0051, +0.0045] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 806 (34) | +0.0004 [-0.0057, +0.0065] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 63 (34) | -0.0090 [-0.0223, +0.0038] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1148 (34) | -0.1204 [-0.1762, -0.0612] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 91 projected goalie-games, named goalie started 72.5% (mean published P(start) 0.9243).
- participation CONFIRMED_ACTIVE: n=55, started 100.0%
- participation LIKELY_ACTIVE: n=36, started 30.6%

**Skater lineup check**: 1259 projected skaters, 95.3% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1040, dressed 96.0%
- participation UNCERTAIN: n=16, dressed 31.2%

**Availability capture**: mean coverage 1.0, newest capture age 11.4 min (median over recent runs), runs summarised: 12.
