## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-08T23:25:20Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 94042 across 148 games. Settled: 32130 (void/DNP 1322, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 674 (20) | 0.426 | -0.014 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 706 (20) | 0.406 | -0.021 | 0.220 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 674 (20) | 0.286 | +0.003 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 706 (20) | 0.282 | -0.003 | 0.147 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 674 (20) | 0.545 | -0.011 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 706 (20) | 0.528 | -0.025 | 0.306 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 31 (20) | 5.504 | +0.512 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 40 (20) | 5.509 | +0.269 | 4.113 | 80% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 674 (20) | 1.004 | -0.076 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 706 (20) | 1.010 | +0.010 | 0.673 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 40 (20) | 1.179 | -0.056 | 0.830 | 85% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 674 (20) | 1.950 | -0.315 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 706 (20) | 1.841 | +0.083 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 40 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 40 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 672 (20) | -0.0027 [-0.0087, +0.0036] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 672 (20) | -0.0002 [-0.0016, +0.0014] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 436 (20) | -0.0037 [-0.0070, +0.0002] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 437 (20) | -0.0032 [-0.0076, +0.0012] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 31 (20) | +0.0092 [-0.0041, +0.0267] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 672 (20) | -0.1014 [-0.1633, -0.0363] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 49 projected goalie-games, named goalie started 81.6% (mean published P(start) 0.9171).
- participation CONFIRMED_ACTIVE: n=30, started 100.0%
- participation LIKELY_ACTIVE: n=19, started 52.6%

**Skater lineup check**: 736 projected skaters, 95.9% dressed.
- participation CONFIRMED_ACTIVE: n=38, dressed 94.7%
- participation LIKELY_ACTIVE: n=689, dressed 96.8%
- participation UNCERTAIN: n=9, dressed 33.3%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
