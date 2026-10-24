# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T16:40:05Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +25.29 | +9.63 | +24.03 | 0.752 | -20.05 | -32.00 | 89.81 |
| B thesis-diversified (joint) ← optimiser card | 149.09 | +24.43 | +12.17 | +22.49 | 0.745 | -20.57 | -31.12 | 115.06 |
| C best expression per thesis | 150.02 | +23.71 | +12.43 | +20.33 | 0.671 | -33.05 | -45.64 | 114.10 |
| R FUNDED research stakes | 25.00 | +3.47 | +2.11 | +1.80 | 0.566 | -7.19 | -9.53 | 0.00 |

## ANA @ PHI  ·  10000 joint draws  ·  416 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.520 / away 0.480

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
| A.J. Greer: 1+ goals YES | 12 | 0.204 | 0.181 | +0.076 | +0.054 | $5.44 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 14 | 0.186 | 0.172 | +0.038 | +0.024 | $2.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Denver Barkey: 1+ goals YES | 14 | 0.187 | 0.171 | +0.038 | +0.023 | $2.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ assists YES | 23 | 0.300 | 0.260 | +0.058 | +0.018 | $1.80 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24ANAPHI-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (55.34 vs 3.77 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT24ANAPHI-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.051); failure: ANA offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes; why: higher confidence-adjusted growth (9.65 vs 8.84 bp); despite a smaller raw edge (+0.038 vs +0.038/contract); relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT24ANAPHI-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: PHI offense suppressed (<= 2 goals)
- **Denver Barkey: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (9.65 vs 8.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT24ANAPHI-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: PHI offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ assists YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes has the higher standalone adjusted growth (55.34 vs 3.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.051); they share one thesis budget; relationships: KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.051); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3508): highest fidelity KXNHLAST-26OCT24ANAPHI-ANAAKILLORN17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3952): highest fidelity KXNHLAST-26OCT24ANAPHI-PHITSANHEIM6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4295, phi -0.234)
- KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3846, phi -0.205)
- KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3846, phi -0.199)
- KXNHLAST-26OCT24ANAPHI-ANAAKILLORN17-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4295, phi -0.262)

portfolios: A EV +4.64 (adj +2.06) on $14.10, P(profit) 0.4202, adj growth 19.4 bp · B EV +5.01 (adj +3.25) on $12.39, P(profit) 0.4762, adj growth 30.5 bp · C EV +6.07 (adj +4.22) on $12.49, P(profit) 0.3555, adj growth 38.2 bp · R EV +1.20 (adj +0.85) on $2.00, P(profit) 0.2037, adj growth 30.8 bp

## LAK @ NJD  ·  10000 joint draws  ·  414 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.631 / away 0.369

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
| Joel Edmundson: 1+ goals YES | 3 | 0.058 | 0.049 | +0.026 | +0.017 | $1.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 63 | 0.701 | 0.680 | +0.054 | +0.034 | $6.06 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 62 | 0.790 | 0.667 | +0.154 | +0.030 | $6.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Alex Laferriere: 1+ goals YES | 23 | 0.278 | 0.265 | +0.036 | +0.022 | $2.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (18.56 vs 5.95 bp); despite a smaller raw edge (+0.026 vs +0.036/contract); relationships: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: LAK offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (11.21 vs 8.61 bp); despite a smaller raw edge (+0.054 vs +0.154/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24LANJ-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: NJD offense succeeds (4+ goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no has the higher standalone adjusted growth (11.21 vs 8.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.062); they share one thesis budget; relationships: KXNHLGOAL-26OCT24LANJ-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: NJD offense succeeds (4+ goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24LANJ-NJ3|no; why: higher confidence-adjusted growth (5.95 vs 4.06 bp); despite a smaller raw edge (+0.036 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24LANJ-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.11.
- thesis NJD:SUPPRESSED (p 0.4061): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.3022): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4578): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24LANJ-NJ2|no (same contract)
- KXNHLGOAL-26OCT24LANJ-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4795, phi -0.122)
- KXNHLGOAL-26OCT24LANJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3725, phi -0.249)
- KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.0 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3725, phi -0.201)
- KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4795, phi -0.262)

portfolios: A EV +1.76 (adj +0.55) on $14.10, P(profit) 0.708, adj growth 5.4 bp · B EV +3.49 (adj +1.57) on $16.30, P(profit) 0.6868, adj growth 14.9 bp · C EV +2.23 (adj +1.22) on $24.38, P(profit) 0.673, adj growth 11.4 bp · R EV +0.17 (adj +0.11) on $2.00, P(profit) 0.7006, adj growth 4.1 bp

## SJS @ BOS  ·  10000 joint draws  ·  478 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.625 / away 0.375

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_SJS_win | p_overtime | goals | shots BOS/SJS | BOS/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.67 | 0.33 | 0.00 | 6.07 | 27.8/27.8 | 24.9/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.46 | 6.0 | 27.6/27.7 | 24.5/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.66 | 0.34 | 0.00 | 9.42 | 29.2/29.2 | 24.0/22.0 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.080 | 0.68 | 0.32 | 0.00 | 6.04 | 32.3/22.0 | 19.3/27.8 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.55 | 0.45 | 0.48 | 5.97 | 32.9/22.2 | 18.9/29.3 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.061 | 0.74 | 0.26 | 0.00 | 9.21 | 34.3/23.6 | 19.3/26.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tanner Jeannot: 1+ goals YES | 9 | 0.116 | 0.108 | +0.020 | +0.013 | $1.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Mark Kastelic: 1+ goals YES | 11 | 0.138 | 0.130 | +0.021 | +0.013 | $1.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 60 | 0.641 | 0.630 | +0.025 | +0.013 | $3.32 | FUNDED_RESEARCH | $1 | BOS:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Pavel Zacha: 1+ goals YES | 28 | 0.317 | 0.305 | +0.022 | +0.011 | $1.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Tanner Jeannot: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (3.91 vs 1.24 bp); despite a smaller raw edge (+0.020 vs +0.022/contract); relationships: KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: BOS offense suppressed (<= 2 goals)
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (3.57 vs 1.24 bp); despite a smaller raw edge (+0.021 vs +0.022/contract); relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: BOS offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no; why: Player prop expression KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.82 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: BOS offense succeeds (4+ goals)
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24SJBOS-BOSHLINDHOLM27-1|yes; why: higher confidence-adjusted growth (1.24 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:SUPPRESSED (p 0.3089): highest fidelity KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.4872): highest fidelity KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes (same contract)
- KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3089, phi -0.129)
- KXNHLGOAL-26OCT24SJBOS-BOSMKASTELIC47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3089, phi -0.149)
- KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4872, phi -0.251)
- KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3089, phi -0.24)
- override: Player prop expression KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.82 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.09 (adj +0.48) on $14.10, P(profit) 0.6805, adj growth 4.5 bp · B EV +0.77 (adj +0.45) on $7.50, P(profit) 0.3928, adj growth 4.2 bp · C EV +0.82 (adj +0.26) on $10.79, P(profit) 0.7377, adj growth 2.4 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6415, adj growth 0.8 bp

## NYR @ OTT  ·  10000 joint draws  ·  444 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.532 / away 0.468

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYR_win | p_overtime | goals | shots OTT/NYR | OTT/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.126 | 0.62 | 0.38 | 0.00 | 5.98 | 32.4/20.8 | 17.9/28.1 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.53 | 0.47 | 0.45 | 5.92 | 32.7/21.1 | 17.9/29.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.54 | 0.46 | 0.00 | 5.99 | 26.9/26.2 | 22.8/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.47 | 5.91 | 27.1/26.6 | 23.4/23.8 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.076 | 0.63 | 0.37 | 0.00 | 9.28 | 34.1/22.4 | 17.3/26.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.54 | 0.46 | 0.00 | 9.24 | 28.6/27.8 | 22.1/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Taylor Raddysh: 1+ goals YES | 8 | 0.120 | 0.102 | +0.034 | +0.017 | $1.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 8 | 0.108 | 0.096 | +0.023 | +0.011 | $1.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Alexis Lafreniere: 1+ goals YES | 29 | 0.334 | 0.317 | +0.029 | +0.012 | $1.71 | FUNDED_RESEARCH | $1 | NYR:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ goals YES | 22 | 0.252 | 0.243 | +0.020 | +0.011 | $1.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NYROTT-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (7.99 vs 1.53 bp); relationships: KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT24NYROTT-NYRALAFRENIERE13-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense suppressed (<= 2 goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24NYROTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (3.44 vs 0.17 bp); despite a smaller raw edge (+0.023 vs +0.071/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT24NYROTT-NYRALAFRENIERE13-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense suppressed (<= 2 goals)
- **Alexis Lafreniere: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (1.53 vs 1.45 bp); relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: NYR offense suppressed (<= 2 goals)
- **Gabe Perreault: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NYROTT-NYRALAFRENIERE13-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24NYROTT-NYRALAFRENIERE13-1|yes has the higher standalone adjusted growth (1.53 vs 1.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24NYROTT-NYRALAFRENIERE13-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis NYR:OFFENSE_4PLUS (p 0.3446): highest fidelity KXNHLGOAL-26OCT24NYROTT-NYRALAFRENIERE13-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24NYROTT-NYRALAFRENIERE13-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4115): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4331, phi -0.162)
- KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3708, phi -0.134)
- KXNHLGOAL-26OCT24NYROTT-NYRALAFRENIERE13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4331, phi -0.302)
- KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4331, phi -0.242)

portfolios: A EV +2.01 (adj +0.97) on $9.28, P(profit) 0.4796, adj growth 8.8 bp · B EV +1.24 (adj +0.60) on $5.81, P(profit) 0.4142, adj growth 5.7 bp · C EV +0.25 (adj +0.10) on $2.62, P(profit) 0.3338, adj growth 1.0 bp · R EV +0.10 (adj +0.04) on $1.00, P(profit) 0.3338, adj growth 1.4 bp

## NSH @ PIT  ·  10000 joint draws  ·  398 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.532 / away 0.468

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_NSH_win | p_overtime | goals | shots PIT/NSH | PIT/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.62 | 0.38 | 0.00 | 6.06 | 27.9/27.6 | 24.5/23.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.109 | 0.66 | 0.34 | 0.00 | 6.01 | 33.5/21.9 | 19.2/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.59 | 0.41 | 0.00 | 9.4 | 29.5/29.2 | 23.4/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.52 | 0.48 | 0.44 | 5.94 | 27.6/27.2 | 24.1/24.3 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.46 | 0.47 | 5.95 | 33.3/22.1 | 19.0/29.8 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.077 | 0.70 | 0.30 | 0.00 | 9.38 | 35.1/23.4 | 18.7/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Rickard Rakell: 1+ goals YES | 35 | 0.430 | 0.408 | +0.064 | +0.042 | $6.48 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.58) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ assists NO | 76 | 0.875 | 0.794 | +0.102 | +0.021 | $8.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Declan Carlile: 1+ goals YES | 7 | 0.095 | 0.085 | +0.020 | +0.010 | $1.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ goals YES | 34 | 0.386 | 0.369 | +0.030 | +0.013 | $2.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_STRONGER | D |
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes; why: higher confidence-adjusted growth (16.26 vs 1.73 bp); relationships: KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT24NSHPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: PIT offense suppressed (<= 2 goals)
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT24NSHPIT-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (5.55 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT24NSHPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NSH offense succeeds (4+ goals)
- **Declan Carlile: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes has the higher standalone adjusted growth (16.26 vs 3.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes has the higher standalone adjusted growth (16.26 vs 1.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT24NSHPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4828): highest fidelity KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes (same contract)
- thesis NSH:SUPPRESSED (p 0.4247): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis NSH:OFFENSE_4PLUS (p 0.3654): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 42% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.28)
- KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.5 pts; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3654, phi -0.166)
- KXNHLGOAL-26OCT24NSHPIT-PITDCARLILE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.132)
- KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.267)

portfolios: A EV +1.91 (adj +0.88) on $14.10, P(profit) 0.6672, adj growth 8.5 bp · B EV +2.65 (adj +1.17) on $17.61, P(profit) 0.4795, adj growth 11.2 bp · C EV +1.73 (adj +1.12) on $9.87, P(profit) 0.4301, adj growth 10.3 bp · R EV +0.35 (adj +0.23) on $2.00, P(profit) 0.4301, adj growth 8.5 bp

## BUF @ WSH  ·  10000 joint draws  ·  458 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_BUF_win | p_overtime | goals | shots WSH/BUF | WSH/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.59 | 0.41 | 0.00 | 5.99 | 27.5/27.7 | 24.6/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.47 | 6.0 | 27.6/27.6 | 24.3/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.56 | 0.44 | 0.00 | 9.42 | 29.1/29.3 | 23.2/22.6 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.079 | 0.48 | 0.52 | 0.00 | 6.04 | 22.0/32.8 | 29.0/18.5 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.48 | 0.52 | 0.48 | 5.96 | 22.1/33.1 | 29.6/19.0 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.058 | 0.61 | 0.39 | 0.00 | 6.02 | 32.4/22.2 | 19.2/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.240 | 0.219 | +0.061 | +0.039 | $4.34 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Rasmus Dahlin: 1+ assists NO | 52 | 0.608 | 0.561 | +0.070 | +0.024 | $5.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Justin Sourdif: 1+ goals YES | 11 | 0.146 | 0.132 | +0.030 | +0.015 | $1.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 25 | 0.365 | 0.284 | +0.102 | +0.021 | $1.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (22.39 vs 4.85 bp); despite a smaller raw edge (+0.061 vs +0.102/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24BUFWSH-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.039); failure: WSH offense suppressed (<= 2 goals)
- **Rasmus Dahlin: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no; why: higher confidence-adjusted growth (5.08 vs 2.42 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24BUFWSH-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: BUF offense succeeds (4+ goals)
- **Justin Sourdif: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (22.39 vs 5.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.123); failure: WSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (22.39 vs 4.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.039); they share one thesis budget; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT24BUFWSH-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.123); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4409): highest fidelity KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3956): highest fidelity KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3477, phi -0.227)
- KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3883, phi -0.276)
- KXNHLGOAL-26OCT24BUFWSH-WSHJSOURDIF34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3477, phi -0.159)
- KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.6 pts; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3477, phi -0.279)

portfolios: A EV +3.96 (adj +1.61) on $14.10, P(profit) 0.5653, adj growth 15.0 bp · B EV +3.27 (adj +1.53) on $12.95, P(profit) 0.4598, adj growth 14.4 bp · C EV +3.31 (adj +1.82) on $14.71, P(profit) 0.7006, adj growth 16.7 bp · R EV +0.67 (adj +0.44) on $2.00, P(profit) 0.2405, adj growth 15.7 bp

## VGK @ CBJ  ·  10000 joint draws  ·  424 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.447 / away 0.553

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_VGK_win | p_overtime | goals | shots CBJ/VGK | CBJ/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.47 | 0.53 | 0.00 | 6.01 | 27.3/27.4 | 23.8/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.47 | 0.53 | 0.48 | 5.96 | 27.6/27.4 | 24.0/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.43 | 0.57 | 0.00 | 9.26 | 29.2/29.2 | 22.7/23.2 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.071 | 0.38 | 0.62 | 0.00 | 5.99 | 21.6/32.2 | 27.9/18.8 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.065 | 0.53 | 0.47 | 0.00 | 5.95 | 32.3/21.8 | 18.6/28.5 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.52 | 0.48 | 0.48 | 5.89 | 32.3/22.0 | 18.8/28.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Fantilli: 1+ assists NO | 61 | 0.694 | 0.649 | +0.067 | +0.023 | $6.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Charlie Coyle: 1+ goals YES | 22 | 0.260 | 0.247 | +0.028 | +0.015 | $2.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Trevor Connelly: 1+ goals NO | 77 | 0.803 | 0.793 | +0.020 | +0.011 | $5.10 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Adam Fantilli: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24VGKCBJ-CBJZWERENSKI8-1|no; why: higher confidence-adjusted growth (4.79 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.103); KXNHLGOAL-26OCT24VGKCBJ-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: CBJ offense succeeds (4+ goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (2.90 vs 0.86 bp); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no: INTENTIONAL_DIVERSIFIER (phi -0.103); KXNHLGOAL-26OCT24VGKCBJ-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: CBJ offense suppressed (<= 2 goals)
- **Trevor Connelly: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24VGKCBJ-VGKMSTONE61-1|no; why: higher confidence-adjusted growth (1.55 vs 0.54 bp); despite a smaller raw edge (+0.020 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:SUPPRESSED (p 0.4353): highest fidelity KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.346): highest fidelity KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.386): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.346, phi -0.274)
- KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4353, phi -0.253)
- KXNHLGOAL-26OCT24VGKCBJ-VGKTCONNELLY24-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.396, phi -0.182)

portfolios: A EV +1.06 (adj +0.45) on $13.84, P(profit) 0.6688, adj growth 4.3 bp · B EV +1.15 (adj +0.47) on $14.31, P(profit) 0.6688, adj growth 4.5 bp · C EV +1.55 (adj +0.61) on $14.13, P(profit) 0.794, adj growth 5.7 bp · R EV +0.05 (adj +0.03) on $2.00, P(profit) 0.8028, adj growth 1.0 bp

## CAR @ STL  ·  10000 joint draws  ·  424 bet sides mapped, 15 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.417 / away 0.583

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_CAR_win | p_overtime | goals | shots STL/CAR | STL/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.136 | 0.51 | 0.49 | 0.00 | 6.07 | 21.3/33.2 | 29.4/17.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.50 | 0.50 | 0.49 | 5.92 | 21.2/33.4 | 30.1/18.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.58 | 0.42 | 0.00 | 6.04 | 26.4/27.0 | 23.9/22.4 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.102 | 0.49 | 0.51 | 0.00 | 9.28 | 22.5/34.6 | 27.9/16.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.51 | 0.49 | 0.45 | 5.97 | 26.6/27.3 | 23.9/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.57 | 0.43 | 0.00 | 9.32 | 27.9/28.9 | 23.1/21.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 2.5 goals NO | 76 | 0.834 | 0.795 | +0.061 | +0.022 | $8.07 | FUNDED_RESEARCH | $3 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Robert Thomas: 1+ goals YES | 23 | 0.282 | 0.264 | +0.040 | +0.022 | $2.48 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 13 | 0.167 | 0.154 | +0.029 | +0.016 | $1.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Carolina wins by over 2.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (5.99 vs 5.71 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; wins across more scripts (relative breadth 1.035 vs 0.918); relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.108); failure: CAR wins by 2+
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24CARSTL-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-CAR3|no has the higher standalone adjusted growth (5.99 vs 5.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.132); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-CAR3|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24CARSTL-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-CAR3|no has the higher standalone adjusted growth (5.99 vs 4.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.108); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-CAR3|no: MOSTLY_INDEPENDENT (phi 0.108); KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis STL:WINS (p 0.5285): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.4291): highest fidelity KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS_BY_2PLUS (p 0.3069): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-CAR3|no (same contract)
- KXNHLSPREAD-26OCT24CARSTL-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2595, phi -0.753)
- KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.248)
- KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.198)

portfolios: A EV +2.11 (adj +0.51) on $14.10, P(profit) 0.6121, adj growth 4.8 bp · B EV +1.37 (adj +0.63) on $12.08, P(profit) 0.3665, adj growth 6.0 bp · C EV +0.98 (adj +0.35) on $12.31, P(profit) 0.8342, adj growth 3.3 bp · R EV +0.24 (adj +0.08) on $3.00, P(profit) 0.8342, adj growth 3.2 bp

## TOR @ EDM  ·  10000 joint draws  ·  448 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.608 / away 0.393

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
| Teddy Blueger: 1+ goals YES | 11 | 0.151 | 0.136 | +0.035 | +0.019 | $1.99 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Kasperi Kapanen: 1+ assists YES | 26 | 0.338 | 0.292 | +0.065 | +0.018 | $2.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 27 | 0.312 | 0.301 | +0.029 | +0.017 | $2.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 66 | 0.741 | 0.693 | +0.065 | +0.017 | $7.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHL2PSPREAD-26OCT24TOREDM-TOR2|yes; why: higher confidence-adjusted growth (7.68 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.007); failure: TOR offense suppressed (<= 2 goals)
- **Kasperi Kapanen: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (3.62 vs 3.04 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.074); KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.037); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes has the higher standalone adjusted growth (3.62 vs 3.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.074); they share one thesis budget; relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi 0.074); KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.201); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT24TOREDM-4|no; why: higher confidence-adjusted growth (2.93 vs 1.05 bp); wins across more scripts (relative breadth 1.042 vs 0.382); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.201); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, EDM shot control · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3474): highest fidelity KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.5538): highest fidelity KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.25): highest fidelity KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no (same contract)
- KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4321, phi -0.21)
- KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.25, phi -0.232)
- KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.25, phi -0.233)
- KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5538, phi -0.334)

portfolios: A EV +2.31 (adj +0.79) on $14.10, P(profit) 0.4416, adj growth 7.4 bp · B EV +2.12 (adj +0.83) on $14.41, P(profit) 0.499, adj growth 7.8 bp · C EV +3.17 (adj +1.11) on $21.35, P(profit) 0.6861, adj growth 10.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TBL @ UTA  ·  10000 joint draws  ·  426 bet sides mapped, 0 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.564 / away 0.436

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

sportsbook moneyline consensus (5 books): home 0.447 / away 0.553

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_DET_win | p_overtime | goals | shots CGY/DET | CGY/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.52 | 0.48 | 0.00 | 6.0 | 28.5/28.8 | 25.2/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.46 | 5.85 | 28.3/28.6 | 25.4/24.9 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.087 | 0.46 | 0.54 | 0.00 | 5.96 | 22.8/34.0 | 30.2/19.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.51 | 0.49 | 0.00 | 9.25 | 29.8/30.0 | 23.9/23.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.50 | 0.50 | 0.47 | 5.83 | 22.6/34.1 | 30.8/19.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.062 | 0.48 | 0.52 | 0.45 | 2.85 | 27.2/27.5 | 26.0/25.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Justin Faulk: 1+ goals NO | 89 | 0.919 | 0.910 | +0.022 | +0.013 | $8.07 | FUNDED_RESEARCH | $3 | DET:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 11 | 0.153 | 0.131 | +0.036 | +0.014 | $1.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Detroit wins by over 2.5 goals NO | 78 | 0.836 | 0.805 | +0.044 | +0.013 | $6.32 | FUNDED_RESEARCH | $2 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Justin Faulk: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24DETCGY-DET3|no; why: higher confidence-adjusted growth (4.32 vs 2.41 bp); despite a smaller raw edge (+0.022 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT24DETCGY-DET3|no: MOSTLY_INDEPENDENT (phi 0.045); failure: DET offense succeeds (4+ goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24DETCGY-DET3|no; why: higher confidence-adjusted growth (4.10 vs 2.41 bp); despite a smaller raw edge (+0.036 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT24DETCGY-DET3|no: MOSTLY_INDEPENDENT (phi 0.099); failure: CGY offense suppressed (<= 2 goals)
- **Detroit wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24DETCGY-DET2|no; why: higher confidence-adjusted growth (2.41 vs 1.50 bp); despite a smaller raw edge (+0.044 vs +0.045/contract); relationships: KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: MOSTLY_INDEPENDENT (phi 0.045); KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.099); failure: DET wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:OFFENSE_4PLUS (p 0.3627): highest fidelity KXNHLSPREAD-26OCT24DETCGY-DET3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4323): highest fidelity KXNHLSPREAD-26OCT24DETCGY-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24DETCGY-DET3|no (same contract)
- thesis CGY:WINS (p 0.5096): highest fidelity KXNHLSPREAD-26OCT24DETCGY-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24DETCGY-DET3|no (same contract)
- KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3466, phi -0.104)
- KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4175, phi -0.203)
- KXNHLSPREAD-26OCT24DETCGY-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2698, phi -0.729)

portfolios: A EV +1.56 (adj +0.54) on $14.10, P(profit) 0.7533, adj growth 4.8 bp · B EV +0.94 (adj +0.38) on $15.68, P(profit) 0.7948, adj growth 3.6 bp · C EV +1.15 (adj +0.40) on $11.98, P(profit) 0.8478, adj growth 3.7 bp · R EV +0.18 (adj +0.08) on $5.00, P(profit) 0.7725, adj growth 3.0 bp

## MIN @ SEA  ·  10000 joint draws  ·  420 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.415 / away 0.585

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
| Kirill Kaprizov: 1+ goals NO | 55 | 0.625 | 0.604 | +0.058 | +0.036 | $7.62 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Minnesota wins by over 2.5 goals NO | 76 | 0.842 | 0.798 | +0.069 | +0.026 | $8.07 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Shane Wright: 1+ goals YES | 15 | 0.197 | 0.181 | +0.038 | +0.022 | $2.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Mackie Samoskevich: 1+ goals YES | 18 | 0.226 | 0.209 | +0.035 | +0.019 | $2.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: higher confidence-adjusted growth (11.76 vs 9.69 bp); despite a smaller raw edge (+0.058 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.998 vs 0.536); relationships: KXNHLSPREAD-26OCT24MINSEA-MIN3|no: REINFORCING (phi 0.195); KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: MIN offense succeeds (4+ goals)
- **Minnesota wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no has the higher standalone adjusted growth (11.76 vs 8.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.195); they share one thesis budget; relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: REINFORCING (phi 0.195); KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.096); KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi 0.105); failure: MIN wins by 2+
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes has the higher standalone adjusted growth (9.69 vs 7.96 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.151); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLSPREAD-26OCT24MINSEA-MIN3|no: MOSTLY_INDEPENDENT (phi 0.096); KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: SEA offense suppressed (<= 2 goals)
- **Mackie Samoskevich: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes has the higher standalone adjusted growth (9.69 vs 5.09 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.154); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLSPREAD-26OCT24MINSEA-MIN3|no: MOSTLY_INDEPENDENT (phi 0.105); KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.41): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.531): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.3055): highest fidelity KXNHLSPREAD-26OCT24MINSEA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes (same contract)
- KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3649, phi -0.296)
- KXNHLSPREAD-26OCT24MINSEA-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2533, phi -0.743)
- KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3646, phi -0.194)
- KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3646, phi -0.208)

portfolios: A EV +2.89 (adj +0.79) on $14.10, P(profit) 0.4865, adj growth 7.0 bp · B EV +2.43 (adj +1.29) on $20.05, P(profit) 0.6926, adj growth 12.2 bp · C EV +2.43 (adj +1.22) on $15.39, P(profit) 0.6968, adj growth 11.2 bp · R EV +0.47 (adj +0.23) on $5.00, P(profit) 0.5605, adj growth 8.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
