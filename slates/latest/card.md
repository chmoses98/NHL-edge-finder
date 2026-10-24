# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T13:49:06Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +26.94 | +9.06 | +25.33 | 0.739 | -24.92 | -37.70 | 82.20 |
| B thesis-diversified (joint) ← optimiser card | 149.11 | +24.35 | +11.19 | +20.39 | 0.707 | -25.35 | -37.00 | 103.63 |
| C best expression per thesis | 150.00 | +26.16 | +11.23 | +21.37 | 0.690 | -32.34 | -45.91 | 100.66 |
| R FUNDED research stakes | 24.00 | +3.25 | +1.72 | +1.67 | 0.626 | -7.29 | -9.19 | 0.00 |

## ANA @ PHI  ·  10000 joint draws  ·  414 bet sides mapped, 6 +EV candidates, 4 on card


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
| A.J. Greer: 1+ goals YES | 12 | 0.195 | 0.175 | +0.068 | +0.048 | $7.03 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Denver Barkey: 1+ goals YES | 14 | 0.184 | 0.172 | +0.036 | +0.024 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 19 | 0.237 | 0.222 | +0.036 | +0.021 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 14 | 0.184 | 0.165 | +0.035 | +0.017 | $2.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24ANAPHI-ANAJLACOMBE2-1|yes; why: higher confidence-adjusted growth (43.14 vs 0.81 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: ANA offense suppressed (<= 2 goals)
- **Denver Barkey: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (9.57 vs 5.93 bp); despite a smaller raw edge (+0.036 vs +0.036/contract); relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (5.93 vs 4.90 bp); relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PHI offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes has the higher standalone adjusted growth (5.93 vs 4.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3451): highest fidelity KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.403): highest fidelity KXNHLAST-26OCT24ANAPHI-PHITSANHEIM6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4306, phi -0.23)
- KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3834, phi -0.195)
- KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3834, phi -0.213)
- KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3834, phi -0.209)

portfolios: A EV +4.98 (adj +2.52) on $16.89, P(profit) 0.3998, adj growth 23.3 bp · B EV +5.96 (adj +3.92) on $17.16, P(profit) 0.5969, adj growth 35.9 bp · C EV +6.17 (adj +4.22) on $14.99, P(profit) 0.3885, adj growth 37.1 bp · R EV +1.06 (adj +0.75) on $2.00, P(profit) 0.1951, adj growth 26.9 bp

## LAK @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 11 +EV candidates, 4 on card


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
| Joel Edmundson: 1+ goals YES | 3 | 0.058 | 0.050 | +0.026 | +0.018 | $1.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 66 | 0.818 | 0.712 | +0.142 | +0.036 | $10.22 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 63 | 0.701 | 0.679 | +0.054 | +0.033 | $10.22 | FUNDED_RESEARCH | $3 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 75 | 0.786 | 0.776 | +0.023 | +0.013 | $6.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24LANJ-NJ2|no; why: higher confidence-adjusted growth (21.36 vs 3.73 bp); despite a smaller raw edge (+0.026 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: LAK offense suppressed (<= 2 goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT24LANJ-5|no; why: higher confidence-adjusted growth (13.25 vs 0.31 bp); wins across more scripts (relative breadth 0.993 vs 0.386); alternative not eligible: confidence-adjusted EV +0.0051 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24LANJ-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: LAK offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (10.40 vs 8.61 bp); despite a smaller raw edge (+0.054 vs +0.154/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24LANJ-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: NJD offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no selected over broad KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.89 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24LANJ-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.11.
- thesis LAK:SUPPRESSED (p 0.4795): highest fidelity KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no (same contract)
- thesis NJD:SUPPRESSED (p 0.4061): highest fidelity KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no selected over broad KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.89 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis LAK:OFFENSE_4PLUS (p 0.3022): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT24LANJ-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24LANJ-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4795, phi -0.122)
- KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.3 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3022, phi -0.223)
- KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3725, phi -0.249)
- KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3725, phi -0.223)
- override: Player prop expression KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no selected over broad KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.89 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.78 (adj +0.69) on $16.89, P(profit) 0.6598, adj growth 6.6 bp · B EV +4.70 (adj +2.19) on $29.06, P(profit) 0.5983, adj growth 20.6 bp · C EV +5.50 (adj +1.92) on $40.65, P(profit) 0.5709, adj growth 17.9 bp · R EV +0.25 (adj +0.15) on $3.00, P(profit) 0.7006, adj growth 5.7 bp

## SJS @ BOS  ·  10000 joint draws  ·  470 bet sides mapped, 5 +EV candidates, 4 on card


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
| Pavel Zacha: 1+ goals YES | 27 | 0.320 | 0.306 | +0.036 | +0.022 | $4.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Mark Kastelic: 1+ goals YES | 11 | 0.141 | 0.132 | +0.024 | +0.015 | $2.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Macklin Celebrini: 1+ goals YES | 35 | 0.393 | 0.381 | +0.028 | +0.015 | $3.41 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | DIRECT (0.60) | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: 1+ goals YES | 19 | 0.223 | 0.213 | +0.022 | +0.013 | $2.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT24SJBOS-3|yes; why: higher confidence-adjusted growth (5.39 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.903 vs 0.768); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT24SJBOS-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: BOS offense suppressed (<= 2 goals)
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes has the higher standalone adjusted growth (5.39 vs 4.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24SJBOS-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: BOS offense suppressed (<= 2 goals)
- **Macklin Celebrini: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-SJKSHERWOOD44-1|yes; why: higher confidence-adjusted growth (2.22 vs 2.20 bp); relationships: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24SJBOS-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: SJS offense suppressed (<= 2 goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes has the higher standalone adjusted growth (2.22 vs 2.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis BOS:OFFENSE_4PLUS (p 0.4963): highest fidelity KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3429): highest fidelity KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.303): highest fidelity KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no (same contract)
- KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.303, phi -0.224)
- KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.303, phi -0.16)
- KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 40% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4378, phi -0.327)
- KXNHLGOAL-26OCT24SJBOS-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4378, phi -0.218)

portfolios: A EV +1.49 (adj +0.89) on $15.20, P(profit) 0.5055, adj growth 8.2 bp · B EV +1.56 (adj +0.95) on $12.41, P(profit) 0.4698, adj growth 8.7 bp · C EV +1.37 (adj +0.80) on $17.04, P(profit) 0.4918, adj growth 7.2 bp · R EV +0.08 (adj +0.04) on $1.00, P(profit) 0.3934, adj growth 1.5 bp

## NYR @ OTT  ·  10000 joint draws  ·  440 bet sides mapped, 2 +EV candidates, 2 on card


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
| Gabe Perreault: 1+ goals YES | 21 | 0.257 | 0.243 | +0.035 | +0.021 | $3.78 | FUNDED_RESEARCH | $1 | NYR:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 8 | 0.110 | 0.095 | +0.025 | +0.010 | $1.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Gabe Perreault: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (5.62 vs 0.05 bp); despite a smaller raw edge (+0.035 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NYR offense suppressed (<= 2 goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24NYROTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (2.81 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.037/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis NYR:OFFENSE_4PLUS (p 0.3534): highest fidelity KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4016): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4249, phi -0.245)
- KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3767, phi -0.166)

portfolios: A EV +1.30 (adj +0.64) on $6.16, P(profit) 0.3394, adj growth 5.8 bp · B EV +1.01 (adj +0.52) on $5.17, P(profit) 0.3394, adj growth 4.8 bp · C EV +0.84 (adj +0.50) on $5.28, P(profit) 0.257, adj growth 4.5 bp · R EV +0.16 (adj +0.10) on $1.00, P(profit) 0.257, adj growth 3.5 bp

## NSH @ PIT  ·  10000 joint draws  ·  414 bet sides mapped, 0 +EV candidates, 0 on card


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

## BUF @ WSH  ·  10000 joint draws  ·  436 bet sides mapped, 2 +EV candidates, 2 on card


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
| Tage Thompson: 1+ goals NO | 63 | 0.693 | 0.675 | +0.047 | +0.029 | $11.63 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 26 | 0.387 | 0.294 | +0.113 | +0.021 | $3.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no; why: higher confidence-adjusted growth (7.81 vs 0.70 bp); despite a smaller raw edge (+0.047 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: BUF offense succeeds (4+ goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24BUFWSH-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (4.85 vs 0.29 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0052 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:SUPPRESSED (p 0.4097): highest fidelity KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no (same contract)
- thesis WSH:OFFENSE_4PLUS (p 0.4361): highest fidelity KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes (same contract)
- KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3743, phi -0.259)
- KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.2 pts; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3506, phi -0.279)

portfolios: A EV +3.28 (adj +0.82) on $13.51, P(profit) 0.3865, adj growth 7.3 bp · B EV +2.36 (adj +0.80) on $15.29, P(profit) 0.6931, adj growth 7.4 bp · C EV +3.30 (adj +1.11) on $21.39, P(profit) 0.6931, adj growth 10.0 bp · R EV +0.22 (adj +0.13) on $3.00, P(profit) 0.6931, adj growth 4.9 bp

## VGK @ CBJ  ·  10000 joint draws  ·  418 bet sides mapped, 2 +EV candidates, 2 on card


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
| Jack Eichel: 1+ assists NO | 42 | 0.568 | 0.449 | +0.131 | +0.012 | $2.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.75) | CALIBRATION_WARNING | D |
| Mark Stone: 1+ assists NO | 56 | 0.620 | 0.588 | +0.043 | +0.010 | $3.05 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Jack Eichel: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24VGKCBJ-VGKMSTONE61-1|no; why: higher confidence-adjusted growth (1.36 vs 0.94 bp); evidence CALIBRATION_WARNING vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT24VGKCBJ-VGKMSTONE61-1|no: MOSTLY_INDEPENDENT (phi 0.146); failure: VGK offense succeeds (4+ goals)
- **Mark Stone: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no has the higher standalone adjusted growth (1.36 vs 0.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.146); they share one thesis budget; relationships: KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.146); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis VGK:SUPPRESSED (p 0.409): highest fidelity KXNHLAST-26OCT24VGKCBJ-VGKMSTONE61-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.363, phi -0.288)
- KXNHLAST-26OCT24VGKCBJ-VGKMSTONE61-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.363, phi -0.26)

portfolios: A EV +2.52 (adj +0.31) on $13.51, P(profit) 0.5677, adj growth 2.6 bp · B EV +1.08 (adj +0.13) on $5.90, P(profit) 0.5677, adj growth 1.2 bp · C EV +1.33 (adj +0.13) on $4.45, P(profit) 0.5677, adj growth 1.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ STL  ·  10000 joint draws  ·  422 bet sides mapped, 10 +EV candidates, 4 on card


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
| St. Louis wins by over 1.5 goals YES | 22 | 0.306 | 0.260 | +0.074 | +0.028 | $3.29 | FUNDED_RESEARCH | $1 | STL:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Robert Thomas: 1+ goals YES | 23 | 0.290 | 0.266 | +0.047 | +0.024 | $3.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 76 | 0.830 | 0.792 | +0.057 | +0.020 | $8.07 | FUNDED_RESEARCH | $3 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 68 | 0.727 | 0.712 | +0.032 | +0.017 | $5.76 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **St. Louis wins by over 1.5 goals YES** — thesis: STL wins by 2+; alternative: KXNHLSPREAD-26OCT24CARSTL-CAR2|no; why: higher confidence-adjusted growth (9.73 vs 6.10 bp); relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: REINFORCING (phi 0.179); KXNHLSPREAD-26OCT24CARSTL-CAR3|no: DUPLICATIVE (phi 0.3); KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.144); failure: CAR wins (incl. OT/SO)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-STL2|yes has the higher standalone adjusted growth (9.73 vs 6.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.179); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-STL2|yes: REINFORCING (phi 0.179); KXNHLSPREAD-26OCT24CARSTL-CAR3|no: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: STL offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-STL2|yes has the higher standalone adjusted growth (9.73 vs 4.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.300); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-STL2|yes: DUPLICATIVE (phi 0.3); KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.133); failure: CAR wins by 2+
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-STL2|yes has the higher standalone adjusted growth (9.73 vs 2.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.144); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-STL2|yes: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLSPREAD-26OCT24CARSTL-CAR3|no: MOSTLY_INDEPENDENT (phi 0.133); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis STL:WINS_BY_2PLUS (p 0.3056): highest fidelity KXNHLSPREAD-26OCT24CARSTL-STL2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-STL2|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.4257): highest fidelity KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-STL2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.5186): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-STL2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT24CARSTL-STL2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.4814, phi -0.639)
- KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3549, phi -0.242)
- KXNHLSPREAD-26OCT24CARSTL-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2727, phi -0.739)
- KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4043, phi -0.227)

portfolios: A EV +3.30 (adj +1.09) on $16.89, P(profit) 0.4702, adj growth 9.8 bp · B EV +2.56 (adj +1.07) on $20.45, P(profit) 0.4575, adj growth 9.9 bp · C EV +2.11 (adj +0.81) on $6.66, P(profit) 0.3056, adj growth 7.2 bp · R EV +0.63 (adj +0.25) on $6.00, P(profit) 0.6798, adj growth 9.0 bp

## TOR @ EDM  ·  10000 joint draws  ·  448 bet sides mapped, 3 +EV candidates, 3 on card


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
| Kirill Marchenko: 1+ assists NO | 63 | 0.702 | 0.661 | +0.056 | +0.015 | $6.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Leon Draisaitl: 1+ assists NO | 38 | 0.485 | 0.410 | +0.089 | +0.014 | $3.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.75) | EVIDENCE_MIXED | D |
| Auston Matthews: 1+ assists NO | 57 | 0.642 | 0.601 | +0.055 | +0.014 | $4.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Kirill Marchenko: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (2.10 vs 1.72 bp); relationships: KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.077); failure: TOR offense succeeds (4+ goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-EDMRNUGENTHOPKINS93-1|no; why: higher confidence-adjusted growth (1.77 vs 0.56 bp); alternative not eligible: confidence-adjusted EV +0.0077 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: EDM offense succeeds (4+ goals)
- **Auston Matthews: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no has the higher standalone adjusted growth (2.10 vs 1.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.077); they share one thesis budget; relationships: KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi 0.077); KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: TOR offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, EDM shot control · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:SUPPRESSED (p 0.4321): highest fidelity KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no (same contract)
- thesis EDM:SUPPRESSED (p 0.25): highest fidelity KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no (same contract)
- KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3474, phi -0.251)
- KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.5 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5538, phi -0.303)
- KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3474, phi -0.269)

portfolios: A EV +2.28 (adj +0.46) on $16.89, P(profit) 0.6663, adj growth 4.1 bp · B EV +1.69 (adj +0.36) on $14.00, P(profit) 0.6663, adj growth 3.4 bp · C EV +1.81 (adj +0.37) on $13.67, P(profit) 0.7022, adj growth 3.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TBL @ UTA  ·  10000 joint draws  ·  430 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TBL_win | p_overtime | goals | shots UTA/TBL | UTA/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.61 | 0.39 | 0.00 | 6.01 | 26.7/26.8 | 23.8/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.49 | 0.51 | 0.49 | 5.92 | 26.9/26.9 | 23.7/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.61 | 0.39 | 0.00 | 9.39 | 28.4/28.5 | 22.9/21.6 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.075 | 0.67 | 0.33 | 0.00 | 5.99 | 31.6/21.3 | 18.6/27.1 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.062 | 0.55 | 0.45 | 0.00 | 6.03 | 21.2/31.4 | 27.9/17.5 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.057 | 0.50 | 0.50 | 0.48 | 5.89 | 21.5/31.9 | 28.6/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anthony Cirelli: 1+ goals YES | 17 | 0.216 | 0.193 | +0.036 | +0.013 | $2.12 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Anthony Cirelli: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24TBUTA-TBACIRELLI71-1|yes; why: higher confidence-adjusted growth (2.52 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: TBL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.3396): highest fidelity KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes (same contract)
- KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.4411, phi -0.232)

portfolios: A EV +0.73 (adj +0.27) on $3.68, P(profit) 0.2156, adj growth 2.3 bp · B EV +0.42 (adj +0.15) on $2.12, P(profit) 0.2156, adj growth 1.4 bp · C EV +0.59 (adj +0.22) on $2.96, P(profit) 0.2156, adj growth 1.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Detroit wins by over 2.5 goals NO | 77 | 0.832 | 0.798 | +0.050 | +0.016 | $10.75 | FUNDED_RESEARCH | $3 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit wins by over 1.5 goals NO | 66 | 0.727 | 0.691 | +0.052 | +0.015 | $1.46 | FUNDED_RESEARCH | $1 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Detroit wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24DETCGY-DET2|no; why: higher confidence-adjusted growth (3.37 vs 2.39 bp); despite a smaller raw edge (+0.050 vs +0.052/contract); relationships: KXNHLSPREAD-26OCT24DETCGY-DET2|no: DUPLICATIVE (phi 0.734); failure: DET wins by 2+
- **Detroit wins by over 1.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24DETCGY-DET3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24DETCGY-DET3|no has the higher standalone adjusted growth (3.37 vs 2.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.734); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24DETCGY-DET3|no: DUPLICATIVE (phi 0.734); failure: DET wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:WINS (p 0.5057): highest fidelity KXNHLSPREAD-26OCT24DETCGY-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24DETCGY-DET3|no (same contract)
- KXNHLSPREAD-26OCT24DETCGY-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2727, phi -0.734)
- KXNHLSPREAD-26OCT24DETCGY-DET2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2727, phi -1.0)

portfolios: A EV +0.94 (adj +0.29) on $13.51, P(profit) 0.7273, adj growth 2.7 bp · B EV +0.79 (adj +0.26) on $12.21, P(profit) 0.8321, adj growth 2.4 bp · C EV +1.03 (adj +0.34) on $16.26, P(profit) 0.8321, adj growth 3.1 bp · R EV +0.27 (adj +0.08) on $4.00, P(profit) 0.7273, adj growth 3.1 bp

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
| Seattle wins by over 1.5 goals YES | 22 | 0.305 | 0.260 | +0.073 | +0.028 | $3.71 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 76 | 0.842 | 0.798 | +0.069 | +0.026 | $11.63 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: higher confidence-adjusted growth (9.69 vs 8.36 bp); relationships: KXNHLSPREAD-26OCT24MINSEA-MIN3|no: REINFORCING (phi 0.287); failure: MIN wins (incl. OT/SO)
- **Minnesota wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes has the higher standalone adjusted growth (9.69 vs 8.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.287); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes: REINFORCING (phi 0.287); failure: MIN wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:WINS_BY_2PLUS (p 0.3055): highest fidelity KXNHLSPREAD-26OCT24MINSEA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes (same contract)
- thesis SEA:WINS (p 0.531): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.4111): highest fidelity KXNHLTEAMTOTAL-26OCT24MINSEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT24MINSEA-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.469, phi -0.623)
- KXNHLSPREAD-26OCT24MINSEA-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2533, phi -0.743)

portfolios: A EV +3.33 (adj +1.08) on $16.89, P(profit) 0.5885, adj growth 9.5 bp · B EV +2.22 (adj +0.84) on $15.34, P(profit) 0.3055, adj growth 7.9 bp · C EV +2.10 (adj +0.81) on $6.65, P(profit) 0.3055, adj growth 7.2 bp · R EV +0.59 (adj +0.22) on $4.00, P(profit) 0.3055, adj growth 8.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
