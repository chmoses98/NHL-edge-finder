# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-28T20:15:10Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +29.89 | +5.81 | +29.08 | 0.699 | -37.74 | -55.52 | 44.28 |
| B thesis-diversified (joint) ← optimiser card | 142.65 | +28.74 | +16.75 | +24.56 | 0.646 | -55.18 | -73.91 | 145.33 |
| C best expression per thesis | 112.27 | +21.51 | +8.86 | +16.79 | 0.641 | -38.77 | -49.70 | 77.27 |
| R FUNDED research stakes | 14.00 | +1.47 | +0.95 | -1.61 | 0.400 | -7.36 | -8.25 | 0.00 |

## PHI @ WSH  ·  10000 joint draws  ·  488 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.673 / away 0.327

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
| Sean Couturier: 1+ goals YES | 10 | 0.145 | 0.133 | +0.039 | +0.026 | $6.55 | FUNDED_RESEARCH | $2 | PHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 18 | 0.239 | 0.218 | +0.049 | +0.028 | $7.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 16 | 0.209 | 0.196 | +0.040 | +0.026 | $7.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Cole Knuble: 1+ goals YES | 12 | 0.165 | 0.150 | +0.038 | +0.023 | $5.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (15.41 vs 10.49 bp); despite a smaller raw edge (+0.039 vs +0.040/contract); relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT28PHIWSH-PHICKNUBLE54-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PHI offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (10.90 vs 1.34 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT28PHIWSH-PHICKNUBLE54-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: WSH offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (15.41 vs 10.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT28PHIWSH-PHICKNUBLE54-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: PHI offense suppressed (<= 2 goals)
- **Cole Knuble: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (15.41 vs 10.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.304): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.4038): highest fidelity KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:SUPPRESSED (p 0.3834): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4725, phi -0.199)
- KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3834, phi -0.24)
- KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4725, phi -0.216)
- KXNHLGOAL-26OCT28PHIWSH-PHICKNUBLE54-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4725, phi -0.213)

portfolios: A EV +8.43 (adj +1.28) on $37.50, P(profit) 0.5996, adj growth 9.9 bp · B EV +7.89 (adj +4.96) on $27.65, P(profit) 0.5708, adj growth 42.7 bp · C EV +11.65 (adj +4.34) on $41.75, P(profit) 0.54, adj growth 37.6 bp · R EV +0.73 (adj +0.49) on $2.00, P(profit) 0.145, adj growth 16.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT28PHIWSH-WSH|no == KXNHLGAME-26OCT28PHIWSH-PHI|yes

## CGY @ EDM  ·  10000 joint draws  ·  488 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.627 / away 0.373

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CGY_win | p_overtime | goals | shots EDM/CGY | EDM/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.73 | 0.27 | 0.00 | 6.05 | 28.9/28.4 | 25.8/24.2 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.113 | 0.77 | 0.23 | 0.00 | 6.07 | 34.3/22.4 | 20.2/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.70 | 0.30 | 0.00 | 9.49 | 30.4/30.0 | 24.8/22.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.096 | 0.77 | 0.23 | 0.00 | 9.42 | 36.0/24.0 | 19.7/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.55 | 0.45 | 0.47 | 5.96 | 28.9/28.4 | 25.1/25.5 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.59 | 0.41 | 0.46 | 5.92 | 34.7/22.8 | 19.7/31.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 14 | 0.207 | 0.185 | +0.058 | +0.037 | $9.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 7 | 0.109 | 0.094 | +0.034 | +0.019 | $4.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 10 | 0.129 | 0.121 | +0.023 | +0.014 | $3.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ goals YES | 46 | 0.512 | 0.498 | +0.035 | +0.021 | $9.75 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | DIRECT (0.65) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes; why: higher confidence-adjusted growth (22.64 vs 11.13 bp); wins across more scripts (relative breadth 0.826 vs 0.719); relationships: KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT28CGYEDM-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: EDM offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-CGYASUNIEV61-1|yes; why: higher confidence-adjusted growth (11.60 vs 2.85 bp); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT28CGYEDM-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: CGY offense suppressed (<= 2 goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-CGYASUNIEV61-1|yes; why: higher confidence-adjusted growth (4.63 vs 2.85 bp); despite a smaller raw edge (+0.023 vs +0.024/contract); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CGY offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes; why: Player prop expression KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.65 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT28CGYEDM-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, EDM shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5559): highest fidelity KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes — Player prop expression KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.65 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis CGY:OFFENSE_4PLUS (p 0.318): highest fidelity KXNHLGOAL-26OCT28CGYEDM-CGYASUNIEV61-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28CGYEDM-CGYASUNIEV61-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.2493): highest fidelity KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no (same contract)
- KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2493, phi -0.178)
- KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4641, phi -0.156)
- KXNHLGOAL-26OCT28CGYEDM-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4641, phi -0.195)
- KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 35% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2493, phi -0.304)
- override: Player prop expression KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.65 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +10.12 (adj +1.93) on $37.50, P(profit) 0.62, adj growth 13.9 bp · B EV +7.34 (adj +4.46) on $27.61, P(profit) 0.3861, adj growth 38.4 bp · C EV +3.45 (adj +1.74) on $22.85, P(profit) 0.2933, adj growth 15.1 bp · R EV +0.22 (adj +0.13) on $3.00, P(profit) 0.5124, adj growth 4.4 bp

## NJD @ COL  ·  10000 joint draws  ·  456 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.572 / away 0.428

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NJD_win | p_overtime | goals | shots COL/NJD | COL/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.68 | 0.32 | 0.00 | 6.05 | 28.8/28.6 | 25.8/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.57 | 0.43 | 0.46 | 5.9 | 28.5/28.6 | 25.3/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.68 | 0.32 | 0.00 | 9.32 | 30.3/30.3 | 25.3/22.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.081 | 0.72 | 0.28 | 0.00 | 6.0 | 33.8/23.1 | 20.5/28.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.56 | 0.44 | 0.49 | 5.85 | 34.0/23.0 | 19.9/30.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.063 | 0.75 | 0.25 | 0.00 | 9.22 | 35.4/24.2 | 20.0/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Amadeus Lombardi: 1+ goals YES | 9 | 0.123 | 0.114 | +0.028 | +0.018 | $4.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Nicolas Roy: 1+ assists NO | 82 | 0.900 | 0.850 | +0.070 | +0.020 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 68 | 0.723 | 0.711 | +0.028 | +0.016 | $12.59 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Jake Allen: 27+ saves NO | 50 | 0.603 | 0.533 | +0.086 | +0.015 | $8.50 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT28NJCOL-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (8.02 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi -0.021); failure: NJD offense suppressed (<= 2 goals)
- **Nicolas Roy: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT28NJCOL-COLCMAKAR8-1|no; why: higher confidence-adjusted growth (6.01 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi -0.028); failure: COL offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no; why: higher confidence-adjusted growth (2.58 vs 2.39 bp); relationships: KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi 0.032); failure: NJD offense succeeds (4+ goals)
- **Jake Allen: 27+ saves NO** — thesis: NJD net faces light volume (<= 25 shots; COL suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.032); failure: NJD net faces heavy volume (33+ shots; COL pressure)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NJD:SUPPRESSED (p 0.4797): highest fidelity KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:NET_LOW_VOLUME (p 0.3032): highest fidelity KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.3008): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4797, phi -0.174)
- KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4821, phi -0.134)
- KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3008, phi -0.248)
- KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.8 pts; fragile player expression; opposing: failure thesis NJD:NET_HIGH_VOLUME (p 0.2768, phi -0.626)

portfolios: A EV +4.36 (adj +0.87) on $37.50, P(profit) 0.733, adj growth 7.8 bp · B EV +4.91 (adj +1.88) on $45.70, P(profit) 0.4714, adj growth 16.6 bp · C EV +1.83 (adj +0.53) on $20.80, P(profit) 0.4432, adj growth 4.6 bp · R EV +0.16 (adj +0.09) on $4.00, P(profit) 0.723, adj growth 3.1 bp

## TOR @ SEA  ·  10000 joint draws  ·  442 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.446 / away 0.554

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_TOR_win | p_overtime | goals | shots SEA/TOR | SEA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.59 | 0.41 | 0.00 | 6.06 | 29.3/29.1 | 25.8/25.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.46 | 6.02 | 29.3/29.2 | 25.8/26.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.59 | 0.41 | 0.00 | 9.49 | 31.0/31.0 | 25.1/24.0 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.079 | 0.62 | 0.38 | 0.00 | 6.03 | 34.4/23.2 | 20.2/30.0 | even strength |
| SEA shot control · high event (8+) · decided (2+) | 0.067 | 0.66 | 0.34 | 0.00 | 9.38 | 36.2/24.9 | 19.9/28.3 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.56 | 0.44 | 0.44 | 5.98 | 34.4/23.4 | 20.1/31.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Berkly Catton: 1+ goals YES | 15 | 0.219 | 0.197 | +0.060 | +0.038 | $10.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 74 | 0.808 | 0.790 | +0.055 | +0.036 | $20.00 | FUNDED_RESEARCH | $5 | TOR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 11 | 0.156 | 0.141 | +0.040 | +0.024 | $6.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $5.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (22.99 vs 8.24 bp); despite a smaller raw edge (+0.060 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (15.76 vs 8.24 bp); despite a smaller raw edge (+0.055 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: TOR offense succeeds (4+ goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT28TORSEA-3|yes; why: higher confidence-adjusted growth (12.15 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.875 vs 0.74); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT28TORSEA-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: TOR offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: KXNHLSPREAD-26OCT28TORSEA-TOR2|no has the higher standalone adjusted growth (8.24 vs 7.26 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.100); relationships: KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT28TORSEA-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3882): highest fidelity KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.4677): highest fidelity KXNHLTEAMTOTAL-26OCT28TORSEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3912): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3252, phi -0.198)
- KXNHLGOAL-26OCT28TORSEA-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3882, phi -0.21)
- KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3912, phi -0.2)
- KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3252, phi -0.176)

portfolios: A EV +6.98 (adj +1.73) on $37.50, P(profit) 0.4787, adj growth 12.7 bp · B EV +8.59 (adj +5.45) on $41.69, P(profit) 0.4333, adj growth 47.6 bp · C EV +4.58 (adj +2.25) on $26.87, P(profit) 0.8264, adj growth 19.9 bp · R EV +0.36 (adj +0.24) on $5.00, P(profit) 0.8081, adj growth 9.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
