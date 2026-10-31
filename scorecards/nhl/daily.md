## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-31T20:17:47Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 59189 across 92 games. Settled: 20719 (void/DNP 812, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1082 (32) | 0.429 | -0.004 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1136 (32) | 0.411 | -0.016 | 0.223 | 79% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1082 (32) | 0.287 | -0.008 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1136 (32) | 0.276 | -0.007 | 0.144 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1082 (32) | 0.547 | -0.011 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1136 (32) | 0.527 | -0.024 | 0.305 | 82% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 51 (31) | 4.714 | -0.202 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 62 (32) | 4.690 | +0.154 | 3.393 | 89% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1082 (32) | 1.003 | -0.057 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1136 (32) | 1.001 | +0.042 | 0.669 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 64 (32) | 1.434 | -0.118 | 0.975 | 80% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1082 (32) | 1.859 | -0.389 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1136 (32) | 1.776 | +0.040 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 62 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 64 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1082 (32) | -0.0099 [-0.0150, -0.0044] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1082 (32) | -0.0019 [-0.0029, -0.0010] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 711 (32) | -0.0031 [-0.0067, +0.0006] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 711 (32) | -0.0050 [-0.0094, -0.0008] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 51 (31) | -0.0113 [-0.0276, +0.0044] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1082 (32) | -0.0826 [-0.1669, -0.0063] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 76 projected goalie-games, named goalie started 81.6% (mean published P(start) 0.9116).
- participation CONFIRMED_ACTIVE: n=43, started 100.0%
- participation LIKELY_ACTIVE: n=33, started 57.6%

**Skater lineup check**: 1186 projected skaters, 95.8% dressed.
- participation CONFIRMED_ACTIVE: n=95, dressed 93.7%
- participation CONFIRMED_OUT: n=1, dressed 100.0%
- participation LIKELY_ACTIVE: n=1070, dressed 96.6%
- participation UNCERTAIN: n=20, dressed 60.0%

**Availability capture**: mean coverage 1.0, newest capture age 6.2 min (median over recent runs), runs summarised: 12.
