# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-27T21:05:41Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +26.18 | +7.79 | +25.13 | 0.787 | -14.10 | -24.12 | 72.70 |
| B thesis-diversified (joint) ← optimiser card | 148.35 | +20.14 | +10.87 | +19.18 | 0.735 | -19.07 | -28.23 | 104.08 |
| C best expression per thesis | 150.00 | +18.89 | +7.87 | +18.83 | 0.747 | -17.64 | -27.71 | 74.66 |
| R FUNDED research stakes | 18.00 | +1.67 | +1.05 | +1.36 | 0.623 | -4.55 | -6.46 | 0.00 |

## CBJ @ PHI  ·  10000 joint draws  ·  466 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.479 / away 0.521

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CBJ_win | p_overtime | goals | shots PHI/CBJ | PHI/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.56 | 0.44 | 0.00 | 5.96 | 26.5/26.7 | 23.6/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.52 | 0.48 | 0.47 | 5.85 | 26.7/26.8 | 23.6/23.4 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.086 | 0.49 | 0.51 | 0.00 | 6.0 | 21.2/32.0 | 28.3/17.8 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.44 | 0.56 | 0.47 | 5.79 | 21.0/31.4 | 28.0/17.9 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.47 | 0.53 | 0.49 | 2.81 | 25.1/25.6 | 24.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.064 | 0.59 | 0.41 | 0.00 | 9.25 | 28.0/28.3 | 22.7/21.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Damon Severson: 1+ goals YES | 8 | 0.115 | 0.105 | +0.030 | +0.020 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Conor Garland: 1+ goals NO | 84 | 0.882 | 0.870 | +0.032 | +0.021 | $6.83 | FUNDED_RESEARCH | $2 | CBJ:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 15 | 0.185 | 0.175 | +0.027 | +0.017 | $1.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Columbus wins by over 1.5 goals NO | 70 | 0.766 | 0.731 | +0.052 | +0.016 | $6.83 | FUNDED_RESEARCH | $2 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (10.96 vs 4.38 bp); relationships: KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no: INTENTIONAL_DIVERSIFIER (phi -0.094); failure: CBJ offense suppressed (<= 2 goals)
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no; why: higher confidence-adjusted growth (7.42 vs 2.77 bp); despite a smaller raw edge (+0.032 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no: MOSTLY_INDEPENDENT (phi 0.109); failure: CBJ offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27CBJPHI-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (4.38 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0010 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no: INTENTIONAL_DIVERSIFIER (phi -0.21); failure: CBJ offense suppressed (<= 2 goals)
- **Columbus wins by over 1.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT27CBJPHI-CBJ3|no; why: higher confidence-adjusted growth (2.77 vs 1.79 bp); relationships: KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.094); KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.109); KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.21); failure: CBJ wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3118): highest fidelity KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3647): highest fidelity KXNHLSPREAD-26OCT27CBJPHI-CBJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:SUPPRESSED (p 0.4704): highest fidelity KXNHLSPREAD-26OCT27CBJPHI-CBJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4704, phi -0.172)
- KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3118, phi -0.155)
- KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4704, phi -0.229)
- KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CBJ:WINS_BY_2PLUS (p 0.2335, phi -1.0)

portfolios: A EV +1.02 (adj +0.29) on $13.64, P(profit) 0.6951, adj growth 2.8 bp · B EV +1.69 (adj +0.93) on $17.31, P(profit) 0.8025, adj growth 8.9 bp · C EV +1.02 (adj +0.44) on $10.88, P(profit) 0.8444, adj growth 4.2 bp · R EV +0.22 (adj +0.09) on $4.00, P(profit) 0.6908, adj growth 3.6 bp

## BOS @ CAR  ·  10000 joint draws  ·  460 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.629 / away 0.371

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_BOS_win | p_overtime | goals | shots CAR/BOS | CAR/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.164 | 0.61 | 0.39 | 0.00 | 6.07 | 34.5/21.2 | 18.2/30.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.142 | 0.54 | 0.46 | 0.44 | 5.98 | 34.8/21.7 | 18.5/31.1 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.138 | 0.69 | 0.31 | 0.00 | 9.47 | 36.3/22.7 | 17.8/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.081 | 0.59 | 0.41 | 0.00 | 6.07 | 27.7/26.6 | 23.4/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.49 | 0.51 | 0.46 | 6.01 | 28.3/27.2 | 23.7/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.56 | 0.44 | 0.00 | 9.4 | 29.7/28.7 | 23.0/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Casey Mittelstadt: 1+ goals YES | 12 | 0.183 | 0.166 | +0.055 | +0.038 | $3.42 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Pavel Zacha: 1+ goals YES | 22 | 0.276 | 0.259 | +0.044 | +0.027 | $2.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mark Kastelic: 1+ goals YES | 8 | 0.109 | 0.101 | +0.024 | +0.016 | $1.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| William Carrier: 1+ goals YES | 15 | 0.187 | 0.177 | +0.028 | +0.018 | $1.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (28.15 vs 9.09 bp); relationships: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27BOSCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: BOS offense suppressed (<= 2 goals)
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSFMINTEN93-1|yes; why: higher confidence-adjusted growth (9.09 vs 4.59 bp); relationships: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT27BOSCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: BOS offense suppressed (<= 2 goals)
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes has the higher standalone adjusted growth (9.09 vs 6.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT27BOSCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: BOS offense suppressed (<= 2 goals)
- **William Carrier: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27BOSCAR-CARKMILLER19-1|yes; why: higher confidence-adjusted growth (5.13 vs 4.42 bp); despite a smaller raw edge (+0.028 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: CAR offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.14.
- thesis BOS:OFFENSE_4PLUS (p 0.3761): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:OFFENSE_4PLUS (p 0.4764): highest fidelity KXNHLTOTAL-26OCT27BOSCAR-7|yes [DIRECT], best adjusted EV KXNHLAST-26OCT27BOSCAR-CARKMILLER19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3188): highest fidelity KXNHLTOTAL-26OCT27BOSCAR-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3979, phi -0.196)
- KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3979, phi -0.228)
- KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3979, phi -0.153)
- KXNHLGOAL-26OCT27BOSCAR-CARWCARRIER28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:SUPPRESSED (p 0.3132, phi -0.18)

portfolios: A EV +2.47 (adj +0.73) on $13.64, P(profit) 0.5631, adj growth 6.7 bp · B EV +2.73 (adj +1.82) on $9.43, P(profit) 0.5735, adj growth 17.2 bp · C EV +2.16 (adj +0.87) on $14.52, P(profit) 0.5732, adj growth 8.2 bp · R EV +0.43 (adj +0.30) on $1.00, P(profit) 0.1827, adj growth 11.3 bp

## LAK @ CHI  ·  10000 joint draws  ·  436 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.503 / away 0.497

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_LAK_win | p_overtime | goals | shots CHI/LAK | CHI/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.50 | 0.50 | 0.00 | 5.99 | 26.7/27.2 | 23.7/23.2 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.107 | 0.45 | 0.55 | 0.00 | 5.98 | 21.2/32.4 | 28.3/18.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.49 | 0.51 | 0.47 | 5.84 | 27.0/27.5 | 24.1/23.7 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.47 | 0.53 | 0.50 | 5.93 | 21.4/32.5 | 29.2/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.068 | 0.48 | 0.52 | 0.00 | 9.1 | 28.3/28.6 | 22.7/22.4 | even strength |
| LAK shot control · low event (<=4) · tight (1-goal/OT) | 0.060 | 0.46 | 0.54 | 0.45 | 2.72 | 19.9/30.8 | 29.3/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.077 | 0.069 | +0.024 | +0.016 | $1.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Roman Kantserov: 1+ goals NO | 74 | 0.792 | 0.778 | +0.039 | +0.025 | $6.91 | FUNDED_RESEARCH | $2 | CHI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 52 | 0.607 | 0.561 | +0.069 | +0.023 | $4.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Erik Gustafsson: 1+ assists NO | 62 | 0.737 | 0.654 | +0.100 | +0.018 | $4.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27LACHI-LAEHAULA56-1|yes; why: higher confidence-adjusted growth (10.21 vs 0.89 bp); alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.093); KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: LAK offense suppressed (<= 2 goals)
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no; why: Player prop expression KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.89 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: CHI offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no; why: higher confidence-adjusted growth (4.79 vs 3.00 bp); despite a smaller raw edge (+0.069 vs +0.100/contract); relationships: KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.093); KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi 0.056); failure: LAK offense succeeds (4+ goals)
- **Erik Gustafsson: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no; why: second expression of the same thesis: KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no has the higher standalone adjusted growth (4.79 vs 3.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.056); they share one thesis budget; relationships: KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.056); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CHI:SUPPRESSED (p 0.4415): highest fidelity KXNHLAST-26OCT27LACHI-CHICBEDARD98-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no — Player prop expression KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.89 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis LAK:SUPPRESSED (p 0.4197): highest fidelity KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.365): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4197, phi -0.134)
- KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3433, phi -0.195)
- KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.365, phi -0.287)
- KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.7 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.365, phi -0.236)
- override: Player prop expression KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.89 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.36 (adj +0.49) on $13.64, P(profit) 0.6002, adj growth 4.7 bp · B EV +2.24 (adj +0.94) on $17.31, P(profit) 0.5349, adj growth 9.0 bp · C EV +1.13 (adj +0.51) on $13.89, P(profit) 0.4852, adj growth 4.9 bp · R EV +0.10 (adj +0.07) on $2.00, P(profit) 0.7923, adj growth 2.5 bp

## MTL @ STL  ·  10000 joint draws  ·  456 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.492 / away 0.508

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_MTL_win | p_overtime | goals | shots STL/MTL | STL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.62 | 0.38 | 0.00 | 6.06 | 27.0/26.8 | 23.7/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.45 | 5.94 | 27.1/27.0 | 23.7/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.61 | 0.39 | 0.00 | 9.38 | 28.6/28.5 | 22.9/21.8 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.080 | 0.69 | 0.31 | 0.00 | 6.07 | 31.7/21.3 | 18.7/27.0 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.54 | 0.46 | 0.47 | 5.9 | 31.9/21.4 | 18.3/28.5 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.060 | 0.69 | 0.31 | 0.00 | 9.32 | 33.5/22.7 | 18.0/25.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 24 | 0.306 | 0.288 | +0.053 | +0.035 | $3.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 14 | 0.187 | 0.174 | +0.038 | +0.025 | $2.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 30 | 0.357 | 0.341 | +0.042 | +0.026 | $3.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
| Noah Dobson: 1+ goals NO | 87 | 0.903 | 0.893 | +0.025 | +0.015 | $6.93 | FUNDED_RESEARCH | $2 | MTL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes; why: higher confidence-adjusted growth (14.36 vs 10.94 bp); relationships: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27MTLSTL-MTLNDOBSON53-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (14.36 vs 10.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT27MTLSTL-MTLNDOBSON53-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (14.36 vs 7.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT27MTLSTL-MTLNDOBSON53-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: STL offense suppressed (<= 2 goals)
- **Noah Dobson: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT27MTLSTL-MTL2|no; why: higher confidence-adjusted growth (4.88 vs 3.66 bp); despite a smaller raw edge (+0.025 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4648): highest fidelity KXNHLTEAMTOTAL-26OCT27MTLSTL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.573): highest fidelity KXNHLSPREAD-26OCT27MTLSTL-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.4187): highest fidelity KXNHLSPREAD-26OCT27MTLSTL-MTL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27MTLSTL-MTL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3177, phi -0.245)
- KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3177, phi -0.19)
- KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3177, phi -0.269)
- KXNHLGOAL-26OCT27MTLSTL-MTLNDOBSON53-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3629, phi -0.145)

portfolios: A EV +2.86 (adj +1.18) on $13.64, P(profit) 0.619, adj growth 11.1 bp · B EV +2.04 (adj +1.33) on $16.37, P(profit) 0.5926, adj growth 12.8 bp · C EV +1.38 (adj +0.77) on $10.10, P(profit) 0.3059, adj growth 7.3 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.9027, adj growth 1.4 bp

## NYI @ NSH  ·  10000 joint draws  ·  438 bet sides mapped, 9 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.521 / away 0.479

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_NYI_win | p_overtime | goals | shots NSH/NYI | NSH/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.54 | 0.46 | 0.00 | 6.02 | 27.7/27.8 | 24.4/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.50 | 5.96 | 28.2/28.5 | 25.2/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.55 | 0.45 | 0.00 | 9.24 | 29.2/29.4 | 23.5/22.9 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.082 | 0.49 | 0.51 | 0.00 | 6.0 | 22.2/33.2 | 29.4/18.8 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.49 | 0.51 | 0.46 | 5.91 | 22.2/33.5 | 30.0/19.0 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.056 | 0.59 | 0.41 | 0.00 | 6.04 | 32.6/22.1 | 19.2/28.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Wilsby: 1+ goals YES | 5 | 0.078 | 0.070 | +0.025 | +0.017 | $1.33 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ assists NO | 72 | 0.792 | 0.754 | +0.058 | +0.019 | $6.93 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Ryan O'Reilly: 1+ goals YES | 28 | 0.322 | 0.310 | +0.028 | +0.016 | $1.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NYINSH-NSHAWILSBY2-1|yes; why: higher confidence-adjusted growth (11.41 vs 3.79 bp); despite a smaller raw edge (+0.025 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27NYINSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: NSH offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27NYINSH-NYIMSCHAEFER48-1|no; why: higher confidence-adjusted growth (4.28 vs 0.69 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27NYINSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27NYINSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: NYI offense succeeds (4+ goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NYINSH-NSHAWILSBY2-1|yes; why: Player prop expression KXNHLGOAL-26OCT27NYINSH-NSHROREILLY90-1|yes selected over player prop KXNHLAST-26OCT27NYINSH-NSHAWILSBY2-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.45 vs 0.43 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27NYINSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NYI:SUPPRESSED (p 0.4006): highest fidelity KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.4082): highest fidelity KXNHLGOAL-26OCT27NYINSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT27NYINSH-NSHAWILSBY2-1|yes — Player prop expression KXNHLGOAL-26OCT27NYINSH-NSHROREILLY90-1|yes selected over player prop KXNHLAST-26OCT27NYINSH-NSHAWILSBY2-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.45 vs 0.43 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NYI:OFFENSE_4PLUS (p 0.3835): highest fidelity KXNHLGOAL-26OCT27NYINSH-NYIBSCHENN10-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27NYINSH-NYIJPAGEAU44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27NYINSH-NSHAWILSBY2-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3633, phi -0.121)
- KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.3835, phi -0.223)
- KXNHLGOAL-26OCT27NYINSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3633, phi -0.234)
- override: Player prop expression KXNHLGOAL-26OCT27NYINSH-NSHROREILLY90-1|yes selected over player prop KXNHLAST-26OCT27NYINSH-NSHAWILSBY2-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.45 vs 0.43 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.60 (adj +1.11) on $13.64, P(profit) 0.5137, adj growth 10.2 bp · B EV +1.35 (adj +0.70) on $10.24, P(profit) 0.3122, adj growth 6.7 bp · C EV +1.45 (adj +0.50) on $12.29, P(profit) 0.3493, adj growth 4.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ DAL  ·  10000 joint draws  ·  486 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.508 / away 0.492

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NJD_win | p_overtime | goals | shots DAL/NJD | DAL/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.61 | 0.39 | 0.00 | 5.98 | 26.6/26.8 | 23.5/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.48 | 5.91 | 26.9/27.0 | 23.7/23.7 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.078 | 0.52 | 0.48 | 0.00 | 5.92 | 21.5/31.7 | 28.2/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.56 | 0.44 | 0.00 | 9.09 | 28.3/28.2 | 22.3/21.8 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.46 | 0.54 | 0.47 | 5.82 | 21.2/31.6 | 28.3/18.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.57 | 0.43 | 0.00 | 3.48 | 25.4/25.5 | 23.8/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Amadeus Lombardi: 1+ goals YES | 9 | 0.123 | 0.114 | +0.028 | +0.018 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 75 | 0.795 | 0.783 | +0.032 | +0.019 | $6.37 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Roope Hintz: 1+ goals YES | 26 | 0.305 | 0.293 | +0.032 | +0.019 | $2.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 68 | 0.723 | 0.711 | +0.028 | +0.016 | $4.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT27NJDAL-NJCGLASS12-1|yes; why: higher confidence-adjusted growth (7.96 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.068/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NJDAL-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: NJD offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (4.61 vs 3.83 bp); despite a smaller raw edge (+0.032 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense succeeds (4+ goals)
- **Roope Hintz: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes; why: higher confidence-adjusted growth (4.03 vs 3.92 bp); despite a smaller raw edge (+0.032 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT27NJDAL-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: DAL offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27NJDAL-NJTMEIER28-1|no; why: Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT27NJDAL-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NJD:SUPPRESSED (p 0.4734): highest fidelity KXNHLGOAL-26OCT27NJDAL-NJTMEIER28-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis DAL:OFFENSE_4PLUS (p 0.3866): highest fidelity KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.3148): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4734, phi -0.174)
- KXNHLGOAL-26OCT27NJDAL-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3148, phi -0.228)
- KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3953, phi -0.264)
- KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3148, phi -0.254)
- override: Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.56 (adj +0.48) on $13.64, P(profit) 0.6547, adj growth 4.6 bp · B EV +1.15 (adj +0.71) on $14.28, P(profit) 0.3391, adj growth 6.8 bp · C EV +0.68 (adj +0.41) on $11.26, P(profit) 0.2422, adj growth 3.9 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.7951, adj growth 1.9 bp

## FLA @ WPG  ·  10000 joint draws  ·  512 bet sides mapped, 13 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.455 / away 0.545

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_FLA_win | p_overtime | goals | shots WPG/FLA | WPG/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.53 | 0.47 | 0.00 | 6.01 | 26.6/26.8 | 23.5/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.47 | 0.53 | 0.48 | 5.93 | 26.9/26.9 | 23.6/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.52 | 0.48 | 0.00 | 9.17 | 28.3/28.5 | 22.5/21.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.073 | 0.50 | 0.50 | 0.00 | 5.99 | 21.3/31.8 | 28.2/17.9 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.44 | 5.88 | 21.3/31.8 | 28.5/18.1 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.063 | 0.58 | 0.42 | 0.00 | 6.02 | 31.6/21.7 | 18.7/27.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 65 | 0.720 | 0.701 | +0.054 | +0.035 | $5.19 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 67 | 0.730 | 0.714 | +0.045 | +0.028 | $5.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Neal Pionk: 1+ goals NO | 89 | 0.918 | 0.910 | +0.021 | +0.013 | $5.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no; why: higher confidence-adjusted growth (12.40 vs 8.24 bp); relationships: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT27FLAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: FLA offense succeeds (4+ goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no; why: Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no because adjusted EV is 0.3 pts higher while thesis capture is 0.87 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT27FLAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: FLA offense succeeds (4+ goals)
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT27FLAWPG-WPGNPIONK4-2|no; why: higher confidence-adjusted growth (3.99 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis FLA:SUPPRESSED (p 0.4303): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no — Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no because adjusted EV is 0.3 pts higher while thesis capture is 0.87 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WPG:WINS (p 0.5261): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3823): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT27FLAWPG-FLA3|no (same contract)
- KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3496, phi -0.241)
- KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3496, phi -0.26)
- KXNHLGOAL-26OCT27FLAWPG-WPGNPIONK4-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3823, phi -0.124)
- override: Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no because adjusted EV is 0.3 pts higher while thesis capture is 0.87 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.44 (adj +0.61) on $13.64, P(profit) 0.7394, adj growth 5.9 bp · B EV +0.90 (adj +0.57) on $16.16, P(profit) 0.4834, adj growth 5.6 bp · C EV +1.20 (adj +0.69) on $17.66, P(profit) 0.5267, adj growth 6.6 bp · R EV +0.16 (adj +0.11) on $2.00, P(profit) 0.7201, adj growth 4.1 bp

## MIN @ UTA  ·  10000 joint draws  ·  464 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.523 / away 0.477

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_MIN_win | p_overtime | goals | shots UTA/MIN | UTA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.59 | 0.41 | 0.00 | 6.01 | 28.1/28.0 | 24.9/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.54 | 0.46 | 0.47 | 5.94 | 28.1/28.2 | 24.9/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.60 | 0.40 | 0.00 | 9.43 | 29.9/29.6 | 24.2/23.0 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.079 | 0.63 | 0.37 | 0.00 | 6.03 | 33.4/22.5 | 19.6/29.0 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.55 | 0.45 | 0.47 | 5.95 | 33.5/22.7 | 19.4/30.2 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.061 | 0.70 | 0.30 | 0.00 | 9.33 | 35.2/23.8 | 19.2/27.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kirill Kaprizov: 1+ goals NO | 56 | 0.642 | 0.620 | +0.065 | +0.043 | $6.93 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 12 | 0.156 | 0.145 | +0.029 | +0.017 | $1.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 19 | 0.235 | 0.221 | +0.034 | +0.021 | $2.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.127 | 0.119 | +0.021 | +0.013 | $1.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-2|no; why: higher confidence-adjusted growth (16.69 vs 6.61 bp); relationships: KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27MINUTA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: MIN offense succeeds (4+ goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (5.78 vs 5.67 bp); despite a smaller raw edge (+0.029 vs +0.034/contract); relationships: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT27MINUTA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: UTA offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes; why: higher confidence-adjusted growth (5.67 vs 1.93 bp); relationships: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT27MINUTA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: UTA offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT27MINUTA-3|yes; why: higher confidence-adjusted growth (3.80 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.907 vs 0.762); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.4274): highest fidelity KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.4483): highest fidelity KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.3534): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3534, phi -0.298)
- KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3344, phi -0.166)
- KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3344, phi -0.211)
- KXNHLGOAL-26OCT27MINUTA-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4274, phi -0.174)

portfolios: A EV +1.97 (adj +0.57) on $13.64, P(profit) 0.5534, adj growth 5.4 bp · B EV +1.73 (adj +1.09) on $11.83, P(profit) 0.7053, adj growth 10.5 bp · C EV +1.40 (adj +0.90) on $11.13, P(profit) 0.7272, adj growth 8.6 bp · R EV +0.22 (adj +0.15) on $2.00, P(profit) 0.6421, adj growth 5.7 bp

## OTT @ VGK  ·  10000 joint draws  ·  456 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.588 / away 0.412

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_OTT_win | p_overtime | goals | shots VGK/OTT | VGK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.01 | 26.8/26.7 | 23.8/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.47 | 5.91 | 26.8/26.6 | 23.3/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.61 | 0.39 | 0.00 | 9.29 | 28.1/28.1 | 22.4/21.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.080 | 0.68 | 0.32 | 0.00 | 5.99 | 31.3/21.2 | 18.6/26.7 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.55 | 0.45 | 0.47 | 5.89 | 31.6/21.3 | 18.2/28.3 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.060 | 0.56 | 0.44 | 0.00 | 6.06 | 21.2/31.2 | 27.7/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 6 | 0.086 | 0.078 | +0.022 | +0.014 | $1.21 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Marc Gatcomb: 1+ goals YES | 9 | 0.120 | 0.111 | +0.024 | +0.015 | $1.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ assists NO | 47 | 0.607 | 0.512 | +0.120 | +0.024 | $4.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Jake Sanderson: 1+ assists NO | 59 | 0.712 | 0.629 | +0.105 | +0.022 | $5.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (7.22 vs 1.83 bp); relationships: KXNHLGOAL-26OCT27OTTVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VGK offense suppressed (<= 2 goals)
- **Marc Gatcomb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (5.87 vs 1.83 bp); relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (5.09 vs 1.04 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT27OTTVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: VGK offense succeeds (4+ goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27OTTVGK-OTTTSTUTZLE18-2|no; why: higher confidence-adjusted growth (4.59 vs 3.30 bp); relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT27OTTVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.3344): highest fidelity KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:SUPPRESSED (p 0.4484): highest fidelity KXNHLAST-26OCT27OTTVGK-OTTTSTUTZLE18-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.3355): highest fidelity KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes (same contract)
- KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3344, phi -0.122)
- KXNHLGOAL-26OCT27OTTVGK-VGKMGATCOMB17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3344, phi -0.148)
- KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.7 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4477, phi -0.278)
- KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.7 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3355, phi -0.245)

portfolios: A EV +2.45 (adj +0.43) on $13.64, P(profit) 0.7329, adj growth 4.2 bp · B EV +2.72 (adj +0.89) on $12.14, P(profit) 0.5489, adj growth 8.5 bp · C EV +3.95 (adj +0.80) on $18.98, P(profit) 0.7218, adj growth 7.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ ANA  ·  10000 joint draws  ·  454 bet sides mapped, 8 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.653 / away 0.347

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_VAN_win | p_overtime | goals | shots ANA/VAN | ANA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.152 | 0.68 | 0.32 | 0.00 | 6.07 | 34.4/21.6 | 18.9/29.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.137 | 0.71 | 0.29 | 0.00 | 9.36 | 36.0/22.6 | 18.1/27.7 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.55 | 0.45 | 0.45 | 5.97 | 34.1/21.5 | 18.3/30.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.096 | 0.64 | 0.36 | 0.00 | 6.08 | 28.0/27.3 | 24.2/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.59 | 0.41 | 0.00 | 9.49 | 29.6/28.6 | 22.8/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.50 | 0.50 | 0.44 | 6.01 | 28.0/27.1 | 23.7/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Filip Chytil: 1+ goals YES | 18 | 0.234 | 0.220 | +0.044 | +0.029 | $2.91 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 17 | 0.212 | 0.199 | +0.032 | +0.019 | $1.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 12 | 0.153 | 0.144 | +0.026 | +0.016 | $1.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (11.95 vs 5.20 bp); relationships: KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (11.95 vs 5.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (11.95 vs 5.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.15, ANA shot control · high event (8+) · decided (2+) 0.14, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.12.
- thesis VAN:OFFENSE_4PLUS (p 0.3715): highest fidelity KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.5242): highest fidelity KXNHLAST-26OCT27VANANA-ANATWASHE42-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:SUPPRESSED (p 0.2756): highest fidelity KXNHLGOAL-26OCT27VANANA-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27VANANA-ANACGAUTHIER61-1|no (same contract)
- KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.416, phi -0.232)
- KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.416, phi -0.208)
- KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.416, phi -0.204)

portfolios: A EV +4.78 (adj +1.39) on $13.64, P(profit) 0.5683, adj growth 12.4 bp · B EV +1.32 (adj +0.84) on $6.35, P(profit) 0.4879, adj growth 8.0 bp · C EV +1.87 (adj +0.80) on $8.43, P(profit) 0.4404, adj growth 7.6 bp · R EV +0.23 (adj +0.15) on $1.00, P(profit) 0.2344, adj growth 5.7 bp

## BUF @ SJS  ·  10000 joint draws  ·  534 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.430 / away 0.570

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_BUF_win | p_overtime | goals | shots SJS/BUF | SJS/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.55 | 0.45 | 0.00 | 6.05 | 27.8/28.1 | 24.6/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.45 | 5.94 | 27.7/28.1 | 24.8/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.55 | 0.45 | 0.00 | 9.35 | 29.4/29.8 | 24.1/23.0 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.076 | 0.48 | 0.52 | 0.00 | 6.0 | 22.0/32.8 | 28.8/18.8 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.47 | 0.53 | 0.46 | 5.98 | 22.2/33.0 | 29.5/18.9 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.060 | 0.44 | 0.56 | 0.00 | 9.38 | 23.6/34.6 | 28.0/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Gaudette: 1+ goals YES | 13 | 0.175 | 0.162 | +0.037 | +0.024 | $2.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 61 | 0.676 | 0.658 | +0.049 | +0.031 | $6.93 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 62 | 0.734 | 0.657 | +0.098 | +0.020 | $5.83 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Mason Marchment: 1+ goals YES | 23 | 0.270 | 0.257 | +0.027 | +0.015 | $1.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF2|no; why: higher confidence-adjusted growth (10.73 vs 6.31 bp); despite a smaller raw edge (+0.037 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: SJS offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF2|no; why: higher confidence-adjusted growth (9.20 vs 6.31 bp); despite a smaller raw edge (+0.049 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: BUF offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT27BUFSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (3.91 vs 2.25 bp); despite a smaller raw edge (+0.098 vs +0.145/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.085); failure: SJS offense succeeds (4+ goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes has the higher standalone adjusted growth (10.73 vs 2.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.085); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4384): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS_BY_2PLUS (p 0.3061): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3869): highest fidelity KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3465, phi -0.197)
- KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.398, phi -0.24)
- KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.9 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4384, phi -0.229)
- KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3465, phi -0.221)

portfolios: A EV +2.67 (adj +0.51) on $13.64, P(profit) 0.5394, adj growth 4.8 bp · B EV +2.25 (adj +1.05) on $16.93, P(profit) 0.6759, adj growth 10.0 bp · C EV +2.65 (adj +1.18) on $20.86, P(profit) 0.58, adj growth 11.2 bp · R EV +0.16 (adj +0.10) on $2.00, P(profit) 0.6756, adj growth 3.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
