## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-07T21:05:01Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 89158 across 142 games. Settled: 31084 (void/DNP 1285, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 798 (24) | 0.437 | -0.022 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 843 (24) | 0.414 | -0.025 | 0.227 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 798 (24) | 0.292 | -0.005 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 843 (24) | 0.286 | -0.008 | 0.151 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 798 (24) | 0.572 | -0.027 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 843 (24) | 0.550 | -0.033 | 0.322 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 39 (24) | 4.715 | +0.563 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 48 (24) | 4.826 | +1.009 | 3.621 | 85% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 798 (24) | 0.989 | -0.016 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 843 (24) | 0.999 | +0.069 | 0.659 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 48 (24) | 1.328 | -0.130 | 0.920 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 798 (24) | 1.876 | -0.291 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 843 (24) | 1.762 | +0.143 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **WATCH** — CRPS 110% of historical holdout
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 48 settled forecasts (< 100)
- shots: **ALERT** — challenger worse than incumbent on identical forecasts (MAE): +0.0096 [+0.0006, +0.0193]
- team_goals: **INSUFFICIENT** — 48 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 796 (24) | -0.0000 [-0.0053, +0.0055] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 796 (24) | -0.0003 [-0.0016, +0.0011] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 525 (24) | -0.0061 [-0.0095, -0.0025] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 526 (24) | -0.0065 [-0.0106, -0.0025] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 39 (24) | +0.0058 [-0.0087, +0.0217] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 796 (24) | -0.1115 [-0.1670, -0.0503] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 60 projected goalie-games, named goalie started 80.0% (mean published P(start) 0.9173).
- participation CONFIRMED_ACTIVE: n=37, started 100.0%
- participation LIKELY_ACTIVE: n=23, started 47.8%

**Skater lineup check**: 882 projected skaters, 95.6% dressed.
- participation CONFIRMED_ACTIVE: n=74, dressed 97.3%
- participation LIKELY_ACTIVE: n=795, dressed 96.4%
- participation UNCERTAIN: n=13, dressed 38.5%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
