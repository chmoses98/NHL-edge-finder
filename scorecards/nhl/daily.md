## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-01T22:15:59Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 62040 across 97 games. Settled: 24111 (void/DNP 1027, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1102 (33) | 0.427 | -0.004 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1159 (33) | 0.407 | -0.017 | 0.220 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1102 (33) | 0.288 | -0.006 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1159 (33) | 0.277 | -0.006 | 0.145 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1102 (33) | 0.556 | -0.010 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1159 (33) | 0.534 | -0.023 | 0.309 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 48 (30) | 4.699 | +0.316 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 64 (33) | 4.891 | +0.661 | 3.641 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1102 (33) | 1.015 | -0.049 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1159 (33) | 1.013 | +0.063 | 0.675 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 66 (33) | 1.398 | -0.084 | 0.943 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1102 (33) | 1.912 | -0.366 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1159 (33) | 1.813 | +0.083 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 64 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 66 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1102 (33) | -0.0074 [-0.0135, -0.0010] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1102 (33) | -0.0014 [-0.0023, -0.0003] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 704 (33) | -0.0060 [-0.0101, -0.0020] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 704 (33) | -0.0078 [-0.0122, -0.0032] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 48 (30) | -0.0037 [-0.0188, +0.0124] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1102 (33) | -0.0989 [-0.1850, -0.0249] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 85 projected goalie-games, named goalie started 75.3% (mean published P(start) 0.8998).
- participation CONFIRMED_ACTIVE: n=43, started 100.0%
- participation LIKELY_ACTIVE: n=42, started 50.0%

**Skater lineup check**: 1221 projected skaters, 94.9% dressed.
- participation CONFIRMED_ACTIVE: n=114, dressed 93.0%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1085, dressed 95.8%
- participation UNCERTAIN: n=20, dressed 60.0%

**Availability capture**: mean coverage 1.0, newest capture age 17.9 min (median over recent runs), runs summarised: 12.
