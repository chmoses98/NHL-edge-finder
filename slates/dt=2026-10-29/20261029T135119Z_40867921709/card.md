# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-29T13:51:19Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +26.26 | +9.50 | +25.17 | 0.728 | -24.98 | -39.05 | 86.80 |
| B thesis-diversified (joint) ← optimiser card | 149.04 | +23.89 | +13.44 | +21.54 | 0.692 | -30.04 | -42.42 | 124.83 |
| C best expression per thesis | 150.01 | +24.58 | +14.04 | +21.95 | 0.671 | -38.57 | -53.66 | 128.27 |
| R FUNDED research stakes | 28.00 | +2.87 | +1.55 | +2.44 | 0.631 | -6.84 | -9.37 | 0.00 |

## WPG @ TBL  ·  10000 joint draws  ·  376 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WPG_win | p_overtime | goals | shots TBL/WPG | TBL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.69 | 0.31 | 0.00 | 6.0 | 27.1/26.6 | 23.9/22.8 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.119 | 0.73 | 0.27 | 0.00 | 5.98 | 32.3/21.0 | 18.5/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.52 | 0.48 | 0.47 | 5.87 | 27.0/26.7 | 23.4/23.7 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.57 | 0.43 | 0.48 | 5.89 | 32.7/21.2 | 18.1/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.67 | 0.33 | 0.00 | 9.12 | 28.8/28.1 | 23.2/21.8 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.067 | 0.75 | 0.25 | 0.00 | 9.2 | 34.4/22.4 | 18.2/26.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charle-Edouard D'Astous: 1+ goals NO | 89 | 0.919 | 0.909 | +0.022 | +0.012 | $11.11 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 11 | 0.138 | 0.129 | +0.021 | +0.012 | $1.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 25 | 0.288 | 0.277 | +0.025 | +0.014 | $2.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Anthony Cirelli: 1+ goals YES | 24 | 0.280 | 0.265 | +0.027 | +0.012 | $2.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (3.59 vs 1.69 bp); despite a smaller raw edge (+0.022 vs +0.088/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: TBL offense succeeds (4+ goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (2.96 vs 2.17 bp); despite a smaller raw edge (+0.021 vs +0.025/contract); relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29WPGTB-TB2|no; why: higher confidence-adjusted growth (2.17 vs 1.61 bp); despite a smaller raw edge (+0.025 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.952 vs 0.836); relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: WPG offense suppressed (<= 2 goals)
- **Anthony Cirelli: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes; why: higher confidence-adjusted growth (1.71 vs 1.57 bp); relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: TBL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.2621): highest fidelity KXNHLSPREAD-26OCT29WPGTB-TB2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:OFFENSE_4PLUS (p 0.4474): highest fidelity KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.3387): highest fidelity KXNHLSPREAD-26OCT29WPGTB-TB2|no [DIRECT], best adjusted EV KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4474, phi -0.114)
- KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.5209, phi -0.193)
- KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.5209, phi -0.282)
- KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3387, phi -0.238)

portfolios: A EV +2.48 (adj +0.64) on $18.07, P(profit) 0.5749, adj growth 5.7 bp · B EV +1.07 (adj +0.57) on $17.61, P(profit) 0.5239, adj growth 5.3 bp · C EV +1.83 (adj +0.54) on $14.30, P(profit) 0.5749, adj growth 4.9 bp · R EV +0.07 (adj +0.04) on $3.00, P(profit) 0.9188, adj growth 1.6 bp

## UTA @ PIT  ·  10000 joint draws  ·  398 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_UTA_win | p_overtime | goals | shots PIT/UTA | PIT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.49 | 0.51 | 0.00 | 6.02 | 27.2/27.0 | 23.6/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.51 | 0.49 | 0.00 | 9.47 | 28.9/28.9 | 22.5/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.47 | 6.01 | 27.1/27.1 | 23.8/23.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.071 | 0.61 | 0.39 | 0.00 | 6.01 | 31.9/21.6 | 18.6/27.7 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.065 | 0.44 | 0.56 | 0.00 | 6.07 | 21.6/31.8 | 27.7/18.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.45 | 0.55 | 0.47 | 5.96 | 21.7/32.1 | 28.8/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Blake Lizotte: 1+ goals YES | 10 | 0.163 | 0.140 | +0.057 | +0.034 | $4.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Declan Carlile: 1+ goals YES | 6 | 0.097 | 0.086 | +0.033 | +0.022 | $2.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ goals YES | 32 | 0.386 | 0.368 | +0.051 | +0.033 | $6.71 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 32 | 0.434 | 0.357 | +0.099 | +0.021 | $4.05 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.60) | EVIDENCE_STRONGER | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (25.29 vs 4.51 bp); despite a smaller raw edge (+0.057 vs +0.099/contract); relationships: KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: PIT offense suppressed (<= 2 goals)
- **Declan Carlile: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes; why: higher confidence-adjusted growth (17.67 vs 11.36 bp); despite a smaller raw edge (+0.033 vs +0.035/contract); wins across more scripts (relative breadth 0.88 vs 0.73); relationships: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITEKARLSSON65-1|yes because adjusted EV is 0.1 pts higher while thesis capture is 0.53 vs 0.29 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.60 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:WINS_BY_2PLUS (p 0.2966): highest fidelity KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.4351): highest fidelity KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes — Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITEKARLSSON65-1|yes because adjusted EV is 0.1 pts higher while thesis capture is 0.53 vs 0.29 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis UTA:SUPPRESSED (p 0.3568): highest fidelity KXNHLAST-26OCT29UTAPIT-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3475, phi -0.177)
- KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3475, phi -0.136)
- KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3475, phi -0.265)
- KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 40% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.9 pts; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3475, phi -0.308)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITEKARLSSON65-1|yes because adjusted EV is 0.1 pts higher while thesis capture is 0.53 vs 0.29 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.60 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +7.63 (adj +1.71) on $18.07, P(profit) 0.6064, adj growth 15.0 bp · B EV +6.01 (adj +3.30) on $17.97, P(profit) 0.5357, adj growth 30.3 bp · C EV +5.21 (adj +3.07) on $21.44, P(profit) 0.2526, adj growth 27.9 bp · R EV +0.30 (adj +0.20) on $2.00, P(profit) 0.386, adj growth 7.2 bp

## CBJ @ CAR  ·  10000 joint draws  ·  422 bet sides mapped, 24 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CBJ_win | p_overtime | goals | shots CAR/CBJ | CAR/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.153 | 0.66 | 0.34 | 0.00 | 6.0 | 33.6/21.2 | 18.4/29.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.127 | 0.54 | 0.46 | 0.47 | 5.91 | 33.9/21.5 | 18.3/30.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.61 | 0.39 | 0.00 | 6.06 | 27.7/26.9 | 23.9/23.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.094 | 0.68 | 0.32 | 0.00 | 9.18 | 35.2/22.5 | 17.9/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.51 | 0.49 | 0.48 | 5.95 | 27.8/26.9 | 23.5/24.4 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.072 | 0.62 | 0.38 | 0.00 | 3.47 | 32.0/19.9 | 18.4/29.8 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 17 | 0.253 | 0.231 | +0.073 | +0.051 | $6.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.183 | 0.169 | +0.046 | +0.031 | $3.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 72 | 0.772 | 0.758 | +0.038 | +0.024 | $8.78 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 66 | 0.716 | 0.701 | +0.041 | +0.025 | $7.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (37.34 vs 17.25 bp); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (37.34 vs 17.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: CBJ offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no; why: Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSGOSTISBEHERE4-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.89 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: CAR offense succeeds (4+ goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no has the higher standalone adjusted growth (6.51 vs 6.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.3206): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.2167): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.3455): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR5|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no — Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSGOSTISBEHERE4-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.89 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4608, phi -0.243)
- KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4608, phi -0.232)
- KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4423, phi -0.216)
- KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4423, phi -0.212)
- override: Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSGOSTISBEHERE4-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.89 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.91 (adj +1.65) on $18.07, P(profit) 0.5728, adj growth 15.4 bp · B EV +4.63 (adj +3.14) on $26.46, P(profit) 0.3805, adj growth 29.4 bp · C EV +6.44 (adj +4.14) on $33.62, P(profit) 0.3885, adj growth 37.9 bp · R EV +0.16 (adj +0.10) on $3.00, P(profit) 0.7725, adj growth 3.7 bp

## CHI @ DET  ·  10000 joint draws  ·  420 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_CHI_win | p_overtime | goals | shots DET/CHI | DET/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.145 | 0.69 | 0.31 | 0.00 | 6.03 | 33.2/21.0 | 18.4/28.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.55 | 0.45 | 0.47 | 5.81 | 33.1/21.2 | 18.1/29.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.101 | 0.66 | 0.34 | 0.00 | 6.06 | 27.5/26.8 | 23.9/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.53 | 0.47 | 0.47 | 5.92 | 27.7/27.0 | 23.7/24.2 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.089 | 0.71 | 0.29 | 0.00 | 9.11 | 34.9/22.5 | 18.1/27.0 | even strength |
| DET shot control · low event (<=4) · decided (2+) | 0.072 | 0.68 | 0.32 | 0.00 | 3.47 | 31.8/19.7 | 18.5/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Roman Kantserov: 1+ goals NO | 75 | 0.802 | 0.788 | +0.039 | +0.025 | $9.00 | FUNDED_RESEARCH | $3 | CHI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 58 | 0.708 | 0.618 | +0.111 | +0.021 | $4.86 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Connor Bedard: 1+ assists NO | 57 | 0.648 | 0.604 | +0.061 | +0.017 | $2.80 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no; why: higher confidence-adjusted growth (7.54 vs 4.07 bp); despite a smaller raw edge (+0.039 vs +0.111/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: REINFORCING (phi 0.197); KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: REINFORCING (phi 0.258); failure: CHI offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no has the higher standalone adjusted growth (7.54 vs 4.07 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.197); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no: REINFORCING (phi 0.197); KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.126); failure: CHI offense succeeds (4+ goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no has the higher standalone adjusted growth (7.54 vs 2.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.258); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no: REINFORCING (phi 0.258); KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.126); failure: CHI offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.15, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:SUPPRESSED (p 0.5013): highest fidelity KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no (same contract)
- KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2898, phi -0.195)
- KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.8 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2898, phi -0.255)
- KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2898, phi -0.267)

portfolios: A EV +2.05 (adj +0.58) on $18.07, P(profit) 0.6114, adj growth 5.4 bp · B EV +1.65 (adj +0.55) on $16.67, P(profit) 0.6035, adj growth 5.2 bp · C EV +0.69 (adj +0.44) on $13.45, P(profit) 0.8023, adj growth 4.1 bp · R EV +0.15 (adj +0.10) on $3.00, P(profit) 0.8023, adj growth 3.7 bp

## BOS @ STL  ·  10000 joint draws  ·  422 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_BOS_win | p_overtime | goals | shots STL/BOS | STL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.53 | 0.47 | 0.00 | 6.05 | 27.4/27.2 | 23.8/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.47 | 5.97 | 27.2/27.1 | 23.8/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.54 | 0.46 | 0.00 | 9.31 | 28.9/28.6 | 22.9/22.6 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.088 | 0.62 | 0.38 | 0.00 | 5.98 | 32.3/21.6 | 18.7/27.9 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.51 | 0.49 | 0.45 | 5.9 | 32.7/21.7 | 18.5/29.4 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.064 | 0.64 | 0.36 | 0.00 | 9.2 | 33.9/22.9 | 18.1/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 24 | 0.283 | 0.271 | +0.031 | +0.019 | $3.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 64 | 0.681 | 0.669 | +0.025 | +0.013 | $5.40 | FUNDED_RESEARCH | $2 | BOS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT29BOSSTL-8|yes; why: higher confidence-adjusted growth (3.99 vs 0.02 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.881 vs 0.34); alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29BOSSTL-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: STL offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (1.70 vs 0.55 bp); despite a smaller raw edge (+0.025 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.4174): highest fidelity KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.4059): highest fidelity KXNHLGOAL-26OCT29BOSSTL-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29BOSSTL-BOSDPASTRNAK88-1|no (same contract)
- KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.369, phi -0.258)
- KXNHLGOAL-26OCT29BOSSTL-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3722, phi -0.248)

portfolios: A EV +0.70 (adj +0.40) on $10.20, P(profit) 0.2835, adj growth 3.7 bp · B EV +0.61 (adj +0.36) on $8.74, P(profit) 0.2835, adj growth 3.3 bp · C EV +0.74 (adj +0.43) on $10.58, P(profit) 0.2835, adj growth 3.9 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.6808, adj growth 1.4 bp

## WSH @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_WSH_win | p_overtime | goals | shots NSH/WSH | NSH/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.56 | 0.44 | 0.00 | 6.03 | 28.0/28.0 | 24.6/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.54 | 0.46 | 0.47 | 5.92 | 27.8/27.9 | 24.5/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.56 | 0.44 | 0.00 | 9.31 | 29.2/29.3 | 23.7/22.5 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.069 | 0.52 | 0.48 | 0.00 | 5.97 | 22.6/33.2 | 29.5/19.0 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.066 | 0.59 | 0.41 | 0.00 | 6.01 | 32.8/22.6 | 19.7/29.0 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.49 | 0.51 | 0.49 | 5.9 | 22.5/33.3 | 29.9/19.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 16 | 0.227 | 0.209 | +0.057 | +0.039 | $6.09 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 29 | 0.331 | 0.320 | +0.027 | +0.015 | $3.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT29WSHNSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (23.58 vs 1.10 bp); despite a smaller raw edge (+0.057 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: WSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29WSHNSH-WSH3|no; why: higher confidence-adjusted growth (2.41 vs 0.35 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0049 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.371): highest fidelity KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.4209): highest fidelity KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes (same contract)
- KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4132, phi -0.243)
- KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3649, phi -0.266)

portfolios: A EV +2.42 (adj +1.62) on $9.72, P(profit) 0.4837, adj growth 14.9 bp · B EV +2.32 (adj +1.57) on $9.09, P(profit) 0.4837, adj growth 14.4 bp · C EV +2.81 (adj +1.89) on $11.00, P(profit) 0.4837, adj growth 17.1 bp · R EV +0.68 (adj +0.46) on $2.00, P(profit) 0.2267, adj growth 16.7 bp

## MTL @ DAL  ·  10000 joint draws  ·  412 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_MTL_win | p_overtime | goals | shots DAL/MTL | DAL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DAL shot control · normal event (5-7) · decided (2+) | 0.117 | 0.66 | 0.34 | 0.00 | 5.98 | 31.5/20.4 | 17.8/26.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.53 | 0.47 | 0.00 | 5.99 | 26.5/25.9 | 22.7/22.9 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.48 | 5.86 | 31.5/20.7 | 17.5/28.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.52 | 0.48 | 0.48 | 5.86 | 26.8/26.3 | 23.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.57 | 0.43 | 0.00 | 9.18 | 27.9/27.3 | 21.8/21.6 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.068 | 0.66 | 0.34 | 0.00 | 9.19 | 33.3/21.9 | 17.3/25.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts DAL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, DAL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ MIN  ·  10000 joint draws  ·  400 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_NYI_win | p_overtime | goals | shots MIN/NYI | MIN/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.59 | 0.41 | 0.00 | 6.01 | 28.2/28.0 | 24.7/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.54 | 0.46 | 0.48 | 5.9 | 28.0/28.0 | 24.8/24.7 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.088 | 0.64 | 0.36 | 0.00 | 5.94 | 33.4/22.5 | 19.6/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.62 | 0.38 | 0.00 | 9.2 | 29.9/29.7 | 24.3/23.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.54 | 0.46 | 0.45 | 5.88 | 33.5/22.5 | 19.2/30.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.58 | 0.42 | 0.00 | 3.46 | 27.3/27.2 | 25.6/25.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kirill Kaprizov: 1+ goals NO | 52 | 0.606 | 0.583 | +0.068 | +0.046 | $11.11 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 18 | 0.244 | 0.225 | +0.053 | +0.035 | $5.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Olli Maatta: 1+ goals YES | 4 | 0.064 | 0.055 | +0.021 | +0.013 | $1.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.159 | 0.147 | +0.032 | +0.020 | $2.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no; why: higher confidence-adjusted growth (18.35 vs 2.21 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.989 vs 0.883); relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MIN offense succeeds (4+ goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes; why: higher confidence-adjusted growth (17.12 vs 3.15 bp); despite a smaller raw edge (+0.053 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NYI offense suppressed (<= 2 goals)
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT29NYIMIN-2|yes; why: higher confidence-adjusted growth (8.11 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: MIN offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (17.12 vs 7.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.3629): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:OFFENSE_4PLUS (p 0.3232): highest fidelity KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4447): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29NYIMIN-MIN2|no (same contract)
- KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4187, phi -0.294)
- KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4527, phi -0.244)
- KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3629, phi -0.1)
- KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4527, phi -0.197)

portfolios: A EV +2.67 (adj +1.42) on $18.07, P(profit) 0.4732, adj growth 13.2 bp · B EV +4.45 (adj +2.86) on $21.07, P(profit) 0.4059, adj growth 26.6 bp · C EV +3.59 (adj +2.37) on $20.15, P(profit) 0.7006, adj growth 21.8 bp · R EV +0.38 (adj +0.25) on $3.00, P(profit) 0.6058, adj growth 9.6 bp

## BUF @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BUF_win | p_overtime | goals | shots ANA/BUF | ANA/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.58 | 0.42 | 0.00 | 6.06 | 28.2/28.2 | 25.1/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.53 | 0.47 | 0.46 | 5.99 | 28.1/28.2 | 24.8/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.60 | 0.40 | 0.00 | 9.44 | 29.8/29.7 | 23.8/22.8 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.081 | 0.64 | 0.36 | 0.00 | 6.01 | 33.1/22.1 | 19.3/28.7 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.51 | 0.49 | 0.47 | 6.01 | 33.4/22.5 | 19.3/30.0 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.066 | 0.67 | 0.33 | 0.00 | 9.37 | 35.1/23.7 | 18.7/27.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim wins by over 1.5 goals YES | 25 | 0.344 | 0.294 | +0.081 | +0.031 | $2.39 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 2.5 goals NO | 77 | 0.858 | 0.809 | +0.075 | +0.026 | $9.38 | FUNDED_RESEARCH | $3 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 1.5 goals NO | 67 | 0.763 | 0.714 | +0.077 | +0.028 | $3.95 | FUNDED_RESEARCH | $1 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: higher confidence-adjusted growth (10.97 vs 9.12 bp); relationships: KXNHLSPREAD-26OCT29BUFANA-BUF3|no: REINFORCING (phi 0.295); KXNHLSPREAD-26OCT29BUFANA-BUF2|no: DUPLICATIVE (phi 0.404); failure: BUF wins (incl. OT/SO)
- **Buffalo wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (10.97 vs 9.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.295); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: REINFORCING (phi 0.295); KXNHLSPREAD-26OCT29BUFANA-BUF2|no: DUPLICATIVE (phi 0.73); failure: BUF wins by 2+
- **Buffalo wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: Broad expression KXNHLSPREAD-26OCT29BUFANA-BUF2|no selected over broad KXNHLTEAMTOTAL-26OCT29BUFANA-BUF6|no because adjusted EV is 1.8 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.404); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: DUPLICATIVE (phi 0.73); failure: BUF wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:WINS_BY_2PLUS (p 0.3439): highest fidelity KXNHLSPREAD-26OCT29BUFANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes (same contract)
- thesis ANA:WINS (p 0.557): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — Broad expression KXNHLSPREAD-26OCT29BUFANA-BUF2|no selected over broad KXNHLTEAMTOTAL-26OCT29BUFANA-BUF6|no because adjusted EV is 1.8 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis BUF:SUPPRESSED (p 0.4054): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.443, phi -0.646)
- KXNHLSPREAD-26OCT29BUFANA-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2373, phi -0.73)
- KXNHLSPREAD-26OCT29BUFANA-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2373, phi -1.0)
- override: Broad expression KXNHLSPREAD-26OCT29BUFANA-BUF2|no selected over broad KXNHLTEAMTOTAL-26OCT29BUFANA-BUF6|no because adjusted EV is 1.8 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.93 (adj +1.06) on $18.07, P(profit) 0.6022, adj growth 9.7 bp · B EV +2.08 (adj +0.77) on $15.72, P(profit) 0.7627, adj growth 7.3 bp · C EV +1.98 (adj +0.77) on $6.45, P(profit) 0.3439, adj growth 7.0 bp · R EV +0.71 (adj +0.26) on $5.00, P(profit) 0.7627, adj growth 9.8 bp

## OTT @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_OTT_win | p_overtime | goals | shots LAK/OTT | LAK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.58 | 0.42 | 0.00 | 6.04 | 27.0/27.1 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.45 | 5.91 | 26.9/27.0 | 23.7/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.57 | 0.43 | 0.00 | 9.23 | 28.1/28.4 | 22.7/21.7 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.074 | 0.53 | 0.47 | 0.00 | 5.96 | 21.5/32.3 | 28.8/18.1 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.52 | 0.48 | 0.48 | 2.81 | 25.4/25.6 | 24.1/23.9 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.49 | 0.51 | 0.46 | 5.85 | 21.7/32.0 | 28.7/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ottawa wins by over 1.5 goals NO | 70 | 0.762 | 0.729 | +0.047 | +0.014 | $7.27 | FUNDED_RESEARCH | $2 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ottawa wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT3|no; why: higher confidence-adjusted growth (2.05 vs 0.17 bp); alternative not eligible: confidence-adjusted EV +0.0033 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: OTT wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.07.
- thesis LAK:WINS (p 0.5456): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT2|no (same contract)
- KXNHLSPREAD-26OCT29OTTLA-OTT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.238, phi -1.0)

portfolios: A EV +0.48 (adj +0.14) on $7.23, P(profit) 0.762, adj growth 1.3 bp · B EV +0.48 (adj +0.14) on $7.27, P(profit) 0.762, adj growth 1.3 bp · C EV +0.58 (adj +0.17) on $8.80, P(profit) 0.762, adj growth 1.6 bp · R EV +0.13 (adj +0.04) on $2.00, P(profit) 0.762, adj growth 1.4 bp

## VAN @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_VAN_win | p_overtime | goals | shots SJS/VAN | SJS/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.59 | 0.41 | 0.00 | 6.05 | 27.6/27.1 | 23.9/23.8 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.107 | 0.67 | 0.33 | 0.00 | 6.02 | 32.9/21.6 | 18.9/28.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.51 | 0.49 | 0.47 | 5.91 | 28.0/27.6 | 24.2/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.56 | 0.44 | 0.00 | 9.43 | 29.4/28.9 | 23.2/22.7 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.54 | 0.46 | 0.47 | 5.94 | 33.4/22.0 | 18.8/30.1 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.080 | 0.64 | 0.36 | 0.00 | 9.24 | 34.7/23.1 | 18.2/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| San Jose wins by over 2.5 goals NO | 71 | 0.774 | 0.740 | +0.050 | +0.015 | $8.44 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **San Jose wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29VANSJ-SJ2|no; why: higher confidence-adjusted growth (2.59 vs 1.05 bp); wins across more scripts (relative breadth 1.023 vs 0.92); relationships: only recommended bet in this game; failure: SJS wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS (p 0.4388): highest fidelity KXNHLSPREAD-26OCT29VANSJ-SJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29VANSJ-SJ3|no (same contract)
- KXNHLSPREAD-26OCT29VANSJ-SJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis SJS:WINS_BY_2PLUS (p 0.3401, phi -0.752)

portfolios: A EV +1.00 (adj +0.28) on $14.45, P(profit) 0.6599, adj growth 2.4 bp · B EV +0.58 (adj +0.18) on $8.44, P(profit) 0.7745, adj growth 1.7 bp · C EV +0.71 (adj +0.22) on $10.22, P(profit) 0.7745, adj growth 2.0 bp · R EV +0.21 (adj +0.06) on $3.00, P(profit) 0.7745, adj growth 2.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
