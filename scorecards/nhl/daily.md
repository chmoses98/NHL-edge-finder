## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-29T14:32:46Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 47238 across 79 games. Settled: 16856 (void/DNP 649, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1082 (32) | 0.433 | -0.004 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1135 (32) | 0.414 | -0.011 | 0.225 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1082 (32) | 0.282 | -0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1135 (32) | 0.272 | +0.001 | 0.140 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1082 (32) | 0.553 | -0.005 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1135 (32) | 0.532 | -0.011 | 0.307 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 54 (32) | 5.131 | -1.253 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 62 (32) | 4.951 | -0.719 | 3.676 | 87% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1082 (32) | 1.002 | -0.080 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1135 (32) | 1.003 | +0.019 | 0.675 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 64 (32) | 1.517 | -0.008 | 1.044 | 78% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1082 (32) | 1.817 | -0.423 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1135 (32) | 1.737 | +0.019 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 1082 (32) | -0.0100 [-0.0173, -0.0032] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1082 (32) | -0.0013 [-0.0021, -0.0004] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 783 (32) | -0.0007 [-0.0060, +0.0043] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 782 (32) | -0.0016 [-0.0085, +0.0047] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 54 (32) | -0.0181 [-0.0342, -0.0016] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1082 (32) | -0.0840 [-0.1591, -0.0167] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 83 projected goalie-games, named goalie started 74.7% (mean published P(start) 0.9063).
- participation CONFIRMED_ACTIVE: n=45, started 100.0%
- participation LIKELY_ACTIVE: n=38, started 44.7%

**Skater lineup check**: 1183 projected skaters, 95.9% dressed.
- participation CONFIRMED_ACTIVE: n=237, dressed 98.3%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=925, dressed 96.8%
- participation UNCERTAIN: n=17, dressed 41.2%

**Availability capture**: mean coverage 1.0, newest capture age 9.2 min (median over recent runs), runs summarised: 12.
