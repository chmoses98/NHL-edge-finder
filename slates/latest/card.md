# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-16T12:17:55Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +7.48 | +2.09 | -11.77 | 0.408 | -50.00 | -50.00 | 1.96 |
| B thesis-diversified (joint) ← optimiser card | 5.36 | +1.48 | +0.51 | -5.36 | 0.346 | -5.36 | -5.36 | 4.39 |
| C best expression per thesis | 3.06 | +1.21 | +0.43 | -3.06 | 0.134 | -3.06 | -3.06 | 3.74 |
| R FUNDED research stakes | 2.00 | +0.58 | +0.20 | -2.00 | 0.346 | -2.00 | -2.00 | 0.00 |

## PIT @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_PIT_win | p_overtime | goals | shots COL/PIT | COL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.122 | 0.72 | 0.28 | 0.00 | 6.04 | 34.0/22.2 | 19.7/29.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.68 | 0.32 | 0.00 | 6.07 | 28.6/27.9 | 25.0/24.2 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.101 | 0.74 | 0.26 | 0.00 | 9.45 | 35.7/23.5 | 19.2/27.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.63 | 0.37 | 0.00 | 9.48 | 29.8/29.3 | 23.7/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.53 | 0.47 | 0.47 | 5.96 | 28.5/27.9 | 24.7/25.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.56 | 0.44 | 0.47 | 5.97 | 34.5/22.4 | 19.2/30.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BOS_win | p_overtime | goals | shots ANA/BOS | ANA/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.116 | 0.61 | 0.39 | 0.00 | 6.05 | 34.3/22.0 | 19.1/29.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.53 | 0.47 | 0.00 | 6.06 | 28.6/28.0 | 24.5/24.9 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.101 | 0.60 | 0.40 | 0.00 | 9.28 | 35.8/23.6 | 18.5/28.5 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.56 | 0.44 | 0.46 | 5.99 | 34.6/22.5 | 19.3/31.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.48 | 0.52 | 0.45 | 5.98 | 28.5/27.9 | 24.6/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.54 | 0.46 | 0.00 | 9.48 | 30.2/29.5 | 23.6/23.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim over 5.5 goals scored YES | 9 | 0.134 | 0.109 | +0.038 | +0.013 | $2.38 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | FRAGILE (0.37) | EVIDENCE_MIXED | D |
| Full Game: Over 7.5 goals scored YES | 27 | 0.335 | 0.300 | +0.051 | +0.016 | $2.97 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Anaheim over 5.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT16BOSANA-8|yes; why: higher confidence-adjusted growth (4.55 vs 2.83 bp); despite a smaller raw edge (+0.038 vs +0.051/contract); relationships: KXNHLTOTAL-26OCT16BOSANA-8|yes: REINFORCING (phi 0.487); failure: BOS wins (incl. OT/SO)
- **Full Game: Over 7.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6|yes has the higher standalone adjusted growth (4.55 vs 2.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.487); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6|yes: REINFORCING (phi 0.487); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis GAME:HIGH_EVENT (p 0.3351): highest fidelity KXNHLTOTAL-26OCT16BOSANA-8|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT16BOSANA-8|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4649): highest fidelity KXNHLTOTAL-26OCT16BOSANA-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT16BOSANA-8|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6|yes: FUNDED_RESEARCH; family MIXED; loses 63% of the draws where the thesis happens; opposing: failure thesis BOS:WINS (p 0.4684, phi -0.336)
- KXNHLTOTAL-26OCT16BOSANA-8|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.3728, phi -0.419)
- override: override declined: the joint re-optimisation gives KXNHLTOTAL-26OCT16BOSANA-7|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6|yes kept

portfolios: A EV +7.48 (adj +2.09) on $50.00, P(profit) 0.4081, adj growth 2.0 bp · B EV +1.48 (adj +0.51) on $5.36, P(profit) 0.3457, adj growth 4.4 bp · C EV +1.21 (adj +0.43) on $3.06, P(profit) 0.1335, adj growth 3.7 bp · R EV +0.58 (adj +0.20) on $2.00, P(profit) 0.3457, adj growth 6.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
