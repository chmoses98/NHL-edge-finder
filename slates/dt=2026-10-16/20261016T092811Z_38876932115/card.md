# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-16T09:28:11Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +8.58 | +2.56 | -13.44 | 0.407 | -50.00 | -50.00 | 5.46 |
| B thesis-diversified (joint) ← optimiser card | 2.61 | +0.68 | +0.21 | -2.61 | 0.279 | -2.61 | -2.61 | 1.98 |
| C best expression per thesis | 5.15 | +1.34 | +0.42 | -5.15 | 0.279 | -5.15 | -5.15 | 3.63 |
| R FUNDED research stakes | 1.00 | +0.26 | +0.08 | -1.00 | 0.279 | -1.00 | -1.00 | 0.00 |

## PIT @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_PIT_win | p_overtime | goals | shots COL/PIT | COL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.118 | 0.72 | 0.28 | 0.00 | 6.05 | 34.1/22.2 | 19.6/29.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.65 | 0.35 | 0.00 | 6.06 | 28.6/27.9 | 25.0/24.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.103 | 0.75 | 0.25 | 0.00 | 9.42 | 35.7/23.6 | 19.2/27.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.47 | 6.01 | 28.6/28.0 | 24.7/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.67 | 0.33 | 0.00 | 9.39 | 30.3/29.4 | 24.2/22.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.57 | 0.43 | 0.47 | 5.97 | 34.2/22.3 | 19.2/30.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BOS_win | p_overtime | goals | shots ANA/BOS | ANA/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.122 | 0.58 | 0.42 | 0.00 | 6.04 | 34.0/22.1 | 18.9/29.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.53 | 0.47 | 0.00 | 6.09 | 28.8/28.2 | 24.8/24.9 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.54 | 0.46 | 0.48 | 5.98 | 34.5/22.3 | 19.1/31.1 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.099 | 0.61 | 0.39 | 0.00 | 9.38 | 35.9/23.7 | 18.5/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.53 | 0.47 | 0.00 | 9.52 | 30.5/29.6 | 23.6/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.51 | 0.49 | 0.48 | 5.98 | 28.5/27.8 | 24.5/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim over 4.5 goals scored YES | 21 | 0.279 | 0.240 | +0.058 | +0.018 | $2.61 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | DIRECT (0.60) | EVIDENCE_MIXED | D |
- **Anaheim over 4.5 goals scored YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6|yes; why: higher confidence-adjusted growth (4.05 vs 2.66 bp); wins across more scripts (relative breadth 0.526 vs 0.302); relationships: only recommended bet in this game; failure: BOS wins (incl. OT/SO)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4615): highest fidelity KXNHLTOTAL-26OCT16BOSANA-7|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3311): highest fidelity KXNHLTOTAL-26OCT16BOSANA-8|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5|yes: FUNDED_RESEARCH; family MIXED; loses 40% of the draws where the thesis happens; opposing: failure thesis BOS:WINS (p 0.465, phi -0.469)

portfolios: A EV +8.58 (adj +2.56) on $50.00, P(profit) 0.4069, adj growth 5.5 bp · B EV +0.68 (adj +0.21) on $2.61, P(profit) 0.2791, adj growth 2.0 bp · C EV +1.34 (adj +0.42) on $5.15, P(profit) 0.2791, adj growth 3.6 bp · R EV +0.26 (adj +0.08) on $1.00, P(profit) 0.2791, adj growth 2.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
