# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-28T23:56:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +24.61 | +6.23 | +23.33 | 0.678 | -36.67 | -54.04 | 50.28 |
| B thesis-diversified (joint) ← optimiser card | 119.00 | +24.54 | +13.08 | +18.82 | 0.616 | -47.04 | -62.72 | 113.01 |
| C best expression per thesis | 101.79 | +15.01 | +7.22 | +11.79 | 0.607 | -33.37 | -46.40 | 62.96 |
| R FUNDED research stakes | 9.00 | +1.91 | +1.17 | -2.72 | 0.412 | -9.00 | -9.00 | 0.00 |

## CGY @ EDM  ·  10000 joint draws  ·  488 bet sides mapped, 14 +EV candidates, 4 on card

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
| Alex Formenton: 1+ goals YES | 14 | 0.207 | 0.184 | +0.058 | +0.035 | $9.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 7 | 0.109 | 0.095 | +0.034 | +0.021 | $4.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Ryan Nugent-Hopkins: 1+ assists NO | 60 | 0.689 | 0.642 | +0.072 | +0.025 | $19.32 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Connor McDavid: 1+ goals YES | 46 | 0.512 | 0.498 | +0.035 | +0.021 | $11.67 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | DIRECT (0.65) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes; why: higher confidence-adjusted growth (21.14 vs 12.31 bp); wins across more scripts (relative breadth 0.826 vs 0.719); relationships: KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: EDM offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-CGYMBACKLUND11-1|yes; why: higher confidence-adjusted growth (13.12 vs 1.23 bp); alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: CGY offense suppressed (<= 2 goals)
- **Ryan Nugent-Hopkins: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (5.94 vs 1.99 bp); despite a smaller raw edge (+0.072 vs +0.089/contract); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.134); failure: EDM offense succeeds (4+ goals)
- **Connor McDavid: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes; why: Player prop expression KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.65 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.134); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, EDM shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5559): highest fidelity KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes — Player prop expression KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.65 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis EDM:SUPPRESSED (p 0.2493): highest fidelity KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.318): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2493, phi -0.178)
- KXNHLGOAL-26OCT28CGYEDM-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4641, phi -0.156)
- KXNHLAST-26OCT28CGYEDM-EDMRNUGENTHOPKINS93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5559, phi -0.218)
- KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 35% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2493, phi -0.304)
- override: Player prop expression KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.65 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +9.70 (adj +2.59) on $50.00, P(profit) 0.5945, adj growth 21.4 bp · B EV +8.90 (adj +4.80) on $44.93, P(profit) 0.5235, adj growth 41.4 bp · C EV +4.50 (adj +2.26) on $27.27, P(profit) 0.7602, adj growth 19.6 bp · R EV +0.22 (adj +0.13) on $3.00, P(profit) 0.5124, adj growth 4.4 bp

## NJD @ COL  ·  10000 joint draws  ·  456 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.576 / away 0.424

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
| Nicolas Roy: 1+ assists NO | 79 | 0.900 | 0.825 | +0.098 | +0.024 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Amadeus Lombardi: 1+ goals YES | 10 | 0.123 | 0.116 | +0.017 | +0.010 | $2.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Jake Allen: 27+ saves NO | 53 | 0.603 | 0.562 | +0.056 | +0.014 | $8.19 | FUNDED_RESEARCH | $3 | NJD:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Luke Evangelista: 1+ assists NO | 67 | 0.776 | 0.698 | +0.091 | +0.012 | $11.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Nicolas Roy: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT28NJCOL-COLNROY10-1|no; why: higher confidence-adjusted growth (7.72 vs 0.02 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: COL offense succeeds (4+ goals)
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT28NJCOL-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (2.31 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: NJD offense suppressed (<= 2 goals)
- **Jake Allen: 27+ saves NO** — thesis: NJD net faces light volume (<= 25 shots; COL suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.039); failure: NJD net faces heavy volume (33+ shots; COL pressure)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (1.48 vs 1.31 bp); relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi 0.039); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NJD:NET_LOW_VOLUME (p 0.3032): highest fidelity KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no (same contract)
- thesis NJD:SUPPRESSED (p 0.4797): highest fidelity KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:NET_LOW_VOLUME (p 0.3591): highest fidelity KXNHLSAVE-26OCT28NJCOL-COLMBLACKWOOD39-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT28NJCOL-COLMBLACKWOOD39-27|no (same contract)
- KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.5 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4821, phi -0.134)
- KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4797, phi -0.175)
- KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis NJD:NET_HIGH_VOLUME (p 0.2768, phi -0.626)
- KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3008, phi -0.213)

portfolios: A EV +6.40 (adj +1.09) on $50.00, P(profit) 0.7152, adj growth 9.3 bp · B EV +5.21 (adj +1.26) on $42.04, P(profit) 0.4965, adj growth 11.4 bp · C EV +2.96 (adj +0.52) on $25.49, P(profit) 0.7445, adj growth 4.5 bp · R EV +0.31 (adj +0.08) on $3.00, P(profit) 0.6034, adj growth 2.5 bp

## TOR @ SEA  ·  10000 joint draws  ·  442 bet sides mapped, 22 +EV candidates, 4 on card

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
| Teddy Blueger: 1+ goals YES | 10 | 0.155 | 0.140 | +0.049 | +0.034 | $8.38 | FUNDED_RESEARCH | $3 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 16 | 0.219 | 0.203 | +0.050 | +0.034 | $9.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 11 | 0.160 | 0.145 | +0.043 | +0.028 | $6.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Mackie Samoskevich: 1+ goals YES | 20 | 0.248 | 0.235 | +0.037 | +0.024 | $7.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT28TORSEA-3|yes; why: higher confidence-adjusted growth (25.77 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.881 vs 0.77); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT28TORSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: TOR offense suppressed (<= 2 goals)
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

portfolios: A EV +8.50 (adj +2.55) on $50.00, P(profit) 0.5004, adj growth 19.6 bp · B EV +10.44 (adj +7.02) on $32.03, P(profit) 0.587, adj growth 60.1 bp · C EV +7.55 (adj +4.44) on $49.03, P(profit) 0.716, adj growth 38.8 bp · R EV +1.39 (adj +0.96) on $3.00, P(profit) 0.1554, adj growth 30.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
