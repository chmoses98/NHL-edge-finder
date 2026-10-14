# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-14T20:49:56Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +13.44 | +3.30 | +10.79 | 0.634 | -40.90 | -58.71 | 23.72 |
| B thesis-diversified (joint) ← optimiser card | 88.62 | +8.31 | +3.60 | +3.22 | 0.563 | -24.55 | -40.96 | 31.88 |
| C best expression per thesis | 36.23 | +4.30 | +1.90 | +9.86 | 0.510 | -13.45 | -13.45 | 16.82 |
| R FUNDED research stakes | 9.00 | +0.71 | +0.36 | +1.80 | 0.565 | -3.24 | -3.96 | 0.00 |

## MTL @ WSH  ·  10000 joint draws  ·  512 bet sides mapped, 7 +EV candidates, 4 on card

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
| Aliaksei Protas: 1+ goals YES | 19 | 0.234 | 0.222 | +0.033 | +0.021 | $7.07 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Jordan Kyrou: 1+ assists NO | 70 | 0.769 | 0.732 | +0.054 | +0.017 | $17.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Ryan Leonard: 1+ assists YES | 32 | 0.399 | 0.352 | +0.064 | +0.017 | $7.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
| Full Game: Over 5.5 goals scored NO | 38 | 0.441 | 0.408 | +0.044 | +0.011 | $6.51 | FUNDED_RESEARCH | $2 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-2|yes; why: higher confidence-adjusted growth (5.90 vs 4.38 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.89 vs 0.756); relationships: KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.103); KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLTOTAL-26OCT14MTLWSH-6|no: INTENTIONAL_DIVERSIFIER (phi -0.144); failure: WSH offense suppressed (<= 2 goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-4|no; why: KXNHLTOTAL-26OCT14MTLWSH-4|no has the higher standalone adjusted growth (3.73 vs 3.17 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.134); relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.103); KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLTOTAL-26OCT14MTLWSH-6|no: REINFORCING (phi 0.153); failure: WSH offense succeeds (4+ goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes; why: Player prop expression KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes selected over player prop KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-2|yes because adjusted EV is 0.6 pts higher while thesis capture is 0.56 vs 0.17 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLTOTAL-26OCT14MTLWSH-6|no: INTENTIONAL_DIVERSIFIER (phi -0.203); failure: WSH offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-4|no; why: Broad expression KXNHLTOTAL-26OCT14MTLWSH-6|no selected over broad KXNHLTOTAL-26OCT14MTLWSH-4|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.61 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.144); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: REINFORCING (phi 0.153); KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.203); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4077): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes — Player prop expression KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes selected over player prop KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-2|yes because adjusted EV is 0.6 pts higher while thesis capture is 0.56 vs 0.17 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:LOW_EVENT (p 0.2339): highest fidelity KXNHLTOTAL-26OCT14MTLWSH-6|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT14MTLWSH-5|no — Broad expression KXNHLTOTAL-26OCT14MTLWSH-6|no selected over broad KXNHLTOTAL-26OCT14MTLWSH-4|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.61 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis WSH:SUPPRESSED (p 0.3766): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no (same contract)
- KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3766, phi -0.243)
- KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4077, phi -0.217)
- KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3766, phi -0.29)
- KXNHLTOTAL-26OCT14MTLWSH-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2602, phi -0.527)
- override: Broad expression KXNHLTOTAL-26OCT14MTLWSH-6|no selected over broad KXNHLTOTAL-26OCT14MTLWSH-4|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.61 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes selected over player prop KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-2|yes because adjusted EV is 0.6 pts higher while thesis capture is 0.56 vs 0.17 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +7.46 (adj +2.17) on $50.00, P(profit) 0.5993, adj growth 14.7 bp · B EV +4.61 (adj +1.71) on $38.62, P(profit) 0.661, adj growth 15.0 bp · C EV +2.34 (adj +1.13) on $10.34, P(profit) 0.3617, adj growth 9.8 bp · R EV +0.55 (adj +0.27) on $4.00, P(profit) 0.602, adj growth 9.0 bp

## DAL @ COL  ·  10000 joint draws  ·  476 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.557 / away 0.443

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
| Nicolas Roy: 1+ goals YES | 10 | 0.134 | 0.124 | +0.027 | +0.018 | $4.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Devon Toews: 1+ goals NO | 86 | 0.895 | 0.885 | +0.026 | +0.016 | $19.86 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Jason Robertson: 2+ assists NO | 87 | 0.931 | 0.893 | +0.053 | +0.015 | $19.86 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Artturi Lehkonen: 1+ goals YES | 24 | 0.285 | 0.271 | +0.032 | +0.018 | $5.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Nicolas Roy: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (7.11 vs 3.81 bp); despite a smaller raw edge (+0.027 vs +0.032/contract); relationships: KXNHLGOAL-26OCT14DALCOL-COLDTOEWS7-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: COL offense suppressed (<= 2 goals)
- **Devon Toews: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (5.23 vs 0.14 bp); alternative not eligible: confidence-adjusted EV +0.0040 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: COL offense succeeds (4+ goals)
- **Jason Robertson: 2+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT14DALCOL-DALMHEISKANEN4-2|no; why: higher confidence-adjusted growth (4.77 vs 4.05 bp); relationships: KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT14DALCOL-COLDTOEWS7-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: DAL offense succeeds (4+ goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (3.81 vs 0.57 bp); despite a smaller raw edge (+0.032 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT14DALCOL-COLDTOEWS7-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no: MOSTLY_INDEPENDENT (phi -0.004); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis DAL:SUPPRESSED (p 0.4873): highest fidelity KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT14DALCOL-DALRHINTZ24-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:OFFENSE_4PLUS (p 0.4441): highest fidelity KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.3357): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.163)
- KXNHLGOAL-26OCT14DALCOL-COLDTOEWS7-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4441, phi -0.126)
- KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3011, phi -0.241)
- KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.203)

portfolios: A EV +5.98 (adj +1.13) on $50.00, P(profit) 0.6146, adj growth 9.0 bp · B EV +3.70 (adj +1.89) on $50.00, P(profit) 0.3385, adj growth 16.9 bp · C EV +1.96 (adj +0.77) on $25.89, P(profit) 0.2646, adj growth 7.0 bp · R EV +0.15 (adj +0.09) on $5.00, P(profit) 0.8948, adj growth 3.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
