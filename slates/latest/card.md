# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T14:49:02Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +27.68 | +10.01 | +25.46 | 0.718 | -29.15 | -42.83 | 90.08 |
| B thesis-diversified (joint) ← optimiser card | 149.98 | +27.29 | +12.57 | +23.13 | 0.697 | -30.73 | -43.24 | 114.56 |
| C best expression per thesis | 147.31 | +26.09 | +11.71 | +19.62 | 0.651 | -39.64 | -55.00 | 101.75 |
| R FUNDED research stakes | 22.00 | +4.03 | +2.32 | +0.54 | 0.573 | -9.23 | -11.71 | 0.00 |

## ANA @ PHI  ·  10000 joint draws  ·  414 bet sides mapped, 7 +EV candidates, 4 on card


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
| A.J. Greer: 1+ goals YES | 12 | 0.195 | 0.175 | +0.068 | +0.048 | $8.23 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Denver Barkey: 1+ goals YES | 14 | 0.184 | 0.172 | +0.036 | +0.024 | $4.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 14 | 0.184 | 0.169 | +0.035 | +0.021 | $3.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Noah Cates: 1+ goals YES | 13 | 0.164 | 0.153 | +0.026 | +0.015 | $2.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (43.14 vs 1.16 bp); alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24ANAPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: ANA offense suppressed (<= 2 goals)
- **Denver Barkey: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (9.57 vs 7.30 bp); relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT24ANAPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: PHI offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24ANAPHI-PHITSANHEIM6-1|yes; why: higher confidence-adjusted growth (7.30 vs 4.19 bp); despite a smaller raw edge (+0.035 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT24ANAPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: PHI offense suppressed (<= 2 goals)
- **Noah Cates: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (7.30 vs 4.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3451): highest fidelity KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.403): highest fidelity KXNHLAST-26OCT24ANAPHI-PHITSANHEIM6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4306, phi -0.23)
- KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3834, phi -0.195)
- KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3834, phi -0.209)
- KXNHLGOAL-26OCT24ANAPHI-PHINCATES27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3834, phi -0.175)

portfolios: A EV +5.90 (adj +3.10) on $19.29, P(profit) 0.4303, adj growth 28.4 bp · B EV +6.87 (adj +4.61) on $19.21, P(profit) 0.5538, adj growth 41.5 bp · C EV +7.77 (adj +5.31) on $17.74, P(profit) 0.3444, adj growth 45.2 bp · R EV +1.59 (adj +1.12) on $3.00, P(profit) 0.1951, adj growth 38.2 bp

## LAK @ NJD  ·  10000 joint draws  ·  414 bet sides mapped, 14 +EV candidates, 4 on card


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
| Jack Hughes: 1+ goals NO | 62 | 0.701 | 0.678 | +0.064 | +0.042 | $10.23 | FUNDED_RESEARCH | $3 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 62 | 0.790 | 0.667 | +0.154 | +0.030 | $10.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Alex Laferriere: 1+ goals YES | 23 | 0.278 | 0.259 | +0.036 | +0.016 | $3.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 56 | 0.626 | 0.590 | +0.049 | +0.013 | $6.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (16.35 vs 8.61 bp); despite a smaller raw edge (+0.064 vs +0.154/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: NJD offense succeeds (4+ goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no has the higher standalone adjusted growth (16.35 vs 8.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.062); they share one thesis budget; relationships: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: NJD offense succeeds (4+ goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24LANJ-NJ3|no; why: KXNHLSPREAD-26OCT24LANJ-NJ3|no has the higher standalone adjusted growth (4.06 vs 3.10 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.144); relationships: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.22); failure: LAK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT24LANJ-5|no; why: higher confidence-adjusted growth (1.56 vs 0.31 bp); wins across more scripts (relative breadth 0.962 vs 0.386); alternative not eligible: confidence-adjusted EV +0.0051 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.22); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.11.
- thesis NJD:SUPPRESSED (p 0.4061): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.3022): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT24LANJ-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4578): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24LANJ-NJ2|no (same contract)
- KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3725, phi -0.249)
- KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.0 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3725, phi -0.201)
- KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4795, phi -0.262)
- KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3022, phi -0.3)

portfolios: A EV +2.65 (adj +0.82) on $19.29, P(profit) 0.6288, adj growth 7.7 bp · B EV +4.54 (adj +1.53) on $30.13, P(profit) 0.6673, adj growth 14.5 bp · C EV +4.28 (adj +2.00) on $48.77, P(profit) 0.677, adj growth 18.0 bp · R EV +0.30 (adj +0.20) on $3.00, P(profit) 0.7006, adj growth 7.4 bp

## SJS @ BOS  ·  10000 joint draws  ·  470 bet sides mapped, 4 +EV candidates, 4 on card


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
| Mark Kastelic: 1+ goals YES | 11 | 0.141 | 0.132 | +0.024 | +0.015 | $2.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Michael Misa: 1+ goals YES | 16 | 0.199 | 0.185 | +0.029 | +0.016 | $3.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Macklin Celebrini: 1+ goals YES | 35 | 0.393 | 0.381 | +0.028 | +0.015 | $4.07 | FUNDED_RESEARCH | $2 | SJS:OFFENSE_4PLUS | DIRECT (0.60) | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: 1+ goals YES | 19 | 0.223 | 0.213 | +0.022 | +0.013 | $2.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT24SJBOS-9|yes; why: higher confidence-adjusted growth (4.94 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.842 vs 0.369); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24SJBOS-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24SJBOS-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: BOS offense suppressed (<= 2 goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes; why: higher confidence-adjusted growth (3.88 vs 2.22 bp); relationships: KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT24SJBOS-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: SJS offense suppressed (<= 2 goals)
- **Macklin Celebrini: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-SJKSHERWOOD44-1|yes; why: higher confidence-adjusted growth (2.22 vs 2.20 bp); relationships: KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24SJBOS-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT24SJBOS-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: SJS offense suppressed (<= 2 goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes has the higher standalone adjusted growth (2.22 vs 2.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24SJBOS-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis SJS:OFFENSE_4PLUS (p 0.3429): highest fidelity KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.4963): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.303, phi -0.16)
- KXNHLGOAL-26OCT24SJBOS-SJMMISA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4378, phi -0.201)
- KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 40% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4378, phi -0.327)
- KXNHLGOAL-26OCT24SJBOS-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4378, phi -0.218)

portfolios: A EV +1.76 (adj +1.02) on $12.93, P(profit) 0.4681, adj growth 9.2 bp · B EV +1.72 (adj +1.00) on $12.59, P(profit) 0.4681, adj growth 9.1 bp · C EV +0.45 (adj +0.25) on $5.98, P(profit) 0.3934, adj growth 2.2 bp · R EV +0.15 (adj +0.08) on $2.00, P(profit) 0.3934, adj growth 2.8 bp

## NYR @ OTT  ·  10000 joint draws  ·  440 bet sides mapped, 1 +EV candidates, 1 on card


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
| Gabe Perreault: 1+ goals YES | 22 | 0.257 | 0.244 | +0.025 | +0.012 | $2.56 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
- **Gabe Perreault: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (1.76 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis NYR:OFFENSE_4PLUS (p 0.3534): highest fidelity KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes (same contract)
- KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4249, phi -0.245)

portfolios: A EV +0.34 (adj +0.16) on $3.14, P(profit) 0.257, adj growth 1.4 bp · B EV +0.28 (adj +0.13) on $2.56, P(profit) 0.257, adj growth 1.2 bp · C EV +0.40 (adj +0.19) on $3.76, P(profit) 0.257, adj growth 1.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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

## BUF @ WSH  ·  10000 joint draws  ·  436 bet sides mapped, 1 +EV candidates, 1 on card


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
| Ryan Leonard: 1+ assists YES | 26 | 0.387 | 0.294 | +0.113 | +0.021 | $4.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24BUFWSH-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (4.85 vs 0.29 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0052 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4361): highest fidelity KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes (same contract)
- KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.2 pts; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3506, phi -0.279)

portfolios: A EV +3.19 (adj +0.59) on $7.72, P(profit) 0.3865, adj growth 5.0 bp · B EV +1.75 (adj +0.33) on $4.23, P(profit) 0.3865, adj growth 3.0 bp · C EV +2.57 (adj +0.48) on $6.21, P(profit) 0.3865, adj growth 4.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ CBJ  ·  10000 joint draws  ·  410 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_VGK_win | p_overtime | goals | shots CBJ/VGK | CBJ/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.44 | 0.56 | 0.00 | 5.99 | 27.3/27.4 | 23.5/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.45 | 5.95 | 27.4/27.6 | 24.2/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.45 | 0.55 | 0.00 | 9.23 | 28.9/28.8 | 22.2/23.0 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.071 | 0.39 | 0.61 | 0.00 | 5.96 | 21.8/32.0 | 27.9/18.7 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.066 | 0.47 | 0.53 | 0.00 | 6.0 | 32.3/22.1 | 18.5/28.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.44 | 0.56 | 0.00 | 3.45 | 26.0/26.0 | 23.9/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 15 | 0.183 | 0.172 | +0.024 | +0.013 | $2.60 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Adam Fantilli: 1+ assists NO | 62 | 0.693 | 0.646 | +0.057 | +0.010 | $5.35 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (2.82 vs 0.87 bp); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no: MOSTLY_INDEPENDENT (phi -0.041); failure: CBJ offense suppressed (<= 2 goals)
- **Adam Fantilli: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24VGKCBJ-CBJVNICHUSHKIN43-1|no; why: higher confidence-adjusted growth (0.95 vs 0.19 bp); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.041); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3426): highest fidelity KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.4391): highest fidelity KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no (same contract)
- KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4391, phi -0.225)
- KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3426, phi -0.251)

portfolios: A EV +1.10 (adj +0.35) on $10.46, P(profit) 0.7565, adj growth 3.1 bp · B EV +0.87 (adj +0.30) on $7.95, P(profit) 0.7565, adj growth 2.7 bp · C EV +1.27 (adj +0.44) on $11.66, P(profit) 0.7565, adj growth 3.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ STL  ·  10000 joint draws  ·  422 bet sides mapped, 13 +EV candidates, 4 on card


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
| St. Louis wins by over 1.5 goals YES | 22 | 0.306 | 0.260 | +0.074 | +0.028 | $3.89 | FUNDED_RESEARCH | $1 | STL:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Robert Thomas: 1+ goals YES | 23 | 0.290 | 0.271 | +0.047 | +0.029 | $5.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 13 | 0.167 | 0.151 | +0.029 | +0.013 | $1.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 68 | 0.727 | 0.712 | +0.032 | +0.017 | $7.63 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **St. Louis wins by over 1.5 goals YES** — thesis: STL wins by 2+; alternative: KXNHLSPREAD-26OCT24CARSTL-CAR2|no; why: higher confidence-adjusted growth (9.73 vs 6.10 bp); relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: REINFORCING (phi 0.179); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: REINFORCING (phi 0.188); KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.144); failure: CAR wins (incl. OT/SO)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-STL2|yes has the higher standalone adjusted growth (9.73 vs 9.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.179); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-STL2|yes: REINFORCING (phi 0.179); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-STL2|yes has the higher standalone adjusted growth (9.73 vs 3.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.188); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-STL2|yes: REINFORCING (phi 0.188); KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: STL offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-STL2|yes has the higher standalone adjusted growth (9.73 vs 2.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.144); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-STL2|yes: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis STL:WINS_BY_2PLUS (p 0.3056): highest fidelity KXNHLSPREAD-26OCT24CARSTL-STL2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-STL2|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.4257): highest fidelity KXNHLTEAMTOTAL-26OCT24CARSTL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.5186): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-STL2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT24CARSTL-STL2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.4814, phi -0.639)
- KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3549, phi -0.242)
- KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3549, phi -0.193)
- KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4043, phi -0.227)

portfolios: A EV +3.80 (adj +1.13) on $19.29, P(profit) 0.4953, adj growth 10.1 bp · B EV +3.01 (adj +1.46) on $18.68, P(profit) 0.492, adj growth 13.3 bp · C EV +2.60 (adj +1.00) on $8.19, P(profit) 0.3056, adj growth 8.7 bp · R EV +0.41 (adj +0.17) on $3.00, P(profit) 0.3056, adj growth 6.3 bp

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
| Leon Draisaitl: 1+ assists NO | 37 | 0.485 | 0.407 | +0.099 | +0.021 | $5.22 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.75) | EVIDENCE_MIXED | D |
| Auston Matthews: 1+ assists NO | 57 | 0.642 | 0.601 | +0.055 | +0.014 | $5.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Connor McDavid: 2+ assists NO | 67 | 0.741 | 0.698 | +0.055 | +0.012 | $6.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (4.00 vs 1.54 bp); relationships: KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.098); failure: EDM offense succeeds (4+ goals)
- **Auston Matthews: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT24TOREDM-4|no; why: higher confidence-adjusted growth (1.72 vs 1.05 bp); wins across more scripts (relative breadth 0.998 vs 0.382); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense succeeds (4+ goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no has the higher standalone adjusted growth (4.00 vs 1.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.098); they share one thesis budget; relationships: KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.098); KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, EDM shot control · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis EDM:SUPPRESSED (p 0.25): highest fidelity KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.4321): highest fidelity KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no (same contract)
- KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5538, phi -0.303)
- KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3474, phi -0.269)
- KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5538, phi -0.334)

portfolios: A EV +2.77 (adj +0.61) on $19.29, P(profit) 0.6794, adj growth 5.5 bp · B EV +2.39 (adj +0.53) on $17.35, P(profit) 0.6794, adj growth 4.9 bp · C EV +2.90 (adj +0.64) on $16.83, P(profit) 0.4855, adj growth 5.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TBL @ UTA  ·  10000 joint draws  ·  430 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TBL_win | p_overtime | goals | shots UTA/TBL | UTA/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.61 | 0.39 | 0.00 | 6.01 | 27.0/26.9 | 23.9/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.49 | 5.96 | 26.9/26.9 | 23.7/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.63 | 0.37 | 0.00 | 9.29 | 28.5/28.6 | 23.3/21.6 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.077 | 0.69 | 0.31 | 0.00 | 5.98 | 31.2/20.9 | 18.3/26.5 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.067 | 0.55 | 0.45 | 0.00 | 5.99 | 21.4/31.8 | 28.4/17.9 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.48 | 0.52 | 0.45 | 5.91 | 21.5/31.6 | 28.1/18.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ CGY  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 2 on card


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
| Jonathan Castagna: 1+ goals YES | 10 | 0.147 | 0.125 | +0.041 | +0.019 | $2.85 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Detroit wins by over 2.5 goals NO | 77 | 0.832 | 0.798 | +0.050 | +0.016 | $12.10 | FUNDED_RESEARCH | $4 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24DETCGY-DET3|no; why: higher confidence-adjusted growth (7.99 vs 3.37 bp); despite a smaller raw edge (+0.041 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT24DETCGY-DET3|no: MOSTLY_INDEPENDENT (phi 0.102); failure: CGY offense suppressed (<= 2 goals)
- **Detroit wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24DETCGY-DET2|no; why: higher confidence-adjusted growth (3.37 vs 2.39 bp); despite a smaller raw edge (+0.050 vs +0.052/contract); relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.102); failure: DET wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:OFFENSE_4PLUS (p 0.3631): highest fidelity KXNHLSPREAD-26OCT24DETCGY-DET3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT24DETCGY-DET3|no (same contract)
- thesis CGY:WINS (p 0.5057): highest fidelity KXNHLSPREAD-26OCT24DETCGY-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24DETCGY-DET3|no (same contract)
- KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4195, phi -0.188)
- KXNHLSPREAD-26OCT24DETCGY-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2727, phi -0.734)

portfolios: A EV +2.67 (adj +1.08) on $19.29, P(profit) 0.7483, adj growth 9.4 bp · B EV +1.85 (adj +0.75) on $14.95, P(profit) 0.8433, adj growth 6.9 bp · C EV +1.27 (adj +0.41) on $20.00, P(profit) 0.8321, adj growth 3.7 bp · R EV +0.25 (adj +0.08) on $4.00, P(profit) 0.8321, adj growth 3.0 bp

## MIN @ SEA  ·  10000 joint draws  ·  420 bet sides mapped, 6 +EV candidates, 3 on card


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
| Shane Wright: 1+ goals YES | 14 | 0.197 | 0.180 | +0.048 | +0.031 | $5.11 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Seattle wins by over 1.5 goals YES | 22 | 0.305 | 0.260 | +0.073 | +0.028 | $3.58 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 76 | 0.842 | 0.796 | +0.069 | +0.023 | $13.64 | FUNDED_RESEARCH | $4 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: higher confidence-adjusted growth (16.77 vs 9.69 bp); despite a smaller raw edge (+0.048 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.891 vs 0.536); relationships: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes: REINFORCING (phi 0.151); KXNHLSPREAD-26OCT24MINSEA-MIN3|no: MOSTLY_INDEPENDENT (phi 0.096); failure: SEA offense suppressed (<= 2 goals)
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: higher confidence-adjusted growth (9.69 vs 6.81 bp); relationships: KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: REINFORCING (phi 0.151); KXNHLSPREAD-26OCT24MINSEA-MIN3|no: REINFORCING (phi 0.287); failure: MIN wins (incl. OT/SO)
- **Minnesota wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes has the higher standalone adjusted growth (9.69 vs 6.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.287); they share one thesis budget; relationships: KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.096); KXNHLSPREAD-26OCT24MINSEA-SEA2|yes: REINFORCING (phi 0.287); failure: MIN wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4111): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.3055): highest fidelity KXNHLSPREAD-26OCT24MINSEA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes (same contract)
- thesis SEA:WINS (p 0.531): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3646, phi -0.194)
- KXNHLSPREAD-26OCT24MINSEA-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.469, phi -0.623)
- KXNHLSPREAD-26OCT24MINSEA-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2533, phi -0.743)

portfolios: A EV +3.50 (adj +1.15) on $19.29, P(profit) 0.3055, adj growth 10.2 bp · B EV +4.01 (adj +1.93) on $22.33, P(profit) 0.4143, adj growth 17.5 bp · C EV +2.59 (adj +0.99) on $8.17, P(profit) 0.3055, adj growth 8.6 bp · R EV +1.32 (adj +0.67) on $7.00, P(profit) 0.4143, adj growth 23.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
