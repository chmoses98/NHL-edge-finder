# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-27T16:46:57Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +25.20 | +8.31 | +24.02 | 0.757 | -18.45 | -29.73 | 77.26 |
| B thesis-diversified (joint) ← optimiser card | 147.11 | +23.23 | +11.88 | +21.14 | 0.731 | -20.79 | -32.11 | 112.47 |
| C best expression per thesis | 150.01 | +23.75 | +9.42 | +22.08 | 0.735 | -22.11 | -33.62 | 87.73 |
| R FUNDED research stakes | 20.00 | +1.75 | +1.05 | +0.94 | 0.587 | -5.29 | -7.42 | 0.00 |

## CBJ @ PHI  ·  10000 joint draws  ·  440 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.478 / away 0.522

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
| Damon Severson: 1+ goals YES | 7 | 0.115 | 0.101 | +0.041 | +0.027 | $2.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Travis Sanheim: 1+ goals YES | 8 | 0.117 | 0.106 | +0.032 | +0.021 | $2.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Conor Garland: 1+ goals NO | 84 | 0.882 | 0.870 | +0.032 | +0.021 | $7.37 | FUNDED_RESEARCH | $2 | CBJ:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Adam Fantilli: 1+ goals NO | 70 | 0.742 | 0.730 | +0.027 | +0.015 | $4.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (21.99 vs 0.81 bp); alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: CBJ offense suppressed (<= 2 goals)
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no; why: higher confidence-adjusted growth (12.46 vs 2.77 bp); despite a smaller raw edge (+0.032 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: PHI offense suppressed (<= 2 goals)
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no; why: higher confidence-adjusted growth (7.42 vs 3.11 bp); despite a smaller raw edge (+0.032 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: CBJ offense succeeds (4+ goals)
- **Adam Fantilli: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no; why: Player prop expression KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no selected over player prop KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:SUPPRESSED (p 0.4704): highest fidelity KXNHLSPREAD-26OCT27CBJPHI-CBJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no — Player prop expression KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no selected over player prop KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:OFFENSE_4PLUS (p 0.3647): highest fidelity KXNHLSPREAD-26OCT27CBJPHI-CBJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.5341): highest fidelity KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27CBJPHI-CBJ2|no (same contract)
- KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4704, phi -0.172)
- KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4173, phi -0.163)
- KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3118, phi -0.155)
- KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3118, phi -0.225)
- override: Player prop expression KXNHLGOAL-26OCT27CBJPHI-CBJAFANTILLI19-1|no selected over player prop KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.07 (adj +0.31) on $13.64, P(profit) 0.6951, adj growth 2.9 bp · B EV +2.61 (adj +1.71) on $16.63, P(profit) 0.2201, adj growth 16.1 bp · C EV +1.06 (adj +0.33) on $13.15, P(profit) 0.5639, adj growth 3.1 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.8818, adj growth 1.9 bp

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
| Pavel Zacha: 1+ goals YES | 21 | 0.277 | 0.259 | +0.055 | +0.037 | $4.55 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Casey Mittelstadt: 1+ goals YES | 13 | 0.185 | 0.166 | +0.047 | +0.028 | $3.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Mark Kastelic: 1+ goals YES | 7 | 0.106 | 0.093 | +0.031 | +0.018 | $1.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT27BOSCAR-10|yes; why: higher confidence-adjusted growth (17.41 vs 8.42 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.935 vs 0.324); relationships: KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: BOS offense suppressed (<= 2 goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes has the higher standalone adjusted growth (17.41 vs 14.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: BOS offense suppressed (<= 2 goals)
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes has the higher standalone adjusted growth (17.41 vs 10.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.14.
- thesis BOS:OFFENSE_4PLUS (p 0.3761): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3188): highest fidelity KXNHLTOTAL-26OCT27BOSCAR-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:OFFENSE_4PLUS (p 0.4764): highest fidelity KXNHLTOTAL-26OCT27BOSCAR-7|yes [DIRECT], best adjusted EV KXNHLAST-26OCT27BOSCAR-CARKMILLER19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27BOSCAR-BOSPZACHA18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3979, phi -0.229)
- KXNHLGOAL-26OCT27BOSCAR-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3979, phi -0.184)
- KXNHLGOAL-26OCT27BOSCAR-BOSMKASTELIC47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3979, phi -0.133)

portfolios: A EV +2.43 (adj +0.62) on $13.64, P(profit) 0.5619, adj growth 5.6 bp · B EV +2.90 (adj +1.82) on $9.32, P(profit) 0.4775, adj growth 17.2 bp · C EV +2.26 (adj +1.28) on $7.17, P(profit) 0.3435, adj growth 11.9 bp · R EV +0.50 (adj +0.34) on $2.00, P(profit) 0.2769, adj growth 12.2 bp

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
| Patrick Kane: 1+ assists NO | 55 | 0.700 | 0.596 | +0.133 | +0.029 | $5.20 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Roman Kantserov: 1+ goals NO | 74 | 0.794 | 0.778 | +0.041 | +0.025 | $6.82 | FUNDED_RESEARCH | $2 | CHI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Erik Gustafsson: 1+ assists NO | 61 | 0.733 | 0.650 | +0.107 | +0.023 | $6.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
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

portfolios: A EV +2.45 (adj +0.50) on $13.64, P(profit) 0.6409, adj growth 4.8 bp · B EV +2.64 (adj +0.72) on $18.18, P(profit) 0.8214, adj growth 6.9 bp · C EV +4.02 (adj +0.87) on $19.81, P(profit) 0.5107, adj growth 8.2 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.7945, adj growth 2.6 bp

## MTL @ STL  ·  10000 joint draws  ·  454 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.513 / away 0.487

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_MTL_win | p_overtime | goals | shots STL/MTL | STL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.57 | 0.43 | 0.00 | 6.04 | 26.8/26.8 | 23.7/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.54 | 0.46 | 0.45 | 5.98 | 26.9/26.9 | 23.6/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.59 | 0.41 | 0.00 | 9.37 | 28.4/28.5 | 23.0/21.9 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.081 | 0.69 | 0.31 | 0.00 | 5.99 | 31.6/21.2 | 18.6/26.9 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.57 | 0.43 | 0.47 | 6.01 | 31.7/21.4 | 18.1/28.3 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.060 | 0.53 | 0.47 | 0.00 | 5.95 | 21.5/31.5 | 28.3/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pius Suter: 1+ goals YES | 14 | 0.183 | 0.169 | +0.035 | +0.020 | $2.06 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Philip Broberg: 1+ assists YES | 35 | 0.434 | 0.387 | +0.068 | +0.021 | $2.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | DIRECT (0.58) | EVIDENCE_MIXED | D |
| Robert Thomas: 1+ goals YES | 26 | 0.303 | 0.291 | +0.030 | +0.018 | $2.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 30 | 0.351 | 0.332 | +0.036 | +0.018 | $2.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27MTLSTL-STLPBROBERG6-1|yes; why: higher confidence-adjusted growth (6.99 vs 4.18 bp); despite a smaller raw edge (+0.035 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT27MTLSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.073); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: STL offense suppressed (<= 2 goals)
- **Philip Broberg: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes has the higher standalone adjusted growth (6.99 vs 4.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.073); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.073); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.142); failure: STL offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes has the higher standalone adjusted growth (6.99 vs 3.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.036); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26OCT27MTLSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes has the higher standalone adjusted growth (6.99 vs 3.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT27MTLSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.142); KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis STL:OFFENSE_4PLUS (p 0.4657): highest fidelity KXNHLAST-26OCT27MTLSTL-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT27MTLSTL-STLPBROBERG6-1|yes (same contract)
- KXNHLGOAL-26OCT27MTLSTL-STLPSUTER22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3252, phi -0.197)
- KXNHLAST-26OCT27MTLSTL-STLPBROBERG6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 42% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3252, phi -0.287)
- KXNHLGOAL-26OCT27MTLSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3252, phi -0.256)
- KXNHLGOAL-26OCT27MTLSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3252, phi -0.252)

portfolios: A EV +2.23 (adj +1.00) on $13.64, P(profit) 0.5596, adj growth 9.2 bp · B EV +1.37 (adj +0.66) on $8.49, P(profit) 0.4407, adj growth 6.3 bp · C EV +0.70 (adj +0.40) on $2.97, P(profit) 0.1832, adj growth 3.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ NSH  ·  10000 joint draws  ·  440 bet sides mapped, 7 +EV candidates, 4 on card

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
| Adam Edstrom: 1+ goals YES | 13 | 0.174 | 0.162 | +0.036 | +0.024 | $2.51 | FUNDED_RESEARCH | $1 | NSH:WINS_BY_2PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ goals YES | 17 | 0.208 | 0.198 | +0.029 | +0.018 | $2.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 12 | 0.154 | 0.139 | +0.027 | +0.012 | $1.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ assists NO | 73 | 0.799 | 0.757 | +0.055 | +0.013 | $5.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Adam Edstrom: 1+ goals YES** — thesis: NSH wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT27NYINSH-NSH4|yes; why: higher confidence-adjusted growth (10.08 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: MOSTLY_INDEPENDENT (phi 0.028); failure: NSH offense suppressed (<= 2 goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (10.08 vs 4.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NSH offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT27NYINSH-8|yes; why: higher confidence-adjusted growth (2.78 vs 1.56 bp); despite a smaller raw edge (+0.027 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.906 vs 0.33); relationships: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.061); failure: NYI offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27NYINSH-NYIMSCHAEFER48-1|no; why: higher confidence-adjusted growth (2.04 vs 0.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.061); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NSH:WINS_BY_2PLUS (p 0.3009): highest fidelity KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.4139): highest fidelity KXNHLTOTAL-26OCT27NYINSH-8|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:SUPPRESSED (p 0.3992): highest fidelity KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no (same contract)
- KXNHLGOAL-26OCT27NYINSH-NSHAEDSTROM84-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3694, phi -0.198)
- KXNHLGOAL-26OCT27NYINSH-NSHMBOURQUE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3694, phi -0.198)
- KXNHLGOAL-26OCT27NYINSH-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3992, phi -0.175)
- KXNHLAST-26OCT27NYINSH-NYIVEKLUND73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.3855, phi -0.216)

portfolios: A EV +2.16 (adj +0.85) on $13.64, P(profit) 0.5263, adj growth 7.8 bp · B EV +1.69 (adj +0.86) on $11.75, P(profit) 0.3913, adj growth 8.1 bp · C EV +1.76 (adj +0.79) on $13.25, P(profit) 0.328, adj growth 7.3 bp · R EV +0.26 (adj +0.17) on $1.00, P(profit) 0.1737, adj growth 6.2 bp

## NJD @ DAL  ·  10000 joint draws  ·  428 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.520 / away 0.479

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NJD_win | p_overtime | goals | shots DAL/NJD | DAL/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.59 | 0.41 | 0.00 | 6.01 | 26.8/26.9 | 23.8/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.53 | 0.47 | 0.50 | 5.99 | 26.8/27.0 | 23.6/23.4 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.074 | 0.52 | 0.48 | 0.00 | 5.94 | 21.3/31.8 | 28.3/17.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.58 | 0.42 | 0.00 | 9.17 | 28.1/28.2 | 22.8/21.4 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.51 | 0.49 | 0.47 | 5.81 | 21.4/31.8 | 28.4/18.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.60 | 0.40 | 0.00 | 3.43 | 25.2/25.5 | 23.9/23.1 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Brown: 1+ goals YES | 11 | 0.169 | 0.153 | +0.052 | +0.036 | $3.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Jamie Benn: 1+ goals YES | 13 | 0.168 | 0.156 | +0.030 | +0.018 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Amadeus Lombardi: 1+ goals YES | 9 | 0.124 | 0.111 | +0.029 | +0.015 | $1.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 68 | 0.728 | 0.715 | +0.033 | +0.019 | $6.61 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Connor Brown: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NJDAL-NJJSIEGENTHALER71-1|yes; why: higher confidence-adjusted growth (26.31 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: NJD offense suppressed (<= 2 goals)
- **Jamie Benn: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes; why: higher confidence-adjusted growth (6.09 vs 2.86 bp); despite a smaller raw edge (+0.030 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: DAL offense suppressed (<= 2 goals)
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes has the higher standalone adjusted growth (26.31 vs 5.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.032); they share one thesis budget; relationships: KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: NJD offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.85 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.07.
- thesis NJD:OFFENSE_4PLUS (p 0.3134): highest fidelity KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes (same contract)
- thesis NJD:SUPPRESSED (p 0.4716): highest fidelity KXNHLAST-26OCT27NJDAL-NJLEVANGELISTA77-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.85 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis DAL:OFFENSE_4PLUS (p 0.3983): highest fidelity KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT27NJDAL-DALTHARLEY55-1|yes (same contract)
- KXNHLGOAL-26OCT27NJDAL-NJCBROWN16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4716, phi -0.227)
- KXNHLGOAL-26OCT27NJDAL-DALJBENN14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.381, phi -0.181)
- KXNHLGOAL-26OCT27NJDAL-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4716, phi -0.183)
- KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3134, phi -0.235)
- override: Player prop expression KXNHLGOAL-26OCT27NJDAL-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT27NJDAL-NJJHUGHES86-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.85 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.68 (adj +1.21) on $13.64, P(profit) 0.4884, adj growth 11.6 bp · B EV +2.73 (adj +1.75) on $13.47, P(profit) 0.3892, adj growth 16.5 bp · C EV +3.96 (adj +2.12) on $17.85, P(profit) 0.3956, adj growth 19.6 bp · R EV +0.09 (adj +0.06) on $2.00, P(profit) 0.728, adj growth 2.1 bp

## FLA @ WPG  ·  10000 joint draws  ·  438 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.456 / away 0.544

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_FLA_win | p_overtime | goals | shots WPG/FLA | WPG/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.58 | 0.42 | 0.00 | 6.01 | 26.8/27.0 | 23.9/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.48 | 5.94 | 26.7/26.8 | 23.5/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.56 | 0.44 | 0.00 | 9.22 | 28.2/28.3 | 22.7/22.0 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.48 | 0.52 | 0.49 | 5.82 | 21.5/31.9 | 28.6/18.2 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.071 | 0.45 | 0.55 | 0.00 | 6.0 | 21.4/31.9 | 28.2/18.3 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.062 | 0.61 | 0.39 | 0.00 | 5.98 | 31.2/21.3 | 18.3/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 68 | 0.738 | 0.722 | +0.042 | +0.027 | $6.53 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 66 | 0.718 | 0.700 | +0.042 | +0.024 | $5.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.123 | 0.110 | +0.027 | +0.014 | $1.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 79 | 0.850 | 0.817 | +0.048 | +0.016 | $6.31 | FUNDED_RESEARCH | $2 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (7.41 vs 5.69 bp); relationships: KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT27FLAWPG-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLSPREAD-26OCT27FLAWPG-FLA3|no: REINFORCING (phi 0.167); failure: FLA offense succeeds (4+ goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no; why: Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.85 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT27FLAWPG-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT27FLAWPG-FLA3|no: MOSTLY_INDEPENDENT (phi 0.128); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT27FLAWPG-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (4.68 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.035/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT27FLAWPG-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.162); failure: FLA offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no has the higher standalone adjusted growth (7.41 vs 3.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.167); they share one thesis budget; relationships: KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: REINFORCING (phi 0.167); KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.128); KXNHLGOAL-26OCT27FLAWPG-FLACSCHWINDT79-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.162); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis FLA:SUPPRESSED (p 0.4349): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no — Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.85 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WPG:WINS (p 0.5271): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3879): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT27FLAWPG-FLA3|no (same contract)
- KXNHLGOAL-26OCT27FLAWPG-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3423, phi -0.253)
- KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3423, phi -0.236)
- KXNHLGOAL-26OCT27FLAWPG-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4349, phi -0.183)
- KXNHLSPREAD-26OCT27FLAWPG-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2516, phi -0.726)
- override: Player prop expression KXNHLGOAL-26OCT27FLAWPG-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26OCT27FLAWPG-FLASJONES3-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.85 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.15 (adj +0.34) on $13.64, P(profit) 0.7086, adj growth 3.3 bp · B EV +1.46 (adj +0.74) on $19.55, P(profit) 0.5499, adj growth 7.2 bp · C EV +1.23 (adj +0.60) on $20.38, P(profit) 0.653, adj growth 5.6 bp · R EV +0.24 (adj +0.12) on $4.00, P(profit) 0.653, adj growth 4.4 bp

## MIN @ UTA  ·  10000 joint draws  ·  462 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.536 / away 0.464

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
| Olli Maatta: 1+ goals YES | 3 | 0.055 | 0.046 | +0.023 | +0.014 | $1.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 9 | 0.123 | 0.114 | +0.028 | +0.018 | $1.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 58 | 0.634 | 0.618 | +0.037 | +0.021 | $5.54 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 14 | 0.172 | 0.162 | +0.024 | +0.013 | $1.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT27MINUTA-3|yes; why: higher confidence-adjusted growth (13.15 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.915 vs 0.763); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27MINUTA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT27MINUTA-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT27MINUTA-3|yes; why: higher confidence-adjusted growth (8.15 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.892 vs 0.763); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27MINUTA-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT27MINUTA-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no; why: Player prop expression KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.81 vs 0.69 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT27MINUTA-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT27MINUTA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT27MINUTA-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: MIN offense succeeds (4+ goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT27MINUTA-3|yes; why: higher confidence-adjusted growth (3.10 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.887 vs 0.763); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT27MINUTA-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27MINUTA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:SUPPRESSED (p 0.4275): highest fidelity KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no — Player prop expression KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.81 vs 0.69 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis MIN:OFFENSE_4PLUS (p 0.3567): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis UTA:OFFENSE_4PLUS (p 0.4538): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27MINUTA-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4275, phi -0.115)
- KXNHLGOAL-26OCT27MINUTA-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4275, phi -0.162)
- KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3567, phi -0.311)
- KXNHLGOAL-26OCT27MINUTA-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4275, phi -0.187)
- override: Player prop expression KXNHLGOAL-26OCT27MINUTA-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT27MINUTA-MINQHUGHES43-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.81 vs 0.69 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.59 (adj +0.63) on $13.64, P(profit) 0.5187, adj growth 5.9 bp · B EV +1.97 (adj +1.21) on $10.11, P(profit) 0.2632, adj growth 11.3 bp · C EV +1.21 (adj +0.44) on $6.28, P(profit) 0.485, adj growth 4.1 bp · R EV +0.13 (adj +0.07) on $2.00, P(profit) 0.6345, adj growth 2.6 bp

## OTT @ VGK  ·  10000 joint draws  ·  448 bet sides mapped, 6 +EV candidates, 4 on card

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
| Brayden McNabb: 1+ goals YES | 6 | 0.088 | 0.076 | +0.024 | +0.012 | $1.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 59 | 0.712 | 0.629 | +0.105 | +0.022 | $6.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Ivan Barbashev: 1+ goals YES | 21 | 0.248 | 0.236 | +0.026 | +0.014 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ goals NO | 66 | 0.699 | 0.688 | +0.023 | +0.012 | $3.80 | FUNDED_RESEARCH | $1 | VGK:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (5.07 vs 2.58 bp); despite a smaller raw edge (+0.024 vs +0.026/contract); relationships: KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: VGK offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27OTTVGK-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (4.66 vs 1.93 bp); relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: OTT offense succeeds (4+ goals)
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27OTTVGK-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (2.58 vs 0.00 bp); despite a smaller raw edge (+0.026 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0003 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: VGK offense suppressed (<= 2 goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27OTTVGK-VGKMSTONE61-1|no; why: higher confidence-adjusted growth (1.53 vs 0.34 bp); despite a smaller raw edge (+0.023 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0062 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.4569): highest fidelity KXNHLGOAL-26OCT27OTTVGK-OTTDBATHERSON19-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:OFFENSE_4PLUS (p 0.4537): highest fidelity KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.33): highest fidelity KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no (same contract)
- KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.33, phi -0.122)
- KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.7 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3283, phi -0.241)
- KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.33, phi -0.218)
- KXNHLGOAL-26OCT27OTTVGK-VGKJEICHEL9-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4537, phi -0.223)

portfolios: A EV +2.19 (adj +0.74) on $13.64, P(profit) 0.6072, adj growth 6.9 bp · B EV +1.83 (adj +0.62) on $12.96, P(profit) 0.6359, adj growth 5.8 bp · C EV +1.95 (adj +0.57) on $16.21, P(profit) 0.6036, adj growth 5.3 bp · R EV +0.03 (adj +0.02) on $1.00, P(profit) 0.6991, adj growth 0.7 bp

## VAN @ ANA  ·  10000 joint draws  ·  394 bet sides mapped, 5 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.648 / away 0.352

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
| Max Sasson: 1+ goals YES | 12 | 0.162 | 0.149 | +0.035 | +0.022 | $2.29 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 17 | 0.213 | 0.200 | +0.034 | +0.020 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ goals YES | 19 | 0.238 | 0.218 | +0.037 | +0.018 | $2.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (9.22 vs 5.97 bp); relationships: KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes; why: higher confidence-adjusted growth (5.97 vs 4.21 bp); despite a smaller raw edge (+0.034 vs +0.037/contract); relationships: KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: VAN offense suppressed (<= 2 goals)
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes has the higher standalone adjusted growth (5.97 vs 4.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.15, ANA shot control · high event (8+) · decided (2+) 0.14, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.12.
- thesis ANA:OFFENSE_4PLUS (p 0.5182): highest fidelity KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3728): highest fidelity KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4102, phi -0.193)
- KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4102, phi -0.204)
- KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4102, phi -0.239)

portfolios: A EV +4.63 (adj +1.72) on $13.64, P(profit) 0.6316, adj growth 15.6 bp · B EV +1.43 (adj +0.83) on $6.63, P(profit) 0.4977, adj growth 7.8 bp · C EV +2.10 (adj +0.72) on $5.92, P(profit) 0.4166, adj growth 6.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ SJS  ·  10000 joint draws  ·  470 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.431 / away 0.569

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
| Adam Gaudette: 1+ goals YES | 13 | 0.177 | 0.159 | +0.040 | +0.021 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 62 | 0.682 | 0.665 | +0.046 | +0.029 | $6.92 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 2.5 goals NO | 76 | 0.837 | 0.796 | +0.064 | +0.023 | $7.87 | FUNDED_RESEARCH | $2 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Macklin Celebrini: 1+ assists NO | 43 | 0.568 | 0.461 | +0.121 | +0.014 | $3.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.77) | CALIBRATION_WARNING | D |
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no; why: higher confidence-adjusted growth (8.34 vs 6.64 bp); despite a smaller raw edge (+0.040 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLAST-26OCT27BUFSJ-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi -0.029); failure: SJS offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no; why: higher confidence-adjusted growth (7.89 vs 6.64 bp); despite a smaller raw edge (+0.046 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: REINFORCING (phi 0.166); KXNHLAST-26OCT27BUFSJ-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: BUF offense succeeds (4+ goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF2|no; why: higher confidence-adjusted growth (6.64 vs 5.49 bp); despite a smaller raw edge (+0.064 vs +0.068/contract); relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.113); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.166); KXNHLAST-26OCT27BUFSJ-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.168); failure: BUF wins by 2+
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT27BUFSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (1.65 vs 1.46 bp); relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: INTENTIONAL_DIVERSIFIER (phi -0.168); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4359): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3858): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS (p 0.5311): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no (same contract)
- KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3456, phi -0.199)
- KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3959, phi -0.249)
- KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.266, phi -0.734)
- KXNHLAST-26OCT27BUFSJ-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4359, phi -0.272)

portfolios: A EV +2.62 (adj +0.39) on $13.64, P(profit) 0.6067, adj growth 3.7 bp · B EV +2.59 (adj +0.96) on $20.02, P(profit) 0.6584, adj growth 9.2 bp · C EV +3.50 (adj +1.30) on $27.02, P(profit) 0.6584, adj growth 12.1 bp · R EV +0.31 (adj +0.15) on $4.00, P(profit) 0.5992, adj growth 5.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
