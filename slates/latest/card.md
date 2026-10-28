# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-28T13:51:34Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +20.94 | +5.63 | +19.82 | 0.648 | -41.06 | -59.29 | 44.24 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +19.53 | +9.37 | +17.15 | 0.637 | -40.89 | -55.15 | 82.03 |
| C best expression per thesis | 114.20 | +13.46 | +6.54 | +12.50 | 0.639 | -34.51 | -44.53 | 58.36 |
| R FUNDED research stakes | 18.00 | +1.52 | +0.72 | +1.61 | 0.598 | -8.77 | -11.28 | 0.00 |

## PHI @ WSH  ·  10000 joint draws  ·  416 bet sides mapped, 14 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PHI_win | p_overtime | goals | shots WSH/PHI | WSH/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.60 | 0.40 | 0.00 | 5.96 | 26.5/26.4 | 23.2/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.50 | 5.88 | 26.8/26.5 | 23.4/23.6 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.093 | 0.63 | 0.37 | 0.00 | 5.97 | 31.5/21.0 | 18.2/27.3 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.56 | 0.44 | 0.47 | 5.86 | 31.9/21.2 | 18.2/28.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.59 | 0.41 | 0.00 | 9.25 | 28.3/28.0 | 22.6/21.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.58 | 0.42 | 0.00 | 3.47 | 25.4/25.1 | 23.5/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.239 | 0.220 | +0.059 | +0.040 | $10.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 16 | 0.209 | 0.194 | +0.040 | +0.025 | $6.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Jordan Kyrou: 1+ goals NO | 73 | 0.784 | 0.769 | +0.041 | +0.026 | $19.50 | FUNDED_RESEARCH | $5 | WSH:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 11 | 0.146 | 0.135 | +0.029 | +0.018 | $4.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (22.79 vs 2.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: WSH offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (9.52 vs 6.72 bp); relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: PHI offense suppressed (<= 2 goals)
- **Jordan Kyrou: 1+ goals NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no; why: Player prop expression KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no selected over broad KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no because adjusted EV is 0.2 pts higher while thesis capture is 0.90 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: WSH offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28PHIWSH-WSH2|no; why: higher confidence-adjusted growth (6.72 vs 3.37 bp); despite a smaller raw edge (+0.029 vs +0.097/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4038): highest fidelity KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:SUPPRESSED (p 0.3834): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no — Player prop expression KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no selected over broad KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no because adjusted EV is 0.2 pts higher while thesis capture is 0.90 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:OFFENSE_4PLUS (p 0.304): highest fidelity KXNHLSPREAD-26OCT28PHIWSH-WSH3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT28PHIWSH-WSH2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3834, phi -0.24)
- KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4725, phi -0.216)
- KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4038, phi -0.234)
- KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4725, phi -0.2)
- override: Player prop expression KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no selected over broad KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no because adjusted EV is 0.2 pts higher while thesis capture is 0.90 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.41 (adj +1.12) on $37.50, P(profit) 0.6595, adj growth 8.4 bp · B EV +7.32 (adj +4.72) on $41.41, P(profit) 0.4369, adj growth 41.1 bp · C EV +6.73 (adj +3.88) on $44.23, P(profit) 0.3431, adj growth 34.7 bp · R EV +0.27 (adj +0.17) on $5.00, P(profit) 0.7843, adj growth 6.3 bp

## CGY @ EDM  ·  10000 joint draws  ·  412 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CGY_win | p_overtime | goals | shots EDM/CGY | EDM/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.75 | 0.25 | 0.00 | 6.07 | 28.9/28.5 | 25.9/24.2 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.112 | 0.77 | 0.23 | 0.00 | 6.11 | 34.1/22.3 | 20.0/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.109 | 0.74 | 0.26 | 0.00 | 9.47 | 30.7/30.1 | 25.2/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.57 | 0.43 | 0.47 | 5.98 | 28.9/28.3 | 25.2/25.4 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.097 | 0.78 | 0.22 | 0.00 | 9.44 | 36.2/24.0 | 19.8/27.0 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.59 | 0.41 | 0.44 | 5.99 | 34.8/22.9 | 19.7/30.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 16 | 0.212 | 0.191 | +0.042 | +0.022 | $5.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ goals YES | 46 | 0.522 | 0.505 | +0.044 | +0.028 | $14.78 | FUNDED_RESEARCH | $4 | EDM:OFFENSE_4PLUS | DIRECT (0.66) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 32 | 0.374 | 0.356 | +0.038 | +0.021 | $8.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Ryan Nugent-Hopkins: 1+ assists NO | 60 | 0.686 | 0.638 | +0.069 | +0.021 | $18.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes; why: higher confidence-adjusted growth (7.39 vs 6.69 bp); despite a smaller raw edge (+0.042 vs +0.044/contract); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT28CGYEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (6.69 vs 4.43 bp); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT28CGYEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.147); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes has the higher standalone adjusted growth (6.69 vs 4.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); failure: EDM offense suppressed (<= 2 goals)
- **Ryan Nugent-Hopkins: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (4.09 vs 0.59 bp); alternative not eligible: confidence-adjusted EV +0.0076 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.147); KXNHLGOAL-26OCT28CGYEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, EDM shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5597): highest fidelity KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.2439): highest fidelity KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3148): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2439, phi -0.173)
- KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 34% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2439, phi -0.316)
- KXNHLGOAL-26OCT28CGYEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2439, phi -0.244)
- KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5597, phi -0.224)

portfolios: A EV +6.72 (adj +1.86) on $37.50, P(profit) 0.5127, adj growth 14.8 bp · B EV +5.84 (adj +2.77) on $47.24, P(profit) 0.6177, adj growth 24.2 bp · C EV +3.36 (adj +1.47) on $32.65, P(profit) 0.3236, adj growth 12.9 bp · R EV +0.37 (adj +0.23) on $4.00, P(profit) 0.5217, adj growth 7.9 bp

## NJD @ COL  ·  10000 joint draws  ·  434 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NJD_win | p_overtime | goals | shots COL/NJD | COL/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.68 | 0.32 | 0.00 | 6.04 | 28.7/28.7 | 26.0/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.54 | 0.46 | 0.48 | 5.93 | 28.7/28.6 | 25.3/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.68 | 0.32 | 0.00 | 9.34 | 30.4/30.2 | 25.1/23.2 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.086 | 0.73 | 0.27 | 0.00 | 6.01 | 33.8/22.8 | 20.3/29.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.57 | 0.43 | 0.47 | 5.89 | 33.6/23.0 | 20.0/30.2 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.060 | 0.60 | 0.40 | 0.00 | 5.97 | 22.9/33.2 | 30.1/19.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Hughes: 1+ assists NO | 56 | 0.643 | 0.599 | +0.066 | +0.022 | $12.13 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Luke Evangelista: 1+ assists NO | 68 | 0.786 | 0.708 | +0.091 | +0.012 | $9.94 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Nico Hischier: 1+ assists NO | 64 | 0.710 | 0.668 | +0.054 | +0.011 | $6.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Artturi Lehkonen: 1+ goals YES | 29 | 0.329 | 0.315 | +0.024 | +0.011 | $3.84 | FUNDED_RESEARCH | $1 | COL:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Jack Hughes: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (4.19 vs 1.56 bp); despite a smaller raw edge (+0.066 vs +0.091/contract); relationships: KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.06); KXNHLAST-26OCT28NJCOL-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.079); KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: NJD offense succeeds (4+ goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no has the higher standalone adjusted growth (4.19 vs 1.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.060); they share one thesis budget; relationships: KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.06); KXNHLAST-26OCT28NJCOL-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.103); KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NJD offense succeeds (4+ goals)
- **Nico Hischier: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no has the higher standalone adjusted growth (4.19 vs 1.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.079); they share one thesis budget; relationships: KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.079); KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.103); KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NJD offense succeeds (4+ goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28NJCOL-COL2|yes; why: higher confidence-adjusted growth (1.23 vs 0.03 bp); despite a smaller raw edge (+0.024 vs +0.025/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.898 vs 0.525); alternative not eligible: confidence-adjusted EV +0.0018 below the 0.010/contract floor; relationships: KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT28NJCOL-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NJD:SUPPRESSED (p 0.4755): highest fidelity KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:OFFENSE_4PLUS (p 0.4874): highest fidelity KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes (same contract)
- KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3114, phi -0.288)
- KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3114, phi -0.198)
- KXNHLAST-26OCT28NJCOL-NJNHISCHIER13-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3114, phi -0.265)
- KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3063, phi -0.235)

portfolios: A EV +3.95 (adj +0.96) on $37.50, P(profit) 0.5237, adj growth 8.3 bp · B EV +3.54 (adj +0.88) on $32.58, P(profit) 0.618, adj growth 7.8 bp · C EV +1.83 (adj +0.64) on $17.32, P(profit) 0.6427, adj growth 5.6 bp · R EV +0.08 (adj +0.04) on $1.00, P(profit) 0.3288, adj growth 1.2 bp

## TOR @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_TOR_win | p_overtime | goals | shots SEA/TOR | SEA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.57 | 0.43 | 0.00 | 6.07 | 29.2/29.0 | 25.7/25.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.45 | 6.02 | 29.2/29.2 | 25.8/25.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.56 | 0.44 | 0.00 | 9.43 | 30.9/30.8 | 24.8/24.1 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.082 | 0.64 | 0.36 | 0.00 | 6.06 | 34.7/23.3 | 20.4/30.1 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.53 | 0.47 | 0.50 | 6.0 | 34.8/23.3 | 19.9/31.4 | even strength |
| SEA shot control · high event (8+) · decided (2+) | 0.062 | 0.59 | 0.41 | 0.00 | 9.32 | 36.2/24.9 | 19.6/28.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Toronto wins by over 2.5 goals NO | 78 | 0.853 | 0.814 | +0.061 | +0.022 | $19.50 | FUNDED_RESEARCH | $5 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Toronto wins by over 1.5 goals NO | 67 | 0.753 | 0.709 | +0.068 | +0.024 | $5.64 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Seattle wins by over 1.5 goals YES | 26 | 0.332 | 0.293 | +0.058 | +0.020 | $3.64 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Toronto wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (6.42 vs 5.71 bp); despite a smaller raw edge (+0.061 vs +0.068/contract); relationships: KXNHLSPREAD-26OCT28TORSEA-TOR2|no: DUPLICATIVE (phi 0.726); KXNHLSPREAD-26OCT28TORSEA-SEA2|yes: REINFORCING (phi 0.293); failure: TOR wins by 2+
- **Toronto wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT28TORSEA-TOR3|no has the higher standalone adjusted growth (6.42 vs 5.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.726); they share one thesis budget; relationships: KXNHLSPREAD-26OCT28TORSEA-TOR3|no: DUPLICATIVE (phi 0.726); KXNHLSPREAD-26OCT28TORSEA-SEA2|yes: DUPLICATIVE (phi 0.403); failure: TOR wins by 2+
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT28TORSEA-TOR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT28TORSEA-TOR3|no has the higher standalone adjusted growth (6.42 vs 4.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.293); they share one thesis budget; relationships: KXNHLSPREAD-26OCT28TORSEA-TOR3|no: REINFORCING (phi 0.293); KXNHLSPREAD-26OCT28TORSEA-TOR2|no: DUPLICATIVE (phi 0.403); failure: TOR wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis SEA:WINS (p 0.5451): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.3317): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no (same contract)
- thesis TOR:SUPPRESSED (p 0.3923): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT28TORSEA-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2467, phi -0.726)
- KXNHLSPREAD-26OCT28TORSEA-TOR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2467, phi -1.0)
- KXNHLSPREAD-26OCT28TORSEA-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS (p 0.4549, phi -0.644)

portfolios: A EV +4.86 (adj +1.69) on $37.50, P(profit) 0.3317, adj growth 12.7 bp · B EV +2.83 (adj +1.00) on $28.78, P(profit) 0.7533, adj growth 8.9 bp · C EV +1.54 (adj +0.55) on $20.00, P(profit) 0.8528, adj growth 5.1 bp · R EV +0.79 (adj +0.28) on $8.00, P(profit) 0.7533, adj growth 9.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
