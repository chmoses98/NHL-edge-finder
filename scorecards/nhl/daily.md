## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-01T23:51:59Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 62358 across 97 games. Settled: 24467 (void/DNP 1027, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1102 (33) | 0.431 | -0.009 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1159 (33) | 0.411 | -0.021 | 0.223 | 82% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1102 (33) | 0.289 | -0.008 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1159 (33) | 0.278 | -0.008 | 0.147 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1102 (33) | 0.559 | -0.017 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1159 (33) | 0.537 | -0.029 | 0.312 | 79% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 48 (30) | 4.479 | +0.423 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 64 (33) | 4.711 | +0.743 | 3.554 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1102 (33) | 1.014 | -0.042 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1159 (33) | 1.014 | +0.067 | 0.674 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 66 (33) | 1.413 | -0.130 | 0.955 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1102 (33) | 1.874 | -0.367 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1159 (33) | 1.782 | +0.083 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 1102 (33) | -0.0074 [-0.0137, -0.0013] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1102 (33) | -0.0014 [-0.0024, -0.0004] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 690 (33) | -0.0062 [-0.0103, -0.0019] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 690 (33) | -0.0082 [-0.0132, -0.0035] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 48 (30) | -0.0055 [-0.0221, +0.0110] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1102 (33) | -0.0956 [-0.1796, -0.0218] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 85 projected goalie-games, named goalie started 75.3% (mean published P(start) 0.902).
- participation CONFIRMED_ACTIVE: n=44, started 100.0%
- participation LIKELY_ACTIVE: n=41, started 48.8%

**Skater lineup check**: 1220 projected skaters, 95.0% dressed.
- participation CONFIRMED_ACTIVE: n=114, dressed 93.0%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1084, dressed 95.9%
- participation UNCERTAIN: n=20, dressed 60.0%

**Availability capture**: mean coverage 1.0, newest capture age 16.7 min (median over recent runs), runs summarised: 12.
