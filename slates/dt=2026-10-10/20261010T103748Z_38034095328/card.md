# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-10T10:37:48Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +29.39 | +7.28 | +28.74 | 0.764 | -22.23 | -35.64 | 64.78 |
| B thesis-diversified (joint) ← optimiser card | 149.06 | +29.12 | +13.23 | +26.90 | 0.734 | -25.13 | -37.75 | 122.53 |
| C best expression per thesis | 149.98 | +30.13 | +13.02 | +26.23 | 0.680 | -38.89 | -55.05 | 114.47 |
| R FUNDED research stakes | 30.00 | +4.26 | +1.66 | +4.38 | 0.687 | -6.58 | -9.72 | 0.00 |

## PHI @ BOS  ·  10000 joint draws  ·  426 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_PHI_win | p_overtime | goals | shots BOS/PHI | BOS/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.56 | 0.44 | 0.00 | 5.99 | 26.9/26.9 | 23.6/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.48 | 5.87 | 26.9/27.0 | 23.8/23.6 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.079 | 0.65 | 0.35 | 0.00 | 5.94 | 31.6/21.2 | 18.6/27.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.58 | 0.42 | 0.00 | 9.2 | 28.4/28.3 | 22.9/22.1 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.56 | 0.44 | 0.44 | 5.83 | 31.9/21.4 | 18.2/28.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.54 | 0.46 | 0.47 | 2.84 | 25.7/25.5 | 24.1/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Sanheim: 1+ goals YES | 6 | 0.098 | 0.087 | +0.034 | +0.023 | $3.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 61 | 0.673 | 0.656 | +0.046 | +0.029 | $8.26 | FUNDED_RESEARCH | $3 | BOS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 14 | 0.183 | 0.168 | +0.034 | +0.020 | $3.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ goals NO | 74 | 0.790 | 0.775 | +0.036 | +0.021 | $9.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (19.09 vs 6.73 bp); despite a smaller raw edge (+0.034 vs +0.034/contract); relationships: KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: PHI offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (7.96 vs 5.38 bp); relationships: KXNHLGOAL-26OCT10PHIBOS-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: BOS offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT10PHIBOS-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (6.73 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT10PHIBOS-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: PHI offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no; why: Player prop expression KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no selected over player prop KXNHLAST-26OCT10PHIBOS-BOSJPETERKA10-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.89 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT10PHIBOS-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BOS shot control · normal event (5-7) · decided (2+) 0.08.
- thesis BOS:SUPPRESSED (p 0.3883): highest fidelity KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no — Player prop expression KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no selected over player prop KXNHLAST-26OCT10PHIBOS-BOSJPETERKA10-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.89 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:OFFENSE_4PLUS (p 0.3107): highest fidelity KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes (same contract)
- KXNHLGOAL-26OCT10PHIBOS-PHITSANHEIM6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4679, phi -0.161)
- KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3862, phi -0.272)
- KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4679, phi -0.244)
- KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3862, phi -0.211)
- override: Player prop expression KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no selected over player prop KXNHLAST-26OCT10PHIBOS-BOSJPETERKA10-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.89 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.37 (adj +0.71) on $19.23, P(profit) 0.765, adj growth 6.9 bp · B EV +3.40 (adj +2.18) on $23.60, P(profit) 0.6407, adj growth 20.1 bp · C EV +2.47 (adj +1.50) on $23.09, P(profit) 0.731, adj growth 13.3 bp · R EV +0.22 (adj +0.14) on $3.00, P(profit) 0.6727, adj growth 5.2 bp

## VAN @ NJD  ·  10000 joint draws  ·  412 bet sides mapped, 27 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_VAN_win | p_overtime | goals | shots NJD/VAN | NJD/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.135 | 0.65 | 0.35 | 0.00 | 5.98 | 34.1/21.9 | 19.2/29.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.54 | 0.46 | 0.47 | 5.91 | 34.3/22.0 | 18.9/30.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.56 | 0.44 | 0.00 | 6.0 | 28.5/27.6 | 24.2/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.50 | 0.50 | 0.46 | 5.92 | 28.5/27.6 | 24.3/25.2 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.090 | 0.64 | 0.36 | 0.00 | 9.2 | 35.8/23.2 | 18.3/28.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.55 | 0.45 | 0.00 | 9.34 | 29.8/29.0 | 23.0/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Luke Evangelista: 1+ assists NO | 57 | 0.762 | 0.631 | +0.175 | +0.044 | $9.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| New Jersey wins by over 1.5 goals NO | 51 | 0.663 | 0.560 | +0.136 | +0.033 | $4.21 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 58 | 0.648 | 0.629 | +0.051 | +0.032 | $7.47 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 2.5 goals NO | 64 | 0.781 | 0.686 | +0.125 | +0.030 | $6.58 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (21.04 vs 17.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.115); relationships: KXNHLSPREAD-26OCT10VANNJ-NJ2|no: REINFORCING (phi 0.152); KXNHLGOAL-26OCT10VANNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.082); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.147); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (21.04 vs 9.47 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.284); relationships: KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.152); KXNHLGOAL-26OCT10VANNJ-NJJHUGHES86-1|no: REINFORCING (phi 0.152); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: DUPLICATIVE (phi 0.742); failure: NJD wins by 2+
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (21.04 vs 9.24 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.134); relationships: KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.082); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: REINFORCING (phi 0.152); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: REINFORCING (phi 0.159); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (21.04 vs 8.79 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.211); relationships: KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: DUPLICATIVE (phi 0.742); KXNHLGOAL-26OCT10VANNJ-NJJHUGHES86-1|no: REINFORCING (phi 0.159); failure: NJD wins by 2+

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.14, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.3397): highest fidelity KXNHLTEAMTOTAL-26OCT10VANNJ-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10VANNJ-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2297): highest fidelity KXNHLGAME-26OCT10VANNJ-VAN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10VANNJ-VAN|yes (same contract)
- thesis NJD:SUPPRESSED (p 0.353): highest fidelity KXNHLSPREAD-26OCT10VANNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.2 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4303, phi -0.218)
- KXNHLSPREAD-26OCT10VANNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.8 pts; opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3369, phi -1.0)
- KXNHLGOAL-26OCT10VANNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4303, phi -0.256)
- KXNHLSPREAD-26OCT10VANNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.6 pts; opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3369, phi -0.742)

portfolios: A EV +6.75 (adj +1.41) on $19.23, P(profit) 0.6671, adj growth 13.1 bp · B EV +5.97 (adj +1.71) on $28.26, P(profit) 0.7458, adj growth 16.1 bp · C EV +6.35 (adj +3.57) on $12.16, P(profit) 0.282, adj growth 30.8 bp · R EV +1.07 (adj +0.32) on $6.00, P(profit) 0.7366, adj growth 11.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10VANNJ-VAN|yes == KXNHLGAME-26OCT10VANNJ-NJ|no

## EDM @ SJS  ·  10000 joint draws  ·  424 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_EDM_win | p_overtime | goals | shots SJS/EDM | SJS/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.118 | 0.48 | 0.52 | 0.00 | 9.53 | 29.1/29.5 | 23.1/23.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.49 | 0.51 | 0.00 | 6.1 | 27.5/27.8 | 24.1/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.49 | 0.51 | 0.48 | 6.02 | 27.6/28.0 | 24.5/24.2 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.092 | 0.42 | 0.58 | 0.00 | 6.07 | 21.7/32.8 | 28.6/18.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.083 | 0.40 | 0.60 | 0.00 | 9.45 | 23.5/35.1 | 27.7/18.3 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.46 | 0.54 | 0.47 | 6.05 | 22.1/33.2 | 29.7/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 13 | 0.199 | 0.179 | +0.061 | +0.041 | $6.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 31 | 0.471 | 0.360 | +0.146 | +0.035 | $6.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ goals YES | 8 | 0.117 | 0.103 | +0.032 | +0.018 | $2.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Kasperi Kapanen: 1+ goals NO | 77 | 0.823 | 0.808 | +0.040 | +0.026 | $10.57 | FUNDED_RESEARCH | $3 | EDM:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10EDMSJ-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (29.99 vs 2.04 bp); despite a smaller raw edge (+0.061 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT10EDMSJ-EDMKKAPANEN42-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (11.96 vs 5.27 bp); relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.139); KXNHLGOAL-26OCT10EDMSJ-EDMKKAPANEN42-1|no: MOSTLY_INDEPENDENT (phi 0.061); failure: EDM offense succeeds (4+ goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10EDMSJ-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (8.87 vs 2.04 bp); despite a smaller raw edge (+0.032 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.139); KXNHLGOAL-26OCT10EDMSJ-EDMKKAPANEN42-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: EDM offense suppressed (<= 2 goals)
- **Kasperi Kapanen: 1+ goals NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no; why: second expression of the same thesis: KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no has the higher standalone adjusted growth (11.96 vs 8.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.061); they share one thesis budget; relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.061); KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:SUPPRESSED (p 0.3271): highest fidelity KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS (p 0.478): highest fidelity KXNHLGAME-26OCT10EDMSJ-EDM|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:OFFENSE_4PLUS (p 0.439): highest fidelity KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4|yes (same contract)
- KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3271, phi -0.198)
- KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.1 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4654, phi -0.319)
- KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3271, phi -0.151)
- KXNHLGOAL-26OCT10EDMSJ-EDMKKAPANEN42-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4654, phi -0.173)

portfolios: A EV +4.47 (adj +0.99) on $19.23, P(profit) 0.6616, adj growth 9.2 bp · B EV +7.49 (adj +3.57) on $26.62, P(profit) 0.6009, adj growth 32.9 bp · C EV +8.35 (adj +2.01) on $39.66, P(profit) 0.7059, adj growth 17.7 bp · R EV +0.15 (adj +0.10) on $3.00, P(profit) 0.8226, adj growth 3.8 bp

## MIN @ FLA  ·  10000 joint draws  ·  400 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_MIN_win | p_overtime | goals | shots FLA/MIN | FLA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.44 | 0.56 | 0.00 | 6.02 | 28.2/28.0 | 24.2/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.47 | 0.53 | 0.45 | 5.93 | 28.1/27.9 | 24.5/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.46 | 0.54 | 0.00 | 9.37 | 29.8/29.5 | 23.1/23.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.080 | 0.52 | 0.48 | 0.00 | 6.0 | 33.1/22.4 | 19.0/29.3 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.54 | 0.46 | 0.45 | 5.91 | 33.2/22.5 | 19.4/29.9 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.055 | 0.46 | 0.54 | 0.49 | 5.9 | 22.9/33.2 | 29.8/19.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Hartman: 1+ goals YES | 18 | 0.243 | 0.226 | +0.053 | +0.036 | $6.02 | FUNDED_RESEARCH | $2 | MIN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 9 | 0.141 | 0.122 | +0.045 | +0.026 | $3.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Sandis Vilmanis: 1+ goals YES | 10 | 0.151 | 0.132 | +0.044 | +0.025 | $3.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Anton Lundell: 1+ goals YES | 17 | 0.220 | 0.206 | +0.040 | +0.026 | $4.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4|yes; why: higher confidence-adjusted growth (17.69 vs 5.14 bp); despite a smaller raw edge (+0.053 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.92 vs 0.714); relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: MIN offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (17.69 vs 17.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense suppressed (<= 2 goals)
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes; why: higher confidence-adjusted growth (14.58 vs 9.95 bp); relationships: KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense suppressed (<= 2 goals)
- **Anton Lundell: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT10MINFLA-7|yes; why: higher confidence-adjusted growth (9.95 vs 1.44 bp); despite a smaller raw edge (+0.040 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.916 vs 0.678); relationships: KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4175): highest fidelity KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:OFFENSE_4PLUS (p 0.381): highest fidelity KXNHLTOTAL-26OCT10MINFLA-7|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:WINS (p 0.5265): highest fidelity KXNHLGAME-26OCT10MINFLA-MIN|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.359, phi -0.214)
- KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.359, phi -0.153)
- KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4023, phi -0.174)
- KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4023, phi -0.217)

portfolios: A EV +3.56 (adj +1.38) on $19.23, P(profit) 0.501, adj growth 12.5 bp · B EV +5.80 (adj +3.59) on $17.52, P(profit) 0.5719, adj growth 33.0 bp · C EV +5.06 (adj +3.02) on $21.09, P(profit) 0.4125, adj growth 26.4 bp · R EV +0.55 (adj +0.37) on $2.00, P(profit) 0.2429, adj growth 13.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10MINFLA-FLA|no == KXNHLGAME-26OCT10MINFLA-MIN|yes

## UTA @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_UTA_win | p_overtime | goals | shots BUF/UTA | BUF/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.54 | 0.46 | 0.00 | 6.03 | 27.7/27.6 | 24.1/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.47 | 5.98 | 27.3/27.2 | 23.8/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.50 | 0.50 | 0.00 | 9.36 | 28.9/29.0 | 22.8/22.4 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.082 | 0.58 | 0.42 | 0.00 | 6.03 | 32.4/21.8 | 18.6/28.2 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.55 | 0.45 | 0.46 | 5.93 | 32.1/21.7 | 18.5/28.7 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.062 | 0.45 | 0.55 | 0.00 | 5.99 | 21.7/31.7 | 27.6/18.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_DET_win | p_overtime | goals | shots MTL/DET | MTL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.64 | 0.36 | 0.00 | 5.99 | 26.9/27.4 | 24.5/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.49 | 5.95 | 27.4/27.7 | 24.4/23.7 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.095 | 0.59 | 0.41 | 0.00 | 5.96 | 21.7/32.7 | 29.6/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.66 | 0.34 | 0.00 | 9.29 | 28.7/29.0 | 23.8/21.5 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.50 | 0.50 | 0.48 | 5.83 | 21.8/32.7 | 29.3/18.7 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.062 | 0.58 | 0.42 | 0.00 | 9.18 | 23.3/34.7 | 29.0/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Montreal wins by over 2.5 goals NO | 70 | 0.762 | 0.729 | +0.047 | +0.014 | $7.62 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Montreal wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT10DETMTL-MTL2|no; why: higher confidence-adjusted growth (2.05 vs 0.98 bp); wins across more scripts (relative breadth 0.995 vs 0.873); relationships: only recommended bet in this game; failure: MTL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4331): highest fidelity KXNHLSPREAD-26OCT10DETMTL-MTL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10DETMTL-MTL3|no (same contract)
- KXNHLSPREAD-26OCT10DETMTL-MTL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.3601, phi -0.745)

portfolios: A EV +1.06 (adj +0.28) on $15.38, P(profit) 0.6399, adj growth 2.3 bp · B EV +0.50 (adj +0.15) on $7.62, P(profit) 0.762, adj growth 1.4 bp · C EV +0.80 (adj +0.23) on $12.07, P(profit) 0.762, adj growth 2.1 bp · R EV +0.13 (adj +0.04) on $2.00, P(profit) 0.762, adj growth 1.4 bp

## NSH @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NSH_win | p_overtime | goals | shots OTT/NSH | OTT/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.130 | 0.68 | 0.32 | 0.00 | 5.99 | 33.7/21.7 | 19.1/29.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.60 | 0.40 | 0.00 | 6.01 | 28.3/27.6 | 24.5/24.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.55 | 0.45 | 0.47 | 5.97 | 34.0/22.3 | 19.1/30.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.53 | 0.47 | 0.47 | 5.89 | 28.4/27.7 | 24.5/25.0 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.090 | 0.71 | 0.29 | 0.00 | 9.29 | 35.3/23.2 | 18.6/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.63 | 0.37 | 0.00 | 9.38 | 29.9/29.2 | 23.7/22.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_DAL_win | p_overtime | goals | shots PIT/DAL | PIT/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.54 | 0.46 | 0.00 | 6.04 | 26.6/26.5 | 23.2/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.52 | 0.48 | 0.47 | 5.96 | 26.4/26.4 | 23.1/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.55 | 0.45 | 0.00 | 9.38 | 28.4/28.1 | 22.3/21.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 6.03 | 31.2/20.7 | 17.8/27.0 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.53 | 0.47 | 0.48 | 5.98 | 31.2/20.8 | 17.7/27.9 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.060 | 0.67 | 0.33 | 0.00 | 9.35 | 32.9/22.3 | 17.5/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dallas wins by over 2.5 goals NO | 76 | 0.850 | 0.802 | +0.077 | +0.030 | $11.64 | FUNDED_RESEARCH | $3 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pittsburgh wins by over 1.5 goals YES | 23 | 0.319 | 0.272 | +0.076 | +0.029 | $3.20 | FUNDED_RESEARCH | $1 | PIT:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 2.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes; why: higher confidence-adjusted growth (11.06 vs 10.16 bp); wins across more scripts (relative breadth 1.012 vs 0.529); relationships: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes: REINFORCING (phi 0.287); failure: DAL wins by 2+
- **Pittsburgh wins by over 1.5 goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT10DALPIT-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT10DALPIT-DAL3|no has the higher standalone adjusted growth (11.06 vs 10.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.287); they share one thesis budget; relationships: KXNHLSPREAD-26OCT10DALPIT-DAL3|no: REINFORCING (phi 0.287); failure: DAL wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:WINS (p 0.5407): highest fidelity KXNHLSPREAD-26OCT10DALPIT-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10DALPIT-DAL3|no (same contract)
- thesis PIT:WINS_BY_2PLUS (p 0.3185): highest fidelity KXNHLSPREAD-26OCT10DALPIT-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10DALPIT-DAL3|no (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4338): highest fidelity KXNHLSPREAD-26OCT10DALPIT-DAL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT10DALPIT-DAL3|no (same contract)
- KXNHLSPREAD-26OCT10DALPIT-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.2467, phi -0.735)
- KXNHLSPREAD-26OCT10DALPIT-PIT2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.4593, phi -0.63)
- override: override declined: the joint re-optimisation gives KXNHLGAME-26OCT10DALPIT-DAL|no less than the minimum stake; KXNHLSPREAD-26OCT10DALPIT-PIT3|yes kept

portfolios: A EV +3.11 (adj +0.77) on $19.23, P(profit) 0.5407, adj growth 6.9 bp · B EV +2.16 (adj +0.83) on $14.84, P(profit) 0.8498, adj growth 7.9 bp · C EV +1.84 (adj +0.71) on $18.45, P(profit) 0.8498, adj growth 6.7 bp · R EV +0.61 (adj +0.24) on $4.00, P(profit) 0.3185, adj growth 8.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10DALPIT-PIT|yes == KXNHLGAME-26OCT10DALPIT-DAL|no

## CAR @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_CAR_win | p_overtime | goals | shots CHI/CAR | CHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.170 | 0.33 | 0.67 | 0.00 | 6.04 | 20.4/33.4 | 28.8/17.8 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.141 | 0.46 | 0.54 | 0.47 | 5.89 | 20.7/33.8 | 30.4/17.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.124 | 0.31 | 0.69 | 0.00 | 9.29 | 21.9/35.2 | 27.4/17.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.083 | 0.40 | 0.60 | 0.00 | 6.04 | 26.0/27.2 | 23.1/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.51 | 0.49 | 0.47 | 5.95 | 26.0/27.0 | 23.6/22.7 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.075 | 0.36 | 0.64 | 0.00 | 3.49 | 19.6/32.4 | 30.1/18.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 2.5 goals NO | 67 | 0.750 | 0.708 | +0.065 | +0.022 | $7.76 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Chicago over 1.5 goals scored YES | 71 | 0.781 | 0.743 | +0.057 | +0.019 | $5.98 | FUNDED_RESEARCH | $2 | CHI:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Chicago over 3.5 goals scored YES | 25 | 0.346 | 0.281 | +0.083 | +0.017 | $1.21 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT10CARCHI-CAR2|no; why: higher confidence-adjusted growth (5.01 vs 2.36 bp); despite a smaller raw edge (+0.065 vs +0.088/contract); wins across more scripts (relative breadth 1.035 vs 0.917); relationships: KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes: REINFORCING (phi 0.399); KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4|yes: REINFORCING (phi 0.355); failure: CAR wins by 2+
- **Chicago over 1.5 goals scored YES** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes; why: KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes has the higher standalone adjusted growth (11.61 vs 3.87 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.245); relationships: KXNHLSPREAD-26OCT10CARCHI-CAR3|no: REINFORCING (phi 0.399); KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4|yes: DUPLICATIVE (phi 0.385); failure: CHI offense suppressed (<= 2 goals)
- **Chicago over 3.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4|yes selected over broad KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.52 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT10CARCHI-CAR3|no: REINFORCING (phi 0.355); KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes: DUPLICATIVE (phi 0.385); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis CHI:OFFENSE_4PLUS (p 0.3362): highest fidelity KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes — Broad expression KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4|yes selected over broad KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.52 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CHI:WINS (p 0.409): highest fidelity KXNHLSPREAD-26OCT10CARCHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes — override declined: the joint re-optimisation gives KXNHLGAME-26OCT10CARCHI-CAR|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes kept
- thesis CHI:WINS_BY_2PLUS (p 0.2073): highest fidelity KXNHLSPREAD-26OCT10CARCHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT10CARCHI-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3642, phi -0.762)
- KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis CHI:SUPPRESSED (p 0.4513, phi -0.583)
- KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.1 pts; opposing: failure thesis CHI:SUPPRESSED (p 0.4513, phi -0.66)
- override: override declined: the joint re-optimisation gives KXNHLGAME-26OCT10CARCHI-CAR|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes kept
- override: Broad expression KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4|yes selected over broad KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.52 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.72 (adj +0.94) on $19.23, P(profit) 0.486, adj growth 6.9 bp · B EV +1.59 (adj +0.49) on $14.95, P(profit) 0.6576, adj growth 4.5 bp · C EV +3.37 (adj +1.28) on $17.05, P(profit) 0.753, adj growth 11.2 bp · R EV +0.66 (adj +0.18) on $5.00, P(profit) 0.6709, adj growth 6.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10CARCHI-CHI|yes == KXNHLGAME-26OCT10CARCHI-CAR|no

## CBJ @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_CBJ_win | p_overtime | goals | shots STL/CBJ | STL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.54 | 0.46 | 0.00 | 6.0 | 26.8/27.0 | 23.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.53 | 0.47 | 0.50 | 5.86 | 27.0/27.3 | 24.0/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.58 | 0.42 | 0.00 | 9.24 | 28.5/28.9 | 23.4/22.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.077 | 0.49 | 0.51 | 0.00 | 5.96 | 21.5/32.4 | 28.6/18.2 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.47 | 0.53 | 0.45 | 5.83 | 21.5/32.1 | 28.7/18.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.52 | 0.48 | 0.00 | 3.47 | 25.6/25.9 | 24.1/23.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_TOR_win | p_overtime | goals | shots COL/TOR | COL/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.188 | 0.77 | 0.23 | 0.00 | 6.04 | 36.8/22.1 | 19.8/31.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.157 | 0.78 | 0.22 | 0.00 | 9.35 | 38.5/23.6 | 19.5/29.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.139 | 0.58 | 0.42 | 0.48 | 5.96 | 37.1/22.6 | 19.4/33.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.079 | 0.73 | 0.27 | 0.00 | 6.01 | 30.2/28.7 | 26.1/25.5 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.073 | 0.73 | 0.27 | 0.00 | 3.45 | 35.6/21.2 | 20.1/33.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.064 | 0.72 | 0.28 | 0.00 | 9.39 | 31.7/30.3 | 25.4/23.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.19, COL shot control · high event (8+) · decided (2+) 0.16, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.14.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TBL @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_TBL_win | p_overtime | goals | shots NYI/TBL | NYI/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.55 | 0.45 | 0.00 | 6.0 | 26.6/26.9 | 23.7/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.50 | 0.50 | 0.49 | 5.93 | 27.1/27.2 | 23.9/23.9 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.085 | 0.45 | 0.55 | 0.00 | 5.94 | 21.6/31.7 | 27.9/18.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.52 | 0.48 | 0.00 | 9.15 | 28.4/28.4 | 22.6/22.6 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.47 | 0.53 | 0.47 | 5.82 | 21.6/32.0 | 28.4/18.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.51 | 2.83 | 25.5/25.6 | 24.2/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York I wins by over 1.5 goals YES | 21 | 0.287 | 0.246 | +0.065 | +0.024 | $2.27 | FUNDED_RESEARCH | $1 | NYI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I wins YES | 38 | 0.514 | 0.424 | +0.118 | +0.027 | $1.73 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 76 | 0.840 | 0.795 | +0.068 | +0.022 | $11.64 | FUNDED_RESEARCH | $3 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New York I wins by over 1.5 goals YES** — thesis: NYI wins by 2+; alternative: KXNHLGAME-26OCT10TBNYI-NYI|yes; why: higher confidence-adjusted growth (7.41 vs 6.79 bp); despite a smaller raw edge (+0.065 vs +0.118/contract); relationships: KXNHLGAME-26OCT10TBNYI-NYI|yes: DUPLICATIVE (phi 0.616); KXNHLSPREAD-26OCT10TBNYI-TB3|no: REINFORCING (phi 0.276); failure: TBL wins (incl. OT/SO)
- **New York I wins YES** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10TBNYI-NYI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT10TBNYI-NYI2|yes has the higher standalone adjusted growth (7.41 vs 6.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.616); they share one thesis budget; relationships: KXNHLSPREAD-26OCT10TBNYI-NYI2|yes: DUPLICATIVE (phi 0.616); KXNHLSPREAD-26OCT10TBNYI-TB3|no: DUPLICATIVE (phi 0.449); failure: TBL wins (incl. OT/SO)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10TBNYI-NYI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT10TBNYI-NYI2|yes has the higher standalone adjusted growth (7.41 vs 6.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.276); they share one thesis budget; relationships: KXNHLSPREAD-26OCT10TBNYI-NYI2|yes: REINFORCING (phi 0.276); KXNHLGAME-26OCT10TBNYI-NYI|yes: DUPLICATIVE (phi 0.449); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:WINS_BY_2PLUS (p 0.2868): highest fidelity KXNHLGAME-26OCT10TBNYI-NYI|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10TBNYI-NYI|yes (same contract)
- thesis NYI:WINS (p 0.5144): highest fidelity KXNHLGAME-26OCT10TBNYI-NYI|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10TBNYI-NYI|yes (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3603): highest fidelity KXNHLTEAMTOTAL-26OCT10TBNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10TBNYI-NYI|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT10TBNYI-NYI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS (p 0.4856, phi -0.616)
- KXNHLGAME-26OCT10TBNYI-NYI|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.9 pts; opposing: failure thesis TBL:WINS (p 0.4856, phi -1.0)
- KXNHLSPREAD-26OCT10TBNYI-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.265, phi -0.726)

portfolios: A EV +3.35 (adj +0.80) on $19.23, P(profit) 0.5144, adj growth 7.1 bp · B EV +2.20 (adj +0.71) on $15.65, P(profit) 0.5144, adj growth 6.6 bp · C EV +1.89 (adj +0.70) on $6.41, P(profit) 0.2868, adj growth 6.2 bp · R EV +0.85 (adj +0.27) on $5.00, P(profit) 0.5144, adj growth 9.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10TBNYI-TB|no == KXNHLGAME-26OCT10TBNYI-NYI|yes

## ANA @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_ANA_win | p_overtime | goals | shots CGY/ANA | CGY/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.48 | 0.52 | 0.00 | 6.06 | 28.7/29.2 | 25.4/25.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.110 | 0.43 | 0.57 | 0.00 | 6.04 | 22.5/34.6 | 30.6/19.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.48 | 0.52 | 0.47 | 6.03 | 28.7/29.2 | 25.7/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.46 | 0.54 | 0.00 | 9.4 | 30.0/30.8 | 24.2/24.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.47 | 0.53 | 0.45 | 5.98 | 22.7/34.5 | 31.0/19.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.080 | 0.38 | 0.62 | 0.00 | 9.28 | 24.2/36.3 | 28.8/19.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## LAK @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_LAK_win | p_overtime | goals | shots VGK/LAK | VGK/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.62 | 0.38 | 0.00 | 6.0 | 27.5/27.1 | 23.9/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.50 | 0.50 | 0.47 | 5.87 | 27.4/27.1 | 23.9/24.1 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.090 | 0.67 | 0.33 | 0.00 | 5.99 | 32.5/21.6 | 18.9/28.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.60 | 0.40 | 0.48 | 5.86 | 32.6/21.6 | 18.6/29.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.63 | 0.37 | 0.00 | 9.18 | 28.8/28.8 | 23.5/22.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.62 | 0.38 | 0.00 | 3.42 | 26.2/26.0 | 24.5/24.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, VGK shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
