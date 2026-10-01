# HANDOFF: NHL game-script / thesis engine and portfolio construction (2026-10-01)

Method, evidence and limits in full: `docs/research/THESIS_ENGINE.md` (sections referenced as §).

## A. VERDICT

**PRODUCTION-READY FOR RESEARCH USE.**
- The layer runs inside every RUN NHL (`nhl simulate`) on the existing joint draw. It emits `card.md` plus a
  `thesis_card` block only when the 18-field completion gate and the JOINT CARD CHECK pass, and it logs the full pregame
  decision state for a postmortem that keeps thesis, expression, price, model and portfolio results separate.
- It is a decision architecture, not edge evidence. All model families stay RESEARCH_ONLY. No staking authority was
  created and no bet was placed.
- No model was tuned and no historical evidence was rewritten.

## B. PRs / SHAs

| item | value |
|---|---|
| start `main` | `489a187` (PR #12), then `fea6ea2`-based PR #13 merged by the owner during this work (docs only) |
| PR | [chmoses98/NHL-edge-finder#14](https://github.com/chmoses98/NHL-edge-finder/pull/14): the thesis engine, RUN NHL wiring, postmortem, replay / audit tools, docs, sample |
| merge SHA / production evidence | recorded in the follow-up section **P** below once merged and observed |
| kalshi-bet-router | not touched: the card lives in this repo's packet and `card.md`; no router schema change was needed |

## C. ARCHITECTURE

```
nhl simulate
  V1 (unchanged) -> DATA_ONLY_V2 shadow (unchanged) -> PLAYER_SIM_V1 shadow (unchanged outputs)
      inside the player shadow, per game: GameDistribution = per-draw features + per-draw settlement of EVERY joined
      contract side (game families via the V2 pricer's own indicator, player families via player_outcome)
  -> thesis card (workflows/thesis_card.py -> thesis/engine.py)
      reliability (artifacts + PIT prospective ledger) . sportsbook consensus (quarantined kind, <= cutoff)
      per game: scripts -> thesis events -> full-board mapping -> confidence-adjusted economics -> candidates
                -> equivalence dedupe -> shortlist -> expressions per thesis -> joint matrix -> portfolios A/B/C
                (B = capped joint Kelly, greedy to <= 4 bets) -> diversifier test
      slate: slate cap -> card entries (18 fields) -> completion gate -> COMPLETE / INCOMPLETE / NO_BETS
  -> slate.json `thesis_card` (compact), packet.json `thesis_card` (full), card.md, ledger thesis_games + thesis_decisions
nhl evaluate -> thesis_postmortems + eval/report_thesis.{json,md}
```
Disable with `NHL_EDGE_THESIS_CARD=0`; set the nominal bankroll with `NHL_EDGE_CARD_BANKROLL` (default $1,000).

## D. SCRIPT TAXONOMY (§3)

- Primary partition (18 scripts) = SHOT CONTROL (home ≥ 0.55 shot share / balanced / away) × ENVIRONMENT
  (non-shootout goals ≤4 / 5–7 / ≥8) × MARGIN (tight = one goal or OT / decided = 2+).
- Other dimensions: SHAPE (OT/SO, one-goal regulation, 2–3, blowout 4+) and NET VOLUME per net (≤25 / mid / ≥33
  shots).
- Overlays: GOALIE_STEAL, NET_VOLUME_HIGH/LOW, PP_DRIVEN, COMEBACK per team, EMPTY_NET_MATERIAL, OT_OR_LATE_TIGHT.
- Thresholds were frozen from 2021-26 completed seasons (6,560 games), never from a slate. There is no clustering.
- 27 thesis events per game (§4).

## E. JOINT ANALYSIS (§6)

- Every pair of shortlisted same-game bets, computed from the same draws: P(A), P(B), P(A∧B), P(A|B), P(B|A),
  P(A xor B), P(both lose), phi, expected joint profit and script overlap. Identities are checked.
- Labels: DUPLICATIVE (shares one budget), REINFORCING, MOSTLY_INDEPENDENT, PARTIALLY_CONTRADICTORY, and
  INTENTIONAL_DIVERSIFIER. A diversifier is a pair where both bets are +EV after adjustment, both are kept by the pair
  optimum, and the pair's growth beats either bet alone.
- Example, NYI @ TOR: P(NYI) 0.520, P(Sorokin ≤24) 0.627, P(both) 0.295, P(Sorokin ≤24 | NYI) 0.569, P(NYI | Sorokin
  ≤24) 0.472, phi −0.125.

## F. PORTFOLIO ENGINE (§7)

- Objective: maximise expected log wealth on the joint simulated P/L, with each bet's EV haircut to the
  confidence-adjusted probability, then scale to quarter Kelly. It does not maximise P(profit), and a −EV bet is never
  a candidate.
- Caps: 2% per bet, 5% per game, 3% per thesis (shared with duplicative bets), 15% per slate, $1 minimum stake, 4 bets
  per game (greedy marginal growth beyond that).
- Each game shows portfolios A (top raw edges, independent stakes), B (joint optimum, the card) and C (best expression
  per thesis), with EV, adjusted EV, median, P(profit), P(lose > 50%), p05–p95, worst / best script and concentration
  by thesis and family.

## G. CARD COMPLETION GATE (§10)

- Each recommended bet needs 18 fields: contract, team / opponent, executable price, fair probability, estimated edge,
  bet-up-to price, recommended stake, family reliability, primary thesis, secondary thesis, best alternative, reason
  chosen, thesis concentration, relationship to every other same-game recommended bet, same-game exposure, thesis
  exposure, portfolio impact and failure case.
- UNKNOWN requires a reason. NOT_APPLICABLE (with a reason) is allowed only for the secondary thesis, the alternative
  and the relationships of a one-bet game.
- Two or more same-game bets require a joint matrix covering every pair (JOINT CARD CHECK).
- If the gate fails, the status is INCOMPLETE and the card is **not emitted**.

## H. PERFORMANCE (§12)

- `nhl simulate` total: 17.6 s for 3 games. Of that, the thesis card is 1.0 s and building the distributions is
  0.15 s. The player shadow is 11.6 s and the V2 shadow 3.3 s.
- Per game: scripts 19 ms, full-board mapping 35 ms, expressions 9 ms, joint matrix 8 ms, portfolio 140–300 ms.
- 15 games with 5,260 bet sides take 5.3 s.
- Pairwise and portfolio work runs only on the eligible shortlist. The full board is always mapped and reported.

## I. VALIDATION

- Full suite: 434 passed (26 new) plus ruff and the CI smoke.
- Covered by tests:
  - script assignment, and script probabilities summing to 1
  - contributions reconciling exactly to the unconditional probability
  - P(A∧B) ≤ min and the conditional identities
  - exact portfolio P/L on synthetic draws; the single-bet optimum matching closed-form Kelly
  - DUPLICATIVE / CONTRADICTORY / INTENTIONAL_DIVERSIFIER detection
  - no −EV hedge ever staked
  - gate failures: missing joint matrix, missing field, unexplained UNKNOWN; a one-bet game passing without pairs
  - outcome vectors reproducing V2 and player prices; unsupported contracts failing closed
  - seed reproducibility
  - V1 / V2 / player rows byte-identical with the layer on or off; failure containment
  - sportsbook odds after the cutoff staying invisible; decisions stamped at the cutoff
  - postmortem semantics; audits of proposed cards

## J. MODEL AUDIT (§11; diagnostic only, nothing changed)

- **Scorer attribution: no defect.** Held-out actual / allocated goals conditional on team goals is 0.97–1.04 by
  share, and simulated distinct-scorer structure matches history within 1–2 points.
- **Saves:** marginal saves are calibrated (24.08 vs 24.16), but score effects on shot volume are muted in the
  simulation (about a quarter of history's size). The result–saves dependence is therefore probably understated. This
  is a research lead; nothing was changed from one Sorokin result.
- **TOI:** the held-out caveat stands. Line-informed prospective forecasts look better on 2 games, which is not
  evidence.
- **Assists / points:** held-out compression is confirmed. There is no recalibration; it now lowers per-bet confidence
  instead.

## K. PROSPECTIVE LOGGING (§13)

- data-archive ledger kinds: `thesis_decisions` (per shortlisted bet side per run: the full decision state, chosen or
  rejected and why), `thesis_games` (scripts, thesis events, portfolios, joint check, expressions), and
  `thesis_postmortems` (from `nhl evaluate`).
- Reports: `eval/report_thesis.{json,md}`.
- Per slate: `card.md` and `packet.json` `thesis_card`.

## L. SAMPLE (§14; diagnostic only)

2026-09-30 replayed at 23:20Z on an archive copy, pregame inputs only. Outputs are in
`docs/research/thesis_engine/sample_2026-09-30/`.

The engine's card, 4 bets per game, gate PASS:
- PIT@PHI: Martone goal NO, Dewar goal YES, Rakell goal YES, Couturier goal YES.
- NYI@TOR: Blueger goal YES, Matthews assist NO, NYI ML, Sorokin under 24.5 at 49.
- LAK@COL: MacKinnon goal NO, Zuccarello assist NO, Laferriere goal YES, COL team total under 3.5.

The card that was actually placed passes completeness. But two of its bets, Sorokin at the executed 51.5 (a 15-point
gap to the mid, so confidence was capped) and LAK@COL under 6.5 at 55, were −EV after the confidence adjustment.

Postmortem on the two settled games: the PIT-offense thesis was right but both of its expressions missed
(THESIS_RIGHT_EXPRESSION_LOST; the model's own P(Rakell goal | PIT 4+) was 0.495). The NYI-wins thesis was wrong.
This does not imply the card would have won, and nothing was tuned.

## M. REMAINING LIMITATIONS

- Shots come from a conditional saves layer with muted score effects, and SHOT CONTROL scripts inherit that.
- All thresholds and k values are documented a-priori choices, not optimised.
- The sportsbook benchmark covers moneylines only.
- Prospective evidence is 1–2 slates.
- Stakes use a nominal bankroll and taker fills at the snapshot ask, with no depth or slippage.
- Player and goalie probabilities are conditional on playing.
- LAK@COL's postmortem awaits its settlement in production.

## N. OWNER ACTION

**NONE.** The next capture-worker generation dispatched after the merge picks up the code automatically. Optional: set
`NHL_EDGE_CARD_BANKROLL` in the workflow environment if a nominal bankroll other than $1,000 is wanted for the
research stakes.
