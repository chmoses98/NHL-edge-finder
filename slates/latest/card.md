# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-14T19:01:48Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +14.01 | +4.99 | +11.22 | 0.599 | -40.39 | -53.28 | 40.58 |
| B thesis-diversified (joint) ← optimiser card | 66.98 | +10.01 | +4.36 | +9.47 | 0.584 | -36.92 | -42.05 | 38.02 |
| C best expression per thesis | 34.65 | +6.44 | +2.58 | +1.11 | 0.556 | -34.65 | -34.65 | 22.48 |
| R FUNDED research stakes | 6.00 | +1.20 | +0.67 | +3.41 | 0.543 | -6.00 | -6.00 | 0.00 |

## MTL @ WSH  ·  10000 joint draws  ·  512 bet sides mapped, 5 +EV candidates, 4 on card

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
| Ryan Leonard: 1+ assists YES | 31 | 0.399 | 0.350 | +0.074 | +0.025 | $9.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
| Aliaksei Protas: 1+ goals YES | 19 | 0.234 | 0.222 | +0.033 | +0.021 | $7.07 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Full Game: Over 3.5 goals scored NO | 10 | 0.143 | 0.119 | +0.037 | +0.013 | $3.74 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | DIRECT (0.61) | EVIDENCE_MIXED | D |
| Jordan Kyrou: 1+ assists NO | 70 | 0.769 | 0.732 | +0.054 | +0.017 | $17.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes; why: higher confidence-adjusted growth (6.00 vs 5.90 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLTOTAL-26OCT14MTLWSH-4|no: INTENTIONAL_DIVERSIFIER (phi -0.164); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); failure: WSH offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes has the higher standalone adjusted growth (6.00 vs 5.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.049); they share one thesis budget; relationships: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLTOTAL-26OCT14MTLWSH-4|no: INTENTIONAL_DIVERSIFIER (phi -0.122); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.103); failure: WSH offense suppressed (<= 2 goals)
- **Full Game: Over 3.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-5|no; why: higher confidence-adjusted growth (3.73 vs 1.11 bp); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.164); KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.122); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi 0.134); failure: WSH offense succeeds (4+ goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-4|no; why: second expression of the same thesis: KXNHLTOTAL-26OCT14MTLWSH-4|no has the higher standalone adjusted growth (3.73 vs 3.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.134); they share one thesis budget; relationships: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.103); KXNHLTOTAL-26OCT14MTLWSH-4|no: INTENTIONAL_DIVERSIFIER (phi 0.134); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4077): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes (same contract)
- thesis GAME:LOW_EVENT (p 0.2339): highest fidelity KXNHLTOTAL-26OCT14MTLWSH-4|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT14MTLWSH-4|no (same contract)
- thesis WSH:SUPPRESSED (p 0.3766): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHATUCH89-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3766, phi -0.29)
- KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3766, phi -0.243)
- KXNHLTOTAL-26OCT14MTLWSH-4|no: FUNDED_RESEARCH; family MIXED; loses 39% of the draws where the thesis happens; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4077, phi -0.339)
- KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4077, phi -0.217)

portfolios: A EV +8.63 (adj +2.57) on $50.00, P(profit) 0.4861, adj growth 20.3 bp · B EV +6.04 (adj +2.35) on $38.40, P(profit) 0.5194, adj growth 20.5 bp · C EV +3.49 (adj +1.18) on $13.39, P(profit) 0.5133, adj growth 10.3 bp · R EV +0.68 (adj +0.33) on $3.00, P(profit) 0.3617, adj growth 11.1 bp

## DAL @ COL  ·  10000 joint draws  ·  470 bet sides mapped, 6 +EV candidates, 4 on card

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
| Artturi Lehkonen: 1+ goals YES | 23 | 0.285 | 0.270 | +0.042 | +0.027 | $8.66 | FUNDED_RESEARCH | $3 | COL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Jason Robertson: 1+ assists NO | 57 | 0.654 | 0.607 | +0.067 | +0.020 | $12.60 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Fedor Svechkov: 1+ goals YES | 10 | 0.126 | 0.118 | +0.020 | +0.012 | $3.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Gabriel Landeskog: 1+ goals YES | 21 | 0.245 | 0.235 | +0.023 | +0.013 | $4.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (8.80 vs 2.21 bp); relationships: KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT14DALCOL-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: COL offense suppressed (<= 2 goals)
- **Jason Robertson: 1+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT14DALCOL-DALMRANTANEN96-2|no; why: higher confidence-adjusted growth (3.56 vs 2.68 bp); relationships: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT14DALCOL-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: DAL offense succeeds (4+ goals)
- **Fedor Svechkov: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (8.80 vs 3.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT14DALCOL-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: COL offense suppressed (<= 2 goals)
- **Gabriel Landeskog: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (8.80 vs 2.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4441): highest fidelity KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.4873): highest fidelity KXNHLAST-26OCT14DALCOL-DALMRANTANEN96-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.3357): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.203)
- KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3011, phi -0.273)
- KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.149)
- KXNHLGOAL-26OCT14DALCOL-COLGLANDESKOG92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.226)

portfolios: A EV +5.38 (adj +2.42) on $50.00, P(profit) 0.3932, adj growth 20.3 bp · B EV +3.97 (adj +2.01) on $28.58, P(profit) 0.4768, adj growth 17.5 bp · C EV +2.94 (adj +1.40) on $21.26, P(profit) 0.7534, adj growth 12.2 bp · R EV +0.52 (adj +0.34) on $3.00, P(profit) 0.2846, adj growth 11.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
