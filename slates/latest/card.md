# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-14T13:24:05Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 59.57 | +5.34 | +1.74 | -0.12 | 0.397 | -34.62 | -34.62 | 11.60 |
| B thesis-diversified (joint) ← optimiser card | 33.14 | +2.06 | +0.83 | +2.81 | 0.670 | -12.78 | -17.63 | 7.33 |
| C best expression per thesis | 16.16 | +1.53 | +0.58 | +4.20 | 0.601 | -16.17 | -16.17 | 5.10 |
| R FUNDED research stakes | 8.00 | +0.31 | +0.17 | -1.76 | 0.497 | -2.71 | -8.00 | 0.00 |

## MTL @ WSH  ·  10000 joint draws  ·  426 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_MTL_win | p_overtime | goals | shots WSH/MTL | WSH/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.56 | 0.44 | 0.00 | 6.0 | 27.4/27.3 | 24.0/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.44 | 5.9 | 27.3/27.2 | 24.0/24.1 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 5.99 | 32.2/21.4 | 18.4/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.55 | 0.45 | 0.00 | 9.33 | 29.1/28.6 | 22.8/22.5 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.51 | 0.49 | 0.45 | 5.83 | 32.8/21.7 | 18.6/29.4 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.058 | 0.62 | 0.38 | 0.00 | 9.28 | 34.4/23.2 | 18.3/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jakob Chychrun: 1+ goals NO | 79 | 0.822 | 0.813 | +0.021 | +0.011 | $16.39 | FUNDED_RESEARCH | $5 | WSH:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 32 | 0.397 | 0.348 | +0.061 | +0.013 | $5.20 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
- **Jakob Chychrun: 1+ goals NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-4|no; why: higher confidence-adjusted growth (1.76 vs 1.11 bp); despite a smaller raw edge (+0.021 vs +0.026/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.004 vs 0.355); alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.105); failure: WSH offense succeeds (4+ goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT14MTLWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (1.66 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT14MTLWSH-WSHJCHYCHRUN6-1|no: INTENTIONAL_DIVERSIFIER (phi -0.105); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4077): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes (same contract)
- thesis WSH:SUPPRESSED (p 0.3766): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT14MTLWSH-WSHJCHYCHRUN6-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4077, phi -0.175)
- KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3766, phi -0.293)

portfolios: A EV +4.17 (adj +1.06) on $40.00, P(profit) 0.3965, adj growth 6.2 bp · B EV +1.37 (adj +0.43) on $21.59, P(profit) 0.3064, adj growth 3.8 bp · C EV +0.84 (adj +0.18) on $4.61, P(profit) 0.3965, adj growth 1.6 bp · R EV +0.13 (adj +0.07) on $5.00, P(profit) 0.8222, adj growth 2.4 bp

## DAL @ COL  ·  10000 joint draws  ·  390 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_DAL_win | p_overtime | goals | shots COL/DAL | COL/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.128 | 0.70 | 0.30 | 0.00 | 6.0 | 32.7/21.0 | 18.5/27.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.64 | 0.36 | 0.00 | 5.99 | 27.2/26.7 | 23.9/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.53 | 0.47 | 0.48 | 5.9 | 27.5/26.8 | 23.5/24.2 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.55 | 0.45 | 0.49 | 5.9 | 32.9/21.2 | 18.1/29.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.078 | 0.70 | 0.30 | 0.00 | 9.23 | 34.5/22.5 | 18.1/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.62 | 0.38 | 0.00 | 9.28 | 28.9/28.3 | 23.0/22.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 1+ goals NO | 55 | 0.601 | 0.587 | +0.034 | +0.020 | $11.55 | FUNDED_RESEARCH | $3 | COL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT14DALCOL-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (3.51 vs 0.00 bp); despite a smaller raw edge (+0.034 vs +0.075/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:SUPPRESSED (p 0.3357): highest fidelity KXNHLGOAL-26OCT14DALCOL-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT14DALCOL-COLNMACKINNON29-1|no (same contract)
- KXNHLGOAL-26OCT14DALCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4441, phi -0.288)

portfolios: A EV +1.17 (adj +0.68) on $19.57, P(profit) 0.6012, adj growth 5.4 bp · B EV +0.69 (adj +0.40) on $11.55, P(profit) 0.6012, adj growth 3.5 bp · C EV +0.69 (adj +0.40) on $11.55, P(profit) 0.6012, adj growth 3.5 bp · R EV +0.18 (adj +0.10) on $3.00, P(profit) 0.6012, adj growth 3.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
