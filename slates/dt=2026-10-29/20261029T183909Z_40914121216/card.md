# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-29T18:39:09Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +34.30 | +11.74 | +31.41 | 0.761 | -23.29 | -37.09 | 106.25 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +27.23 | +15.41 | +24.91 | 0.730 | -26.34 | -38.69 | 144.65 |
| C best expression per thesis | 150.01 | +26.26 | +13.46 | +23.28 | 0.687 | -33.05 | -45.86 | 123.16 |
| R FUNDED research stakes | 21.00 | +1.99 | +1.18 | +1.95 | 0.608 | -6.33 | -8.21 | 0.00 |

## WPG @ TBL  ·  10000 joint draws  ·  418 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.655 / away 0.345

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WPG_win | p_overtime | goals | shots TBL/WPG | TBL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.123 | 0.75 | 0.25 | 0.00 | 5.98 | 32.4/21.0 | 18.6/27.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.69 | 0.31 | 0.00 | 5.99 | 27.3/26.8 | 24.0/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.47 | 5.91 | 27.0/26.6 | 23.4/23.7 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.59 | 0.41 | 0.46 | 5.82 | 32.6/21.4 | 18.4/29.1 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.067 | 0.79 | 0.21 | 0.00 | 9.13 | 33.9/22.3 | 18.2/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.066 | 0.71 | 0.29 | 0.00 | 9.18 | 28.6/28.0 | 23.2/21.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charle-Edouard D'Astous: 1+ goals NO | 89 | 0.929 | 0.918 | +0.032 | +0.021 | $9.39 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Adam Lowry: 1+ goals YES | 9 | 0.118 | 0.110 | +0.022 | +0.014 | $1.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 25 | 0.290 | 0.279 | +0.027 | +0.016 | $2.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 11 | 0.139 | 0.128 | +0.022 | +0.011 | $1.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no; why: higher confidence-adjusted growth (10.50 vs 2.34 bp); despite a smaller raw edge (+0.032 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.001 vs 0.58); relationships: KXNHLGOAL-26OCT29WPGTB-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: TBL offense succeeds (4+ goals)
- **Adam Lowry: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (4.99 vs 2.74 bp); despite a smaller raw edge (+0.022 vs +0.027/contract); relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (2.74 vs 0.74 bp); alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29WPGTB-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: WPG offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes has the higher standalone adjusted growth (2.74 vs 2.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29WPGTB-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.2594): highest fidelity KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.3355): highest fidelity KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no [FRAGILE], best adjusted EV KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no (same contract)
- KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4503, phi -0.108)
- KXNHLGOAL-26OCT29WPGTB-WPGALOWRY17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.535, phi -0.165)
- KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.535, phi -0.296)
- KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.535, phi -0.192)

portfolios: A EV +1.93 (adj +0.93) on $15.02, P(profit) 0.4444, adj growth 8.4 bp · B EV +1.23 (adj +0.74) on $14.82, P(profit) 0.4359, adj growth 7.0 bp · C EV +0.81 (adj +0.35) on $5.00, P(profit) 0.3951, adj growth 3.2 bp · R EV +0.11 (adj +0.07) on $3.00, P(profit) 0.9286, adj growth 2.7 bp

## UTA @ PIT  ·  10000 joint draws  ·  396 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.459 / away 0.541

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_UTA_win | p_overtime | goals | shots PIT/UTA | PIT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.51 | 0.49 | 0.00 | 6.06 | 27.2/27.3 | 23.9/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.45 | 6.01 | 27.4/27.5 | 24.2/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.49 | 0.51 | 0.00 | 9.51 | 28.8/29.0 | 22.4/22.6 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.071 | 0.57 | 0.43 | 0.00 | 6.04 | 32.1/21.7 | 18.6/28.2 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.070 | 0.44 | 0.56 | 0.00 | 6.05 | 21.6/32.0 | 27.9/18.5 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.53 | 0.47 | 0.47 | 5.92 | 32.0/21.7 | 18.6/28.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nick Robertson: 1+ goals YES | 16 | 0.251 | 0.227 | +0.082 | +0.058 | $6.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 9 | 0.154 | 0.136 | +0.059 | +0.040 | $3.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ goals YES | 32 | 0.381 | 0.365 | +0.046 | +0.029 | $4.21 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 19 | 0.224 | 0.213 | +0.024 | +0.013 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Nick Robertson: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (49.87 vs 38.59 bp); relationships: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT29UTAPIT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes has the higher standalone adjusted growth (49.87 vs 38.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT29UTAPIT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.53 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT29UTAPIT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: PIT offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-UTAALEE72-1|yes; why: higher confidence-adjusted growth (2.13 vs 0.17 bp); alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4347): highest fidelity KXNHLAST-26OCT29UTAPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes — Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.53 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis UTA:OFFENSE_4PLUS (p 0.4353): highest fidelity KXNHLGOAL-26OCT29UTAPIT-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-UTALCROUSE67-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3547): highest fidelity KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no (same contract)
- KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.217)
- KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.195)
- KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.267)
- KXNHLGOAL-26OCT29UTAPIT-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3547, phi -0.221)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.53 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +7.96 (adj +2.91) on $16.82, P(profit) 0.5189, adj growth 26.8 bp · B EV +6.04 (adj +4.13) on $16.03, P(profit) 0.4239, adj growth 38.8 bp · C EV +5.41 (adj +3.73) on $18.64, P(profit) 0.3694, adj growth 33.7 bp · R EV +0.27 (adj +0.18) on $2.00, P(profit) 0.3812, adj growth 6.3 bp

## CBJ @ CAR  ·  10000 joint draws  ·  440 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.687 / away 0.313

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CBJ_win | p_overtime | goals | shots CAR/CBJ | CAR/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.145 | 0.67 | 0.33 | 0.00 | 6.0 | 33.6/20.9 | 18.2/29.2 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.128 | 0.53 | 0.47 | 0.47 | 5.9 | 33.6/21.3 | 18.0/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.097 | 0.57 | 0.43 | 0.00 | 5.97 | 27.5/26.8 | 23.5/23.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.089 | 0.65 | 0.35 | 0.00 | 9.27 | 35.4/22.7 | 17.8/27.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.50 | 0.50 | 0.45 | 5.94 | 27.8/26.9 | 23.7/24.3 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.075 | 0.52 | 0.48 | 0.46 | 2.78 | 32.5/20.0 | 18.5/30.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 13 | 0.185 | 0.170 | +0.047 | +0.032 | $3.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Sean Monahan: 1+ goals YES | 14 | 0.184 | 0.171 | +0.036 | +0.022 | $2.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Seth Jarvis: 1+ goals NO | 70 | 0.751 | 0.737 | +0.036 | +0.022 | $7.80 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 67 | 0.722 | 0.705 | +0.036 | +0.020 | $6.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJSMONAHAN23-1|yes; why: higher confidence-adjusted growth (18.34 vs 8.48 bp); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (18.34 vs 8.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: CBJ offense suppressed (<= 2 goals)
- **Seth Jarvis: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes; why: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes has the higher standalone adjusted growth (6.61 vs 5.44 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.123); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29CBJCAR-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: CAR offense succeeds (4+ goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes; why: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes has the higher standalone adjusted growth (6.61 vs 3.95 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.131); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29CBJCAR-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.3293): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.2133): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.3571): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29CBJCAR-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4607, phi -0.225)
- KXNHLGOAL-26OCT29CBJCAR-CBJSMONAHAN23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4607, phi -0.199)
- KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4247, phi -0.212)
- KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4247, phi -0.214)

portfolios: A EV +3.63 (adj +0.68) on $16.82, P(profit) 0.5736, adj growth 6.1 bp · B EV +2.72 (adj +1.74) on $20.73, P(profit) 0.324, adj growth 16.3 bp · C EV +3.51 (adj +1.64) on $12.72, P(profit) 0.3269, adj growth 14.9 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7512, adj growth 2.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT29CBJCAR-CBJ|yes == KXNHLGAME-26OCT29CBJCAR-CAR|no

## CHI @ DET  ·  10000 joint draws  ·  426 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_CHI_win | p_overtime | goals | shots DET/CHI | DET/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.138 | 0.70 | 0.30 | 0.00 | 5.99 | 33.2/21.0 | 18.5/28.5 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.55 | 0.45 | 0.50 | 5.93 | 33.4/21.4 | 18.2/30.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.64 | 0.36 | 0.00 | 5.99 | 27.3/26.6 | 23.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.52 | 0.48 | 0.46 | 5.88 | 27.7/26.8 | 23.6/24.5 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.083 | 0.73 | 0.27 | 0.00 | 9.21 | 34.8/22.5 | 18.2/26.7 | even strength |
| DET shot control · low event (<=4) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 3.44 | 31.5/19.9 | 18.6/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Emmitt Finnie: 1+ assists YES | 32 | 0.402 | 0.359 | +0.067 | +0.023 | $3.73 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
| Patrick Kane: 1+ assists NO | 58 | 0.715 | 0.621 | +0.118 | +0.024 | $8.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Anton Frondell: 1+ goals YES | 16 | 0.198 | 0.183 | +0.028 | +0.014 | $2.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 41 | 0.451 | 0.439 | +0.024 | +0.012 | $1.44 | FUNDED_RESEARCH | $1 | DET:OFFENSE_4PLUS | DIRECT (0.63) | EVIDENCE_STRONGER | D |
- **Emmitt Finnie: 1+ assists YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT29CHIDET-DETEFINNIE58-2|yes; why: KXNHLAST-26OCT29CHIDET-DETEFINNIE58-2|yes has the higher standalone adjusted growth (7.54 vs 5.34 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.403); relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT29CHIDET-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: REINFORCING (phi 0.22); failure: DET offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no; why: higher confidence-adjusted growth (5.07 vs 0.72 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLAST-26OCT29CHIDET-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT29CHIDET-CHIAFRONDELL16-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.061); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CHI offense succeeds (4+ goals)
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CHIDET-CHIRDONATO8-1|yes; why: higher confidence-adjusted growth (2.94 vs 0.09 bp); alternative not eligible: confidence-adjusted EV +0.0023 below the 0.010/contract floor; relationships: KXNHLAST-26OCT29CHIDET-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.061); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CHI offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT29CHIDET-DETEFINNIE58-2|yes; why: Player prop expression KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT29CHIDET-DETACOPP18-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.63 vs 0.31 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLAST-26OCT29CHIDET-DETEFINNIE58-1|yes: REINFORCING (phi 0.22); KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29CHIDET-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.14, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis DET:OFFENSE_4PLUS (p 0.4373): highest fidelity KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT29CHIDET-DETEFINNIE58-1|yes — Player prop expression KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT29CHIDET-DETACOPP18-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.63 vs 0.31 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis CHI:SUPPRESSED (p 0.4966): highest fidelity KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.2834): highest fidelity KXNHLGOAL-26OCT29CHIDET-CHIAFRONDELL16-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29CHIDET-CHIAFRONDELL16-1|yes (same contract)
- KXNHLAST-26OCT29CHIDET-DETEFINNIE58-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3444, phi -0.285)
- KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.5 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2834, phi -0.259)
- KXNHLGOAL-26OCT29CHIDET-CHIAFRONDELL16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4966, phi -0.235)
- KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 37% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3444, phi -0.317)
- override: Player prop expression KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT29CHIDET-DETACOPP18-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.63 vs 0.31 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +4.65 (adj +1.30) on $16.82, P(profit) 0.3677, adj growth 11.0 bp · B EV +2.76 (adj +0.79) on $15.31, P(profit) 0.5324, adj growth 7.4 bp · C EV +4.40 (adj +1.14) on $20.02, P(profit) 0.5774, adj growth 10.4 bp · R EV +0.06 (adj +0.03) on $1.00, P(profit) 0.4508, adj growth 1.1 bp

## BOS @ STL  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.503 / away 0.497

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_BOS_win | p_overtime | goals | shots STL/BOS | STL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.54 | 0.46 | 0.00 | 5.98 | 27.2/26.9 | 23.5/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.49 | 0.51 | 0.47 | 5.97 | 27.3/27.1 | 23.7/24.0 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.089 | 0.61 | 0.39 | 0.00 | 5.98 | 32.3/21.5 | 18.6/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.51 | 0.49 | 0.00 | 9.35 | 29.0/28.6 | 22.7/22.5 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.55 | 0.45 | 0.45 | 5.92 | 32.5/21.6 | 18.4/29.2 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.061 | 0.63 | 0.37 | 0.00 | 9.29 | 34.1/23.0 | 18.0/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Casey Mittelstadt: 1+ goals YES | 14 | 0.179 | 0.167 | +0.030 | +0.018 | $2.37 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 24 | 0.282 | 0.271 | +0.030 | +0.018 | $2.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 29 | 0.331 | 0.319 | +0.026 | +0.015 | $2.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT29BOSSTL-9|yes; why: higher confidence-adjusted growth (5.60 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.916 vs 0.374); alternative not eligible: confidence-adjusted EV +0.0010 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: BOS offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (3.67 vs 2.23 bp); relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (3.67 vs 2.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.4127): highest fidelity KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.3665): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4158, phi -0.197)
- KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3698, phi -0.252)
- KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3698, phi -0.282)

portfolios: A EV +1.27 (adj +0.75) on $9.49, P(profit) 0.6064, adj growth 6.9 bp · B EV +1.01 (adj +0.60) on $7.51, P(profit) 0.6064, adj growth 5.6 bp · C EV +0.44 (adj +0.27) on $3.78, P(profit) 0.2825, adj growth 2.4 bp · R EV +0.20 (adj +0.12) on $1.00, P(profit) 0.1787, adj growth 4.3 bp

## WSH @ NSH  ·  10000 joint draws  ·  432 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.498 / away 0.502

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_WSH_win | p_overtime | goals | shots NSH/WSH | NSH/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.58 | 0.42 | 0.00 | 6.07 | 27.9/28.0 | 24.6/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.49 | 5.93 | 28.0/28.2 | 25.0/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.58 | 0.42 | 0.00 | 9.38 | 29.6/29.7 | 23.8/22.9 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.071 | 0.52 | 0.48 | 0.00 | 5.99 | 22.2/32.8 | 29.5/18.5 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.065 | 0.64 | 0.36 | 0.00 | 6.02 | 33.0/22.4 | 19.6/28.6 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.49 | 0.51 | 0.49 | 5.94 | 22.6/33.0 | 29.7/19.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.223 | 0.209 | +0.043 | +0.029 | $3.90 | FUNDED_RESEARCH | $1 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 29 | 0.331 | 0.320 | +0.027 | +0.015 | $2.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (12.22 vs 0.26 bp); alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: WSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-NSHMBOURQUE22-1|yes; why: higher confidence-adjusted growth (2.44 vs 1.01 bp); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.3679): highest fidelity KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.4437): highest fidelity KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes (same contract)
- KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4126, phi -0.235)
- KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3418, phi -0.264)

portfolios: A EV +1.37 (adj +0.88) on $7.73, P(profit) 0.4816, adj growth 8.2 bp · B EV +1.17 (adj +0.76) on $6.46, P(profit) 0.4816, adj growth 7.1 bp · C EV +1.62 (adj +1.05) on $8.96, P(profit) 0.4816, adj growth 9.6 bp · R EV +0.24 (adj +0.16) on $1.00, P(profit) 0.2234, adj growth 6.0 bp

## MTL @ DAL  ·  10000 joint draws  ·  420 bet sides mapped, 0 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.601 / away 0.400

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_MTL_win | p_overtime | goals | shots DAL/MTL | DAL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DAL shot control · normal event (5-7) · decided (2+) | 0.122 | 0.64 | 0.36 | 0.00 | 5.96 | 31.4/20.3 | 17.5/27.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.55 | 0.45 | 0.00 | 6.0 | 26.4/25.9 | 22.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.46 | 5.9 | 26.7/26.0 | 22.7/23.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.46 | 5.89 | 31.6/20.8 | 17.7/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.58 | 0.42 | 0.00 | 9.28 | 28.1/27.5 | 21.8/21.6 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.068 | 0.66 | 0.34 | 0.00 | 9.21 | 32.9/21.7 | 17.0/25.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts DAL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ MIN  ·  10000 joint draws  ·  446 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.631 / away 0.369

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_NYI_win | p_overtime | goals | shots MIN/NYI | MIN/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.59 | 0.41 | 0.00 | 5.96 | 28.1/27.9 | 24.8/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.46 | 5.9 | 28.3/28.2 | 25.0/25.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.087 | 0.64 | 0.36 | 0.00 | 5.97 | 33.2/22.3 | 19.6/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.57 | 0.43 | 0.00 | 9.23 | 29.7/29.4 | 23.8/23.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.57 | 0.43 | 0.48 | 5.84 | 33.6/22.8 | 19.6/30.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.59 | 0.41 | 0.00 | 3.46 | 26.9/26.7 | 25.2/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 18 | 0.254 | 0.230 | +0.064 | +0.040 | $5.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 53 | 0.617 | 0.594 | +0.069 | +0.046 | $9.39 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Olli Maatta: 1+ goals YES | 4 | 0.063 | 0.055 | +0.020 | +0.012 | $1.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.153 | 0.141 | +0.026 | +0.014 | $1.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes; why: higher confidence-adjusted growth (22.39 vs 5.35 bp); despite a smaller raw edge (+0.064 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: NYI offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-2|no; why: higher confidence-adjusted growth (18.94 vs 5.14 bp); relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: MIN offense succeeds (4+ goals)
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT29NYIMIN-9|yes; why: higher confidence-adjusted growth (7.36 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.846 vs 0.378); alternative not eligible: confidence-adjusted EV +0.0006 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: MIN offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (22.39 vs 3.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:OFFENSE_4PLUS (p 0.3313): highest fidelity KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3716): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.4437): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4536, phi -0.244)
- KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4048, phi -0.296)
- KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3716, phi -0.108)
- KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4536, phi -0.225)

portfolios: A EV +3.40 (adj +1.70) on $16.82, P(profit) 0.4581, adj growth 15.7 bp · B EV +3.87 (adj +2.43) on $17.54, P(profit) 0.3678, adj growth 22.9 bp · C EV +4.55 (adj +2.76) on $23.98, P(profit) 0.486, adj growth 25.4 bp · R EV +0.38 (adj +0.25) on $3.00, P(profit) 0.6166, adj growth 9.6 bp

## BUF @ ANA  ·  10000 joint draws  ·  460 bet sides mapped, 24 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.439 / away 0.561

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BUF_win | p_overtime | goals | shots ANA/BUF | ANA/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.60 | 0.40 | 0.00 | 6.03 | 28.1/28.0 | 24.7/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.45 | 6.02 | 27.9/27.9 | 24.5/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.58 | 0.42 | 0.00 | 9.51 | 30.1/29.9 | 23.9/23.5 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.089 | 0.65 | 0.35 | 0.00 | 6.02 | 33.2/22.2 | 19.4/28.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.56 | 0.44 | 0.47 | 5.95 | 33.3/22.5 | 19.4/29.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.061 | 0.63 | 0.37 | 0.00 | 9.45 | 34.7/23.8 | 18.5/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 10 | 0.163 | 0.146 | +0.057 | +0.040 | $4.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 2.5 goals NO | 76 | 0.853 | 0.804 | +0.080 | +0.031 | $9.39 | FUNDED_RESEARCH | $3 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ goals NO | 63 | 0.695 | 0.676 | +0.049 | +0.030 | $8.95 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: higher confidence-adjusted growth (35.21 vs 12.22 bp); despite a smaller raw edge (+0.057 vs +0.080/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT29BUFANA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: ANA offense suppressed (<= 2 goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: higher confidence-adjusted growth (12.22 vs 11.25 bp); despite a smaller raw edge (+0.080 vs +0.082/contract); wins across more scripts (relative breadth 1.034 vs 0.516); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.088); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.157); failure: BUF wins by 2+
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-BUF3|no has the higher standalone adjusted growth (12.22 vs 8.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.157); they share one thesis budget; relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: REINFORCING (phi 0.157); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4751): highest fidelity KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5562): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3447): highest fidelity KXNHLSPREAD-26OCT29BUFANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes (same contract)
- KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3186, phi -0.168)
- KXNHLSPREAD-26OCT29BUFANA-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2359, phi -0.748)
- KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3848, phi -0.268)

portfolios: A EV +5.67 (adj +1.17) on $16.82, P(profit) 0.6326, adj growth 9.9 bp · B EV +4.03 (adj +2.46) on $22.79, P(profit) 0.673, adj growth 23.0 bp · C EV +1.92 (adj +0.92) on $26.05, P(profit) 0.8264, adj growth 9.0 bp · R EV +0.54 (adj +0.26) on $6.00, P(profit) 0.6185, adj growth 9.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT29BUFANA-ANA|yes == KXNHLGAME-26OCT29BUFANA-BUF|no

## OTT @ LAK  ·  10000 joint draws  ·  424 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.480 / away 0.520

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_OTT_win | p_overtime | goals | shots LAK/OTT | LAK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.56 | 0.44 | 0.00 | 5.95 | 27.0/27.1 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.46 | 5.85 | 26.9/27.2 | 24.0/23.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.077 | 0.48 | 0.52 | 0.00 | 5.99 | 21.6/31.8 | 28.0/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.57 | 0.43 | 0.00 | 9.14 | 28.2/28.4 | 23.0/21.7 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.48 | 0.52 | 0.48 | 5.84 | 21.5/32.2 | 28.8/18.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.066 | 0.53 | 0.47 | 0.00 | 3.43 | 25.7/25.9 | 24.2/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Scott Laughton: 1+ goals YES | 11 | 0.160 | 0.141 | +0.043 | +0.025 | $2.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.077 | 0.068 | +0.024 | +0.014 | $1.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Drake Batherson: 1+ goals NO | 70 | 0.747 | 0.733 | +0.033 | +0.018 | $6.86 | FUNDED_RESEARCH | $2 | OTT:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 58 | 0.700 | 0.612 | +0.103 | +0.015 | $3.80 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT2|no; why: higher confidence-adjusted growth (12.66 vs 1.30 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: LAK offense suppressed (<= 2 goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes has the higher standalone adjusted growth (12.66 vs 8.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.024); failure: LAK offense suppressed (<= 2 goals)
- **Drake Batherson: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (3.63 vs 2.20 bp); despite a smaller raw edge (+0.033 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.141); failure: OTT offense succeeds (4+ goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no has the higher standalone adjusted growth (3.63 vs 2.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.141); they share one thesis budget; relationships: KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.141); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:OFFENSE_4PLUS (p 0.3742): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:SUPPRESSED (p 0.4531): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS (p 0.5343): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.402, phi -0.205)
- KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.402, phi -0.146)
- KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3288, phi -0.212)
- KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.5 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3288, phi -0.259)

portfolios: A EV +2.62 (adj +0.92) on $16.82, P(profit) 0.4865, adj growth 8.5 bp · B EV +2.66 (adj +1.26) on $14.92, P(profit) 0.6465, adj growth 11.7 bp · C EV +2.34 (adj +1.19) on $17.61, P(profit) 0.5912, adj growth 10.9 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.7474, adj growth 1.9 bp

## VAN @ SJS  ·  10000 joint draws  ·  420 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.609 / away 0.392

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_VAN_win | p_overtime | goals | shots SJS/VAN | SJS/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.55 | 0.45 | 0.00 | 6.09 | 27.6/27.3 | 23.9/23.6 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.107 | 0.62 | 0.38 | 0.00 | 6.05 | 33.1/21.8 | 18.8/28.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.49 | 0.51 | 0.45 | 6.0 | 27.9/27.5 | 24.1/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.59 | 0.41 | 0.00 | 9.32 | 29.4/28.9 | 23.3/22.6 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.089 | 0.66 | 0.34 | 0.00 | 9.36 | 34.9/23.2 | 18.4/27.3 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.56 | 0.44 | 0.43 | 5.99 | 33.1/21.7 | 18.5/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 1+ goals NO | 71 | 0.809 | 0.741 | +0.085 | +0.017 | $8.79 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 19 | 0.227 | 0.214 | +0.026 | +0.013 | $1.87 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 13 | 0.158 | 0.148 | +0.020 | +0.010 | $1.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Tyler Toffoli: 1+ assists YES | 28 | 0.336 | 0.305 | +0.042 | +0.011 | $1.89 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT29VANSJ-SJ5|no; why: higher confidence-adjusted growth (3.16 vs 1.03 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT29VANSJ-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: SJS offense succeeds (4+ goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29VANSJ-SJ3|no; why: higher confidence-adjusted growth (2.42 vs 0.89 bp); despite a smaller raw edge (+0.026 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT29VANSJ-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: VAN offense suppressed (<= 2 goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (2.42 vs 1.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: VAN offense suppressed (<= 2 goals)
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29VANSJ-SJAGAUDETTE81-1|yes; why: higher confidence-adjusted growth (1.38 vs 0.01 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0007 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT29VANSJ-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3779): highest fidelity KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.4638): highest fidelity KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3271): highest fidelity KXNHLTEAMTOTAL-26OCT29VANSJ-SJ5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT29VANSJ-SJ5|no (same contract)
- KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.4 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4638, phi -0.169)
- KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4017, phi -0.212)
- KXNHLGOAL-26OCT29VANSJ-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4017, phi -0.173)
- KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3271, phi -0.253)

portfolios: A EV +1.79 (adj +0.50) on $16.82, P(profit) 0.4521, adj growth 4.7 bp · B EV +1.73 (adj +0.50) on $13.88, P(profit) 0.4899, adj growth 4.7 bp · C EV +1.25 (adj +0.41) on $13.25, P(profit) 0.382, adj growth 3.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
