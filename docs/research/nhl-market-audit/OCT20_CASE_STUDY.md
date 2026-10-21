# October 20 case study (routed wagers, real fills)

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

## What the ledger says (this corrects the premise)

The accounting ledger records **four** NHL wagers on the 2026-10-20 slate, and **two of them won**. Net result: **-27.29** on **114.99** staked (2 wins, 2 losses). My independent resolver agrees with the ledger on all four
(and on all 34 routed wagers). The two losses were Toronto/Columbus Under 6.5 (final 6-2, total 8) and LA Kings Under 2.5 team goals (LA scored 5, one empty-net). Boston/Dallas Under 5.5 (2-3 in OT, total 5) and Anaheim Under 2.5 team goals
(Anaheim scored 2) **won**. Any analysis that treats all four as losses is analysing a different set of bets.

## The four wagers

Expected value is per contract at the ACTUAL fill price (price + taker fee), under four probability views: the market mid at the fill, V1, V2 (each the last pregame run at or before the fill) and the thesis workflow's confidence-adjusted probability.

| bet | fill price | min after sched. start | stake $ | result | net $ | final | EV @ market mid | EV @ V1 | EV @ V2 | EV @ thesis-adj. | thesis snapshots |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TOR @ CBJ TOTAL 7 NO | 0.540 | 6.1 | 35.00 | LOST | -35.00 | TOR 6 - CBJ 2 (REG) | -3.2% | -0.4% | +2.9% | -1.0% | 13 |
| LAK @ WSH TEAMTOTAL LA3 NO | 0.510 | 6.8 | 35.00 | LOST | -35.00 | LAK 5 - WSH 2 (REG) | -4.2% | +3.0% | -4.1% | none | 0 |
| BOS @ DAL TOTAL 6 NO | 0.500 | -52.7 | 25.00 | WON | 23.30 | BOS 2 - DAL 3 (OT) | -2.3% | +3.3% | -7.5% | none | 0 |
| ANA @ NYI TEAMTOTAL ANA3 NO | 0.490 | 7.7 | 20.00 | WON | 19.40 | ANA 2 - NYI 3 (REG) | -2.7% | -0.5% | -7.4% | none | 0 |

## Was the decision undermined by ...?

* **Weak probabilities.** Under the market's own probability every bet had negative expected value at its fill (the half-spread plus fee, about -2% to -4% per contract). Only some model views were positive, by 2.9 to 3.3 cents per contract - inside the model's measured error (PREDICTION_ENGINE_COMPARISON.md: no incremental information, coefficient not distinguishable from zero).
* **Model disagreement** (each model's win probability minus the market's, for the side bought): TOR @ CBJ: V1 +2.8 pts, V2 +6.1 pts vs the market's probability of winning (same direction); LAK @ WSH: V1 +7.2 pts, V2 +0.2 pts vs the market's probability of winning (same direction); BOS @ DAL: V1 +5.6 pts, V2 -5.3 pts vs the market's probability of winning (opposite directions); ANA @ NYI: V1 +2.3 pts, V2 -4.7 pts vs the market's probability of winning (opposite directions).
* **Price changes / timing.** Three of the four fills were 6 to 8 minutes AFTER the scheduled puck drop (Boston/Dallas started an hour later and was filled 53 minutes before). The last pregame model run was about 10 minutes before the scheduled start, so the
  pregame model could not have priced an in-play quote. Toronto/Columbus was filled at 0.54 against a displayed NO ask of 0.53 (the Over mid had already fallen from 0.485).
* **Alternative scripts.** For Toronto/Columbus the forecast gave the realised script (OPEN_GAME) 19% and the most likely script (BACK_AND_FORTH) 26%; the Under 6.5 cannot win in an 8-goal game. Toronto was on the second night of a back-to-back and still scored six.
* **Matchup adjustments.** The production context knew the confirmed goalies, rest and back-to-back flags (shown in `data/oct20_case.json`); the audit finds no incremental information in those factors beyond the market.
* **Unjustified confidence.** Only one of the four wagers (Toronto/Columbus) was ever a candidate in the thesis workflow; it was FUNDED_RESEARCH in 3 of 13 snapshots at a **$2** research stake and labelled EVIDENCE_MIXED. The routed stake was **$35**. The other three have no thesis decision at all, so they
  did not come from the model-generated recommendations; the ledger carries no provenance field, so "independent handicapping" cannot be separated from other sources.

## How much can four bets say?

Market-implied expected P/L on these four at the fills was about **-7.02** dollars (the cost of fees and spread) against a realised **-27.29**. Across all 34 routed wagers the market-implied expectation is -55.85 with a standard
deviation of 219; the realised -187.64 is -0.60 standard deviations from it. **The results are indistinguishable from paying fees on fairly priced contracts.**
Four bets, all Unders, all driven by one correlated factor (scoring environment), are one observation of that factor, not four.
