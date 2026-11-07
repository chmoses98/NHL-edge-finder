## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-07T19:01:31Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 88561 across 142 games. Settled: 30739 (void/DNP 1274, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 831 (25) | 0.437 | -0.022 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 875 (25) | 0.414 | -0.025 | 0.226 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 831 (25) | 0.291 | -0.004 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 875 (25) | 0.283 | -0.006 | 0.149 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 831 (25) | 0.571 | -0.025 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 875 (25) | 0.550 | -0.031 | 0.320 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 40 (24) | 4.665 | +0.498 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 50 (25) | 4.738 | +0.864 | 3.571 | 86% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 831 (25) | 1.015 | -0.029 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 875 (25) | 1.024 | +0.062 | 0.677 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 50 (25) | 1.348 | -0.085 | 0.924 | 84% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 831 (25) | 1.847 | -0.302 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 875 (25) | 1.737 | +0.144 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 50 settled forecasts (< 100)
- shots: **ALERT** — challenger worse than incumbent on identical forecasts (MAE): +0.0103 [+0.0016, +0.0197]
- team_goals: **INSUFFICIENT** — 50 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 829 (25) | -0.0003 [-0.0060, +0.0049] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 829 (25) | -0.0006 [-0.0017, +0.0006] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 559 (25) | -0.0061 [-0.0099, -0.0020] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 560 (25) | -0.0066 [-0.0110, -0.0022] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 40 (24) | +0.0026 [-0.0147, +0.0181] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 829 (25) | -0.1107 [-0.1775, -0.0389] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 64 projected goalie-games, named goalie started 78.1% (mean published P(start) 0.91).
- participation CONFIRMED_ACTIVE: n=37, started 100.0%
- participation LIKELY_ACTIVE: n=27, started 48.1%

**Skater lineup check**: 919 projected skaters, 95.2% dressed.
- participation CONFIRMED_ACTIVE: n=74, dressed 97.3%
- participation LIKELY_ACTIVE: n=831, dressed 96.0%
- participation UNCERTAIN: n=14, dressed 35.7%

**Availability capture**: mean coverage 1.0, newest capture age 4.4 min (median over recent runs), runs summarised: 12.
