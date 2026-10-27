# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-27T23:43:21Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.93 | +8.36 | +26.61 | 0.784 | -16.68 | -28.13 | 77.51 |
| B thesis-diversified (joint) ← optimiser card | 149.11 | +27.61 | +14.41 | +25.85 | 0.744 | -22.34 | -35.41 | 136.06 |
| C best expression per thesis | 149.99 | +23.71 | +11.21 | +21.88 | 0.725 | -23.47 | -35.39 | 105.20 |
| R FUNDED research stakes | 18.00 | +2.54 | +1.69 | +2.02 | 0.554 | -7.68 | -9.93 | 0.00 |

## BOS @ CAR  ·  10000 joint draws  ·  460 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.629 / away 0.371

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_BOS_win | p_overtime | goals | shots CAR/BOS | CAR/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.165 | 0.64 | 0.36 | 0.00 | 6.03 | 34.3/21.2 | 18.4/30.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.140 | 0.54 | 0.46 | 0.47 | 5.97 | 34.7/21.3 | 18.1/31.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.139 | 0.61 | 0.39 | 0.00 | 9.46 | 36.1/22.8 | 17.6/28.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.082 | 0.56 | 0.43 | 0.00 | 6.1 | 28.2/27.1 | 23.7/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.52 | 0.48 | 0.51 | 6.0 | 28.3/27.3 | 23.8/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.59 | 0.41 | 0.00 | 9.39 | 29.7/28.4 | 22.6/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Casey Mittelstadt: 1+ goals YES | 12 | 0.183 | 0.166 | +0.056 | +0.039 | $4.23 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Pavel Zacha: 1+ goals YES | 21 | 0.276 | 0.256 | +0.055 | +0.034 | $4.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| William Borgen: 1+ goals YES | 4 | 0.063 | 0.056 | +0.020 | +0.013 | $1.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:WINS_BY_2PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Mark Kastelic: 1+ goals YES | 8 | 0.111 | 0.102 | +0.025 | +0.017 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (29.02 vs 14.85 bp); relationships: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27BOSCAR-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: BOS offense suppressed (<= 2 goals)
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes has the higher standalone adjusted growth (29.02 vs 14.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27BOSCAR-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: BOS offense suppressed (<= 2 goals)
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS5|yes; why: higher confidence-adjusted growth (8.86 vs 4.19 bp); despite a smaller raw edge (+0.020 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.838 vs 0.558); relationships: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CAR wins (incl. OT/SO)
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes has the higher standalone adjusted growth (29.02 vs 7.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27BOSCAR-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.14.
- thesis BOS:OFFENSE_4PLUS (p 0.3802): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:WINS_BY_2PLUS (p 0.2322): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes (same contract)
- thesis CAR:SUPPRESSED (p 0.3116): highest fidelity KXNHLAST-26OCT27BOSCAR-CARSJARVIS24-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27BOSCAR-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4015, phi -0.202)
- KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4015, phi -0.252)
- KXNHLGOAL-26OCT27BOSCAR-BOSWBORGEN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:WINS (p 0.5674, phi -0.146)
- KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4015, phi -0.152)

portfolios: A EV +3.01 (adj +1.45) on $15.00, P(profit) 0.4655, adj growth 13.4 bp · B EV +4.03 (adj +2.69) on $11.55, P(profit) 0.5092, adj growth 25.2 bp · C EV +4.13 (adj +2.36) on $19.90, P(profit) 0.6029, adj growth 22.0 bp · R EV +0.88 (adj +0.61) on $2.00, P(profit) 0.1835, adj growth 21.6 bp

## LAK @ CHI  ·  10000 joint draws  ·  436 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.503 / away 0.497

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_LAK_win | p_overtime | goals | shots CHI/LAK | CHI/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.50 | 0.50 | 0.00 | 5.96 | 26.9/27.5 | 23.9/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.48 | 5.84 | 27.0/27.3 | 24.1/23.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.102 | 0.42 | 0.58 | 0.00 | 5.96 | 21.3/32.6 | 28.5/18.3 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.47 | 0.53 | 0.49 | 5.83 | 21.1/32.4 | 29.1/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.47 | 0.53 | 0.00 | 9.2 | 28.1/28.7 | 22.6/22.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.49 | 0.51 | 0.00 | 3.44 | 25.3/26.0 | 24.0/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.075 | 0.068 | +0.022 | +0.015 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Roman Kantserov: 1+ goals NO | 74 | 0.796 | 0.781 | +0.042 | +0.027 | $7.62 | FUNDED_RESEARCH | $2 | CHI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 55 | 0.694 | 0.594 | +0.127 | +0.026 | $5.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 52 | 0.606 | 0.558 | +0.068 | +0.021 | $5.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLPTS-26OCT27LACHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (8.90 vs 0.08 bp); despite a smaller raw edge (+0.022 vs +0.093/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.093); failure: LAK offense suppressed (<= 2 goals)
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (8.75 vs 6.27 bp); despite a smaller raw edge (+0.042 vs +0.127/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: REINFORCING (phi 0.228); KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: CHI offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no has the higher standalone adjusted growth (8.75 vs 6.27 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.228); they share one thesis budget; relationships: KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: REINFORCING (phi 0.228); KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: CHI offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no; why: higher confidence-adjusted growth (3.69 vs 3.45 bp); despite a smaller raw edge (+0.068 vs +0.094/contract); relationships: KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.093); KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:SUPPRESSED (p 0.4354): highest fidelity KXNHLAST-26OCT27LACHI-CHICBEDARD98-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.4204): highest fidelity KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS_BY_2PLUS (p 0.2914): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4204, phi -0.142)
- KXNHLGOAL-26OCT27LACHI-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3391, phi -0.213)
- KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.4 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3391, phi -0.251)
- KXNHLAST-26OCT27LACHI-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3668, phi -0.291)

portfolios: A EV +2.41 (adj +0.52) on $15.00, P(profit) 0.5942, adj growth 5.0 bp · B EV +2.87 (adj +1.13) on $19.61, P(profit) 0.5297, adj growth 10.7 bp · C EV +1.25 (adj +0.56) on $15.28, P(profit) 0.4814, adj growth 5.4 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.7958, adj growth 2.8 bp

## MTL @ STL  ·  10000 joint draws  ·  484 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.489 / away 0.511

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
| Jimmy Snuggerud: 1+ goals YES | 28 | 0.357 | 0.336 | +0.062 | +0.042 | $5.75 | FUNDED_RESEARCH | $2 | STL:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
| Robert Thomas: 2+ goals YES | 3 | 0.056 | 0.048 | +0.024 | +0.016 | $1.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 24 | 0.306 | 0.288 | +0.053 | +0.035 | $3.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 14 | 0.187 | 0.172 | +0.038 | +0.024 | $2.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (18.48 vs 14.36 bp); relationships: KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-2|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: STL offense suppressed (<= 2 goals)
- **Robert Thomas: 2+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes has the higher standalone adjusted growth (18.48 vs 16.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: DUPLICATIVE (phi 0.365); KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: STL offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes has the higher standalone adjusted growth (18.48 vs 14.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-2|yes: DUPLICATIVE (phi 0.365); KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes has the higher standalone adjusted growth (18.48 vs 9.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-2|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4648): highest fidelity KXNHLTEAMTOTAL-26OCT27MTLSTL-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS_BY_2PLUS (p 0.3513): highest fidelity KXNHLSPREAD-26OCT27MTLSTL-STL2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.573): highest fidelity KXNHLSPREAD-26OCT27MTLSTL-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3177, phi -0.269)
- KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3177, phi -0.152)
- KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3177, phi -0.245)
- KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3177, phi -0.19)

portfolios: A EV +3.69 (adj +1.30) on $15.00, P(profit) 0.5496, adj growth 12.0 bp · B EV +3.34 (adj +2.22) on $12.69, P(profit) 0.6341, adj growth 20.9 bp · C EV +2.65 (adj +1.78) on $12.52, P(profit) 0.555, adj growth 16.6 bp · R EV +0.42 (adj +0.29) on $2.00, P(profit) 0.3566, adj growth 10.6 bp

## NYI @ NSH  ·  10000 joint draws  ·  438 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.524 / away 0.475

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_NYI_win | p_overtime | goals | shots NSH/NYI | NSH/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.54 | 0.46 | 0.00 | 6.07 | 27.8/27.9 | 24.5/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.49 | 5.95 | 28.0/28.2 | 24.8/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.55 | 0.45 | 0.00 | 9.34 | 29.5/29.7 | 23.7/22.9 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.080 | 0.48 | 0.52 | 0.00 | 5.99 | 21.9/33.0 | 29.1/18.5 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.49 | 0.51 | 0.50 | 5.95 | 22.3/33.3 | 29.8/19.1 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.057 | 0.58 | 0.42 | 0.00 | 5.97 | 32.3/22.1 | 19.2/28.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Wilsby: 1+ assists YES | 22 | 0.308 | 0.262 | +0.076 | +0.030 | $3.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
| Victor Eklund: 1+ assists NO | 72 | 0.797 | 0.756 | +0.063 | +0.022 | $8.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Victor Eklund: 1+ goals YES | 17 | 0.207 | 0.196 | +0.027 | +0.017 | $2.03 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 22 | 0.261 | 0.250 | +0.029 | +0.018 | $3.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Adam Wilsby: 1+ assists YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (10.71 vs 2.12 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT27NYINSH-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT27NYINSH-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: NSH offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT27NYINSH-NYIVEKLUND73-1|no; why: higher confidence-adjusted growth (5.38 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT27NYINSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT27NYINSH-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT27NYINSH-NYIBSCHENN10-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.236); failure: NYI offense succeeds (4+ goals)
- **Victor Eklund: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NYINSH-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (4.03 vs 3.79 bp); despite a smaller raw edge (+0.027 vs +0.029/contract); relationships: KXNHLAST-26OCT27NYINSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT27NYINSH-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: NYI offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NYINSH-NYIVEKLUND73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27NYINSH-NYIVEKLUND73-1|yes has the higher standalone adjusted growth (4.03 vs 3.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.014); they share one thesis budget; relationships: KXNHLAST-26OCT27NYINSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.236); KXNHLGOAL-26OCT27NYINSH-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.4175): highest fidelity KXNHLTOTAL-26OCT27NYINSH-6|yes [DIRECT], best adjusted EV KXNHLAST-26OCT27NYINSH-NSHAWILSBY2-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:SUPPRESSED (p 0.393): highest fidelity KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3804): highest fidelity KXNHLTOTAL-26OCT27NYINSH-6|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT27NYINSH-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT27NYINSH-NSHAWILSBY2-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3733, phi -0.243)
- KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.3804, phi -0.195)
- KXNHLGOAL-26OCT27NYINSH-NYIVEKLUND73-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.393, phi -0.209)
- KXNHLGOAL-26OCT27NYINSH-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.393, phi -0.245)

portfolios: A EV +2.45 (adj +0.82) on $15.00, P(profit) 0.5409, adj growth 7.6 bp · B EV +2.61 (adj +1.13) on $17.14, P(profit) 0.5, adj growth 10.8 bp · C EV +2.65 (adj +1.05) on $17.88, P(profit) 0.4111, adj growth 9.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ DAL  ·  10000 joint draws  ·  486 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.519 / away 0.481

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
| Amadeus Lombardi: 1+ goals YES | 9 | 0.123 | 0.114 | +0.028 | +0.018 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Roope Hintz: 1+ goals YES | 26 | 0.306 | 0.293 | +0.032 | +0.020 | $2.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 11 | 0.137 | 0.129 | +0.020 | +0.012 | $1.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 68 | 0.723 | 0.711 | +0.028 | +0.016 | $5.50 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT27NJDAL-NJCGLASS12-1|yes; why: higher confidence-adjusted growth (7.96 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.068/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT27NJDAL-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: NJD offense suppressed (<= 2 goals)
- **Roope Hintz: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes; why: higher confidence-adjusted growth (4.22 vs 3.54 bp); despite a smaller raw edge (+0.032 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT27NJDAL-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: DAL offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT27NJDAL-NJCGLASS12-1|yes; why: higher confidence-adjusted growth (3.21 vs 0.00 bp); despite a smaller raw edge (+0.020 vs +0.068/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: NJD offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27NJDAL-NJLEVANGELISTA77-1|no; why: Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJLEVANGELISTA77-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.85 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27NJDAL-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.08.
- thesis DAL:OFFENSE_4PLUS (p 0.3866): highest fidelity KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4734): highest fidelity KXNHLGOAL-26OCT27NJDAL-NJTMEIER28-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJLEVANGELISTA77-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.85 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NJD:OFFENSE_4PLUS (p 0.3148): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4734, phi -0.174)
- KXNHLGOAL-26OCT27NJDAL-DALRHINTZ24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3953, phi -0.265)
- KXNHLGOAL-26OCT27NJDAL-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4734, phi -0.176)
- KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3148, phi -0.254)
- override: Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJLEVANGELISTA77-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.85 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.92 (adj +0.57) on $15.00, P(profit) 0.4859, adj growth 5.3 bp · B EV +1.36 (adj +0.84) on $11.71, P(profit) 0.4151, adj growth 7.9 bp · C EV +0.63 (adj +0.37) on $9.55, P(profit) 0.3058, adj growth 3.5 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.7228, adj growth 1.7 bp

## FLA @ WPG  ·  10000 joint draws  ·  512 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.462 / away 0.538

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
| Brady Tkachuk: 1+ goals NO | 65 | 0.720 | 0.701 | +0.054 | +0.035 | $8.46 | FUNDED_RESEARCH | $3 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 13 | 0.172 | 0.160 | +0.034 | +0.022 | $2.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Adam Lowry: 1+ goals YES | 11 | 0.145 | 0.135 | +0.028 | +0.018 | $2.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.118 | 0.110 | +0.022 | +0.014 | $1.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no; why: higher confidence-adjusted growth (12.40 vs 8.24 bp); relationships: KXNHLGOAL-26OCT27FLAWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT27FLAWPG-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT27FLAWPG-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense succeeds (4+ goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27FLAWPG-FLA2|no; why: higher confidence-adjusted growth (8.79 vs 0.91 bp); despite a smaller raw edge (+0.034 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT27FLAWPG-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT27FLAWPG-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: WPG offense suppressed (<= 2 goals)
- **Adam Lowry: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27FLAWPG-FLA2|no; why: higher confidence-adjusted growth (6.87 vs 0.91 bp); despite a smaller raw edge (+0.028 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT27FLAWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT27FLAWPG-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: WPG offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT27FLAWPG-FLADKULIKOV7-1|yes; why: higher confidence-adjusted growth (4.84 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.035/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27FLAWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT27FLAWPG-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis FLA:SUPPRESSED (p 0.4303): highest fidelity KXNHLGOAL-26OCT27FLAWPG-FLAALUNDELL15-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3823): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis FLA:OFFENSE_4PLUS (p 0.3496): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3496, phi -0.241)
- KXNHLGOAL-26OCT27FLAWPG-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3987, phi -0.186)
- KXNHLGOAL-26OCT27FLAWPG-WPGALOWRY17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3987, phi -0.171)
- KXNHLGOAL-26OCT27FLAWPG-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4303, phi -0.177)

portfolios: A EV +1.27 (adj +0.50) on $15.00, P(profit) 0.6848, adj growth 4.8 bp · B EV +2.16 (adj +1.40) on $14.59, P(profit) 0.3772, adj growth 13.3 bp · C EV +0.79 (adj +0.52) on $9.74, P(profit) 0.7201, adj growth 5.0 bp · R EV +0.24 (adj +0.16) on $3.00, P(profit) 0.7201, adj growth 6.0 bp

## MIN @ UTA  ·  10000 joint draws  ·  464 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

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
| Kirill Kaprizov: 1+ goals NO | 56 | 0.642 | 0.620 | +0.065 | +0.043 | $8.46 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Anders Lee: 1+ goals YES | 20 | 0.245 | 0.233 | +0.034 | +0.021 | $2.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 12 | 0.156 | 0.145 | +0.029 | +0.017 | $1.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 19 | 0.235 | 0.221 | +0.034 | +0.021 | $2.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-2|no; why: higher confidence-adjusted growth (16.69 vs 6.61 bp); relationships: KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: MIN offense succeeds (4+ goals)
- **Anders Lee: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (6.03 vs 5.67 bp); despite a smaller raw edge (+0.034 vs +0.034/contract); relationships: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: UTA offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes has the higher standalone adjusted growth (6.03 vs 5.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: UTA offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes has the higher standalone adjusted growth (6.03 vs 5.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.4274): highest fidelity KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.4483): highest fidelity KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.3534): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3534, phi -0.298)
- KXNHLGOAL-26OCT27MINUTA-UTAALEE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3344, phi -0.214)
- KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3344, phi -0.166)
- KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3344, phi -0.211)

portfolios: A EV +2.56 (adj +0.74) on $15.00, P(profit) 0.5841, adj growth 7.0 bp · B EV +2.26 (adj +1.43) on $15.69, P(profit) 0.3751, adj growth 13.6 bp · C EV +1.61 (adj +1.05) on $12.94, P(profit) 0.7308, adj growth 10.0 bp · R EV +0.34 (adj +0.22) on $3.00, P(profit) 0.6421, adj growth 8.5 bp

## OTT @ VGK  ·  10000 joint draws  ·  468 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.590 / away 0.410

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
| Mitch Marner: 1+ assists NO | 46 | 0.607 | 0.508 | +0.130 | +0.031 | $6.86 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.086 | 0.078 | +0.022 | +0.014 | $1.48 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Jonas Johansson: 28+ saves NO | 61 | 0.773 | 0.647 | +0.146 | +0.020 | $7.74 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:NET_LOW_VOLUME | STRUCTURAL (1.00) | CALIBRATION_WARNING | D |
| Michael Amadio: 1+ goals YES | 13 | 0.161 | 0.152 | +0.023 | +0.014 | $1.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (8.38 vs 1.04 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no: INTENTIONAL_DIVERSIFIER (phi -0.054); KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: VGK offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (7.22 vs 1.83 bp); relationships: KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: VGK offense suppressed (<= 2 goals)
- **Jonas Johansson: 28+ saves NO** — thesis: OTT net faces light volume (<= 25 shots; VGK suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.054); KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: OTT net faces heavy volume (33+ shots; VGK pressure)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27OTTVGK-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (3.50 vs 0.62 bp); alternative not eligible: confidence-adjusted EV +0.0062 below the 0.010/contract floor; relationships: KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no: MOSTLY_INDEPENDENT (phi -0.022); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.3344): highest fidelity KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:NET_LOW_VOLUME (p 0.4375): highest fidelity KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3355): highest fidelity KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes (same contract)
- KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.2 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4477, phi -0.278)
- KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3344, phi -0.122)
- KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.8 pts; fragile player expression; opposing: failure thesis OTT:NET_HIGH_VOLUME (p 0.1648, phi -0.694)
- KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4484, phi -0.214)

portfolios: A EV +2.73 (adj +0.53) on $15.00, P(profit) 0.7329, adj growth 5.2 bp · B EV +4.45 (adj +1.19) on $17.70, P(profit) 0.5776, adj growth 11.2 bp · C EV +4.70 (adj +1.08) on $20.48, P(profit) 0.6343, adj growth 10.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ ANA  ·  10000 joint draws  ·  458 bet sides mapped, 7 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

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
| Filip Chytil: 1+ goals YES | 18 | 0.234 | 0.220 | +0.044 | +0.029 | $3.58 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| A.J. Greer: 1+ goals YES | 17 | 0.269 | 0.202 | +0.089 | +0.022 | $1.38 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 17 | 0.212 | 0.199 | +0.032 | +0.019 | $2.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (11.95 vs 5.20 bp); relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27VANANA-ANATWASHE42-1|yes; why: higher confidence-adjusted growth (6.86 vs 2.65 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: ANA offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (11.95 vs 5.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.15, ANA shot control · high event (8+) · decided (2+) 0.14, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.12.
- thesis VAN:OFFENSE_4PLUS (p 0.3715): highest fidelity KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.5242): highest fidelity KXNHLAST-26OCT27VANANA-ANABSENNECKE45-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:SUPPRESSED (p 0.2756): highest fidelity KXNHLGOAL-26OCT27VANANA-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27VANANA-ANACGAUTHIER61-1|no (same contract)
- KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.416, phi -0.232)
- KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 64% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.4 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2756, phi -0.214)
- KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.416, phi -0.208)

portfolios: A EV +4.63 (adj +1.30) on $15.00, P(profit) 0.4911, adj growth 11.5 bp · B EV +1.92 (adj +0.96) on $7.27, P(profit) 0.5601, adj growth 9.1 bp · C EV +2.33 (adj +0.99) on $9.66, P(profit) 0.4404, adj growth 9.2 bp · R EV +0.23 (adj +0.15) on $1.00, P(profit) 0.2344, adj growth 5.7 bp

## BUF @ SJS  ·  10000 joint draws  ·  534 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.428 / away 0.572

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
| Adam Gaudette: 1+ goals YES | 13 | 0.175 | 0.162 | +0.037 | +0.024 | $2.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 61 | 0.676 | 0.658 | +0.049 | +0.031 | $8.24 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 22 | 0.270 | 0.256 | +0.037 | +0.024 | $3.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 65 | 0.734 | 0.685 | +0.069 | +0.019 | $6.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (10.73 vs 6.93 bp); despite a smaller raw edge (+0.037 vs +0.037/contract); relationships: KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: SJS offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF3|no; why: higher confidence-adjusted growth (9.20 vs 7.42 bp); despite a smaller raw edge (+0.049 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.008 vs 0.776); relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: BUF offense succeeds (4+ goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes has the higher standalone adjusted growth (10.73 vs 6.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.085); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT27BUFSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (3.48 vs 1.58 bp); despite a smaller raw edge (+0.069 vs +0.135/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.085); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4384): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS_BY_2PLUS (p 0.3061): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3869): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3465, phi -0.197)
- KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.398, phi -0.24)
- KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3465, phi -0.221)
- KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4384, phi -0.229)

portfolios: A EV +3.26 (adj +0.63) on $15.00, P(profit) 0.4576, adj growth 5.7 bp · B EV +2.60 (adj +1.42) on $21.16, P(profit) 0.6759, adj growth 13.5 bp · C EV +2.98 (adj +1.45) on $22.04, P(profit) 0.6524, adj growth 13.6 bp · R EV +0.23 (adj +0.15) on $3.00, P(profit) 0.6756, adj growth 5.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
