# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-27T18:23:49Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +22.26 | +7.31 | +21.37 | 0.760 | -16.24 | -26.01 | 68.47 |
| B thesis-diversified (joint) ← optimiser card | 146.23 | +21.74 | +11.69 | +19.81 | 0.727 | -21.06 | -30.76 | 110.80 |
| C best expression per thesis | 150.01 | +20.30 | +8.26 | +19.54 | 0.740 | -18.85 | -28.18 | 77.91 |
| R FUNDED research stakes | 19.00 | +1.78 | +1.08 | +1.27 | 0.603 | -5.01 | -7.62 | 0.00 |

## CBJ @ PHI  ·  10000 joint draws  ·  466 bet sides mapped, 13 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.483 / away 0.517

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
| Conor Garland: 1+ goals NO | 84 | 0.882 | 0.870 | +0.032 | +0.021 | $7.87 | FUNDED_RESEARCH | $2 | CBJ:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 8 | 0.115 | 0.101 | +0.030 | +0.016 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Noah Cates: 1+ goals YES | 12 | 0.156 | 0.146 | +0.029 | +0.018 | $1.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no; why: higher confidence-adjusted growth (7.42 vs 2.77 bp); despite a smaller raw edge (+0.032 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27CBJPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: CBJ offense succeeds (4+ goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (7.27 vs 4.38 bp); relationships: KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27CBJPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: CBJ offense suppressed (<= 2 goals)
- **Noah Cates: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no; why: higher confidence-adjusted growth (6.48 vs 2.77 bp); despite a smaller raw edge (+0.029 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3118): highest fidelity KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3647): highest fidelity KXNHLSPREAD-26OCT27CBJPHI-CBJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:SUPPRESSED (p 0.4704): highest fidelity KXNHLSPREAD-26OCT27CBJPHI-CBJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3118, phi -0.155)
- KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4704, phi -0.172)
- KXNHLGOAL-26OCT27CBJPHI-PHINCATES27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4173, phi -0.188)

portfolios: A EV +1.26 (adj +0.36) on $13.64, P(profit) 0.6146, adj growth 3.4 bp · B EV +1.25 (adj +0.75) on $11.26, P(profit) 0.2526, adj growth 7.1 bp · C EV +1.09 (adj +0.47) on $11.65, P(profit) 0.8444, adj growth 4.4 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.8818, adj growth 1.9 bp

## BOS @ CAR  ·  10000 joint draws  ·  460 bet sides mapped, 14 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.629 / away 0.371

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_BOS_win | p_overtime | goals | shots CAR/BOS | CAR/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.165 | 0.61 | 0.39 | 0.00 | 6.07 | 34.5/21.2 | 18.2/30.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.142 | 0.54 | 0.46 | 0.44 | 5.99 | 34.8/21.7 | 18.5/31.1 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.138 | 0.68 | 0.32 | 0.00 | 9.46 | 36.3/22.7 | 17.7/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.080 | 0.58 | 0.42 | 0.00 | 6.07 | 27.7/26.6 | 23.4/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.49 | 0.51 | 0.46 | 6.01 | 28.3/27.2 | 23.7/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.56 | 0.44 | 0.00 | 9.4 | 29.7/28.7 | 23.1/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pavel Zacha: 1+ goals YES | 21 | 0.277 | 0.259 | +0.055 | +0.037 | $4.47 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Casey Mittelstadt: 1+ goals YES | 13 | 0.185 | 0.166 | +0.047 | +0.028 | $2.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Mark Kastelic: 1+ goals YES | 7 | 0.106 | 0.096 | +0.031 | +0.021 | $2.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT27BOSCAR-10|yes; why: higher confidence-adjusted growth (17.41 vs 3.29 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.935 vs 0.324); relationships: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: BOS offense suppressed (<= 2 goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes has the higher standalone adjusted growth (17.41 vs 14.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: BOS offense suppressed (<= 2 goals)
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes has the higher standalone adjusted growth (17.41 vs 13.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.14.
- thesis BOS:OFFENSE_4PLUS (p 0.3761): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:OFFENSE_4PLUS (p 0.4764): highest fidelity KXNHLAST-26OCT27BOSCAR-CARKMILLER19-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT27BOSCAR-CARKMILLER19-1|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.3188): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3979, phi -0.229)
- KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3979, phi -0.184)
- KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3979, phi -0.133)

portfolios: A EV +2.07 (adj +0.57) on $13.64, P(profit) 0.558, adj growth 5.2 bp · B EV +2.97 (adj +1.93) on $9.44, P(profit) 0.4775, adj growth 18.2 bp · C EV +2.94 (adj +1.37) on $21.76, P(profit) 0.4199, adj growth 12.9 bp · R EV +0.50 (adj +0.34) on $2.00, P(profit) 0.2769, adj growth 12.2 bp

## LAK @ CHI  ·  10000 joint draws  ·  434 bet sides mapped, 5 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.487 / away 0.513

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_LAK_win | p_overtime | goals | shots CHI/LAK | CHI/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.49 | 0.51 | 0.00 | 6.0 | 26.8/27.4 | 23.8/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.45 | 5.91 | 26.7/27.3 | 24.0/23.5 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.108 | 0.43 | 0.57 | 0.00 | 5.93 | 21.1/32.3 | 28.3/18.1 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.48 | 0.52 | 0.47 | 5.82 | 21.5/32.8 | 29.4/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.068 | 0.48 | 0.52 | 0.00 | 9.27 | 28.3/28.8 | 22.6/22.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.48 | 0.52 | 0.00 | 3.43 | 25.9/26.0 | 24.0/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Patrick Kane: 1+ assists NO | 55 | 0.700 | 0.596 | +0.133 | +0.029 | $5.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Roman Kantserov: 1+ goals NO | 74 | 0.794 | 0.778 | +0.041 | +0.025 | $6.70 | FUNDED_RESEARCH | $2 | CHI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Erik Gustafsson: 1+ assists NO | 61 | 0.733 | 0.650 | +0.107 | +0.023 | $6.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no; why: higher confidence-adjusted growth (7.40 vs 7.37 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: REINFORCING (phi 0.197); KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: CHI offense succeeds (4+ goals)
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no; why: second expression of the same thesis: KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no has the higher standalone adjusted growth (7.40 vs 7.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.197); they share one thesis budget; relationships: KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: REINFORCING (phi 0.197); KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: CHI offense succeeds (4+ goals)
- **Erik Gustafsson: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-LAQBYFIELD55-1|no; why: higher confidence-adjusted growth (5.09 vs 0.32 bp); alternative not eligible: confidence-adjusted EV +0.0055 below the 0.010/contract floor; relationships: KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:SUPPRESSED (p 0.4409): highest fidelity KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.4112): highest fidelity KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.3641): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.0 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3456, phi -0.241)
- KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3456, phi -0.196)
- KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.8 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3641, phi -0.203)

portfolios: A EV +1.68 (adj +0.48) on $13.64, P(profit) 0.7623, adj growth 4.7 bp · B EV +2.60 (adj +0.71) on $17.88, P(profit) 0.8214, adj growth 6.8 bp · C EV +3.40 (adj +0.74) on $16.74, P(profit) 0.5107, adj growth 7.0 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.7945, adj growth 2.6 bp

## MTL @ STL  ·  10000 joint draws  ·  456 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.512 / away 0.488

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
| Pius Suter: 1+ goals YES | 14 | 0.187 | 0.169 | +0.038 | +0.020 | $2.10 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 30 | 0.357 | 0.340 | +0.042 | +0.025 | $3.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 26 | 0.306 | 0.291 | +0.032 | +0.017 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Oliver Kapanen: 1+ assists NO | 71 | 0.776 | 0.741 | +0.052 | +0.016 | $5.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (7.07 vs 6.43 bp); despite a smaller raw edge (+0.038 vs +0.042/contract); relationships: KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26OCT27MTLSTL-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes has the higher standalone adjusted growth (7.07 vs 6.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT27MTLSTL-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi 0.028); failure: STL offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes has the higher standalone adjusted growth (7.07 vs 3.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT27MTLSTL-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: STL offense suppressed (<= 2 goals)
- **Oliver Kapanen: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT27MTLSTL-MTL2|no; why: KXNHLSPREAD-26OCT27MTLSTL-MTL2|no has the higher standalone adjusted growth (3.66 vs 2.85 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.152); relationships: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4648): highest fidelity KXNHLSPREAD-26OCT27MTLSTL-MTL2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.573): highest fidelity KXNHLSPREAD-26OCT27MTLSTL-MTL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27MTLSTL-MTL2|no (same contract)
- thesis MTL:SUPPRESSED (p 0.4187): highest fidelity KXNHLSPREAD-26OCT27MTLSTL-MTL2|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT27MTLSTL-MTL2|no (same contract)
- KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3177, phi -0.19)
- KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3177, phi -0.269)
- KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3177, phi -0.245)
- KXNHLAST-26OCT27MTLSTL-MTLOKAPANEN91-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3629, phi -0.207)

portfolios: A EV +1.81 (adj +0.43) on $13.64, P(profit) 0.5771, adj growth 4.0 bp · B EV +1.68 (adj +0.83) on $13.70, P(profit) 0.5549, adj growth 7.9 bp · C EV +1.14 (adj +0.49) on $9.39, P(profit) 0.8011, adj growth 4.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ NSH  ·  10000 joint draws  ·  442 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.524 / away 0.476

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_NYI_win | p_overtime | goals | shots NSH/NYI | NSH/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.54 | 0.46 | 0.00 | 5.97 | 28.0/28.0 | 24.6/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.48 | 5.95 | 27.8/28.0 | 24.7/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.52 | 0.48 | 0.00 | 9.35 | 29.2/29.6 | 23.7/22.7 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.083 | 0.47 | 0.53 | 0.00 | 5.98 | 22.0/33.0 | 29.3/18.8 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.48 | 0.52 | 0.49 | 5.93 | 22.5/33.4 | 29.8/19.3 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.056 | 0.60 | 0.40 | 0.00 | 6.0 | 32.6/22.3 | 19.4/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Edstrom: 1+ goals YES | 13 | 0.174 | 0.162 | +0.036 | +0.024 | $2.45 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:WINS_BY_2PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ assists NO | 72 | 0.799 | 0.757 | +0.065 | +0.023 | $7.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Mavrik Bourque: 1+ goals YES | 17 | 0.208 | 0.198 | +0.029 | +0.018 | $1.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 12 | 0.154 | 0.138 | +0.027 | +0.011 | $1.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Adam Edstrom: 1+ goals YES** — thesis: NSH wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT27NYINSH-NSH4|yes; why: higher confidence-adjusted growth (10.08 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: NSH offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27NYINSH-NYIMSCHAEFER48-1|no; why: higher confidence-adjusted growth (5.96 vs 1.64 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.061); failure: NYI offense succeeds (4+ goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (10.08 vs 4.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: NSH offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT27NYINSH-8|yes; why: higher confidence-adjusted growth (2.23 vs 1.56 bp); despite a smaller raw edge (+0.027 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.906 vs 0.33); relationships: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.061); KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NSH:WINS_BY_2PLUS (p 0.3009): highest fidelity KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.4139): highest fidelity KXNHLTOTAL-26OCT27NYINSH-8|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:SUPPRESSED (p 0.3992): highest fidelity KXNHLGOAL-26OCT27NYINSH-NYIMSCHAEFER48-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3694, phi -0.198)
- KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.3855, phi -0.216)
- KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3694, phi -0.198)
- KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3992, phi -0.175)

portfolios: A EV +2.35 (adj +0.63) on $13.64, P(profit) 0.5646, adj growth 5.6 bp · B EV +1.90 (adj +0.96) on $13.49, P(profit) 0.3913, adj growth 9.1 bp · C EV +1.79 (adj +0.83) on $13.47, P(profit) 0.328, adj growth 7.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ DAL  ·  10000 joint draws  ·  498 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.510 / away 0.490

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
| Nils Lundkvist: 1+ goals YES | 3 | 0.057 | 0.050 | +0.025 | +0.018 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Connor Brown: 1+ goals YES | 11 | 0.159 | 0.143 | +0.043 | +0.026 | $2.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Roope Hintz: 1+ goals YES | 26 | 0.305 | 0.293 | +0.032 | +0.019 | $2.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 68 | 0.723 | 0.711 | +0.028 | +0.016 | $5.11 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Nils Lundkvist: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes; why: higher confidence-adjusted growth (21.30 vs 4.03 bp); despite a smaller raw edge (+0.025 vs +0.032/contract); relationships: KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: DAL offense suppressed (<= 2 goals)
- **Connor Brown: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT27NJDAL-NJCGLASS12-1|yes; why: higher confidence-adjusted growth (14.49 vs 0.00 bp); despite a smaller raw edge (+0.043 vs +0.068/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NJDAL-DALNLUNDKVIST5-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: NJD offense suppressed (<= 2 goals)
- **Roope Hintz: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes; why: higher confidence-adjusted growth (4.03 vs 3.92 bp); despite a smaller raw edge (+0.032 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27NJDAL-DALNLUNDKVIST5-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: DAL offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27NJDAL-DALNLUNDKVIST5-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.08.
- thesis DAL:OFFENSE_4PLUS (p 0.3866): highest fidelity KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes (same contract)
- thesis NJD:SUPPRESSED (p 0.4734): highest fidelity KXNHLAST-26OCT27NJDAL-NJLEVANGELISTA77-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NJD:OFFENSE_4PLUS (p 0.3148): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27NJDAL-DALNLUNDKVIST5-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3953, phi -0.11)
- KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4734, phi -0.201)
- KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3953, phi -0.264)
- KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3148, phi -0.254)
- override: Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.40 (adj +0.96) on $13.64, P(profit) 0.4752, adj growth 9.1 bp · B EV +2.61 (adj +1.73) on $11.78, P(profit) 0.3849, adj growth 16.2 bp · C EV +0.96 (adj +0.40) on $8.40, P(profit) 0.7395, adj growth 3.8 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.7228, adj growth 1.7 bp

## FLA @ WPG  ·  10000 joint draws  ·  440 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.457 / away 0.543

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
| Brady Tkachuk: 1+ goals NO | 65 | 0.720 | 0.701 | +0.054 | +0.035 | $5.23 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Seth Jones: 1+ assists NO | 55 | 0.640 | 0.593 | +0.073 | +0.025 | $2.88 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | FLA:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Sam Reinhart: 1+ goals NO | 68 | 0.730 | 0.716 | +0.035 | +0.021 | $3.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.118 | 0.107 | +0.022 | +0.011 | $1.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no; why: higher confidence-adjusted growth (12.40 vs 5.66 bp); despite a smaller raw edge (+0.054 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no: REINFORCING (phi 0.154); KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT27FLAWPG-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense succeeds (4+ goals)
- **Seth Jones: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no has the higher standalone adjusted growth (12.40 vs 5.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.154); they share one thesis budget; relationships: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: REINFORCING (phi 0.154); KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: REINFORCING (phi 0.176); KXNHLGOAL-26OCT27FLAWPG-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.047); failure: FLA offense succeeds (4+ goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no; why: Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no selected over broad KXNHLSPREAD-26OCT27FLAWPG-FLA3|no because adjusted EV is 0.8 pts higher while thesis capture is 0.82 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no: REINFORCING (phi 0.176); KXNHLGOAL-26OCT27FLAWPG-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT27FLAWPG-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (3.27 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.033/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis FLA:SUPPRESSED (p 0.4303): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.5261): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no — Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no selected over broad KXNHLSPREAD-26OCT27FLAWPG-FLA3|no because adjusted EV is 0.8 pts higher while thesis capture is 0.82 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis FLA:OFFENSE_4PLUS (p 0.3496): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3496, phi -0.241)
- KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3496, phi -0.265)
- KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3496, phi -0.26)
- KXNHLGOAL-26OCT27FLAWPG-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4303, phi -0.177)
- override: Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no selected over broad KXNHLSPREAD-26OCT27FLAWPG-FLA3|no because adjusted EV is 0.8 pts higher while thesis capture is 0.82 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.07 (adj +0.49) on $13.64, P(profit) 0.6905, adj growth 4.8 bp · B EV +1.25 (adj +0.66) on $12.99, P(profit) 0.5797, adj growth 6.4 bp · C EV +1.36 (adj +0.68) on $13.70, P(profit) 0.4941, adj growth 6.5 bp · R EV +0.16 (adj +0.11) on $2.00, P(profit) 0.7201, adj growth 4.1 bp

## MIN @ UTA  ·  10000 joint draws  ·  464 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.532 / away 0.468

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_MIN_win | p_overtime | goals | shots UTA/MIN | UTA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.59 | 0.41 | 0.00 | 6.05 | 28.2/28.2 | 25.0/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.46 | 5.95 | 28.2/27.9 | 24.6/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.59 | 0.41 | 0.00 | 9.34 | 29.7/29.7 | 24.1/23.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.078 | 0.65 | 0.35 | 0.00 | 6.01 | 33.3/22.4 | 19.6/28.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.55 | 0.45 | 0.48 | 5.91 | 33.5/22.5 | 19.4/30.2 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.059 | 0.65 | 0.35 | 0.00 | 9.34 | 35.3/23.9 | 19.1/27.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Olli Maatta: 1+ goals YES | 3 | 0.056 | 0.048 | +0.024 | +0.016 | $1.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 57 | 0.637 | 0.619 | +0.050 | +0.032 | $7.58 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Anders Lee: 1+ goals YES | 20 | 0.245 | 0.233 | +0.034 | +0.021 | $2.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ assists NO | 49 | 0.605 | 0.527 | +0.097 | +0.019 | $4.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT27MINUTA-3|yes; why: higher confidence-adjusted growth (17.39 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.897 vs 0.76); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT27MINUTA-MINKKAPRIZOV97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.063); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no; why: higher confidence-adjusted growth (9.31 vs 4.02 bp); despite a smaller raw edge (+0.050 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27MINUTA-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: MIN offense succeeds (4+ goals)
- **Anders Lee: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (5.95 vs 1.85 bp); relationships: KXNHLGOAL-26OCT27MINUTA-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: UTA offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no has the higher standalone adjusted growth (9.31 vs 3.27 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MINUTA-MINOMAATTA3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:SUPPRESSED (p 0.4306): highest fidelity KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.4519): highest fidelity KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.3532): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27MINUTA-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4306, phi -0.11)
- KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3532, phi -0.309)
- KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3355, phi -0.204)
- KXNHLAST-26OCT27MINUTA-MINKKAPRIZOV97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3532, phi -0.274)

portfolios: A EV +2.04 (adj +0.76) on $13.64, P(profit) 0.6621, adj growth 7.3 bp · B EV +2.89 (adj +1.53) on $15.70, P(profit) 0.5375, adj growth 14.4 bp · C EV +1.23 (adj +0.78) on $11.82, P(profit) 0.724, adj growth 7.4 bp · R EV +0.17 (adj +0.11) on $2.00, P(profit) 0.6373, adj growth 4.2 bp

## OTT @ VGK  ·  10000 joint draws  ·  452 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.590 / away 0.410

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
| Brayden McNabb: 1+ goals YES | 6 | 0.088 | 0.076 | +0.024 | +0.012 | $1.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Drake Batherson: 1+ goals NO | 69 | 0.735 | 0.722 | +0.030 | +0.018 | $5.82 | FUNDED_RESEARCH | $2 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ goals YES | 21 | 0.248 | 0.237 | +0.026 | +0.016 | $1.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ goals NO | 66 | 0.699 | 0.688 | +0.023 | +0.012 | $3.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (5.07 vs 3.05 bp); despite a smaller raw edge (+0.024 vs +0.026/contract); relationships: KXNHLGOAL-26OCT27OTTVGK-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: VGK offense suppressed (<= 2 goals)
- **Drake Batherson: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no; why: Player prop expression KXNHLGOAL-26OCT27OTTVGK-OTTDBATHERSON19-1|no selected over player prop KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.86 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: OTT offense succeeds (4+ goals)
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27OTTVGK-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (3.05 vs 0.00 bp); despite a smaller raw edge (+0.026 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0003 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27OTTVGK-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: VGK offense suppressed (<= 2 goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27OTTVGK-VGKMSTONE61-1|no; why: Player prop expression KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT27OTTVGK-VGKMSTONE61-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.86 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT27OTTVGK-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.4569): highest fidelity KXNHLGOAL-26OCT27OTTVGK-OTTDBATHERSON19-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no — Player prop expression KXNHLGOAL-26OCT27OTTVGK-OTTDBATHERSON19-1|no selected over player prop KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.86 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VGK:OFFENSE_4PLUS (p 0.4537): highest fidelity KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.33): highest fidelity KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no (same contract)
- KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.33, phi -0.122)
- KXNHLGOAL-26OCT27OTTVGK-OTTDBATHERSON19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3283, phi -0.222)
- KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.33, phi -0.218)
- KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4537, phi -0.223)
- override: Player prop expression KXNHLGOAL-26OCT27OTTVGK-OTTDBATHERSON19-1|no selected over player prop KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.86 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT27OTTVGK-VGKMSTONE61-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.86 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.39 (adj +0.32) on $13.64, P(profit) 0.6735, adj growth 3.1 bp · B EV +0.99 (adj +0.54) on $12.50, P(profit) 0.6483, adj growth 5.1 bp · C EV +1.67 (adj +0.51) on $13.89, P(profit) 0.6036, adj growth 4.8 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.7349, adj growth 1.9 bp

## VAN @ ANA  ·  10000 joint draws  ·  446 bet sides mapped, 5 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.653 / away 0.347

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
| Filip Chytil: 1+ goals YES | 18 | 0.238 | 0.220 | +0.048 | +0.029 | $3.33 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 12 | 0.162 | 0.149 | +0.035 | +0.022 | $2.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 17 | 0.213 | 0.200 | +0.034 | +0.020 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (12.05 vs 5.97 bp); relationships: KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (12.05 vs 9.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (12.05 vs 5.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.15, ANA shot control · high event (8+) · decided (2+) 0.14, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.12.
- thesis VAN:OFFENSE_4PLUS (p 0.3728): highest fidelity KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.5182): highest fidelity KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes (same contract)
- KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4102, phi -0.239)
- KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4102, phi -0.193)
- KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4102, phi -0.204)

portfolios: A EV +4.72 (adj +1.93) on $13.64, P(profit) 0.6305, adj growth 17.7 bp · B EV +1.86 (adj +1.15) on $7.80, P(profit) 0.4977, adj growth 10.9 bp · C EV +2.29 (adj +0.93) on $6.36, P(profit) 0.4404, adj growth 8.7 bp · R EV +0.25 (adj +0.15) on $1.00, P(profit) 0.2379, adj growth 5.8 bp

## BUF @ SJS  ·  10000 joint draws  ·  484 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.435 / away 0.565

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
| Adam Gaudette: 1+ goals YES | 13 | 0.177 | 0.161 | +0.040 | +0.023 | $1.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 62 | 0.682 | 0.665 | +0.046 | +0.029 | $5.89 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 1.5 goals NO | 65 | 0.734 | 0.690 | +0.068 | +0.024 | $5.07 | FUNDED_RESEARCH | $2 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ goals NO | 77 | 0.813 | 0.800 | +0.031 | +0.018 | $6.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no; why: higher confidence-adjusted growth (9.34 vs 6.64 bp); despite a smaller raw edge (+0.040 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLSPREAD-26OCT27BUFSJ-BUF2|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLGOAL-26OCT27BUFSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: SJS offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no; why: higher confidence-adjusted growth (7.89 vs 6.64 bp); despite a smaller raw edge (+0.046 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLSPREAD-26OCT27BUFSJ-BUF2|no: REINFORCING (phi 0.171); KXNHLGOAL-26OCT27BUFSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: BUF offense succeeds (4+ goals)
- **Buffalo wins by over 1.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no; why: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no has the higher standalone adjusted growth (6.64 vs 5.49 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.734); relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.139); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.171); KXNHLGOAL-26OCT27BUFSJ-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.12); failure: BUF wins by 2+
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (4.00 vs 0.97 bp); despite a smaller raw edge (+0.031 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSPREAD-26OCT27BUFSJ-BUF2|no: INTENTIONAL_DIVERSIFIER (phi -0.12); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4359): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3858): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS (p 0.5311): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no (same contract)
- KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3456, phi -0.199)
- KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3959, phi -0.249)
- KXNHLSPREAD-26OCT27BUFSJ-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.266, phi -1.0)
- KXNHLGOAL-26OCT27BUFSJ-SJISTENBERG41-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4359, phi -0.183)

portfolios: A EV +1.47 (adj +0.38) on $13.64, P(profit) 0.6984, adj growth 3.6 bp · B EV +1.73 (adj +0.90) on $19.69, P(profit) 0.5118, adj growth 8.6 bp · C EV +2.45 (adj +1.06) on $22.83, P(profit) 0.6586, adj growth 10.0 bp · R EV +0.35 (adj +0.16) on $4.00, P(profit) 0.5359, adj growth 6.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
