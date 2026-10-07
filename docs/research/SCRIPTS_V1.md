# NHL_SCRIPT_V1: game scripts, script survival, research candidates, opponent adjustment and the learning loop

**AUTHORITY: RESEARCH_ONLY.** This layer adds research evidence for SIFT. It places nothing, routes nothing, and does not
change DATA_ONLY_V1, PLAYER_SIM_V1, the thesis card, research governance, research stakes or any cap.

| piece | version | code |
|---|---|---|
| script taxonomy (pregame) | `NHL_SCRIPT_V1` / `nhl-script-1.0` | `src/nhl_edge/scripts_v1/taxonomy.py` |
| realised-script classifier (postgame only) | `nhl-realized-script-1.0` | `scripts_v1/taxonomy.py::realized` |
| script-conditioned pricing + survival | `nhl-survival-1.0` | `scripts_v1/survival.py` |
| research-candidate ranking + exposure groups | `nhl-candidates-1.0` | `scripts_v1/candidates.py` |
| opponent-adjusted team strength | `nhl-oppadj-1.0` | `src/nhl_edge/features/opponent_adjust.py` |
| learning loop / scorecard | `nhl-learning-1.0` | `src/nhl_edge/workflows/learning.py` |
| SIFT publication | additive, contract 1.1.1 unchanged | `src/nhl_edge/research_sift.py` |

Tests: `tests/test_scripts_v1.py`, `tests/test_opponent_adjust.py`, `tests/test_learning.py`, and additions in
`tests/test_thesis_integration.py` / `tests/test_research_export.py`.

## 1. Reuse decision

The thesis engine (`docs/research/THESIS_ENGINE.md`) already holds a coherent joint draw per game (10,000 draws of
`nhl-sim-2.0` + PLAYER_SIM_V1). It also holds a per-draw settlement indicator for both sides of every priced contract, and
deterministic per-draw features (`DrawFeatures`, with `from_actual` for real games). Its 18-cell primary script partition
(shot control x environment x margin) is right for portfolio construction but too fine to read. **No second simulator or
feature definition was built.** NHL_SCRIPT_V1 is a coarsening of the same per-draw features into seven scripts. It runs
inside `thesis_card.run_thesis_card` after the card is final, so the card, its gate and its stakes cannot be affected
(tested: a forced failure leaves the card COMPLETE and records `scripts_v1_error`).

## 2. Script taxonomy

Each draw, or each real final, gets exactly one script. The first rule that matches in precedence order wins, so a game's
script probabilities are integer draw shares that sum to exactly 1. BACK_AND_FORTH is the explicit catch-all; there is
no hidden "other".

| # | id | rule | 2022-23..2025-26 base rate |
|---|---|---|---:|
| 1 | SPECIAL_TEAMS | a team scores >= 2 PP goals and they are >= half its goals | 13.2% |
| 2 | OPEN_GAME | >= 8 non-shootout goals | 21.4% |
| 3 | TIGHT_LOW_EVENT | <= 4 goals and a one-goal final or OT | 10.4% |
| 4 | GOALIE_DRIVEN | the winner had <= 42% of the shots on goal | 8.7% |
| 5 | HOME_CONTROL | home wins by 2+ with >= 50% of the shots | 12.0% |
| 6 | AWAY_CONTROL | away wins by 2+ with >= 50% of the shots | 9.2% |
| 7 | BACK_AND_FORTH | everything else | 25.2% |

The base rates come from 5,248 official regular-season finals classified with the same rule
(`python -m nhl_edge.research.script_base_rates` writes `scripts_v1/base_rates.json`). The thresholds are a-priori
choices: they reuse the thesis engine's 8/4-goal and PP_DRIVEN cut points, add two new ones, and were never fit to a
slate, price or result.

For every script the block reports, from the draws inside it:
- probability and whether it is major (>= 5%);
- P(home win) and P(away win);
- mean goals per side and in total, plus the total-goals p10/p50/p90;
- shots, starter saves and home shot share;
- P(overtime), and the PP and empty-net share of goals;
- the players whose point probability rises most;
- the markets it helps most (largest lift of P(side | script) over P(side));
- the shortlisted candidates it hurts most.

The labels, summaries, "what would need to happen" and "what breaks it" lines are fixed templates. Nothing is
generated at runtime by an LLM.

**Known caveat:** simulated shots come from the goalie-saves layer, whose score effects are muted (THESIS_ENGINE 11B).
Real trailing teams out-shoot leaders, so GOALIE_DRIVEN is expected to be under-forecast. The learning loop measures the
gap instead of hiding it.

## 3. Script-conditioned pricing and survival

For each bet side `b` with draw indicator `y_b`:

```
P(b | s)  = wins in script s / draws in script s
delta_b   = p_b - p_adjusted_b         (the card's confidence adjustment, as a per-contract cost, like thesis.portfolio)
EV(b | s) = P(b | s) - delta_b - cost_b,   cost = ask of THIS side + Kalshi taker fee
sum_s freq_s * EV(b | s) == adjusted EV   (tested identity)
```

`b` survives `s` when `EV(b | s) >= 1c` and the data gates pass: an executable ask on a fresh, uncrossed board, pregame.
YES and NO sides each use their own ask and fee (tested). A contract with no simulated outcome is listed as unpriced
with its reason; no price is invented for it.

Each bet side gets these aggregates:
- mass survived (sum of `freq_s` over the scripts it survives);
- the number of major scripts survived;
- worst and best major-script EV;
- expected EV;
- the primary failure script (most negative freq-weighted EV) and downside concentration.

**Tiers** (a priori; based on probability mass, not script counts):

| tier | rule |
|---|---|
| ROBUST | adjusted EV >= 2c, mass >= 0.65, >= 3 major scripts survived |
| MODERATE | adjusted EV >= 1c, mass >= 0.45, >= 2 major scripts |
| FRAGILE | adjusted EV > 0 otherwise |
| DOES_NOT_SURVIVE | adjusted EV <= 0 |
| UNAVAILABLE | data-quality gate failed |

A binary contract always loses everything in some script (a home moneyline never wins AWAY_CONTROL), so worst-script EV
is reported but cannot define the tier.

## 4. Research candidates

Candidates are the thesis engine's existing shortlist. Shortlisting, governance (FUNDED_RESEARCH / SHADOW_ONLY /
REJECTED) and research stakes are unchanged. Robustness is logged with every decision (`thesis_decisions.script_survival`)
as a new decision feature. **It gates nothing in V1**: it must earn that prospectively.

SIFT orders candidates by a fixed key:
1. data quality OK
2. not REJECTED
3. not FRAGILE
4. research score = adjusted EV (c) x (0.5 + mass) x reliability weight x dependency factor x liquidity factor x
   exposure factor (x1.10 if FUNDED)

The effect is that a +7c edge surviving one narrow script ranks below a +4c edge surviving most of the mass (tested).

**Exposure groups.** Candidates that are DUPLICATIVE on the joint draw, or have phi >= 0.50, are grouped
(union-find). The lower-ranked member is flagged `duplicate_of` and down-weighted. Each candidate states its
relationship to the others in words:
- "Highly correlated with … — same thesis";
- "Reinforces …";
- "Partly offsets …";
- "Different expression: survives <script>, which it does not".

**Findings.** Supporting findings are model, simulation, market-benchmark, calibration or governance outputs only.
Opposing findings include the failure script, large market disagreement, calibration warnings and fragile expressions.

**Dependency flags.** Each candidate carries any of:
- an unconfirmed goalie on either side;
- player role not confirmed;
- low projection quality;
- a wide spread.

## 5. Opponent adjustment (RESEARCH)

```
rate_for(team, game) = mu + OFF_team + DEF_opponent + eta*home + noise
```

The model is fit by weighted ridge regression on 5v5 MoneyPuck team-game rows dated strictly before the cutoff:
- the window is the current season plus the previous one;
- weights are ice-time hours x 0.5^(days/60) x 0.6 for last-season games;
- the ridge penalty is 12 hours (about 15 games);
- teams need >= 10 games to be rated.

Adjusted offense is `mu + OFF` and adjusted defense is `mu + DEF`. The raw rate on the same games and weights is kept
beside it, and the schedule effect is raw minus adjusted. Metrics: 5v5 xGF/60, xGA/60, xG share, CF share, high-danger
xG share, GF/60, GA/60.

The walk-forward check (`docs/research/opponent_adjustment/eval.json`) refits on prior games at every 14-day checkpoint
of 2023-24..2025-26 and scores on 7,052 unseen team-games:

| metric | league mean | raw multiplicative | adjusted | adjusted vs raw | forward stability (adj better) |
|---|---:|---:|---:|---:|---:|
| 5v5 xG/60 | 0.694 | 0.661 | **0.644** | -2.6% MSE | 78% of checkpoints |
| 5v5 CF/60 | 142.7 | 121.9 | **119.7** | -1.8% | 89% |
| 5v5 HD xG/60 | 0.309 | 0.320 | **0.309** | -3.4% | 72% |
| 5v5 goals/60 | 3.01 | 3.07 | **2.97** | -3.2% | 58% |

That is a modest, consistent improvement, which is why the capability is RESEARCH and not VERIFIED. It is not a
DATA_ONLY_V1 input. Special teams, save percentage and player rates are not adjusted.

**Publication.** Adjusted metrics are separate metric ids (`met_nhl.oa_*`, category `opponent_adjusted`,
`supports.opponent_adjustment = true`, `extensions.basis = OPPONENT_ADJUSTED`). Their observations carry the adjusted
number in `value` and `adjusted_value`, and the raw number in `extensions.raw_value`. A raw rank cannot be mistaken for
an adjusted rank, and no raw metric claims adjustment (tested).

**Betting-evidence rule.** Each finding in `extensions.nhl_matchup_v1` carries a basis. Only OPPONENT_ADJUSTED, MODEL
and AVAILABILITY findings are `evidence_eligible`. RAW statistics (raw PP%/PK%, raw xG%, form) are context and say so
(tested).

## 6. Snapshots and the learning loop

| artefact | kind | content |
|---|---|---|
| `script_forecasts` | ledger, append-only, one row per game per thesis snapshot | script probabilities, script summaries, every candidate's price, p, conservative p, bet-up-to, survival, tier, governance status, dependency flags, pregame context |
| `thesis_decisions.script_survival` | ledger | the same survival fields on every logged decision |
| `script_postmortems` | ledger, append-only, deduped on (snapshot, game, realized version) | predicted distribution, realised script + metrics, multiclass Brier / log loss, base-rate Brier, top-script hit, hours before start |
| `eval/report_learning.json` | derived, overwritten | the scorecard |

Forecast rows are never rewritten when the realised label arrives (tested). Only snapshots stamped strictly before the
scheduled start are scored.

Populations are never mixed:
1. **Model vs market** (DATA_ONLY_V1 final pregame snapshot per contract): Brier, log loss, calibration buckets, bias,
   mean signed and absolute disagreement, the share of times the market moved toward the model, and model-side CLV.
   Windows ~24h / ~6h / ~90m / ~30m are computed from the snapshots that actually exist.
2. **Projection quality** (final pregame thesis snapshot per game): expected total and team goals vs actual (MAE, RMSE,
   bias, home/away bias).
3. **Research candidates (shadow)**: every shortlisted side at the game's final pregame snapshot, scored per $1 of
   contract cost whether or not anything was wagered. Broken down by governance status, family, edge bucket and
   robustness.
4. **NHL_SCRIPT_V1 candidates**: by robustness, survival bucket, family, status and goalie dependency.
5. **Funded research P/L** (nominal research stakes): reported separately.
6. **Actual routed wagers**: never in this report (accounting ledger / app `performance.json`).

Confidence intervals treat rows as independent and say so; same-game correlation makes them too narrow. A group with
n < 30 is flagged `small_sample`.

**Maturity gates.** These are a status only; they grant nothing, and ROI is never a criterion.

| stage | requirements |
|---|---|
| EARLY_LEARNING | the default |
| CALIBRATION_BUILDING | >= 100 settled games and >= 1,000 final-pregame contracts |
| EVIDENCE_EMERGING | >= 300 games, >= 200 settled script forecasts, >= 500 candidate CLV observations, model Brier within 0.005 of the market in both halves, no family with abs(bias) > 0.03 at n >= 200 |
| VALIDATED | >= 800 games, >= 600 script forecasts, model Brier <= market in both halves, candidate CLV 95% interval > 0 at n >= 1,000, scripts beat the league base rate |

## 7. Automatic operation

There is no new scheduler. The capture worker and conductor already run:

| job | what this layer adds |
|---|---|
| `simulate` | scripts, survival and candidates per game; `script_forecasts` rows |
| `settle` | (unchanged) |
| `evaluate` | realised scripts, `script_postmortems`, `report_learning.json`; `STATUS_evaluate.json.steps.learning` |
| `app_export` | a `learning` component in `health.json`, DEGRADED with the error when the learning step failed |
| `research_export` | the SIFT extensions, `met_nhl.oa_*` metrics and the learning scorecard |

Every new step is contained. A failure is recorded and visible, and it never deletes the last good publication: the
explorer still publishes atomically through the contract's `publish_explorer`.

## 8. Publication for SIFT (contract 1.1.1 unchanged; `extensions` is the open slot)

- `event_research.extensions.nhl_scripts_v1`: either `status = OK` or an explicit `NOT_SIMULATED` / `FAILED` with a
  reason. An OK block carries:
  - the scripts;
  - the compact market matrix (`market_columns` / `side_columns`, P(YES | script) per market, per-side ask / cost /
    delta / adjusted EV / mass / tier / survives bitstring / failure script);
  - the top 12 candidates and the rules.
- `event_research.extensions.nhl_matchup_v1`: ranked, basis-labelled findings, plus the What Matters ids (never RAW).
- `event_research.context.notes`: deterministic script and candidate one-liners. The handicap packet already carries
  context notes.
- `metric_registry` → `met_nhl.model_learning_stage.extensions.learning_v1`: the scorecard. It reports
  `status = STALE_LAST_RUN_FAILED` when the last learning step failed.
- Capability manifest:
  - `opponent_adjustment` = RESEARCH and `schedule_strength` = RESEARCH;
  - `matchup_metrics` mentions the scripts.

## 9. Known limitations

- Scripts exist only for games in the latest simulated slate. A game is simulated on its game day; later games show
  `NOT_SIMULATED`.
- Script probabilities are simulation-derived and not yet calibrated against real games. The first script postmortems
  arrive with the first settled games after this release. A learned script classifier (pregame features -> realised
  script, walk-forward) is the documented next step once there are a few hundred settled forecasts.
- Shot-volume scripts inherit the saves layer's muted score effects (section 2).
- Candidates are dominated by player props, because that is where the shortlist finds positive adjusted EV. Goal-scorer
  props are not up-weighted: the score uses absolute cents, not percentage edge.
- Survival uses the published executable ask at the research run. SIFT shows when the live ask has moved past bet-up-to.
- The opponent adjustment is RESEARCH (section 5).
