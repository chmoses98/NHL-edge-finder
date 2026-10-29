# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-29T12:51:18Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +27.35 | +10.31 | +25.12 | 0.720 | -28.83 | -41.28 | 93.54 |
| B thesis-diversified (joint) ← optimiser card | 149.14 | +25.27 | +13.84 | +22.26 | 0.690 | -31.21 | -44.53 | 127.70 |
| C best expression per thesis | 149.99 | +26.86 | +15.63 | +22.35 | 0.652 | -47.06 | -64.10 | 138.63 |
| R FUNDED research stakes | 27.00 | +3.34 | +1.79 | +2.62 | 0.607 | -8.53 | -11.11 | 0.00 |

## WPG @ TBL  ·  10000 joint draws  ·  376 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WPG_win | p_overtime | goals | shots TBL/WPG | TBL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.69 | 0.31 | 0.00 | 6.03 | 27.0/26.5 | 23.7/22.7 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.118 | 0.73 | 0.27 | 0.00 | 5.98 | 32.4/21.1 | 18.7/27.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.53 | 0.47 | 0.45 | 5.88 | 27.3/26.8 | 23.5/24.0 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.57 | 0.43 | 0.47 | 5.81 | 32.6/21.3 | 18.1/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.69 | 0.31 | 0.00 | 9.27 | 28.7/28.2 | 23.1/21.6 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.071 | 0.75 | 0.25 | 0.00 | 9.21 | 34.2/22.2 | 18.0/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mark Scheifele: 1+ goals YES | 25 | 0.296 | 0.282 | +0.033 | +0.019 | $3.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Charle-Edouard D'Astous: 1+ goals NO | 89 | 0.919 | 0.909 | +0.022 | +0.013 | $11.34 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Ilya Mikheyev: 1+ goals YES | 17 | 0.206 | 0.192 | +0.026 | +0.012 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Anthony Cirelli: 1+ goals YES | 24 | 0.281 | 0.265 | +0.028 | +0.012 | $2.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29WPGTB-TB2|no; why: higher confidence-adjusted growth (4.06 vs 1.15 bp); despite a smaller raw edge (+0.033 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense suppressed (<= 2 goals)
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29WPGTB-TB2|no; why: higher confidence-adjusted growth (3.86 vs 1.15 bp); despite a smaller raw edge (+0.023 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.006 vs 0.844); relationships: KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: TBL offense succeeds (4+ goals)
- **Ilya Mikheyev: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes; why: higher confidence-adjusted growth (2.14 vs 1.59 bp); despite a smaller raw edge (+0.026 vs +0.028/contract); relationships: KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: TBL offense suppressed (<= 2 goals)
- **Anthony Cirelli: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes has the higher standalone adjusted growth (2.14 vs 1.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: TBL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.2705): highest fidelity KXNHLSPREAD-26OCT29WPGTB-TB2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:OFFENSE_4PLUS (p 0.4491): highest fidelity KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.3364): highest fidelity KXNHLSPREAD-26OCT29WPGTB-TB2|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT29WPGTB-TB2|no (same contract)
- KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.5189, phi -0.281)
- KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4491, phi -0.121)
- KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3364, phi -0.203)
- KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3364, phi -0.236)

portfolios: A EV +1.97 (adj +0.82) on $18.26, P(profit) 0.4206, adj growth 7.4 bp · B EV +1.25 (adj +0.65) on $18.96, P(profit) 0.5633, adj growth 6.0 bp · C EV +1.50 (adj +0.67) on $13.33, P(profit) 0.4418, adj growth 6.0 bp · R EV +0.08 (adj +0.04) on $3.00, P(profit) 0.9194, adj growth 1.6 bp

## UTA @ PIT  ·  10000 joint draws  ·  398 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_UTA_win | p_overtime | goals | shots PIT/UTA | PIT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.53 | 0.47 | 0.00 | 6.1 | 27.1/27.1 | 23.6/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.112 | 0.51 | 0.49 | 0.00 | 9.55 | 29.0/29.0 | 22.8/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.49 | 5.97 | 27.4/27.4 | 24.0/24.0 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.070 | 0.61 | 0.39 | 0.00 | 6.09 | 31.9/21.5 | 18.5/27.7 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.068 | 0.39 | 0.61 | 0.00 | 6.02 | 21.7/31.9 | 27.7/18.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.47 | 0.53 | 0.48 | 5.99 | 21.8/32.2 | 28.7/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Rickard Rakell: 2+ goals YES | 7 | 0.116 | 0.098 | +0.041 | +0.024 | $2.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Declan Carlile: 1+ goals YES | 6 | 0.099 | 0.084 | +0.035 | +0.020 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 32 | 0.447 | 0.361 | +0.112 | +0.026 | $2.56 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.61) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ goals YES | 33 | 0.383 | 0.367 | +0.038 | +0.022 | $4.62 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
- **Rickard Rakell: 2+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (16.89 vs 11.66 bp); despite a smaller raw edge (+0.041 vs +0.045/contract); relationships: KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: DUPLICATIVE (phi 0.403); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: PIT offense suppressed (<= 2 goals)
- **Declan Carlile: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes has the higher standalone adjusted growth (16.89 vs 14.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes because adjusted EV differs by only 0.0 pts while thesis capture is 0.61 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes: DUPLICATIVE (phi 0.403); KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.53 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4394): highest fidelity KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3574): highest fidelity KXNHLAST-26OCT29UTAPIT-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3425, phi -0.22)
- KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3425, phi -0.141)
- KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 39% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.2 pts; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3425, phi -0.296)
- KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3425, phi -0.257)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes because adjusted EV differs by only 0.0 pts while thesis capture is 0.61 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.53 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +8.11 (adj +1.62) on $18.78, P(profit) 0.6104, adj growth 13.9 bp · B EV +4.17 (adj +2.11) on $12.30, P(profit) 0.5085, adj growth 19.3 bp · C EV +3.59 (adj +2.09) on $21.03, P(profit) 0.7293, adj growth 18.5 bp · R EV +0.22 (adj +0.13) on $2.00, P(profit) 0.3833, adj growth 4.5 bp

## CBJ @ CAR  ·  10000 joint draws  ·  422 bet sides mapped, 19 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CBJ_win | p_overtime | goals | shots CAR/CBJ | CAR/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.152 | 0.68 | 0.32 | 0.00 | 6.04 | 33.6/21.2 | 18.5/28.8 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.127 | 0.55 | 0.45 | 0.45 | 5.91 | 33.9/21.2 | 18.1/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.60 | 0.40 | 0.00 | 6.01 | 27.7/26.8 | 23.6/23.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.097 | 0.68 | 0.32 | 0.00 | 9.18 | 35.3/22.4 | 17.8/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.52 | 0.48 | 0.46 | 5.98 | 27.8/27.1 | 23.8/24.5 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.069 | 0.63 | 0.37 | 0.00 | 3.45 | 32.5/20.1 | 18.7/30.3 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 17 | 0.250 | 0.229 | +0.070 | +0.049 | $7.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.185 | 0.170 | +0.048 | +0.032 | $4.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 67 | 0.758 | 0.712 | +0.073 | +0.026 | $5.69 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 66 | 0.716 | 0.699 | +0.040 | +0.024 | $9.41 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (34.25 vs 18.86 bp); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLSPREAD-26OCT29CBJCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.14); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (34.25 vs 18.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.019); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLSPREAD-26OCT29CBJCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR5|no; why: Broad expression KXNHLSPREAD-26OCT29CBJCAR-CAR3|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSGOSTISBEHERE4-1|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.14); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.147); failure: CAR wins by 2+
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29CBJCAR-CAR3|no has the higher standalone adjusted growth (7.04 vs 5.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.147); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLSPREAD-26OCT29CBJCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.147); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.3173): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.2117): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4248): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29CBJCAR-CAR3|no (same contract)
- KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4642, phi -0.256)
- KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4642, phi -0.237)
- KXNHLSPREAD-26OCT29CBJCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3635, phi -0.747)
- KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.452, phi -0.215)
- override: Broad expression KXNHLSPREAD-26OCT29CBJCAR-CAR3|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSGOSTISBEHERE4-1|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.65 (adj +1.78) on $18.78, P(profit) 0.5674, adj growth 16.7 bp · B EV +5.57 (adj +3.59) on $26.96, P(profit) 0.3856, adj growth 33.1 bp · C EV +7.58 (adj +4.86) on $28.03, P(profit) 0.3856, adj growth 42.9 bp · R EV +0.39 (adj +0.18) on $5.00, P(profit) 0.5711, adj growth 6.7 bp

## CHI @ DET  ·  10000 joint draws  ·  420 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_CHI_win | p_overtime | goals | shots DET/CHI | DET/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.139 | 0.69 | 0.31 | 0.00 | 6.0 | 33.1/21.1 | 18.6/28.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.55 | 0.45 | 0.50 | 5.91 | 33.6/21.6 | 18.5/30.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.65 | 0.35 | 0.00 | 6.02 | 27.4/26.7 | 23.8/23.3 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.090 | 0.72 | 0.28 | 0.00 | 9.19 | 34.6/22.2 | 17.8/26.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.52 | 0.48 | 0.50 | 5.9 | 27.5/26.9 | 23.5/24.2 | even strength |
| DET shot control · low event (<=4) · decided (2+) | 0.070 | 0.66 | 0.34 | 0.00 | 3.47 | 31.8/19.8 | 18.4/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Roman Kantserov: 1+ goals NO | 75 | 0.805 | 0.788 | +0.042 | +0.025 | $9.63 | FUNDED_RESEARCH | $3 | CHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ assists NO | 57 | 0.650 | 0.605 | +0.062 | +0.018 | $3.50 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Patrick Kane: 1+ assists NO | 58 | 0.696 | 0.614 | +0.098 | +0.017 | $3.88 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (7.39 vs 2.83 bp); despite a smaller raw edge (+0.042 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: REINFORCING (phi 0.242); KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: REINFORCING (phi 0.192); failure: CHI offense succeeds (4+ goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no has the higher standalone adjusted growth (7.39 vs 2.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.242); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no: REINFORCING (phi 0.242); KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.1); failure: CHI offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no has the higher standalone adjusted growth (7.39 vs 2.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.192); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no: REINFORCING (phi 0.192); KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.1); failure: CHI offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.14, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:SUPPRESSED (p 0.4811): highest fidelity KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no (same contract)
- KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2978, phi -0.203)
- KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2978, phi -0.277)
- KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.5 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2978, phi -0.241)

portfolios: A EV +2.05 (adj +0.57) on $18.78, P(profit) 0.6093, adj growth 5.3 bp · B EV +1.54 (adj +0.53) on $17.01, P(profit) 0.7304, adj growth 5.0 bp · C EV +0.92 (adj +0.54) on $16.66, P(profit) 0.8053, adj growth 5.0 bp · R EV +0.17 (adj +0.10) on $3.00, P(profit) 0.8053, adj growth 3.7 bp

## BOS @ STL  ·  10000 joint draws  ·  416 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_BOS_win | p_overtime | goals | shots STL/BOS | STL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.53 | 0.47 | 0.00 | 6.05 | 27.1/26.8 | 23.4/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.48 | 5.95 | 27.4/27.3 | 24.0/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.55 | 0.45 | 0.00 | 9.36 | 28.8/28.6 | 22.7/22.6 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.088 | 0.61 | 0.39 | 0.00 | 6.04 | 32.1/21.4 | 18.4/27.8 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.51 | 0.49 | 0.49 | 5.91 | 32.5/21.9 | 18.8/29.2 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.068 | 0.65 | 0.35 | 0.00 | 9.41 | 34.0/23.1 | 18.3/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 24 | 0.293 | 0.278 | +0.040 | +0.026 | $4.59 | FUNDED_RESEARCH | $2 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Charlie McAvoy: 1+ assists NO | 54 | 0.622 | 0.579 | +0.065 | +0.021 | $6.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT29BOSSTL-10|yes; why: higher confidence-adjusted growth (7.56 vs 0.94 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.886 vs 0.325); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.028); failure: STL offense suppressed (<= 2 goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29BOSSTL-BOSDPASTRNAK88-1|no; why: higher confidence-adjusted growth (3.94 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.028); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4348): highest fidelity KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.3957): highest fidelity KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no (same contract)
- KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3465, phi -0.254)
- KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.385, phi -0.256)

portfolios: A EV +1.67 (adj +0.80) on $12.56, P(profit) 0.7264, adj growth 7.3 bp · B EV +1.50 (adj +0.72) on $11.25, P(profit) 0.7264, adj growth 6.7 bp · C EV +2.20 (adj +1.06) on $16.54, P(profit) 0.7264, adj growth 9.4 bp · R EV +0.32 (adj +0.20) on $2.00, P(profit) 0.2929, adj growth 7.1 bp

## WSH @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_WSH_win | p_overtime | goals | shots NSH/WSH | NSH/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.51 | 0.49 | 0.00 | 6.02 | 28.0/28.0 | 24.4/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.45 | 5.94 | 28.2/28.0 | 24.7/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.51 | 0.49 | 0.00 | 9.41 | 29.5/29.5 | 23.3/23.0 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.075 | 0.44 | 0.56 | 0.00 | 6.03 | 22.2/32.8 | 28.8/18.9 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.066 | 0.59 | 0.41 | 0.00 | 6.0 | 32.9/22.6 | 19.6/28.8 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.48 | 0.52 | 0.46 | 5.91 | 22.5/33.0 | 29.7/19.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 16 | 0.240 | 0.217 | +0.071 | +0.048 | $7.46 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ assists NO | 74 | 0.800 | 0.768 | +0.047 | +0.014 | $9.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT29WSHNSH-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (35.03 vs 0.07 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0025 below the 0.010/contract floor; relationships: KXNHLAST-26OCT29WSHNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: WSH offense suppressed (<= 2 goals)
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHL3PTOTAL-26OCT29WSHNSH-3|no; why: higher confidence-adjusted growth (2.38 vs 0.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3925): highest fidelity KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes (same contract)
- thesis NSH:SUPPRESSED (p 0.3742): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.391, phi -0.24)
- KXNHLAST-26OCT29WSHNSH-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.4055, phi -0.191)

portfolios: A EV +3.60 (adj +2.27) on $15.03, P(profit) 0.24, adj growth 20.9 bp · B EV +3.68 (adj +2.29) on $16.69, P(profit) 0.24, adj growth 21.0 bp · C EV +4.56 (adj +3.11) on $10.94, P(profit) 0.24, adj growth 27.3 bp · R EV +0.83 (adj +0.57) on $2.00, P(profit) 0.24, adj growth 20.7 bp

## MTL @ DAL  ·  10000 joint draws  ·  406 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_MTL_win | p_overtime | goals | shots DAL/MTL | DAL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.57 | 0.43 | 0.00 | 6.02 | 26.2/25.7 | 22.5/22.3 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.113 | 0.65 | 0.35 | 0.00 | 5.97 | 31.5/20.4 | 17.6/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.46 | 5.96 | 26.5/26.0 | 22.7/23.2 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.56 | 0.44 | 0.45 | 5.88 | 31.8/20.9 | 17.7/28.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.59 | 0.41 | 0.00 | 9.2 | 28.0/27.5 | 22.0/21.4 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.073 | 0.66 | 0.34 | 0.00 | 9.22 | 33.2/22.0 | 17.3/25.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Phillip Danault: 1+ goals YES | 9 | 0.122 | 0.113 | +0.026 | +0.017 | $2.45 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Phillip Danault: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29MTLDAL-MTLJANDERSON17-1|yes; why: higher confidence-adjusted growth (7.12 vs 0.15 bp); alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis MTL:OFFENSE_4PLUS (p 0.3288): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29MTLDAL-MTLPDANAULT24-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.4565, phi -0.172)

portfolios: A EV +0.74 (adj +0.48) on $2.72, P(profit) 0.1219, adj growth 4.4 bp · B EV +0.67 (adj +0.43) on $2.45, P(profit) 0.1219, adj growth 4.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ MIN  ·  10000 joint draws  ·  390 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_NYI_win | p_overtime | goals | shots MIN/NYI | MIN/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.58 | 0.42 | 0.00 | 6.0 | 28.3/28.0 | 24.8/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.52 | 0.48 | 0.47 | 5.89 | 28.2/28.0 | 24.7/24.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.086 | 0.63 | 0.37 | 0.00 | 5.98 | 33.3/22.2 | 19.4/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.58 | 0.42 | 0.00 | 9.28 | 29.6/29.4 | 23.8/22.9 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.58 | 0.42 | 0.46 | 5.9 | 33.6/22.5 | 19.5/30.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.055 | 0.53 | 0.47 | 0.00 | 3.51 | 27.0/26.9 | 25.2/24.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kirill Kaprizov: 1+ goals NO | 53 | 0.611 | 0.588 | +0.063 | +0.041 | $11.34 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 19 | 0.250 | 0.231 | +0.049 | +0.030 | $4.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.165 | 0.151 | +0.037 | +0.024 | $3.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 11 | 0.158 | 0.138 | +0.042 | +0.021 | $2.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no; why: higher confidence-adjusted growth (14.63 vs 3.86 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.996 vs 0.889); relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT29NYIMIN-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: MIN offense succeeds (4+ goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes; why: higher confidence-adjusted growth (12.25 vs 10.65 bp); relationships: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT29NYIMIN-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: NYI offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (12.25 vs 10.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.026); they share one thesis budget; relationships: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT29NYIMIN-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NYI offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (12.25 vs 8.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.3645): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:OFFENSE_4PLUS (p 0.3337): highest fidelity KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4451): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29NYIMIN-MIN2|no (same contract)
- KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4206, phi -0.303)
- KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4457, phi -0.249)
- KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4457, phi -0.21)
- KXNHLGOAL-26OCT29NYIMIN-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4457, phi -0.191)

portfolios: A EV +2.42 (adj +0.92) on $18.78, P(profit) 0.4643, adj growth 8.3 bp · B EV +4.47 (adj +2.69) on $22.36, P(profit) 0.469, adj growth 24.9 bp · C EV +4.01 (adj +2.42) on $27.39, P(profit) 0.706, adj growth 21.7 bp · R EV +0.35 (adj +0.22) on $3.00, P(profit) 0.6108, adj growth 8.3 bp

## BUF @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BUF_win | p_overtime | goals | shots ANA/BUF | ANA/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.57 | 0.43 | 0.00 | 6.02 | 28.3/28.0 | 24.8/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.52 | 0.48 | 0.50 | 5.99 | 28.1/28.2 | 24.8/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.57 | 0.43 | 0.00 | 9.37 | 29.5/29.5 | 23.6/23.0 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.084 | 0.64 | 0.36 | 0.00 | 6.03 | 33.4/22.6 | 19.8/28.9 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.47 | 5.98 | 33.2/22.5 | 19.3/29.9 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.067 | 0.65 | 0.35 | 0.00 | 9.37 | 34.7/23.6 | 18.7/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim wins by over 1.5 goals YES | 25 | 0.336 | 0.290 | +0.073 | +0.027 | $2.54 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 2.5 goals YES | 16 | 0.227 | 0.191 | +0.057 | +0.021 | $1.14 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Buffalo wins by over 2.5 goals NO | 77 | 0.849 | 0.804 | +0.066 | +0.022 | $11.34 | FUNDED_RESEARCH | $3 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT29BUFANA-ANA3|yes; why: higher confidence-adjusted growth (8.42 vs 7.10 bp); relationships: KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: DUPLICATIVE (phi 0.761); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: DUPLICATIVE (phi 0.301); failure: BUF wins (incl. OT/SO)
- **Anaheim wins by over 2.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (8.42 vs 7.10 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.761); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.761); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: REINFORCING (phi 0.229); failure: BUF wins (incl. OT/SO)
- **Buffalo wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (8.42 vs 6.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.301); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.301); KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: REINFORCING (phi 0.229); failure: BUF wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:WINS_BY_2PLUS (p 0.3361): highest fidelity KXNHLSPREAD-26OCT29BUFANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes (same contract)
- thesis ANA:WINS (p 0.5487): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3936): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4513, phi -0.645)
- KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: FUNDED_RESEARCH; family MIXED; loses 33% of the draws where the thesis happens; opposing: failure thesis BUF:WINS (p 0.4513, phi -0.491)
- KXNHLSPREAD-26OCT29BUFANA-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2482, phi -0.735)

portfolios: A EV +2.69 (adj +0.93) on $18.78, P(profit) 0.5903, adj growth 8.3 bp · B EV +2.05 (adj +0.73) on $15.01, P(profit) 0.3361, adj growth 6.8 bp · C EV +1.95 (adj +0.73) on $7.04, P(profit) 0.3361, adj growth 6.5 bp · R EV +0.87 (adj +0.32) on $5.00, P(profit) 0.3361, adj growth 10.9 bp

## OTT @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_OTT_win | p_overtime | goals | shots LAK/OTT | LAK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.57 | 0.43 | 0.00 | 5.98 | 26.9/27.0 | 23.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.55 | 0.45 | 0.46 | 5.93 | 26.8/27.0 | 23.7/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.55 | 0.45 | 0.00 | 9.17 | 28.4/28.8 | 23.3/22.2 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.077 | 0.53 | 0.47 | 0.00 | 5.98 | 21.6/32.2 | 28.7/18.2 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.51 | 0.49 | 0.45 | 5.82 | 21.4/32.3 | 29.0/18.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.49 | 0.51 | 0.48 | 2.8 | 25.4/25.7 | 24.1/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ottawa wins by over 1.5 goals NO | 70 | 0.757 | 0.726 | +0.043 | +0.011 | $6.15 | FUNDED_RESEARCH | $2 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ottawa wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT3|no; why: higher confidence-adjusted growth (1.42 vs 0.07 bp); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: OTT wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis LAK:WINS (p 0.5494): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT2|no (same contract)
- KXNHLSPREAD-26OCT29OTTLA-OTT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2426, phi -1.0)

portfolios: A EV +0.45 (adj +0.12) on $7.51, P(profit) 0.7574, adj growth 1.1 bp · B EV +0.37 (adj +0.10) on $6.15, P(profit) 0.7574, adj growth 0.9 bp · C EV +0.54 (adj +0.15) on $9.03, P(profit) 0.7574, adj growth 1.3 bp · R EV +0.12 (adj +0.03) on $2.00, P(profit) 0.7574, adj growth 1.2 bp

## VAN @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_VAN_win | p_overtime | goals | shots SJS/VAN | SJS/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.61 | 0.39 | 0.00 | 6.06 | 27.8/27.4 | 24.2/23.6 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.106 | 0.65 | 0.35 | 0.00 | 6.06 | 33.0/21.7 | 18.8/28.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.60 | 0.40 | 0.00 | 9.4 | 29.4/29.0 | 23.4/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.47 | 5.93 | 27.7/27.3 | 24.0/24.4 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.54 | 0.46 | 0.46 | 5.99 | 33.2/21.8 | 18.7/29.8 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.093 | 0.70 | 0.30 | 0.00 | 9.39 | 34.6/23.0 | 18.4/26.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
