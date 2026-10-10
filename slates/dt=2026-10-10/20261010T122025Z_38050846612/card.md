# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-10T12:20:25Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +28.35 | +8.29 | +27.88 | 0.829 | -9.19 | -19.81 | 78.30 |
| B thesis-diversified (joint) ← optimiser card | 149.20 | +26.74 | +11.44 | +25.83 | 0.807 | -11.37 | -20.81 | 109.81 |
| C best expression per thesis | 150.00 | +29.23 | +12.25 | +27.79 | 0.781 | -17.35 | -28.77 | 115.59 |
| R FUNDED research stakes | 24.00 | +3.29 | +1.82 | +1.93 | 0.625 | -5.36 | -7.44 | 0.00 |

## PHI @ BOS  ·  10000 joint draws  ·  426 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_PHI_win | p_overtime | goals | shots BOS/PHI | BOS/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.59 | 0.41 | 0.00 | 5.98 | 27.1/27.0 | 23.8/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.53 | 0.47 | 0.47 | 5.93 | 27.1/27.0 | 23.6/23.7 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.081 | 0.63 | 0.37 | 0.00 | 5.95 | 31.7/21.4 | 18.5/27.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.63 | 0.37 | 0.00 | 9.14 | 28.4/28.3 | 23.0/22.0 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.45 | 5.85 | 32.0/21.5 | 18.3/28.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.61 | 0.39 | 0.00 | 3.43 | 25.8/25.7 | 24.2/23.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Frederic Brunet: 1+ assists NO | 64 | 0.812 | 0.691 | +0.156 | +0.035 | $5.75 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| David Pastrnak: 1+ goals NO | 61 | 0.667 | 0.652 | +0.041 | +0.025 | $4.30 | FUNDED_RESEARCH | $2 | BOS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 14 | 0.179 | 0.165 | +0.030 | +0.017 | $1.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| David Jiricek: 1+ assists NO | 75 | 0.819 | 0.777 | +0.056 | +0.014 | $5.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **Frederic Brunet: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no; why: higher confidence-adjusted growth (11.61 vs 5.97 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.092); KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT10PHIBOS-PHIDJIRICEK55-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: BOS offense succeeds (4+ goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (5.97 vs 4.24 bp); relationships: KXNHLAST-26OCT10PHIBOS-BOSFBRUNET42-1|no: MOSTLY_INDEPENDENT (phi 0.092); KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT10PHIBOS-PHIDJIRICEK55-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: BOS offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT10PHIBOS-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (4.90 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT10PHIBOS-BOSFBRUNET42-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT10PHIBOS-PHIDJIRICEK55-1|no: INTENTIONAL_DIVERSIFIER (phi -0.078); failure: PHI offense suppressed (<= 2 goals)
- **David Jiricek: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10PHIBOS-PHIPMARTONE94-1|no; why: higher confidence-adjusted growth (2.32 vs 0.77 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLAST-26OCT10PHIBOS-BOSFBRUNET42-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.078); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BOS shot control · normal event (5-7) · decided (2+) 0.08.
- thesis BOS:SUPPRESSED (p 0.3869): highest fidelity KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3103): highest fidelity KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes (same contract)
- thesis PHI:SUPPRESSED (p 0.4669): highest fidelity KXNHLAST-26OCT10PHIBOS-PHIDJIRICEK55-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10PHIBOS-PHIDJIRICEK55-1|no (same contract)
- KXNHLAST-26OCT10PHIBOS-BOSFBRUNET42-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.8 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.395, phi -0.184)
- KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.395, phi -0.263)
- KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4669, phi -0.235)
- KXNHLAST-26OCT10PHIBOS-PHIDJIRICEK55-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3103, phi -0.202)

portfolios: A EV +2.61 (adj +0.48) on $13.76, P(profit) 0.7712, adj growth 4.6 bp · B EV +2.30 (adj +0.72) on $16.53, P(profit) 0.5415, adj growth 7.0 bp · C EV +1.59 (adj +0.72) on $18.57, P(profit) 0.6199, adj growth 6.8 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.6675, adj growth 3.0 bp

## VAN @ NJD  ·  10000 joint draws  ·  412 bet sides mapped, 29 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_VAN_win | p_overtime | goals | shots NJD/VAN | NJD/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.139 | 0.64 | 0.36 | 0.00 | 6.02 | 34.0/21.8 | 19.0/29.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.53 | 0.47 | 0.46 | 5.91 | 34.3/22.1 | 18.9/30.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.49 | 0.51 | 0.47 | 5.99 | 28.5/27.6 | 24.4/25.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.57 | 0.43 | 0.00 | 6.02 | 28.2/27.4 | 24.2/24.5 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.089 | 0.63 | 0.37 | 0.00 | 9.17 | 36.1/23.3 | 18.4/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.56 | 0.44 | 0.00 | 9.29 | 30.0/29.0 | 23.0/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Luke Evangelista: 1+ assists NO | 57 | 0.765 | 0.635 | +0.177 | +0.048 | $5.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 58 | 0.653 | 0.632 | +0.056 | +0.035 | $4.62 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 1.5 goals NO | 51 | 0.666 | 0.561 | +0.138 | +0.034 | $2.28 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 2.5 goals NO | 64 | 0.785 | 0.687 | +0.129 | +0.031 | $3.95 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: higher confidence-adjusted growth (20.65 vs 19.19 bp); wins across more scripts (relative breadth 1.009 vs 0.482); relationships: KXNHLGOAL-26OCT10VANNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.079); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: REINFORCING (phi 0.161); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: REINFORCING (phi 0.153); failure: NJD offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no; why: second expression of the same thesis: KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no has the higher standalone adjusted growth (20.65 vs 11.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.079); they share one thesis budget; relationships: KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.079); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: REINFORCING (phi 0.159); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: REINFORCING (phi 0.151); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (19.19 vs 10.03 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.279); relationships: KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.161); KXNHLGOAL-26OCT10VANNJ-NJJHUGHES86-1|no: REINFORCING (phi 0.159); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: DUPLICATIVE (phi 0.739); failure: NJD wins by 2+
- **New Jersey wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (19.19 vs 9.53 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.206); relationships: KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.153); KXNHLGOAL-26OCT10VANNJ-NJJHUGHES86-1|no: REINFORCING (phi 0.151); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: DUPLICATIVE (phi 0.739); failure: NJD wins by 2+

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.14, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NJD:SUPPRESSED (p 0.3532): highest fidelity KXNHLSPREAD-26OCT10VANNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2281): highest fidelity KXNHLGAME-26OCT10VANNJ-VAN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10VANNJ-VAN|yes (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3408): highest fidelity KXNHLTEAMTOTAL-26OCT10VANNJ-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10VANNJ-VAN|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.0 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4263, phi -0.211)
- KXNHLGOAL-26OCT10VANNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4263, phi -0.25)
- KXNHLSPREAD-26OCT10VANNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.1 pts; opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3342, phi -1.0)
- KXNHLSPREAD-26OCT10VANNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.0 pts; opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3342, phi -0.739)

portfolios: A EV +4.90 (adj +1.05) on $13.76, P(profit) 0.6698, adj growth 10.0 bp · B EV +3.45 (adj +1.05) on $16.28, P(profit) 0.7466, adj growth 10.2 bp · C EV +4.37 (adj +1.42) on $11.13, P(profit) 0.7808, adj growth 13.5 bp · R EV +0.65 (adj +0.23) on $4.00, P(profit) 0.5422, adj growth 8.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10VANNJ-VAN|yes == KXNHLGAME-26OCT10VANNJ-NJ|no

## EDM @ SJS  ·  10000 joint draws  ·  424 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_EDM_win | p_overtime | goals | shots SJS/EDM | SJS/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.118 | 0.48 | 0.52 | 0.00 | 9.57 | 29.3/29.7 | 23.2/22.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.48 | 0.52 | 0.00 | 6.06 | 27.3/27.7 | 23.9/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.49 | 0.51 | 0.47 | 6.05 | 27.7/27.9 | 24.5/24.4 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.088 | 0.42 | 0.58 | 0.00 | 6.07 | 22.0/33.1 | 28.8/19.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.082 | 0.40 | 0.60 | 0.00 | 9.41 | 23.2/34.9 | 27.5/17.9 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.46 | 0.54 | 0.47 | 5.93 | 22.2/33.2 | 29.9/19.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 13 | 0.207 | 0.186 | +0.069 | +0.048 | $4.30 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Collin Graf: 1+ goals YES | 18 | 0.237 | 0.223 | +0.046 | +0.032 | $3.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 31 | 0.473 | 0.361 | +0.148 | +0.036 | $4.75 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ goals YES | 8 | 0.113 | 0.105 | +0.028 | +0.020 | $1.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT10EDMSJ-10|yes; why: higher confidence-adjusted growth (41.73 vs 0.27 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.855 vs 0.324); alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.071); KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: EDM offense suppressed (<= 2 goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10EDMSJ-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (14.42 vs 3.12 bp); relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: SJS offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (12.59 vs 3.36 bp); relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.071); KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.135); failure: EDM offense succeeds (4+ goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (41.73 vs 10.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.135); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4672): highest fidelity KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.4308): highest fidelity KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3236): highest fidelity KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3236, phi -0.199)
- KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.348, phi -0.217)
- KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.3 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4672, phi -0.305)
- KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3236, phi -0.159)

portfolios: A EV +4.31 (adj +1.79) on $13.76, P(profit) 0.5965, adj growth 17.1 bp · B EV +5.68 (adj +2.98) on $13.99, P(profit) 0.7389, adj growth 28.4 bp · C EV +6.59 (adj +3.40) on $15.84, P(profit) 0.6893, adj growth 31.8 bp · R EV +1.00 (adj +0.70) on $2.00, P(profit) 0.2068, adj growth 25.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10EDMSJ-SJ|yes == KXNHLGAME-26OCT10EDMSJ-EDM|no

## MIN @ FLA  ·  10000 joint draws  ·  400 bet sides mapped, 18 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_MIN_win | p_overtime | goals | shots FLA/MIN | FLA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.47 | 0.53 | 0.00 | 6.03 | 28.1/27.9 | 24.2/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.49 | 0.51 | 0.46 | 5.96 | 28.2/28.1 | 24.8/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.48 | 0.52 | 0.00 | 9.35 | 29.7/29.5 | 23.0/24.0 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.076 | 0.52 | 0.48 | 0.00 | 6.0 | 33.1/22.3 | 19.0/29.3 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.47 | 0.53 | 0.50 | 5.97 | 33.5/22.7 | 19.3/30.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.056 | 0.38 | 0.62 | 0.00 | 5.97 | 22.2/32.4 | 28.3/19.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 9 | 0.139 | 0.118 | +0.044 | +0.023 | $1.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Anton Lundell: 1+ goals YES | 17 | 0.220 | 0.207 | +0.041 | +0.027 | $2.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 67 | 0.734 | 0.717 | +0.048 | +0.031 | $6.70 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Sandis Vilmanis: 1+ goals YES | 10 | 0.148 | 0.126 | +0.042 | +0.020 | $1.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5|yes; why: higher confidence-adjusted growth (12.56 vs 4.91 bp); despite a smaller raw edge (+0.044 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.909 vs 0.531); relationships: KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT10MINFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: MIN offense suppressed (<= 2 goals)
- **Anton Lundell: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT10MINFLA-8|yes; why: higher confidence-adjusted growth (10.41 vs 1.50 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.881 vs 0.331); relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT10MINFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: FLA offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT10MINFLA-FLA|no; why: higher confidence-adjusted growth (9.89 vs 3.45 bp); despite a smaller raw edge (+0.048 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: FLA offense succeeds (4+ goals)
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes has the higher standalone adjusted growth (10.41 vs 8.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT10MINFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis FLA:OFFENSE_4PLUS (p 0.379): highest fidelity KXNHLTOTAL-26OCT10MINFLA-7|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.403): highest fidelity KXNHLSPREAD-26OCT10MINFLA-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10MINFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.4144): highest fidelity KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4|yes (same contract)
- KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3583, phi -0.151)
- KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.403, phi -0.215)
- KXNHLGOAL-26OCT10MINFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.379, phi -0.237)
- KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.403, phi -0.18)

portfolios: A EV +2.00 (adj +0.51) on $13.76, P(profit) 0.541, adj growth 4.7 bp · B EV +2.50 (adj +1.41) on $12.69, P(profit) 0.4341, adj growth 13.4 bp · C EV +2.09 (adj +1.17) on $14.91, P(profit) 0.3514, adj growth 11.0 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.7338, adj growth 3.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10MINFLA-MIN|yes == KXNHLGAME-26OCT10MINFLA-FLA|no

## UTA @ BUF  ·  10000 joint draws  ·  412 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_UTA_win | p_overtime | goals | shots BUF/UTA | BUF/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.53 | 0.47 | 0.00 | 6.06 | 27.4/27.3 | 23.9/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.47 | 5.97 | 27.5/27.4 | 24.1/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.50 | 0.50 | 0.00 | 9.39 | 29.0/28.8 | 22.5/22.8 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.084 | 0.61 | 0.39 | 0.00 | 5.99 | 32.1/21.4 | 18.4/28.0 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.51 | 6.0 | 32.6/21.8 | 18.6/29.2 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.058 | 0.56 | 0.44 | 0.00 | 9.25 | 34.3/23.2 | 17.9/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vincent Trocheck: 1+ assists NO | 69 | 0.817 | 0.721 | +0.112 | +0.016 | $6.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ goals NO | 62 | 0.667 | 0.653 | +0.031 | +0.016 | $3.86 | FUNDED_RESEARCH | $1 | BUF:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT10UTABUF-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (2.83 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT10UTABUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: UTA offense succeeds (4+ goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT10UTABUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (2.53 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:SUPPRESSED (p 0.3958): highest fidelity KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3634): highest fidelity KXNHLGOAL-26OCT10UTABUF-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10UTABUF-BUFTTHOMPSON72-1|no (same contract)
- KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.7 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3992, phi -0.213)
- KXNHLGOAL-26OCT10UTABUF-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.416, phi -0.251)

portfolios: A EV +1.14 (adj +0.27) on $11.00, P(profit) 0.5433, adj growth 2.6 bp · B EV +1.15 (adj +0.24) on $9.95, P(profit) 0.5433, adj growth 2.3 bp · C EV +1.56 (adj +0.33) on $13.53, P(profit) 0.5433, adj growth 3.1 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.6671, adj growth 1.0 bp

## DET @ MTL  ·  10000 joint draws  ·  394 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_DET_win | p_overtime | goals | shots MTL/DET | MTL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.69 | 0.31 | 0.00 | 6.01 | 27.0/27.3 | 24.6/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.45 | 5.9 | 27.4/27.8 | 24.6/24.1 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.093 | 0.66 | 0.34 | 0.00 | 6.0 | 21.8/32.6 | 29.4/17.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.69 | 0.31 | 0.00 | 9.29 | 28.8/29.2 | 24.3/21.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.50 | 0.50 | 0.47 | 5.92 | 21.8/32.8 | 29.4/18.6 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.061 | 0.65 | 0.35 | 0.00 | 9.22 | 23.4/34.6 | 28.9/16.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cole Caufield: 1+ goals NO | 55 | 0.594 | 0.582 | +0.026 | +0.014 | $2.77 | FUNDED_RESEARCH | $1 | MTL:SUPPRESSED | DIRECT (0.78) | EVIDENCE_STRONGER | D |
- **Cole Caufield: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT10DETMTL-MTLCKREIDER22-1|no; why: higher confidence-adjusted growth (1.80 vs 0.00 bp); despite a smaller raw edge (+0.026 vs +0.057/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis MTL:SUPPRESSED (p 0.3124): highest fidelity KXNHLGOAL-26OCT10DETMTL-MTLCCAUFIELD13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10DETMTL-MTLCCAUFIELD13-1|no (same contract)
- KXNHLGOAL-26OCT10DETMTL-MTLCCAUFIELD13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4816, phi -0.243)

portfolios: A EV +0.19 (adj +0.10) on $4.19, P(profit) 0.5937, adj growth 1.0 bp · B EV +0.13 (adj +0.07) on $2.77, P(profit) 0.5937, adj growth 0.7 bp · C EV +0.18 (adj +0.09) on $3.76, P(profit) 0.5937, adj growth 0.9 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.5937, adj growth 0.9 bp

## NSH @ OTT  ·  10000 joint draws  ·  400 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NSH_win | p_overtime | goals | shots OTT/NSH | OTT/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.133 | 0.69 | 0.31 | 0.00 | 6.0 | 33.6/21.9 | 19.4/28.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.62 | 0.38 | 0.00 | 6.05 | 28.4/27.6 | 24.6/24.3 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.55 | 0.45 | 0.50 | 5.93 | 33.8/22.0 | 18.8/30.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.48 | 0.52 | 0.46 | 5.95 | 28.3/27.6 | 24.3/25.0 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.087 | 0.71 | 0.29 | 0.00 | 9.36 | 35.7/23.4 | 18.7/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.62 | 0.38 | 0.00 | 9.36 | 29.8/28.9 | 23.3/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Michael Amadio: 1+ goals YES | 16 | 0.212 | 0.196 | +0.042 | +0.027 | $2.58 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 23 | 0.282 | 0.268 | +0.040 | +0.025 | $2.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Claude Giroux: 1+ goals YES | 19 | 0.230 | 0.218 | +0.029 | +0.018 | $2.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Carter Yakemchuk: 1+ assists NO | 68 | 0.763 | 0.714 | +0.068 | +0.019 | $6.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10NSHOTT-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (11.00 vs 4.23 bp); relationships: KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT10NSHOTT-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT10NSHOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.039); failure: OTT offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT10NSHOTT-9|yes; why: higher confidence-adjusted growth (7.59 vs 0.03 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.929 vs 0.379); alternative not eligible: confidence-adjusted EV +0.0014 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT10NSHOTT-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT10NSHOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: NSH offense suppressed (<= 2 goals)
- **Claude Giroux: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (11.00 vs 4.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT10NSHOTT-OTTCYAKEMCHUK26-1|no: INTENTIONAL_DIVERSIFIER (phi -0.083); failure: OTT offense suppressed (<= 2 goals)
- **Carter Yakemchuk: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10NSHOTT-OTTDBATHERSON19-1|no; why: higher confidence-adjusted growth (3.71 vs 0.27 bp); alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.039); KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT10NSHOTT-OTTCGIROUX28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.083); failure: OTT offense succeeds (4+ goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.4604): highest fidelity KXNHLGOAL-26OCT10NSHOTT-OTTCGIROUX28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.3268): highest fidelity KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3217): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3217, phi -0.19)
- KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4537, phi -0.257)
- KXNHLGOAL-26OCT10NSHOTT-OTTCGIROUX28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3217, phi -0.221)
- KXNHLAST-26OCT10NSHOTT-OTTCYAKEMCHUK26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4604, phi -0.198)

portfolios: A EV +2.15 (adj +1.18) on $13.76, P(profit) 0.4925, adj growth 11.2 bp · B EV +2.03 (adj +1.05) on $13.99, P(profit) 0.4925, adj growth 10.1 bp · C EV +1.45 (adj +0.92) on $7.06, P(profit) 0.4334, adj growth 8.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ PIT  ·  10000 joint draws  ·  412 bet sides mapped, 10 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_DAL_win | p_overtime | goals | shots PIT/DAL | PIT/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.50 | 0.50 | 0.00 | 6.01 | 26.5/26.4 | 22.9/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.47 | 5.99 | 26.4/26.3 | 23.1/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.49 | 0.51 | 0.00 | 9.35 | 28.0/28.0 | 21.8/21.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.081 | 0.59 | 0.41 | 0.00 | 6.01 | 31.3/20.8 | 17.8/27.1 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.56 | 0.44 | 0.46 | 5.94 | 31.3/21.1 | 17.9/27.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.058 | 0.62 | 0.38 | 0.00 | 9.24 | 32.6/22.3 | 17.3/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Bryan Rust: 1+ goals YES | 26 | 0.323 | 0.305 | +0.049 | +0.031 | $3.26 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Roope Hintz: 1+ assists NO | 56 | 0.709 | 0.606 | +0.131 | +0.028 | $5.71 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 64 | 0.722 | 0.679 | +0.066 | +0.022 | $3.13 | FUNDED_RESEARCH | $1 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT10DALPIT-DAL2|no; why: higher confidence-adjusted growth (10.58 vs 4.94 bp); despite a smaller raw edge (+0.049 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSPREAD-26OCT10DALPIT-DAL2|no: MOSTLY_INDEPENDENT (phi 0.146); failure: PIT offense suppressed (<= 2 goals)
- **Roope Hintz: 1+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10DALPIT-DAL2|no; why: higher confidence-adjusted growth (7.16 vs 4.94 bp); relationships: KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSPREAD-26OCT10DALPIT-DAL2|no: REINFORCING (phi 0.16); failure: DAL offense succeeds (4+ goals)
- **Dallas wins by over 1.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLGAME-26OCT10DALPIT-DAL|no; why: higher confidence-adjusted growth (4.94 vs 4.78 bp); despite a smaller raw edge (+0.066 vs +0.068/contract); relationships: KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: REINFORCING (phi 0.16); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis PIT:OFFENSE_4PLUS (p 0.4065): highest fidelity KXNHLSPREAD-26OCT10DALPIT-DAL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.3833): highest fidelity KXNHLSPREAD-26OCT10DALPIT-DAL3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.5055): highest fidelity KXNHLGAME-26OCT10DALPIT-DAL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10DALPIT-DAL|no (same contract)
- KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3792, phi -0.248)
- KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.398, phi -0.249)
- KXNHLSPREAD-26OCT10DALPIT-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.2777, phi -1.0)

portfolios: A EV +2.06 (adj +0.55) on $13.76, P(profit) 0.5532, adj growth 5.1 bp · B EV +2.20 (adj +0.76) on $12.10, P(profit) 0.6457, adj growth 7.3 bp · C EV +3.06 (adj +1.05) on $17.11, P(profit) 0.6457, adj growth 9.9 bp · R EV +0.28 (adj +0.15) on $2.00, P(profit) 0.3228, adj growth 5.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10DALPIT-PIT|yes == KXNHLGAME-26OCT10DALPIT-DAL|no

## CAR @ CHI  ·  10000 joint draws  ·  404 bet sides mapped, 16 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_CAR_win | p_overtime | goals | shots CHI/CAR | CHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.178 | 0.36 | 0.64 | 0.00 | 6.03 | 20.4/33.2 | 28.7/17.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.141 | 0.44 | 0.56 | 0.44 | 5.89 | 20.8/33.7 | 30.2/17.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.124 | 0.32 | 0.68 | 0.00 | 9.25 | 21.8/35.0 | 27.3/17.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.083 | 0.38 | 0.62 | 0.00 | 6.06 | 26.0/27.3 | 23.4/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.50 | 0.50 | 0.48 | 5.98 | 26.1/27.1 | 23.8/22.8 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.070 | 0.34 | 0.66 | 0.00 | 3.47 | 19.2/31.8 | 29.5/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 13 | 0.170 | 0.158 | +0.033 | +0.020 | $1.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 67 | 0.755 | 0.710 | +0.070 | +0.025 | $5.14 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 67 | 0.722 | 0.705 | +0.036 | +0.019 | $4.55 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Andrei Svechnikov: 1+ goals NO | 65 | 0.695 | 0.680 | +0.029 | +0.014 | $2.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes; why: KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes has the higher standalone adjusted growth (9.42 vs 7.17 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.176); relationships: KXNHLSPREAD-26OCT10CARCHI-CAR3|no: MOSTLY_INDEPENDENT (phi 0.119); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT10CARCHI-CARASVECHNIKOV37-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: CHI offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT10CARCHI-CAR2|no; why: Broad expression KXNHLSPREAD-26OCT10CARCHI-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.119); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: REINFORCING (phi 0.155); KXNHLGOAL-26OCT10CARCHI-CARASVECHNIKOV37-1|no: REINFORCING (phi 0.161); failure: CAR wins by 2+
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10CARCHI-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT10CARCHI-CAR3|no has the higher standalone adjusted growth (6.21 vs 3.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.155); they share one thesis budget; relationships: KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26OCT10CARCHI-CAR3|no: REINFORCING (phi 0.155); KXNHLGOAL-26OCT10CARCHI-CARASVECHNIKOV37-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: CAR offense succeeds (4+ goals)
- **Andrei Svechnikov: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10CARCHI-CAR3|no; why: Player prop expression KXNHLGOAL-26OCT10CARCHI-CARASVECHNIKOV37-1|no selected over player prop KXNHLAST-26OCT10CARCHI-CARSAHO20-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.85 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT10CARCHI-CAR3|no: REINFORCING (phi 0.161); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.18, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis CHI:WINS (p 0.4113): highest fidelity KXNHLSPREAD-26OCT10CARCHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes — Broad expression KXNHLSPREAD-26OCT10CARCHI-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CHI:OFFENSE_4PLUS (p 0.3355): highest fidelity KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes (same contract)
- thesis CHI:WINS_BY_2PLUS (p 0.2117): highest fidelity KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes (same contract)
- KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4475, phi -0.221)
- KXNHLSPREAD-26OCT10CARCHI-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3664, phi -0.748)
- KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4646, phi -0.223)
- KXNHLGOAL-26OCT10CARCHI-CARASVECHNIKOV37-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4646, phi -0.243)
- override: Broad expression KXNHLSPREAD-26OCT10CARCHI-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26OCT10CARCHI-CARASVECHNIKOV37-1|no selected over player prop KXNHLAST-26OCT10CARCHI-CARSAHO20-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.85 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.76 (adj +0.48) on $13.76, P(profit) 0.4719, adj growth 4.2 bp · B EV +1.27 (adj +0.61) on $14.15, P(profit) 0.5092, adj growth 5.8 bp · C EV +1.66 (adj +0.61) on $15.28, P(profit) 0.6648, adj growth 5.8 bp · R EV +0.31 (adj +0.13) on $4.00, P(profit) 0.5748, adj growth 4.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10CARCHI-CAR|no == KXNHLGAME-26OCT10CARCHI-CHI|yes

## CBJ @ STL  ·  10000 joint draws  ·  416 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_CBJ_win | p_overtime | goals | shots STL/CBJ | STL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.62 | 0.38 | 0.00 | 5.98 | 27.0/27.2 | 24.2/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.47 | 5.85 | 26.9/27.1 | 23.9/23.6 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.083 | 0.51 | 0.49 | 0.00 | 5.98 | 21.4/32.0 | 28.5/18.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.61 | 0.39 | 0.00 | 9.17 | 28.6/28.7 | 23.3/21.9 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.49 | 0.51 | 0.47 | 5.89 | 21.3/32.3 | 28.7/18.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.60 | 0.40 | 0.00 | 3.46 | 25.8/26.0 | 24.4/23.6 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Conor Garland: 1+ goals NO | 83 | 0.890 | 0.872 | +0.050 | +0.032 | $6.70 | FUNDED_RESEARCH | $2 | CBJ:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Adam Fantilli: 1+ assists NO | 61 | 0.687 | 0.641 | +0.060 | +0.014 | $3.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10CBJSTL-CBJAFANTILLI19-1|no; why: higher confidence-adjusted growth (17.34 vs 1.96 bp); despite a smaller raw edge (+0.050 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT10CBJSTL-CBJAFANTILLI19-1|no: MOSTLY_INDEPENDENT (phi 0.038); failure: CBJ offense succeeds (4+ goals)
- **Adam Fantilli: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (1.96 vs 0.03 bp); despite a smaller raw edge (+0.060 vs +0.071/contract); alternative not eligible: confidence-adjusted EV +0.0017 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10CBJSTL-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.038); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CBJ:SUPPRESSED (p 0.4684): highest fidelity KXNHLAST-26OCT10CBJSTL-CBJAFANTILLI19-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10CBJSTL-CBJAFANTILLI19-1|no (same contract)
- KXNHLGOAL-26OCT10CBJSTL-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3118, phi -0.138)
- KXNHLAST-26OCT10CBJSTL-CBJAFANTILLI19-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3118, phi -0.265)

portfolios: A EV +0.86 (adj +0.34) on $11.00, P(profit) 0.6168, adj growth 3.3 bp · B EV +0.72 (adj +0.33) on $10.01, P(profit) 0.6168, adj growth 3.3 bp · C EV +0.45 (adj +0.11) on $4.68, P(profit) 0.6872, adj growth 1.0 bp · R EV +0.12 (adj +0.08) on $2.00, P(profit) 0.8896, adj growth 3.0 bp

## TOR @ COL  ·  10000 joint draws  ·  424 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_TOR_win | p_overtime | goals | shots COL/TOR | COL/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.193 | 0.77 | 0.23 | 0.00 | 6.05 | 36.9/22.2 | 19.9/31.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.157 | 0.80 | 0.20 | 0.00 | 9.36 | 38.5/23.8 | 19.8/29.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.141 | 0.56 | 0.44 | 0.46 | 5.94 | 37.0/22.5 | 19.3/33.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.078 | 0.76 | 0.24 | 0.00 | 6.06 | 30.2/28.8 | 26.3/25.4 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.070 | 0.71 | 0.29 | 0.00 | 3.52 | 35.6/21.4 | 20.2/32.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.54 | 0.46 | 0.48 | 6.06 | 30.1/28.7 | 25.1/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zachary L'Heureux: 1+ goals YES | 12 | 0.165 | 0.149 | +0.038 | +0.022 | $1.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:WINS_BY_2PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Martin Necas: 1+ goals NO | 62 | 0.668 | 0.653 | +0.031 | +0.017 | $3.84 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 77 | 0.806 | 0.793 | +0.024 | +0.011 | $4.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Zachary L'Heureux: 1+ goals YES** — thesis: COL wins by 2+; alternative: KXNHLPTS-26OCT10TORCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (9.08 vs 0.00 bp); despite a smaller raw edge (+0.038 vs +0.049/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: COL offense suppressed (<= 2 goals)
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10TORCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (2.67 vs 0.83 bp); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: COL offense succeeds (4+ goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no has the higher standalone adjusted growth (2.67 vs 1.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.19, COL shot control · high event (8+) · decided (2+) 0.16, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.14.
- thesis COL:SUPPRESSED (p 0.2507): highest fidelity KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no (same contract)
- thesis COL:WINS_BY_2PLUS (p 0.4642): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2507, phi -0.151)
- KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5575, phi -0.225)
- KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5575, phi -0.173)

portfolios: A EV +1.31 (adj +0.72) on $13.76, P(profit) 0.612, adj growth 6.7 bp · B EV +0.87 (adj +0.48) on $10.00, P(profit) 0.612, adj growth 4.6 bp · C EV +0.26 (adj +0.14) on $5.35, P(profit) 0.6677, adj growth 1.3 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.6677, adj growth 1.0 bp

## TBL @ NYI  ·  10000 joint draws  ·  388 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_TBL_win | p_overtime | goals | shots NYI/TBL | NYI/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.53 | 0.47 | 0.00 | 5.97 | 26.9/27.1 | 23.8/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.54 | 0.46 | 0.45 | 5.89 | 26.9/27.1 | 24.0/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.51 | 0.49 | 0.00 | 9.31 | 28.1/28.3 | 22.5/21.9 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.44 | 0.56 | 0.48 | 5.82 | 21.4/31.8 | 28.4/18.4 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.072 | 0.49 | 0.51 | 0.00 | 5.98 | 21.5/31.8 | 28.1/18.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.53 | 0.47 | 0.00 | 3.45 | 25.5/25.6 | 23.8/23.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| John Carlson: 1+ assists NO | 51 | 0.737 | 0.586 | +0.209 | +0.059 | $6.20 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Brayden Schenn: 1+ goals YES | 19 | 0.263 | 0.240 | +0.063 | +0.039 | $3.21 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 75 | 0.842 | 0.793 | +0.078 | +0.030 | $6.20 | FUNDED_RESEARCH | $2 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ondrej Palat: 1+ goals YES | 10 | 0.139 | 0.123 | +0.033 | +0.017 | $1.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10TBNYI-TB3|no; why: higher confidence-adjusted growth (30.20 vs 11.10 bp); relationships: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT10TBNYI-TB3|no: MOSTLY_INDEPENDENT (phi 0.14); KXNHLGOAL-26OCT10TBNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: TBL offense succeeds (4+ goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT10TBNYI-TB3|no; why: higher confidence-adjusted growth (20.68 vs 11.10 bp); despite a smaller raw edge (+0.063 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT10TBNYI-TB3|no: MOSTLY_INDEPENDENT (phi 0.126); KXNHLGOAL-26OCT10TBNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: NYI offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGAME-26OCT10TBNYI-NYI|yes; why: higher confidence-adjusted growth (11.10 vs 7.00 bp); despite a smaller raw edge (+0.078 vs +0.119/contract); relationships: KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.14); KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.126); KXNHLGOAL-26OCT10TBNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.085); failure: TBL wins by 2+
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (20.68 vs 6.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSPREAD-26OCT10TBNYI-TB3|no: MOSTLY_INDEPENDENT (phi 0.085); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis TBL:SUPPRESSED (p 0.4421): highest fidelity KXNHLSPREAD-26OCT10TBNYI-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:OFFENSE_4PLUS (p 0.359): highest fidelity KXNHLTEAMTOTAL-26OCT10TBNYI-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.5156): highest fidelity KXNHLSPREAD-26OCT10TBNYI-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10TBNYI-TB3|no (same contract)
- KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 23.2 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3381, phi -0.207)
- KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4154, phi -0.248)
- KXNHLSPREAD-26OCT10TBNYI-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.258, phi -0.736)
- KXNHLGOAL-26OCT10TBNYI-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4154, phi -0.159)

portfolios: A EV +4.08 (adj +0.82) on $13.76, P(profit) 0.6554, adj growth 7.8 bp · B EV +4.45 (adj +1.74) on $16.74, P(profit) 0.74, adj growth 16.8 bp · C EV +5.98 (adj +2.29) on $22.78, P(profit) 0.7232, adj growth 21.8 bp · R EV +0.52 (adj +0.27) on $3.00, P(profit) 0.2634, adj growth 10.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10TBNYI-TB|no == KXNHLGAME-26OCT10TBNYI-NYI|yes

## ANA @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_ANA_win | p_overtime | goals | shots CGY/ANA | CGY/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.51 | 0.49 | 0.00 | 6.02 | 28.6/29.1 | 25.6/25.0 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.105 | 0.47 | 0.53 | 0.00 | 6.0 | 22.8/34.5 | 30.6/19.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.48 | 0.52 | 0.50 | 6.02 | 28.7/29.1 | 25.7/25.3 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.49 | 0.51 | 0.46 | 5.95 | 23.0/34.7 | 31.3/19.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.52 | 0.48 | 0.00 | 9.42 | 30.2/30.9 | 24.8/23.6 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.074 | 0.44 | 0.56 | 0.00 | 9.37 | 24.2/36.2 | 29.0/18.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## LAK @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_LAK_win | p_overtime | goals | shots VGK/LAK | VGK/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.62 | 0.38 | 0.00 | 5.95 | 27.3/27.1 | 24.1/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.46 | 5.94 | 27.7/27.5 | 24.2/24.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.096 | 0.70 | 0.30 | 0.00 | 5.99 | 32.4/21.4 | 18.9/27.9 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.58 | 0.42 | 0.45 | 5.88 | 32.7/22.0 | 19.0/29.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.64 | 0.36 | 0.00 | 9.2 | 28.9/28.7 | 23.7/22.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.63 | 0.37 | 0.00 | 3.44 | 26.1/25.9 | 24.5/23.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
