# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T11:12:28Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +30.21 | +8.12 | +25.05 | 0.671 | -45.53 | -65.51 | 62.42 |
| B thesis-diversified (joint) ← optimiser card | 128.97 | +21.87 | +6.58 | +21.59 | 0.717 | -27.78 | -41.85 | 58.20 |
| C best expression per thesis | 105.82 | +17.25 | +4.75 | +20.27 | 0.672 | -26.12 | -31.98 | 42.52 |
| R FUNDED research stakes | 24.00 | +3.27 | +1.27 | +3.50 | 0.603 | -8.55 | -11.50 | 0.00 |

## ANA @ PHI  ·  10000 joint draws  ·  406 bet sides mapped, 5 +EV candidates, 4 on card


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
| Christian Dvorak: 1+ goals YES | 17 | 0.231 | 0.208 | +0.051 | +0.028 | $7.69 | FUNDED_RESEARCH | $2 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Denver Barkey: 1+ goals YES | 15 | 0.185 | 0.175 | +0.026 | +0.016 | $4.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| A.J. Greer: 1+ goals YES | 11 | 0.205 | 0.130 | +0.088 | +0.013 | $2.49 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 14 | 0.181 | 0.161 | +0.033 | +0.012 | $3.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (11.46 vs 2.64 bp); relationships: KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PHI offense suppressed (<= 2 goals)
- **Denver Barkey: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes has the higher standalone adjusted growth (11.46 vs 4.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: PHI offense suppressed (<= 2 goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24ANAPHI-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (3.68 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes has the higher standalone adjusted growth (11.46 vs 2.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:OFFENSE_4PLUS (p 0.3925): highest fidelity KXNHLAST-26OCT24ANAPHI-PHITSANHEIM6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:OFFENSE_4PLUS (p 0.349): highest fidelity KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes (same contract)
- KXNHLGOAL-26OCT24ANAPHI-PHICDVORAK22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3884, phi -0.225)
- KXNHLGOAL-26OCT24ANAPHI-PHIDBARKEY86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3884, phi -0.206)
- KXNHLGOAL-26OCT24ANAPHI-ANAAGREER18-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 66% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.5 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4309, phi -0.227)
- KXNHLGOAL-26OCT24ANAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3884, phi -0.214)

portfolios: A EV +12.27 (adj +3.06) on $31.25, P(profit) 0.5915, adj growth 21.5 bp · B EV +5.49 (adj +2.21) on $17.93, P(profit) 0.5888, adj growth 19.2 bp · C EV +4.04 (adj +1.49) on $10.25, P(profit) 0.3872, adj growth 12.9 bp · R EV +0.56 (adj +0.31) on $2.00, P(profit) 0.2305, adj growth 10.7 bp

## LAK @ NJD  ·  10000 joint draws  ·  434 bet sides mapped, 3 +EV candidates, 3 on card


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
| Luke Evangelista: 1+ assists NO | 62 | 0.794 | 0.668 | +0.158 | +0.031 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Mats Zuccarello: 1+ assists NO | 68 | 0.819 | 0.709 | +0.124 | +0.014 | $15.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| New Jersey over 3.5 goals scored NO | 55 | 0.616 | 0.580 | +0.048 | +0.013 | $4.41 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no; why: higher confidence-adjusted growth (9.39 vs 1.49 bp); wins across more scripts (relative breadth 0.992 vs 0.869); relationships: KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no: REINFORCING (phi 0.203); failure: NJD offense succeeds (4+ goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (2.05 vs 0.83 bp); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no: MOSTLY_INDEPENDENT (phi -0.002); failure: LAK offense succeeds (4+ goals)
- **New Jersey over 3.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no has the higher standalone adjusted growth (9.39 vs 1.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.203); they share one thesis budget; relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.203); KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NJD:SUPPRESSED (p 0.403): highest fidelity KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.4855): highest fidelity KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no (same contract)
- KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.4 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.374, phi -0.202)
- KXNHLAST-26OCT24LANJ-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.9 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2973, phi -0.191)
- KXNHLTEAMTOTAL-26OCT24LANJ-NJ4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.374, phi -0.978)

portfolios: A EV +5.32 (adj +0.96) on $31.25, P(profit) 0.8209, adj growth 8.7 bp · B EV +8.10 (adj +1.40) on $39.96, P(profit) 0.6506, adj growth 12.7 bp · C EV +7.73 (adj +1.30) on $35.57, P(profit) 0.6506, adj growth 11.8 bp · R EV +0.17 (adj +0.05) on $2.00, P(profit) 0.6155, adj growth 1.6 bp

## SJS @ BOS  ·  10000 joint draws  ·  448 bet sides mapped, 0 +EV candidates, 0 on card


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

## NYR @ OTT  ·  10000 joint draws  ·  434 bet sides mapped, 0 +EV candidates, 0 on card


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

## NSH @ PIT  ·  10000 joint draws  ·  392 bet sides mapped, 0 +EV candidates, 0 on card


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

## BUF @ WSH  ·  10000 joint draws  ·  436 bet sides mapped, 0 +EV candidates, 0 on card


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

## VGK @ CBJ  ·  10000 joint draws  ·  412 bet sides mapped, 0 +EV candidates, 0 on card


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

## CAR @ STL  ·  10000 joint draws  ·  414 bet sides mapped, 7 +EV candidates, 4 on card


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
| Carolina wins by over 1.5 goals NO | 64 | 0.731 | 0.683 | +0.074 | +0.027 | $10.77 | FUNDED_RESEARCH | $3 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| St. Louis over 3.5 goals scored YES | 35 | 0.436 | 0.390 | +0.070 | +0.025 | $4.14 | FUNDED_RESEARCH | $2 | STL:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| St. Louis wins by over 1.5 goals YES | 23 | 0.307 | 0.264 | +0.065 | +0.021 | $2.38 | FUNDED_RESEARCH | $1 | STL:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 76 | 0.830 | 0.793 | +0.058 | +0.020 | $7.61 | FUNDED_RESEARCH | $2 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes; why: higher confidence-adjusted growth (6.90 vs 5.65 bp); wins across more scripts (relative breadth 0.991 vs 0.762); relationships: KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes: REINFORCING (phi 0.423); KXNHLSPREAD-26OCT24CARSTL-STL2|yes: DUPLICATIVE (phi 0.404); KXNHLSPREAD-26OCT24CARSTL-CAR3|no: DUPLICATIVE (phi 0.744); failure: CAR wins by 2+
- **St. Louis over 3.5 goals scored YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24CARSTL-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-CAR2|no has the higher standalone adjusted growth (6.90 vs 5.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.423); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-CAR2|no: REINFORCING (phi 0.423); KXNHLSPREAD-26OCT24CARSTL-STL2|yes: REINFORCING (phi 0.535); KXNHLSPREAD-26OCT24CARSTL-CAR3|no: DUPLICATIVE (phi 0.332); failure: STL offense suppressed (<= 2 goals)
- **St. Louis wins by over 1.5 goals YES** — thesis: STL wins by 2+; alternative: KXNHLSPREAD-26OCT24CARSTL-CAR2|no; why: Broad expression KXNHLSPREAD-26OCT24CARSTL-STL2|yes selected over broad KXNHLSPREAD-26OCT24CARSTL-STL3|yes because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.64 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT24CARSTL-CAR2|no: DUPLICATIVE (phi 0.404); KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes: REINFORCING (phi 0.535); KXNHLSPREAD-26OCT24CARSTL-CAR3|no: DUPLICATIVE (phi 0.301); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 2.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24CARSTL-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24CARSTL-CAR2|no has the higher standalone adjusted growth (6.90 vs 4.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.744); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24CARSTL-CAR2|no: DUPLICATIVE (phi 0.744); KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes: DUPLICATIVE (phi 0.332); KXNHLSPREAD-26OCT24CARSTL-STL2|yes: DUPLICATIVE (phi 0.301); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, CAR shot control · high event (8+) · decided (2+) 0.10.
- thesis STL:WINS (p 0.5183): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-CAR2|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.4278): highest fidelity KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS_BY_2PLUS (p 0.307): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-CAR2|no (same contract)
- KXNHLSPREAD-26OCT24CARSTL-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2695, phi -1.0)
- KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis STL:SUPPRESSED (p 0.3595, phi -0.659)
- KXNHLSPREAD-26OCT24CARSTL-STL2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.4817, phi -0.642)
- KXNHLSPREAD-26OCT24CARSTL-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2695, phi -0.744)
- override: Broad expression KXNHLSPREAD-26OCT24CARSTL-STL2|yes selected over broad KXNHLSPREAD-26OCT24CARSTL-STL3|yes because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.64 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.31 (adj +1.76) on $31.25, P(profit) 0.4866, adj growth 13.2 bp · B EV +3.21 (adj +1.12) on $24.89, P(profit) 0.7305, adj growth 9.8 bp · C EV +2.27 (adj +0.81) on $20.00, P(profit) 0.7305, adj growth 7.2 bp · R EV +1.14 (adj +0.39) on $8.00, P(profit) 0.4745, adj growth 13.0 bp

## TOR @ EDM  ·  10000 joint draws  ·  440 bet sides mapped, 0 +EV candidates, 0 on card


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

## DET @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


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
- KXNHLSPREAD-26OCT24DETCGY-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2723, phi -0.722)

portfolios: A EV +1.83 (adj +0.54) on $25.00, P(profit) 0.7277, adj growth 4.5 bp · B EV +1.39 (adj +0.47) on $20.00, P(profit) 0.8369, adj growth 4.3 bp · C EV +1.39 (adj +0.47) on $20.00, P(profit) 0.8369, adj growth 4.3 bp · R EV +0.35 (adj +0.12) on $5.00, P(profit) 0.8369, adj growth 4.3 bp

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
| Seattle wins by over 1.5 goals YES | 22 | 0.302 | 0.258 | +0.070 | +0.026 | $6.19 | FUNDED_RESEARCH | $2 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: higher confidence-adjusted growth (8.59 vs 8.44 bp); wins across more scripts (relative breadth 1.022 vs 0.535); relationships: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes: REINFORCING (phi 0.284); failure: MIN wins by 2+
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24MINSEA-MIN3|no has the higher standalone adjusted growth (8.59 vs 8.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.284); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24MINSEA-MIN3|no: REINFORCING (phi 0.284); failure: MIN wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis SEA:WINS (p 0.5281): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.3017): highest fidelity KXNHLSPREAD-26OCT24MINSEA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.4121): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT24MINSEA-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2562, phi -0.736)
- KXNHLSPREAD-26OCT24MINSEA-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.4719, phi -0.621)

portfolios: A EV +5.46 (adj +1.80) on $31.25, P(profit) 0.3017, adj growth 14.5 bp · B EV +3.67 (adj +1.38) on $26.19, P(profit) 0.3017, adj growth 12.3 bp · C EV +1.81 (adj +0.68) on $20.00, P(profit) 0.8428, adj growth 6.3 bp · R EV +1.05 (adj +0.40) on $7.00, P(profit) 0.3017, adj growth 13.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
