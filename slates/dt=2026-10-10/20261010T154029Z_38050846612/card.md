# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-10T15:40:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.94 | +30.56 | +8.48 | +29.95 | 0.865 | -4.57 | -13.53 | 81.00 |
| B thesis-diversified (joint) ← optimiser card | 147.68 | +29.16 | +14.34 | +28.43 | 0.822 | -9.68 | -19.25 | 138.59 |
| C best expression per thesis | 149.05 | +26.54 | +11.60 | +25.45 | 0.796 | -12.73 | -22.92 | 111.25 |
| R FUNDED research stakes | 17.00 | +2.07 | +1.21 | +1.71 | 0.639 | -4.17 | -5.81 | 0.00 |

## PHI @ BOS  ·  10000 joint draws  ·  428 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_PHI_win | p_overtime | goals | shots BOS/PHI | BOS/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 5.94 | 26.8/26.7 | 23.5/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.49 | 5.88 | 27.3/27.2 | 23.8/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.60 | 0.40 | 0.00 | 9.19 | 28.3/28.0 | 22.5/21.7 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.077 | 0.65 | 0.35 | 0.00 | 5.95 | 31.8/21.2 | 18.4/27.7 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.57 | 0.43 | 0.48 | 5.79 | 31.9/21.3 | 18.3/28.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.56 | 0.44 | 0.00 | 3.5 | 25.7/25.6 | 24.0/23.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Couturier: 1+ goals YES | 13 | 0.187 | 0.171 | +0.049 | +0.033 | $2.31 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Frederic Brunet: 1+ assists NO | 64 | 0.811 | 0.690 | +0.155 | +0.034 | $5.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Travis Sanheim: 1+ goals YES | 7 | 0.100 | 0.091 | +0.025 | +0.017 | $1.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Elias Lindholm: 1+ goals YES | 21 | 0.252 | 0.240 | +0.030 | +0.018 | $1.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10PHIBOS-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (19.91 vs 1.90 bp); relationships: KXNHLAST-26OCT10PHIBOS-BOSFBRUNET42-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10PHIBOS-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT10PHIBOS-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: PHI offense suppressed (<= 2 goals)
- **Frederic Brunet: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (11.28 vs 5.07 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10PHIBOS-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT10PHIBOS-BOSELINDHOLM28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.089); failure: BOS offense succeeds (4+ goals)
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (19.91 vs 8.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT10PHIBOS-BOSFBRUNET42-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT10PHIBOS-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense suppressed (<= 2 goals)
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10PHIBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (4.23 vs 0.43 bp); alternative not eligible: confidence-adjusted EV +0.0063 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT10PHIBOS-BOSFBRUNET42-1|no: INTENTIONAL_DIVERSIFIER (phi -0.089); KXNHLGOAL-26OCT10PHIBOS-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis PHI:OFFENSE_4PLUS (p 0.3122): highest fidelity KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.3825): highest fidelity KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.3932): highest fidelity KXNHLGOAL-26OCT10PHIBOS-BOSELINDHOLM28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10PHIBOS-BOSELINDHOLM28-1|yes (same contract)
- KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4679, phi -0.223)
- KXNHLAST-26OCT10PHIBOS-BOSFBRUNET42-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.6 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3932, phi -0.182)
- KXNHLGOAL-26OCT10PHIBOS-PHITSANHEIM6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4679, phi -0.167)
- KXNHLGOAL-26OCT10PHIBOS-BOSELINDHOLM28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3825, phi -0.23)

portfolios: A EV +2.63 (adj +0.82) on $10.71, P(profit) 0.6961, adj growth 8.0 bp · B EV +2.64 (adj +1.20) on $10.30, P(profit) 0.4038, adj growth 11.6 bp · C EV +1.87 (adj +1.11) on $16.56, P(profit) 0.3464, adj growth 10.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ NJD  ·  10000 joint draws  ·  416 bet sides mapped, 35 +EV candidates, 3 on card


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
| Nico Hischier: 1+ goals NO | 66 | 0.737 | 0.715 | +0.061 | +0.039 | $4.13 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 58 | 0.653 | 0.632 | +0.056 | +0.035 | $3.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 2.5 goals NO | 64 | 0.785 | 0.687 | +0.129 | +0.031 | $4.53 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nico Hischier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: Player prop expression KXNHLGOAL-26OCT10VANNJ-NJNHISCHIER13-1|no selected over player prop KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.88 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT10VANNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: REINFORCING (phi 0.16); failure: NJD offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (19.19 vs 11.50 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.120); relationships: KXNHLGOAL-26OCT10VANNJ-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: REINFORCING (phi 0.151); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (19.19 vs 9.53 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.206); relationships: KXNHLGOAL-26OCT10VANNJ-NJNHISCHIER13-1|no: REINFORCING (phi 0.16); KXNHLGOAL-26OCT10VANNJ-NJJHUGHES86-1|no: REINFORCING (phi 0.151); failure: NJD wins by 2+

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.14, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.2281): highest fidelity KXNHLGAME-26OCT10VANNJ-VAN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10VANNJ-VAN|yes (same contract)
- thesis NJD:SUPPRESSED (p 0.3532): highest fidelity KXNHLSPREAD-26OCT10VANNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no — Player prop expression KXNHLGOAL-26OCT10VANNJ-NJNHISCHIER13-1|no selected over player prop KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.88 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VAN:OFFENSE_4PLUS (p 0.3408): highest fidelity KXNHLTEAMTOTAL-26OCT10VANNJ-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10VANNJ-VAN|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10VANNJ-NJNHISCHIER13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4263, phi -0.24)
- KXNHLGOAL-26OCT10VANNJ-NJJHUGHES86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4263, phi -0.25)
- KXNHLSPREAD-26OCT10VANNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.0 pts; opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3342, phi -0.739)
- override: Player prop expression KXNHLGOAL-26OCT10VANNJ-NJNHISCHIER13-1|no selected over player prop KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.88 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.38 (adj +0.48) on $10.71, P(profit) 0.7336, adj growth 4.6 bp · B EV +1.62 (adj +0.68) on $12.49, P(profit) 0.7963, adj growth 6.7 bp · C EV +1.27 (adj +0.53) on $1.59, P(profit) 0.1342, adj growth 5.1 bp · R EV +0.57 (adj +0.21) on $4.00, P(profit) 0.6071, adj growth 8.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10VANNJ-NJ|no == KXNHLGAME-26OCT10VANNJ-VAN|yes

## EDM @ SJS  ·  10000 joint draws  ·  424 bet sides mapped, 18 +EV candidates, 4 on card


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
| Alex Formenton: 1+ goals YES | 13 | 0.207 | 0.186 | +0.069 | +0.048 | $3.39 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Collin Graf: 1+ goals YES | 18 | 0.237 | 0.217 | +0.046 | +0.027 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 8 | 0.113 | 0.102 | +0.028 | +0.017 | $1.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 33 | 0.473 | 0.374 | +0.128 | +0.028 | $3.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10EDMSJ-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (41.73 vs 6.06 bp); despite a smaller raw edge (+0.069 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.071); failure: EDM offense suppressed (<= 2 goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10EDMSJ-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (10.31 vs 6.77 bp); relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: SJS offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (41.73 vs 8.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.135); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (7.63 vs 6.27 bp); relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.071); KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.135); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4672): highest fidelity KXNHLAST-26OCT10EDMSJ-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:OFFENSE_4PLUS (p 0.4308): highest fidelity KXNHLGAME-26OCT10EDMSJ-SJ|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3236): highest fidelity KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3236, phi -0.199)
- KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.348, phi -0.217)
- KXNHLGOAL-26OCT10EDMSJ-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3236, phi -0.159)
- KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.3 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4672, phi -0.305)

portfolios: A EV +3.06 (adj +0.49) on $10.71, P(profit) 0.6333, adj growth 4.6 bp · B EV +3.81 (adj +2.00) on $9.95, P(profit) 0.4636, adj growth 19.2 bp · C EV +4.58 (adj +2.29) on $16.56, P(profit) 0.6, adj growth 21.9 bp · R EV +0.50 (adj +0.35) on $1.00, P(profit) 0.2068, adj growth 13.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10EDMSJ-SJ|yes == KXNHLGAME-26OCT10EDMSJ-EDM|no

## MIN @ FLA  ·  10000 joint draws  ·  402 bet sides mapped, 21 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_MIN_win | p_overtime | goals | shots FLA/MIN | FLA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.45 | 0.55 | 0.00 | 6.02 | 28.0/28.0 | 24.0/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.48 | 0.52 | 0.46 | 5.93 | 28.1/28.0 | 24.6/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.46 | 0.54 | 0.00 | 9.35 | 29.8/29.7 | 23.3/23.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.077 | 0.50 | 0.50 | 0.00 | 6.0 | 33.5/22.7 | 19.2/29.6 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.54 | 0.46 | 0.50 | 5.96 | 33.3/22.5 | 19.4/29.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.057 | 0.37 | 0.63 | 0.00 | 6.02 | 22.3/32.8 | 28.6/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Michael McCarron: 1+ goals YES | 8 | 0.127 | 0.114 | +0.042 | +0.029 | $1.81 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 9 | 0.137 | 0.125 | +0.041 | +0.029 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Sandis Vilmanis: 1+ goals YES | 10 | 0.150 | 0.135 | +0.044 | +0.029 | $1.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 18 | 0.242 | 0.225 | +0.051 | +0.035 | $2.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Michael McCarron: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (22.79 vs 16.81 bp); despite a smaller raw edge (+0.042 vs +0.051/contract); relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: MIN offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (21.33 vs 16.81 bp); despite a smaller raw edge (+0.041 vs +0.051/contract); relationships: KXNHLGOAL-26OCT10MINFLA-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: MIN offense suppressed (<= 2 goals)
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT10MINFLA-7|yes; why: higher confidence-adjusted growth (18.36 vs 2.13 bp); despite a smaller raw edge (+0.044 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.916 vs 0.676); relationships: KXNHLGOAL-26OCT10MINFLA-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: FLA offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10MINFLA-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (16.81 vs 8.75 bp); despite a smaller raw edge (+0.051 vs +0.110/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10MINFLA-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4253): highest fidelity KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.4036): highest fidelity KXNHLSPREAD-26OCT10MINFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10MINFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:WINS (p 0.5314): highest fidelity KXNHLGAME-26OCT10MINFLA-MIN|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10MINFLA-MINMMCCARRON47-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3525, phi -0.169)
- KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3525, phi -0.156)
- KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4036, phi -0.182)
- KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3525, phi -0.212)

portfolios: A EV +2.63 (adj +0.58) on $10.71, P(profit) 0.5615, adj growth 5.4 bp · B EV +3.17 (adj +2.17) on $8.14, P(profit) 0.5128, adj growth 20.9 bp · C EV +1.76 (adj +1.00) on $11.81, P(profit) 0.4719, adj growth 9.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10MINFLA-MIN|yes == KXNHLGAME-26OCT10MINFLA-FLA|no

## UTA @ BUF  ·  10000 joint draws  ·  414 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_UTA_win | p_overtime | goals | shots BUF/UTA | BUF/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.52 | 0.48 | 0.00 | 6.04 | 27.3/27.2 | 23.8/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.48 | 0.52 | 0.45 | 5.97 | 27.6/27.4 | 24.1/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.52 | 0.48 | 0.00 | 9.35 | 29.0/28.7 | 22.6/23.1 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.076 | 0.57 | 0.43 | 0.00 | 6.01 | 32.4/21.4 | 18.4/28.2 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.54 | 0.46 | 0.45 | 5.94 | 32.7/22.0 | 18.8/29.2 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.058 | 0.59 | 0.41 | 0.00 | 9.38 | 34.2/23.1 | 17.8/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vincent Trocheck: 1+ assists NO | 68 | 0.816 | 0.725 | +0.121 | +0.029 | $5.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ goals NO | 61 | 0.666 | 0.651 | +0.040 | +0.024 | $4.79 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 12 | 0.152 | 0.141 | +0.024 | +0.014 | $1.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10UTABUF-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (8.90 vs 0.28 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10UTABUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT10UTABUF-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: UTA offense succeeds (4+ goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10UTABUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (5.51 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0008 below the 0.010/contract floor; relationships: KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT10UTABUF-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: BUF offense succeeds (4+ goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10UTABUF-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (3.79 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0010 below the 0.010/contract floor; relationships: KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT10UTABUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.4173): highest fidelity KXNHLAST-26OCT10UTABUF-BUFOPOWER25-2|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT10UTABUF-BUFOPOWER25-2|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.3655): highest fidelity KXNHLGOAL-26OCT10UTABUF-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10UTABUF-BUFTTHOMPSON72-1|no (same contract)
- thesis UTA:SUPPRESSED (p 0.3807): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.1 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3915, phi -0.206)
- KXNHLGOAL-26OCT10UTABUF-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4173, phi -0.254)
- KXNHLGOAL-26OCT10UTABUF-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3807, phi -0.176)

portfolios: A EV +2.02 (adj +0.83) on $10.71, P(profit) 0.6547, adj growth 7.9 bp · B EV +1.42 (adj +0.52) on $11.10, P(profit) 0.6052, adj growth 5.0 bp · C EV +0.38 (adj +0.23) on $5.95, P(profit) 0.6662, adj growth 2.2 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.6662, adj growth 2.9 bp

## DET @ MTL  ·  10000 joint draws  ·  392 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_DET_win | p_overtime | goals | shots MTL/DET | MTL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.69 | 0.31 | 0.00 | 6.01 | 27.0/27.3 | 24.6/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.55 | 0.45 | 0.47 | 5.92 | 27.2/27.5 | 24.3/23.7 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.097 | 0.62 | 0.38 | 0.00 | 6.01 | 22.0/33.1 | 30.1/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.68 | 0.32 | 0.00 | 9.36 | 29.0/29.2 | 24.0/21.8 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.50 | 0.50 | 0.45 | 5.92 | 22.0/33.2 | 29.9/18.9 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.062 | 0.59 | 0.41 | 0.00 | 9.19 | 23.3/34.5 | 28.8/17.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jacob Fowler: 23+ saves YES | 52 | 0.661 | 0.569 | +0.123 | +0.032 | $4.41 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | DET:SHOT_CONTROL | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Nick Suzuki: 2+ assists NO | 78 | 0.838 | 0.806 | +0.046 | +0.014 | $4.59 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Chris Kreider: 1+ assists NO | 69 | 0.768 | 0.719 | +0.063 | +0.014 | $3.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Jacob Fowler: 23+ saves YES** — thesis: DET controls shots (share >= 0.55); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLAST-26OCT10DETMTL-MTLNSUZUKI14-2|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT10DETMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: MTL net faces light volume (<= 25 shots; DET suppressed)
- **Nick Suzuki: 2+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10DETMTL-MTL3|no; why: higher confidence-adjusted growth (2.79 vs 0.16 bp); alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLSAVE-26OCT10DETMTL-MTLJFOWLER32-23|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT10DETMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.056); failure: MTL offense succeeds (4+ goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10DETMTL-MTLNSUZUKI14-2|no; why: second expression of the same thesis: KXNHLAST-26OCT10DETMTL-MTLNSUZUKI14-2|no has the higher standalone adjusted growth (2.79 vs 2.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.056); they share one thesis budget; relationships: KXNHLSAVE-26OCT10DETMTL-MTLJFOWLER32-23|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT10DETMTL-MTLNSUZUKI14-2|no: MOSTLY_INDEPENDENT (phi 0.056); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DET:SHOT_CONTROL (p 0.3566): highest fidelity KXNHLSAVE-26OCT10DETMTL-MTLJFOWLER32-23|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT10DETMTL-MTLJFOWLER32-23|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3096): highest fidelity KXNHLAST-26OCT10DETMTL-MTLNSUZUKI14-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT10DETMTL-MTLNSUZUKI14-2|no (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.481): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLSAVE-26OCT10DETMTL-MTLJFOWLER32-23|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.1 pts; fragile player expression; opposing: failure thesis MTL:NET_LOW_VOLUME (p 0.3287, phi -0.769)
- KXNHLAST-26OCT10DETMTL-MTLNSUZUKI14-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.481, phi -0.283)
- KXNHLAST-26OCT10DETMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.481, phi -0.193)

portfolios: A EV +1.33 (adj +0.38) on $10.71, P(profit) 0.5242, adj growth 3.7 bp · B EV +1.58 (adj +0.41) on $12.36, P(profit) 0.6303, adj growth 4.0 bp · C EV +1.78 (adj +0.48) on $12.73, P(profit) 0.5511, adj growth 4.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ OTT  ·  10000 joint draws  ·  402 bet sides mapped, 7 +EV candidates, 4 on card


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
| Ryan O'Reilly: 1+ goals YES | 22 | 0.282 | 0.264 | +0.050 | +0.032 | $2.55 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Stephen Halliday: 1+ goals YES | 11 | 0.159 | 0.141 | +0.042 | +0.024 | $1.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 16 | 0.213 | 0.197 | +0.043 | +0.028 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Warren Foegele: 1+ goals YES | 14 | 0.193 | 0.173 | +0.044 | +0.025 | $1.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10NSHOTT-NSHJMARCHESSAULT81-1|yes; why: higher confidence-adjusted growth (12.42 vs 0.74 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10NSHOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT10NSHOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NSH offense suppressed (<= 2 goals)
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (11.83 vs 11.74 bp); despite a smaller raw edge (+0.042 vs +0.043/contract); relationships: KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT10NSHOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.024); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10NSHOTT-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (11.74 vs 1.98 bp); despite a smaller raw edge (+0.043 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT10NSHOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT10NSHOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: OTT offense suppressed (<= 2 goals)
- **Warren Foegele: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (11.74 vs 10.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10NSHOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NSH:OFFENSE_4PLUS (p 0.3268): highest fidelity KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4604): highest fidelity KXNHLAST-26OCT10NSHOTT-OTTCGIROUX28-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4537, phi -0.257)
- KXNHLGOAL-26OCT10NSHOTT-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3217, phi -0.155)
- KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3217, phi -0.191)
- KXNHLGOAL-26OCT10NSHOTT-OTTWFOEGELE37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3217, phi -0.164)

portfolios: A EV +2.47 (adj +1.28) on $10.71, P(profit) 0.696, adj growth 12.1 bp · B EV +2.17 (adj +1.30) on $7.93, P(profit) 0.6155, adj growth 12.5 bp · C EV +1.35 (adj +0.87) on $5.80, P(profit) 0.434, adj growth 8.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ PIT  ·  10000 joint draws  ·  412 bet sides mapped, 20 +EV candidates, 3 on card


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
| Connor Dewar: 1+ goals YES | 10 | 0.151 | 0.138 | +0.045 | +0.032 | $2.13 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Bryan Rust: 1+ goals YES | 26 | 0.323 | 0.306 | +0.049 | +0.032 | $2.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Roope Hintz: 1+ assists NO | 55 | 0.709 | 0.602 | +0.141 | +0.035 | $5.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGAME-26OCT10DALPIT-PIT|yes; why: higher confidence-adjusted growth (23.01 vs 7.14 bp); despite a smaller raw edge (+0.045 vs +0.119/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: MOSTLY_INDEPENDENT (phi 0.024); failure: PIT offense suppressed (<= 2 goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (23.01 vs 11.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: PIT offense suppressed (<= 2 goals)
- **Roope Hintz: 1+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT10DALPIT-PIT|yes; why: higher confidence-adjusted growth (10.88 vs 7.14 bp); relationships: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis PIT:WINS_BY_2PLUS (p 0.2826): highest fidelity KXNHLGAME-26OCT10DALPIT-PIT|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.4065): highest fidelity KXNHLTEAMTOTAL-26OCT10DALPIT-PIT4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.3833): highest fidelity KXNHLSPREAD-26OCT10DALPIT-DAL3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3792, phi -0.196)
- KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3792, phi -0.248)
- KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.4 pts; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.398, phi -0.249)

portfolios: A EV +2.20 (adj +0.47) on $10.71, P(profit) 0.6327, adj growth 4.5 bp · B EV +2.73 (adj +1.30) on $10.27, P(profit) 0.4273, adj growth 12.6 bp · C EV +3.28 (adj +1.30) on $11.00, P(profit) 0.7486, adj growth 12.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10DALPIT-DAL|no == KXNHLGAME-26OCT10DALPIT-PIT|yes

## CAR @ CHI  ·  10000 joint draws  ·  408 bet sides mapped, 19 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_CAR_win | p_overtime | goals | shots CHI/CAR | CHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.171 | 0.34 | 0.66 | 0.00 | 6.01 | 20.4/33.5 | 28.9/17.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.139 | 0.45 | 0.55 | 0.46 | 5.9 | 20.5/33.4 | 30.1/17.4 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.120 | 0.34 | 0.66 | 0.00 | 9.36 | 22.2/35.2 | 27.5/17.4 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.079 | 0.38 | 0.62 | 0.00 | 3.46 | 19.0/32.1 | 29.8/17.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.079 | 0.39 | 0.61 | 0.00 | 6.04 | 26.1/27.1 | 23.1/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.47 | 0.53 | 0.47 | 5.91 | 26.3/27.4 | 24.0/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 26 | 0.326 | 0.308 | +0.052 | +0.035 | $3.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 65 | 0.721 | 0.702 | +0.055 | +0.036 | $5.30 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 15 | 0.199 | 0.184 | +0.040 | +0.025 | $1.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Ryan Donato: 1+ goals YES | 14 | 0.177 | 0.165 | +0.029 | +0.017 | $1.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes; why: higher confidence-adjusted growth (13.20 vs 10.16 bp); relationships: KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT10CARCHI-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: CHI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10CARCHI-CARSAHO20-1|no; why: higher confidence-adjusted growth (12.93 vs 6.91 bp); despite a smaller raw edge (+0.055 vs +0.122/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT10CARCHI-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: CAR offense succeeds (4+ goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (13.20 vs 10.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT10CARCHI-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: CHI offense suppressed (<= 2 goals)
- **Ryan Donato: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (13.20 vs 4.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis CHI:OFFENSE_4PLUS (p 0.3328): highest fidelity KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.3257): highest fidelity KXNHLSPREAD-26OCT10CARCHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.4121): highest fidelity KXNHLSPREAD-26OCT10CARCHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4482, phi -0.268)
- KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4595, phi -0.215)
- KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4482, phi -0.234)
- KXNHLGOAL-26OCT10CARCHI-CHIRDONATO8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4482, phi -0.207)

portfolios: A EV +1.98 (adj +0.39) on $10.71, P(profit) 0.554, adj growth 3.8 bp · B EV +1.71 (adj +1.10) on $11.37, P(profit) 0.4663, adj growth 10.6 bp · C EV +1.89 (adj +1.04) on $16.44, P(profit) 0.6656, adj growth 10.0 bp · R EV +0.17 (adj +0.11) on $2.00, P(profit) 0.7211, adj growth 4.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10CARCHI-CHI|yes == KXNHLGAME-26OCT10CARCHI-CAR|no

## CBJ @ STL  ·  10000 joint draws  ·  424 bet sides mapped, 3 +EV candidates, 3 on card


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
| Conor Garland: 1+ goals NO | 84 | 0.890 | 0.876 | +0.040 | +0.026 | $4.14 | FUNDED_RESEARCH | $2 | CBJ:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Matthew Knies: 1+ assists NO | 65 | 0.737 | 0.691 | +0.071 | +0.025 | $3.81 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Adam Jiricek: 1+ assists NO | 68 | 0.771 | 0.705 | +0.076 | +0.010 | $2.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (12.26 vs 6.31 bp); despite a smaller raw edge (+0.040 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no: MOSTLY_INDEPENDENT (phi 0.038); KXNHLAST-26OCT10CBJSTL-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CBJ offense succeeds (4+ goals)
- **Matthew Knies: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10CBJSTL-CBJCGARLAND83-1|no; why: higher confidence-adjusted growth (6.31 vs 0.99 bp); alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10CBJSTL-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.038); KXNHLAST-26OCT10CBJSTL-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: CBJ offense succeeds (4+ goals)
- **Adam Jiricek: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT10CBJSTL-STLAJIRICEK36-1|no; why: higher confidence-adjusted growth (1.07 vs 0.00 bp); despite a smaller raw edge (+0.076 vs +0.087/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT10CBJSTL-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CBJ:SUPPRESSED (p 0.4684): highest fidelity KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no (same contract)
- thesis STL:SUPPRESSED (p 0.3719): highest fidelity KXNHLAST-26OCT10CBJSTL-STLAJIRICEK36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10CBJSTL-STLAJIRICEK36-1|no (same contract)
- KXNHLGOAL-26OCT10CBJSTL-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3118, phi -0.138)
- KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3118, phi -0.236)
- KXNHLAST-26OCT10CBJSTL-STLAJIRICEK36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.1 pts; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4086, phi -0.22)

portfolios: A EV +0.94 (adj +0.30) on $10.71, P(profit) 0.5118, adj growth 2.9 bp · B EV +0.88 (adj +0.31) on $10.46, P(profit) 0.6612, adj growth 3.1 bp · C EV +1.05 (adj +0.30) on $9.74, P(profit) 0.7374, adj growth 2.9 bp · R EV +0.09 (adj +0.06) on $2.00, P(profit) 0.8896, adj growth 2.5 bp

## TOR @ COL  ·  10000 joint draws  ·  430 bet sides mapped, 5 +EV candidates, 4 on card


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
| Zachary L'Heureux: 1+ goals YES | 12 | 0.165 | 0.150 | +0.038 | +0.023 | $1.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:WINS_BY_2PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 76 | 0.806 | 0.792 | +0.033 | +0.019 | $5.00 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Kirill Marchenko: 1+ assists NO | 62 | 0.700 | 0.655 | +0.063 | +0.018 | $3.37 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Martin Necas: 1+ goals NO | 62 | 0.668 | 0.654 | +0.031 | +0.018 | $2.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Zachary L'Heureux: 1+ goals YES** — thesis: COL wins by 2+; alternative: KXNHLPTS-26OCT10TORCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (10.14 vs 0.00 bp); despite a smaller raw edge (+0.038 vs +0.049/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: COL offense suppressed (<= 2 goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no; why: higher confidence-adjusted growth (4.68 vs 3.08 bp); relationships: KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: COL offense succeeds (4+ goals)
- **Kirill Marchenko: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10TORCOL-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (3.18 vs 0.05 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0022 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: TOR offense succeeds (4+ goals)
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10TORCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (3.08 vs 1.45 bp); despite a smaller raw edge (+0.031 vs +0.085/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.19, COL shot control · high event (8+) · decided (2+) 0.16, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.14.
- thesis TOR:SUPPRESSED (p 0.4923): highest fidelity KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no (same contract)
- thesis COL:SUPPRESSED (p 0.2507): highest fidelity KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no (same contract)
- thesis COL:WINS_BY_2PLUS (p 0.4642): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2507, phi -0.151)
- KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5575, phi -0.173)
- KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2851, phi -0.251)
- KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5575, phi -0.225)

portfolios: A EV +1.57 (adj +0.55) on $10.71, P(profit) 0.5546, adj growth 5.3 bp · B EV +1.15 (adj +0.58) on $12.86, P(profit) 0.474, adj growth 5.6 bp · C EV +0.64 (adj +0.24) on $8.53, P(profit) 0.469, adj growth 2.3 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.8061, adj growth 1.9 bp

## TBL @ NYI  ·  10000 joint draws  ·  390 bet sides mapped, 24 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_TBL_win | p_overtime | goals | shots NYI/TBL | NYI/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.134 | 0.54 | 0.46 | 0.00 | 6.01 | 26.7/26.9 | 23.7/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.48 | 5.9 | 26.8/27.1 | 23.9/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.59 | 0.41 | 0.00 | 9.24 | 28.6/28.8 | 23.3/22.0 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.075 | 0.47 | 0.53 | 0.00 | 5.97 | 21.6/31.9 | 27.9/18.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.48 | 0.52 | 0.47 | 5.88 | 21.4/32.3 | 28.9/18.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.49 | 0.51 | 0.48 | 2.79 | 25.3/25.4 | 24.0/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 19 | 0.263 | 0.243 | +0.062 | +0.042 | $3.24 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| John Carlson: 1+ assists NO | 52 | 0.726 | 0.582 | +0.188 | +0.045 | $5.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Ondrej Palat: 1+ goals YES | 10 | 0.145 | 0.134 | +0.038 | +0.027 | $1.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 14 | 0.174 | 0.165 | +0.025 | +0.017 | $1.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT10TBNYI-NYI|yes; why: higher confidence-adjusted growth (24.09 vs 7.86 bp); despite a smaller raw edge (+0.062 vs +0.124/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10TBNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT10TBNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.027); failure: NYI offense suppressed (<= 2 goals)
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT10TBNYI-NYI|yes; why: higher confidence-adjusted growth (17.73 vs 7.86 bp); relationships: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10TBNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT10TBNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: TBL offense succeeds (4+ goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (24.09 vs 16.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT10TBNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NYI offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes; why: Player prop expression KXNHLGOAL-26OCT10TBNYI-NYIJPAGEAU44-1|yes selected over player prop KXNHLAST-26OCT10TBNYI-NYIBSCHENN10-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.28 vs 0.51 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT10TBNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3668): highest fidelity KXNHLTEAMTOTAL-26OCT10TBNYI-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes — Player prop expression KXNHLGOAL-26OCT10TBNYI-NYIJPAGEAU44-1|yes selected over player prop KXNHLAST-26OCT10TBNYI-NYIBSCHENN10-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.28 vs 0.51 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis TBL:SUPPRESSED (p 0.4441): highest fidelity KXNHLSPREAD-26OCT10TBNYI-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.5203): highest fidelity KXNHLGAME-26OCT10TBNYI-NYI|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10TBNYI-NYI|yes (same contract)
- KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4233, phi -0.248)
- KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 22.1 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3314, phi -0.243)
- KXNHLGOAL-26OCT10TBNYI-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4233, phi -0.18)
- KXNHLGOAL-26OCT10TBNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4233, phi -0.212)
- override: Player prop expression KXNHLGOAL-26OCT10TBNYI-NYIJPAGEAU44-1|yes selected over player prop KXNHLAST-26OCT10TBNYI-NYIBSCHENN10-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.28 vs 0.51 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.22 (adj +0.65) on $10.71, P(profit) 0.7835, adj growth 6.2 bp · B EV +3.72 (adj +1.73) on $11.57, P(profit) 0.448, adj growth 16.7 bp · C EV +4.38 (adj +1.42) on $16.56, P(profit) 0.7081, adj growth 13.8 bp · R EV +0.31 (adj +0.21) on $1.00, P(profit) 0.2626, adj growth 8.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10TBNYI-TB|no == KXNHLGAME-26OCT10TBNYI-NYI|yes

## ANA @ CGY  ·  10000 joint draws  ·  424 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_ANA_win | p_overtime | goals | shots CGY/ANA | CGY/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.51 | 0.49 | 0.00 | 6.02 | 28.6/29.1 | 25.6/25.0 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.105 | 0.47 | 0.53 | 0.00 | 6.0 | 22.8/34.5 | 30.6/19.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.48 | 0.52 | 0.50 | 6.02 | 28.7/29.1 | 25.7/25.3 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.49 | 0.51 | 0.46 | 5.95 | 23.0/34.7 | 31.3/19.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.52 | 0.48 | 0.00 | 9.42 | 30.2/30.9 | 24.8/23.6 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.074 | 0.44 | 0.56 | 0.00 | 9.37 | 24.2/36.2 | 29.0/18.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Judd Caulfield: 1+ goals YES | 9 | 0.135 | 0.117 | +0.040 | +0.021 | $1.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Leo Carlsson: 1+ assists NO | 52 | 0.609 | 0.559 | +0.071 | +0.022 | $2.83 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | ANA:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Cutter Gauthier: 1+ goals NO | 59 | 0.640 | 0.626 | +0.033 | +0.019 | $2.67 | FUNDED_RESEARCH | $1 | ANA:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (10.63 vs 0.00 bp); despite a smaller raw edge (+0.040 vs +0.050/contract); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi -0.021); failure: ANA offense suppressed (<= 2 goals)
- **Leo Carlsson: 1+ assists NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no; why: higher confidence-adjusted growth (4.21 vs 3.35 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no: REINFORCING (phi 0.209); failure: ANA offense succeeds (4+ goals)
- **Cutter Gauthier: 1+ goals NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-1|no; why: second expression of the same thesis: KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-1|no has the higher standalone adjusted growth (4.21 vs 3.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.209); they share one thesis budget; relationships: KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-1|no: REINFORCING (phi 0.209); failure: ANA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:SUPPRESSED (p 0.3653): highest fidelity KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:OFFENSE_4PLUS (p 0.4182): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3653, phi -0.165)
- KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.4182, phi -0.272)
- KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.4182, phi -0.284)

portfolios: A EV +1.74 (adj +0.80) on $10.71, P(profit) 0.5196, adj growth 7.5 bp · B EV +1.07 (adj +0.49) on $6.82, P(profit) 0.5196, adj growth 4.7 bp · C EV +0.53 (adj +0.16) on $4.02, P(profit) 0.6087, adj growth 1.6 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.6397, adj growth 1.2 bp

## LAK @ VGK  ·  10000 joint draws  ·  412 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_LAK_win | p_overtime | goals | shots VGK/LAK | VGK/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.62 | 0.38 | 0.00 | 5.95 | 27.3/27.1 | 24.1/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.46 | 5.94 | 27.7/27.5 | 24.2/24.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.096 | 0.70 | 0.30 | 0.00 | 5.99 | 32.4/21.4 | 18.9/27.9 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.58 | 0.42 | 0.45 | 5.88 | 32.7/22.0 | 19.0/29.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.64 | 0.36 | 0.00 | 9.2 | 28.9/28.7 | 23.7/22.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.63 | 0.37 | 0.00 | 3.44 | 26.1/25.9 | 24.5/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 68 | 0.751 | 0.732 | +0.056 | +0.036 | $5.13 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 50 | 0.642 | 0.546 | +0.124 | +0.029 | $4.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Tomas Hertl: 1+ goals NO | 70 | 0.738 | 0.727 | +0.023 | +0.013 | $2.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10LAVGK-VGKTHERTL48-1|no; why: higher confidence-adjusted growth (13.90 vs 1.72 bp); relationships: KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT10LAVGK-VGKTHERTL48-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: VGK offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT10LAVGK-5|no; why: higher confidence-adjusted growth (7.28 vs 0.10 bp); wins across more scripts (relative breadth 0.978 vs 0.39); alternative not eligible: confidence-adjusted EV +0.0028 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT10LAVGK-VGKTHERTL48-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: LAK offense succeeds (4+ goals)
- **Tomas Hertl: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no; why: Player prop expression KXNHLGOAL-26OCT10LAVGK-VGKTHERTL48-1|no selected over player prop KXNHLAST-26OCT10LAVGK-VGKTHERTL48-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.86 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.3662): highest fidelity KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no (same contract)
- thesis LAK:SUPPRESSED (p 0.4923): highest fidelity KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no (same contract)
- KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4128, phi -0.235)
- KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.7 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2867, phi -0.289)
- KXNHLGOAL-26OCT10LAVGK-VGKTHERTL48-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4128, phi -0.203)
- override: Player prop expression KXNHLGOAL-26OCT10LAVGK-VGKTHERTL48-1|no selected over player prop KXNHLAST-26OCT10LAVGK-VGKTHERTL48-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.86 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.39 (adj +0.46) on $10.71, P(profit) 0.5807, adj growth 4.5 bp · B EV +1.49 (adj +0.55) on $12.06, P(profit) 0.4841, adj growth 5.3 bp · C EV +1.76 (adj +0.63) on $11.76, P(profit) 0.4841, adj growth 6.1 bp · R EV +0.16 (adj +0.11) on $2.00, P(profit) 0.7507, adj growth 4.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
