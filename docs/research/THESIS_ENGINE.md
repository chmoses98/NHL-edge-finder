# NHL game-script / thesis engine and portfolio construction (`nhl-thesis-1.0`)

**AUTHORITY: RESEARCH_ONLY.** This layer changes how the existing joint simulation is turned into a betting *card*. It
places nothing, routes nothing and grants no staking authority. Stakes are research suggestions for a nominal bankroll.
No model was tuned, no historical evidence was rewritten, and every model family keeps its RESEARCH_ONLY label.

Code: `src/nhl_edge/thesis/` (pure functions), `src/nhl_edge/workflows/thesis_card.py` (RUN NHL wiring),
`src/nhl_edge/workflows/thesis_postmortem.py` (evaluate step), `src/nhl_edge/research/thesis_replay.py` (replay and
proposed-card audit), `src/nhl_edge/research/thesis_model_audit.py` (Phase 12 audit).
Tests: `tests/test_thesis_core.py`, `tests/test_thesis_card.py`, `tests/test_thesis_integration.py`.

## 1. Why

Before this layer, card construction went: model probability → compare with Kalshi → pick individually attractive bets
→ check correlation afterwards. The PLAYER_SIM_V1 joint draw already held the whole distribution of games, but only
marginal probabilities and a 40-contract correlation matrix reached the packet. Now no card is emitted until its bets
have been evaluated as a **portfolio of game theses** on the same simulated games that priced them.

## 2. Audit of the existing simulation (Phase 1)

| item | state before this work |
|---|---|
| simulations per game | V1 `nhl-sim-1.1`: 20,000 draws. Joint draw: `nhl-sim-2.0` + PLAYER_SIM_V1, **10,000 draws** |
| seed | deterministic: `sha256(game_id, date, versions)`. V2 / player use `seed ^ 0x5F3759DF`, player allocation `+11`, saves `+21/+22`. Same inputs give the same draws (tested) |
| team outcomes | per draw: home/away regulation goals, OT, shootout, final, per-period goals, per half-minute step goals (`record_steps`) |
| player outcomes | per draw and player: goals, primary/secondary assists, points, TOI multiplier; first scorer and first team |
| goal state | strength of every goal (EV/PP/SH/EA/EN/OT) drawn per goal, **but only per-game means were kept** |
| goalies | per draw and net: starter saves, goals against, replaced flag, shots faced by the starter |
| shots | **no possession or shot process.** Shots on goal exist only through the saves layer: NegBin on pre-game expected non-goal shots, moved by the simulated regulation margin (+0.017 per goal of the net's team's lead) and OT. The coefficient on GA is ≈ 0, so shots = non-goal shots + goals against |
| score state / timing | goal times at half-minute resolution; score path recoverable from the step arrays |
| retention | draws lived only inside `shadow_player._one_game` and were discarded; the packet kept marginals plus the correlation matrix |
| game markets | V1 prices them from its own (different) 20k draws. V2 prices them from the joint draw's team path, which is identical to the player draw |

Changes, all additive and drawing **no extra random numbers** (every pre-existing output is bit-identical; tested):
`TeamDraws.state_goals` keeps per-draw goals by strength state, `SavesDraws.net_shots_faced` keeps full-game shots
against each net before the starter-replacement thinning, and `players.pricing.player_outcome` returns the indicator
`price_player` averages. Each game's joint draw is now held in memory as a `GameDistribution` until the card is built.
There is no second simulator: the thesis layer only reads the existing draw. Game markets are priced on that same draw
through the production V2 pricer (`thesis.outcomes` captures the exact indicator the pricer averaged, and the test
checks the captured mean equals the price).

## 3. Game-script taxonomy (Phase 2)

Every label is a fixed rule on per-draw features (`thesis.features.DrawFeatures`). There is no clustering, so a label is
reproducible prospectively and the same rule later classifies the real game (`DrawFeatures.from_actual`). Thresholds
were frozen **before** looking at any slate, from the completed regular seasons 2021-22 .. 2025-26 of the official
event history (6,560 games):

| quantity | history | thresholds |
|---|---|---|
| non-shootout total goals | P(≤4) 22.9%, P(5–7) 51.5%, P(≥8) 25.6%; mean 6.17 | LOW ≤ 4 · NORMAL 5–7 · HIGH ≥ 8 |
| home shot share | sd 0.088; P(≥0.55) 27.6%, P(≤0.45) 30.3% | team SHOT CONTROL ≥ 0.55 |
| shots on goal against one net | p33 26, median 29, p67 32 | LOW ≤ 25 · HIGH ≥ 33 |
| final margin | | TIGHT = one goal or OT/SO · DECIDED = 2+ · BLOWOUT ≥ 4 |

Dimensions (each a partition of draws): **SHOT CONTROL** (home / balanced / away), **ENVIRONMENT** (low / normal /
high), **MARGIN** (tight / decided), **SHAPE** (OT/SO, one-goal regulation, 2–3, blowout), **NET VOLUME** per net
(low / mid / high).
Overlays (non-exclusive): `GOALIE_STEAL_<team>` (wins while the opponent controls shots), `NET_VOLUME_HIGH/LOW_<team>`,
`PP_DRIVEN_<team>` (2+ PP goals and at least half the team's goals), `COMEBACK_<team>` (wins after trailing),
`EMPTY_NET_MATERIAL`, `OT_OR_LATE_TIGHT` (OT, or within one goal at 55:00).

The **primary partition** is SHOT CONTROL × ENVIRONMENT × MARGIN, 18 scripts (key `C{H,B,A}|E{L,N,H}|M{T,D}`). It
describes *how* the game is played, and the winner is reported **conditional** on the script. "TOR shot control · low
event · tight" with a high NYI win rate is the "Toronto presses, the NYI goalie steals it" script. A script is "major"
when its frequency is ≥ 3%. For every script the card reports frequency, win probability of each side, mean goals
per side and in total, shots per side, each starter's saves, PP and EN share of goals, P(OT), the driver (even strength
/ special teams / late empty net), overlay tags occurring in ≥ 15% of its draws, and the three players with the highest
point-probability lift in it.

Caveat, stated on the card: simulated shot volume comes from the saves layer, not a possession process, so SHOT CONTROL
in the simulation reflects expected shot share, noise and score effects. The audit (section 11) found that score
effects on shot volume are muted in the simulation.

## 4. Thesis events and bet-to-script mapping (Phases 3–4)

**Thesis events** (`thesis.events`, 27 per game) are named binary statements, each with a `category` so the secondary
thesis is a genuinely different idea. For each team: `WINS`, `WINS_BY_2PLUS`, `OFFENSE_4PLUS`, `SUPPRESSED` (≤2 goals),
`SHOT_CONTROL`, `NET_HIGH_VOLUME`, `NET_LOW_VOLUME`, `GOALIE_STEAL`, `PP_DRIVEN`, `COMEBACK`, `SCORES_FIRST`. For the
game: `HIGH_EVENT`, `LOW_EVENT`, `TIGHT`, `OVERTIME`, `EMPTY_NET`.

**Mapping.** Every priced contract, both sides (≈350 bet sides per game), is mapped using matrix products over the
same draws:

```
contribution_s = P(bet wins AND script s)        -> sums EXACTLY to P(bet) (integer counts; tested)
share_s        = contribution_s / P(bet)
THESIS_CONCENTRATION = top-1 and top-2 script shares
SCRIPT_BREADTH = 1 / sum(share_s^2)                (effective number of scripts the bet wins in)
relative breadth = breadth / (1 / sum(freq_s^2))   (1.0 = script-neutral; << 1 = needs specific scripts)
phi(bet, event)  for all 27 events                 (association with each thesis)
```

The primary thesis is the event with the largest positive phi (≥ 0.10, otherwise `DIFFUSE`). The secondary thesis is the
best event of a different category that is not a near-synonym of the primary (|phi between the events| < 0.70). The
failure thesis is the event with the most negative phi. Each thesis also carries P(bet | thesis), P(thesis | bet) and
P(bet | not thesis). Player props additionally get the team-offense conditionals, for example *P(Rakell goal | PIT 4+)
= 0.495, P(PIT 4+ | Rakell goal) = 0.526, P(Rakell goal | PIT ≤3) = 0.238*. That separates "Pittsburgh's offense
succeeds" from "Rakell is the one who scores".

## 5. Expression layer (Phase 5)

**Confidence-adjusted probability.** This is a documented prior, not a fit. The model's gap to the Kalshi midpoint is
credited only in part:

```
p_adj = mid + k (p - mid),  k = K_BASE[family reliability] + K_BENCH[sportsbook category], clipped to [0.10, 1.00]
K_BASE  EVIDENCE_STRONGER 0.75 | EVIDENCE_MIXED 0.50 | EVIDENCE_THIN 0.35 | CALIBRATION_WARNING 0.25
K_BENCH A +0.15 | B +0.05 | C -0.15 | D 0
|p - mid| >= 0.10  ->  k capped at 0.35   (LARGE_DISAGREEMENT)
```

The large-gap cap is based on evidence. In the historical player benchmark at T-10m, the 279 rows where the model sat
10+ points *below* the Kalshi mid settled only 3.0 points below the mid, so the market was closer. The 41 rows 10+
points above favoured the model, but that sample is too small to trust, so the cap is symmetric. Disagreement with the
market therefore increases scrutiny, not confidence.

**Candidate.** A bet side is a candidate when it is executable, pregame, quoted from a board that is neither stale nor
crossed, has positive fee-adjusted EV at the ask under the **model** probability, *and* has an adjusted EV of at least
**1.0¢ per contract** (`min_ev_adjusted`, a floor for model error).

**Best expression of a thesis.** Every bet side in the game whose phi with the thesis is ≥ 0.20 is compared, eligible or
not. The table shows ask, model p, p_adj, raw EV, adjusted EV, confidence-adjusted Kelly growth, fit (phi), purity
P(thesis | bet), P(bet | thesis), relative breadth, concentration, reliability and benchmark. The best expression is the
eligible row with the highest **confidence-adjusted expected log growth at its fractional-Kelly stake**. Raw edge is
never the selector. Equivalent contracts (identical settlement on every draw, e.g. "NYI wins" YES and "TOR wins" NO)
are collapsed to one.

## 6. Same-game joint outcome matrix (Phase 6)

For every pair of shortlisted same-game bets, computed from the same draws: P(A), P(B), P(A∧B), P(A|B), P(B|A),
P(A xor B), P(both lose), phi, expected profit if both are bought at $1 each, and script overlap = Σ_s min(share_A,s,
share_B,s). Identities are checked: P(A∧B) ≤ min, ≥ P(A)+P(B)−1, conditional × marginal = joint, and xor (tested; the
gate re-checks every card pair).

Labels (thresholds fixed a priori):

| label | rule |
|---|---|
| DUPLICATIVE | phi ≥ 0.60, or one bet (almost) implies the other (max conditional ≥ 0.97) with phi ≥ 0.30: the two share one exposure budget |
| REINFORCING | 0.15 ≤ phi < 0.60 |
| PARTIALLY_CONTRADICTORY | phi ≤ −0.15 |
| MOSTLY_INDEPENDENT | otherwise |
| INTENTIONAL_DIVERSIFIER | assigned by the portfolio layer: a pair with phi ≤ −0.05 or script overlap ≤ 0.50 where **both** bets are +EV after adjustment, both keep positive stake in the pair's joint optimum, and the pair's optimal growth beats either alone by > 2% |

Negative correlation is never labelled bad in itself, and a −EV bet can never be a diversifier because it is never a
candidate. Worked example, NYI @ TOR, 2026-09-30, 23:20Z: P(NYI wins) 0.520, P(Sorokin ≤ 24 saves) 0.627,
P(both) 0.295, P(Sorokin ≤ 24 | NYI wins) 0.569, P(NYI wins | Sorokin ≤ 24) 0.472, phi −0.125, script overlap 0.85.
The two bets are mildly opposed: NYI's win scripts include Toronto pressure that the goalie survives. They are not
contradictory, and on the engine's card the pair qualifies as an INTENTIONAL_DIVERSIFIER.

## 7. Portfolio constructor (Phase 7)

```
profit_draw = Σ_k stake_k (settle_k(draw) − cost_k) / cost_k        cost = executable ask + Kalshi fee
objective   = max E[log(1 + Σ_k f_k R_k)] on the joint draws, with R_k haircut to p_adj
              (an extra per-contract cost p − p_adj, so the dependence structure is untouched),
              then scaled by the fractional-Kelly multiplier 0.25
```

This is expected-return maximisation that accounts for joint outcomes: duplicative bets end up sharing stake, a
negatively related +EV pair is rewarded for lowering variance, and adding a −EV bet can only lower the objective. The
optimiser does **not** maximise P(profit). It is a projected damped diagonal-Newton ascent, and the single-bet case
matches closed-form Kelly (tested).

Constraints (fractions of the nominal bankroll, $1,000 by default via `NHL_EDGE_CARD_BANKROLL`): per bet 2%, per game
5%, per thesis 3% (bets that share a primary thesis or are linked as DUPLICATIVE form one budget), per slate 15%, a
$1 minimum stake, and **at most 4 bets per game**. When the joint optimum spreads wider than that, bets are
forward-selected greedily by marginal adjusted log growth and re-optimised jointly at each step; the selection log is
kept.

Outputs per game and per slate, from the simulated P/L distribution itself (never under an independence assumption):
expected profit, ROI, confidence-adjusted expected profit, median, P(profit), P(loss), P(losing > 50% of the
allocation), p05 / p10 / p25 / p75 / p95, worst and best draw, expected log growth (model) and adjusted log growth
(the objective), worst and best major script by mean P/L, and concentration by thesis and by market family.

Three portfolios are compared on the same draws:
- **A**: highest individual raw edges at independent quarter-Kelly stakes (the old contract-centric approach)
- **B**: the thesis-diversified joint optimum. **This is the card.**
- **C**: one best expression per thesis, jointly optimised

On the optimiser's own objective, B ≥ C (C's set is a subset). A's *model* EV can look larger because it uses raw
probabilities and larger independent stakes; card.md shows both views.

## 8. Normal-market benchmark (Phase 8)

Source: the quarantined `context/sportsbook_odds` kind (moneylines carried by the official NHL schedule feed). Nothing
is scraped and no paid source is used. Each provider's two prices are de-vigged proportionally; a provider whose
implied probabilities sum outside [1.00, 1.15] is dropped (that shape is a three-way or regulation price), and the
consensus is the median. Only `game_winner` contracts can be benchmarked; everything else is category D. The latest
partition observed at or before the cutoff is read (tested: odds observed after the cutoff are invisible).

| category | meaning |
|---|---|
| A | model and sportsbook agree Kalshi is mispriced (both beyond the executable cost) |
| B | model disagrees with Kalshi; sportsbook leans the model's way (≥ 0.5 pt beyond the mid) |
| C | model alone disagrees with both Kalshi and the sportsbook |
| D | no external benchmark |

The category moves confidence (k); it never overrides the probability.

## 9. Market-family reliability (Phase 9)

Labels are derived by `thesis.reliability` from committed evaluation artifacts (held-out 2025-26 walk-forward
`docs/research/player_sim_v1/eval.json`, historical Kalshi benchmarks `player_sim_v1/market_benchmark.json` and
`market_benchmark.json`) plus prospective evidence. The prospective part reads only `evaluations*` ledger partitions
observed at or before the run's cutoff, never the overwritten `eval/report*.json` (that would leak later games into a
replay). Distinct games are counted, not rows.

Rules, in precedence order: **CALIBRATION_WARNING** if held-out excess ECE > 0.010, where excess = ECE − sqrt(2/π)·
sqrt(0.25·10/n), the noise floor a perfectly calibrated forecaster shows (the Kalshi market's own moneyline ECE on the
benchmark rows is 0.029, so raw ECE would flag the market too). **EVIDENCE_STRONGER** if held-out n ≥ 5,000, ECE ≤
0.010, it beats its simple baseline, and it ties or beats the Kalshi mid on ≥ 1,000 benchmark rows. **EVIDENCE_MIXED**
if there is some depth but it isn't STRONGER. **EVIDENCE_THIN** otherwise. Fewer than 30 prospective games always adds
`SMALL_PROSPECTIVE_SAMPLE`.

| family | label | evidence |
|---|---|---|
| player_goals | EVIDENCE_STRONGER | held-out n 47,231, ECE 0.0019, beats role baseline; vs Kalshi mid −0.0001 Brier (n 3,783) |
| player_points | CALIBRATION_WARNING | ECE 0.0192 (floor 0.0058); market better by 0.0033 |
| player_assists | EVIDENCE_MIXED | ECE 0.0140; does not beat the role baseline; market better by 0.0019 |
| goalie_saves, first_goal | EVIDENCE_MIXED | calibrated held-out ladders; no market benchmark |
| game_winner, game_total, team_total, game_spread | EVIDENCE_MIXED | DATA_ONLY_V2 vs Kalshi mid: market better by 0.001–0.003 Brier |
| period_*, game_overtime, others | EVIDENCE_THIN | no artifact |

**Per-bet bucket calibration.** For goals, assists, points, saves and first goal, the held-out calibration bucket that
holds the model's YES probability is attached to the bet. When the bet side relies on a bias measured at ≥ 2 se (for
example a NO on a 45–50% assist, a bucket the model under-predicts by 7.3 pts at z 4.7), that bet is labelled
CALIBRATION_WARNING (k 0.25). This lowers confidence only; the probability is never recalibrated.

## 10. Card completion gate (Phase 10)

`thesis.card.run_gate`. A card is emitted (`status COMPLETE`) only if every recommended bet carries all 18 fields:

1 contract · 2 team / opponent · 3 executable price · 4 fair probability · 5 estimated edge · 6 bet-up-to price ·
7 recommended stake · 8 market-family reliability · 9 primary thesis · 10 secondary thesis · 11 best alternative ·
12 reason chosen · 13 thesis concentration · 14 relationship to every other same-game recommended bet ·
15 same-game exposure · 16 thesis exposure · 17 portfolio impact · 18 failure case.

A field that cannot be computed is `{"status": "UNKNOWN", "reason": ...}`, and an empty reason fails. Only fields 10, 11
and 14 may be `NOT_APPLICABLE`, with a reason. A missing field fails. **JOINT CARD CHECK:** a game with two or more
recommended bets needs a joint matrix from the same draws covering every pair, with each pair's identities satisfied and
each bet stating its relationship to every other. A one-bet game passes without pairs. If the gate fails, the card is
`INCOMPLETE` and is **not emitted**; the decisions are still logged. A slate with no qualifying bet is `NO_BETS`, which
is still a valid result.

## 11. Model improvement audit (Phase 12): diagnostic only, nothing changed

Full output: `docs/research/thesis_engine/model_audit.json` (from `thesis_replay --model-audit`).

**A. Goal attribution concentration: no defect found.**
- Held-out 2025-26, 45,196 skater-games. Conditional on the team's *realised* goals, actual / allocated goals by
  predicted share: 0.996, 0.971, 0.974, 1.029, 1.019, 1.002, 1.042 for shares up to 0.16, and 0.86 for the 281
  skater-games with share ≥ 0.16 (152 vs 131 goals, about −1.7 se).
- The team's three highest-share players given G = 2, 3, 4, 5 goals: 1.06, 1.05, 1.00, 1.01.
- Distinct scorers and P(someone scores 2+) given team goals N, simulated vs history (2023-26, league and the same six
  clubs), agree within 1–2 points. Example, N = 4: 3.565 vs 3.546 distinct scorers, 0.390 vs 0.402.
- Watch item: elite scorers' 2025-26 empirical P(goal | team 4+) exceeds the simulation in small per-player samples
  (MacKinnon 0.68 vs 0.52, n 37; Matthews 0.70 vs 0.50, n 23). The pooled held-out test does not confirm
  over-diffusion. Rakell is the other way: simulated 0.495 vs empirical 0.382 (n 34, about 1.4 se). Nothing was changed.

**B. Goalie saves: one structural finding, not tuned.**
- Held-out 2,624 starts: mean predicted saves 24.08 vs 24.16 actual; replacement rate predicted 6.2% vs 5.6% actual.
- Expected shots faced runs about 0.8 shots high (27.8 vs 27.0), mostly in the lower quintiles, but the saves
  conversion offsets it.
- **Score effects on shot volume are muted in the simulation.** Shots against by the goalie team's regulation margin,
  as deviations from the mean: history tied +1.13, −1 −1.24, +1 +0.26; simulation tied +0.33, −1 −0.25, +1 −0.33. The
  sim's sign pattern is only partly right and its size is roughly a quarter.
- Consequence: the simulated dependence between results and saves (e.g. NYI ML vs Sorokin saves, phi −0.125) is
  probably *understated*. It is listed as a research lead (a margin/trailing-state term in the saves layer, validated
  walk-forward), not changed from one Sorokin result. The first prospective saves sample is 4 contracts in 2 games.

**C. TOI.** The held-out evidence stands: model MAE 1.94 min vs recent-mean 1.89. Prospective line-informed forecasts so
far (68 player-games, 2 games): model 1.82 vs recent mean 1.96, and with confirmed lines 1.70 vs 2.02 (17
player-games). That is consistent with current lines helping, but far too small to claim anything.

**D. Assists and points.** Held-out compression is unchanged and clear: points under-predicted at 55–70% (+2.8 to
+5.6 pts, z 2.3–4.5) and over-predicted at 20–40% (−2.5 to −2.8 pts, z ≈ −4.5); assists the same S-shape. Prospective:
2 games (assists model Brier 0.1004 vs market 0.1054; points 0.1234 vs 0.1347 on market rows). No recalibration. The
compression now feeds per-bet confidence (section 9) instead.

## 12. Performance

Measured on the 2026-09-30 production archive copy (3 games, 1,052 bet sides, this container):

| step | time |
|---|---:|
| `nhl simulate` total (V1 + V2 + PLAYER_SIM_V1 + thesis card) | 17.6 s |
| market board reconstruction | 0.2 s |
| DATA_ONLY_V2 shadow | 3.3 s |
| PLAYER_SIM_V1 shadow (runtime load + joint draws + pricing) | 11.6 s |
| building the 3 `GameDistribution`s (all outcome vectors) | 0.15 s |
| thesis card (3 games) | 1.0 s |
| per game: scripts / mapping / expressions / joint / portfolio | ≈ 19 / 35 / 9 / 8 / 140–300 ms |
| scale test: 15 games, 5,260 bet sides | 5.3 s |

Shape: the full board is mapped with matrix products (bets × draws @ draws × scripts/events). Pairwise and portfolio
work runs only on the eligible shortlist (≤ 40 per game; typically 12–17), so nothing is O(N²) over the 2,000+ market
board, and no contract is hidden (the full board, unpriced contracts and their reasons are all in the packet). Memory is
about 3.5 MB of outcome vectors per game.

## 13. Prospective logging and postmortem (Phase 11)

| artefact | where | contents |
|---|---|---|
| `thesis_decisions` | data-archive ledger kind (append-only) | one row per shortlisted bet side per run: timestamp (= cutoff), game, ticker / side, executable price and its observation time, model p, p_adj, Kalshi mid, sportsbook p, V1 p, benchmark category, reliability, script mapping, per-script win rates, concentration, primary / secondary / failure theses with conditionals, joint relationships, alternatives considered, best expression of the thesis, chosen, stake, why selected / why rejected, card status |
| `thesis_games` | data-archive ledger kind | per game per run: script distribution, dimensions, thesis-event probabilities, sportsbook consensus, portfolios A/B/C, joint card check, expression tables, recommended bets, gate status, config |
| `thesis_card` | `slate.json` (compact) and `packet.json` (full) | the card plus everything above, including the full board |
| `card.md` | next to `slate.md` (and `slates/latest/`) | the human card |
| `thesis_postmortems` | data-archive ledger kind, written by `nhl evaluate` | per settled decision: THESIS result (primary / secondary event happened?), EXPRESSION result (`THESIS_{RIGHT,WRONG}_EXPRESSION_{WON,LOST}`, with the model's P(bet \| thesis outcome)), realised script and the model's P(win \| realised script), PRICE result (CLV vs the closing mid), MODEL result (Brier / log loss of p and p_adj vs the Kalshi mid), realised P/L |
| `eval/report_thesis.{json,md}` | archive | card-level summary on each game's last pregame run, plus a per-game PORTFOLIO result: realised vs simulated percentile, largest thesis share, multiple losses on one thesis and whether that thesis happened ("expression risk" vs "concentration cost") |

Point-in-time: decisions are stamped at the cutoff and use the board observed before it; the postmortem scores only
decisions made strictly before the scheduled start, and classifies the real game with the pregame functions.

## 14. Diagnostic sample: 2026-09-30, replayed at 23:20Z (10 minutes before the first puck drop)

`python -m nhl_edge.research.thesis_replay --archive <copy> --now 2026-09-30T23:20:00Z --date 2026-09-30 ...`.
Outputs: `docs/research/thesis_engine/sample_2026-09-30/` (card.md, a slim card JSON, the audit of the actually placed
card, the postmortem). **Diagnostic only.** It does not imply the card would have won, and nothing was tuned to make it
look better. Only pregame information is used: the archive partitions observed at or before 23:20Z, and history and
params that end on 2026-09-29.

Engine card (4 bets per game, gate PASS):
- **PIT @ PHI:** Porter Martone 1+ goal NO @70 (thesis PHI suppressed); Connor Dewar goal YES @11 and Rickard Rakell
  goal YES @27 (both PIT 4+ goals; nearly independent given the game, phi +0.011, sharing one thesis budget); Sean
  Couturier goal YES @13 (PHI 4+).
- **NYI @ TOR:** Teddy Blueger goal YES @9, Auston Matthews 1+ assist NO @60, NYI to win (collapsed with "Toronto wins"
  NO) @44 with sportsbook category B, Sorokin 25+ saves NO @49. The ML vs saves pair is an INTENTIONAL_DIVERSIFIER.
- **LAK @ COL:** MacKinnon 1+ goal NO @55, Zuccarello 1+ assist NO @67, Laferriere goal YES @21, COL over 3.5 team
  goals NO @50.

**Audit of the card that was actually placed** (router ledger: NYI ML $50 @44, LAK@COL under 6.5 $50 @55, Sorokin
under 24.5 $30 @51.5, Rakell goal $75 @27): the gate PASSES (NYI@TOR gets its joint card check), but **2 bets were −EV
after the confidence adjustment at the executed price**.
- Sorokin @51.5: model 0.627 vs mid 0.475 is a 15-pt disagreement, so k is capped at 0.35: raw EV +0.094, adjusted
  −0.0045. At the 49 ask on the 23:20 board it was +0.021.
- LAK@COL under 6.5 @55: raw +0.020, adjusted −0.001.
- NYI ML and Rakell were also on the engine's card.
- Stake shape: the proposed $75 Rakell bet is 7.5% of a $1,000 nominal bankroll against a 2% cap; the engine staked
  $9.51.

**Postmortem (two settled games; LAK@COL not yet settled in the archive copy):**
- PIT won 7–0, realised script "PIT shot control · normal event · decided". The PIT-offense thesis happened, and
  Dewar and Rakell both missed: THESIS_RIGHT_EXPRESSION_LOST × 2. The model's own P(Rakell goal | PIT 4+) was 0.495,
  so a miss was expected about half the time. Martone NO won (PHI suppressed); Couturier lost (thesis wrong). Card
  −$16.26 vs simulated EV +$7.89 (≤ p25).
- TOR won 2–1 in a balanced, low-event, tight game. The NYI-wins thesis was wrong, Matthews assist NO won, and Sorokin
  under won although his net did face more than 25 shots (THESIS_WRONG_EXPRESSION_WON). Card +$3.84.
- Two games prove nothing. The point is that thesis, expression, price, model and portfolio results are now separated.

## 15. Limitations

- Shot volume is a conditional saves layer, not a possession model. SHOT CONTROL scripts and goalie-volume theses
  inherit that, and score effects on shots look muted (section 11B).
- Thresholds (scripts, phi labels, k values, caps, the 1¢ floor, 4 bets per game) are a priori choices. They are
  documented and were not fit, but they are not optimised either. Changing them needs prospective evidence.
- The sportsbook benchmark covers moneylines only (the only odds the official feed carries).
- Reliability for game families uses historical benchmarks (V2 vs Kalshi mid). Prospective samples are 1–2 slates.
- Stakes assume a nominal bankroll and taker fills at the displayed ask. Depth and slippage are not modelled; the board
  is a snapshot.
- Player and goalie probabilities are conditional on playing / starting (Kalshi settles a no-show at the pre-game fair
  price), as before.
- The engine is one research layer on top of RESEARCH_ONLY models. Its card is a structured research view, not a
  recommendation with authority.
