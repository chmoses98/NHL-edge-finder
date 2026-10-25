# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T12:31:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +24.58 | +6.88 | +22.19 | 0.650 | -48.73 | -67.63 | 52.29 |
| B thesis-diversified (joint) ← optimiser card | 111.28 | +20.67 | +9.69 | +16.72 | 0.633 | -41.57 | -55.87 | 85.06 |
| C best expression per thesis | 106.51 | +17.27 | +8.17 | +15.32 | 0.629 | -35.55 | -52.88 | 72.29 |
| R FUNDED research stakes | 25.00 | +4.81 | +1.98 | +3.28 | 0.621 | -11.57 | -13.70 | 0.00 |

## FLA @ CHI  ·  10000 joint draws  ·  436 bet sides mapped, 13 +EV candidates, 4 on card


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
| Sam Reinhart: 1+ goals NO | 65 | 0.733 | 0.711 | +0.067 | +0.045 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 10 | 0.151 | 0.130 | +0.045 | +0.023 | $5.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Anton Frondell: 1+ goals YES | 19 | 0.241 | 0.227 | +0.041 | +0.027 | $8.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Frank Nazar: 1+ goals YES | 19 | 0.235 | 0.223 | +0.035 | +0.022 | $6.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (19.81 vs 13.36 bp); relationships: KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT25FLACHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT25FLACHI-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (12.20 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT25FLACHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: FLA offense suppressed (<= 2 goals)
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25FLACHI-FLA3|no; why: higher confidence-adjusted growth (9.54 vs 8.79 bp); despite a smaller raw edge (+0.041 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT25FLACHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CHI offense suppressed (<= 2 goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (9.54 vs 6.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis FLA:SUPPRESSED (p 0.3764): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:OFFENSE_4PLUS (p 0.4002): highest fidelity KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3658): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4002, phi -0.238)
- KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3764, phi -0.193)
- KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4176, phi -0.239)
- KXNHLGOAL-26OCT25FLACHI-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4176, phi -0.223)

portfolios: A EV +4.53 (adj +0.94) on $33.25, P(profit) 0.6666, adj growth 8.1 bp · B EV +7.19 (adj +4.39) on $40.43, P(profit) 0.4718, adj growth 38.9 bp · C EV +7.57 (adj +4.12) on $50.00, P(profit) 0.7562, adj growth 37.1 bp · R EV +0.50 (adj +0.34) on $5.00, P(profit) 0.7325, adj growth 12.5 bp

## NYI @ DAL  ·  10000 joint draws  ·  408 bet sides mapped, 7 +EV candidates, 3 on card


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
| Kyle Palmieri: 1+ goals YES | 20 | 0.247 | 0.230 | +0.036 | +0.019 | $4.73 | FUNDED_RESEARCH | $2 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 73 | 0.796 | 0.760 | +0.052 | +0.017 | $13.00 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I over 3.5 goals scored YES | 26 | 0.330 | 0.290 | +0.057 | +0.017 | $2.31 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Kyle Palmieri: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25NYIDAL-DAL3|no; why: higher confidence-adjusted growth (4.69 vs 3.14 bp); despite a smaller raw edge (+0.036 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.119); KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: REINFORCING (phi 0.225); failure: NYI offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25NYIDAL-DAL2|no; why: higher confidence-adjusted growth (3.14 vs 1.80 bp); wins across more scripts (relative breadth 0.99 vs 0.875); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: MOSTLY_INDEPENDENT (phi 0.119); KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: DUPLICATIVE (phi 0.312); failure: DAL wins by 2+
- **New York I over 3.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes has the higher standalone adjusted growth (4.69 vs 3.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.225); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: REINFORCING (phi 0.225); KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: DUPLICATIVE (phi 0.312); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3212): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4484): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25NYIDAL-DAL3|no (same contract)
- thesis NYI:WINS_BY_2PLUS (p 0.2276): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4642, phi -0.244)
- KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.324, phi -0.732)
- KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:SUPPRESSED (p 0.4642, phi -0.653)

portfolios: A EV +4.38 (adj +1.27) on $33.25, P(profit) 0.5217, adj growth 8.1 bp · B EV +2.18 (adj +0.85) on $20.04, P(profit) 0.4445, adj growth 7.5 bp · C EV +1.96 (adj +0.81) on $20.78, P(profit) 0.8253, adj growth 7.1 bp · R EV +0.82 (adj +0.33) on $7.00, P(profit) 0.4445, adj growth 10.6 bp

## MTL @ WPG  ·  10000 joint draws  ·  388 bet sides mapped, 3 +EV candidates, 3 on card


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
| Dylan Samberg: 1+ goals YES | 4 | 0.061 | 0.054 | +0.018 | +0.012 | $2.70 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 17 | 0.212 | 0.200 | +0.032 | +0.020 | $5.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 29 | 0.335 | 0.318 | +0.031 | +0.013 | $4.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
- **Dylan Samberg: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (7.24 vs 1.78 bp); despite a smaller raw edge (+0.018 vs +0.031/contract); relationships: KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: WPG offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT25MTLWPG-3|yes; why: higher confidence-adjusted growth (6.00 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: MTL offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT25MTLWPG-3|yes; why: higher confidence-adjusted growth (1.78 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.935 vs 0.766); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MTL:OFFENSE_4PLUS (p 0.3953): highest fidelity KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3703): highest fidelity KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes (same contract)
- KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.116)
- KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3782, phi -0.216)
- KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.28)

portfolios: A EV +3.25 (adj +1.92) on $16.99, P(profit) 0.5135, adj growth 16.1 bp · B EV +2.70 (adj +1.62) on $13.45, P(profit) 0.5135, adj growth 14.0 bp · C EV +1.54 (adj +0.88) on $10.73, P(profit) 0.4808, adj growth 7.6 bp · R EV +0.43 (adj +0.28) on $1.00, P(profit) 0.061, adj growth 8.7 bp

## COL @ NSH  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 1 on card


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
| Colorado wins by over 2.5 goals NO | 66 | 0.734 | 0.694 | +0.058 | +0.018 | $14.37 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: higher confidence-adjusted growth (3.44 vs 2.29 bp); wins across more scripts (relative breadth 1.026 vs 0.896); relationships: only recommended bet in this game; failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · high event (8+) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4179): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- thesis NSH:WINS (p 0.388): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- KXNHLSPREAD-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3881, phi -0.757)

portfolios: A EV +2.76 (adj +0.81) on $33.25, P(profit) 0.6892, adj growth 5.8 bp · B EV +1.23 (adj +0.39) on $14.37, P(profit) 0.7335, adj growth 3.5 bp · C EV +1.31 (adj +0.42) on $15.37, P(profit) 0.7335, adj growth 3.7 bp · R EV +0.34 (adj +0.11) on $4.00, P(profit) 0.7335, adj growth 3.8 bp

## MIN @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 11 +EV candidates, 4 on card


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
| Vancouver over 4.5 goals scored YES | 16 | 0.251 | 0.203 | +0.081 | +0.033 | $5.92 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | DIRECT (0.58) | EVIDENCE_MIXED | D |
| Vancouver wins by over 2.5 goals YES | 12 | 0.199 | 0.154 | +0.071 | +0.027 | $1.90 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | DIRECT (0.65) | EVIDENCE_MIXED | D |
| Minnesota wins by over 1.5 goals NO | 59 | 0.739 | 0.639 | +0.132 | +0.032 | $13.50 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota over 1.5 goals scored NO | 13 | 0.184 | 0.152 | +0.046 | +0.014 | $1.68 | FUNDED_RESEARCH | $1 | MIN:SUPPRESSED | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Vancouver over 4.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: higher confidence-adjusted growth (16.97 vs 13.95 bp); relationships: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes: REINFORCING (phi 0.522); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: DUPLICATIVE (phi 0.308); KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2|no: INTENTIONAL_DIVERSIFIER (phi -0.045); failure: MIN wins (incl. OT/SO)
- **Vancouver wins by over 2.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes has the higher standalone adjusted growth (16.97 vs 13.95 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.522); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes: REINFORCING (phi 0.522); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: REINFORCING (phi 0.296); KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2|no: REINFORCING (phi 0.393); failure: MIN wins (incl. OT/SO)
- **Minnesota wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes has the higher standalone adjusted growth (16.97 vs 9.32 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.308); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes: DUPLICATIVE (phi 0.308); KXNHLSPREAD-26OCT25MINVAN-VAN3|yes: REINFORCING (phi 0.296); KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2|no: REINFORCING (phi 0.282); failure: MIN wins by 2+
- **Minnesota over 1.5 goals scored NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes has the higher standalone adjusted growth (13.95 vs 3.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.393); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes: INTENTIONAL_DIVERSIFIER (phi -0.045); KXNHLSPREAD-26OCT25MINVAN-VAN3|yes: REINFORCING (phi 0.393); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: REINFORCING (phi 0.282); failure: MIN wins (incl. OT/SO)

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.4295): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.304): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT25MINVAN-VAN2|yes less than the minimum stake; KXNHLSPREAD-26OCT25MINVAN-VAN3|yes kept
- thesis VAN:WINS (p 0.5303): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes: FUNDED_RESEARCH; family MIXED; loses 42% of the draws where the thesis happens; opposing: failure thesis MIN:WINS (p 0.4697, phi -0.448)
- KXNHLSPREAD-26OCT25MINVAN-VAN3|yes: FUNDED_RESEARCH; family MIXED; loses 35% of the draws where the thesis happens; opposing: failure thesis MIN:WINS (p 0.4697, phi -0.469)
- KXNHLSPREAD-26OCT25MINVAN-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.4 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2614, phi -1.0)
- KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2|no: FUNDED_RESEARCH; family MIXED; loses 53% of the draws where the thesis happens; opposing: failure thesis MIN:WINS (p 0.4697, phi -0.413)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT25MINVAN-VAN2|yes less than the minimum stake; KXNHLSPREAD-26OCT25MINVAN-VAN3|yes kept
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT25MINVAN-MIN3|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2|no kept

portfolios: A EV +9.67 (adj +1.94) on $33.25, P(profit) 0.5303, adj growth 14.3 bp · B EV +7.38 (adj +2.44) on $22.99, P(profit) 0.3956, adj growth 21.2 bp · C EV +4.88 (adj +1.94) on $9.63, P(profit) 0.3092, adj growth 16.8 bp · R EV +2.72 (adj +0.92) on $8.00, P(profit) 0.3956, adj growth 29.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT25MINVAN-VAN|yes == KXNHLGAME-26OCT25MINVAN-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
