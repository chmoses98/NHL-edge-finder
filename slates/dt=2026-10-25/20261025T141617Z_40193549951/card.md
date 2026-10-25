# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T14:16:17Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +25.72 | +7.58 | +23.74 | 0.661 | -48.09 | -64.29 | 59.53 |
| B thesis-diversified (joint) ← optimiser card | 130.65 | +22.63 | +10.54 | +18.67 | 0.646 | -40.73 | -56.75 | 91.97 |
| C best expression per thesis | 103.73 | +17.90 | +8.68 | +11.83 | 0.616 | -35.95 | -51.35 | 76.73 |
| R FUNDED research stakes | 25.00 | +3.63 | +1.40 | +3.20 | 0.643 | -8.41 | -10.87 | 0.00 |

## FLA @ CHI  ·  10000 joint draws  ·  432 bet sides mapped, 14 +EV candidates, 4 on card


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
| Cole Schwindt: 1+ goals YES | 9 | 0.152 | 0.128 | +0.056 | +0.032 | $7.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 65 | 0.731 | 0.708 | +0.065 | +0.043 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Anton Frondell: 1+ goals YES | 19 | 0.241 | 0.227 | +0.041 | +0.027 | $8.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Frank Nazar: 1+ goals YES | 19 | 0.235 | 0.223 | +0.035 | +0.022 | $6.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT25FLACHI-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (24.80 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT25FLACHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: FLA offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (17.88 vs 13.12 bp); relationships: KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT25FLACHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense succeeds (4+ goals)
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25FLACHI-FLA3|no; why: higher confidence-adjusted growth (9.54 vs 8.79 bp); despite a smaller raw edge (+0.041 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT25FLACHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CHI offense suppressed (<= 2 goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (9.54 vs 6.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis FLA:OFFENSE_4PLUS (p 0.4002): highest fidelity KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes (same contract)
- thesis FLA:SUPPRESSED (p 0.3764): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.3658): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3764, phi -0.195)
- KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4002, phi -0.235)
- KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4176, phi -0.239)
- KXNHLGOAL-26OCT25FLACHI-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4176, phi -0.223)

portfolios: A EV +4.42 (adj +1.17) on $33.25, P(profit) 0.6623, adj growth 10.4 bp · B EV +9.02 (adj +5.51) on $42.04, P(profit) 0.4278, adj growth 48.2 bp · C EV +9.00 (adj +5.01) on $50.00, P(profit) 0.7544, adj growth 44.8 bp · R EV +0.49 (adj +0.32) on $5.00, P(profit) 0.7312, adj growth 11.9 bp

## NYI @ DAL  ·  10000 joint draws  ·  408 bet sides mapped, 8 +EV candidates, 4 on card


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
| Kyle Palmieri: 1+ goals YES | 20 | 0.247 | 0.230 | +0.036 | +0.019 | $4.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 73 | 0.796 | 0.760 | +0.052 | +0.017 | $12.01 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I over 3.5 goals scored YES | 26 | 0.330 | 0.290 | +0.057 | +0.017 | $2.76 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mikko Rantanen: 1+ goals NO | 69 | 0.727 | 0.715 | +0.022 | +0.010 | $7.13 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Kyle Palmieri: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5|yes; why: higher confidence-adjusted growth (4.69 vs 3.99 bp); despite a smaller raw edge (+0.036 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.902 vs 0.528); relationships: KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.119); KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: REINFORCING (phi 0.225); KXNHLGOAL-26OCT25NYIDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: NYI offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25NYIDAL-DAL2|no; why: higher confidence-adjusted growth (3.14 vs 1.80 bp); wins across more scripts (relative breadth 0.99 vs 0.875); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: MOSTLY_INDEPENDENT (phi 0.119); KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: DUPLICATIVE (phi 0.312); KXNHLGOAL-26OCT25NYIDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.134); failure: DAL wins by 2+
- **New York I over 3.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes selected over broad KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: REINFORCING (phi 0.225); KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: DUPLICATIVE (phi 0.312); KXNHLGOAL-26OCT25NYIDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: NYI offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25NYIDAL-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25NYIDAL-DAL3|no has the higher standalone adjusted growth (3.14 vs 1.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.134); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.134); KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3212): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes — Broad expression KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes selected over broad KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYI:WINS_BY_2PLUS (p 0.2276): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4484): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25NYIDAL-DAL3|no (same contract)
- KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4642, phi -0.244)
- KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.324, phi -0.732)
- KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:SUPPRESSED (p 0.4642, phi -0.653)
- KXNHLGOAL-26OCT25NYIDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3917, phi -0.232)
- override: Broad expression KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes selected over broad KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.94 (adj +1.13) on $33.25, P(profit) 0.5003, adj growth 7.8 bp · B EV +2.43 (adj +0.96) on $26.66, P(profit) 0.3804, adj growth 8.4 bp · C EV +2.54 (adj +0.97) on $20.24, P(profit) 0.3381, adj growth 8.5 bp · R EV +0.55 (adj +0.18) on $7.00, P(profit) 0.6877, adj growth 6.1 bp

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
| Dylan Samberg: 1+ goals YES | 4 | 0.061 | 0.054 | +0.018 | +0.012 | $2.70 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 17 | 0.212 | 0.200 | +0.032 | +0.020 | $5.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 29 | 0.335 | 0.321 | +0.031 | +0.017 | $6.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
- **Dylan Samberg: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (7.24 vs 2.94 bp); despite a smaller raw edge (+0.018 vs +0.031/contract); relationships: KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: WPG offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (6.00 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: MTL offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT25MTLWPG-3|yes; why: higher confidence-adjusted growth (2.94 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.935 vs 0.766); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MTL:OFFENSE_4PLUS (p 0.3953): highest fidelity KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3703): highest fidelity KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes (same contract)
- KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.116)
- KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3782, phi -0.216)
- KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.28)

portfolios: A EV +3.25 (adj +2.02) on $16.99, P(profit) 0.5135, adj growth 17.0 bp · B EV +2.84 (adj +1.76) on $14.80, P(profit) 0.5135, adj growth 15.2 bp · C EV +1.68 (adj +1.01) on $12.09, P(profit) 0.4808, adj growth 8.8 bp · R EV +0.43 (adj +0.28) on $1.00, P(profit) 0.061, adj growth 8.7 bp

## COL @ NSH  ·  10000 joint draws  ·  454 bet sides mapped, 4 +EV candidates, 2 on card


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
- thesis NSH:WINS (p 0.388): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- KXNHLSPREAD-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3881, phi -0.757)
- KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 28% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4914, phi -0.303)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT25COLNSH-COL5|no less than the minimum stake; KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no kept

portfolios: A EV +3.40 (adj +0.96) on $33.25, P(profit) 0.662, adj growth 7.0 bp · B EV +1.66 (adj +0.50) on $17.73, P(profit) 0.7335, adj growth 4.4 bp · C EV +1.31 (adj +0.42) on $15.37, P(profit) 0.7335, adj growth 3.7 bp · R EV +0.34 (adj +0.11) on $4.00, P(profit) 0.7335, adj growth 3.8 bp

## MIN @ VAN  ·  10000 joint draws  ·  384 bet sides mapped, 16 +EV candidates, 4 on card


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
| Minnesota wins by over 1.5 goals NO | 59 | 0.739 | 0.639 | +0.132 | +0.032 | $11.74 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver wins by over 1.5 goals YES | 19 | 0.304 | 0.227 | +0.103 | +0.026 | $3.58 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 71 | 0.832 | 0.750 | +0.108 | +0.025 | $11.14 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Brendan Gallagher: 1+ goals YES | 12 | 0.154 | 0.142 | +0.027 | +0.015 | $2.95 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Minnesota wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes has the higher standalone adjusted growth (13.95 vs 9.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.296); relationships: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: DUPLICATIVE (phi 0.393); KXNHLSPREAD-26OCT25MINVAN-MIN3|no: DUPLICATIVE (phi 0.755); KXNHLGOAL-26OCT25MINVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.107); failure: MIN wins by 2+
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: Broad expression KXNHLSPREAD-26OCT25MINVAN-VAN2|yes selected over broad KXNHLSPREAD-26OCT25MINVAN-VAN3|yes because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.65 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT25MINVAN-MIN2|no: DUPLICATIVE (phi 0.393); KXNHLSPREAD-26OCT25MINVAN-MIN3|no: REINFORCING (phi 0.297); KXNHLGOAL-26OCT25MINVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.137); failure: MIN wins (incl. OT/SO)
- **Minnesota wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes has the higher standalone adjusted growth (13.95 vs 6.95 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.224); relationships: KXNHLSPREAD-26OCT25MINVAN-MIN2|no: DUPLICATIVE (phi 0.755); KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: REINFORCING (phi 0.297); KXNHLGOAL-26OCT25MINVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.089); failure: MIN wins by 2+
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes has the higher standalone adjusted growth (13.95 vs 4.22 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.127); relationships: KXNHLSPREAD-26OCT25MINVAN-MIN2|no: MOSTLY_INDEPENDENT (phi 0.107); KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: MOSTLY_INDEPENDENT (phi 0.137); KXNHLSPREAD-26OCT25MINVAN-MIN3|no: MOSTLY_INDEPENDENT (phi 0.089); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.304): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- thesis VAN:WINS (p 0.5303): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.4295): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT25MINVAN-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.4 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2614, phi -1.0)
- KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.9 pts; opposing: failure thesis MIN:WINS (p 0.4697, phi -0.622)
- KXNHLSPREAD-26OCT25MINVAN-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.7 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2614, phi -0.755)
- KXNHLGOAL-26OCT25MINVAN-VANBGALLAGHER7-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3624, phi -0.179)
- override: Broad expression KXNHLSPREAD-26OCT25MINVAN-VAN2|yes selected over broad KXNHLSPREAD-26OCT25MINVAN-VAN3|yes because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.65 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +10.72 (adj +2.30) on $33.25, P(profit) 0.5303, adj growth 17.5 bp · B EV +6.67 (adj +1.81) on $29.42, P(profit) 0.7481, adj growth 15.8 bp · C EV +3.37 (adj +1.27) on $6.03, P(profit) 0.1986, adj growth 11.0 bp · R EV +1.82 (adj +0.51) on $8.00, P(profit) 0.7481, adj growth 17.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT25MINVAN-MIN|no == KXNHLGAME-26OCT25MINVAN-VAN|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
