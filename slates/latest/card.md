# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-29T17:49:09Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +31.03 | +10.87 | +29.45 | 0.752 | -24.28 | -37.82 | 98.88 |
| B thesis-diversified (joint) ← optimiser card | 149.31 | +28.74 | +16.33 | +25.85 | 0.724 | -26.97 | -39.02 | 153.18 |
| C best expression per thesis | 150.00 | +27.03 | +13.92 | +23.09 | 0.673 | -35.62 | -48.93 | 126.23 |
| R FUNDED research stakes | 22.00 | +2.40 | +1.32 | +1.44 | 0.598 | -7.00 | -9.34 | 0.00 |

## WPG @ TBL  ·  10000 joint draws  ·  418 bet sides mapped, 3 +EV candidates, 2 on card

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
| Charle-Edouard D'Astous: 1+ goals NO | 89 | 0.929 | 0.916 | +0.032 | +0.020 | $9.43 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ assists NO | 41 | 0.498 | 0.449 | +0.071 | +0.022 | $3.74 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.72) | EVIDENCE_MIXED | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (9.27 vs 4.33 bp); despite a smaller raw edge (+0.032 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.073); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no; why: higher confidence-adjusted growth (4.33 vs 2.34 bp); wins across more scripts (relative breadth 0.99 vs 0.58); relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.073); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.3355): highest fidelity KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no (same contract)
- KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4503, phi -0.108)
- KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 28% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4503, phi -0.307)

portfolios: A EV +2.28 (adj +0.79) on $16.91, P(profit) 0.4948, adj growth 6.8 bp · B EV +0.96 (adj +0.40) on $13.17, P(profit) 0.4718, adj growth 3.8 bp · C EV +1.12 (adj +0.35) on $6.75, P(profit) 0.4979, adj growth 3.2 bp · R EV +0.11 (adj +0.07) on $3.00, P(profit) 0.9286, adj growth 2.6 bp

## UTA @ PIT  ·  10000 joint draws  ·  400 bet sides mapped, 17 +EV candidates, 4 on card

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
| Nick Robertson: 1+ goals YES | 16 | 0.251 | 0.227 | +0.082 | +0.058 | $6.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 9 | 0.154 | 0.137 | +0.059 | +0.041 | $3.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ goals YES | 32 | 0.381 | 0.365 | +0.046 | +0.029 | $4.22 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 65 | 0.692 | 0.679 | +0.026 | +0.013 | $4.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Nick Robertson: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (49.87 vs 40.99 bp); relationships: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes has the higher standalone adjusted growth (49.87 vs 40.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes because adjusted EV is 0.7 pts higher while thesis capture is 0.53 vs 0.14 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: PIT offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29UTAPIT-UTA2|no; why: higher confidence-adjusted growth (1.70 vs 0.64 bp); despite a smaller raw edge (+0.026 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4347): highest fidelity KXNHLAST-26OCT29UTAPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes — Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes because adjusted EV is 0.7 pts higher while thesis capture is 0.53 vs 0.14 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis UTA:SUPPRESSED (p 0.3547): highest fidelity KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no (same contract)
- KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.217)
- KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.195)
- KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.267)
- KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4353, phi -0.24)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes because adjusted EV is 0.7 pts higher while thesis capture is 0.53 vs 0.14 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +8.11 (adj +2.92) on $17.14, P(profit) 0.5189, adj growth 26.9 bp · B EV +6.02 (adj +4.17) on $18.74, P(profit) 0.5311, adj growth 39.2 bp · C EV +5.65 (adj +3.93) on $18.16, P(profit) 0.2509, adj growth 35.2 bp · R EV +0.27 (adj +0.18) on $2.00, P(profit) 0.3812, adj growth 6.3 bp

## CBJ @ CAR  ·  10000 joint draws  ·  440 bet sides mapped, 19 +EV candidates, 4 on card

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
| Charlie Coyle: 1+ goals YES | 17 | 0.258 | 0.234 | +0.078 | +0.055 | $7.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.185 | 0.170 | +0.047 | +0.032 | $3.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 8 | 0.115 | 0.103 | +0.029 | +0.018 | $2.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 73 | 0.778 | 0.764 | +0.035 | +0.020 | $9.36 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (43.09 vs 18.34 bp); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT29CBJCAR-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (43.09 vs 18.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT29CBJCAR-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (43.09 vs 9.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: CBJ offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes; why: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes has the higher standalone adjusted growth (6.61 vs 4.62 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.131); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29CBJCAR-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.3293): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.2133): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29CBJCAR-CAR2|no (same contract)
- thesis CAR:SUPPRESSED (p 0.3571): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29CBJCAR-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4607, phi -0.265)
- KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4607, phi -0.225)
- KXNHLGOAL-26OCT29CBJCAR-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4607, phi -0.169)
- KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4247, phi -0.215)

portfolios: A EV +4.75 (adj +1.84) on $17.14, P(profit) 0.5376, adj growth 17.0 bp · B EV +5.48 (adj +3.71) on $22.25, P(profit) 0.4603, adj growth 34.6 bp · C EV +5.89 (adj +3.53) on $15.96, P(profit) 0.3871, adj growth 31.6 bp · R EV +0.14 (adj +0.08) on $3.00, P(profit) 0.7784, adj growth 3.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT29CBJCAR-CAR|no == KXNHLGAME-26OCT29CBJCAR-CBJ|yes

## CHI @ DET  ·  10000 joint draws  ·  426 bet sides mapped, 6 +EV candidates, 4 on card

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
| Patrick Kane: 1+ assists NO | 57 | 0.715 | 0.614 | +0.128 | +0.027 | $9.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 22 | 0.263 | 0.251 | +0.031 | +0.019 | $3.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 11 | 0.140 | 0.128 | +0.023 | +0.011 | $1.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 41 | 0.451 | 0.439 | +0.024 | +0.012 | $2.43 | FUNDED_RESEARCH | $1 | DET:OFFENSE_4PLUS | DIRECT (0.63) | EVIDENCE_STRONGER | D |
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CHIDET-CHI2|no; why: higher confidence-adjusted growth (6.59 vs 0.35 bp); alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.121); KXNHLGOAL-26OCT29CHIDET-CHIOMOORE11-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.123); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CHI offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CHIDET-CHIRDONATO8-1|yes; why: higher confidence-adjusted growth (4.50 vs 0.09 bp); alternative not eligible: confidence-adjusted EV +0.0023 below the 0.010/contract floor; relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.121); KXNHLGOAL-26OCT29CHIDET-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: CHI offense suppressed (<= 2 goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (4.50 vs 2.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.123); KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes; why: Player prop expression KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes because adjusted EV is 0.2 pts higher while thesis capture is 0.63 vs 0.24 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT29CHIDET-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.14, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:SUPPRESSED (p 0.4966): highest fidelity KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.2834): highest fidelity KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.4373): highest fidelity KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes (same contract)
- KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.5 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2834, phi -0.259)
- KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4966, phi -0.287)
- KXNHLGOAL-26OCT29CHIDET-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4966, phi -0.182)
- KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 37% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3444, phi -0.317)
- override: Player prop expression KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes because adjusted EV is 0.2 pts higher while thesis capture is 0.63 vs 0.24 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +2.32 (adj +0.69) on $17.14, P(profit) 0.5797, adj growth 6.5 bp · B EV +2.94 (adj +0.92) on $16.74, P(profit) 0.5198, adj growth 8.7 bp · C EV +4.72 (adj +1.39) on $26.74, P(profit) 0.6182, adj growth 12.7 bp · R EV +0.06 (adj +0.03) on $1.00, P(profit) 0.4508, adj growth 1.1 bp

## BOS @ STL  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.507 / away 0.493

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
| Casey Mittelstadt: 1+ goals YES | 14 | 0.179 | 0.167 | +0.030 | +0.018 | $2.38 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 24 | 0.282 | 0.271 | +0.030 | +0.018 | $2.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 29 | 0.331 | 0.319 | +0.026 | +0.015 | $2.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT29BOSSTL-9|yes; why: higher confidence-adjusted growth (5.60 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.916 vs 0.374); alternative not eligible: confidence-adjusted EV +0.0010 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: BOS offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (3.67 vs 2.23 bp); relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (3.67 vs 2.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.4127): highest fidelity KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.3665): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4158, phi -0.197)
- KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3698, phi -0.252)
- KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3698, phi -0.282)

portfolios: A EV +1.30 (adj +0.77) on $9.67, P(profit) 0.6064, adj growth 7.1 bp · B EV +1.01 (adj +0.60) on $7.54, P(profit) 0.6064, adj growth 5.6 bp · C EV +0.49 (adj +0.29) on $4.16, P(profit) 0.2825, adj growth 2.7 bp · R EV +0.20 (adj +0.12) on $1.00, P(profit) 0.1787, adj growth 4.3 bp

## WSH @ NSH  ·  10000 joint draws  ·  432 bet sides mapped, 3 +EV candidates, 3 on card

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
| Aliaksei Protas: 1+ goals YES | 18 | 0.223 | 0.210 | +0.033 | +0.020 | $2.76 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 14 | 0.171 | 0.162 | +0.023 | +0.014 | $1.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 29 | 0.331 | 0.317 | +0.027 | +0.013 | $2.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (5.47 vs 0.26 bp); alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: WSH offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (3.19 vs 1.71 bp); despite a smaller raw edge (+0.023 vs +0.027/contract); relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: NSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (3.19 vs 1.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.3679): highest fidelity KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.4437): highest fidelity KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4126, phi -0.235)
- KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3418, phi -0.197)
- KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3418, phi -0.264)

portfolios: A EV +1.25 (adj +0.71) on $9.11, P(profit) 0.5719, adj growth 6.5 bp · B EV +0.95 (adj +0.54) on $6.70, P(profit) 0.5719, adj growth 5.1 bp · C EV +1.15 (adj +0.69) on $6.98, P(profit) 0.3591, adj growth 6.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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

## NYI @ MIN  ·  10000 joint draws  ·  444 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.628 / away 0.372

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
| Brayden Schenn: 1+ goals YES | 18 | 0.246 | 0.223 | +0.056 | +0.033 | $4.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 54 | 0.617 | 0.595 | +0.059 | +0.038 | $9.43 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 11 | 0.154 | 0.141 | +0.038 | +0.024 | $2.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.162 | 0.148 | +0.035 | +0.020 | $2.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIOPALAT81-1|yes; why: higher confidence-adjusted growth (15.21 vs 11.98 bp); relationships: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT29NYIMIN-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NYI offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-2|no; why: higher confidence-adjusted growth (12.54 vs 5.99 bp); relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT29NYIMIN-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: MIN offense succeeds (4+ goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (15.21 vs 11.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: NYI offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (15.21 vs 8.03 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT29NYIMIN-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:OFFENSE_4PLUS (p 0.3313): highest fidelity KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3716): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.4437): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4536, phi -0.245)
- KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4048, phi -0.296)
- KXNHLGOAL-26OCT29NYIMIN-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4536, phi -0.199)
- KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4536, phi -0.208)

portfolios: A EV +2.35 (adj +0.88) on $17.14, P(profit) 0.4621, adj growth 8.0 bp · B EV +3.86 (adj +2.37) on $19.07, P(profit) 0.4637, adj growth 22.2 bp · C EV +4.08 (adj +2.29) on $25.66, P(profit) 0.711, adj growth 20.8 bp · R EV +0.32 (adj +0.20) on $3.00, P(profit) 0.6166, adj growth 7.5 bp

## BUF @ ANA  ·  10000 joint draws  ·  460 bet sides mapped, 25 +EV candidates, 4 on card

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
| Tim Washe: 1+ goals YES | 10 | 0.163 | 0.146 | +0.057 | +0.040 | $4.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 2.5 goals NO | 76 | 0.853 | 0.804 | +0.080 | +0.031 | $9.10 | FUNDED_RESEARCH | $3 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 1.5 goals YES | 25 | 0.345 | 0.295 | +0.082 | +0.032 | $2.30 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ goals NO | 63 | 0.695 | 0.678 | +0.049 | +0.031 | $8.05 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: higher confidence-adjusted growth (35.21 vs 12.22 bp); despite a smaller raw edge (+0.057 vs +0.080/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT29BUFANA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: ANA offense suppressed (<= 2 goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: higher confidence-adjusted growth (12.22 vs 11.25 bp); despite a smaller raw edge (+0.080 vs +0.082/contract); wins across more scripts (relative breadth 1.034 vs 0.516); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.088); KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.301); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.157); failure: BUF wins by 2+
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-BUF3|no has the higher standalone adjusted growth (12.22 vs 11.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.301); they share one thesis budget; relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: DUPLICATIVE (phi 0.301); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.17); failure: BUF wins (incl. OT/SO)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-BUF3|no has the higher standalone adjusted growth (12.22 vs 9.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.157); they share one thesis budget; relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: REINFORCING (phi 0.157); KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: REINFORCING (phi 0.17); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4751): highest fidelity KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5562): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3447): highest fidelity KXNHLSPREAD-26OCT29BUFANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes (same contract)
- KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3186, phi -0.168)
- KXNHLSPREAD-26OCT29BUFANA-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2359, phi -0.748)
- KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4438, phi -0.648)
- KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3848, phi -0.268)

portfolios: A EV +4.62 (adj +0.81) on $17.14, P(profit) 0.5814, adj growth 6.8 bp · B EV +4.47 (adj +2.58) on $23.56, P(profit) 0.673, adj growth 24.1 bp · C EV +2.11 (adj +1.01) on $28.66, P(profit) 0.8264, adj growth 9.8 bp · R EV +0.85 (adj +0.39) on $7.00, P(profit) 0.6864, adj growth 14.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT29BUFANA-ANA|yes == KXNHLGAME-26OCT29BUFANA-BUF|no

## OTT @ LAK  ·  10000 joint draws  ·  422 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.480 / away 0.520

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_OTT_win | p_overtime | goals | shots LAK/OTT | LAK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.56 | 0.44 | 0.00 | 5.95 | 27.0/27.1 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.46 | 5.85 | 26.9/27.2 | 24.0/23.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.077 | 0.48 | 0.52 | 0.00 | 6.0 | 21.6/31.8 | 28.0/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.57 | 0.43 | 0.00 | 9.15 | 28.2/28.4 | 23.0/21.7 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.48 | 0.52 | 0.47 | 5.84 | 21.5/32.2 | 28.8/18.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.066 | 0.53 | 0.47 | 0.00 | 3.43 | 25.7/25.9 | 24.2/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.074 | 0.066 | +0.021 | +0.012 | $1.30 | FUNDED_RESEARCH | $1 | LAK:WINS_BY_2PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Scott Laughton: 1+ goals YES | 12 | 0.155 | 0.141 | +0.028 | +0.014 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Ottawa wins by over 1.5 goals NO | 70 | 0.756 | 0.726 | +0.042 | +0.011 | $3.15 | FUNDED_RESEARCH | $1 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLSPREAD-26OCT29OTTLA-OTT2|no; why: higher confidence-adjusted growth (6.50 vs 1.30 bp); despite a smaller raw edge (+0.021 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT29OTTLA-OTT2|no: MOSTLY_INDEPENDENT (phi 0.089); failure: LAK offense suppressed (<= 2 goals)
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT2|no; why: higher confidence-adjusted growth (3.70 vs 1.30 bp); despite a smaller raw edge (+0.028 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT29OTTLA-OTT2|no: MOSTLY_INDEPENDENT (phi 0.132); failure: LAK offense suppressed (<= 2 goals)
- **Ottawa wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT3|no; why: alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.089); KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.132); failure: OTT wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:WINS_BY_2PLUS (p 0.3062): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT2|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.3742): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT2|no (same contract)
- thesis LAK:WINS (p 0.5343): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT2|no (same contract)
- KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.402, phi -0.132)
- KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.402, phi -0.184)
- KXNHLSPREAD-26OCT29OTTLA-OTT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2436, phi -1.0)

portfolios: A EV +1.73 (adj +0.84) on $11.46, P(profit) 0.2173, adj growth 7.5 bp · B EV +1.04 (adj +0.52) on $6.05, P(profit) 0.2173, adj growth 4.9 bp · C EV +0.43 (adj +0.11) on $7.42, P(profit) 0.7564, adj growth 1.0 bp · R EV +0.45 (adj +0.25) on $2.00, P(profit) 0.0743, adj growth 8.0 bp

## VAN @ SJS  ·  10000 joint draws  ·  418 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.609 / away 0.392

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_VAN_win | p_overtime | goals | shots SJS/VAN | SJS/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.57 | 0.43 | 0.00 | 6.04 | 27.6/27.2 | 23.9/23.7 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.105 | 0.63 | 0.37 | 0.00 | 6.11 | 33.0/21.6 | 18.7/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.57 | 0.43 | 0.00 | 9.45 | 29.6/28.8 | 23.0/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.47 | 6.01 | 27.9/27.5 | 24.1/24.6 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.55 | 0.45 | 0.44 | 5.94 | 33.3/22.2 | 19.1/30.0 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.084 | 0.65 | 0.35 | 0.00 | 9.38 | 34.4/22.9 | 17.9/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 1+ goals NO | 71 | 0.806 | 0.740 | +0.082 | +0.016 | $7.95 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 19 | 0.228 | 0.215 | +0.027 | +0.014 | $1.99 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 13 | 0.160 | 0.150 | +0.022 | +0.012 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 61 | 0.720 | 0.639 | +0.093 | +0.012 | $4.03 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (2.80 vs 1.36 bp); despite a smaller raw edge (+0.082 vs +0.093/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT29VANSJ-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: SJS offense succeeds (4+ goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29VANSJ-SJ3|no; why: higher confidence-adjusted growth (2.65 vs 1.11 bp); despite a smaller raw edge (+0.027 vs +0.039/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT29VANSJ-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: VAN offense suppressed (<= 2 goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (2.65 vs 2.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.021); they share one thesis budget; relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.026); failure: VAN offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29VANSJ-SJ3|no; why: higher confidence-adjusted growth (1.36 vs 1.11 bp); alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT29VANSJ-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3824): highest fidelity KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3257): highest fidelity KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no (same contract)
- KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.1 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4611, phi -0.199)
- KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4045, phi -0.231)
- KXNHLGOAL-26OCT29VANSJ-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4045, phi -0.192)
- KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.5 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4611, phi -0.248)

portfolios: A EV +2.31 (adj +0.62) on $17.14, P(profit) 0.7089, adj growth 5.7 bp · B EV +2.01 (adj +0.52) on $15.49, P(profit) 0.7089, adj growth 4.9 bp · C EV +1.38 (adj +0.33) on $9.51, P(profit) 0.7835, adj growth 3.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
