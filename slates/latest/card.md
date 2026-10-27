# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-27T14:47:19Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +24.24 | +8.60 | +22.65 | 0.731 | -22.24 | -33.56 | 79.07 |
| B thesis-diversified (joint) ← optimiser card | 149.03 | +24.29 | +13.11 | +21.66 | 0.713 | -24.31 | -35.32 | 123.18 |
| C best expression per thesis | 150.00 | +20.30 | +8.25 | +19.33 | 0.714 | -24.45 | -35.85 | 76.26 |
| R FUNDED research stakes | 19.00 | +2.42 | +1.48 | +0.67 | 0.514 | -6.89 | -8.30 | 0.00 |

## CBJ @ PHI  ·  10000 joint draws  ·  442 bet sides mapped, 15 +EV candidates, 4 on card


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
| Travis Sanheim: 1+ goals YES | 8 | 0.120 | 0.109 | +0.035 | +0.024 | $2.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 8 | 0.118 | 0.104 | +0.033 | +0.019 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Conor Garland: 1+ goals NO | 84 | 0.884 | 0.871 | +0.035 | +0.021 | $9.12 | FUNDED_RESEARCH | $3 | CBJ:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 15 | 0.189 | 0.178 | +0.030 | +0.019 | $2.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27CBJPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (15.19 vs 3.19 bp); relationships: KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: PHI offense suppressed (<= 2 goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (10.29 vs 5.93 bp); relationships: KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: CBJ offense suppressed (<= 2 goals)
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no; why: higher confidence-adjusted growth (7.94 vs 3.28 bp); despite a smaller raw edge (+0.035 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: CBJ offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLPTS-26OCT27CBJPHI-CBJCSILLINGER4-1|yes; why: higher confidence-adjusted growth (5.93 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3066): highest fidelity KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.2481): highest fidelity KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.4691): highest fidelity KXNHLSPREAD-26OCT27CBJPHI-CBJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4307, phi -0.168)
- KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4691, phi -0.134)
- KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3066, phi -0.147)
- KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4691, phi -0.223)

portfolios: A EV +2.02 (adj +0.51) on $13.73, P(profit) 0.4962, adj growth 4.7 bp · B EV +2.67 (adj +1.70) on $16.17, P(profit) 0.352, adj growth 16.0 bp · C EV +2.35 (adj +0.99) on $16.98, P(profit) 0.4793, adj growth 9.1 bp · R EV +0.12 (adj +0.08) on $3.00, P(profit) 0.8844, adj growth 2.9 bp

## BOS @ CAR  ·  10000 joint draws  ·  450 bet sides mapped, 13 +EV candidates, 4 on card


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
| Mark Kastelic: 1+ goals YES | 7 | 0.110 | 0.099 | +0.035 | +0.024 | $2.66 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Pavel Zacha: 1+ goals YES | 21 | 0.278 | 0.258 | +0.056 | +0.036 | $5.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Casey Mittelstadt: 1+ goals YES | 13 | 0.181 | 0.164 | +0.043 | +0.026 | $3.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Charlie McAvoy: 1+ assists NO | 57 | 0.632 | 0.599 | +0.045 | +0.011 | $6.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (17.71 vs 16.68 bp); despite a smaller raw edge (+0.035 vs +0.056/contract); relationships: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT27BOSCAR-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi -0.035); failure: BOS offense suppressed (<= 2 goals)
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT27BOSCAR-10|yes; why: higher confidence-adjusted growth (16.68 vs 9.79 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.926 vs 0.327); relationships: KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT27BOSCAR-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.159); failure: BOS offense suppressed (<= 2 goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes has the higher standalone adjusted growth (16.68 vs 12.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT27BOSCAR-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.068); failure: BOS offense suppressed (<= 2 goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27BOSCAR-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (1.18 vs 0.87 bp); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.159); KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.068); failure: BOS offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · high event (8+) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14.
- thesis BOS:OFFENSE_4PLUS (p 0.3773): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3267): highest fidelity KXNHLTOTAL-26OCT27BOSCAR-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:OFFENSE_4PLUS (p 0.4822): highest fidelity KXNHLTOTAL-26OCT27BOSCAR-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT27BOSCAR-10|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4034, phi -0.141)
- KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4034, phi -0.245)
- KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4034, phi -0.197)
- KXNHLAST-26OCT27BOSCAR-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3773, phi -0.268)

portfolios: A EV +2.98 (adj +1.23) on $13.73, P(profit) 0.5051, adj growth 10.8 bp · B EV +4.14 (adj +2.51) on $17.71, P(profit) 0.4765, adj growth 23.5 bp · C EV +4.02 (adj +1.86) on $22.17, P(profit) 0.5304, adj growth 17.1 bp · R EV +0.47 (adj +0.32) on $1.00, P(profit) 0.1098, adj growth 11.5 bp

## LAK @ CHI  ·  10000 joint draws  ·  428 bet sides mapped, 9 +EV candidates, 4 on card


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
| Roman Kantserov: 1+ goals NO | 72 | 0.787 | 0.769 | +0.052 | +0.035 | $7.75 | FUNDED_RESEARCH | $2 | CHI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.081 | 0.070 | +0.028 | +0.016 | $1.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 54 | 0.690 | 0.589 | +0.133 | +0.032 | $5.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 52 | 0.601 | 0.556 | +0.064 | +0.018 | $5.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (13.54 vs 9.04 bp); despite a smaller raw edge (+0.052 vs +0.133/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: REINFORCING (phi 0.277); KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: CHI offense succeeds (4+ goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27LACHI-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (10.97 vs 0.03 bp); alternative not eligible: confidence-adjusted EV +0.0018 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: LAK offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no has the higher standalone adjusted growth (13.54 vs 9.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.277); they share one thesis budget; relationships: KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: REINFORCING (phi 0.277); KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: CHI offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no; why: KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no has the higher standalone adjusted growth (3.44 vs 2.91 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.083); relationships: KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:SUPPRESSED (p 0.4363): highest fidelity KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no (same contract)
- thesis LAK:SUPPRESSED (p 0.4034): highest fidelity KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.3697): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3406, phi -0.196)
- KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4034, phi -0.138)
- KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.5 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3406, phi -0.253)
- KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3697, phi -0.293)

portfolios: A EV +2.20 (adj +0.53) on $13.73, P(profit) 0.5816, adj growth 5.1 bp · B EV +3.44 (adj +1.39) on $20.46, P(profit) 0.6268, adj growth 13.1 bp · C EV +2.32 (adj +0.84) on $20.83, P(profit) 0.5758, adj growth 7.9 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.7866, adj growth 3.7 bp

## MTL @ STL  ·  10000 joint draws  ·  452 bet sides mapped, 5 +EV candidates, 4 on card


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
| Robert Thomas: 1+ goals YES | 25 | 0.296 | 0.283 | +0.033 | +0.020 | $2.97 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 14 | 0.177 | 0.164 | +0.029 | +0.015 | $1.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Connor McMichael: 1+ goals YES | 18 | 0.216 | 0.204 | +0.025 | +0.014 | $1.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 30 | 0.337 | 0.326 | +0.022 | +0.012 | $1.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes; why: higher confidence-adjusted growth (4.64 vs 4.11 bp); relationships: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT27MTLSTL-STLCMCMICHAEL77-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (4.64 vs 4.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.021); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT27MTLSTL-STLCMCMICHAEL77-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: STL offense suppressed (<= 2 goals)
- **Connor McMichael: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (4.64 vs 2.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (4.64 vs 1.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT27MTLSTL-STLCMCMICHAEL77-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4587): highest fidelity KXNHLAST-26OCT27MTLSTL-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3319, phi -0.24)
- KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3319, phi -0.207)
- KXNHLGOAL-26OCT27MTLSTL-STLCMCMICHAEL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3319, phi -0.197)
- KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3319, phi -0.267)

portfolios: A EV +1.98 (adj +0.87) on $13.04, P(profit) 0.5338, adj growth 7.9 bp · B EV +1.10 (adj +0.62) on $8.49, P(profit) 0.5392, adj growth 5.9 bp · C EV +0.51 (adj +0.31) on $4.04, P(profit) 0.2963, adj growth 2.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ NSH  ·  10000 joint draws  ·  438 bet sides mapped, 8 +EV candidates, 4 on card


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
| Ondrej Palat: 1+ goals YES | 12 | 0.158 | 0.144 | +0.030 | +0.017 | $2.11 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 13 | 0.165 | 0.155 | +0.027 | +0.017 | $2.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 14 | 0.173 | 0.164 | +0.025 | +0.015 | $1.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ goals YES | 17 | 0.211 | 0.195 | +0.031 | +0.015 | $1.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NYINSH-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (5.60 vs 0.76 bp); alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT27NYINSH-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: NYI offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NYINSH-NSHJMARCHESSAULT81-1|yes; why: higher confidence-adjusted growth (5.21 vs 1.72 bp); despite a smaller raw edge (+0.027 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT27NYINSH-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NSH offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NYINSH-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (4.05 vs 0.76 bp); alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: NYI offense suppressed (<= 2 goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (5.21 vs 3.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27NYINSH-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:OFFENSE_4PLUS (p 0.4144): highest fidelity KXNHLAST-26OCT27NYINSH-NSHJMARCHESSAULT81-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:SUPPRESSED (p 0.3987): highest fidelity KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.381): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3987, phi -0.192)
- KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3697, phi -0.2)
- KXNHLGOAL-26OCT27NYINSH-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3987, phi -0.186)
- KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3697, phi -0.193)

portfolios: A EV +2.03 (adj +0.76) on $13.73, P(profit) 0.5214, adj growth 7.0 bp · B EV +1.58 (adj +0.91) on $8.16, P(profit) 0.546, adj growth 8.5 bp · C EV +1.24 (adj +0.51) on $11.93, P(profit) 0.8326, adj growth 4.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Connor Brown: 1+ goals YES | 11 | 0.169 | 0.153 | +0.052 | +0.036 | $4.36 | FUNDED_RESEARCH | $2 | NJD:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Amadeus Lombardi: 1+ goals YES | 9 | 0.125 | 0.112 | +0.029 | +0.017 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jamie Benn: 1+ goals YES | 13 | 0.165 | 0.154 | +0.027 | +0.016 | $1.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ assists NO | 56 | 0.630 | 0.593 | +0.053 | +0.015 | $6.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Connor Brown: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NJDAL-NJJSIEGENTHALER71-1|yes; why: higher confidence-adjusted growth (26.74 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: NJD offense suppressed (<= 2 goals)
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NJDAL-NJJSIEGENTHALER71-1|yes; why: higher confidence-adjusted growth (6.91 vs 0.00 bp); despite a smaller raw edge (+0.029 vs +0.031/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.036); failure: NJD offense suppressed (<= 2 goals)
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

portfolios: A EV +2.63 (adj +1.23) on $13.73, P(profit) 0.4857, adj growth 11.8 bp · B EV +3.48 (adj +2.07) on $14.42, P(profit) 0.352, adj growth 19.3 bp · C EV +2.08 (adj +0.52) on $15.17, P(profit) 0.3268, adj growth 4.8 bp · R EV +0.89 (adj +0.62) on $2.00, P(profit) 0.1689, adj growth 21.5 bp

## FLA @ WPG  ·  10000 joint draws  ·  440 bet sides mapped, 6 +EV candidates, 4 on card


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
| Sam Reinhart: 1+ goals NO | 68 | 0.739 | 0.723 | +0.044 | +0.028 | $7.04 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 66 | 0.717 | 0.702 | +0.042 | +0.026 | $6.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 14 | 0.172 | 0.161 | +0.024 | +0.012 | $1.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 30 | 0.338 | 0.327 | +0.023 | +0.012 | $1.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (7.97 vs 6.75 bp); relationships: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27FLAWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27FLAWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: FLA offense succeeds (4+ goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no; why: Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.84 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27FLAWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT27FLAWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: FLA offense succeeds (4+ goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27FLAWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (2.49 vs 1.52 bp); relationships: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT27FLAWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27FLAWPG-FLA2|no; why: higher confidence-adjusted growth (1.52 vs 1.51 bp); despite a smaller raw edge (+0.023 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT27FLAWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis FLA:SUPPRESSED (p 0.4362): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no — Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.84 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WPG:WINS (p 0.5296): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3886): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27FLAWPG-WPGMSCHEIFELE55-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3474, phi -0.249)
- KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3474, phi -0.236)
- KXNHLGOAL-26OCT27FLAWPG-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3842, phi -0.188)
- KXNHLGOAL-26OCT27FLAWPG-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3842, phi -0.255)
- override: Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.84 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.09 (adj +0.48) on $13.73, P(profit) 0.6547, adj growth 4.7 bp · B EV +1.24 (adj +0.74) on $17.21, P(profit) 0.597, adj growth 7.1 bp · C EV +1.79 (adj +0.86) on $20.65, P(profit) 0.5886, adj growth 8.0 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.7389, adj growth 3.1 bp

## MIN @ UTA  ·  10000 joint draws  ·  456 bet sides mapped, 6 +EV candidates, 4 on card


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
| Kirill Kaprizov: 1+ goals NO | 57 | 0.634 | 0.617 | +0.047 | +0.030 | $8.30 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 12 | 0.155 | 0.143 | +0.028 | +0.015 | $1.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Daniil But: 1+ goals YES | 10 | 0.128 | 0.120 | +0.021 | +0.013 | $1.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 19 | 0.232 | 0.216 | +0.031 | +0.016 | $2.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no; why: higher confidence-adjusted growth (8.13 vs 3.85 bp); despite a smaller raw edge (+0.047 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT27MINUTA-UTADBUT19-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: MIN offense succeeds (4+ goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27MINUTA-MIN2|no; why: higher confidence-adjusted growth (4.53 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT27MINUTA-UTADBUT19-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: UTA offense suppressed (<= 2 goals)
- **Daniil But: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27MINUTA-MIN2|no; why: higher confidence-adjusted growth (4.02 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: UTA offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27MINUTA-MIN2|no; why: higher confidence-adjusted growth (3.35 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27MINUTA-UTADBUT19-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:SUPPRESSED (p 0.4275): highest fidelity KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.4538): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3567, phi -0.311)
- KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3298, phi -0.153)
- KXNHLGOAL-26OCT27MINUTA-UTADBUT19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3298, phi -0.153)
- KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3298, phi -0.195)

portfolios: A EV +1.56 (adj +0.62) on $13.73, P(profit) 0.5187, adj growth 5.8 bp · B EV +1.71 (adj +1.00) on $13.78, P(profit) 0.7289, adj growth 9.4 bp · C EV +0.89 (adj +0.57) on $11.10, P(profit) 0.6345, adj growth 5.2 bp · R EV +0.24 (adj +0.15) on $3.00, P(profit) 0.6345, adj growth 5.6 bp

## OTT @ VGK  ·  10000 joint draws  ·  448 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_OTT_win | p_overtime | goals | shots VGK/OTT | VGK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.63 | 0.37 | 0.00 | 6.05 | 26.7/26.6 | 23.6/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.46 | 5.88 | 26.7/26.7 | 23.5/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.63 | 0.37 | 0.00 | 9.34 | 28.2/28.2 | 22.8/21.2 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.078 | 0.70 | 0.30 | 0.00 | 6.03 | 31.0/20.9 | 18.2/26.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.57 | 0.43 | 0.45 | 5.89 | 31.4/21.1 | 17.9/27.9 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.061 | 0.56 | 0.44 | 0.00 | 5.94 | 21.3/31.6 | 28.2/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivan Barbashev: 1+ goals YES | 20 | 0.248 | 0.235 | +0.037 | +0.024 | $3.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 59 | 0.712 | 0.626 | +0.105 | +0.019 | $5.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Jack Eichel: 1+ goals NO | 66 | 0.699 | 0.688 | +0.023 | +0.012 | $4.40 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Tim Stutzle: 1+ assists NO | 56 | 0.634 | 0.589 | +0.057 | +0.012 | $2.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27OTTVGK-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (7.17 vs 0.00 bp); despite a smaller raw edge (+0.037 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0003 below the 0.010/contract floor; relationships: KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT27OTTVGK-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: VGK offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27OTTVGK-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (3.41 vs 1.32 bp); relationships: KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT27OTTVGK-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.092); failure: OTT offense succeeds (4+ goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27OTTVGK-VGKMSTONE61-1|no; why: higher confidence-adjusted growth (1.53 vs 0.34 bp); despite a smaller raw edge (+0.023 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0062 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT27OTTVGK-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: VGK offense succeeds (4+ goals)
- **Tim Stutzle: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no; why: second expression of the same thesis: KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no has the higher standalone adjusted growth (3.41 vs 1.32 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.092); they share one thesis budget; relationships: KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.092); KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VGK:OFFENSE_4PLUS (p 0.4537): highest fidelity KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.4569): highest fidelity KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no (same contract)
- thesis VGK:SUPPRESSED (p 0.33): highest fidelity KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no (same contract)
- KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.33, phi -0.218)
- KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.2 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3283, phi -0.241)
- KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4537, phi -0.223)
- KXNHLAST-26OCT27OTTVGK-OTTTSTUTZLE18-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3283, phi -0.262)

portfolios: A EV +1.59 (adj +0.53) on $13.73, P(profit) 0.4932, adj growth 5.0 bp · B EV +2.02 (adj +0.69) on $16.42, P(profit) 0.4932, adj growth 6.5 bp · C EV +2.37 (adj +0.85) on $18.42, P(profit) 0.6259, adj growth 7.8 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.6991, adj growth 1.3 bp

## VAN @ ANA  ·  10000 joint draws  ·  382 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_VAN_win | p_overtime | goals | shots ANA/VAN | ANA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.148 | 0.66 | 0.34 | 0.00 | 6.06 | 34.1/21.4 | 18.7/29.6 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.140 | 0.71 | 0.29 | 0.00 | 9.53 | 35.9/22.8 | 18.1/27.3 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.54 | 0.46 | 0.48 | 5.99 | 34.5/21.6 | 18.4/30.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.64 | 0.36 | 0.00 | 6.09 | 28.0/27.0 | 24.1/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.61 | 0.39 | 0.00 | 9.52 | 29.7/28.7 | 23.0/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.50 | 0.50 | 0.47 | 5.94 | 28.1/27.3 | 24.1/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 2+ goals YES | 2 | 0.039 | 0.033 | +0.018 | +0.012 | $1.06 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.07) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ goals YES | 19 | 0.238 | 0.223 | +0.037 | +0.023 | $3.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 12 | 0.162 | 0.144 | +0.035 | +0.017 | $1.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.213 | 0.201 | +0.023 | +0.011 | $1.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 2+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (13.15 vs 4.00 bp); despite a smaller raw edge (+0.018 vs +0.091/contract); relationships: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: ANA offense suppressed (<= 2 goals)
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (6.93 vs 1.70 bp); relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (6.93 vs 5.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (6.93 vs 1.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.15, ANA shot control · high event (8+) · decided (2+) 0.14, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.12.
- thesis VAN:OFFENSE_4PLUS (p 0.3728): highest fidelity KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.5182): highest fidelity KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes (same contract)
- KXNHLGOAL-26OCT27VANANA-ANAAGREER18-2|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 93% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2819, phi -0.12)
- KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4102, phi -0.239)
- KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4102, phi -0.193)
- KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4102, phi -0.204)

portfolios: A EV +4.54 (adj +1.36) on $13.38, P(profit) 0.5339, adj growth 12.0 bp · B EV +2.14 (adj +1.26) on $7.50, P(profit) 0.3873, adj growth 11.7 bp · C EV +2.01 (adj +0.69) on $6.44, P(profit) 0.4419, adj growth 6.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ SJS  ·  10000 joint draws  ·  464 bet sides mapped, 6 +EV candidates, 3 on card


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
| Buffalo wins by over 1.5 goals NO | 66 | 0.734 | 0.695 | +0.058 | +0.019 | $1.95 | FUNDED_RESEARCH | $1 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo over 3.5 goals scored NO | 51 | 0.594 | 0.547 | +0.066 | +0.019 | $2.05 | FUNDED_RESEARCH | $1 | BUF:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 2.5 goals NO | 77 | 0.837 | 0.798 | +0.054 | +0.016 | $4.71 | FUNDED_RESEARCH | $2 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Buffalo wins by over 1.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF2|no; why: KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF2|no has the higher standalone adjusted growth (4.17 vs 3.54 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.283); relationships: KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4|no: REINFORCING (phi 0.526); KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: DUPLICATIVE (phi 0.734); failure: BUF wins by 2+
- **Buffalo over 3.5 goals scored NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF2|no; why: KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF2|no has the higher standalone adjusted growth (4.17 vs 3.27 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.389); relationships: KXNHLSPREAD-26OCT27BUFSJ-BUF2|no: REINFORCING (phi 0.526); KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: DUPLICATIVE (phi 0.466); failure: BUF offense succeeds (4+ goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF2|no; why: KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF2|no has the higher standalone adjusted growth (4.17 vs 3.25 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.208); relationships: KXNHLSPREAD-26OCT27BUFSJ-BUF2|no: DUPLICATIVE (phi 0.734); KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4|no: DUPLICATIVE (phi 0.466); failure: BUF wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:SUPPRESSED (p 0.3858): highest fidelity KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4|no (same contract)
- thesis SJS:WINS (p 0.5311): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS_BY_2PLUS (p 0.3168): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT27BUFSJ-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.266, phi -1.0)
- KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3959, phi -0.978)
- KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.266, phi -0.734)
- override: Broad expression KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes selected over broad KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF2|no because adjusted EV is 0.0 pts higher while thesis capture is 0.60 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.64 (adj +0.48) on $13.73, P(profit) 0.5804, adj growth 4.3 bp · B EV +0.75 (adj +0.22) on $8.71, P(profit) 0.7653, adj growth 2.1 bp · C EV +0.71 (adj +0.25) on $2.27, P(profit) 0.1811, adj growth 2.3 bp · R EV +0.35 (adj +0.10) on $4.00, P(profit) 0.7653, adj growth 3.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
