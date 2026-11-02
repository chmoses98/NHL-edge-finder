## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-02T00:48:30Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 62456 across 97 games. Settled: 24768 (void/DNP 1063, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1094 (33) | 0.433 | -0.010 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1156 (33) | 0.412 | -0.022 | 0.225 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1094 (33) | 0.290 | -0.008 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1156 (33) | 0.278 | -0.009 | 0.147 | 82% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1094 (33) | 0.560 | -0.019 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1156 (33) | 0.537 | -0.031 | 0.312 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 48 (30) | 4.435 | +0.621 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 64 (33) | 4.653 | +0.854 | 3.520 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1094 (33) | 1.008 | -0.038 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1156 (33) | 1.006 | +0.072 | 0.669 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 66 (33) | 1.387 | -0.146 | 0.943 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1094 (33) | 1.862 | -0.367 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1156 (33) | 1.770 | +0.082 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 1094 (33) | -0.0071 [-0.0145, -0.0011] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1094 (33) | -0.0014 [-0.0024, -0.0004] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 688 (33) | -0.0062 [-0.0100, -0.0024] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 688 (33) | -0.0086 [-0.0129, -0.0039] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 48 (30) | -0.0071 [-0.0222, +0.0092] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1094 (33) | -0.0959 [-0.1853, -0.0107] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 84 projected goalie-games, named goalie started 76.2% (mean published P(start) 0.9057).
- participation CONFIRMED_ACTIVE: n=45, started 100.0%
- participation LIKELY_ACTIVE: n=39, started 48.7%

**Skater lineup check**: 1220 projected skaters, 94.8% dressed.
- participation CONFIRMED_ACTIVE: n=114, dressed 93.0%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1082, dressed 95.6%
- participation UNCERTAIN: n=22, dressed 63.6%

**Availability capture**: mean coverage 1.0, newest capture age 17.4 min (median over recent runs), runs summarised: 12.
