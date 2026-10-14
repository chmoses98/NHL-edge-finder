# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-14T18:05:44Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +10.94 | +4.44 | +12.93 | 0.565 | -38.71 | -53.68 | 36.92 |
| B thesis-diversified (joint) ← optimiser card | 70.93 | +8.31 | +3.61 | +4.24 | 0.546 | -31.03 | -31.71 | 31.58 |
| C best expression per thesis | 51.47 | +7.04 | +2.85 | +1.66 | 0.532 | -26.22 | -29.45 | 24.85 |
| R FUNDED research stakes | 7.00 | +0.62 | +0.39 | -2.01 | 0.285 | -7.00 | -7.00 | 0.00 |

## MTL @ WSH  ·  10000 joint draws  ·  512 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.529 / away 0.471

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
| Ryan Leonard: 1+ assists YES | 31 | 0.399 | 0.350 | +0.074 | +0.025 | $9.22 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
| Jordan Kyrou: 1+ assists NO | 70 | 0.769 | 0.732 | +0.054 | +0.017 | $16.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Aliaksei Protas: 1+ goals YES | 20 | 0.234 | 0.224 | +0.023 | +0.013 | $4.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Jakob Chychrun: 1+ goals NO | 79 | 0.821 | 0.812 | +0.019 | +0.010 | $13.73 | FUNDED_RESEARCH | $4 | WSH:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes; why: higher confidence-adjusted growth (6.00 vs 2.20 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26OCT14MTLWSH-WSHJCHYCHRUN6-1|no: INTENTIONAL_DIVERSIFIER (phi -0.111); failure: WSH offense suppressed (<= 2 goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-5|no; why: higher confidence-adjusted growth (3.17 vs 1.11 bp); wins across more scripts (relative breadth 1.008 vs 0.392); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.103); KXNHLGOAL-26OCT14MTLWSH-WSHJCHYCHRUN6-1|no: MOSTLY_INDEPENDENT (phi 0.038); failure: WSH offense succeeds (4+ goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes has the higher standalone adjusted growth (6.00 vs 2.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.049); they share one thesis budget; relationships: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.103); KXNHLGOAL-26OCT14MTLWSH-WSHJCHYCHRUN6-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: WSH offense suppressed (<= 2 goals)
- **Jakob Chychrun: 1+ goals NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no; why: second expression of the same thesis: KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no has the higher standalone adjusted growth (3.17 vs 1.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.038); they share one thesis budget; relationships: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.111); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi 0.038); KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4077): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes (same contract)
- thesis WSH:SUPPRESSED (p 0.3766): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no (same contract)
- KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3766, phi -0.29)
- KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4077, phi -0.217)
- KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3766, phi -0.243)
- KXNHLGOAL-26OCT14MTLWSH-WSHJCHYCHRUN6-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4077, phi -0.18)

portfolios: A EV +5.45 (adj +2.00) on $50.00, P(profit) 0.4626, adj growth 16.6 bp · B EV +4.12 (adj +1.52) on $43.43, P(profit) 0.4626, adj growth 13.4 bp · C EV +3.43 (adj +1.12) on $27.11, P(profit) 0.3991, adj growth 9.8 bp · R EV +0.10 (adj +0.05) on $4.00, P(profit) 0.8209, adj growth 1.8 bp

## DAL @ COL  ·  10000 joint draws  ·  470 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.556 / away 0.444

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
| Artturi Lehkonen: 1+ goals YES | 23 | 0.285 | 0.270 | +0.042 | +0.027 | $8.55 | FUNDED_RESEARCH | $3 | COL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Jason Robertson: 1+ assists NO | 57 | 0.654 | 0.607 | +0.067 | +0.020 | $12.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Fedor Svechkov: 1+ goals YES | 10 | 0.126 | 0.118 | +0.020 | +0.012 | $3.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Arttu Hyry: 1+ goals YES | 9 | 0.117 | 0.107 | +0.022 | +0.011 | $2.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (8.80 vs 2.21 bp); relationships: KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT14DALCOL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: COL offense suppressed (<= 2 goals)
- **Jason Robertson: 1+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT14DALCOL-DAL3|no; why: higher confidence-adjusted growth (3.56 vs 0.40 bp); alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT14DALCOL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.034); failure: DAL offense succeeds (4+ goals)
- **Fedor Svechkov: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (8.80 vs 3.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT14DALCOL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: COL offense suppressed (<= 2 goals)
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT14DALCOL-DALJBENN14-1|yes; why: higher confidence-adjusted growth (3.02 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4441): highest fidelity KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.4873): highest fidelity KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no (same contract)
- thesis DAL:OFFENSE_4PLUS (p 0.3011): highest fidelity KXNHLGOAL-26OCT14DALCOL-DALAHYRY25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT14DALCOL-DALAHYRY25-1|yes (same contract)
- KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.203)
- KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3011, phi -0.273)
- KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.149)
- KXNHLGOAL-26OCT14DALCOL-DALAHYRY25-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.4873, phi -0.192)

portfolios: A EV +5.48 (adj +2.44) on $50.00, P(profit) 0.3853, adj growth 20.3 bp · B EV +4.20 (adj +2.09) on $27.50, P(profit) 0.4459, adj growth 18.1 bp · C EV +3.61 (adj +1.73) on $24.36, P(profit) 0.3672, adj growth 15.1 bp · R EV +0.52 (adj +0.34) on $3.00, P(profit) 0.2846, adj growth 11.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
