# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-14T14:24:08Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 58.01 | +3.72 | +1.47 | +1.44 | 0.683 | -33.06 | -58.01 | 9.91 |
| B thesis-diversified (joint) ← optimiser card | 27.62 | +1.43 | +0.67 | +2.85 | 0.529 | -12.58 | -27.63 | 5.92 |
| C best expression per thesis | 16.21 | +1.21 | +0.54 | +4.16 | 0.601 | -16.21 | -16.21 | 4.72 |
| R FUNDED research stakes | 9.00 | +0.50 | +0.21 | +1.28 | 0.683 | -4.01 | -9.00 | 0.00 |

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
| Jakob Chychrun: 1+ goals NO | 79 | 0.821 | 0.812 | +0.019 | +0.010 | $12.06 | FUNDED_RESEARCH | $4 | WSH:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Full Game: Over 5.5 goals scored NO | 38 | 0.441 | 0.408 | +0.044 | +0.011 | $4.01 | FUNDED_RESEARCH | $2 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Jakob Chychrun: 1+ goals NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-6|no; why: higher confidence-adjusted growth (1.47 vs 1.21 bp); despite a smaller raw edge (+0.019 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.003 vs 0.777); relationships: KXNHLTOTAL-26OCT14MTLWSH-6|no: MOSTLY_INDEPENDENT (phi 0.134); failure: WSH offense succeeds (4+ goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-4|no; why: higher confidence-adjusted growth (1.21 vs 1.11 bp); wins across more scripts (relative breadth 0.777 vs 0.355); alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT14MTLWSH-WSHJCHYCHRUN6-1|no: MOSTLY_INDEPENDENT (phi 0.134); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:SUPPRESSED (p 0.3766): highest fidelity KXNHLTOTAL-26OCT14MTLWSH-6|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT14MTLWSH-6|no (same contract)
- thesis GAME:LOW_EVENT (p 0.2339): highest fidelity KXNHLTOTAL-26OCT14MTLWSH-6|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT14MTLWSH-6|no (same contract)
- KXNHLGOAL-26OCT14MTLWSH-WSHJCHYCHRUN6-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4077, phi -0.18)
- KXNHLTOTAL-26OCT14MTLWSH-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2602, phi -0.527)

portfolios: A EV +2.55 (adj +0.79) on $38.44, P(profit) 0.441, adj growth 4.5 bp · B EV +0.74 (adj +0.27) on $16.07, P(profit) 0.3875, adj growth 2.4 bp · C EV +0.52 (adj +0.14) on $4.66, P(profit) 0.441, adj growth 1.2 bp · R EV +0.32 (adj +0.11) on $6.00, P(profit) 0.3875, adj growth 3.5 bp

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
