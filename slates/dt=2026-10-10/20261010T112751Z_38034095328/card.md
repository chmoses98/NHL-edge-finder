# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-10T11:27:51Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +28.85 | +8.72 | +27.80 | 0.768 | -19.02 | -31.77 | 80.13 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +29.08 | +13.20 | +27.11 | 0.770 | -18.86 | -30.20 | 124.69 |
| C best expression per thesis | 150.01 | +28.22 | +13.17 | +24.93 | 0.690 | -38.49 | -53.23 | 117.48 |
| R FUNDED research stakes | 33.00 | +4.93 | +2.27 | +4.15 | 0.672 | -7.21 | -10.24 | 0.00 |

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
| Travis Sanheim: 1+ goals YES | 6 | 0.098 | 0.087 | +0.034 | +0.023 | $2.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 61 | 0.673 | 0.656 | +0.046 | +0.029 | $6.10 | FUNDED_RESEARCH | $2 | BOS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 14 | 0.183 | 0.168 | +0.034 | +0.020 | $2.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ goals NO | 74 | 0.790 | 0.775 | +0.036 | +0.021 | $6.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
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

portfolios: A EV +1.87 (adj +0.56) on $15.67, P(profit) 0.765, adj growth 5.4 bp · B EV +2.52 (adj +1.61) on $17.44, P(profit) 0.6407, adj growth 15.2 bp · C EV +2.17 (adj +1.32) on $20.32, P(profit) 0.731, adj growth 11.9 bp · R EV +0.15 (adj +0.09) on $2.00, P(profit) 0.6727, adj growth 3.5 bp

## VAN @ NJD  ·  10000 joint draws  ·  412 bet sides mapped, 23 +EV candidates, 4 on card


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
| Drew O'Connor: 1+ goals YES | 13 | 0.189 | 0.174 | +0.051 | +0.037 | $3.89 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 57 | 0.762 | 0.631 | +0.175 | +0.044 | $8.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| New Jersey wins by over 1.5 goals NO | 51 | 0.663 | 0.560 | +0.136 | +0.033 | $2.23 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 2.5 goals NO | 64 | 0.781 | 0.686 | +0.125 | +0.030 | $5.73 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: higher confidence-adjusted growth (23.96 vs 21.04 bp); despite a smaller raw edge (+0.051 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.919 vs 0.485); relationships: KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.112); failure: VAN offense suppressed (<= 2 goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (21.04 vs 17.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.115); relationships: KXNHLGOAL-26OCT10VANNJ-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: REINFORCING (phi 0.152); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.147); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (21.04 vs 9.47 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.284); relationships: KXNHLGOAL-26OCT10VANNJ-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.139); KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.152); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: DUPLICATIVE (phi 0.742); failure: NJD wins by 2+
- **New Jersey wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (21.04 vs 8.79 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.211); relationships: KXNHLGOAL-26OCT10VANNJ-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.112); KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: DUPLICATIVE (phi 0.742); failure: NJD wins by 2+

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.14, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.3397): highest fidelity KXNHLTEAMTOTAL-26OCT10VANNJ-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10VANNJ-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2297): highest fidelity KXNHLGAME-26OCT10VANNJ-VAN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10VANNJ-VAN|yes (same contract)
- thesis NJD:SUPPRESSED (p 0.353): highest fidelity KXNHLSPREAD-26OCT10VANNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10VANNJ-VANDOCONNOR18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4431, phi -0.211)
- KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.2 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4303, phi -0.218)
- KXNHLSPREAD-26OCT10VANNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.8 pts; opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3369, phi -1.0)
- KXNHLSPREAD-26OCT10VANNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.6 pts; opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3369, phi -0.742)

portfolios: A EV +5.50 (adj +1.15) on $15.67, P(profit) 0.6671, adj growth 10.8 bp · B EV +5.68 (adj +2.07) on $20.45, P(profit) 0.6804, adj growth 19.6 bp · C EV +5.59 (adj +3.14) on $10.70, P(profit) 0.282, adj growth 27.6 bp · R EV +1.01 (adj +0.42) on $4.00, P(profit) 0.7012, adj growth 15.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10VANNJ-VAN|yes == KXNHLGAME-26OCT10VANNJ-NJ|no

## EDM @ SJS  ·  10000 joint draws  ·  424 bet sides mapped, 8 +EV candidates, 4 on card


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
| Alex Formenton: 1+ goals YES | 13 | 0.199 | 0.179 | +0.061 | +0.041 | $4.71 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 8 | 0.117 | 0.108 | +0.032 | +0.023 | $2.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 31 | 0.471 | 0.360 | +0.146 | +0.035 | $6.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
| Collin Graf: 1+ goals YES | 18 | 0.239 | 0.216 | +0.049 | +0.025 | $2.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT10EDMSJ-9|yes; why: higher confidence-adjusted growth (29.99 vs 0.55 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.837 vs 0.375); alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT10EDMSJ-9|yes; why: higher confidence-adjusted growth (14.41 vs 0.55 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.83 vs 0.375); alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.139); KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT10EDMSJ-EDM|no; why: higher confidence-adjusted growth (11.96 vs 1.90 bp); relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.139); KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: EDM offense succeeds (4+ goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10EDMSJ-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (8.94 vs 2.69 bp); relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:SUPPRESSED (p 0.3271): highest fidelity KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS (p 0.478): highest fidelity KXNHLGAME-26OCT10EDMSJ-SJ|yes [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:OFFENSE_4PLUS (p 0.439): highest fidelity KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3271, phi -0.198)
- KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3271, phi -0.151)
- KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.1 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4654, phi -0.319)
- KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3518, phi -0.225)

portfolios: A EV +4.57 (adj +1.71) on $15.67, P(profit) 0.7187, adj growth 16.3 bp · B EV +6.58 (adj +3.17) on $16.42, P(profit) 0.6566, adj growth 29.7 bp · C EV +5.59 (adj +1.74) on $14.93, P(profit) 0.5952, adj growth 15.6 bp · R EV +0.88 (adj +0.59) on $2.00, P(profit) 0.1985, adj growth 21.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10EDMSJ-SJ|yes == KXNHLGAME-26OCT10EDMSJ-EDM|no

## MIN @ FLA  ·  10000 joint draws  ·  400 bet sides mapped, 17 +EV candidates, 4 on card


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
| Yakov Trenin: 1+ goals YES | 9 | 0.141 | 0.120 | +0.045 | +0.024 | $2.17 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Sandis Vilmanis: 1+ goals YES | 10 | 0.151 | 0.128 | +0.044 | +0.022 | $2.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Anton Lundell: 1+ goals YES | 17 | 0.220 | 0.202 | +0.040 | +0.022 | $3.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Minnesota wins YES | 45 | 0.526 | 0.486 | +0.059 | +0.018 | $4.85 | FUNDED_RESEARCH | $2 | MIN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10MINFLA-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (14.09 vs 3.00 bp); relationships: KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGAME-26OCT10MINFLA-MIN|yes: MOSTLY_INDEPENDENT (phi 0.115); failure: MIN offense suppressed (<= 2 goals)
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes; why: higher confidence-adjusted growth (10.64 vs 7.31 bp); relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGAME-26OCT10MINFLA-MIN|yes: INTENTIONAL_DIVERSIFIER (phi -0.135); failure: FLA offense suppressed (<= 2 goals)
- **Anton Lundell: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT10MINFLA-7|yes; why: higher confidence-adjusted growth (7.31 vs 1.44 bp); despite a smaller raw edge (+0.040 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.916 vs 0.678); relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGAME-26OCT10MINFLA-MIN|yes: INTENTIONAL_DIVERSIFIER (phi -0.17); failure: FLA offense suppressed (<= 2 goals)
- **Minnesota wins YES** — thesis: MIN wins (incl. OT/SO); alternative: KXNHLGAME-26OCT10MINFLA-FLA|no; why: best adjusted growth among the thesis's expressions; relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.135); KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.17); failure: FLA wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis FLA:OFFENSE_4PLUS (p 0.381): highest fidelity KXNHLTOTAL-26OCT10MINFLA-7|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.4175): highest fidelity KXNHLTEAMTOTAL-26OCT10MINFLA-MIN2|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10MINFLA-MIN|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:WINS (p 0.5265): highest fidelity KXNHLGAME-26OCT10MINFLA-MIN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10MINFLA-MIN|yes (same contract)
- KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.359, phi -0.153)
- KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4023, phi -0.174)
- KXNHLGOAL-26OCT10MINFLA-FLAALUNDELL15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4023, phi -0.217)
- KXNHLGAME-26OCT10MINFLA-MIN|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS (p 0.4735, phi -1.0)

portfolios: A EV +2.29 (adj +0.46) on $15.67, P(profit) 0.5719, adj growth 4.1 bp · B EV +3.33 (adj +1.61) on $12.50, P(profit) 0.4305, adj growth 15.1 bp · C EV +2.55 (adj +1.14) on $23.13, P(profit) 0.4173, adj growth 10.2 bp · R EV +0.25 (adj +0.08) on $2.00, P(profit) 0.5265, adj growth 2.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10MINFLA-FLA|no == KXNHLGAME-26OCT10MINFLA-MIN|yes

## UTA @ BUF  ·  10000 joint draws  ·  412 bet sides mapped, 0 +EV candidates, 0 on card


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

## DET @ MTL  ·  10000 joint draws  ·  394 bet sides mapped, 2 +EV candidates, 1 on card


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
| Montreal wins by over 2.5 goals NO | 70 | 0.762 | 0.729 | +0.047 | +0.014 | $5.63 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Montreal wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT10DETMTL-MTL2|no; why: higher confidence-adjusted growth (2.05 vs 0.98 bp); wins across more scripts (relative breadth 0.995 vs 0.873); relationships: only recommended bet in this game; failure: MTL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4331): highest fidelity KXNHLSPREAD-26OCT10DETMTL-MTL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10DETMTL-MTL3|no (same contract)
- KXNHLSPREAD-26OCT10DETMTL-MTL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.3601, phi -0.745)

portfolios: A EV +0.86 (adj +0.23) on $12.53, P(profit) 0.6399, adj growth 2.0 bp · B EV +0.37 (adj +0.11) on $5.63, P(profit) 0.762, adj growth 1.0 bp · C EV +0.70 (adj +0.21) on $10.62, P(profit) 0.762, adj growth 1.9 bp · R EV +0.13 (adj +0.04) on $2.00, P(profit) 0.762, adj growth 1.4 bp

## NSH @ OTT  ·  10000 joint draws  ·  400 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NSH_win | p_overtime | goals | shots OTT/NSH | OTT/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.130 | 0.68 | 0.32 | 0.00 | 5.99 | 33.7/21.7 | 19.1/29.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.60 | 0.40 | 0.00 | 6.01 | 28.3/27.6 | 24.5/24.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.55 | 0.45 | 0.47 | 5.97 | 34.0/22.3 | 19.1/30.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.53 | 0.47 | 0.47 | 5.89 | 28.4/27.7 | 24.5/25.0 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.090 | 0.71 | 0.29 | 0.00 | 9.29 | 35.3/23.2 | 18.6/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.63 | 0.37 | 0.00 | 9.38 | 29.9/29.2 | 23.7/22.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Michael Amadio: 1+ goals YES | 16 | 0.216 | 0.198 | +0.047 | +0.029 | $3.45 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 23 | 0.278 | 0.262 | +0.035 | +0.020 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Claude Giroux: 1+ goals YES | 19 | 0.229 | 0.218 | +0.028 | +0.017 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10NSHOTT-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (12.73 vs 4.05 bp); relationships: KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT10NSHOTT-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: OTT offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT10NSHOTT-9|yes; why: higher confidence-adjusted growth (4.59 vs 0.36 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.941 vs 0.371); alternative not eligible: confidence-adjusted EV +0.0049 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT10NSHOTT-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: NSH offense suppressed (<= 2 goals)
- **Claude Giroux: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (12.73 vs 4.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis OTT:OFFENSE_4PLUS (p 0.4624): highest fidelity KXNHLGOAL-26OCT10NSHOTT-OTTCGIROUX28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.3267): highest fidelity KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes (same contract)
- KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3276, phi -0.214)
- KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4572, phi -0.26)
- KXNHLGOAL-26OCT10NSHOTT-OTTCGIROUX28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3276, phi -0.211)

portfolios: A EV +2.14 (adj +1.29) on $10.83, P(profit) 0.5656, adj growth 11.9 bp · B EV +1.66 (adj +1.00) on $8.40, P(profit) 0.5656, adj growth 9.4 bp · C EV +2.56 (adj +1.54) on $11.72, P(profit) 0.4366, adj growth 13.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ PIT  ·  10000 joint draws  ·  412 bet sides mapped, 9 +EV candidates, 4 on card


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
| Bryan Rust: 1+ goals YES | 26 | 0.337 | 0.314 | +0.063 | +0.040 | $4.44 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 76 | 0.850 | 0.802 | +0.077 | +0.030 | $7.83 | FUNDED_RESEARCH | $2 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Roope Hintz: 1+ assists NO | 56 | 0.716 | 0.611 | +0.139 | +0.034 | $7.45 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Pittsburgh wins by over 1.5 goals YES | 23 | 0.319 | 0.272 | +0.076 | +0.029 | $1.79 | FUNDED_RESEARCH | $1 | PIT:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT10DALPIT-DAL3|no; why: higher confidence-adjusted growth (17.76 vs 11.06 bp); despite a smaller raw edge (+0.063 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT10DALPIT-DAL3|no: MOSTLY_INDEPENDENT (phi 0.133); KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT10DALPIT-PIT2|yes: REINFORCING (phi 0.16); failure: PIT offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes; why: higher confidence-adjusted growth (11.06 vs 10.16 bp); wins across more scripts (relative breadth 1.012 vs 0.529); relationships: KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.133); KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: MOSTLY_INDEPENDENT (phi 0.129); KXNHLSPREAD-26OCT10DALPIT-PIT2|yes: REINFORCING (phi 0.287); failure: DAL wins by 2+
- **Roope Hintz: 1+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10DALPIT-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT10DALPIT-DAL3|no has the higher standalone adjusted growth (11.06 vs 10.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.129); they share one thesis budget; relationships: KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT10DALPIT-DAL3|no: MOSTLY_INDEPENDENT (phi 0.129); KXNHLSPREAD-26OCT10DALPIT-PIT2|yes: MOSTLY_INDEPENDENT (phi 0.134); failure: DAL offense succeeds (4+ goals)
- **Pittsburgh wins by over 1.5 goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT10DALPIT-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT10DALPIT-DAL3|no has the higher standalone adjusted growth (11.06 vs 10.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.287); they share one thesis budget; relationships: KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: REINFORCING (phi 0.16); KXNHLSPREAD-26OCT10DALPIT-DAL3|no: REINFORCING (phi 0.287); KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: MOSTLY_INDEPENDENT (phi 0.134); failure: DAL wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4338): highest fidelity KXNHLTEAMTOTAL-26OCT10DALPIT-PIT2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.5407): highest fidelity KXNHLSPREAD-26OCT10DALPIT-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10DALPIT-DAL3|no (same contract)
- thesis DAL:SUPPRESSED (p 0.4027): highest fidelity KXNHLSPREAD-26OCT10DALPIT-DAL3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3437, phi -0.26)
- KXNHLSPREAD-26OCT10DALPIT-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.2467, phi -0.735)
- KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.1 pts; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3763, phi -0.236)
- KXNHLSPREAD-26OCT10DALPIT-PIT2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.4593, phi -0.63)

portfolios: A EV +2.84 (adj +0.70) on $15.67, P(profit) 0.6898, adj growth 6.6 bp · B EV +4.16 (adj +1.61) on $21.51, P(profit) 0.7257, adj growth 15.4 bp · C EV +3.96 (adj +2.12) on $26.36, P(profit) 0.3368, adj growth 19.2 bp · R EV +0.98 (adj +0.49) on $5.00, P(profit) 0.5128, adj growth 18.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10DALPIT-PIT|yes == KXNHLGAME-26OCT10DALPIT-DAL|no

## CAR @ CHI  ·  10000 joint draws  ·  404 bet sides mapped, 10 +EV candidates, 4 on card


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
| Carolina wins by over 2.5 goals NO | 67 | 0.750 | 0.708 | +0.065 | +0.022 | $4.79 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Chicago over 1.5 goals scored YES | 71 | 0.781 | 0.743 | +0.057 | +0.019 | $5.85 | FUNDED_RESEARCH | $2 | CHI:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 67 | 0.717 | 0.700 | +0.031 | +0.015 | $4.38 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Andrei Svechnikov: 1+ goals NO | 65 | 0.695 | 0.679 | +0.029 | +0.013 | $3.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT10CARCHI-CAR2|no; why: higher confidence-adjusted growth (5.01 vs 2.36 bp); despite a smaller raw edge (+0.065 vs +0.088/contract); wins across more scripts (relative breadth 1.035 vs 0.917); relationships: KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes: REINFORCING (phi 0.399); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: REINFORCING (phi 0.15); KXNHLGOAL-26OCT10CARCHI-CARASVECHNIKOV37-1|no: MOSTLY_INDEPENDENT (phi 0.146); failure: CAR wins by 2+
- **Chicago over 1.5 goals scored YES** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes selected over broad KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.52 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT10CARCHI-CAR3|no: REINFORCING (phi 0.399); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT10CARCHI-CARASVECHNIKOV37-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: CHI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10CARCHI-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT10CARCHI-CAR3|no has the higher standalone adjusted growth (5.01 vs 2.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.150); they share one thesis budget; relationships: KXNHLSPREAD-26OCT10CARCHI-CAR3|no: REINFORCING (phi 0.15); KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT10CARCHI-CARASVECHNIKOV37-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: CAR offense succeeds (4+ goals)
- **Andrei Svechnikov: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10CARCHI-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT10CARCHI-CAR3|no has the higher standalone adjusted growth (5.01 vs 1.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.146); they share one thesis budget; relationships: KXNHLSPREAD-26OCT10CARCHI-CAR3|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis CHI:OFFENSE_4PLUS (p 0.3362): highest fidelity KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10CARCHI-CAR3|no — Broad expression KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes selected over broad KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.52 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CHI:WINS (p 0.409): highest fidelity KXNHLSPREAD-26OCT10CARCHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10CARCHI-CAR3|no (same contract)
- thesis CHI:WINS_BY_2PLUS (p 0.2073): highest fidelity KXNHLSPREAD-26OCT10CARCHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10CARCHI-CAR3|no (same contract)
- KXNHLSPREAD-26OCT10CARCHI-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3642, phi -0.762)
- KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis CHI:SUPPRESSED (p 0.4513, phi -0.583)
- KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4645, phi -0.226)
- KXNHLGOAL-26OCT10CARCHI-CARASVECHNIKOV37-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4645, phi -0.241)
- override: Broad expression KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes selected over broad KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.52 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.56 (adj +0.61) on $15.67, P(profit) 0.486, adj growth 4.7 bp · B EV +1.28 (adj +0.47) on $18.73, P(profit) 0.7093, adj growth 4.5 bp · C EV +2.75 (adj +0.97) on $15.03, P(profit) 0.753, adj growth 8.6 bp · R EV +0.44 (adj +0.16) on $6.00, P(profit) 0.4927, adj growth 5.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10CARCHI-CHI|yes == KXNHLGAME-26OCT10CARCHI-CAR|no

## CBJ @ STL  ·  10000 joint draws  ·  416 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_CBJ_win | p_overtime | goals | shots STL/CBJ | STL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.54 | 0.46 | 0.00 | 6.0 | 26.8/27.0 | 23.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.53 | 0.47 | 0.50 | 5.86 | 27.0/27.3 | 24.0/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.58 | 0.42 | 0.00 | 9.24 | 28.5/28.9 | 23.4/22.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.077 | 0.49 | 0.51 | 0.00 | 5.96 | 21.5/32.4 | 28.6/18.2 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.47 | 0.53 | 0.45 | 5.83 | 21.5/32.1 | 28.7/18.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.52 | 0.48 | 0.00 | 3.47 | 25.6/25.9 | 24.1/23.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Conor Garland: 1+ goals NO | 84 | 0.884 | 0.869 | +0.034 | +0.019 | $8.61 | FUNDED_RESEARCH | $3 | CBJ:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10CBJSTL-CBJAFANTILLI19-1|no; why: higher confidence-adjusted growth (6.62 vs 0.31 bp); despite a smaller raw edge (+0.034 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:SUPPRESSED (p 0.4307): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT10CBJSTL-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3463, phi -0.152)

portfolios: A EV +0.25 (adj +0.14) on $6.27, P(profit) 0.8836, adj growth 1.4 bp · B EV +0.35 (adj +0.20) on $8.61, P(profit) 0.8836, adj growth 1.9 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.12 (adj +0.07) on $3.00, P(profit) 0.8836, adj growth 2.7 bp

## TOR @ COL  ·  10000 joint draws  ·  424 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_TOR_win | p_overtime | goals | shots COL/TOR | COL/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.188 | 0.77 | 0.23 | 0.00 | 6.04 | 36.8/22.1 | 19.8/31.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.157 | 0.78 | 0.22 | 0.00 | 9.35 | 38.5/23.6 | 19.5/29.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.139 | 0.58 | 0.42 | 0.48 | 5.96 | 37.1/22.6 | 19.4/33.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.079 | 0.73 | 0.27 | 0.00 | 6.01 | 30.2/28.7 | 26.1/25.5 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.073 | 0.73 | 0.27 | 0.00 | 3.45 | 35.6/21.2 | 20.1/33.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.064 | 0.72 | 0.28 | 0.00 | 9.39 | 31.7/30.3 | 25.4/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zachary L'Heureux: 1+ goals YES | 11 | 0.167 | 0.144 | +0.050 | +0.027 | $2.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Martin Necas: 1+ goals NO | 62 | 0.674 | 0.657 | +0.037 | +0.020 | $5.94 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Zachary L'Heureux: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10TORCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (15.01 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0001 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: COL offense suppressed (<= 2 goals)
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10TORCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (3.89 vs 0.52 bp); despite a smaller raw edge (+0.037 vs +0.057/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0076 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.19, COL shot control · high event (8+) · decided (2+) 0.16, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.14.
- thesis COL:SUPPRESSED (p 0.2483): highest fidelity KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no (same contract)
- thesis COL:OFFENSE_4PLUS (p 0.5511): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2483, phi -0.166)
- KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5511, phi -0.225)

portfolios: A EV +2.26 (adj +1.22) on $10.69, P(profit) 0.1667, adj growth 11.1 bp · B EV +1.54 (adj +0.83) on $8.73, P(profit) 0.7257, adj growth 7.8 bp · C EV +0.68 (adj +0.37) on $11.56, P(profit) 0.674, adj growth 3.3 bp · R EV +0.12 (adj +0.06) on $2.00, P(profit) 0.674, adj growth 2.4 bp

## TBL @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 3 on card


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
| New York I wins by over 1.5 goals YES | 21 | 0.287 | 0.246 | +0.065 | +0.024 | $1.68 | FUNDED_RESEARCH | $1 | NYI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I wins YES | 38 | 0.514 | 0.424 | +0.118 | +0.027 | $1.28 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 76 | 0.840 | 0.795 | +0.068 | +0.022 | $8.61 | FUNDED_RESEARCH | $3 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
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

portfolios: A EV +2.73 (adj +0.65) on $15.67, P(profit) 0.5144, adj growth 5.9 bp · B EV +1.63 (adj +0.52) on $11.57, P(profit) 0.5144, adj growth 5.0 bp · C EV +1.66 (adj +0.62) on $5.64, P(profit) 0.2868, adj growth 5.5 bp · R EV +0.85 (adj +0.27) on $5.00, P(profit) 0.5144, adj growth 9.5 bp
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
