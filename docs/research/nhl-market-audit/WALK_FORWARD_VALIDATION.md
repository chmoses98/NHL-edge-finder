# Walk-forward validation and historical replay (Phase H)

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

Everything here uses information available at the decision instant: prices from the board tick whose capture had COMPLETED (stamp + lag), model outputs stamped at or before the cut, chronological tiers, no refitting on
the evaluation window, fees and displayed-ask execution. Selection groups are reported separately and never summed with routed wagers.

## A. Pre-registered market-only strategies

See CANDIDATE_SIGNAL_REGISTRY.md (HIST_DISC -> HIST_HOLD -> LIVE, one look each). No-bet baseline = 0.

## B. The existing thesis workflow, replayed

Each LOGICAL bet (game | ticker | side) is scored once, at the FIRST snapshot where it met the rule, at the executable price recorded in that snapshot, with OUR independent outcome. (The archive holds 22,929 decision rows
for 2,839 logical bets; repeated snapshots are not observations.) Research selections only: stakes in the archive are research suggestions, not wagers.

| selection rule / scope | bets | games | mean price | hit rate | net ROI per $ (per contract) | 95% CI (games) | research-stake-weighted ROI | claimed EV / contract |
|---|---|---|---|---|---|---|---|---|
| S0_everything_considered / all | 2777 | 135 | 0.442 | 42.4% | -6.6% | [-12.4%, -0.6%] | -15.1% | +1.6% |
| S0_everything_considered / ex_goalscorer | 1519 | 134 | 0.504 | 48.1% | -7.1% | [-15.2%, +1.0%] | -16.8% | +1.5% |
| S0_everything_considered / goalscorer_only | 1258 | 134 | 0.367 | 35.5% | -5.6% | [-10.6%, -0.7%] | -13.6% | +1.6% |
| S1_first_FUNDED / all | 618 | 134 | 0.477 | 44.5% | -9.1% | [-18.6%, +0.0%] | -12.6% | +2.1% |
| S1_first_FUNDED / ex_goalscorer | 279 | 69 | 0.472 | 43.4% | -10.7% | [-27.9%, +6.4%] | -15.5% | +1.9% |
| S1_first_FUNDED / goalscorer_only | 339 | 133 | 0.482 | 45.4% | -7.9% | [-15.8%, +0.4%] | -10.6% | +2.3% |
| S2_first_chosen / all | 1393 | 135 | 0.405 | 39.3% | -5.8% | [-12.2%, +0.5%] | -13.0% | +1.9% |
| S2_first_chosen / ex_goalscorer | 621 | 133 | 0.508 | 48.6% | -6.9% | [-15.4%, +2.2%] | -15.3% | +1.9% |
| S2_first_chosen / goalscorer_only | 772 | 134 | 0.323 | 31.7% | -4.5% | [-11.9%, +3.2%] | -10.9% | +1.9% |
| S3_final_card / all | 506 | 135 | 0.346 | 34.8% | -2.6% | [-12.6%, +6.8%] | -9.1% | +2.5% |
| S3_final_card / ex_goalscorer | 137 | 93 | 0.540 | 59.1% | +6.4% | [-7.1%, +20.0%] | +7.6% | +2.6% |

### Does the selection layer pick better contracts than comparable ones it passed over?

Matched control: for each selected bet, a non-selected candidate from the same game, same family, same side, price within 5c (2,000 draws).

| selection | matched bets | selected ROI | control ROI (mean) | control 95% | p(random comparable pick does at least as well) |
|---|---|---|---|---|---|
| first chosen, all families | 434 | -1.0% | -1.1% | [-5.7%, +3.6%] | 0.476 |
| first chosen, ex goal-scorer | 100 | +1.7% | +12.5% | [+6.8%, +18.7%] | 1.000 |
| first FUNDED, all families | 188 | -14.2% | -1.6% | [-8.6%, +6.1%] | 1.000 |

Reading the last column: a value near 1 means a randomly chosen comparable candidate almost always did at least as well as the selection. The selected bets do not beat comparable candidates the workflow passed over, and in the ex-goal-scorer and funded cases they do
worse. The test is conditional on the same games (so game-level luck cancels) but the matched samples are small (100-434 bets). There is no evidence that the selection layer adds skill beyond the price.

### Does claimed EV predict realised ROI? (every distinct candidate, first snapshot)

| claimed adjusted-EV bin | bets | games | claimed EV / contract | realised ROI | 95% CI |
|---|---|---|---|---|---|
| (0.0090, 0.0112] | 557 | 133 | +1.1% | -6.6% | [-15.4%, +2.2%] |
| (0.0112, 0.0127] | 555 | 129 | +1.2% | -2.8% | [-10.8%, +4.5%] |
| (0.0127, 0.0148] | 555 | 130 | +1.4% | -11.8% | [-19.6%, -3.1%] |
| (0.0148, 0.0185] | 554 | 125 | +1.6% | +1.7% | [-7.6%, +11.4%] |
| (0.0185, 0.0586] | 556 | 121 | +2.5% | -13.8% | [-24.1%, -2.8%] |

Claimed EV is about +1% to +2.5% per contract in every bin; realised ROI is negative and NOT monotone in the claim (the highest-claim bin is among the worst). Claimed edge is not informative.

## C. Shadow expression engine over the same games (T-60 min, one decision per game)

| policy | bets | games with a bet | net ROI | 95% CI | claimed EV / contract |
|---|---:|---:|---:|---|---:|
| strict (evidence-gated; the proposed default) | 0 | 0 | - | - | - |
| research_unvalidated (gate waived, w=0.5, uncertainty kept) | 0 | 0 | - | - | - |
| naive_ev (gate waived, full model trust, uncertainty ignored) | 299 | 150 | -7.5% | [-19.2%, +4.2%] | +10.5% |

The strict engine PASSes every game. Ignoring the evidence produces a bet in nearly every game, with a claimed edge of about +10.5% per contract and a realised net ROI of -7.5%:
that gap is what an unvalidated model costs.

## D. Controls and what is missing

* Market-only decisions: section A. Current production model: section B plus PREDICTION_ENGINE_COMPARISON.md. Random / matched-market controls: section B. No-bet baseline: 0 by definition.
* Closing-line value is observable only as the move from decision to the last pregame quote; production `evaluations` carry it, and it is not used as an input anywhere (rule 9).
* Walk-forward for HIST uses fixed chronological splits (discovery -> hold-out); the walk-forward model predictions were produced by the repository's own expanding-window procedure.
* Prospective tier: accumulating from 2026-10-21T17:13:05Z; first look at 150 independent games.
