# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-28T22:13:35Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.34 | +6.45 | +26.15 | 0.720 | -31.03 | -45.72 | 54.84 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +32.88 | +19.26 | +28.01 | 0.662 | -54.42 | -70.52 | 168.90 |
| C best expression per thesis | 150.00 | +26.67 | +13.66 | +22.98 | 0.662 | -38.41 | -51.22 | 122.17 |
| R FUNDED research stakes | 14.00 | +3.40 | +2.08 | -1.61 | 0.336 | -8.42 | -14.00 | 0.00 |

## PHI @ WSH  ·  10000 joint draws  ·  488 bet sides mapped, 23 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.679 / away 0.321

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PHI_win | p_overtime | goals | shots WSH/PHI | WSH/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.60 | 0.40 | 0.00 | 5.97 | 26.6/26.4 | 23.5/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.53 | 0.47 | 0.46 | 5.92 | 26.5/26.1 | 22.9/23.2 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.092 | 0.64 | 0.36 | 0.00 | 5.96 | 31.6/21.0 | 18.2/27.3 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.58 | 0.42 | 0.48 | 5.84 | 31.8/21.1 | 18.0/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.59 | 0.41 | 0.00 | 9.16 | 28.4/27.8 | 22.0/22.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.56 | 0.44 | 0.00 | 3.44 | 25.5/25.4 | 23.6/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.235 | 0.220 | +0.045 | +0.030 | $7.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 16 | 0.210 | 0.196 | +0.041 | +0.027 | $6.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Dylan Strome: 1+ goals NO | 72 | 0.770 | 0.755 | +0.036 | +0.021 | $17.82 | FUNDED_RESEARCH | $5 | WSH:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 27 | 0.342 | 0.303 | +0.058 | +0.020 | $5.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (12.38 vs 4.16 bp); despite a smaller raw edge (+0.045 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT28PHIWSH-WSHDSTROME17-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.037); failure: WSH offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28PHIWSH-PHICKNUBLE54-1|yes; why: higher confidence-adjusted growth (11.10 vs 6.37 bp); relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT28PHIWSH-WSHDSTROME17-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: PHI offense suppressed (<= 2 goals)
- **Dylan Strome: 1+ goals NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no; why: Player prop expression KXNHLGOAL-26OCT28PHIWSH-WSHDSTROME17-1|no selected over broad KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.094); failure: WSH offense succeeds (4+ goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (12.38 vs 4.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.037); they share one thesis budget; relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.037); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT28PHIWSH-WSHDSTROME17-1|no: INTENTIONAL_DIVERSIFIER (phi -0.094); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4025): highest fidelity KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3072): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SUPPRESSED (p 0.4753): highest fidelity KXNHLAST-26OCT28PHIWSH-PHICYORK8-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT28PHIWSH-PHICYORK8-1|no (same contract)
- KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3829, phi -0.251)
- KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4753, phi -0.233)
- KXNHLGOAL-26OCT28PHIWSH-WSHDSTROME17-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4025, phi -0.206)
- KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3829, phi -0.258)
- override: Player prop expression KXNHLGOAL-26OCT28PHIWSH-WSHDSTROME17-1|no selected over broad KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +8.61 (adj +1.47) on $37.50, P(profit) 0.6045, adj growth 11.8 bp · B EV +5.51 (adj +3.18) on $38.10, P(profit) 0.5365, adj growth 28.1 bp · C EV +8.10 (adj +4.12) on $42.93, P(profit) 0.5991, adj growth 37.0 bp · R EV +0.25 (adj +0.14) on $5.00, P(profit) 0.7704, adj growth 5.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT28PHIWSH-WSH|no == KXNHLGAME-26OCT28PHIWSH-PHI|yes

## CGY @ EDM  ·  10000 joint draws  ·  488 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.619 / away 0.381

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
| Alex Formenton: 1+ goals YES | 14 | 0.207 | 0.186 | +0.058 | +0.038 | $8.85 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ goals YES | 11 | 0.165 | 0.150 | +0.048 | +0.033 | $7.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 7 | 0.109 | 0.095 | +0.034 | +0.021 | $4.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Ryan Nugent-Hopkins: 1+ assists NO | 60 | 0.689 | 0.642 | +0.072 | +0.025 | $17.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes; why: higher confidence-adjusted growth (24.19 vs 22.84 bp); wins across more scripts (relative breadth 0.826 vs 0.719); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT28CGYEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (22.84 vs 6.42 bp); despite a smaller raw edge (+0.048 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.114); failure: EDM offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-CGYASUNIEV61-1|yes; why: higher confidence-adjusted growth (13.12 vs 2.85 bp); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: CGY offense suppressed (<= 2 goals)
- **Ryan Nugent-Hopkins: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no; why: KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (6.06 vs 5.94 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.082); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: INTENTIONAL_DIVERSIFIER (phi -0.114); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, EDM shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5559): highest fidelity KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2493): highest fidelity KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.318): highest fidelity KXNHLGOAL-26OCT28CGYEDM-CGYASUNIEV61-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28CGYEDM-CGYASUNIEV61-1|yes (same contract)
- KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2493, phi -0.178)
- KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2493, phi -0.228)
- KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4641, phi -0.156)
- KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5559, phi -0.218)

portfolios: A EV +6.67 (adj +1.90) on $37.50, P(profit) 0.5302, adj growth 16.5 bp · B EV +10.76 (adj +6.41) on $38.79, P(profit) 0.4101, adj growth 56.0 bp · C EV +5.14 (adj +2.92) on $27.69, P(profit) 0.2933, adj growth 25.7 bp · R EV +1.18 (adj +0.76) on $3.00, P(profit) 0.2067, adj growth 25.4 bp

## NJD @ COL  ·  10000 joint draws  ·  456 bet sides mapped, 8 +EV candidates, 4 on card

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
| Nicolas Roy: 1+ assists NO | 79 | 0.900 | 0.825 | +0.098 | +0.024 | $17.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Jake Allen: 27+ saves NO | 52 | 0.603 | 0.559 | +0.066 | +0.022 | $10.38 | FUNDED_RESEARCH | $3 | NJD:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 68 | 0.723 | 0.711 | +0.028 | +0.016 | $11.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 28 | 0.319 | 0.308 | +0.024 | +0.013 | $4.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Nicolas Roy: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT28NJCOL-COLNROY10-1|no; why: higher confidence-adjusted growth (7.72 vs 0.02 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: COL offense succeeds (4+ goals)
- **Jake Allen: 27+ saves NO** — thesis: NJD net faces light volume (<= 25 shots; COL suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.032); KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.037); failure: NJD net faces heavy volume (33+ shots; COL pressure)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no; why: Player prop expression KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi 0.032); KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: NJD offense succeeds (4+ goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28NJCOL-NJ2|no; why: higher confidence-adjusted growth (1.92 vs 0.80 bp); despite a smaller raw edge (+0.024 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi 0.037); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NJD:NET_LOW_VOLUME (p 0.3032): highest fidelity KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no (same contract)
- thesis NJD:SUPPRESSED (p 0.4797): highest fidelity KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no — Player prop expression KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis COL:NET_LOW_VOLUME (p 0.3591): highest fidelity KXNHLSAVE-26OCT28NJCOL-COLMBLACKWOOD39-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT28NJCOL-COLMBLACKWOOD39-27|no (same contract)
- KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.5 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4821, phi -0.134)
- KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis NJD:NET_HIGH_VOLUME (p 0.2768, phi -0.626)
- KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3008, phi -0.248)
- KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3093, phi -0.222)
- override: Player prop expression KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.67 (adj +1.17) on $37.50, P(profit) 0.7022, adj growth 10.8 bp · B EV +4.24 (adj +1.38) on $43.41, P(profit) 0.5342, adj growth 12.7 bp · C EV +4.55 (adj +1.20) on $36.45, P(profit) 0.5566, adj growth 10.7 bp · R EV +0.37 (adj +0.12) on $3.00, P(profit) 0.6034, adj growth 4.3 bp

## TOR @ SEA  ·  10000 joint draws  ·  442 bet sides mapped, 19 +EV candidates, 4 on card

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
| Freddy Gaudreau: 1+ goals YES | 10 | 0.163 | 0.144 | +0.057 | +0.037 | $8.04 | FUNDED_RESEARCH | $3 | SEA:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 10 | 0.155 | 0.140 | +0.049 | +0.034 | $7.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 16 | 0.219 | 0.203 | +0.050 | +0.034 | $8.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 11 | 0.160 | 0.145 | +0.043 | +0.028 | $6.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (31.25 vs 8.42 bp); despite a smaller raw edge (+0.057 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SEA offense suppressed (<= 2 goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT28TORSEA-TORMRIELLY44-1|yes; why: higher confidence-adjusted growth (25.77 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT28TORSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: TOR offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (17.22 vs 8.42 bp); despite a smaller raw edge (+0.050 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (16.22 vs 8.42 bp); despite a smaller raw edge (+0.043 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:WINS_BY_2PLUS (p 0.3423): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT28TORSEA-SEAFGAUDREAU89-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:OFFENSE_4PLUS (p 0.3912): highest fidelity KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.393): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT28TORSEA-SEAFGAUDREAU89-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3185, phi -0.19)
- KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.393, phi -0.194)
- KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3185, phi -0.199)
- KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3185, phi -0.16)

portfolios: A EV +6.38 (adj +1.91) on $37.50, P(profit) 0.5004, adj growth 15.8 bp · B EV +12.38 (adj +8.29) on $29.69, P(profit) 0.536, adj growth 72.1 bp · C EV +8.86 (adj +5.42) on $42.93, P(profit) 0.2951, adj growth 48.7 bp · R EV +1.61 (adj +1.06) on $3.00, P(profit) 0.1634, adj growth 34.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
