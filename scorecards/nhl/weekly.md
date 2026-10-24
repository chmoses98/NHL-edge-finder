## NHL projection scorecard (weekly) — last 28 days

Generated 2026-10-24T08:10:30Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 21779 across 45 games. Settled: 8788 (void/DNP 347, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 846 (25) | 0.416 | +0.010 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 882 (25) | 0.402 | +0.008 | 0.214 | 83% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 846 (25) | 0.271 | +0.012 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 882 (25) | 0.269 | +0.011 | 0.135 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 846 (25) | 0.539 | +0.022 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 882 (25) | 0.527 | +0.018 | 0.298 | 83% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 49 (25) | 5.271 | -1.929 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 49 (25) | 5.232 | -1.729 | 3.732 | 80% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 846 (25) | 1.003 | -0.141 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 882 (25) | 0.995 | -0.009 | 0.678 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 50 (25) | 1.293 | +0.182 | 0.873 | 86% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 846 (25) | 1.897 | -0.440 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 882 (25) | 1.758 | +0.003 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 49 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 50 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 845 (25) | -0.0115 [-0.0194, -0.0036] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 845 (25) | -0.0000 [-0.0015, +0.0013] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 597 (25) | +0.0014 [-0.0043, +0.0069] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 595 (25) | +0.0025 [-0.0056, +0.0093] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 49 (25) | -0.0032 [-0.0166, +0.0090] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 845 (25) | -0.1358 [-0.1996, -0.0728] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 71 projected goalie-games, named goalie started 69.0% (mean published P(start) 0.9249).
- participation CONFIRMED_ACTIVE: n=42, started 100.0%
- participation LIKELY_ACTIVE: n=29, started 24.1%

**Skater lineup check**: 927 projected skaters, 95.2% dressed.
- participation CONFIRMED_ACTIVE: n=161, dressed 100.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=751, dressed 95.6%
- participation UNCERTAIN: n=11, dressed 27.3%

**Availability capture**: mean coverage 1.0, newest capture age 12.9 min (median over recent runs), runs summarised: 12.
