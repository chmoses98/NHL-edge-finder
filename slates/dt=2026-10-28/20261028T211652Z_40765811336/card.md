# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-28T21:16:52Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.01 | +8.02 | +25.00 | 0.698 | -36.52 | -51.67 | 68.56 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +31.20 | +18.08 | +25.45 | 0.640 | -52.09 | -70.39 | 157.69 |
| C best expression per thesis | 145.06 | +24.02 | +13.11 | +20.87 | 0.637 | -46.25 | -63.51 | 114.44 |
| R FUNDED research stakes | 13.00 | +2.89 | +1.74 | -0.61 | 0.300 | -7.42 | -13.00 | 0.00 |

## PHI @ WSH  ·  10000 joint draws  ·  488 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.675 / away 0.325

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PHI_win | p_overtime | goals | shots WSH/PHI | WSH/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.60 | 0.40 | 0.00 | 5.98 | 26.6/26.3 | 23.2/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.45 | 5.85 | 26.6/26.4 | 23.3/23.3 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.092 | 0.66 | 0.34 | 0.00 | 5.99 | 31.4/20.8 | 18.1/26.9 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.54 | 0.46 | 0.48 | 5.88 | 31.6/21.2 | 18.0/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.59 | 0.41 | 0.00 | 9.13 | 28.2/27.8 | 22.3/21.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.60 | 0.40 | 0.00 | 3.48 | 25.4/25.2 | 23.5/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.236 | 0.220 | +0.046 | +0.029 | $7.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 16 | 0.210 | 0.197 | +0.041 | +0.027 | $7.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 27 | 0.343 | 0.304 | +0.059 | +0.020 | $6.18 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
| Dylan Strome: 1+ goals NO | 72 | 0.765 | 0.751 | +0.031 | +0.017 | $16.79 | FUNDED_RESEARCH | $5 | WSH:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (12.03 vs 4.37 bp); despite a smaller raw edge (+0.046 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLGOAL-26OCT28PHIWSH-WSHDSTROME17-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: WSH offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28PHIWSH-PHI2|yes; why: higher confidence-adjusted growth (11.22 vs 5.38 bp); despite a smaller raw edge (+0.041 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.957 vs 0.542); relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT28PHIWSH-WSHDSTROME17-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: PHI offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (12.03 vs 4.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.039); they share one thesis budget; relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT28PHIWSH-WSHDSTROME17-1|no: INTENTIONAL_DIVERSIFIER (phi -0.079); failure: WSH offense suppressed (<= 2 goals)
- **Dylan Strome: 1+ goals NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4|no; why: Player prop expression KXNHLGOAL-26OCT28PHIWSH-WSHDSTROME17-1|no selected over broad KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.87 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.079); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.3993): highest fidelity KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3027): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:SUPPRESSED (p 0.3835): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4|no (same contract)
- KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3835, phi -0.239)
- KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4722, phi -0.222)
- KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3835, phi -0.284)
- KXNHLGOAL-26OCT28PHIWSH-WSHDSTROME17-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.3993, phi -0.2)
- override: Player prop expression KXNHLGOAL-26OCT28PHIWSH-WSHDSTROME17-1|no selected over broad KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.87 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.89 (adj +1.65) on $37.50, P(profit) 0.6307, adj growth 13.6 bp · B EV +5.56 (adj +3.15) on $37.76, P(profit) 0.5402, adj growth 27.6 bp · C EV +6.77 (adj +3.64) on $35.56, P(profit) 0.3974, adj growth 31.6 bp · R EV +0.21 (adj +0.12) on $5.00, P(profit) 0.7647, adj growth 3.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT28PHIWSH-WSH|no == KXNHLGAME-26OCT28PHIWSH-PHI|yes

## CGY @ EDM  ·  10000 joint draws  ·  488 bet sides mapped, 12 +EV candidates, 4 on card

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
| Connor McDavid: 2+ goals YES | 11 | 0.165 | 0.150 | +0.048 | +0.033 | $8.23 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 14 | 0.207 | 0.185 | +0.058 | +0.037 | $8.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 7 | 0.109 | 0.097 | +0.034 | +0.022 | $4.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Ryan Nugent-Hopkins: 1+ assists NO | 60 | 0.689 | 0.640 | +0.072 | +0.023 | $17.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Connor McDavid: 2+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT28CGYEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (22.84 vs 5.10 bp); despite a smaller raw edge (+0.048 vs +0.106/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.114); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes has the higher standalone adjusted growth (22.84 vs 22.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: EDM offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-CGYASUNIEV61-1|yes; why: higher confidence-adjusted growth (14.73 vs 2.85 bp); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: CGY offense suppressed (<= 2 goals)
- **Ryan Nugent-Hopkins: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no; why: KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (6.06 vs 4.82 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.082); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: INTENTIONAL_DIVERSIFIER (phi -0.114); KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, EDM shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5559): highest fidelity KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2493): highest fidelity KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.318): highest fidelity KXNHLGOAL-26OCT28CGYEDM-CGYASUNIEV61-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28CGYEDM-CGYASUNIEV61-1|yes (same contract)
- KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2493, phi -0.228)
- KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2493, phi -0.178)
- KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4641, phi -0.156)
- KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5559, phi -0.218)

portfolios: A EV +8.14 (adj +3.36) on $37.50, P(profit) 0.546, adj growth 29.9 bp · B EV +11.05 (adj +6.54) on $39.19, P(profit) 0.4101, adj growth 56.8 bp · C EV +5.99 (adj +3.40) on $32.25, P(profit) 0.2933, adj growth 29.3 bp · R EV +1.24 (adj +0.85) on $3.00, P(profit) 0.1652, adj growth 27.2 bp

## NJD @ COL  ·  10000 joint draws  ·  456 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.573 / away 0.427

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
| Nicolas Roy: 1+ assists NO | 82 | 0.900 | 0.850 | +0.070 | +0.020 | $18.49 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Jake Allen: 27+ saves NO | 52 | 0.603 | 0.557 | +0.066 | +0.019 | $9.50 | FUNDED_RESEARCH | $3 | NJD:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 68 | 0.723 | 0.711 | +0.028 | +0.016 | $11.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 28 | 0.319 | 0.308 | +0.024 | +0.013 | $4.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Nicolas Roy: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT28NJCOL-COLCMAKAR8-1|no; why: higher confidence-adjusted growth (6.01 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: COL offense succeeds (4+ goals)
- **Jake Allen: 27+ saves NO** — thesis: NJD net faces light volume (<= 25 shots; COL suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.032); KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.037); failure: NJD net faces heavy volume (33+ shots; COL pressure)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no; why: higher confidence-adjusted growth (2.58 vs 2.39 bp); relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi 0.032); KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: NJD offense succeeds (4+ goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28NJCOL-NJ2|no; why: higher confidence-adjusted growth (1.92 vs 0.80 bp); despite a smaller raw edge (+0.024 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi 0.037); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NJD:NET_LOW_VOLUME (p 0.3032): highest fidelity KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no (same contract)
- thesis NJD:SUPPRESSED (p 0.4797): highest fidelity KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:OFFENSE_4PLUS (p 0.4821): highest fidelity KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes (same contract)
- KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4821, phi -0.134)
- KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis NJD:NET_HIGH_VOLUME (p 0.2768, phi -0.626)
- KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3008, phi -0.248)
- KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3093, phi -0.222)

portfolios: A EV +3.96 (adj +0.89) on $37.50, P(profit) 0.733, adj growth 8.0 bp · B EV +3.53 (adj +1.23) on $43.87, P(profit) 0.5342, adj growth 11.2 bp · C EV +2.11 (adj +0.85) on $27.25, P(profit) 0.5797, adj growth 7.5 bp · R EV +0.37 (adj +0.11) on $3.00, P(profit) 0.6034, adj growth 3.7 bp

## TOR @ SEA  ·  10000 joint draws  ·  442 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.449 / away 0.551

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_TOR_win | p_overtime | goals | shots SEA/TOR | SEA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.56 | 0.44 | 0.00 | 6.07 | 29.4/29.3 | 26.0/25.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.60 | 0.40 | 0.00 | 9.39 | 30.9/30.7 | 25.1/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.46 | 5.98 | 29.5/29.2 | 25.8/26.0 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.082 | 0.63 | 0.37 | 0.00 | 6.02 | 34.5/23.4 | 20.5/30.0 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.55 | 0.45 | 0.47 | 5.96 | 34.8/23.7 | 20.4/31.2 | even strength |
| SEA shot control · high event (8+) · decided (2+) | 0.065 | 0.67 | 0.33 | 0.00 | 9.44 | 36.3/24.4 | 19.6/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Freddy Gaudreau: 1+ goals YES | 10 | 0.163 | 0.141 | +0.057 | +0.035 | $7.62 | FUNDED_RESEARCH | $2 | SEA:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 16 | 0.219 | 0.203 | +0.050 | +0.034 | $8.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 11 | 0.160 | 0.145 | +0.043 | +0.028 | $6.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 12 | 0.168 | 0.155 | +0.041 | +0.027 | $6.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (27.28 vs 8.42 bp); despite a smaller raw edge (+0.057 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (17.22 vs 8.42 bp); despite a smaller raw edge (+0.050 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (16.22 vs 8.42 bp); despite a smaller raw edge (+0.043 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (14.50 vs 8.42 bp); despite a smaller raw edge (+0.041 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:WINS_BY_2PLUS (p 0.3423): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT28TORSEA-SEAFGAUDREAU89-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.393): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT28TORSEA-TORGMCKENNA92-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:OFFENSE_4PLUS (p 0.3912): highest fidelity KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes (same contract)
- KXNHLGOAL-26OCT28TORSEA-SEAFGAUDREAU89-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3185, phi -0.19)
- KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3185, phi -0.199)
- KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3185, phi -0.16)
- KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3185, phi -0.165)

portfolios: A EV +7.02 (adj +2.12) on $37.50, P(profit) 0.518, adj growth 17.0 bp · B EV +11.07 (adj +7.16) on $29.18, P(profit) 0.5441, adj growth 62.1 bp · C EV +9.15 (adj +5.22) on $50.00, P(profit) 0.7502, adj growth 46.1 bp · R EV +1.07 (adj +0.66) on $2.00, P(profit) 0.1634, adj growth 22.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
