# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-28T15:41:44Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +22.48 | +7.15 | +20.74 | 0.659 | -45.26 | -62.03 | 57.60 |
| B thesis-diversified (joint) ← optimiser card | 147.27 | +24.83 | +14.00 | +20.48 | 0.644 | -47.48 | -64.52 | 121.98 |
| C best expression per thesis | 137.65 | +22.51 | +10.95 | +16.23 | 0.630 | -41.89 | -57.48 | 95.50 |
| R FUNDED research stakes | 24.00 | +2.17 | +1.01 | +1.31 | 0.667 | -7.23 | -12.14 | 0.00 |

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
| Christian Dvorak: 1+ goals YES | 15 | 0.209 | 0.193 | +0.050 | +0.034 | $9.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 18 | 0.239 | 0.222 | +0.049 | +0.032 | $10.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Washington over 2.5 goals scored NO | 28 | 0.371 | 0.323 | +0.077 | +0.029 | $11.24 | FUNDED_RESEARCH | $3 | WSH:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Jordan Kyrou: 1+ goals NO | 74 | 0.784 | 0.772 | +0.031 | +0.018 | $12.84 | FUNDED_RESEARCH | $4 | WSH:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (18.70 vs 5.96 bp); relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: PHI offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (14.00 vs 1.34 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no: INTENTIONAL_DIVERSIFIER (phi -0.237); KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: WSH offense suppressed (<= 2 goals)
- **Washington over 2.5 goals scored NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no; why: higher confidence-adjusted growth (8.86 vs 7.09 bp); relationships: KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.237); KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no: REINFORCING (phi 0.211); failure: WSH offense succeeds (4+ goals)
- **Jordan Kyrou: 1+ goals NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no; why: Player prop expression KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no selected over broad KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.90 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no: REINFORCING (phi 0.211); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.304): highest fidelity KXNHLSPREAD-26OCT28PHIWSH-WSH3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.4038): highest fidelity KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:SUPPRESSED (p 0.3834): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no — Player prop expression KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no selected over broad KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.90 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4725, phi -0.216)
- KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3834, phi -0.24)
- KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4038, phi -0.633)
- KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4038, phi -0.234)
- override: Player prop expression KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no selected over broad KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.90 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.70 (adj +1.68) on $37.50, P(profit) 0.5296, adj growth 11.9 bp · B EV +9.14 (adj +5.18) on $44.01, P(profit) 0.6286, adj growth 44.9 bp · C EV +10.34 (adj +5.54) on $50.00, P(profit) 0.6566, adj growth 48.1 bp · R EV +0.95 (adj +0.39) on $7.00, P(profit) 0.3714, adj growth 13.1 bp

## CGY @ EDM  ·  10000 joint draws  ·  418 bet sides mapped, 7 +EV candidates, 4 on card


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
| Alex Formenton: 1+ goals YES | 15 | 0.212 | 0.190 | +0.053 | +0.031 | $8.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ goals YES | 12 | 0.165 | 0.149 | +0.038 | +0.022 | $4.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 8 | 0.113 | 0.102 | +0.027 | +0.017 | $4.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ goals YES | 46 | 0.522 | 0.505 | +0.044 | +0.028 | $8.91 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | DIRECT (0.66) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes; why: higher confidence-adjusted growth (15.61 vs 9.01 bp); wins across more scripts (relative breadth 0.817 vs 0.686); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes; why: higher confidence-adjusted growth (9.01 vs 6.69 bp); despite a smaller raw edge (+0.038 vs +0.044/contract); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: DUPLICATIVE (phi 0.426); failure: EDM offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-CGYMBACKLUND11-1|yes; why: higher confidence-adjusted growth (7.69 vs 0.68 bp); alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: CGY offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes; why: Player prop expression KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT28CGYEDM-EDMVPODKOLZIN92-1|yes because adjusted EV is 0.4 pts higher while thesis capture is 0.66 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: DUPLICATIVE (phi 0.426); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, EDM shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5597): highest fidelity KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.2439): highest fidelity KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3148): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2439, phi -0.173)
- KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2439, phi -0.222)
- KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4705, phi -0.156)
- KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 34% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2439, phi -0.316)
- override: Player prop expression KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT28CGYEDM-EDMVPODKOLZIN92-1|yes because adjusted EV is 0.4 pts higher while thesis capture is 0.66 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +7.18 (adj +2.79) on $37.50, P(profit) 0.5503, adj growth 24.1 bp · B EV +6.15 (adj +3.66) on $25.50, P(profit) 0.4161, adj growth 31.6 bp · C EV +2.76 (adj +1.19) on $16.49, P(profit) 0.7596, adj growth 10.3 bp · R EV +0.28 (adj +0.17) on $3.00, P(profit) 0.5217, adj growth 6.2 bp

## NJD @ COL  ·  10000 joint draws  ·  446 bet sides mapped, 7 +EV candidates, 4 on card


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
| Amadeus Lombardi: 1+ goals YES | 9 | 0.114 | 0.107 | +0.019 | +0.011 | $2.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Connor Brown: 1+ goals YES | 13 | 0.160 | 0.149 | +0.022 | +0.011 | $3.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 76 | 0.796 | 0.786 | +0.024 | +0.013 | $12.20 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Nico Hischier: 1+ assists NO | 64 | 0.710 | 0.670 | +0.054 | +0.014 | $9.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28NJCOL-NJCBROWN16-1|yes; why: higher confidence-adjusted growth (3.20 vs 2.26 bp); despite a smaller raw edge (+0.019 vs +0.022/contract); relationships: KXNHLGOAL-26OCT28NJCOL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT28NJCOL-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.028); failure: NJD offense suppressed (<= 2 goals)
- **Connor Brown: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT28NJCOL-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (2.26 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT28NJCOL-NJNHISCHIER13-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: NJD offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no; why: Player prop expression KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT28NJCOL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT28NJCOL-NJNHISCHIER13-1|no: REINFORCING (phi 0.255); failure: NJD offense succeeds (4+ goals)
- **Nico Hischier: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no; why: KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no has the higher standalone adjusted growth (3.60 vs 1.90 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.103); relationships: KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT28NJCOL-NJCBROWN16-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no: REINFORCING (phi 0.255); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NJD:SUPPRESSED (p 0.4755): highest fidelity KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no — Player prop expression KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NJD:OFFENSE_4PLUS (p 0.3114): highest fidelity KXNHLGOAL-26OCT28NJCOL-NJCBROWN16-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28NJCOL-NJCBROWN16-1|yes (same contract)
- thesis COL:OFFENSE_4PLUS (p 0.4874): highest fidelity KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes (same contract)
- KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4755, phi -0.173)
- KXNHLGOAL-26OCT28NJCOL-NJCBROWN16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4755, phi -0.215)
- KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3114, phi -0.225)
- KXNHLAST-26OCT28NJCOL-NJNHISCHIER13-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3114, phi -0.265)
- override: Player prop expression KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.22 (adj +0.91) on $37.50, P(profit) 0.6202, adj growth 7.9 bp · B EV +2.25 (adj +1.02) on $27.76, P(profit) 0.7073, adj growth 8.9 bp · C EV +3.53 (adj +0.92) on $25.54, P(profit) 0.7982, adj growth 8.1 bp · R EV +0.12 (adj +0.07) on $4.00, P(profit) 0.7965, adj growth 2.4 bp

## TOR @ SEA  ·  10000 joint draws  ·  438 bet sides mapped, 13 +EV candidates, 4 on card


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
| Teddy Blueger: 1+ goals YES | 11 | 0.166 | 0.148 | +0.049 | +0.032 | $7.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 75 | 0.812 | 0.795 | +0.049 | +0.032 | $18.99 | FUNDED_RESEARCH | $5 | TOR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 13 | 0.167 | 0.156 | +0.029 | +0.018 | $4.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Toronto wins by over 1.5 goals NO | 67 | 0.753 | 0.709 | +0.068 | +0.024 | $18.99 | FUNDED_RESEARCH | $5 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT28TORSEA-TORMRIELLY44-1|yes; why: higher confidence-adjusted growth (20.53 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT28TORSEA-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26OCT28TORSEA-TOR2|no: INTENTIONAL_DIVERSIFIER (phi -0.171); failure: TOR offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR3|no; why: higher confidence-adjusted growth (12.40 vs 6.42 bp); despite a smaller raw edge (+0.048 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT28TORSEA-TOR2|no: REINFORCING (phi 0.15); failure: TOR offense succeeds (4+ goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR3|no; why: KXNHLSPREAD-26OCT28TORSEA-TOR3|no has the higher standalone adjusted growth (6.42 vs 6.17 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.088); relationships: KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT28TORSEA-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT28TORSEA-TOR2|no: MOSTLY_INDEPENDENT (phi 0.107); failure: SEA offense suppressed (<= 2 goals)
- **Toronto wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR3|no; why: KXNHLSPREAD-26OCT28TORSEA-TOR3|no has the higher standalone adjusted growth (6.42 vs 5.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.726); relationships: KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.171); KXNHLGOAL-26OCT28TORSEA-TORGMCKENNA92-1|no: REINFORCING (phi 0.15); KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.107); failure: TOR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3857): highest fidelity KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.3923): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.5451): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no (same contract)
- KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3923, phi -0.197)
- KXNHLGOAL-26OCT28TORSEA-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3857, phi -0.198)
- KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3246, phi -0.169)
- KXNHLSPREAD-26OCT28TORSEA-TOR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2467, phi -1.0)

portfolios: A EV +5.37 (adj +1.77) on $37.50, P(profit) 0.5136, adj growth 13.7 bp · B EV +7.29 (adj +4.14) on $50.00, P(profit) 0.7508, adj growth 36.6 bp · C EV +5.89 (adj +3.30) on $45.62, P(profit) 0.6752, adj growth 29.0 bp · R EV +0.81 (adj +0.38) on $10.00, P(profit) 0.6367, adj growth 13.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
