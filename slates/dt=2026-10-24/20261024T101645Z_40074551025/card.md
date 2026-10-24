# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T10:16:45Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +21.27 | +6.48 | +19.81 | 0.646 | -45.67 | -62.89 | 50.49 |
| B thesis-diversified (joint) ← optimiser card | 127.63 | +18.69 | +5.55 | +20.00 | 0.717 | -25.75 | -36.77 | 49.70 |
| C best expression per thesis | 105.74 | +15.54 | +4.34 | +10.90 | 0.793 | -22.87 | -25.12 | 39.35 |
| R FUNDED research stakes | 23.00 | +2.83 | +1.05 | +2.07 | 0.615 | -7.92 | -10.79 | 0.00 |

## ANA @ PHI  ·  10000 joint draws  ·  406 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_ANA_win | p_overtime | goals | shots PHI/ANA | PHI/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.56 | 0.44 | 0.00 | 6.0 | 26.6/27.2 | 23.8/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.44 | 5.92 | 26.6/27.1 | 24.0/23.3 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.100 | 0.49 | 0.51 | 0.00 | 5.96 | 21.2/32.2 | 28.5/17.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.50 | 0.50 | 0.46 | 5.92 | 21.4/32.6 | 29.2/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.60 | 0.40 | 0.00 | 9.28 | 28.2/28.8 | 23.2/21.4 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.066 | 0.48 | 0.52 | 0.00 | 9.17 | 22.9/34.3 | 27.9/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Christian Dvorak: 1+ goals YES | 18 | 0.231 | 0.210 | +0.040 | +0.020 | $5.71 | FUNDED_RESEARCH | $2 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Denver Barkey: 1+ goals YES | 15 | 0.185 | 0.175 | +0.026 | +0.016 | $4.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (5.65 vs 1.68 bp); alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: PHI offense suppressed (<= 2 goals)
- **Denver Barkey: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes has the higher standalone adjusted growth (5.65 vs 4.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:OFFENSE_4PLUS (p 0.3925): highest fidelity KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes (same contract)
- KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3884, phi -0.225)
- KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3884, phi -0.206)

portfolios: A EV +2.67 (adj +1.44) on $13.79, P(profit) 0.3724, adj growth 11.8 bp · B EV +1.97 (adj +1.07) on $10.29, P(profit) 0.3724, adj growth 9.3 bp · C EV +1.21 (adj +0.60) on $5.74, P(profit) 0.2305, adj growth 5.2 bp · R EV +0.42 (adj +0.21) on $2.00, P(profit) 0.2305, adj growth 6.9 bp

## LAK @ NJD  ·  10000 joint draws  ·  434 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_LAK_win | p_overtime | goals | shots NJD/LAK | NJD/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.56 | 0.44 | 0.00 | 5.94 | 28.4/28.1 | 24.9/24.7 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.111 | 0.62 | 0.38 | 0.00 | 5.96 | 33.6/22.3 | 19.4/29.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.55 | 0.45 | 0.49 | 5.86 | 28.6/28.2 | 25.1/25.3 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.57 | 0.43 | 0.51 | 5.89 | 34.1/22.6 | 19.5/30.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.51 | 0.49 | 0.50 | 2.79 | 27.2/26.8 | 25.4/25.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.065 | 0.56 | 0.44 | 0.00 | 9.24 | 30.1/29.5 | 24.0/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Luke Evangelista: 1+ assists NO | 62 | 0.794 | 0.668 | +0.158 | +0.031 | $19.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Mats Zuccarello: 1+ assists NO | 67 | 0.819 | 0.713 | +0.134 | +0.027 | $19.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| New Jersey over 3.5 goals scored NO | 55 | 0.616 | 0.580 | +0.048 | +0.013 | $4.32 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 56 | 0.624 | 0.589 | +0.046 | +0.012 | $6.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no; why: higher confidence-adjusted growth (9.39 vs 1.49 bp); wins across more scripts (relative breadth 0.992 vs 0.869); relationships: KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no: REINFORCING (phi 0.203); KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense succeeds (4+ goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (7.47 vs 1.31 bp); relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.06); failure: LAK offense succeeds (4+ goals)
- **New Jersey over 3.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no has the higher standalone adjusted growth (9.39 vs 1.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.203); they share one thesis budget; relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.203); KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NJD offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no has the higher standalone adjusted growth (7.47 vs 1.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.060); they share one thesis budget; relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.06); KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no: MOSTLY_INDEPENDENT (phi 0.002); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NJD:SUPPRESSED (p 0.403): highest fidelity KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.4855): highest fidelity KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no (same contract)
- KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.4 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.374, phi -0.202)
- KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2973, phi -0.191)
- KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.374, phi -0.978)
- KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2973, phi -0.288)

portfolios: A EV +5.18 (adj +1.13) on $34.05, P(profit) 0.674, adj growth 10.4 bp · B EV +9.59 (adj +1.98) on $50.00, P(profit) 0.6506, adj growth 18.0 bp · C EV +8.86 (adj +1.78) on $40.00, P(profit) 0.6506, adj growth 16.3 bp · R EV +0.17 (adj +0.05) on $2.00, P(profit) 0.6155, adj growth 1.6 bp

## SJS @ BOS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_SJS_win | p_overtime | goals | shots BOS/SJS | BOS/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.65 | 0.35 | 0.00 | 6.09 | 27.8/27.7 | 24.8/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.65 | 0.35 | 0.00 | 9.31 | 29.2/29.2 | 23.9/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.52 | 0.48 | 0.47 | 6.04 | 27.7/28.0 | 24.6/24.3 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.081 | 0.68 | 0.32 | 0.00 | 6.03 | 32.2/22.0 | 19.4/27.5 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.063 | 0.58 | 0.42 | 0.00 | 6.03 | 22.3/32.5 | 29.2/18.7 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.062 | 0.73 | 0.27 | 0.00 | 9.32 | 34.5/23.5 | 19.1/26.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYR @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYR_win | p_overtime | goals | shots OTT/NYR | OTT/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.127 | 0.61 | 0.39 | 0.00 | 6.0 | 32.5/20.7 | 17.9/28.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.54 | 0.46 | 0.50 | 5.95 | 32.7/21.1 | 17.9/29.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.53 | 0.47 | 0.00 | 6.01 | 27.0/26.4 | 22.9/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.50 | 0.50 | 0.49 | 5.93 | 27.1/26.5 | 23.2/23.6 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.081 | 0.61 | 0.39 | 0.00 | 9.24 | 33.9/22.1 | 17.2/26.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.52 | 0.48 | 0.00 | 9.3 | 28.6/28.0 | 21.9/22.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_NSH_win | p_overtime | goals | shots PIT/NSH | PIT/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.61 | 0.39 | 0.00 | 6.02 | 27.8/27.4 | 24.4/23.7 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.108 | 0.67 | 0.33 | 0.00 | 6.0 | 33.2/21.9 | 19.2/28.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.61 | 0.39 | 0.00 | 9.42 | 29.6/29.1 | 23.3/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.52 | 0.48 | 0.45 | 5.94 | 27.9/27.6 | 24.4/24.5 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.46 | 0.48 | 5.93 | 33.2/22.0 | 18.8/29.9 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.080 | 0.68 | 0.32 | 0.00 | 9.39 | 35.0/23.4 | 18.8/27.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_BUF_win | p_overtime | goals | shots WSH/BUF | WSH/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.56 | 0.44 | 0.00 | 6.02 | 27.5/27.7 | 24.5/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.48 | 5.97 | 27.5/27.8 | 24.4/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.56 | 0.44 | 0.00 | 9.42 | 29.3/29.4 | 23.2/22.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.075 | 0.54 | 0.46 | 0.00 | 5.94 | 22.0/33.0 | 29.5/18.5 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.49 | 0.51 | 0.47 | 5.9 | 22.1/32.8 | 29.2/18.9 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.061 | 0.62 | 0.38 | 0.00 | 6.01 | 32.3/22.1 | 19.3/28.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_VGK_win | p_overtime | goals | shots CBJ/VGK | CBJ/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.47 | 0.53 | 0.00 | 5.97 | 27.5/27.4 | 23.8/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.48 | 0.52 | 0.49 | 5.92 | 27.6/27.6 | 24.4/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.48 | 0.52 | 0.00 | 9.16 | 28.6/28.8 | 22.8/22.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.071 | 0.40 | 0.60 | 0.00 | 5.96 | 21.9/32.0 | 27.8/19.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.068 | 0.52 | 0.48 | 0.00 | 5.95 | 32.2/22.0 | 18.5/28.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.51 | 0.49 | 0.49 | 2.77 | 26.1/26.1 | 24.7/24.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_CAR_win | p_overtime | goals | shots STL/CAR | STL/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.133 | 0.48 | 0.52 | 0.00 | 6.05 | 21.1/33.1 | 29.3/17.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.46 | 0.54 | 0.47 | 5.96 | 21.1/33.3 | 29.8/17.9 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.104 | 0.48 | 0.52 | 0.00 | 9.35 | 22.4/34.7 | 27.8/16.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.56 | 0.44 | 0.00 | 6.07 | 26.7/27.5 | 24.0/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.51 | 0.49 | 0.46 | 5.98 | 26.4/27.4 | 24.1/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.57 | 0.43 | 0.00 | 9.32 | 28.0/28.7 | 23.1/21.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 64 | 0.731 | 0.683 | +0.074 | +0.027 | $12.32 | FUNDED_RESEARCH | $4 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| St. Louis wins by over 1.5 goals YES | 23 | 0.307 | 0.264 | +0.065 | +0.021 | $1.30 | FUNDED_RESEARCH | $1 | STL:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| St. Louis wins by over 2.5 goals YES | 14 | 0.196 | 0.166 | +0.048 | +0.017 | $2.23 | FUNDED_RESEARCH | $1 | STL:WINS_BY_2PLUS | DIRECT (0.64) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 76 | 0.830 | 0.793 | +0.058 | +0.020 | $7.90 | FUNDED_RESEARCH | $2 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: higher confidence-adjusted growth (6.90 vs 5.27 bp); wins across more scripts (relative breadth 0.991 vs 0.552); relationships: KXNHLSPREAD-26OCT24CARSTL-STL2|yes: DUPLICATIVE (phi 0.404); KXNHLSPREAD-26OCT24CARSTL-STL3|yes: DUPLICATIVE (phi 0.3); KXNHLSPREAD-26OCT24CARSTL-CAR3|no: DUPLICATIVE (phi 0.744); failure: CAR wins by 2+
- **St. Louis wins by over 1.5 goals YES** — thesis: STL wins by 2+; alternative: KXNHLSPREAD-26OCT24CARSTL-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-CAR2|no has the higher standalone adjusted growth (6.90 vs 5.27 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.404); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-CAR2|no: DUPLICATIVE (phi 0.404); KXNHLSPREAD-26OCT24CARSTL-STL3|yes: DUPLICATIVE (phi 0.743); KXNHLSPREAD-26OCT24CARSTL-CAR3|no: DUPLICATIVE (phi 0.301); failure: CAR wins (incl. OT/SO)
- **St. Louis wins by over 2.5 goals YES** — thesis: STL wins by 2+; alternative: KXNHLSPREAD-26OCT24CARSTL-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-CAR2|no has the higher standalone adjusted growth (6.90 vs 5.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.300); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-CAR2|no: DUPLICATIVE (phi 0.3); KXNHLSPREAD-26OCT24CARSTL-STL2|yes: DUPLICATIVE (phi 0.743); KXNHLSPREAD-26OCT24CARSTL-CAR3|no: REINFORCING (phi 0.223); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 2.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24CARSTL-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-CAR2|no has the higher standalone adjusted growth (6.90 vs 4.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.744); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-CAR2|no: DUPLICATIVE (phi 0.744); KXNHLSPREAD-26OCT24CARSTL-STL2|yes: DUPLICATIVE (phi 0.301); KXNHLSPREAD-26OCT24CARSTL-STL3|yes: REINFORCING (phi 0.223); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, CAR shot control · high event (8+) · decided (2+) 0.10.
- thesis STL:WINS (p 0.5183): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-CAR2|no (same contract)
- thesis STL:WINS_BY_2PLUS (p 0.307): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-CAR2|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.4278): highest fidelity KXNHLTEAMTOTAL-26OCT24CARSTL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT24CARSTL-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2695, phi -1.0)
- KXNHLSPREAD-26OCT24CARSTL-STL2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.4817, phi -0.642)
- KXNHLSPREAD-26OCT24CARSTL-STL3|yes: FUNDED_RESEARCH; family MIXED; loses 36% of the draws where the thesis happens; opposing: failure thesis CAR:WINS (p 0.4817, phi -0.477)
- KXNHLSPREAD-26OCT24CARSTL-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2695, phi -0.744)

portfolios: A EV +5.51 (adj +1.68) on $34.05, P(profit) 0.4866, adj growth 11.6 bp · B EV +3.05 (adj +1.08) on $23.75, P(profit) 0.7305, adj growth 9.5 bp · C EV +2.27 (adj +0.81) on $20.00, P(profit) 0.7305, adj growth 7.2 bp · R EV +1.19 (adj +0.42) on $8.00, P(profit) 0.7305, adj growth 13.4 bp

## TOR @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_TOR_win | p_overtime | goals | shots EDM/TOR | EDM/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.127 | 0.74 | 0.26 | 0.00 | 6.08 | 35.4/22.8 | 20.3/30.1 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.119 | 0.73 | 0.27 | 0.00 | 9.55 | 36.9/24.3 | 19.7/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.69 | 0.31 | 0.00 | 9.57 | 31.3/30.3 | 25.2/23.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.69 | 0.31 | 0.00 | 6.06 | 29.4/28.8 | 26.1/24.7 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.56 | 0.44 | 0.48 | 5.95 | 35.4/23.2 | 20.0/32.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.52 | 0.48 | 0.47 | 6.01 | 29.4/28.8 | 25.5/26.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, EDM shot control · high event (8+) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TBL @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TBL_win | p_overtime | goals | shots UTA/TBL | UTA/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.52 | 0.48 | 0.00 | 5.98 | 26.7/26.6 | 23.3/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.47 | 5.92 | 26.8/26.8 | 23.6/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.58 | 0.42 | 0.00 | 9.16 | 28.1/28.1 | 22.7/21.8 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.071 | 0.49 | 0.51 | 0.00 | 5.98 | 21.4/31.5 | 27.6/18.0 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.070 | 0.65 | 0.35 | 0.00 | 6.01 | 31.8/21.2 | 18.5/27.6 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.52 | 0.48 | 0.46 | 5.95 | 31.6/21.5 | 18.4/28.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_DET_win | p_overtime | goals | shots CGY/DET | CGY/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.52 | 0.48 | 0.00 | 6.03 | 28.4/28.8 | 25.3/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.48 | 0.52 | 0.47 | 5.89 | 28.5/28.8 | 25.3/25.3 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.084 | 0.46 | 0.54 | 0.00 | 5.93 | 22.4/33.7 | 29.8/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.52 | 0.48 | 0.00 | 9.25 | 30.1/30.3 | 24.3/23.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.46 | 0.54 | 0.46 | 5.84 | 22.9/34.0 | 30.7/19.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.51 | 0.49 | 0.00 | 3.51 | 27.3/27.4 | 25.5/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Detroit wins by over 2.5 goals NO | 77 | 0.837 | 0.801 | +0.054 | +0.019 | $20.00 | FUNDED_RESEARCH | $5 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Detroit wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24DETCGY-DET2|no; why: higher confidence-adjusted growth (4.46 vs 1.73 bp); relationships: only recommended bet in this game; failure: DET wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DET shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CGY:WINS (p 0.4977): highest fidelity KXNHLSPREAD-26OCT24DETCGY-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24DETCGY-DET3|no (same contract)
- thesis DET:SUPPRESSED (p 0.4215): highest fidelity KXNHLSPREAD-26OCT24DETCGY-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24DETCGY-DET3|no (same contract)
- KXNHLSPREAD-26OCT24DETCGY-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2723, phi -0.722)

portfolios: A EV +2.61 (adj +0.70) on $34.05, P(profit) 0.5747, adj growth 5.2 bp · B EV +1.39 (adj +0.47) on $20.00, P(profit) 0.8369, adj growth 4.3 bp · C EV +1.39 (adj +0.47) on $20.00, P(profit) 0.8369, adj growth 4.3 bp · R EV +0.35 (adj +0.12) on $5.00, P(profit) 0.8369, adj growth 4.3 bp

## MIN @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_MIN_win | p_overtime | goals | shots SEA/MIN | SEA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.54 | 0.46 | 0.00 | 6.0 | 28.2/28.7 | 25.3/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.47 | 5.92 | 29.0/29.2 | 25.9/25.8 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.091 | 0.49 | 0.51 | 0.00 | 5.96 | 22.8/34.4 | 30.8/19.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.54 | 0.46 | 0.00 | 9.4 | 30.1/30.5 | 24.5/23.5 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.47 | 0.53 | 0.46 | 5.9 | 22.9/34.3 | 30.6/19.6 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.060 | 0.49 | 0.51 | 0.00 | 9.23 | 24.0/36.1 | 29.4/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Minnesota wins by over 2.5 goals NO | 76 | 0.843 | 0.799 | +0.070 | +0.026 | $20.00 | FUNDED_RESEARCH | $5 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Seattle wins by over 1.5 goals YES | 23 | 0.302 | 0.261 | +0.059 | +0.018 | $3.59 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: higher confidence-adjusted growth (8.59 vs 4.03 bp); wins across more scripts (relative breadth 1.022 vs 0.535); relationships: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes: REINFORCING (phi 0.284); failure: MIN wins by 2+
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24MINSEA-MIN3|no has the higher standalone adjusted growth (8.59 vs 4.03 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.284); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24MINSEA-MIN3|no: REINFORCING (phi 0.284); failure: MIN wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis SEA:WINS (p 0.5281): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN3|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.3017): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN3|no (same contract)
- thesis MIN:SUPPRESSED (p 0.4121): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN3|no (same contract)
- KXNHLSPREAD-26OCT24MINSEA-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2562, phi -0.736)
- KXNHLSPREAD-26OCT24MINSEA-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.4719, phi -0.621)

portfolios: A EV +5.30 (adj +1.53) on $34.05, P(profit) 0.3017, adj growth 11.4 bp · B EV +2.69 (adj +0.95) on $23.59, P(profit) 0.8428, adj growth 8.6 bp · C EV +1.81 (adj +0.68) on $20.00, P(profit) 0.8428, adj growth 6.3 bp · R EV +0.70 (adj +0.25) on $6.00, P(profit) 0.8428, adj growth 8.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
