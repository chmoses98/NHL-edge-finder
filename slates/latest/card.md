# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T15:19:06Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +26.57 | +9.97 | +25.02 | 0.732 | -24.56 | -37.26 | 91.44 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +24.23 | +11.53 | +21.35 | 0.718 | -23.84 | -34.30 | 107.79 |
| C best expression per thesis | 150.00 | +24.51 | +11.47 | +19.25 | 0.671 | -31.54 | -44.53 | 103.71 |
| R FUNDED research stakes | 21.00 | +2.98 | +1.75 | +0.80 | 0.585 | -7.45 | -8.85 | 0.00 |

## ANA @ PHI  ·  10000 joint draws  ·  416 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_ANA_win | p_overtime | goals | shots PHI/ANA | PHI/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.60 | 0.40 | 0.00 | 6.03 | 26.7/27.1 | 23.9/22.6 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.105 | 0.50 | 0.50 | 0.00 | 5.98 | 21.3/32.3 | 28.6/17.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.52 | 0.48 | 0.50 | 5.95 | 26.6/27.2 | 23.9/23.4 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.45 | 0.55 | 0.48 | 5.93 | 21.6/32.7 | 29.3/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.54 | 0.46 | 0.00 | 9.26 | 28.3/28.8 | 23.3/22.0 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.065 | 0.46 | 0.54 | 0.00 | 9.12 | 22.6/34.0 | 27.5/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 12 | 0.204 | 0.181 | +0.076 | +0.054 | $6.71 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Denver Barkey: 1+ goals YES | 14 | 0.187 | 0.174 | +0.038 | +0.025 | $3.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 14 | 0.186 | 0.171 | +0.038 | +0.022 | $3.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Noah Cates: 1+ goals YES | 13 | 0.162 | 0.151 | +0.024 | +0.013 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24ANAPHI-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (55.34 vs 1.15 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0100 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT24ANAPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: ANA offense suppressed (<= 2 goals)
- **Denver Barkey: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (10.87 vs 8.67 bp); relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT24ANAPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PHI offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes has the higher standalone adjusted growth (10.87 vs 8.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT24ANAPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense suppressed (<= 2 goals)
- **Noah Cates: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes has the higher standalone adjusted growth (10.87 vs 3.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3508): highest fidelity KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3952): highest fidelity KXNHLAST-26OCT24ANAPHI-PHITSANHEIM6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4295, phi -0.234)
- KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3846, phi -0.199)
- KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3846, phi -0.205)
- KXNHLGOAL-26OCT24ANAPHI-PHINCATES27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3846, phi -0.19)

portfolios: A EV +6.21 (adj +3.46) on $16.68, P(profit) 0.6437, adj growth 32.1 bp · B EV +5.97 (adj +4.06) on $14.88, P(profit) 0.4762, adj growth 37.5 bp · C EV +7.09 (adj +4.97) on $14.66, P(profit) 0.3534, adj growth 44.2 bp · R EV +1.20 (adj +0.85) on $2.00, P(profit) 0.2037, adj growth 30.8 bp

## LAK @ NJD  ·  10000 joint draws  ·  414 bet sides mapped, 13 +EV candidates, 4 on card


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
| Jack Hughes: 1+ goals NO | 62 | 0.701 | 0.679 | +0.064 | +0.043 | $7.40 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 62 | 0.790 | 0.667 | +0.154 | +0.030 | $7.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Alex Laferriere: 1+ goals YES | 23 | 0.278 | 0.261 | +0.036 | +0.019 | $2.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 56 | 0.626 | 0.590 | +0.049 | +0.013 | $4.45 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (17.35 vs 8.61 bp); despite a smaller raw edge (+0.064 vs +0.154/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: NJD offense succeeds (4+ goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no has the higher standalone adjusted growth (17.35 vs 8.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.062); they share one thesis budget; relationships: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: NJD offense succeeds (4+ goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24LANJ-NJ3|no; why: higher confidence-adjusted growth (4.13 vs 4.06 bp); despite a smaller raw edge (+0.036 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.22); failure: LAK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT24LANJ-5|no; why: higher confidence-adjusted growth (1.56 vs 0.31 bp); wins across more scripts (relative breadth 0.962 vs 0.386); alternative not eligible: confidence-adjusted EV +0.0051 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.22); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.11.
- thesis NJD:SUPPRESSED (p 0.4061): highest fidelity KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.3022): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT24LANJ-NJ3|no (same contract)
- thesis GAME:TIGHT (p 0.4578): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24LANJ-NJ3|no (same contract)
- KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3725, phi -0.249)
- KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.0 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3725, phi -0.201)
- KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4795, phi -0.262)
- KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3022, phi -0.3)

portfolios: A EV +2.29 (adj +0.74) on $16.68, P(profit) 0.6288, adj growth 7.0 bp · B EV +3.33 (adj +1.17) on $22.08, P(profit) 0.6673, adj growth 11.2 bp · C EV +3.40 (adj +1.65) on $35.84, P(profit) 0.4923, adj growth 15.4 bp · R EV +0.20 (adj +0.13) on $2.00, P(profit) 0.7006, adj growth 5.2 bp

## SJS @ BOS  ·  10000 joint draws  ·  472 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_SJS_win | p_overtime | goals | shots BOS/SJS | BOS/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.65 | 0.35 | 0.00 | 6.06 | 27.6/27.6 | 24.6/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.66 | 0.34 | 0.00 | 9.43 | 29.1/29.2 | 24.0/21.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.51 | 0.49 | 0.46 | 6.01 | 27.7/27.8 | 24.4/24.4 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.077 | 0.69 | 0.31 | 0.00 | 6.03 | 32.7/22.0 | 19.4/27.9 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.063 | 0.60 | 0.40 | 0.00 | 6.01 | 22.0/32.4 | 28.9/18.2 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.56 | 0.44 | 0.47 | 5.97 | 32.6/21.8 | 18.6/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Macklin Celebrini: 1+ goals YES | 35 | 0.393 | 0.381 | +0.027 | +0.015 | $2.92 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 21 | 0.250 | 0.233 | +0.028 | +0.012 | $1.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Pavel Zacha: 1+ goals YES | 29 | 0.327 | 0.315 | +0.022 | +0.011 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Macklin Celebrini: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (2.18 vs 1.77 bp); despite a smaller raw edge (+0.027 vs +0.028/contract); relationships: KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: SJS offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes has the higher standalone adjusted growth (2.18 vs 1.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: SJS offense suppressed (<= 2 goals)
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24SJBOS-BOSHLINDHOLM27-1|yes; why: higher confidence-adjusted growth (1.19 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3466): highest fidelity KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.4969): highest fidelity KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes (same contract)
- KXNHLGOAL-26OCT24SJBOS-SJMCELEBRINI71-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4366, phi -0.31)
- KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4366, phi -0.219)
- KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.2987, phi -0.225)

portfolios: A EV +0.85 (adj +0.40) on $9.28, P(profit) 0.5444, adj growth 3.7 bp · B EV +0.58 (adj +0.28) on $6.59, P(profit) 0.5444, adj growth 2.7 bp · C EV +0.52 (adj +0.27) on $6.96, P(profit) 0.5917, adj growth 2.5 bp · R EV +0.07 (adj +0.04) on $1.00, P(profit) 0.3932, adj growth 1.5 bp

## NYR @ OTT  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYR_win | p_overtime | goals | shots OTT/NYR | OTT/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.129 | 0.61 | 0.39 | 0.00 | 6.01 | 32.5/20.7 | 17.8/28.3 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.54 | 0.46 | 0.48 | 5.87 | 32.9/21.1 | 17.9/29.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.56 | 0.44 | 0.00 | 6.05 | 27.0/26.3 | 23.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.51 | 0.49 | 0.47 | 5.95 | 27.1/26.6 | 23.2/23.6 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.082 | 0.63 | 0.37 | 0.00 | 9.15 | 34.0/22.2 | 17.3/26.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.51 | 0.49 | 0.00 | 9.27 | 28.7/27.9 | 21.9/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Taylor Raddysh: 1+ goals YES | 8 | 0.116 | 0.099 | +0.030 | +0.014 | $1.64 | FUNDED_RESEARCH | $1 | NYR:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ goals YES | 22 | 0.253 | 0.244 | +0.021 | +0.012 | $1.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 59 | 0.708 | 0.618 | +0.101 | +0.011 | $4.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (5.50 vs 1.70 bp); relationships: KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: NYR offense suppressed (<= 2 goals)
- **Gabe Perreault: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (1.70 vs 0.03 bp); despite a smaller raw edge (+0.021 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0015 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NYR offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT24NYROTT-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (1.20 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: OTT offense succeeds (4+ goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis NYR:OFFENSE_4PLUS (p 0.3415): highest fidelity KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3778): highest fidelity KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no (same contract)
- KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4417, phi -0.153)
- KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4417, phi -0.248)
- KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.8 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4084, phi -0.245)

portfolios: A EV +2.33 (adj +0.71) on $11.78, P(profit) 0.2746, adj growth 6.3 bp · B EV +1.44 (adj +0.44) on $7.56, P(profit) 0.3412, adj growth 4.1 bp · C EV +1.23 (adj +0.25) on $8.54, P(profit) 0.7818, adj growth 2.2 bp · R EV +0.36 (adj +0.17) on $1.00, P(profit) 0.1157, adj growth 5.5 bp

## NSH @ PIT  ·  10000 joint draws  ·  414 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_NSH_win | p_overtime | goals | shots PIT/NSH | PIT/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.62 | 0.38 | 0.00 | 6.07 | 27.9/27.5 | 24.3/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.53 | 0.47 | 0.48 | 5.94 | 27.8/27.3 | 24.1/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.58 | 0.42 | 0.00 | 9.43 | 29.7/29.3 | 23.6/22.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.099 | 0.68 | 0.32 | 0.00 | 6.04 | 32.9/21.8 | 19.0/28.4 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.57 | 0.43 | 0.48 | 5.96 | 33.6/22.0 | 18.9/30.2 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.083 | 0.69 | 0.31 | 0.00 | 9.39 | 34.9/23.5 | 18.8/26.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ WSH  ·  10000 joint draws  ·  438 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_BUF_win | p_overtime | goals | shots WSH/BUF | WSH/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.57 | 0.43 | 0.00 | 6.08 | 27.6/27.7 | 24.6/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.44 | 5.97 | 27.5/27.6 | 24.3/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.53 | 0.47 | 0.00 | 9.36 | 29.2/29.4 | 23.5/22.6 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.077 | 0.48 | 0.52 | 0.00 | 6.02 | 22.1/32.9 | 29.3/18.8 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.49 | 0.51 | 0.44 | 5.91 | 22.0/32.8 | 29.4/18.7 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.059 | 0.61 | 0.39 | 0.00 | 6.03 | 32.3/21.8 | 18.9/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Leonard: 1+ assists YES | 26 | 0.389 | 0.295 | +0.115 | +0.022 | $3.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_MIXED | D |
| Rasmus Dahlin: 1+ goals NO | 80 | 0.838 | 0.827 | +0.027 | +0.016 | $9.51 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 64 | 0.687 | 0.672 | +0.031 | +0.015 | $5.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Dylan Strome: 1+ assists YES | 41 | 0.476 | 0.438 | +0.049 | +0.011 | $1.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.65) | EVIDENCE_MIXED | D |
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24BUFWSH-WSHDSTROME17-1|yes; why: higher confidence-adjusted growth (5.21 vs 1.08 bp); relationships: KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT24BUFWSH-WSHDSTROME17-1|yes: MOSTLY_INDEPENDENT (phi 0.063); failure: WSH offense suppressed (<= 2 goals)
- **Rasmus Dahlin: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (3.67 vs 2.32 bp); despite a smaller raw edge (+0.027 vs +0.031/contract); relationships: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT24BUFWSH-WSHDSTROME17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: BUF offense succeeds (4+ goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no; why: higher confidence-adjusted growth (2.32 vs 0.00 bp); despite a smaller raw edge (+0.031 vs +0.040/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT24BUFWSH-WSHDSTROME17-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: BUF offense succeeds (4+ goals)
- **Dylan Strome: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes has the higher standalone adjusted growth (5.21 vs 1.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.063); they share one thesis budget; relationships: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.063); KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.026); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4327): highest fidelity KXNHLAST-26OCT24BUFWSH-WSHDSTROME17-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3966): highest fidelity KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no (same contract)
- KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 46% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.4 pts; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.347, phi -0.281)
- KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3882, phi -0.181)
- KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3882, phi -0.266)
- KXNHLAST-26OCT24BUFWSH-WSHDSTROME17-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 35% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.347, phi -0.327)

portfolios: A EV +2.57 (adj +0.62) on $16.68, P(profit) 0.5377, adj growth 5.7 bp · B EV +2.08 (adj +0.61) on $19.84, P(profit) 0.5057, adj growth 5.7 bp · C EV +2.32 (adj +0.56) on $12.77, P(profit) 0.3887, adj growth 5.1 bp · R EV +0.10 (adj +0.06) on $3.00, P(profit) 0.8379, adj growth 2.2 bp

## VGK @ CBJ  ·  10000 joint draws  ·  420 bet sides mapped, 3 +EV candidates, 3 on card


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
| Adam Fantilli: 1+ assists NO | 61 | 0.695 | 0.650 | +0.068 | +0.023 | $9.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Charlie Coyle: 1+ goals YES | 22 | 0.260 | 0.248 | +0.028 | +0.016 | $2.86 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 16 | 0.194 | 0.180 | +0.024 | +0.011 | $1.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Adam Fantilli: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24VGKCBJ-CBJZWERENSKI8-1|no; why: higher confidence-adjusted growth (5.11 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.108); KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.033); failure: CBJ offense succeeds (4+ goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (3.04 vs 1.85 bp); relationships: KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no: INTENTIONAL_DIVERSIFIER (phi -0.108); KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (3.04 vs 1.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:SUPPRESSED (p 0.4391): highest fidelity KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.3426): highest fidelity KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes (same contract)
- KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3426, phi -0.258)
- KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4391, phi -0.249)
- KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4391, phi -0.23)

portfolios: A EV +1.46 (adj +0.62) on $12.20, P(profit) 0.4063, adj growth 5.8 bp · B EV +1.58 (adj +0.64) on $13.61, P(profit) 0.7146, adj growth 6.0 bp · C EV +1.92 (adj +0.76) on $17.06, P(profit) 0.7963, adj growth 6.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ STL  ·  10000 joint draws  ·  422 bet sides mapped, 14 +EV candidates, 4 on card


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
| St. Louis wins by over 1.5 goals YES | 22 | 0.306 | 0.260 | +0.074 | +0.028 | $2.79 | FUNDED_RESEARCH | $1 | STL:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Robert Thomas: 1+ goals YES | 23 | 0.290 | 0.271 | +0.047 | +0.029 | $3.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 68 | 0.727 | 0.713 | +0.032 | +0.018 | $6.03 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 13 | 0.167 | 0.151 | +0.029 | +0.013 | $1.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **St. Louis wins by over 1.5 goals YES** — thesis: STL wins by 2+; alternative: KXNHLSPREAD-26OCT24CARSTL-CAR2|no; why: higher confidence-adjusted growth (9.73 vs 6.10 bp); relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: REINFORCING (phi 0.179); KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: REINFORCING (phi 0.188); failure: CAR wins (incl. OT/SO)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-STL2|yes has the higher standalone adjusted growth (9.73 vs 9.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.179); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-STL2|yes: REINFORCING (phi 0.179); KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: STL offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-STL2|yes has the higher standalone adjusted growth (9.73 vs 3.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.144); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-STL2|yes: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: CAR offense succeeds (4+ goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-STL2|yes has the higher standalone adjusted growth (9.73 vs 3.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.188); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-STL2|yes: REINFORCING (phi 0.188); KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis STL:WINS_BY_2PLUS (p 0.3056): highest fidelity KXNHLSPREAD-26OCT24CARSTL-STL2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-STL2|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.4257): highest fidelity KXNHLTEAMTOTAL-26OCT24CARSTL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.5186): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-STL2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT24CARSTL-STL2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.4814, phi -0.639)
- KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3549, phi -0.242)
- KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4043, phi -0.227)
- KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3549, phi -0.193)

portfolios: A EV +3.29 (adj +0.97) on $16.68, P(profit) 0.4953, adj growth 8.9 bp · B EV +2.19 (adj +1.08) on $14.00, P(profit) 0.492, adj growth 10.1 bp · C EV +1.86 (adj +0.72) on $5.87, P(profit) 0.3056, adj growth 6.5 bp · R EV +0.41 (adj +0.17) on $3.00, P(profit) 0.3056, adj growth 6.4 bp

## TOR @ EDM  ·  10000 joint draws  ·  448 bet sides mapped, 4 +EV candidates, 4 on card


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
| Leon Draisaitl: 1+ assists NO | 37 | 0.485 | 0.407 | +0.099 | +0.021 | $4.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.75) | EVIDENCE_MIXED | D |
| Auston Matthews: 1+ assists NO | 57 | 0.642 | 0.601 | +0.055 | +0.014 | $4.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Zach Hyman: 1+ goals YES | 34 | 0.381 | 0.369 | +0.026 | +0.013 | $3.29 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 67 | 0.741 | 0.698 | +0.055 | +0.012 | $5.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (4.00 vs 1.54 bp); relationships: KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT24TOREDM-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.098); failure: EDM offense succeeds (4+ goals)
- **Auston Matthews: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT24TOREDM-4|no; why: higher confidence-adjusted growth (1.72 vs 1.05 bp); wins across more scripts (relative breadth 0.998 vs 0.382); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT24TOREDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense succeeds (4+ goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (1.57 vs 0.31 bp); despite a smaller raw edge (+0.026 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.183); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no has the higher standalone adjusted growth (4.00 vs 1.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.098); they share one thesis budget; relationships: KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.098); KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24TOREDM-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.183); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, EDM shot control · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis EDM:SUPPRESSED (p 0.25): highest fidelity KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.4321): highest fidelity KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.5538): highest fidelity KXNHLGOAL-26OCT24TOREDM-EDMZHYMAN18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TOREDM-EDMZHYMAN18-1|yes (same contract)
- KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5538, phi -0.303)
- KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3474, phi -0.269)
- KXNHLGOAL-26OCT24TOREDM-EDMZHYMAN18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.25, phi -0.234)
- KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5538, phi -0.334)

portfolios: A EV +2.22 (adj +0.54) on $16.68, P(profit) 0.556, adj growth 5.1 bp · B EV +2.13 (adj +0.54) on $17.25, P(profit) 0.6027, adj growth 5.1 bp · C EV +2.48 (adj +0.63) on $16.52, P(profit) 0.5152, adj growth 5.7 bp · R EV +0.07 (adj +0.04) on $1.00, P(profit) 0.3814, adj growth 1.3 bp

## TBL @ UTA  ·  10000 joint draws  ·  426 bet sides mapped, 0 +EV candidates, 0 on card


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

## DET @ CGY  ·  10000 joint draws  ·  440 bet sides mapped, 4 +EV candidates, 3 on card


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
| Jonathan Castagna: 1+ goals YES | 10 | 0.147 | 0.125 | +0.041 | +0.019 | $2.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Detroit wins by over 2.5 goals NO | 77 | 0.832 | 0.798 | +0.050 | +0.016 | $8.12 | FUNDED_RESEARCH | $3 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Lucas Raymond: 1+ goals NO | 71 | 0.751 | 0.738 | +0.026 | +0.014 | $5.28 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24DETCGY-DET3|no; why: higher confidence-adjusted growth (7.99 vs 3.37 bp); despite a smaller raw edge (+0.041 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT24DETCGY-DET3|no: MOSTLY_INDEPENDENT (phi 0.102); KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: CGY offense suppressed (<= 2 goals)
- **Detroit wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24DETCGY-DET2|no; why: higher confidence-adjusted growth (3.37 vs 2.39 bp); despite a smaller raw edge (+0.050 vs +0.052/contract); relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.102); KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.137); failure: DET wins by 2+
- **Lucas Raymond: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24DETCGY-DET3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24DETCGY-DET3|no has the higher standalone adjusted growth (3.37 vs 2.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.137); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT24DETCGY-DET3|no: MOSTLY_INDEPENDENT (phi 0.137); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:OFFENSE_4PLUS (p 0.3631): highest fidelity KXNHLSPREAD-26OCT24DETCGY-DET3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT24DETCGY-DET3|no (same contract)
- thesis CGY:WINS (p 0.5057): highest fidelity KXNHLSPREAD-26OCT24DETCGY-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24DETCGY-DET3|no (same contract)
- thesis DET:SUPPRESSED (p 0.4189): highest fidelity KXNHLSPREAD-26OCT24DETCGY-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24DETCGY-DET3|no (same contract)
- KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4195, phi -0.188)
- KXNHLSPREAD-26OCT24DETCGY-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2727, phi -0.734)
- KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3564, phi -0.219)

portfolios: A EV +2.31 (adj +0.93) on $16.68, P(profit) 0.7483, adj growth 8.3 bp · B EV +1.50 (adj +0.63) on $15.47, P(profit) 0.6897, adj growth 5.9 bp · C EV +0.91 (adj +0.30) on $14.34, P(profit) 0.8321, adj growth 2.7 bp · R EV +0.26 (adj +0.10) on $5.00, P(profit) 0.6469, adj growth 3.7 bp

## MIN @ SEA  ·  10000 joint draws  ·  420 bet sides mapped, 13 +EV candidates, 4 on card


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
| Shane Wright: 1+ goals YES | 14 | 0.197 | 0.179 | +0.048 | +0.030 | $4.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 55 | 0.625 | 0.602 | +0.058 | +0.035 | $9.86 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 15 | 0.194 | 0.179 | +0.035 | +0.021 | $2.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 11 | 0.146 | 0.133 | +0.029 | +0.017 | $2.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: higher confidence-adjusted growth (15.48 vs 9.69 bp); despite a smaller raw edge (+0.048 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.891 vs 0.536); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT24MINSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: SEA offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: higher confidence-adjusted growth (10.96 vs 9.69 bp); despite a smaller raw edge (+0.058 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.998 vs 0.536); relationships: KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT24MINSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MIN offense succeeds (4+ goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes has the higher standalone adjusted growth (9.69 vs 6.88 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.139); relationships: KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: SEA offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes has the higher standalone adjusted growth (9.69 vs 5.67 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.137); relationships: KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24MINSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.41): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.531): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.4111): highest fidelity KXNHLTEAMTOTAL-26OCT24MINSEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3646, phi -0.194)
- KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3649, phi -0.296)
- KXNHLGOAL-26OCT24MINSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3646, phi -0.188)
- KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3646, phi -0.158)

portfolios: A EV +3.04 (adj +0.98) on $16.68, P(profit) 0.4667, adj growth 8.7 bp · B EV +3.44 (adj +2.08) on $18.71, P(profit) 0.3655, adj growth 19.4 bp · C EV +2.79 (adj +1.36) on $17.44, P(profit) 0.6968, adj growth 12.4 bp · R EV +0.30 (adj +0.19) on $3.00, P(profit) 0.6248, adj growth 6.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
