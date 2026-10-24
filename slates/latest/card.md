# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T12:59:03Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +27.60 | +9.21 | +26.19 | 0.753 | -20.95 | -33.25 | 84.66 |
| B thesis-diversified (joint) ← optimiser card | 149.20 | +25.33 | +9.88 | +22.67 | 0.748 | -18.88 | -30.07 | 92.19 |
| C best expression per thesis | 149.98 | +27.57 | +10.71 | +23.68 | 0.703 | -30.05 | -43.26 | 96.17 |
| R FUNDED research stakes | 21.00 | +3.28 | +1.74 | +1.44 | 0.586 | -7.51 | -9.38 | 0.00 |

## ANA @ PHI  ·  10000 joint draws  ·  406 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_ANA_win | p_overtime | goals | shots PHI/ANA | PHI/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.58 | 0.42 | 0.00 | 5.97 | 26.7/27.1 | 24.0/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.48 | 5.91 | 26.8/27.1 | 23.8/23.5 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.104 | 0.51 | 0.49 | 0.00 | 6.01 | 21.4/32.3 | 28.6/18.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.46 | 0.54 | 0.44 | 5.9 | 21.2/32.5 | 29.2/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.59 | 0.41 | 0.00 | 9.22 | 28.2/28.9 | 23.4/21.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.064 | 0.47 | 0.53 | 0.00 | 9.15 | 22.5/34.2 | 27.7/17.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 12 | 0.195 | 0.174 | +0.068 | +0.046 | $6.11 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Denver Barkey: 1+ goals YES | 13 | 0.184 | 0.170 | +0.047 | +0.032 | $4.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 14 | 0.184 | 0.164 | +0.035 | +0.016 | $2.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 20 | 0.237 | 0.226 | +0.026 | +0.014 | $2.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24ANAPHI-ANAJLACOMBE2-1|yes; why: higher confidence-adjusted growth (40.94 vs 0.81 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: ANA offense suppressed (<= 2 goals)
- **Denver Barkey: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (18.09 vs 4.21 bp); relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: PHI offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (4.21 vs 2.66 bp); relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (4.21 vs 2.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3451): highest fidelity KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.403): highest fidelity KXNHLAST-26OCT24ANAPHI-PHITSANHEIM6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4306, phi -0.23)
- KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3834, phi -0.195)
- KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3834, phi -0.209)
- KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3834, phi -0.213)

portfolios: A EV +5.13 (adj +2.92) on $15.31, P(profit) 0.6374, adj growth 27.1 bp · B EV +5.54 (adj +3.63) on $15.10, P(profit) 0.3717, adj growth 33.5 bp · C EV +5.69 (adj +3.71) on $12.53, P(profit) 0.3444, adj growth 32.7 bp · R EV +1.06 (adj +0.73) on $2.00, P(profit) 0.1951, adj growth 26.1 bp

## LAK @ NJD  ·  10000 joint draws  ·  434 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_LAK_win | p_overtime | goals | shots NJD/LAK | NJD/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.55 | 0.45 | 0.00 | 5.91 | 28.5/28.0 | 24.8/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.48 | 5.85 | 28.7/28.2 | 25.0/25.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.106 | 0.60 | 0.40 | 0.00 | 5.94 | 34.1/22.5 | 19.6/29.9 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.54 | 0.46 | 0.48 | 5.88 | 33.9/22.1 | 18.9/30.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.068 | 0.57 | 0.43 | 0.00 | 9.09 | 29.7/29.3 | 23.9/23.1 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.49 | 0.51 | 0.49 | 2.8 | 27.0/26.5 | 25.1/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Hughes: 1+ goals NO | 63 | 0.701 | 0.680 | +0.054 | +0.034 | $7.86 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 62 | 0.790 | 0.667 | +0.154 | +0.030 | $7.86 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Mats Zuccarello: 1+ assists NO | 67 | 0.818 | 0.712 | +0.132 | +0.026 | $7.86 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 56 | 0.626 | 0.590 | +0.049 | +0.013 | $2.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (11.21 vs 8.61 bp); despite a smaller raw edge (+0.054 vs +0.154/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: NJD offense succeeds (4+ goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no has the higher standalone adjusted growth (11.21 vs 8.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.062); they share one thesis budget; relationships: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: NJD offense succeeds (4+ goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (7.18 vs 1.56 bp); relationships: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.067); failure: LAK offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no has the higher standalone adjusted growth (7.18 vs 1.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.067); they share one thesis budget; relationships: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.067); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.11.
- thesis NJD:SUPPRESSED (p 0.4061): highest fidelity KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.4795): highest fidelity KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no (same contract)
- KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3725, phi -0.249)
- KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.0 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3725, phi -0.201)
- KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.3 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3022, phi -0.223)
- KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3022, phi -0.3)

portfolios: A EV +2.33 (adj +0.61) on $15.31, P(profit) 0.6867, adj growth 5.9 bp · B EV +4.30 (adj +1.15) on $26.18, P(profit) 0.7106, adj growth 11.1 bp · C EV +4.37 (adj +1.44) on $31.52, P(profit) 0.5709, adj growth 13.4 bp · R EV +0.17 (adj +0.11) on $2.00, P(profit) 0.7006, adj growth 4.1 bp

## SJS @ BOS  ·  10000 joint draws  ·  448 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_SJS_win | p_overtime | goals | shots BOS/SJS | BOS/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.66 | 0.34 | 0.00 | 6.03 | 27.5/27.5 | 24.6/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.55 | 0.45 | 0.46 | 5.96 | 27.9/27.9 | 24.5/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.64 | 0.36 | 0.00 | 9.42 | 29.4/29.2 | 24.0/22.3 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.076 | 0.68 | 0.32 | 0.00 | 6.08 | 32.4/22.0 | 19.3/27.8 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.062 | 0.59 | 0.41 | 0.00 | 6.04 | 22.2/32.6 | 29.1/18.5 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.061 | 0.75 | 0.25 | 0.00 | 9.38 | 34.5/23.6 | 19.4/26.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mark Kastelic: 1+ goals YES | 11 | 0.141 | 0.132 | +0.024 | +0.015 | $2.12 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Tanner Jeannot: 1+ goals YES | 8 | 0.111 | 0.096 | +0.026 | +0.011 | $1.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 66 | 0.735 | 0.690 | +0.059 | +0.014 | $7.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Pavel Zacha: 1+ goals YES | 27 | 0.320 | 0.297 | +0.036 | +0.014 | $2.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (4.94 vs 2.01 bp); despite a smaller raw edge (+0.024 vs +0.036/contract); relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: BOS offense suppressed (<= 2 goals)
- **Tanner Jeannot: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (3.11 vs 2.01 bp); despite a smaller raw edge (+0.026 vs +0.036/contract); relationships: KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: BOS offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no; why: higher confidence-adjusted growth (2.02 vs 0.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0002 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.118); failure: BOS offense succeeds (4+ goals)
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24SJBOS-BOSHLINDHOLM27-1|yes; why: higher confidence-adjusted growth (2.01 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.118); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis BOS:SUPPRESSED (p 0.303): highest fidelity KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.4963): highest fidelity KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3429): highest fidelity KXNHLAST-26OCT24SJBOS-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT24SJBOS-SJTTOFFOLI73-1|yes (same contract)
- KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.303, phi -0.16)
- KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.303, phi -0.129)
- KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4963, phi -0.221)
- KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.303, phi -0.224)

portfolios: A EV +2.55 (adj +0.73) on $15.31, P(profit) 0.5166, adj growth 6.5 bp · B EV +1.81 (adj +0.72) on $13.26, P(profit) 0.3974, adj growth 6.7 bp · C EV +2.08 (adj +0.55) on $17.45, P(profit) 0.4075, adj growth 5.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYR @ OTT  ·  10000 joint draws  ·  434 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYR_win | p_overtime | goals | shots OTT/NYR | OTT/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.128 | 0.61 | 0.39 | 0.00 | 5.97 | 32.3/20.7 | 17.7/28.1 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.53 | 0.47 | 0.46 | 5.86 | 32.8/21.1 | 17.9/29.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.54 | 0.46 | 0.00 | 6.0 | 27.0/26.4 | 23.0/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.48 | 0.52 | 0.48 | 5.93 | 27.0/26.4 | 23.2/23.7 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.082 | 0.60 | 0.40 | 0.00 | 9.28 | 34.3/22.5 | 17.3/27.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.55 | 0.45 | 0.00 | 9.37 | 28.4/27.9 | 21.9/22.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Gabe Perreault: 1+ goals YES | 21 | 0.257 | 0.243 | +0.035 | +0.021 | $3.11 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Vladislav Gavrikov: 1+ assists YES | 26 | 0.342 | 0.293 | +0.068 | +0.020 | $2.88 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
| Nick Cousins: 1+ goals YES | 8 | 0.110 | 0.095 | +0.025 | +0.010 | $1.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 58 | 0.701 | 0.613 | +0.104 | +0.015 | $5.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Gabe Perreault: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (5.62 vs 4.31 bp); despite a smaller raw edge (+0.035 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.122); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense suppressed (<= 2 goals)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes has the higher standalone adjusted growth (5.62 vs 4.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.122); they share one thesis budget; relationships: KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.122); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NYR offense suppressed (<= 2 goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24NYROTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (2.81 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.037/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.044); failure: OTT offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT24NYROTT-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (2.19 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: OTT offense succeeds (4+ goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis NYR:OFFENSE_4PLUS (p 0.3534): highest fidelity KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:SUPPRESSED (p 0.3767): highest fidelity KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4016): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4249, phi -0.245)
- KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4249, phi -0.28)
- KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3767, phi -0.166)
- KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.6 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4016, phi -0.243)

portfolios: A EV +3.23 (adj +1.02) on $15.31, P(profit) 0.508, adj growth 9.2 bp · B EV +2.62 (adj +0.81) on $13.16, P(profit) 0.487, adj growth 7.6 bp · C EV +2.29 (adj +0.71) on $13.61, P(profit) 0.7785, adj growth 6.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ PIT  ·  10000 joint draws  ·  392 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_NSH_win | p_overtime | goals | shots PIT/NSH | PIT/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.61 | 0.39 | 0.00 | 6.04 | 28.0/27.5 | 24.5/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.53 | 0.47 | 0.47 | 5.94 | 27.9/27.6 | 24.4/24.5 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.104 | 0.64 | 0.36 | 0.00 | 6.04 | 33.1/22.0 | 19.3/28.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.59 | 0.41 | 0.00 | 9.42 | 29.6/29.2 | 23.5/22.8 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.56 | 0.44 | 0.47 | 5.92 | 33.7/22.1 | 19.0/30.2 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.085 | 0.69 | 0.31 | 0.00 | 9.33 | 34.8/23.2 | 18.8/26.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, PIT shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ WSH  ·  10000 joint draws  ·  436 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_BUF_win | p_overtime | goals | shots WSH/BUF | WSH/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.57 | 0.43 | 0.00 | 6.01 | 27.8/27.8 | 24.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.47 | 5.95 | 27.5/27.9 | 24.5/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.58 | 0.42 | 0.00 | 9.28 | 29.0/29.0 | 23.4/22.4 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.076 | 0.51 | 0.49 | 0.00 | 6.02 | 22.0/32.7 | 28.8/18.5 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.44 | 0.56 | 0.45 | 5.86 | 22.1/33.0 | 29.7/18.9 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.060 | 0.63 | 0.37 | 0.00 | 6.01 | 32.4/22.1 | 19.3/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tage Thompson: 1+ goals NO | 63 | 0.693 | 0.675 | +0.047 | +0.029 | $10.28 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 26 | 0.387 | 0.294 | +0.113 | +0.021 | $3.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Rasmus Dahlin: 1+ assists NO | 53 | 0.608 | 0.564 | +0.060 | +0.016 | $3.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no; why: higher confidence-adjusted growth (7.81 vs 2.37 bp); despite a smaller raw edge (+0.047 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.136); failure: BUF offense succeeds (4+ goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24BUFWSH-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (4.85 vs 0.29 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0052 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: WSH offense suppressed (<= 2 goals)
- **Rasmus Dahlin: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no has the higher standalone adjusted growth (7.81 vs 2.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.136); they share one thesis budget; relationships: KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.136); KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:SUPPRESSED (p 0.4097): highest fidelity KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no (same contract)
- thesis WSH:OFFENSE_4PLUS (p 0.4361): highest fidelity KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes (same contract)
- KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3743, phi -0.259)
- KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.2 pts; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3506, phi -0.279)
- KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3743, phi -0.282)

portfolios: A EV +3.04 (adj +0.77) on $15.31, P(profit) 0.665, adj growth 7.1 bp · B EV +2.52 (adj +0.82) on $17.28, P(profit) 0.6041, adj growth 7.7 bp · C EV +3.20 (adj +1.08) on $20.73, P(profit) 0.6931, adj growth 9.8 bp · R EV +0.22 (adj +0.13) on $3.00, P(profit) 0.6931, adj growth 4.9 bp

## VGK @ CBJ  ·  10000 joint draws  ·  412 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_VGK_win | p_overtime | goals | shots CBJ/VGK | CBJ/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.47 | 0.53 | 0.00 | 6.02 | 27.3/27.4 | 23.7/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.50 | 0.50 | 0.45 | 5.81 | 27.3/27.3 | 24.0/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.47 | 0.54 | 0.00 | 9.19 | 29.0/29.0 | 22.8/23.3 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.066 | 0.43 | 0.57 | 0.00 | 5.95 | 21.8/31.8 | 27.9/18.8 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.53 | 0.47 | 0.45 | 5.87 | 32.3/22.1 | 19.0/29.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.47 | 0.53 | 0.00 | 3.47 | 26.2/26.2 | 24.3/24.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivan Barbashev: 1+ goals YES | 18 | 0.228 | 0.215 | +0.038 | +0.025 | $4.56 | FUNDED_RESEARCH | $2 | VGK:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ assists NO | 42 | 0.568 | 0.449 | +0.131 | +0.012 | $4.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.75) | CALIBRATION_WARNING | D |
| Mark Stone: 1+ assists NO | 56 | 0.620 | 0.588 | +0.043 | +0.010 | $4.47 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24VGKCBJ-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (8.52 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no: INTENTIONAL_DIVERSIFIER (phi -0.22); KXNHLAST-26OCT24VGKCBJ-VGKMSTONE61-1|no: INTENTIONAL_DIVERSIFIER (phi -0.188); failure: VGK offense suppressed (<= 2 goals)
- **Jack Eichel: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24VGKCBJ-VGKMSTONE61-1|no; why: higher confidence-adjusted growth (1.36 vs 0.94 bp); evidence CALIBRATION_WARNING vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24VGKCBJ-VGKIBARBASHEV49-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.22); KXNHLAST-26OCT24VGKCBJ-VGKMSTONE61-1|no: MOSTLY_INDEPENDENT (phi 0.146); failure: VGK offense succeeds (4+ goals)
- **Mark Stone: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no has the higher standalone adjusted growth (1.36 vs 0.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.146); they share one thesis budget; relationships: KXNHLGOAL-26OCT24VGKCBJ-VGKIBARBASHEV49-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.188); KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.146); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis VGK:OFFENSE_4PLUS (p 0.363): highest fidelity KXNHLGOAL-26OCT24VGKCBJ-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24VGKCBJ-VGKIBARBASHEV49-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.409): highest fidelity KXNHLAST-26OCT24VGKCBJ-VGKMSTONE61-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24VGKCBJ-VGKIBARBASHEV49-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.409, phi -0.202)
- KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.363, phi -0.288)
- KXNHLAST-26OCT24VGKCBJ-VGKMSTONE61-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.363, phi -0.26)

portfolios: A EV +2.90 (adj +0.72) on $15.31, P(profit) 0.5747, adj growth 6.7 bp · B EV +2.48 (adj +0.79) on $13.17, P(profit) 0.5747, adj growth 7.3 bp · C EV +3.33 (adj +1.03) on $13.27, P(profit) 0.7122, adj growth 9.2 bp · R EV +0.40 (adj +0.26) on $2.00, P(profit) 0.2283, adj growth 8.8 bp

## CAR @ STL  ·  10000 joint draws  ·  414 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_CAR_win | p_overtime | goals | shots STL/CAR | STL/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.137 | 0.50 | 0.50 | 0.00 | 6.06 | 21.0/33.3 | 29.4/17.6 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.49 | 0.51 | 0.50 | 5.96 | 21.3/33.3 | 29.9/18.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.55 | 0.45 | 0.00 | 6.04 | 26.5/27.4 | 24.0/22.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.098 | 0.49 | 0.51 | 0.00 | 9.3 | 22.5/34.9 | 28.4/16.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.53 | 0.47 | 0.47 | 5.95 | 26.3/27.2 | 23.9/22.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.56 | 0.44 | 0.00 | 9.38 | 28.0/28.8 | 22.9/21.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| St. Louis wins by over 1.5 goals YES | 22 | 0.306 | 0.260 | +0.074 | +0.028 | $3.31 | FUNDED_RESEARCH | $1 | STL:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 76 | 0.830 | 0.792 | +0.057 | +0.020 | $7.86 | FUNDED_RESEARCH | $2 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| St. Louis over 2.5 goals scored YES | 57 | 0.655 | 0.608 | +0.068 | +0.020 | $1.24 | FUNDED_RESEARCH | $1 | STL:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Shayne Gostisbehere: 1+ assists NO | 56 | 0.638 | 0.589 | +0.061 | +0.012 | $1.89 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CAR:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **St. Louis wins by over 1.5 goals YES** — thesis: STL wins by 2+; alternative: KXNHLSPREAD-26OCT24CARSTL-CAR2|no; why: higher confidence-adjusted growth (9.73 vs 6.10 bp); relationships: KXNHLSPREAD-26OCT24CARSTL-CAR3|no: DUPLICATIVE (phi 0.3); KXNHLTEAMTOTAL-26OCT24CARSTL-STL3|yes: DUPLICATIVE (phi 0.449); KXNHLAST-26OCT24CARSTL-CARSGOSTISBEHERE4-1|no: REINFORCING (phi 0.155); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 2.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-STL2|yes has the higher standalone adjusted growth (9.73 vs 4.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.300); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-STL2|yes: DUPLICATIVE (phi 0.3); KXNHLTEAMTOTAL-26OCT24CARSTL-STL3|yes: REINFORCING (phi 0.419); KXNHLAST-26OCT24CARSTL-CARSGOSTISBEHERE4-1|no: REINFORCING (phi 0.158); failure: CAR wins by 2+
- **St. Louis over 2.5 goals scored YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT24CARSTL-STL3|yes selected over broad KXNHLTEAMTOTAL-26OCT24CARSTL-STL5|yes because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.59 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT24CARSTL-STL2|yes: DUPLICATIVE (phi 0.449); KXNHLSPREAD-26OCT24CARSTL-CAR3|no: REINFORCING (phi 0.419); KXNHLAST-26OCT24CARSTL-CARSGOSTISBEHERE4-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: STL offense suppressed (<= 2 goals)
- **Shayne Gostisbehere: 1+ assists NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-STL2|yes has the higher standalone adjusted growth (9.73 vs 1.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.155); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-STL2|yes: REINFORCING (phi 0.155); KXNHLSPREAD-26OCT24CARSTL-CAR3|no: REINFORCING (phi 0.158); KXNHLTEAMTOTAL-26OCT24CARSTL-STL3|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis STL:WINS_BY_2PLUS (p 0.3056): highest fidelity KXNHLSPREAD-26OCT24CARSTL-STL2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-STL2|yes (same contract)
- thesis STL:WINS (p 0.5186): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-STL2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.4257): highest fidelity KXNHLTEAMTOTAL-26OCT24CARSTL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-STL2|yes — Broad expression KXNHLTEAMTOTAL-26OCT24CARSTL-STL3|yes selected over broad KXNHLTEAMTOTAL-26OCT24CARSTL-STL5|yes because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.59 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLSPREAD-26OCT24CARSTL-STL2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.4814, phi -0.639)
- KXNHLSPREAD-26OCT24CARSTL-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2727, phi -0.739)
- KXNHLTEAMTOTAL-26OCT24CARSTL-STL3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis STL:SUPPRESSED (p 0.3549, phi -0.978)
- KXNHLAST-26OCT24CARSTL-CARSGOSTISBEHERE4-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4043, phi -0.268)
- override: Broad expression KXNHLTEAMTOTAL-26OCT24CARSTL-STL3|yes selected over broad KXNHLTEAMTOTAL-26OCT24CARSTL-STL5|yes because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.59 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.48 (adj +0.82) on $15.31, P(profit) 0.4743, adj growth 7.5 bp · B EV +1.98 (adj +0.69) on $14.30, P(profit) 0.4914, adj growth 6.4 bp · C EV +2.05 (adj +0.79) on $6.45, P(profit) 0.3056, adj growth 7.0 bp · R EV +0.58 (adj +0.21) on $4.00, P(profit) 0.6256, adj growth 7.6 bp

## TOR @ EDM  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_TOR_win | p_overtime | goals | shots EDM/TOR | EDM/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.129 | 0.73 | 0.27 | 0.00 | 6.08 | 35.4/22.9 | 20.4/30.3 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.125 | 0.73 | 0.27 | 0.00 | 9.48 | 37.0/24.1 | 19.6/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.68 | 0.32 | 0.00 | 6.05 | 29.3/28.7 | 25.9/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.69 | 0.31 | 0.00 | 9.58 | 31.4/30.5 | 25.1/23.6 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.57 | 0.43 | 0.45 | 5.99 | 35.4/23.0 | 19.8/31.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.46 | 0.47 | 6.0 | 29.8/29.2 | 25.9/26.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kirill Marchenko: 1+ assists NO | 63 | 0.702 | 0.661 | +0.056 | +0.015 | $5.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Auston Matthews: 1+ assists NO | 57 | 0.642 | 0.601 | +0.055 | +0.014 | $4.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Leon Draisaitl: 1+ assists NO | 38 | 0.485 | 0.407 | +0.089 | +0.011 | $2.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.75) | EVIDENCE_MIXED | D |
- **Kirill Marchenko: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (2.10 vs 1.72 bp); relationships: KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.077); KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: TOR offense succeeds (4+ goals)
- **Auston Matthews: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no has the higher standalone adjusted growth (2.10 vs 1.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.077); they share one thesis budget; relationships: KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi 0.077); KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: TOR offense succeeds (4+ goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (1.04 vs 0.27 bp); alternative not eligible: confidence-adjusted EV +0.0051 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, EDM shot control · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:SUPPRESSED (p 0.4321): highest fidelity KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no (same contract)
- thesis EDM:SUPPRESSED (p 0.25): highest fidelity KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no (same contract)
- KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3474, phi -0.251)
- KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3474, phi -0.269)
- KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5538, phi -0.303)

portfolios: A EV +2.06 (adj +0.37) on $15.31, P(profit) 0.6663, adj growth 3.4 bp · B EV +1.37 (adj +0.28) on $11.92, P(profit) 0.6663, adj growth 2.7 bp · C EV +1.53 (adj +0.29) on $12.22, P(profit) 0.7022, adj growth 2.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TBL @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TBL_win | p_overtime | goals | shots UTA/TBL | UTA/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.61 | 0.39 | 0.00 | 6.01 | 26.7/26.8 | 23.8/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.49 | 0.51 | 0.49 | 5.92 | 26.9/26.9 | 23.7/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.61 | 0.39 | 0.00 | 9.39 | 28.4/28.5 | 22.9/21.6 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.075 | 0.67 | 0.33 | 0.00 | 5.99 | 31.6/21.3 | 18.6/27.1 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.062 | 0.55 | 0.45 | 0.00 | 6.03 | 21.2/31.4 | 27.9/17.5 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.057 | 0.50 | 0.50 | 0.48 | 5.89 | 21.5/31.9 | 28.6/18.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_DET_win | p_overtime | goals | shots CGY/DET | CGY/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.51 | 0.49 | 0.00 | 5.97 | 28.6/28.7 | 25.0/25.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.50 | 0.50 | 0.49 | 5.88 | 28.3/28.7 | 25.5/25.0 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.090 | 0.46 | 0.54 | 0.00 | 5.94 | 22.8/33.9 | 29.9/19.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.52 | 0.48 | 0.50 | 5.82 | 22.7/34.1 | 30.9/19.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.56 | 0.44 | 0.00 | 9.12 | 29.9/30.3 | 24.8/23.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.059 | 0.52 | 0.48 | 0.47 | 2.84 | 26.9/27.1 | 25.7/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Detroit wins by over 2.5 goals NO | 77 | 0.832 | 0.798 | +0.050 | +0.016 | $9.69 | FUNDED_RESEARCH | $3 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit wins by over 1.5 goals NO | 66 | 0.727 | 0.691 | +0.052 | +0.015 | $1.31 | FUNDED_RESEARCH | $1 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Detroit wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24DETCGY-DET2|no; why: higher confidence-adjusted growth (3.37 vs 2.39 bp); despite a smaller raw edge (+0.050 vs +0.052/contract); relationships: KXNHLSPREAD-26OCT24DETCGY-DET2|no: DUPLICATIVE (phi 0.734); failure: DET wins by 2+
- **Detroit wins by over 1.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24DETCGY-DET3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24DETCGY-DET3|no has the higher standalone adjusted growth (3.37 vs 2.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.734); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24DETCGY-DET3|no: DUPLICATIVE (phi 0.734); failure: DET wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:WINS (p 0.5057): highest fidelity KXNHLSPREAD-26OCT24DETCGY-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24DETCGY-DET3|no (same contract)
- KXNHLSPREAD-26OCT24DETCGY-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2727, phi -0.734)
- KXNHLSPREAD-26OCT24DETCGY-DET2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2727, phi -1.0)

portfolios: A EV +0.86 (adj +0.27) on $12.24, P(profit) 0.7273, adj growth 2.5 bp · B EV +0.72 (adj +0.23) on $11.01, P(profit) 0.8321, adj growth 2.2 bp · C EV +1.00 (adj +0.33) on $15.76, P(profit) 0.8321, adj growth 3.0 bp · R EV +0.27 (adj +0.08) on $4.00, P(profit) 0.7273, adj growth 3.1 bp

## MIN @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_MIN_win | p_overtime | goals | shots SEA/MIN | SEA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.54 | 0.46 | 0.00 | 6.0 | 28.4/28.9 | 25.5/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.52 | 0.48 | 0.47 | 5.98 | 28.7/29.0 | 25.7/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.57 | 0.43 | 0.00 | 9.21 | 30.1/30.3 | 24.5/23.7 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.089 | 0.53 | 0.47 | 0.00 | 5.97 | 22.7/34.3 | 30.8/19.2 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.48 | 0.52 | 0.45 | 5.89 | 22.7/34.2 | 30.8/19.5 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.060 | 0.48 | 0.52 | 0.00 | 9.31 | 24.5/36.3 | 29.8/19.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Seattle wins by over 1.5 goals YES | 22 | 0.305 | 0.260 | +0.073 | +0.028 | $3.35 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 76 | 0.842 | 0.798 | +0.069 | +0.026 | $10.47 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: higher confidence-adjusted growth (9.69 vs 8.36 bp); relationships: KXNHLSPREAD-26OCT24MINSEA-MIN3|no: REINFORCING (phi 0.287); failure: MIN wins (incl. OT/SO)
- **Minnesota wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes has the higher standalone adjusted growth (9.69 vs 8.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.287); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes: REINFORCING (phi 0.287); failure: MIN wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:WINS_BY_2PLUS (p 0.3055): highest fidelity KXNHLSPREAD-26OCT24MINSEA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes (same contract)
- thesis SEA:WINS (p 0.531): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.4111): highest fidelity KXNHLTEAMTOTAL-26OCT24MINSEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT24MINSEA-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.469, phi -0.623)
- KXNHLSPREAD-26OCT24MINSEA-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2533, phi -0.743)

portfolios: A EV +3.02 (adj +0.98) on $15.31, P(profit) 0.5885, adj growth 8.7 bp · B EV +2.00 (adj +0.76) on $13.82, P(profit) 0.3055, adj growth 7.1 bp · C EV +2.04 (adj +0.78) on $6.44, P(profit) 0.3055, adj growth 7.0 bp · R EV +0.59 (adj +0.22) on $4.00, P(profit) 0.3055, adj growth 8.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
