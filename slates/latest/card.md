# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-08T01:24:03Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.11 | +8.75 | +21.87 | 0.627 | -52.56 | -65.75 | 66.49 |
| B thesis-diversified (joint) ← optimiser card | 116.65 | +24.21 | +12.69 | +18.98 | 0.630 | -42.50 | -62.60 | 111.02 |
| C best expression per thesis | 107.70 | +20.06 | +9.33 | +16.00 | 0.628 | -37.62 | -53.62 | 82.02 |
| R FUNDED research stakes | 11.00 | +2.43 | +1.64 | -4.81 | 0.416 | -11.00 | -11.00 | 0.00 |

## DET @ COL  ·  10000 joint draws  ·  454 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.664 / away 0.336

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_DET_win | p_overtime | goals | shots COL/DET | COL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.74 | 0.26 | 0.00 | 5.99 | 28.6/28.2 | 25.7/23.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.112 | 0.76 | 0.24 | 0.00 | 6.01 | 33.7/22.1 | 19.8/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.54 | 0.46 | 0.47 | 5.99 | 28.4/28.0 | 24.6/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.73 | 0.27 | 0.00 | 9.37 | 30.0/29.7 | 24.8/22.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.088 | 0.80 | 0.20 | 0.00 | 9.32 | 35.9/23.7 | 19.8/27.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.60 | 0.40 | 0.44 | 5.98 | 34.2/22.6 | 19.3/30.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sheldon Dries: 1+ goals YES | 7 | 0.106 | 0.096 | +0.032 | +0.022 | $5.18 | FUNDED_RESEARCH | $2 | DET:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Carter Mazur: 1+ goals YES | 6 | 0.085 | 0.076 | +0.021 | +0.012 | $2.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Sam Malinski: 1+ assists YES | 25 | 0.318 | 0.281 | +0.055 | +0.018 | $5.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_MIXED | D |
| Lucas Raymond: 1+ assists NO | 60 | 0.682 | 0.636 | +0.065 | +0.019 | $13.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV07DETCOL-2|yes; why: higher confidence-adjusted growth (14.30 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07DETCOL-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.019); failure: DET offense suppressed (<= 2 goals)
- **Carter Mazur: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV07DETCOL-2|yes; why: higher confidence-adjusted growth (5.48 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07DETCOL-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.022); failure: DET offense suppressed (<= 2 goals)
- **Sam Malinski: 1+ assists YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (3.79 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0022 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07DETCOL-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV07DETCOL-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: COL offense suppressed (<= 2 goals)
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV07DETCOL-DETLRAYMOND23-1|no; why: higher confidence-adjusted growth (3.40 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07DETCOL-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV07DETCOL-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.5356): highest fidelity KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4945): highest fidelity KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.2909): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV07DETCOL-DETSDRIES15-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4945, phi -0.164)
- KXNHLGOAL-26NOV07DETCOL-DETCMAZUR34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4945, phi -0.143)
- KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2617, phi -0.218)
- KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.2909, phi -0.265)

portfolios: A EV +10.93 (adj +5.21) on $50.00, P(profit) 0.4382, adj growth 38.1 bp · B EV +5.74 (adj +2.86) on $27.08, P(profit) 0.3611, adj growth 24.6 bp · C EV +2.55 (adj +0.80) on $18.64, P(profit) 0.7795, adj growth 7.0 bp · R EV +0.86 (adj +0.58) on $2.00, P(profit) 0.1065, adj growth 17.9 bp

## PIT @ LAK  ·  10000 joint draws  ·  436 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.526 / away 0.474

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_PIT_win | p_overtime | goals | shots LAK/PIT | LAK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.57 | 0.42 | 0.00 | 5.99 | 27.7/27.5 | 24.1/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.53 | 0.47 | 0.43 | 5.93 | 27.3/27.4 | 24.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.58 | 0.42 | 0.00 | 9.24 | 29.0/29.0 | 23.4/22.4 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.071 | 0.64 | 0.36 | 0.00 | 6.02 | 32.4/22.0 | 19.3/28.2 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.55 | 0.45 | 0.46 | 5.9 | 32.2/22.0 | 18.9/28.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.066 | 0.47 | 0.53 | 0.00 | 6.02 | 21.7/31.7 | 27.8/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.075 | 0.068 | +0.022 | +0.014 | $3.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Kaedan Korczak: 1+ goals YES | 4 | 0.054 | 0.053 | +0.011 | +0.010 | $2.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ assists NO | 70 | 0.777 | 0.733 | +0.062 | +0.019 | $19.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ goals NO | 63 | 0.680 | 0.666 | +0.033 | +0.020 | $14.18 | FUNDED_RESEARCH | $4 | LAK:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07PITLA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (8.55 vs 1.46 bp); relationships: KXNHLGOAL-26NOV07PITLA-PITKKORCZAK6-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV07PITLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: LAK offense suppressed (<= 2 goals)
- **Kaedan Korczak: 1+ goals YES** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26NOV07PITLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: PIT offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07PITLA-PITEMALKIN71-1|no; why: higher confidence-adjusted growth (3.75 vs 1.42 bp); relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV07PITLA-PITKKORCZAK6-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26NOV07PITLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: PIT offense succeeds (4+ goals)
- **Artemi Panarin: 1+ goals NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07PITLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (3.73 vs 0.16 bp); despite a smaller raw edge (+0.033 vs +0.085/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV07PITLA-PITKKORCZAK6-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis PIT:SUPPRESSED (p 0.4178): highest fidelity KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no (same contract)
- thesis LAK:SUPPRESSED (p 0.357): highest fidelity KXNHLGOAL-26NOV07PITLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07PITLA-LAAPANARIN10-1|no (same contract)
- thesis PIT:WINS_BY_2PLUS (p 0.2416): highest fidelity KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.357, phi -0.132)
- KXNHLGOAL-26NOV07PITLA-PITKKORCZAK6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4178, phi -0.099)
- KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3534, phi -0.232)
- KXNHLGOAL-26NOV07PITLA-LAAPANARIN10-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4268, phi -0.23)

portfolios: A EV +3.54 (adj +1.18) on $50.00, P(profit) 0.6483, adj growth 10.1 bp · B EV +4.50 (adj +2.50) on $39.57, P(profit) 0.5925, adj growth 21.5 bp · C EV +3.68 (adj +1.93) on $39.06, P(profit) 0.6041, adj growth 16.7 bp · R EV +0.21 (adj +0.12) on $4.00, P(profit) 0.6797, adj growth 4.2 bp

## VAN @ EDM  ·  10000 joint draws  ·  428 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.752 / away 0.248

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_VAN_win | p_overtime | goals | shots EDM/VAN | EDM/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.147 | 0.80 | 0.20 | 0.00 | 6.08 | 33.2/21.1 | 18.9/28.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.141 | 0.80 | 0.20 | 0.00 | 9.49 | 34.8/22.3 | 18.3/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.73 | 0.27 | 0.00 | 9.52 | 29.1/28.3 | 23.6/21.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.73 | 0.27 | 0.00 | 6.12 | 27.3/26.6 | 24.1/22.8 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.59 | 0.41 | 0.45 | 6.0 | 33.4/21.3 | 18.2/29.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.54 | 0.46 | 0.48 | 6.02 | 27.7/27.1 | 23.8/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vasily Podkolzin: 1+ goals YES | 26 | 0.348 | 0.325 | +0.075 | +0.051 | $16.95 | FUNDED_RESEARCH | $5 | EDM:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 16 | 0.221 | 0.204 | +0.051 | +0.035 | $8.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 10 | 0.144 | 0.130 | +0.037 | +0.024 | $5.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 57 | 0.736 | 0.622 | +0.148 | +0.034 | $18.74 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (28.82 vs 2.40 bp); despite a smaller raw edge (+0.075 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.192); failure: EDM offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (18.39 vs 5.58 bp); relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.014); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (18.39 vs 12.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.017); failure: VAN offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLGAME-26NOV07VANEDM-EDM|no; why: higher confidence-adjusted growth (10.65 vs 3.83 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.192); KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.15, EDM shot control · high event (8+) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5979): highest fidelity KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.3223): highest fidelity KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2184): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2184, phi -0.226)
- KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4569, phi -0.239)
- KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4569, phi -0.19)
- KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.6 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5979, phi -0.33)

portfolios: A EV +12.65 (adj +2.36) on $50.00, P(profit) 0.6228, adj growth 18.3 bp · B EV +13.96 (adj +7.33) on $50.00, P(profit) 0.5678, adj growth 64.8 bp · C EV +13.82 (adj +6.60) on $50.00, P(profit) 0.4929, adj growth 58.3 bp · R EV +1.37 (adj +0.94) on $5.00, P(profit) 0.3483, adj growth 31.7 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07VANEDM-VAN|yes == KXNHLGAME-26NOV07VANEDM-EDM|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
