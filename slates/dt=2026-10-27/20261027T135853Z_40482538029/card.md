# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-27T13:58:53Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +21.48 | +7.57 | +20.42 | 0.718 | -23.53 | -36.25 | 69.28 |
| B thesis-diversified (joint) ← optimiser card | 149.29 | +29.11 | +15.51 | +25.79 | 0.696 | -34.38 | -48.43 | 141.68 |
| C best expression per thesis | 149.98 | +21.55 | +8.01 | +19.52 | 0.702 | -26.42 | -38.96 | 72.85 |
| R FUNDED research stakes | 12.00 | +1.99 | +1.18 | -1.07 | 0.471 | -5.87 | -8.70 | 0.00 |

## CBJ @ PHI  ·  10000 joint draws  ·  442 bet sides mapped, 16 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CBJ_win | p_overtime | goals | shots PHI/CBJ | PHI/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.56 | 0.44 | 0.00 | 5.98 | 26.5/26.8 | 23.5/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.49 | 5.83 | 26.8/27.1 | 23.9/23.5 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.086 | 0.48 | 0.52 | 0.00 | 5.97 | 21.0/31.8 | 27.9/17.8 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.52 | 0.48 | 0.47 | 5.89 | 20.9/31.8 | 28.4/17.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.070 | 0.52 | 0.48 | 0.00 | 3.42 | 25.3/25.7 | 23.9/23.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.069 | 0.50 | 0.50 | 0.48 | 2.8 | 24.7/25.1 | 23.6/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Sanheim: 1+ goals YES | 8 | 0.120 | 0.109 | +0.035 | +0.024 | $3.50 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 8 | 0.118 | 0.107 | +0.033 | +0.022 | $3.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 14 | 0.189 | 0.176 | +0.041 | +0.027 | $4.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Noah Cates: 1+ goals YES | 12 | 0.155 | 0.145 | +0.028 | +0.018 | $3.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27CBJPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (15.19 vs 3.19 bp); relationships: KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27CBJPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: PHI offense suppressed (<= 2 goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (13.08 vs 12.53 bp); despite a smaller raw edge (+0.033 vs +0.041/contract); relationships: KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT27CBJPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLPTS-26OCT27CBJPHI-CBJCSILLINGER4-1|yes; why: higher confidence-adjusted growth (12.53 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT27CBJPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: CBJ offense suppressed (<= 2 goals)
- **Noah Cates: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27CBJPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (6.22 vs 3.19 bp); relationships: KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3066): highest fidelity KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.2481): highest fidelity KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.4691): highest fidelity KXNHLSPREAD-26OCT27CBJPHI-CBJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4307, phi -0.168)
- KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4691, phi -0.134)
- KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4691, phi -0.223)
- KXNHLGOAL-26OCT27CBJPHI-PHINCATES27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4307, phi -0.18)

portfolios: A EV +2.46 (adj +0.55) on $16.76, P(profit) 0.4895, adj growth 4.9 bp · B EV +4.59 (adj +3.07) on $14.36, P(profit) 0.4691, adj growth 27.9 bp · C EV +3.57 (adj +1.77) on $27.92, P(profit) 0.7255, adj growth 16.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ CAR  ·  10000 joint draws  ·  444 bet sides mapped, 16 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_BOS_win | p_overtime | goals | shots CAR/BOS | CAR/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.160 | 0.64 | 0.36 | 0.00 | 6.08 | 34.7/21.2 | 18.4/30.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.142 | 0.64 | 0.36 | 0.00 | 9.39 | 36.2/22.8 | 17.7/28.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.142 | 0.54 | 0.46 | 0.48 | 5.98 | 34.5/21.4 | 18.2/30.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.089 | 0.56 | 0.44 | 0.00 | 6.05 | 28.0/27.0 | 23.6/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.58 | 0.42 | 0.00 | 9.32 | 29.7/28.6 | 22.8/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.51 | 0.49 | 0.50 | 5.99 | 28.0/26.9 | 23.6/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pavel Zacha: 1+ goals YES | 21 | 0.278 | 0.258 | +0.056 | +0.036 | $6.90 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Mark Kastelic: 1+ goals YES | 7 | 0.110 | 0.097 | +0.035 | +0.023 | $3.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Casey Mittelstadt: 1+ goals YES | 13 | 0.181 | 0.166 | +0.043 | +0.028 | $4.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Jalen Chatfield: 1+ goals YES | 5 | 0.077 | 0.069 | +0.024 | +0.016 | $2.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | GAME:HIGH_EVENT | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT27BOSCAR-10|yes; why: higher confidence-adjusted growth (16.68 vs 9.79 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.926 vs 0.327); relationships: KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT27BOSCAR-CARJCHATFIELD5-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: BOS offense suppressed (<= 2 goals)
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes has the higher standalone adjusted growth (16.68 vs 15.95 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.022); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27BOSCAR-CARJCHATFIELD5-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: BOS offense suppressed (<= 2 goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes has the higher standalone adjusted growth (16.68 vs 13.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27BOSCAR-CARJCHATFIELD5-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: BOS offense suppressed (<= 2 goals)
- **Jalen Chatfield: 1+ goals YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT27BOSCAR-10|yes; why: higher confidence-adjusted growth (10.60 vs 9.79 bp); despite a smaller raw edge (+0.024 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.838 vs 0.327); relationships: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: CAR offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · high event (8+) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14.
- thesis BOS:OFFENSE_4PLUS (p 0.3773): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3267): highest fidelity KXNHLTOTAL-26OCT27BOSCAR-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:OFFENSE_4PLUS (p 0.4822): highest fidelity KXNHLTOTAL-26OCT27BOSCAR-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT27BOSCAR-10|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4034, phi -0.245)
- KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4034, phi -0.141)
- KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4034, phi -0.197)
- KXNHLGOAL-26OCT27BOSCAR-CARJCHATFIELD5-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:SUPPRESSED (p 0.3059, phi -0.106)

portfolios: A EV +2.70 (adj +1.15) on $16.76, P(profit) 0.5051, adj growth 10.5 bp · B EV +5.68 (adj +3.70) on $16.87, P(profit) 0.5146, adj growth 33.7 bp · C EV +5.01 (adj +2.26) on $29.03, P(profit) 0.6863, adj growth 20.4 bp · R EV +0.50 (adj +0.33) on $2.00, P(profit) 0.2775, adj growth 11.9 bp

## LAK @ CHI  ·  10000 joint draws  ·  410 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_LAK_win | p_overtime | goals | shots CHI/LAK | CHI/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.48 | 0.52 | 0.00 | 5.97 | 26.7/27.2 | 23.7/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.47 | 5.89 | 26.8/27.3 | 23.9/23.5 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.105 | 0.43 | 0.57 | 0.00 | 5.96 | 21.1/32.4 | 28.4/17.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.46 | 0.54 | 0.47 | 5.84 | 21.5/32.7 | 29.2/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.50 | 0.50 | 0.00 | 9.14 | 28.2/28.9 | 22.8/22.1 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.060 | 0.38 | 0.62 | 0.00 | 9.09 | 22.6/33.9 | 26.7/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.081 | 0.070 | +0.028 | +0.016 | $2.28 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 54 | 0.690 | 0.589 | +0.133 | +0.032 | $11.04 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Connor Bedard: 1+ assists NO | 53 | 0.622 | 0.574 | +0.075 | +0.026 | $7.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 52 | 0.601 | 0.556 | +0.064 | +0.018 | $7.04 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27LACHI-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (10.97 vs 0.03 bp); alternative not eligible: confidence-adjusted EV +0.0018 below the 0.010/contract floor; relationships: KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT27LACHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: LAK offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (9.04 vs 6.05 bp); relationships: KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT27LACHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.125); KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: CHI offense succeeds (4+ goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no; why: second expression of the same thesis: KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no has the higher standalone adjusted growth (9.04 vs 6.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.125); they share one thesis budget; relationships: KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.125); KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no; why: higher confidence-adjusted growth (2.91 vs 2.37 bp); despite a smaller raw edge (+0.064 vs +0.104/contract); relationships: KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT27LACHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:SUPPRESSED (p 0.4363): highest fidelity KXNHLAST-26OCT27LACHI-CHIAFRONDELL16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.4034): highest fidelity KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.3697): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4034, phi -0.138)
- KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.5 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3406, phi -0.253)
- KXNHLAST-26OCT27LACHI-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3406, phi -0.271)
- KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3697, phi -0.293)

portfolios: A EV +2.76 (adj +0.69) on $16.76, P(profit) 0.5816, adj growth 6.6 bp · B EV +5.69 (adj +1.93) on $27.99, P(profit) 0.6314, adj growth 17.7 bp · C EV +4.18 (adj +1.04) on $21.12, P(profit) 0.6901, adj growth 9.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MTL @ STL  ·  10000 joint draws  ·  432 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_MTL_win | p_overtime | goals | shots STL/MTL | STL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.59 | 0.41 | 0.00 | 6.05 | 26.8/26.7 | 23.6/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.53 | 0.47 | 0.47 | 5.96 | 27.1/27.1 | 23.8/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.63 | 0.37 | 0.00 | 9.39 | 28.7/28.3 | 22.8/21.6 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.079 | 0.68 | 0.32 | 0.00 | 6.05 | 31.8/21.3 | 18.6/27.3 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.55 | 0.45 | 0.44 | 5.96 | 31.8/21.4 | 18.1/28.3 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.060 | 0.73 | 0.27 | 0.00 | 9.33 | 33.4/22.7 | 18.2/25.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 25 | 0.296 | 0.283 | +0.033 | +0.020 | $4.07 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 14 | 0.177 | 0.161 | +0.029 | +0.013 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Connor McMichael: 1+ goals YES | 18 | 0.216 | 0.202 | +0.025 | +0.011 | $2.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 30 | 0.337 | 0.325 | +0.022 | +0.010 | $2.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes; why: higher confidence-adjusted growth (4.64 vs 2.90 bp); relationships: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT27MTLSTL-STLCMCMICHAEL77-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (4.64 vs 2.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.021); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT27MTLSTL-STLCMCMICHAEL77-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: STL offense suppressed (<= 2 goals)
- **Connor McMichael: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (4.64 vs 1.87 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (4.64 vs 1.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT27MTLSTL-STLCMCMICHAEL77-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4587): highest fidelity KXNHLAST-26OCT27MTLSTL-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3319, phi -0.24)
- KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3319, phi -0.207)
- KXNHLGOAL-26OCT27MTLSTL-STLCMCMICHAEL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3319, phi -0.197)
- KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3319, phi -0.267)

portfolios: A EV +2.42 (adj +0.94) on $15.92, P(profit) 0.5338, adj growth 8.2 bp · B EV +1.34 (adj +0.69) on $10.43, P(profit) 0.5392, adj growth 6.4 bp · C EV +0.60 (adj +0.37) on $4.75, P(profit) 0.2963, adj growth 3.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ NSH  ·  10000 joint draws  ·  418 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_NYI_win | p_overtime | goals | shots NSH/NYI | NSH/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.55 | 0.45 | 0.00 | 6.0 | 27.9/28.0 | 24.7/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.49 | 5.96 | 27.9/28.2 | 24.8/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.55 | 0.45 | 0.00 | 9.32 | 29.3/29.5 | 23.7/23.0 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.079 | 0.47 | 0.53 | 0.00 | 5.97 | 22.2/33.1 | 29.5/18.9 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.45 | 0.55 | 0.48 | 5.91 | 22.1/32.8 | 29.3/18.9 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.059 | 0.61 | 0.39 | 0.00 | 5.99 | 32.6/22.4 | 19.4/28.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mavrik Bourque: 1+ goals YES | 17 | 0.211 | 0.198 | +0.031 | +0.018 | $3.39 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 13 | 0.165 | 0.154 | +0.027 | +0.016 | $2.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 12 | 0.158 | 0.142 | +0.030 | +0.015 | $2.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 14 | 0.173 | 0.164 | +0.025 | +0.015 | $2.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (5.04 vs 4.47 bp); relationships: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT27NYINSH-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: NSH offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NYINSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (4.47 vs 2.07 bp); relationships: KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT27NYINSH-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: NSH offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NYINSH-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (4.08 vs 0.76 bp); alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT27NYINSH-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: NYI offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NYINSH-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (4.05 vs 0.76 bp); alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:OFFENSE_4PLUS (p 0.4144): highest fidelity KXNHLAST-26OCT27NYINSH-NSHJMARCHESSAULT81-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:SUPPRESSED (p 0.3987): highest fidelity KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.381): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3697, phi -0.193)
- KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3697, phi -0.2)
- KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3987, phi -0.192)
- KXNHLGOAL-26OCT27NYINSH-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3987, phi -0.186)

portfolios: A EV +2.75 (adj +0.94) on $16.76, P(profit) 0.5214, adj growth 8.5 bp · B EV +2.13 (adj +1.21) on $11.15, P(profit) 0.546, adj growth 11.0 bp · C EV +1.83 (adj +0.54) on $13.41, P(profit) 0.8326, adj growth 4.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ DAL  ·  10000 joint draws  ·  426 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NJD_win | p_overtime | goals | shots DAL/NJD | DAL/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.59 | 0.41 | 0.00 | 6.02 | 26.8/26.9 | 23.8/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.48 | 5.9 | 26.9/26.9 | 23.6/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.60 | 0.40 | 0.00 | 9.16 | 28.0/28.1 | 22.7/21.7 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.075 | 0.51 | 0.49 | 0.00 | 5.99 | 21.2/31.7 | 28.0/17.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.48 | 0.52 | 0.48 | 5.86 | 21.6/31.9 | 28.4/18.4 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.065 | 0.69 | 0.31 | 0.00 | 5.94 | 31.0/21.0 | 18.4/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Brown: 1+ goals YES | 11 | 0.169 | 0.153 | +0.052 | +0.036 | $5.94 | FUNDED_RESEARCH | $2 | NJD:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Amadeus Lombardi: 1+ goals YES | 9 | 0.125 | 0.111 | +0.029 | +0.015 | $2.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jamie Benn: 1+ goals YES | 13 | 0.165 | 0.154 | +0.027 | +0.016 | $2.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ assists NO | 56 | 0.630 | 0.593 | +0.053 | +0.015 | $8.38 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Connor Brown: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NJDAL-NJJSIEGENTHALER71-1|yes; why: higher confidence-adjusted growth (26.74 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: NJD offense suppressed (<= 2 goals)
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NJDAL-NJJSIEGENTHALER71-1|yes; why: higher confidence-adjusted growth (5.92 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.036); failure: NJD offense suppressed (<= 2 goals)
- **Jamie Benn: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes; why: higher confidence-adjusted growth (4.47 vs 3.90 bp); despite a smaller raw edge (+0.027 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.019); failure: DAL offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27NJDAL-NJLEVANGELISTA77-1|no; why: KXNHLAST-26OCT27NJDAL-NJLEVANGELISTA77-1|no has the higher standalone adjusted growth (3.11 vs 2.14 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.068); relationships: KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.117); KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis DAL:OFFENSE_4PLUS (p 0.393): highest fidelity KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes (same contract)
- thesis NJD:SUPPRESSED (p 0.4636): highest fidelity KXNHLAST-26OCT27NJDAL-NJLEVANGELISTA77-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27NJDAL-NJLEVANGELISTA77-1|no (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.3209): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4636, phi -0.215)
- KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4636, phi -0.185)
- KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.38, phi -0.178)
- KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3209, phi -0.279)

portfolios: A EV +3.20 (adj +1.50) on $16.76, P(profit) 0.4857, adj growth 14.2 bp · B EV +4.68 (adj +2.76) on $19.44, P(profit) 0.352, adj growth 25.1 bp · C EV +2.45 (adj +0.61) on $17.85, P(profit) 0.3268, adj growth 5.6 bp · R EV +0.89 (adj +0.62) on $2.00, P(profit) 0.1689, adj growth 21.5 bp

## FLA @ WPG  ·  10000 joint draws  ·  440 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_FLA_win | p_overtime | goals | shots WPG/FLA | WPG/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.56 | 0.44 | 0.00 | 6.01 | 26.8/26.7 | 23.4/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.46 | 5.89 | 26.6/27.0 | 23.6/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.54 | 0.46 | 0.00 | 9.24 | 28.3/28.3 | 22.6/22.1 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.075 | 0.48 | 0.52 | 0.00 | 6.01 | 21.5/31.9 | 28.1/18.2 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.49 | 0.51 | 0.47 | 5.9 | 21.5/31.5 | 28.1/18.3 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.060 | 0.62 | 0.38 | 0.00 | 5.96 | 31.4/21.3 | 18.5/27.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Seth Jones: 1+ assists NO | 55 | 0.641 | 0.593 | +0.074 | +0.026 | $6.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | FLA:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Sam Reinhart: 1+ goals NO | 69 | 0.739 | 0.724 | +0.034 | +0.019 | $6.89 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 29 | 0.338 | 0.323 | +0.033 | +0.019 | $4.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ assists NO | 63 | 0.707 | 0.664 | +0.061 | +0.017 | $5.44 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Seth Jones: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no; why: higher confidence-adjusted growth (5.88 vs 3.90 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: REINFORCING (phi 0.17); KXNHLGOAL-26OCT27FLAWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.132); failure: FLA offense succeeds (4+ goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no; why: second expression of the same thesis: KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no has the higher standalone adjusted growth (5.88 vs 3.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.170); they share one thesis budget; relationships: KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no: REINFORCING (phi 0.17); KXNHLGOAL-26OCT27FLAWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: FLA offense succeeds (4+ goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27FLAWPG-FLA2|no; why: higher confidence-adjusted growth (3.63 vs 1.51 bp); despite a smaller raw edge (+0.033 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: WPG offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no; why: second expression of the same thesis: KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no has the higher standalone adjusted growth (5.88 vs 2.87 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.132); they share one thesis budget; relationships: KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT27FLAWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis FLA:SUPPRESSED (p 0.4362): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA2|no [DIRECT], best adjusted EV KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.5296): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3886): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27FLAWPG-WPGMSCHEIFELE55-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3474, phi -0.279)
- KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3474, phi -0.249)
- KXNHLGOAL-26OCT27FLAWPG-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3842, phi -0.255)
- KXNHLAST-26OCT27FLAWPG-FLASREINHART13-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3474, phi -0.245)

portfolios: A EV +1.40 (adj +0.49) on $16.76, P(profit) 0.654, adj growth 4.6 bp · B EV +2.10 (adj +0.87) on $22.67, P(profit) 0.5481, adj growth 8.1 bp · C EV +1.92 (adj +0.78) on $15.56, P(profit) 0.641, adj growth 7.1 bp · R EV +0.10 (adj +0.05) on $2.00, P(profit) 0.7389, adj growth 2.1 bp

## MIN @ UTA  ·  10000 joint draws  ·  426 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_MIN_win | p_overtime | goals | shots UTA/MIN | UTA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.59 | 0.41 | 0.00 | 6.05 | 28.4/28.4 | 25.2/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.44 | 5.97 | 27.8/27.9 | 24.6/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.59 | 0.41 | 0.00 | 9.3 | 29.8/29.6 | 24.2/22.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.084 | 0.65 | 0.35 | 0.00 | 6.01 | 33.4/22.5 | 19.7/29.0 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.57 | 0.43 | 0.46 | 5.93 | 33.4/22.6 | 19.5/29.9 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.059 | 0.67 | 0.33 | 0.00 | 9.26 | 34.8/23.8 | 19.0/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Daniil But: 1+ goals YES | 10 | 0.128 | 0.120 | +0.021 | +0.013 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 12 | 0.155 | 0.141 | +0.028 | +0.014 | $2.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 19 | 0.232 | 0.216 | +0.031 | +0.016 | $2.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 59 | 0.634 | 0.620 | +0.028 | +0.013 | $5.00 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Daniil But: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27MINUTA-MIN2|no; why: higher confidence-adjusted growth (4.02 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: UTA offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27MINUTA-MIN2|no; why: higher confidence-adjusted growth (3.82 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27MINUTA-UTADBUT19-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: UTA offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27MINUTA-MIN2|no; why: higher confidence-adjusted growth (3.35 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27MINUTA-UTADBUT19-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: UTA offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no; why: Player prop expression KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.81 vs 0.69 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27MINUTA-UTADBUT19-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:SUPPRESSED (p 0.4275): highest fidelity KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no — Player prop expression KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.81 vs 0.69 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis UTA:OFFENSE_4PLUS (p 0.4538): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27MINUTA-UTADBUT19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3298, phi -0.153)
- KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3298, phi -0.153)
- KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3298, phi -0.195)
- KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3567, phi -0.311)
- override: Player prop expression KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.81 vs 0.69 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.34 (adj +0.87) on $16.76, P(profit) 0.5228, adj growth 7.9 bp · B EV +1.60 (adj +0.85) on $12.29, P(profit) 0.4338, adj growth 7.8 bp · C EV +1.01 (adj +0.31) on $6.15, P(profit) 0.485, adj growth 2.8 bp · R EV +0.09 (adj +0.04) on $2.00, P(profit) 0.6345, adj growth 1.5 bp

## OTT @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_OTT_win | p_overtime | goals | shots VGK/OTT | VGK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.63 | 0.37 | 0.00 | 6.05 | 26.7/26.6 | 23.6/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.46 | 5.88 | 26.7/26.7 | 23.5/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.63 | 0.37 | 0.00 | 9.34 | 28.2/28.2 | 22.8/21.2 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.078 | 0.70 | 0.30 | 0.00 | 6.03 | 31.0/20.9 | 18.2/26.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.57 | 0.43 | 0.45 | 5.89 | 31.4/21.1 | 17.9/27.9 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.061 | 0.56 | 0.44 | 0.00 | 5.94 | 21.3/31.6 | 28.2/17.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_VAN_win | p_overtime | goals | shots ANA/VAN | ANA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.148 | 0.66 | 0.34 | 0.00 | 6.06 | 34.1/21.4 | 18.7/29.6 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.140 | 0.71 | 0.29 | 0.00 | 9.53 | 35.9/22.8 | 18.1/27.3 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.54 | 0.46 | 0.48 | 5.99 | 34.5/21.6 | 18.4/30.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.64 | 0.36 | 0.00 | 6.09 | 28.0/27.0 | 24.1/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.61 | 0.39 | 0.00 | 9.52 | 29.7/28.7 | 23.0/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.50 | 0.50 | 0.47 | 5.94 | 28.1/27.3 | 24.1/24.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.15, ANA shot control · high event (8+) · decided (2+) 0.14, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.12.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_BUF_win | p_overtime | goals | shots SJS/BUF | SJS/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.56 | 0.44 | 0.00 | 6.01 | 27.7/27.9 | 24.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.46 | 5.93 | 27.6/27.9 | 24.6/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.56 | 0.44 | 0.00 | 9.4 | 29.3/29.6 | 23.8/22.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.082 | 0.50 | 0.50 | 0.00 | 6.02 | 22.0/32.8 | 28.8/18.6 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.48 | 0.52 | 0.46 | 6.03 | 22.5/33.0 | 29.5/19.3 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.060 | 0.46 | 0.54 | 0.00 | 9.34 | 23.5/34.4 | 27.7/18.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Buffalo wins by over 2.5 goals NO | 77 | 0.837 | 0.801 | +0.054 | +0.018 | $11.76 | FUNDED_RESEARCH | $3 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| San Jose wins by over 1.5 goals YES | 25 | 0.317 | 0.281 | +0.054 | +0.018 | $2.33 | FUNDED_RESEARCH | $1 | SJS:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Buffalo wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes; why: higher confidence-adjusted growth (4.36 vs 3.55 bp); wins across more scripts (relative breadth 1.031 vs 0.525); relationships: KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: DUPLICATIVE (phi 0.301); failure: BUF wins by 2+
- **San Jose wins by over 1.5 goals YES** — thesis: SJS wins by 2+; alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no has the higher standalone adjusted growth (4.36 vs 3.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.301); they share one thesis budget; relationships: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: DUPLICATIVE (phi 0.301); failure: BUF wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:WINS (p 0.5311): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no (same contract)
- thesis SJS:WINS_BY_2PLUS (p 0.3168): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3858): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.266, phi -0.734)
- KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4689, phi -0.64)

portfolios: A EV +1.45 (adj +0.44) on $16.76, P(profit) 0.5812, adj growth 3.9 bp · B EV +1.29 (adj +0.43) on $14.09, P(profit) 0.8365, adj growth 4.0 bp · C EV +0.98 (adj +0.33) on $14.19, P(profit) 0.8365, adj growth 3.1 bp · R EV +0.41 (adj +0.14) on $4.00, P(profit) 0.3168, adj growth 5.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
