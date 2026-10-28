# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-28T23:03:30Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.69 | +6.44 | +26.95 | 0.721 | -31.26 | -45.76 | 53.94 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +28.71 | +16.85 | +23.53 | 0.643 | -48.88 | -66.77 | 148.38 |
| C best expression per thesis | 150.01 | +25.64 | +11.26 | +23.10 | 0.669 | -37.28 | -51.71 | 99.37 |
| R FUNDED research stakes | 15.00 | +2.59 | +1.54 | +0.76 | 0.515 | -10.68 | -10.68 | 0.00 |

## PHI @ WSH  ·  10000 joint draws  ·  488 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.677 / away 0.323

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PHI_win | p_overtime | goals | shots WSH/PHI | WSH/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.63 | 0.37 | 0.00 | 6.02 | 26.7/26.6 | 23.7/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.47 | 5.86 | 26.8/26.4 | 23.3/23.6 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.095 | 0.67 | 0.33 | 0.00 | 5.98 | 31.4/20.6 | 17.9/26.7 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.60 | 0.40 | 0.45 | 5.84 | 31.7/21.2 | 18.2/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.58 | 0.42 | 0.00 | 9.14 | 28.5/28.2 | 22.7/22.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.61 | 0.39 | 0.00 | 3.43 | 25.4/25.1 | 23.5/23.1 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.238 | 0.223 | +0.048 | +0.032 | $9.92 | FUNDED_RESEARCH | $3 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 10 | 0.141 | 0.130 | +0.035 | +0.023 | $5.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 16 | 0.210 | 0.196 | +0.040 | +0.026 | $6.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Washington over 3.5 goals scored NO | 50 | 0.591 | 0.543 | +0.073 | +0.025 | $15.93 | FUNDED_RESEARCH | $4 | WSH:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (14.51 vs 4.57 bp); despite a smaller raw edge (+0.048 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4|no: INTENTIONAL_DIVERSIFIER (phi -0.245); failure: WSH offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (12.12 vs 10.79 bp); despite a smaller raw edge (+0.035 vs +0.040/contract); relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4|no: MOSTLY_INDEPENDENT (phi 0.034); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (12.12 vs 10.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4|no: MOSTLY_INDEPENDENT (phi 0.01); failure: PHI offense suppressed (<= 2 goals)
- **Washington over 3.5 goals scored NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no; why: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no has the higher standalone adjusted growth (6.51 vs 5.70 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.628); relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.245); KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.3996): highest fidelity KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.2857): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:SUPPRESSED (p 0.3762): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4|no (same contract)
- KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3762, phi -0.236)
- KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4942, phi -0.2)
- KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4942, phi -0.217)
- KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.3996, phi -0.981)

portfolios: A EV +8.29 (adj +1.35) on $37.50, P(profit) 0.5961, adj growth 10.5 bp · B EV +7.95 (adj +4.58) on $37.37, P(profit) 0.4863, adj growth 40.4 bp · C EV +10.43 (adj +4.14) on $46.30, P(profit) 0.6432, adj growth 36.5 bp · R EV +1.33 (adj +0.70) on $7.00, P(profit) 0.7398, adj growth 24.5 bp

## CGY @ EDM  ·  10000 joint draws  ·  488 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.620 / away 0.380

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
| Alex Formenton: 1+ goals YES | 14 | 0.207 | 0.188 | +0.058 | +0.039 | $9.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 7 | 0.109 | 0.098 | +0.034 | +0.023 | $4.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Ryan Nugent-Hopkins: 1+ assists NO | 60 | 0.689 | 0.642 | +0.072 | +0.025 | $16.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Connor McDavid: 1+ goals YES | 46 | 0.512 | 0.498 | +0.035 | +0.021 | $10.19 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | DIRECT (0.65) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes; why: higher confidence-adjusted growth (25.80 vs 12.31 bp); wins across more scripts (relative breadth 0.826 vs 0.719); relationships: KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: EDM offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-CGYMBACKLUND11-1|yes; why: higher confidence-adjusted growth (16.43 vs 1.23 bp); alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: CGY offense suppressed (<= 2 goals)
- **Ryan Nugent-Hopkins: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (5.94 vs 2.63 bp); despite a smaller raw edge (+0.072 vs +0.082/contract); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.134); failure: EDM offense succeeds (4+ goals)
- **Connor McDavid: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes; why: Player prop expression KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.65 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.134); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, EDM shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5559): highest fidelity KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes — Player prop expression KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.65 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis EDM:SUPPRESSED (p 0.2493): highest fidelity KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.318): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2493, phi -0.178)
- KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4641, phi -0.156)
- KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5559, phi -0.218)
- KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 35% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2493, phi -0.304)
- override: Player prop expression KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.65 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +8.54 (adj +2.23) on $37.50, P(profit) 0.6673, adj growth 19.0 bp · B EV +8.45 (adj +5.00) on $40.85, P(profit) 0.5235, adj growth 43.8 bp · C EV +4.17 (adj +2.09) on $25.25, P(profit) 0.7602, adj growth 18.4 bp · R EV +0.22 (adj +0.13) on $3.00, P(profit) 0.5124, adj growth 4.4 bp

## NJD @ COL  ·  10000 joint draws  ·  456 bet sides mapped, 8 +EV candidates, 4 on card

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
| Nicolas Roy: 1+ assists NO | 79 | 0.900 | 0.825 | +0.098 | +0.024 | $16.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 68 | 0.723 | 0.711 | +0.028 | +0.016 | $10.71 | FUNDED_RESEARCH | $3 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 76 | 0.797 | 0.787 | +0.024 | +0.014 | $12.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 28 | 0.319 | 0.308 | +0.024 | +0.013 | $3.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Nicolas Roy: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT28NJCOL-COLNROY10-1|no; why: higher confidence-adjusted growth (7.72 vs 0.02 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: COL offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no; why: KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no has the higher standalone adjusted growth (3.52 vs 2.58 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.075); relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: NJD offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no; why: Player prop expression KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: NJD offense succeeds (4+ goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28NJCOL-NJ2|no; why: higher confidence-adjusted growth (1.92 vs 0.80 bp); despite a smaller raw edge (+0.024 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NJD:SUPPRESSED (p 0.4797): highest fidelity KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no — Player prop expression KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis COL:OFFENSE_4PLUS (p 0.4821): highest fidelity KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes (same contract)
- thesis NJD:NET_LOW_VOLUME (p 0.3032): highest fidelity KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no (same contract)
- KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.5 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4821, phi -0.134)
- KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3008, phi -0.248)
- KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3008, phi -0.214)
- KXNHLGOAL-26OCT28NJCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3093, phi -0.222)
- override: Player prop expression KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.48 (adj +0.95) on $37.50, P(profit) 0.7022, adj growth 8.6 bp · B EV +3.17 (adj +1.13) on $43.75, P(profit) 0.6393, adj growth 10.5 bp · C EV +4.06 (adj +0.92) on $33.06, P(profit) 0.7253, adj growth 8.2 bp · R EV +0.12 (adj +0.07) on $3.00, P(profit) 0.723, adj growth 2.4 bp

## TOR @ SEA  ·  10000 joint draws  ·  442 bet sides mapped, 20 +EV candidates, 4 on card

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
| Teddy Blueger: 1+ goals YES | 10 | 0.155 | 0.140 | +0.049 | +0.034 | $7.33 | FUNDED_RESEARCH | $2 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 16 | 0.219 | 0.203 | +0.050 | +0.034 | $8.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 11 | 0.160 | 0.145 | +0.043 | +0.028 | $6.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Mackie Samoskevich: 1+ goals YES | 20 | 0.248 | 0.235 | +0.037 | +0.024 | $6.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT28TORSEA-TORMRIELLY44-1|yes; why: higher confidence-adjusted growth (25.77 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT28TORSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: TOR offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (17.22 vs 8.42 bp); despite a smaller raw edge (+0.050 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT28TORSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (16.22 vs 8.42 bp); despite a smaller raw edge (+0.043 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT28TORSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)
- **Mackie Samoskevich: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: KXNHLSPREAD-26OCT28TORSEA-TOR2|no has the higher standalone adjusted growth (8.42 vs 7.40 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.128); relationships: KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3912): highest fidelity KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.393): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.476): highest fidelity KXNHLTEAMTOTAL-26OCT28TORSEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.393, phi -0.194)
- KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3185, phi -0.199)
- KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3185, phi -0.16)
- KXNHLGOAL-26OCT28TORSEA-SEAMSAMOSKEVICH11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3185, phi -0.2)

portfolios: A EV +6.38 (adj +1.91) on $37.50, P(profit) 0.5004, adj growth 15.8 bp · B EV +9.13 (adj +6.14) on $28.03, P(profit) 0.587, adj growth 53.7 bp · C EV +6.99 (adj +4.11) on $45.40, P(profit) 0.716, adj growth 36.3 bp · R EV +0.92 (adj +0.64) on $2.00, P(profit) 0.1554, adj growth 22.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
