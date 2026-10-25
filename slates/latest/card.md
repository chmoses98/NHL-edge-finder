# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T17:31:18Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +27.71 | +8.25 | +26.30 | 0.676 | -45.07 | -64.28 | 66.11 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +25.59 | +14.14 | +22.11 | 0.660 | -44.31 | -60.10 | 126.14 |
| C best expression per thesis | 112.18 | +20.67 | +11.19 | +16.91 | 0.606 | -43.97 | -58.60 | 97.79 |
| R FUNDED research stakes | 23.00 | +3.58 | +1.87 | +2.06 | 0.517 | -8.32 | -12.51 | 0.00 |

## FLA @ CHI  ·  10000 joint draws  ·  448 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.376 / away 0.624

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
| Brady Tkachuk: 1+ goals NO | 61 | 0.693 | 0.671 | +0.067 | +0.044 | $16.74 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Anton Frondell: 1+ goals YES | 18 | 0.241 | 0.225 | +0.051 | +0.035 | $8.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 22 | 0.286 | 0.269 | +0.054 | +0.037 | $9.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 11 | 0.152 | 0.130 | +0.035 | +0.013 | $2.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no; why: higher confidence-adjusted growth (18.62 vs 17.88 bp); relationships: KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: FLA offense succeeds (4+ goals)
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (16.67 vs 16.25 bp); despite a smaller raw edge (+0.051 vs +0.054/contract); relationships: KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (16.67 vs 16.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: CHI offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT25FLACHI-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (3.68 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis FLA:SUPPRESSED (p 0.3764): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.3658): highest fidelity KXNHLTEAMTOTAL-26OCT25FLACHI-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.4714): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4002, phi -0.235)
- KXNHLGOAL-26OCT25FLACHI-CHIAFRONDELL16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4176, phi -0.239)
- KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4176, phi -0.252)
- KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3764, phi -0.195)

portfolios: A EV +5.07 (adj +0.94) on $33.72, P(profit) 0.6269, adj growth 7.2 bp · B EV +7.07 (adj +4.51) on $37.31, P(profit) 0.5188, adj growth 40.5 bp · C EV +7.34 (adj +4.04) on $50.00, P(profit) 0.7157, adj growth 36.2 bp · R EV +0.53 (adj +0.36) on $5.00, P(profit) 0.6932, adj growth 13.1 bp

## NYI @ DAL  ·  10000 joint draws  ·  438 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.632 / away 0.368

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NYI_win | p_overtime | goals | shots DAL/NYI | DAL/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.58 | 0.42 | 0.00 | 6.02 | 26.1/26.0 | 23.0/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.49 | 5.9 | 26.0/26.0 | 22.8/22.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.077 | 0.66 | 0.34 | 0.00 | 5.95 | 30.7/20.6 | 17.9/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.57 | 0.43 | 0.00 | 9.34 | 27.7/27.4 | 21.9/21.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.53 | 0.47 | 0.48 | 5.83 | 30.8/20.8 | 17.5/27.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.55 | 0.45 | 0.00 | 3.42 | 24.8/25.0 | 23.2/22.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 16 | 0.228 | 0.209 | +0.058 | +0.040 | $9.27 | FUNDED_RESEARCH | $3 | NYI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.160 | 0.146 | +0.033 | +0.019 | $4.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ goals YES | 16 | 0.202 | 0.188 | +0.032 | +0.018 | $4.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Kyle Palmieri: 1+ goals YES | 20 | 0.240 | 0.228 | +0.029 | +0.016 | $4.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes; why: higher confidence-adjusted growth (24.39 vs 6.89 bp); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: NYI offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (24.39 vs 6.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NYI offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (24.39 vs 5.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: NYI offense suppressed (<= 2 goals)
- **Kyle Palmieri: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (24.39 vs 3.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3175): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.4477): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS_BY_2PLUS (p 0.2276): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4667, phi -0.239)
- KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4667, phi -0.204)
- KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4667, phi -0.219)
- KXNHLGOAL-26OCT25NYIDAL-NYIKPALMIERI21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4667, phi -0.213)

portfolios: A EV +6.48 (adj +2.99) on $33.72, P(profit) 0.4348, adj growth 23.7 bp · B EV +5.63 (adj +3.58) on $21.95, P(profit) 0.4813, adj growth 31.7 bp · C EV +4.82 (adj +2.86) on $22.51, P(profit) 0.2276, adj growth 24.6 bp · R EV +1.03 (adj +0.71) on $3.00, P(profit) 0.2276, adj growth 24.0 bp

## MTL @ WPG  ·  10000 joint draws  ·  446 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.482 / away 0.518

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
| Dylan Samberg: 1+ goals YES | 4 | 0.061 | 0.053 | +0.018 | +0.011 | $1.97 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 29 | 0.335 | 0.321 | +0.031 | +0.017 | $5.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 18 | 0.212 | 0.203 | +0.021 | +0.012 | $3.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Dylan Samberg: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (5.81 vs 2.94 bp); despite a smaller raw edge (+0.018 vs +0.031/contract); relationships: KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26OCT25MTLWPG-WPGDSAMBERG54-1|yes; why: higher confidence-adjusted growth (2.94 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: WPG offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (2.12 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0016 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WPG:OFFENSE_4PLUS (p 0.3703): highest fidelity KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.3953): highest fidelity KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes (same contract)
- KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.116)
- KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.28)
- KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3782, phi -0.216)

portfolios: A EV +2.64 (adj +1.50) on $15.13, P(profit) 0.5135, adj growth 12.3 bp · B EV +1.71 (adj +0.97) on $10.20, P(profit) 0.5135, adj growth 8.6 bp · C EV +1.03 (adj +0.58) on $9.81, P(profit) 0.4808, adj growth 5.0 bp · R EV +0.43 (adj +0.25) on $1.00, P(profit) 0.061, adj growth 7.5 bp

## COL @ NSH  ·  10000 joint draws  ·  460 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.329 / away 0.671

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_COL_win | p_overtime | goals | shots NSH/COL | NSH/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.134 | 0.29 | 0.71 | 0.00 | 6.0 | 22.5/35.1 | 30.2/20.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.34 | 0.66 | 0.00 | 6.02 | 28.6/29.4 | 25.2/25.7 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.45 | 0.55 | 0.49 | 5.95 | 22.9/35.5 | 32.1/19.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.46 | 0.54 | 0.50 | 5.97 | 28.8/29.5 | 26.1/25.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.093 | 0.28 | 0.72 | 0.00 | 9.27 | 23.7/37.0 | 28.4/19.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.34 | 0.66 | 0.00 | 9.4 | 30.3/31.3 | 23.7/24.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins by over 2.5 goals NO | 66 | 0.730 | 0.693 | +0.054 | +0.017 | $10.72 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mavrik Bourque: 1+ assists NO | 80 | 0.869 | 0.825 | +0.058 | +0.013 | $16.74 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 1+ assists NO | 41 | 0.485 | 0.443 | +0.059 | +0.016 | $3.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
| Cale Makar: 1+ goals NO | 78 | 0.814 | 0.803 | +0.022 | +0.011 | $8.59 | FUNDED_RESEARCH | $3 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: higher confidence-adjusted growth (2.86 vs 2.73 bp); despite a smaller raw edge (+0.054 vs +0.058/contract); wins across more scripts (relative breadth 1.028 vs 0.892); relationships: KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.111); KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: REINFORCING (phi 0.204); KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.118); failure: COL wins by 2+
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT25COLNSH-4|no; why: higher confidence-adjusted growth (2.54 vs 0.11 bp); wins across more scripts (relative breadth 0.989 vs 0.359); alternative not eligible: confidence-adjusted EV +0.0022 below the 0.010/contract floor; relationships: KXNHLSPREAD-26OCT25COLNSH-COL3|no: INTENTIONAL_DIVERSIFIER (phi -0.111); KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: NSH offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25COLNSH-COL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25COLNSH-COL3|no has the higher standalone adjusted growth (2.86 vs 2.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.204); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25COLNSH-COL3|no: REINFORCING (phi 0.204); KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.147); failure: COL offense succeeds (4+ goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25COLNSH-COL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25COLNSH-COL3|no has the higher standalone adjusted growth (2.86 vs 1.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.118); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25COLNSH-COL3|no: MOSTLY_INDEPENDENT (phi 0.118); KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.147); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:TIGHT (p 0.4134): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no (same contract)
- thesis COL:SUPPRESSED (p 0.2954): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:SUPPRESSED (p 0.4625): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLSPREAD-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.395, phi -0.752)
- KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3215, phi -0.162)
- KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 27% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4983, phi -0.302)
- KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4983, phi -0.189)

portfolios: A EV +3.32 (adj +0.93) on $33.72, P(profit) 0.6094, adj growth 7.8 bp · B EV +2.84 (adj +0.81) on $40.02, P(profit) 0.6208, adj growth 7.3 bp · C EV +1.13 (adj +0.35) on $13.95, P(profit) 0.7302, adj growth 3.1 bp · R EV +0.33 (adj +0.12) on $6.00, P(profit) 0.6149, adj growth 4.1 bp

## MIN @ VAN  ·  10000 joint draws  ·  432 bet sides mapped, 27 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.369 / away 0.631

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
| Linus Karlsson: 1+ goals YES | 16 | 0.226 | 0.208 | +0.056 | +0.038 | $8.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.234 | 0.220 | +0.044 | +0.029 | $6.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Minnesota wins by over 1.5 goals NO | 58 | 0.739 | 0.632 | +0.141 | +0.035 | $12.80 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Matt Boldy: 1+ goals NO | 59 | 0.655 | 0.636 | +0.048 | +0.029 | $12.81 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: higher confidence-adjusted growth (22.53 vs 13.95 bp); despite a smaller raw edge (+0.056 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.92 vs 0.473); relationships: KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: MOSTLY_INDEPENDENT (phi 0.13); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (22.53 vs 11.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: MOSTLY_INDEPENDENT (phi 0.13); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: VAN offense suppressed (<= 2 goals)
- **Minnesota wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes has the higher standalone adjusted growth (13.95 vs 11.31 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.296); relationships: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.13); KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.13); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: REINFORCING (phi 0.181); failure: MIN wins by 2+
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes has the higher standalone adjusted growth (13.95 vs 7.75 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.158); relationships: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: REINFORCING (phi 0.181); failure: MIN offense succeeds (4+ goals)

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.4295): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.304): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- thesis VAN:WINS (p 0.5303): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3624, phi -0.202)
- KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3624, phi -0.205)
- KXNHLSPREAD-26OCT25MINVAN-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.4 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2614, phi -1.0)
- KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3921, phi -0.264)

portfolios: A EV +10.19 (adj +1.89) on $33.72, P(profit) 0.616, adj growth 15.1 bp · B EV +8.33 (adj +4.27) on $40.53, P(profit) 0.6762, adj growth 38.0 bp · C EV +6.35 (adj +3.36) on $15.91, P(profit) 0.3558, adj growth 28.9 bp · R EV +1.26 (adj +0.43) on $8.00, P(profit) 0.5214, adj growth 15.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
