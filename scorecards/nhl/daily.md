## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-22T22:41:42Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 18204 across 31 games. Settled: 5591 (void/DNP 243, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 537 (16) | 0.403 | +0.015 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 562 (16) | 0.387 | +0.017 | 0.202 | 83% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 537 (16) | 0.267 | +0.017 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 562 (16) | 0.268 | +0.015 | 0.134 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 537 (16) | 0.516 | +0.032 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 562 (16) | 0.507 | +0.031 | 0.281 | 83% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 32 (16) | 5.208 | -1.640 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 32 (16) | 5.214 | -1.409 | 3.631 | 78% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 537 (16) | 1.002 | -0.131 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 562 (16) | 0.981 | +0.011 | 0.670 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 32 (16) | 1.142 | +0.262 | 0.753 | 94% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 537 (16) | 1.966 | -0.416 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 562 (16) | 1.825 | +0.056 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 32 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 32 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 536 (16) | -0.0131 [-0.0207, -0.0057] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 536 (16) | +0.0002 [-0.0017, +0.0023] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 364 (16) | -0.0005 [-0.0048, +0.0032] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 363 (16) | +0.0020 [-0.0047, +0.0085] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 32 (16) | +0.0031 [-0.0143, +0.0173] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 536 (16) | -0.1460 [-0.2260, -0.0574] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 45 projected goalie-games, named goalie started 71.1% (mean published P(start) 0.926).
- participation CONFIRMED_ACTIVE: n=27, started 100.0%
- participation LIKELY_ACTIVE: n=18, started 27.8%

**Skater lineup check**: 595 projected skaters, 94.5% dressed.
- participation LIKELY_ACTIVE: n=588, dressed 95.1%
- participation UNCERTAIN: n=7, dressed 42.9%

**Availability capture**: mean coverage 1.0, newest capture age 4.2 min (median over recent runs), runs summarised: 12.
