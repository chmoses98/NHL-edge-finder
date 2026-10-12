# Workload vs efficiency audit of the production player projections (2026-10-12)

**Authority: RESEARCH_ONLY.** A diagnostic of PLAYER_SIM_V1 (the production shadow arm behind `player_shadow` in every
packet). No production code, model, workflow or wagering path changes. Numbers: `docs/research/workload_v1/audit_2025.json`
(held-out 2025-26) and `audit_2024.json` (2024-25, the development / validation season). Code:
`src/nhl_edge/research/workload_audit.py`; run with
`python -m nhl_edge.research.workload_experiment audit --season 2025 --cache <dir>`.

## 1. How production produces these numbers today

* **Skater TOI / PP TOI / SOG** (`players.roster.build_roster`, called from `workflows/shadow_player.py`):
  expected TOI by state = the player's deployment share of the team's seconds in that state (EV / PP / SH / EA / EN / OT;
  exponentially weighted, 6-game half-life, 0.5 pseudo-games of the position mean; tonight's DailyFaceoff lines blended
  in when archived) x a fixed team-minute template `{ev 50.6, pp 4.4 x p_pp / 0.215, sh 4.4, ea 0.6, en 0.6, ot 1.2}`,
  where `p_pp` is the PP share of the team's expected GOALS from the DATA_ONLY_V2 components. Expected SOG = sum over
  EV / PP / SH of expected minutes x the player's raw (unshrunk) SOG per 60 in that state (60-game half-life). There is
  no SOG distribution and no opponent term in the SOG mean. Kalshi lists no NHL shots market (`KALSHI_MARKET_MAP.md`), so
  `expected_shots` is a packet field only.
* **Goalie saves** (`players.saves.simulate_saves`): per nhl-sim-2.0 draw, saves ~ NegBin around expected shots faced
  x league save fraction, with game-script terms (regulation margin, goals against, OT) and a pull hazard. Expected shots
  faced = point-in-time league level x opponent shots-for factor x own shots-against factor x venue
  (`players.params.ShotRates`). The saves mean does not depend on which goalie starts; the starter's status /
  confidence is reported next to the probability, not multiplied in (Kalshi settles a goalie who never enters at the
  pre-game fair price).
* **Live parameters** `data/params/player-sim-1.0.json` are fit on 2021-22 .. 2025-26. This audit never uses them: every
  league-level parameter is refit on seasons strictly before the test season (`player_walk_forward.fit_season_params`).

## 2. Data sources

| source | used here | notes |
|---|---|---|
| NHL api-web boxscore / play-by-play + NHL stats shift charts, cached as `data/history/players/*_<season>.parquet` | yes, all of it | pulled by `player_research_data.yml` on a GitHub runner (2025-26: 1,394 games, 0 errors, `pulled_at_utc` 2026-09-30T05:35:53Z, run 36673561068). 2025-26: 1,312 regular-season games, 100% with shift charts; 2024-25: 57 games without shift charts (state minutes unknown there) |
| `docs/research/walk_forward_v2_wf2_20260929_games.csv` | champion only | DATA_ONLY_V2 point-in-time team lambdas and penalty ratings, 2024-25 and 2025-26 |
| live NHL API from this session | **not reachable** | `api-web.nhle.com` was refused by this session's egress policy (proxy 403), so no spot re-fetch was possible; the committed cache is the official API output with per-season manifests |
| DailyFaceoff starting goalies / lines | no | archived only from 2026-09-30: **no point-in-time starter or lineup source exists for 2021-26** |

`pure_forecast.v1` / `pure_gate`: no occurrence anywhere in this repository (code or docs).

## 3. Market-derived inputs (direct and indirect)

* **PLAYER_SIM_V1 TOI / SOG / saves: none.** The chain is official NHL events -> player/team features -> DATA_ONLY_V2
  lambdas (xG ratings, special teams, goalie talent; DATA_ONLY never reads the quarantined `context/sportsbook_odds`) ->
  simulation. The research modules added here are checked by a test to import no Kalshi / pricing / execution code.
* **Side by side, not inside:** every player row also carries `p_market_anchored` = MARKET_ANCHORED_PLAYER_V1 (logit
  blend, 0.8 weight on the Kalshi mid). It is market-derived: its disagreement with the market is not independent
  evidence.
* **Indirect exposure, handled:** the DailyFaceoff goalie page carries sportsbook moneyline / spread fields; they are
  stripped before archiving (`data.goalies.strip_market_fields`). The NHL schedule feed's partner odds are archived
  only under the quarantined `context/sportsbook_odds` kind, read by MARKET_ANCHORED arms and the thesis-card benchmark
  (`thesis/benchmark.py`), never by DATA_ONLY / PLAYER_SIM_V1. DailyFaceoff line combinations and "Confirmed / Likely"
  goalie labels are newsroom information, not prices. Track A status: sports-only.

## 4. Skater shots on goal, 2025-26 held-out (47,231 skater-games, 1,312 games)

Identity used: `pred - y = workload + efficiency + omitted`, where workload = (predicted - actual minutes) at the
champion's own rates, efficiency = (champion rates x actual minutes) - actual EV/PP/SH shots, omitted = shots in states
the mean never counts (overtime, extra attacker / empty net).

| quantity | value |
|---|---|
| mean actual / predicted SOG | 1.546 / 1.467 (bias -0.079) |
| total MAE / RMSE / MSE | 1.011 / 1.325 / 1.755 |
| Poisson noise floor (MSE of a perfect Poisson mean) | ~1.47 to 1.55 |
| MSE with the ACTUAL minutes (champion rates) | 1.672: oracle minutes remove 4.7% of the MSE, about 30-40% of the reducible part |
| workload component | MAE 0.192, RMSE 0.269, bias -0.040 |
| efficiency component | MAE 0.978, RMSE 1.261, bias +0.032 (mostly irreducible count noise) |
| omitted states (OT / EA / EN shots) | bias -0.071 per skater-game |

Workload (minutes per skater-game, champion minus actual): total TOI MAE 1.93, bias **-0.34**; PP MAE 0.79, bias
**-0.19** (predicted 1.22 vs actual 1.41, -14%); SH MAE 0.67, bias **-0.18**; EV incl. OT MAE 1.85, bias -0.01.
2024-25 (45,176 rows): oracle minutes remove 4.2%; PP bias -0.14, SH -0.11, total TOI -0.22.

**Why PP / SH minutes run low.** `team_states` (`data.player_events.state_timeline`) fills every period to its full
20 minutes, so every regular-season OT game has `n_seconds = 4800` (all 1,459 regular-season OT games 2021-26) and the phantom
(20 min - actual OT) is booked to the last strength state. The share denominators are inflated in a quarter of all games
(EV on-ice ratio 4.51 skaters vs 4.99 in regulation games, 2025-26); the EV template 50.6 is itself the inflated mean, so
EV roughly cancels, but PP and SH (template 4.4 vs 5.1 actual per team-game in regulation) do not. `tsec_ot` is the
constant 1,200 s, so the OT share is ~15x too small (predicted OT TOI 0.038 min vs 0.578 actual in OT games).

**Overtime.** 24.8% of 2025-26 games (326) went to OT. In OT games the champion's SOG bias is -0.119 (regulation games
-0.066) and TOI bias -0.75 min (regulation -0.20): the 0.103 OT shots per skater are never counted, the EV rate's
numerator excludes OT shots while its minutes include OT minutes, and `ot 1.2` adds minutes the EV template already holds.

By position: forwards SOG bias -0.102 (n 31,370), defence -0.034 (n 15,861).

## 5. Goalie saves, 2025-26 held-out (2,624 starts, 1,312 games; CONDITIONAL_ON_ACTUAL_STARTER)

Identity: `E[saves] - saves = (E[faced] - SA) x sv^ + (SA x sv^ - saves)`, sv^ = the draws' implied save fraction.

| quantity | value |
|---|---|
| mean actual / predicted saves | 24.16 / 24.08 (bias -0.08) |
| total MAE / RMSE / MSE | 5.35 / 6.82 / 46.5 |
| shots faced by the starter: actual / predicted | 26.96 / 26.95; MAE 5.33, RMSE 6.80 |
| MSE left with the ACTUAL shots faced | 2.55: **94.5% of the saves MSE is workload** (2024-25: 94.5%) |
| efficiency (saves given actual shots) | MAE 1.29, RMSE 1.60, bias -0.07; implied sv 0.893 vs 0.896 actual |
| pulled starters | 144 (5.5%; predicted 6.2%), MAE 12.9, bias +12.1: 24% of the total MSE |
| full-game starters | 2,480, MAE 4.91, bias -0.79 |

**Overtime.** The model's mean P(OT) is 0.216; 0.248 of games went to OT. Split by the REALISED outcome, OT-game saves
are under-predicted by 1.35 and regulation-game saves over-predicted by 0.34: any pregame forecast shows this split; the
mean over all games is right.

## 6. Starting goalies

No point-in-time starter source exists for 2021-26, so every saves number here is conditional on the actual starter. As
a pregame-computable stand-in, "most starts in the team's last 10 games, rotate on the second night of a back-to-back"
named the right goalie in **63.8%** of 2,623 team-games in 2025-26 (78.8% of 430 back-to-backs; 2024-25: 67.3%); "the
previous game's starter" only 40.7%. When that rule was wrong (n 950) the champion's saves error was MAE 5.40, bias -0.41
vs MAE 5.32, bias +0.11 when right (n 1,673); the actual starters' save fractions were the same (0.896 both). Because the
production saves mean is goalie-agnostic, a wrong starter changes which contract is live, not the number. The archived
DailyFaceoff statuses (from 2026-09-30) are the only way to measure real pregame starter accuracy; that is prospective.

## 7. What this says to build

Skater error is mostly irreducible count noise; of the reducible part about a third is workload (with clear, fixable
biases in PP / SH / OT minutes caused by a data-construction defect) and the rest is rate quality (raw unshrunk rates,
league drift, no opponent term, no OT shots). Saves error is ~95% shots-faced volume, most of it game randomness and
pulls. The preregistered challenger (`WORKLOAD_V1_PREREGISTRATION.md`) targets both; results in `WORKLOAD_V1_RESULTS.md`.
