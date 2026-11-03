## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-03T00:52:41Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 65057 across 101 games. Settled: 25454 (void/DNP 1079, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1090 (33) | 0.431 | -0.004 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1155 (33) | 0.409 | -0.015 | 0.221 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1090 (33) | 0.290 | -0.005 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1155 (33) | 0.278 | -0.006 | 0.146 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1090 (33) | 0.561 | -0.009 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1155 (33) | 0.537 | -0.022 | 0.310 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 48 (30) | 4.618 | +0.591 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 64 (33) | 4.586 | +0.644 | 3.377 | 86% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1090 (33) | 1.001 | -0.031 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1155 (33) | 1.003 | +0.076 | 0.665 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 66 (33) | 1.388 | -0.100 | 0.940 | 79% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1090 (33) | 1.855 | -0.355 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1155 (33) | 1.749 | +0.096 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 64 settled forecasts (< 100)
- shots: **ALERT** — bias +0.076 (95% CI +0.010..+0.145) exceeds 5% of the mean
- team_goals: **INSUFFICIENT** — 66 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1090 (33) | -0.0050 [-0.0110, +0.0013] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 1090 (33) | -0.0015 [-0.0025, -0.0005] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 682 (33) | -0.0074 [-0.0115, -0.0032] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 682 (33) | -0.0099 [-0.0142, -0.0054] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 48 (30) | -0.0063 [-0.0216, +0.0107] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1090 (33) | -0.1122 [-0.1875, -0.0406] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 84 projected goalie-games, named goalie started 76.2% (mean published P(start) 0.91).
- participation CONFIRMED_ACTIVE: n=47, started 100.0%
- participation LIKELY_ACTIVE: n=37, started 46.0%

**Skater lineup check**: 1218 projected skaters, 94.8% dressed.
- participation CONFIRMED_ACTIVE: n=150, dressed 94.7%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1044, dressed 95.7%
- participation UNCERTAIN: n=22, dressed 54.5%

**Availability capture**: mean coverage 1.0, newest capture age 8.3 min (median over recent runs), runs summarised: 12.
