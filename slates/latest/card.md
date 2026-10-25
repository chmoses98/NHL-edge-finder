# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T16:01:18Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +26.89 | +8.92 | +24.35 | 0.661 | -48.18 | -62.95 | 72.34 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +27.25 | +15.80 | +23.75 | 0.644 | -48.38 | -70.44 | 138.44 |
| C best expression per thesis | 129.45 | +21.13 | +11.09 | +17.86 | 0.617 | -42.61 | -58.33 | 97.19 |
| R FUNDED research stakes | 19.00 | +2.82 | +1.61 | +3.14 | 0.516 | -11.02 | -11.29 | 0.00 |

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
| Brady Tkachuk: 1+ goals NO | 61 | 0.693 | 0.671 | +0.067 | +0.044 | $19.29 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 10 | 0.152 | 0.129 | +0.045 | +0.022 | $5.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 23 | 0.286 | 0.271 | +0.044 | +0.029 | $8.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Anton Frondell: 1+ goals YES | 19 | 0.241 | 0.224 | +0.041 | +0.023 | $6.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no; why: higher confidence-adjusted growth (18.62 vs 17.88 bp); relationships: KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT25FLACHI-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (11.46 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: FLA offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25FLACHI-FLA3|no; why: higher confidence-adjusted growth (9.74 vs 8.79 bp); despite a smaller raw edge (+0.044 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CHI offense suppressed (<= 2 goals)
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (9.74 vs 7.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis FLA:SUPPRESSED (p 0.3764): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:OFFENSE_4PLUS (p 0.4002): highest fidelity KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3658): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4002, phi -0.235)
- KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3764, phi -0.195)
- KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4176, phi -0.252)
- KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4176, phi -0.239)

portfolios: A EV +3.89 (adj +1.42) on $33.72, P(profit) 0.6926, adj growth 13.0 bp · B EV +7.20 (adj +4.26) on $39.79, P(profit) 0.4438, adj growth 37.8 bp · C EV +7.52 (adj +4.05) on $50.00, P(profit) 0.7241, adj growth 36.4 bp · R EV +0.53 (adj +0.36) on $5.00, P(profit) 0.6932, adj growth 13.1 bp

## NYI @ DAL  ·  10000 joint draws  ·  414 bet sides mapped, 11 +EV candidates, 4 on card


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
| Brayden Schenn: 1+ goals YES | 17 | 0.241 | 0.217 | +0.061 | +0.037 | $9.84 | FUNDED_RESEARCH | $3 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Kyle Palmieri: 1+ goals YES | 19 | 0.247 | 0.229 | +0.046 | +0.028 | $7.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 9 | 0.128 | 0.113 | +0.032 | +0.017 | $4.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Logan Stanley: 1+ goals YES | 4 | 0.057 | 0.053 | +0.014 | +0.010 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes; why: higher confidence-adjusted growth (20.30 vs 10.67 bp); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT25NYIDAL-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT25NYIDAL-NYILSTANLEY8-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: NYI offense suppressed (<= 2 goals)
- **Kyle Palmieri: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (20.30 vs 10.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT25NYIDAL-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT25NYIDAL-NYILSTANLEY8-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: NYI offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (20.30 vs 7.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT25NYIDAL-NYILSTANLEY8-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: NYI offense suppressed (<= 2 goals)
- **Logan Stanley: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (20.30 vs 5.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT25NYIDAL-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3212): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.4417): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS_BY_2PLUS (p 0.2276): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI2|yes (same contract)
- KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4642, phi -0.235)
- KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4642, phi -0.244)
- KXNHLGOAL-26OCT25NYIDAL-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4642, phi -0.186)
- KXNHLGOAL-26OCT25NYIDAL-NYILSTANLEY8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4642, phi -0.118)

portfolios: A EV +6.21 (adj +2.68) on $33.72, P(profit) 0.4453, adj growth 20.9 bp · B EV +7.28 (adj +4.43) on $24.07, P(profit) 0.5289, adj growth 38.4 bp · C EV +5.08 (adj +2.77) on $39.28, P(profit) 0.599, adj growth 24.0 bp · R EV +1.02 (adj +0.62) on $3.00, P(profit) 0.2413, adj growth 20.9 bp

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
| Dylan Samberg: 1+ goals YES | 4 | 0.061 | 0.053 | +0.018 | +0.011 | $2.27 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 29 | 0.335 | 0.320 | +0.031 | +0.016 | $5.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 18 | 0.212 | 0.203 | +0.021 | +0.012 | $3.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Dylan Samberg: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (5.81 vs 2.52 bp); despite a smaller raw edge (+0.018 vs +0.031/contract); relationships: KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT25MTLWPG-3|yes; why: higher confidence-adjusted growth (2.52 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.935 vs 0.766); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: WPG offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (2.12 vs 1.08 bp); alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WPG:OFFENSE_4PLUS (p 0.3703): highest fidelity KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.3953): highest fidelity KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes (same contract)
- KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.116)
- KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.28)
- KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3782, phi -0.216)

portfolios: A EV +2.64 (adj +1.47) on $15.13, P(profit) 0.5135, adj growth 12.0 bp · B EV +1.93 (adj +1.08) on $11.31, P(profit) 0.5135, adj growth 9.3 bp · C EV +0.99 (adj +0.53) on $9.35, P(profit) 0.4808, adj growth 4.6 bp · R EV +0.43 (adj +0.25) on $1.00, P(profit) 0.061, adj growth 7.5 bp

## COL @ NSH  ·  10000 joint draws  ·  454 bet sides mapped, 3 +EV candidates, 3 on card


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
| Mavrik Bourque: 1+ assists NO | 78 | 0.866 | 0.818 | +0.074 | +0.026 | $19.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 66 | 0.734 | 0.694 | +0.058 | +0.018 | $14.50 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 1.5 goals NO | 54 | 0.612 | 0.574 | +0.054 | +0.016 | $1.65 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT25COLNSH-4|no; why: higher confidence-adjusted growth (9.03 vs 0.38 bp); wins across more scripts (relative breadth 0.998 vs 0.358); alternative not eligible: confidence-adjusted EV +0.0040 below the 0.010/contract floor; relationships: KXNHLSPREAD-26OCT25COLNSH-COL3|no: INTENTIONAL_DIVERSIFIER (phi -0.097); KXNHLSPREAD-26OCT25COLNSH-COL2|no: INTENTIONAL_DIVERSIFIER (phi -0.108); failure: NSH offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: higher confidence-adjusted growth (3.44 vs 2.29 bp); wins across more scripts (relative breadth 1.026 vs 0.896); relationships: KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.097); KXNHLSPREAD-26OCT25COLNSH-COL2|no: DUPLICATIVE (phi 0.757); failure: COL wins by 2+
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25COLNSH-COL3|no has the higher standalone adjusted growth (3.44 vs 2.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.757); they share one thesis budget; relationships: KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.108); KXNHLSPREAD-26OCT25COLNSH-COL3|no: DUPLICATIVE (phi 0.757); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · high event (8+) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4179): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- thesis NSH:SUPPRESSED (p 0.456): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3284, phi -0.166)
- KXNHLSPREAD-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3881, phi -0.757)
- KXNHLSPREAD-26OCT25COLNSH-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3881, phi -1.0)

portfolios: A EV +3.11 (adj +1.00) on $33.72, P(profit) 0.6119, adj growth 8.7 bp · B EV +3.20 (adj +1.08) on $35.44, P(profit) 0.6205, adj growth 9.9 bp · C EV +1.31 (adj +0.42) on $15.37, P(profit) 0.7335, adj growth 3.7 bp · R EV +0.44 (adj +0.14) on $5.00, P(profit) 0.7335, adj growth 4.6 bp

## MIN @ VAN  ·  10000 joint draws  ·  384 bet sides mapped, 24 +EV candidates, 4 on card


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
| Linus Karlsson: 1+ goals YES | 16 | 0.226 | 0.208 | +0.056 | +0.038 | $10.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 11 | 0.154 | 0.141 | +0.038 | +0.024 | $5.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Matt Boldy: 1+ goals NO | 59 | 0.655 | 0.636 | +0.048 | +0.029 | $17.45 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 19 | 0.234 | 0.221 | +0.034 | +0.020 | $5.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: higher confidence-adjusted growth (22.53 vs 13.95 bp); despite a smaller raw edge (+0.056 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.92 vs 0.473); relationships: KXNHLGOAL-26OCT25MINVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (22.53 vs 11.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: VAN offense suppressed (<= 2 goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes has the higher standalone adjusted growth (13.95 vs 7.75 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.158); relationships: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25MINVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: MIN offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (22.53 vs 5.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT25MINVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.4295): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.304): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- thesis MIN:SUPPRESSED (p 0.3933): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3624, phi -0.202)
- KXNHLGOAL-26OCT25MINVAN-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3624, phi -0.179)
- KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3921, phi -0.264)
- KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3624, phi -0.205)

portfolios: A EV +11.04 (adj +2.35) on $33.72, P(profit) 0.5303, adj growth 17.8 bp · B EV +7.63 (adj +4.95) on $39.39, P(profit) 0.4494, adj growth 43.0 bp · C EV +6.22 (adj +3.32) on $15.45, P(profit) 0.3558, adj growth 28.5 bp · R EV +0.39 (adj +0.24) on $5.00, P(profit) 0.6546, adj growth 8.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT25MINVAN-VAN|yes == KXNHLGAME-26OCT25MINVAN-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
