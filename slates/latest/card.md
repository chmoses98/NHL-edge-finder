# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-27T15:46:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +24.78 | +7.66 | +23.36 | 0.772 | -16.04 | -26.24 | 71.35 |
| B thesis-diversified (joint) ← optimiser card | 149.02 | +25.56 | +13.58 | +22.86 | 0.727 | -23.95 | -35.50 | 127.64 |
| C best expression per thesis | 150.00 | +20.82 | +7.75 | +20.13 | 0.751 | -17.77 | -29.03 | 72.84 |
| R FUNDED research stakes | 15.00 | +1.89 | +1.14 | +0.12 | 0.501 | -6.17 | -6.72 | 0.00 |

## CBJ @ PHI  ·  10000 joint draws  ·  444 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CBJ_win | p_overtime | goals | shots PHI/CBJ | PHI/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.53 | 0.47 | 0.00 | 5.97 | 26.4/26.8 | 23.5/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.46 | 5.8 | 26.8/27.0 | 23.8/23.7 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.088 | 0.46 | 0.54 | 0.00 | 5.95 | 21.1/31.7 | 27.7/17.9 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.49 | 0.51 | 0.47 | 5.8 | 21.2/31.9 | 28.7/18.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.071 | 0.53 | 0.47 | 0.00 | 3.45 | 25.1/25.6 | 23.9/23.2 | late empty net |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.54 | 0.46 | 0.46 | 2.78 | 25.1/25.3 | 23.9/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Sanheim: 1+ goals YES | 8 | 0.118 | 0.108 | +0.033 | +0.022 | $2.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 15 | 0.195 | 0.183 | +0.036 | +0.024 | $2.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 8 | 0.113 | 0.101 | +0.027 | +0.015 | $1.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Adam Fantilli: 1+ goals NO | 70 | 0.744 | 0.732 | +0.029 | +0.017 | $6.53 | FUNDED_RESEARCH | $2 | CBJ:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27CBJPHI-PHITSANHEIM6-1|yes; why: higher confidence-adjusted growth (13.79 vs 3.49 bp); despite a smaller raw edge (+0.033 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: PHI offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27CBJPHI-CBJDSEVERSON78-1|yes; why: higher confidence-adjusted growth (9.03 vs 0.10 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense suppressed (<= 2 goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (9.03 vs 6.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: CBJ offense suppressed (<= 2 goals)
- **Adam Fantilli: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no; why: Player prop expression KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no selected over player prop KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3113): highest fidelity KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.4684): highest fidelity KXNHLGOAL-26OCT27CBJPHI-CBJKJOHNSON91-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no — Player prop expression KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no selected over player prop KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:OFFENSE_4PLUS (p 0.3356): highest fidelity KXNHLAST-26OCT27CBJPHI-PHITSANHEIM6-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT27CBJPHI-PHITSANHEIM6-1|yes (same contract)
- KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4421, phi -0.154)
- KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4684, phi -0.249)
- KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4684, phi -0.155)
- KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3113, phi -0.224)
- override: Player prop expression KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no selected over player prop KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.23 (adj +0.50) on $13.64, P(profit) 0.5519, adj growth 4.7 bp · B EV +2.39 (adj +1.52) on $13.46, P(profit) 0.3715, adj growth 14.2 bp · C EV +2.20 (adj +0.95) on $14.40, P(profit) 0.3877, adj growth 8.9 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.7437, adj growth 1.8 bp

## BOS @ CAR  ·  10000 joint draws  ·  450 bet sides mapped, 20 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_BOS_win | p_overtime | goals | shots CAR/BOS | CAR/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.160 | 0.63 | 0.37 | 0.00 | 6.04 | 34.4/21.2 | 18.3/29.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.142 | 0.55 | 0.45 | 0.49 | 5.98 | 34.9/21.3 | 18.1/31.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.137 | 0.67 | 0.33 | 0.00 | 9.44 | 36.1/22.7 | 17.7/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.083 | 0.57 | 0.43 | 0.00 | 6.02 | 28.1/27.1 | 23.8/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.57 | 0.43 | 0.00 | 9.47 | 29.9/28.5 | 22.8/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.52 | 0.48 | 0.46 | 5.99 | 28.0/27.1 | 23.8/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Casey Mittelstadt: 1+ goals YES | 13 | 0.186 | 0.170 | +0.048 | +0.032 | $3.64 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Pavel Zacha: 1+ goals YES | 21 | 0.275 | 0.256 | +0.053 | +0.034 | $4.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Mark Kastelic: 1+ goals YES | 7 | 0.110 | 0.096 | +0.035 | +0.021 | $2.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (18.20 vs 14.76 bp); despite a smaller raw edge (+0.048 vs +0.053/contract); relationships: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: BOS offense suppressed (<= 2 goals)
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT27BOSCAR-10|yes; why: higher confidence-adjusted growth (14.76 vs 10.34 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.912 vs 0.33); relationships: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: BOS offense suppressed (<= 2 goals)
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes has the higher standalone adjusted growth (14.76 vs 13.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.14.
- thesis BOS:OFFENSE_4PLUS (p 0.3823): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3307): highest fidelity KXNHLTOTAL-26OCT27BOSCAR-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:OFFENSE_4PLUS (p 0.49): highest fidelity KXNHLTOTAL-26OCT27BOSCAR-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT27BOSCAR-10|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.399, phi -0.184)
- KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.399, phi -0.233)
- KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.399, phi -0.133)

portfolios: A EV +2.18 (adj +0.59) on $13.64, P(profit) 0.5588, adj growth 5.4 bp · B EV +3.36 (adj +2.15) on $10.31, P(profit) 0.4786, adj growth 20.2 bp · C EV +2.86 (adj +1.28) on $14.65, P(profit) 0.3448, adj growth 11.9 bp · R EV +0.35 (adj +0.23) on $1.00, P(profit) 0.1863, adj growth 8.6 bp

## LAK @ CHI  ·  10000 joint draws  ·  428 bet sides mapped, 7 +EV candidates, 4 on card


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
| Ian Cole: 1+ goals YES | 3 | 0.054 | 0.047 | +0.022 | +0.015 | $1.39 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.076 | 0.069 | +0.023 | +0.015 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 55 | 0.687 | 0.592 | +0.120 | +0.024 | $6.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Erik Gustafsson: 1+ assists NO | 61 | 0.733 | 0.650 | +0.107 | +0.023 | $7.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Ian Cole: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27LACHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (14.66 vs 0.14 bp); alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: CHI offense suppressed (<= 2 goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27LACHI-LATMOORE12-1|yes; why: higher confidence-adjusted growth (9.74 vs 0.00 bp); despite a smaller raw edge (+0.023 vs +0.037/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27LACHI-CHIICOLE28-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: LAK offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (5.22 vs 4.87 bp); relationships: KXNHLGOAL-26OCT27LACHI-CHIICOLE28-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: CHI offense succeeds (4+ goals)
- **Erik Gustafsson: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27LACHI-LAQBYFIELD55-1|no; why: higher confidence-adjusted growth (5.09 vs 0.32 bp); alternative not eligible: confidence-adjusted EV +0.0055 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27LACHI-CHIICOLE28-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:SUPPRESSED (p 0.4409): highest fidelity KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no (same contract)
- thesis LAK:SUPPRESSED (p 0.4112): highest fidelity KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3456): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27LACHI-CHIICOLE28-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4409, phi -0.113)
- KXNHLGOAL-26OCT27LACHI-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4112, phi -0.135)
- KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.7 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3456, phi -0.245)
- KXNHLAST-26OCT27LACHI-LAEGUSTAFSSON64-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.8 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3641, phi -0.203)

portfolios: A EV +2.60 (adj +0.50) on $13.64, P(profit) 0.5697, adj growth 4.7 bp · B EV +4.31 (adj +1.64) on $17.12, P(profit) 0.5706, adj growth 15.3 bp · C EV +2.97 (adj +0.62) on $15.68, P(profit) 0.5074, adj growth 5.9 bp · R EV +0.69 (adj +0.46) on $1.00, P(profit) 0.0541, adj growth 14.7 bp

## MTL @ STL  ·  10000 joint draws  ·  452 bet sides mapped, 6 +EV candidates, 4 on card


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
| Pius Suter: 1+ goals YES | 14 | 0.177 | 0.165 | +0.029 | +0.017 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Oliver Kapanen: 1+ goals NO | 78 | 0.816 | 0.806 | +0.024 | +0.014 | $7.43 | FUNDED_RESEARCH | $2 | MTL:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 26 | 0.296 | 0.285 | +0.023 | +0.011 | $1.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 30 | 0.337 | 0.326 | +0.022 | +0.012 | $1.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27MTLSTL-STLJBERGGREN29-1|yes; why: higher confidence-adjusted growth (4.80 vs 2.50 bp); despite a smaller raw edge (+0.029 vs +0.057/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27MTLSTL-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: STL offense suppressed (<= 2 goals)
- **Oliver Kapanen: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT27MTLSTL-MTL2|no; why: higher confidence-adjusted growth (2.55 vs 1.21 bp); despite a smaller raw edge (+0.024 vs +0.039/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: MTL offense succeeds (4+ goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes; why: Player prop expression KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes selected over player prop KXNHLAST-26OCT27MTLSTL-STLJBERGGREN29-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.42 vs 0.42 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT27MTLSTL-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes has the higher standalone adjusted growth (4.80 vs 1.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT27MTLSTL-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4587): highest fidelity KXNHLSPREAD-26OCT27MTLSTL-MTL2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes — Player prop expression KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes selected over player prop KXNHLAST-26OCT27MTLSTL-STLJBERGGREN29-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.42 vs 0.42 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis MTL:SUPPRESSED (p 0.4358): highest fidelity KXNHLSPREAD-26OCT27MTLSTL-MTL2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27MTLSTL-MTLOKAPANEN91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.5784): highest fidelity KXNHLSPREAD-26OCT27MTLSTL-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3319, phi -0.207)
- KXNHLGOAL-26OCT27MTLSTL-MTLOKAPANEN91-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3448, phi -0.199)
- KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3319, phi -0.24)
- KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3319, phi -0.267)
- override: Player prop expression KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes selected over player prop KXNHLAST-26OCT27MTLSTL-STLJBERGGREN29-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.42 vs 0.42 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.54 (adj +0.54) on $13.64, P(profit) 0.4174, adj growth 5.0 bp · B EV +0.86 (adj +0.48) on $12.78, P(profit) 0.5272, adj growth 4.5 bp · C EV +0.81 (adj +0.46) on $12.34, P(profit) 0.4, adj growth 4.3 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.8161, adj growth 1.3 bp

## NYI @ NSH  ·  10000 joint draws  ·  438 bet sides mapped, 7 +EV candidates, 4 on card


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
| Adam Edstrom: 1+ goals YES | 13 | 0.165 | 0.155 | +0.027 | +0.017 | $2.05 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ goals YES | 17 | 0.211 | 0.198 | +0.031 | +0.018 | $2.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 12 | 0.158 | 0.143 | +0.030 | +0.016 | $1.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ assists NO | 73 | 0.800 | 0.758 | +0.056 | +0.014 | $7.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NYINSH-NSHJMARCHESSAULT81-1|yes; why: higher confidence-adjusted growth (5.21 vs 2.46 bp); despite a smaller raw edge (+0.027 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: NSH offense suppressed (<= 2 goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (5.21 vs 5.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: NSH offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT27NYINSH-8|yes; why: higher confidence-adjusted growth (4.81 vs 0.78 bp); despite a smaller raw edge (+0.030 vs +0.034/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.916 vs 0.339); alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.054); failure: NYI offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT27NYINSH-NYIVEKLUND73-1|no; why: higher confidence-adjusted growth (2.20 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.054); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:OFFENSE_4PLUS (p 0.4144): highest fidelity KXNHLAST-26OCT27NYINSH-NSHJMARCHESSAULT81-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:SUPPRESSED (p 0.3987): highest fidelity KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.381): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3697, phi -0.2)
- KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3697, phi -0.193)
- KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3987, phi -0.192)
- KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.381, phi -0.22)

portfolios: A EV +2.02 (adj +0.82) on $13.64, P(profit) 0.5214, adj growth 7.6 bp · B EV +1.81 (adj +0.87) on $13.46, P(profit) 0.4224, adj growth 8.2 bp · C EV +0.99 (adj +0.41) on $9.57, P(profit) 0.8326, adj growth 3.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ DAL  ·  10000 joint draws  ·  426 bet sides mapped, 9 +EV candidates, 4 on card


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
| Connor Brown: 1+ goals YES | 11 | 0.169 | 0.153 | +0.052 | +0.036 | $4.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Jamie Benn: 1+ goals YES | 13 | 0.171 | 0.158 | +0.033 | +0.020 | $2.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Amadeus Lombardi: 1+ goals YES | 9 | 0.125 | 0.110 | +0.029 | +0.014 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 68 | 0.718 | 0.707 | +0.023 | +0.012 | $4.06 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Connor Brown: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NJDAL-NJJSIEGENTHALER71-1|yes; why: higher confidence-adjusted growth (26.74 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: NJD offense suppressed (<= 2 goals)
- **Jamie Benn: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes; why: higher confidence-adjusted growth (7.28 vs 2.18 bp); despite a smaller raw edge (+0.033 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: DAL offense suppressed (<= 2 goals)
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NJDAL-NJJSIEGENTHALER71-1|yes; why: higher confidence-adjusted growth (5.01 vs 0.00 bp); despite a smaller raw edge (+0.029 vs +0.042/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: NJD offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27NJDAL-NJLEVANGELISTA77-1|no; why: Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.84 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis DAL:OFFENSE_4PLUS (p 0.393): highest fidelity KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes (same contract)
- thesis NJD:SUPPRESSED (p 0.4636): highest fidelity KXNHLAST-26OCT27NJDAL-NJLEVANGELISTA77-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27NJDAL-NJLEVANGELISTA77-1|no (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.3209): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4636, phi -0.215)
- KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.38, phi -0.187)
- KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4636, phi -0.185)
- KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3209, phi -0.247)
- override: Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.84 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.61 (adj +1.14) on $13.64, P(profit) 0.4862, adj growth 10.9 bp · B EV +2.95 (adj +1.88) on $11.98, P(profit) 0.401, adj growth 17.6 bp · C EV +1.31 (adj +0.25) on $9.63, P(profit) 0.7911, adj growth 2.4 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.7182, adj growth 1.3 bp

## FLA @ WPG  ·  10000 joint draws  ·  440 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_FLA_win | p_overtime | goals | shots WPG/FLA | WPG/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.56 | 0.44 | 0.00 | 6.02 | 26.9/27.1 | 23.8/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.49 | 0.51 | 0.49 | 5.91 | 26.9/27.1 | 23.8/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.57 | 0.43 | 0.00 | 9.2 | 28.5/28.6 | 23.0/22.1 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.44 | 0.56 | 0.46 | 5.92 | 21.5/31.8 | 28.5/18.3 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.071 | 0.48 | 0.52 | 0.00 | 5.98 | 21.4/32.0 | 28.2/18.1 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.060 | 0.66 | 0.34 | 0.00 | 6.09 | 31.4/21.4 | 18.6/27.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 66 | 0.718 | 0.702 | +0.042 | +0.026 | $7.30 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 14 | 0.178 | 0.165 | +0.030 | +0.017 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 69 | 0.739 | 0.724 | +0.034 | +0.019 | $5.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Cole Koepke: 1+ goals YES | 9 | 0.113 | 0.106 | +0.018 | +0.011 | $1.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:WINS_BY_2PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no; why: higher confidence-adjusted growth (6.99 vs 6.40 bp); despite a smaller raw edge (+0.042 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27FLAWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT27FLAWPG-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: FLA offense succeeds (4+ goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27FLAWPG-FLA3|no; why: higher confidence-adjusted growth (4.64 vs 3.30 bp); despite a smaller raw edge (+0.030 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27FLAWPG-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: WPG offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no; why: Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.86 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT27FLAWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27FLAWPG-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.037); failure: FLA offense succeeds (4+ goals)
- **Cole Koepke: 1+ goals YES** — thesis: WPG wins by 2+; alternative: KXNHLSPREAD-26OCT27FLAWPG-FLA3|no; why: KXNHLSPREAD-26OCT27FLAWPG-FLA3|no has the higher standalone adjusted growth (3.30 vs 2.79 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.089); relationships: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT27FLAWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.037); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis FLA:SUPPRESSED (p 0.4354): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no — Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.86 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WPG:WINS (p 0.5283): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3877): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27FLAWPG-WPGAIAFALLO9-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3433, phi -0.228)
- KXNHLGOAL-26OCT27FLAWPG-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3932, phi -0.192)
- KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3433, phi -0.233)
- KXNHLGOAL-26OCT27FLAWPG-WPGCKOEPKE45-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3932, phi -0.157)
- override: Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.86 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.22 (adj +0.38) on $13.64, P(profit) 0.718, adj growth 3.6 bp · B EV +1.32 (adj +0.78) on $16.08, P(profit) 0.6342, adj growth 7.4 bp · C EV +2.08 (adj +0.95) on $22.12, P(profit) 0.5624, adj growth 8.9 bp · R EV +0.12 (adj +0.08) on $2.00, P(profit) 0.7178, adj growth 3.0 bp

## MIN @ UTA  ·  10000 joint draws  ·  456 bet sides mapped, 5 +EV candidates, 4 on card


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
| Quinn Hughes: 1+ assists NO | 39 | 0.485 | 0.435 | +0.078 | +0.028 | $4.32 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.69) | EVIDENCE_MIXED | D |
| Kirill Kaprizov: 1+ goals NO | 58 | 0.634 | 0.618 | +0.037 | +0.021 | $4.21 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 19 | 0.232 | 0.216 | +0.031 | +0.016 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 12 | 0.155 | 0.140 | +0.028 | +0.013 | $1.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no; why: higher confidence-adjusted growth (7.27 vs 4.14 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: REINFORCING (phi 0.244); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: MIN offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no; why: second expression of the same thesis: KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no has the higher standalone adjusted growth (7.27 vs 4.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.244); they share one thesis budget; relationships: KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no: REINFORCING (phi 0.244); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27MINUTA-MIN2|no; why: higher confidence-adjusted growth (3.35 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: UTA offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27MINUTA-MIN2|no; why: higher confidence-adjusted growth (3.17 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:SUPPRESSED (p 0.4275): highest fidelity KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.4538): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 31% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.0 pts; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3567, phi -0.319)
- KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3567, phi -0.311)
- KXNHLGOAL-26OCT27MINUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3298, phi -0.195)
- KXNHLGOAL-26OCT27MINUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3298, phi -0.153)

portfolios: A EV +1.59 (adj +0.63) on $13.64, P(profit) 0.5187, adj growth 5.9 bp · B EV +1.72 (adj +0.75) on $11.98, P(profit) 0.5114, adj growth 7.1 bp · C EV +1.08 (adj +0.39) on $5.62, P(profit) 0.485, adj growth 3.7 bp · R EV +0.13 (adj +0.07) on $2.00, P(profit) 0.6345, adj growth 2.6 bp

## OTT @ VGK  ·  10000 joint draws  ·  448 bet sides mapped, 8 +EV candidates, 4 on card


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
| Brayden McNabb: 1+ goals YES | 6 | 0.088 | 0.076 | +0.024 | +0.012 | $1.18 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 59 | 0.712 | 0.629 | +0.105 | +0.022 | $7.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Michael Amadio: 1+ goals YES | 12 | 0.149 | 0.141 | +0.022 | +0.013 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ goals YES | 21 | 0.248 | 0.236 | +0.026 | +0.014 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (5.07 vs 2.58 bp); despite a smaller raw edge (+0.024 vs +0.026/contract); relationships: KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: VGK offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27OTTVGK-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (4.66 vs 2.64 bp); relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: OTT offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27OTTVGK-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (3.42 vs 0.52 bp); alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: OTT offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27OTTVGK-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (2.58 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0020 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.4569): highest fidelity KXNHLGOAL-26OCT27OTTVGK-OTTDBATHERSON19-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.3283): highest fidelity KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.4537): highest fidelity KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes (same contract)
- KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.33, phi -0.122)
- KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.7 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3283, phi -0.241)
- KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4569, phi -0.203)
- KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.33, phi -0.218)

portfolios: A EV +2.18 (adj +0.46) on $13.64, P(profit) 0.6339, adj growth 4.4 bp · B EV +2.22 (adj +0.79) on $12.10, P(profit) 0.366, adj growth 7.5 bp · C EV +2.14 (adj +0.72) on $16.82, P(profit) 0.6189, adj growth 6.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ ANA  ·  10000 joint draws  ·  394 bet sides mapped, 6 +EV candidates, 4 on card


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
| A.J. Greer: 2+ goals YES | 2 | 0.039 | 0.033 | +0.018 | +0.012 | $1.00 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.07) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 12 | 0.162 | 0.149 | +0.035 | +0.022 | $2.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ goals YES | 19 | 0.238 | 0.222 | +0.037 | +0.021 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 17 | 0.213 | 0.200 | +0.034 | +0.020 | $2.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 2+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (13.15 vs 3.49 bp); despite a smaller raw edge (+0.018 vs +0.081/contract); relationships: KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: ANA offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes; why: higher confidence-adjusted growth (9.22 vs 6.19 bp); despite a smaller raw edge (+0.035 vs +0.037/contract); relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (6.19 vs 5.97 bp); relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (6.19 vs 5.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.15, ANA shot control · high event (8+) · decided (2+) 0.14, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.12.
- thesis VAN:OFFENSE_4PLUS (p 0.3728): highest fidelity KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.5182): highest fidelity KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes (same contract)
- KXNHLGOAL-26OCT27VANANA-ANAAGREER18-2|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 93% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2819, phi -0.12)
- KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4102, phi -0.193)
- KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4102, phi -0.239)
- KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4102, phi -0.204)

portfolios: A EV +4.15 (adj +1.53) on $13.64, P(profit) 0.6316, adj growth 13.8 bp · B EV +2.47 (adj +1.54) on $8.70, P(profit) 0.5169, adj growth 14.4 bp · C EV +1.42 (adj +0.49) on $4.99, P(profit) 0.4419, adj growth 4.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ SJS  ·  10000 joint draws  ·  464 bet sides mapped, 12 +EV candidates, 4 on card


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
| Adam Gaudette: 1+ goals YES | 13 | 0.177 | 0.162 | +0.040 | +0.024 | $2.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 62 | 0.682 | 0.665 | +0.046 | +0.029 | $7.76 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| San Jose wins by over 1.5 goals YES | 24 | 0.317 | 0.276 | +0.064 | +0.023 | $2.14 | FUNDED_RESEARCH | $1 | SJS:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ goals NO | 77 | 0.813 | 0.801 | +0.031 | +0.019 | $8.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no; why: higher confidence-adjusted growth (10.38 vs 6.64 bp); despite a smaller raw edge (+0.040 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: REINFORCING (phi 0.195); KXNHLGOAL-26OCT27BUFSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: SJS offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no; why: higher confidence-adjusted growth (7.89 vs 6.64 bp); despite a smaller raw edge (+0.046 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: REINFORCING (phi 0.165); KXNHLGOAL-26OCT27BUFSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: BUF offense succeeds (4+ goals)
- **San Jose wins by over 1.5 goals YES** — thesis: SJS wins by 2+; alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no; why: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no has the higher standalone adjusted growth (6.64 vs 6.15 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.301); relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: REINFORCING (phi 0.195); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.165); KXNHLGOAL-26OCT27BUFSJ-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: BUF wins (incl. OT/SO)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT27BUFSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (4.59 vs 0.93 bp); despite a smaller raw edge (+0.031 vs +0.108/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4359): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3858): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS (p 0.5311): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no (same contract)
- KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3456, phi -0.199)
- KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3959, phi -0.249)
- KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4689, phi -0.64)
- KXNHLGOAL-26OCT27BUFSJ-SJISTENBERG41-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4359, phi -0.183)

portfolios: A EV +2.47 (adj +0.57) on $13.64, P(profit) 0.4921, adj growth 5.4 bp · B EV +2.15 (adj +1.18) on $21.05, P(profit) 0.6269, adj growth 11.2 bp · C EV +2.96 (adj +1.23) on $24.18, P(profit) 0.6582, adj growth 11.6 bp · R EV +0.40 (adj +0.18) on $3.00, P(profit) 0.7471, adj growth 6.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
