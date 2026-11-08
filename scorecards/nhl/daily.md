## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-08T02:50:15Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 90201 across 142 games. Settled: 31785 (void/DNP 1296, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 768 (23) | 0.437 | -0.021 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 810 (23) | 0.414 | -0.027 | 0.227 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 768 (23) | 0.291 | -0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 810 (23) | 0.284 | -0.006 | 0.150 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 768 (23) | 0.563 | -0.023 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 810 (23) | 0.542 | -0.034 | 0.316 | 78% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 37 (23) | 5.135 | +0.810 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 46 (23) | 5.170 | +1.112 | 3.841 | 85% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 768 (23) | 0.995 | -0.035 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 810 (23) | 0.996 | +0.055 | 0.658 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 46 (23) | 1.321 | -0.122 | 0.928 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 768 (23) | 1.839 | -0.299 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 810 (23) | 1.740 | +0.125 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 46 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 46 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 766 (23) | -0.0018 [-0.0075, +0.0038] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 766 (23) | -0.0006 [-0.0019, +0.0008] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 491 (23) | -0.0053 [-0.0091, -0.0015] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 492 (23) | -0.0054 [-0.0096, -0.0010] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 37 (23) | +0.0048 [-0.0102, +0.0225] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 766 (23) | -0.0934 [-0.1472, -0.0339] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 56 projected goalie-games, named goalie started 82.1% (mean published P(start) 0.9156).
- participation CONFIRMED_ACTIVE: n=34, started 100.0%
- participation LIKELY_ACTIVE: n=22, started 54.5%

**Skater lineup check**: 844 projected skaters, 96.0% dressed.
- participation CONFIRMED_ACTIVE: n=74, dressed 97.3%
- participation LIKELY_ACTIVE: n=759, dressed 96.7%
- participation UNCERTAIN: n=11, dressed 36.4%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
