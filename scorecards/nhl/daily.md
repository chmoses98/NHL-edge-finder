## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-08T19:19:40Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 93439 across 148 games. Settled: 31785 (void/DNP 1296, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 735 (22) | 0.435 | -0.020 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 775 (22) | 0.414 | -0.026 | 0.227 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 735 (22) | 0.290 | -0.000 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 775 (22) | 0.283 | -0.005 | 0.149 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 735 (22) | 0.560 | -0.020 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 775 (22) | 0.540 | -0.031 | 0.315 | 79% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 36 (22) | 5.121 | +0.989 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 44 (22) | 4.908 | +0.966 | 3.665 | 86% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 735 (22) | 0.993 | -0.030 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 775 (22) | 0.994 | +0.059 | 0.657 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 44 (22) | 1.242 | -0.106 | 0.873 | 91% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 735 (22) | 1.853 | -0.313 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 775 (22) | 1.752 | +0.104 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 44 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 44 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 733 (22) | -0.0018 [-0.0076, +0.0036] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 733 (22) | -0.0005 [-0.0020, +0.0009] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 470 (22) | -0.0044 [-0.0076, -0.0011] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 471 (22) | -0.0046 [-0.0091, -0.0001] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 36 (22) | +0.0025 [-0.0120, +0.0187] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 733 (22) | -0.0975 [-0.1501, -0.0365] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 53 projected goalie-games, named goalie started 83.0% (mean published P(start) 0.9188).
- participation CONFIRMED_ACTIVE: n=33, started 100.0%
- participation LIKELY_ACTIVE: n=20, started 55.0%

**Skater lineup check**: 808 projected skaters, 95.9% dressed.
- participation CONFIRMED_ACTIVE: n=74, dressed 97.3%
- participation LIKELY_ACTIVE: n=723, dressed 96.7%
- participation UNCERTAIN: n=11, dressed 36.4%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
