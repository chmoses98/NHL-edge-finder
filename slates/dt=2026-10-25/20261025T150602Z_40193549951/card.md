# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T15:06:02Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +28.13 | +7.92 | +26.15 | 0.663 | -48.75 | -66.34 | 61.80 |
| B thesis-diversified (joint) ← optimiser card | 145.40 | +24.99 | +12.70 | +22.32 | 0.646 | -46.75 | -62.75 | 110.92 |
| C best expression per thesis | 117.17 | +17.74 | +8.66 | +13.19 | 0.620 | -37.94 | -54.42 | 76.31 |
| R FUNDED research stakes | 25.00 | +3.41 | +1.55 | +0.84 | 0.608 | -9.12 | -11.74 | 0.00 |

## FLA @ CHI  ·  10000 joint draws  ·  434 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_FLA_win | p_overtime | goals | shots CHI/FLA | CHI/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.46 | 0.54 | 0.00 | 6.05 | 26.4/27.0 | 23.2/23.0 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.109 | 0.42 | 0.58 | 0.00 | 5.96 | 20.8/32.0 | 27.9/17.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.48 | 5.92 | 26.4/26.8 | 23.5/23.1 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.49 | 0.51 | 0.43 | 5.85 | 20.9/32.1 | 28.8/17.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.50 | 0.50 | 0.00 | 9.34 | 27.9/28.4 | 22.2/21.7 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.073 | 0.38 | 0.62 | 0.00 | 9.22 | 22.3/33.9 | 26.4/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 65 | 0.731 | 0.708 | +0.065 | +0.043 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 10 | 0.152 | 0.130 | +0.045 | +0.024 | $5.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Anton Frondell: 1+ goals YES | 19 | 0.241 | 0.227 | +0.041 | +0.027 | $8.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 12 | 0.158 | 0.145 | +0.031 | +0.018 | $4.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (17.88 vs 13.12 bp); relationships: KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT25FLACHI-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (12.75 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: FLA offense suppressed (<= 2 goals)
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25FLACHI-FLA3|no; why: higher confidence-adjusted growth (9.54 vs 6.22 bp); despite a smaller raw edge (+0.041 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: CHI offense suppressed (<= 2 goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (9.54 vs 6.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis FLA:SUPPRESSED (p 0.3764): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:OFFENSE_4PLUS (p 0.4002): highest fidelity KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3658): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4002, phi -0.235)
- KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3764, phi -0.195)
- KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4176, phi -0.239)
- KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4176, phi -0.181)

portfolios: A EV +5.65 (adj +1.05) on $32.61, P(profit) 0.6108, adj growth 8.8 bp · B EV +7.23 (adj +4.30) on $38.58, P(profit) 0.4345, adj growth 38.0 bp · C EV +7.31 (adj +3.96) on $50.00, P(profit) 0.7544, adj growth 35.5 bp · R EV +0.49 (adj +0.32) on $5.00, P(profit) 0.7312, adj growth 11.9 bp

## NYI @ DAL  ·  10000 joint draws  ·  408 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NYI_win | p_overtime | goals | shots DAL/NYI | DAL/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 6.0 | 26.1/25.9 | 22.7/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.53 | 0.47 | 0.45 | 5.88 | 26.0/26.0 | 22.8/22.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.58 | 0.42 | 0.00 | 9.24 | 27.7/27.6 | 22.1/21.4 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.079 | 0.64 | 0.36 | 0.00 | 5.98 | 30.5/20.6 | 17.8/26.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.53 | 0.47 | 0.45 | 5.9 | 30.9/20.8 | 17.5/27.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.57 | 0.43 | 0.00 | 3.42 | 24.6/24.6 | 22.9/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 18 | 0.241 | 0.220 | +0.051 | +0.029 | $8.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Kyle Palmieri: 1+ goals YES | 20 | 0.247 | 0.230 | +0.036 | +0.019 | $5.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 68 | 0.727 | 0.714 | +0.032 | +0.018 | $14.55 | FUNDED_RESEARCH | $4 | DAL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 73 | 0.796 | 0.760 | +0.052 | +0.017 | $9.12 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes; why: higher confidence-adjusted growth (12.10 vs 4.69 bp); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT25NYIDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.131); failure: NYI offense suppressed (<= 2 goals)
- **Kyle Palmieri: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (12.10 vs 4.69 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT25NYIDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.119); failure: NYI offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25NYIDAL-DAL3|no; why: higher confidence-adjusted growth (3.56 vs 3.14 bp); despite a smaller raw edge (+0.032 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.134); failure: DAL offense succeeds (4+ goals)
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25NYIDAL-DAL2|no; why: higher confidence-adjusted growth (3.14 vs 1.80 bp); wins across more scripts (relative breadth 0.99 vs 0.875); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: MOSTLY_INDEPENDENT (phi 0.119); KXNHLGOAL-26OCT25NYIDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.134); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3212): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS_BY_2PLUS (p 0.2276): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.3847): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25NYIDAL-DALMRANTANEN96-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4642, phi -0.235)
- KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4642, phi -0.244)
- KXNHLGOAL-26OCT25NYIDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3917, phi -0.232)
- KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.324, phi -0.732)

portfolios: A EV +5.22 (adj +2.04) on $32.61, P(profit) 0.4453, adj growth 15.6 bp · B EV +4.37 (adj +2.32) on $37.12, P(profit) 0.4191, adj growth 20.2 bp · C EV +4.08 (adj +2.00) on $33.68, P(profit) 0.6856, adj growth 17.4 bp · R EV +0.39 (adj +0.17) on $7.00, P(profit) 0.6022, adj growth 6.1 bp

## MTL @ WPG  ·  10000 joint draws  ·  396 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_MTL_win | p_overtime | goals | shots WPG/MTL | WPG/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.43 | 0.57 | 0.00 | 6.01 | 27.2/27.1 | 23.3/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.48 | 5.91 | 27.1/27.2 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.48 | 0.52 | 0.00 | 9.26 | 28.8/28.6 | 22.5/22.7 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.077 | 0.53 | 0.47 | 0.00 | 5.99 | 32.1/21.5 | 18.3/28.1 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.50 | 0.50 | 0.47 | 5.88 | 32.4/21.7 | 18.6/29.0 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.061 | 0.41 | 0.59 | 0.00 | 5.99 | 21.8/31.9 | 27.7/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Josh Anderson: 1+ goals YES | 17 | 0.212 | 0.200 | +0.032 | +0.020 | $5.95 | FUNDED_RESEARCH | $2 | MTL:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 29 | 0.335 | 0.321 | +0.031 | +0.017 | $6.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 13 | 0.170 | 0.149 | +0.032 | +0.011 | $2.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (6.00 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0016 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: MTL offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT25MTLWPG-3|yes; why: higher confidence-adjusted growth (2.94 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.935 vs 0.766); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: WPG offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes has the higher standalone adjusted growth (2.94 vs 2.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MTL:OFFENSE_4PLUS (p 0.3953): highest fidelity KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3703): highest fidelity KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes (same contract)
- KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3782, phi -0.216)
- KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.28)
- KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.204)

portfolios: A EV +3.25 (adj +1.58) on $19.57, P(profit) 0.5676, adj growth 12.8 bp · B EV +2.29 (adj +1.22) on $14.73, P(profit) 0.5676, adj growth 10.6 bp · C EV +1.68 (adj +1.01) on $12.09, P(profit) 0.4808, adj growth 8.8 bp · R EV +0.35 (adj +0.22) on $2.00, P(profit) 0.2118, adj growth 7.4 bp

## COL @ NSH  ·  10000 joint draws  ·  454 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_COL_win | p_overtime | goals | shots NSH/COL | NSH/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.126 | 0.30 | 0.70 | 0.00 | 6.01 | 22.8/35.4 | 30.5/20.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.33 | 0.67 | 0.00 | 6.06 | 28.5/29.4 | 24.9/25.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.100 | 0.30 | 0.70 | 0.00 | 9.32 | 24.1/37.0 | 28.7/19.5 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.45 | 0.55 | 0.48 | 5.91 | 22.8/35.3 | 31.8/19.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.47 | 0.53 | 0.47 | 6.06 | 28.5/29.3 | 25.9/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.34 | 0.66 | 0.00 | 9.44 | 30.4/31.2 | 23.8/24.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins by over 2.5 goals NO | 66 | 0.734 | 0.694 | +0.058 | +0.018 | $13.89 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 1+ assists NO | 41 | 0.479 | 0.440 | +0.053 | +0.013 | $3.83 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.72) | EVIDENCE_MIXED | D |
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: higher confidence-adjusted growth (3.44 vs 2.29 bp); wins across more scripts (relative breadth 1.026 vs 0.896); relationships: KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: REINFORCING (phi 0.204); failure: COL wins by 2+
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25COLNSH-COL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25COLNSH-COL3|no has the higher standalone adjusted growth (3.44 vs 1.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.204); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25COLNSH-COL3|no: REINFORCING (phi 0.204); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · high event (8+) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4179): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- thesis COL:SUPPRESSED (p 0.2987): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- KXNHLSPREAD-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3881, phi -0.757)
- KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 28% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4914, phi -0.303)

portfolios: A EV +3.33 (adj +0.94) on $32.61, P(profit) 0.662, adj growth 6.9 bp · B EV +1.66 (adj +0.50) on $17.73, P(profit) 0.7335, adj growth 4.4 bp · C EV +1.31 (adj +0.42) on $15.37, P(profit) 0.7335, adj growth 3.7 bp · R EV +0.34 (adj +0.11) on $4.00, P(profit) 0.7335, adj growth 3.8 bp

## MIN @ VAN  ·  10000 joint draws  ·  384 bet sides mapped, 22 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_MIN_win | p_overtime | goals | shots VAN/MIN | VAN/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| MIN shot control · normal event (5-7) · decided (2+) | 0.120 | 0.50 | 0.50 | 0.00 | 6.01 | 22.4/34.5 | 30.8/19.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.55 | 0.45 | 0.00 | 6.01 | 27.8/28.4 | 25.1/24.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.47 | 0.53 | 0.45 | 5.98 | 22.1/34.3 | 30.6/18.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.54 | 0.46 | 0.47 | 5.92 | 28.2/28.9 | 25.6/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.56 | 0.44 | 0.00 | 9.49 | 29.5/30.3 | 24.5/23.1 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.083 | 0.49 | 0.51 | 0.00 | 9.31 | 23.9/36.1 | 29.6/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brendan Gallagher: 1+ goals YES | 11 | 0.154 | 0.142 | +0.038 | +0.025 | $5.97 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ goals YES | 19 | 0.248 | 0.230 | +0.047 | +0.029 | $7.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Minnesota wins by over 1.5 goals NO | 58 | 0.739 | 0.632 | +0.141 | +0.035 | $17.24 | FUNDED_RESEARCH | $5 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Linus Karlsson: 1+ goals YES | 17 | 0.226 | 0.207 | +0.046 | +0.027 | $6.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes has the higher standalone adjusted growth (13.95 vs 13.25 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.127); relationships: KXNHLGOAL-26OCT25MINVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: VAN offense suppressed (<= 2 goals)
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes has the higher standalone adjusted growth (13.95 vs 11.36 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.140); relationships: KXNHLGOAL-26OCT25MINVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: VAN offense suppressed (<= 2 goals)
- **Minnesota wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes has the higher standalone adjusted growth (13.95 vs 11.31 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.296); relationships: KXNHLGOAL-26OCT25MINVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26OCT25MINVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.13); failure: MIN wins by 2+
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes has the higher standalone adjusted growth (13.95 vs 10.47 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.141); relationships: KXNHLGOAL-26OCT25MINVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MINVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: MOSTLY_INDEPENDENT (phi 0.13); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.304): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.4295): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5303): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- KXNHLGOAL-26OCT25MINVAN-VANBGALLAGHER7-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3624, phi -0.179)
- KXNHLGOAL-26OCT25MINVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3624, phi -0.227)
- KXNHLSPREAD-26OCT25MINVAN-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.4 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2614, phi -1.0)
- KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3624, phi -0.202)

portfolios: A EV +10.68 (adj +2.31) on $32.61, P(profit) 0.5303, adj growth 17.7 bp · B EV +9.44 (adj +4.36) on $37.24, P(profit) 0.4462, adj growth 37.8 bp · C EV +3.37 (adj +1.27) on $6.03, P(profit) 0.1986, adj growth 11.0 bp · R EV +1.83 (adj +0.73) on $7.00, P(profit) 0.762, adj growth 24.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT25MINVAN-MIN|no == KXNHLGAME-26OCT25MINVAN-VAN|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
