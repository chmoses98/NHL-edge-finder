# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-14T19:59:57Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +13.71 | +4.69 | +8.67 | 0.551 | -47.22 | -63.11 | 33.56 |
| B thesis-diversified (joint) ← optimiser card | 51.65 | +8.65 | +4.10 | +4.90 | 0.565 | -30.83 | -37.81 | 35.66 |
| C best expression per thesis | 41.61 | +4.53 | +2.20 | -3.28 | 0.434 | -18.83 | -18.83 | 19.46 |
| R FUNDED research stakes | 8.00 | +1.19 | +0.64 | -0.43 | 0.452 | -8.00 | -8.00 | 0.00 |

## MTL @ WSH  ·  10000 joint draws  ·  512 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

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
| Aliaksei Protas: 1+ goals YES | 19 | 0.234 | 0.222 | +0.033 | +0.021 | $6.63 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 2+ assists YES | 6 | 0.090 | 0.075 | +0.026 | +0.011 | $2.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_MIXED | D |
| Ryan Leonard: 1+ assists YES | 32 | 0.399 | 0.352 | +0.064 | +0.017 | $4.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
| Full Game: Over 5.5 goals scored NO | 38 | 0.441 | 0.408 | +0.044 | +0.011 | $8.26 | FUNDED_RESEARCH | $3 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-2|yes; why: higher confidence-adjusted growth (5.90 vs 4.38 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.89 vs 0.756); relationships: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-2|yes: MOSTLY_INDEPENDENT (phi 0.038); KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLTOTAL-26OCT14MTLWSH-6|no: INTENTIONAL_DIVERSIFIER (phi -0.144); failure: WSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 2+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (5.90 vs 4.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.038); they share one thesis budget; relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.038); KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: DUPLICATIVE (phi 0.386); KXNHLTOTAL-26OCT14MTLWSH-6|no: INTENTIONAL_DIVERSIFIER (phi -0.165); failure: WSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (5.90 vs 2.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.049); they share one thesis budget; relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-2|yes: DUPLICATIVE (phi 0.386); KXNHLTOTAL-26OCT14MTLWSH-6|no: INTENTIONAL_DIVERSIFIER (phi -0.203); failure: WSH offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-5|no; why: higher confidence-adjusted growth (1.21 vs 1.11 bp); wins across more scripts (relative breadth 0.777 vs 0.392); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.144); KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-2|yes: INTENTIONAL_DIVERSIFIER (phi -0.165); KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.203); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4077): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:LOW_EVENT (p 0.2339): highest fidelity KXNHLTOTAL-26OCT14MTLWSH-6|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT14MTLWSH-6|no (same contract)
- KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3766, phi -0.243)
- KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-2|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3766, phi -0.211)
- KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3766, phi -0.29)
- KXNHLTOTAL-26OCT14MTLWSH-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2602, phi -0.527)

portfolios: A EV +9.35 (adj +3.43) on $50.00, P(profit) 0.4497, adj growth 22.6 bp · B EV +3.76 (adj +1.52) on $21.62, P(profit) 0.3893, adj growth 13.2 bp · C EV +1.81 (adj +0.88) on $12.94, P(profit) 0.602, adj growth 7.7 bp · R EV +0.67 (adj +0.30) on $5.00, P(profit) 0.602, adj growth 9.6 bp

## DAL @ COL  ·  10000 joint draws  ·  476 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.553 / away 0.447

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_DAL_win | p_overtime | goals | shots COL/DAL | COL/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.129 | 0.70 | 0.30 | 0.00 | 5.99 | 32.7/21.1 | 18.6/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.64 | 0.36 | 0.00 | 6.0 | 27.1/26.7 | 23.9/23.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.55 | 0.45 | 0.49 | 5.9 | 32.9/21.2 | 18.1/29.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.53 | 0.47 | 0.48 | 5.9 | 27.5/26.9 | 23.5/24.2 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.077 | 0.70 | 0.30 | 0.00 | 9.25 | 34.6/22.6 | 18.1/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.63 | 0.37 | 0.00 | 9.26 | 28.9/28.3 | 23.0/22.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Artturi Lehkonen: 1+ goals YES | 23 | 0.285 | 0.270 | +0.042 | +0.027 | $8.57 | FUNDED_RESEARCH | $3 | COL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Nicolas Roy: 1+ goals YES | 10 | 0.134 | 0.124 | +0.027 | +0.018 | $4.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Jason Robertson: 1+ assists NO | 57 | 0.657 | 0.609 | +0.070 | +0.021 | $13.81 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Fedor Svechkov: 1+ goals YES | 10 | 0.126 | 0.118 | +0.020 | +0.012 | $3.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (8.80 vs 0.57 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: COL offense suppressed (<= 2 goals)
- **Nicolas Roy: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (8.80 vs 7.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: COL offense suppressed (<= 2 goals)
- **Jason Robertson: 1+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no; why: KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no has the higher standalone adjusted growth (4.77 vs 4.14 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.376); relationships: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: DAL offense succeeds (4+ goals)
- **Fedor Svechkov: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (8.80 vs 3.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4441): highest fidelity KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.4873): highest fidelity KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.3357): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.203)
- KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.163)
- KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3011, phi -0.28)
- KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.149)

portfolios: A EV +4.36 (adj +1.26) on $50.00, P(profit) 0.7465, adj growth 11.0 bp · B EV +4.89 (adj +2.58) on $30.03, P(profit) 0.4298, adj growth 22.4 bp · C EV +2.72 (adj +1.32) on $28.67, P(profit) 0.2846, adj growth 11.8 bp · R EV +0.52 (adj +0.34) on $3.00, P(profit) 0.2846, adj growth 11.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
