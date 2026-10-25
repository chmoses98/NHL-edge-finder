# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T18:44:18Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +30.26 | +9.56 | +26.98 | 0.676 | -44.18 | -61.67 | 77.81 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +24.73 | +14.81 | +21.86 | 0.653 | -44.95 | -58.60 | 133.38 |
| C best expression per thesis | 133.91 | +23.43 | +12.54 | +20.40 | 0.641 | -44.56 | -61.48 | 110.31 |
| R FUNDED research stakes | 21.00 | +3.05 | +1.89 | +0.71 | 0.521 | -10.02 | -10.63 | 0.00 |

## FLA @ CHI  ·  10000 joint draws  ·  448 bet sides mapped, 26 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.375 / away 0.625

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_FLA_win | p_overtime | goals | shots CHI/FLA | CHI/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.47 | 0.53 | 0.00 | 5.97 | 26.1/26.5 | 23.1/22.7 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.107 | 0.42 | 0.58 | 0.00 | 5.97 | 20.8/32.4 | 28.3/17.7 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.47 | 0.53 | 0.49 | 5.95 | 21.1/32.1 | 28.6/17.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.51 | 0.49 | 0.47 | 5.92 | 26.5/27.0 | 23.8/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.49 | 0.51 | 0.00 | 9.2 | 27.8/28.3 | 22.2/21.9 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.070 | 0.41 | 0.59 | 0.00 | 9.27 | 22.4/33.9 | 26.9/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 65 | 0.737 | 0.714 | +0.071 | +0.048 | $12.57 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 61 | 0.696 | 0.673 | +0.070 | +0.047 | $12.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 23 | 0.292 | 0.276 | +0.050 | +0.033 | $7.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 10 | 0.148 | 0.127 | +0.042 | +0.021 | $3.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (23.21 vs 20.63 bp); relationships: KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: FLA offense succeeds (4+ goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no has the higher standalone adjusted growth (23.21 vs 20.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: FLA offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25FLACHI-FLA3|no; why: higher confidence-adjusted growth (12.95 vs 8.07 bp); despite a smaller raw edge (+0.050 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: CHI offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT25FLACHI-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (9.83 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, FLA shot control · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis FLA:SUPPRESSED (p 0.3847): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.3677): highest fidelity KXNHLTEAMTOTAL-26OCT25FLACHI-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:OFFENSE_4PLUS (p 0.3984): highest fidelity KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes (same contract)
- KXNHLGOAL-26OCT25FLACHI-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3984, phi -0.247)
- KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3984, phi -0.232)
- KXNHLGOAL-26OCT25FLACHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4101, phi -0.266)
- KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3847, phi -0.193)

portfolios: A EV +6.78 (adj +1.04) on $32.11, P(profit) 0.6441, adj growth 7.9 bp · B EV +5.79 (adj +3.63) on $36.55, P(profit) 0.6801, adj growth 33.7 bp · C EV +7.45 (adj +4.12) on $50.00, P(profit) 0.7438, adj growth 37.2 bp · R EV +0.43 (adj +0.29) on $4.00, P(profit) 0.7374, adj growth 11.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT25FLACHI-FLA|no == KXNHLGAME-26OCT25FLACHI-CHI|yes

## NYI @ DAL  ·  10000 joint draws  ·  438 bet sides mapped, 17 +EV candidates, 4 on card

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
| Brayden Schenn: 1+ goals YES | 16 | 0.228 | 0.209 | +0.058 | +0.040 | $9.33 | FUNDED_RESEARCH | $3 | NYI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.160 | 0.146 | +0.033 | +0.019 | $4.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ goals YES | 16 | 0.202 | 0.188 | +0.032 | +0.018 | $4.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| David Perron: 1+ goals YES | 13 | 0.163 | 0.154 | +0.025 | +0.016 | $3.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes; why: higher confidence-adjusted growth (24.39 vs 6.89 bp); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT25NYIDAL-DALDPERRON57-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: NYI offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (24.39 vs 6.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT25NYIDAL-DALDPERRON57-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: NYI offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (24.39 vs 5.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT25NYIDAL-DALDPERRON57-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: NYI offense suppressed (<= 2 goals)
- **David Perron: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT25NYIDAL-9|yes; why: higher confidence-adjusted growth (4.55 vs 1.07 bp); despite a smaller raw edge (+0.025 vs +0.028/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.919 vs 0.354); alternative not eligible: confidence-adjusted EV +0.0076 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3175): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.4477): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS_BY_2PLUS (p 0.2276): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4667, phi -0.239)
- KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4667, phi -0.204)
- KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4667, phi -0.219)
- KXNHLGOAL-26OCT25NYIDAL-DALDPERRON57-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3863, phi -0.196)

portfolios: A EV +6.17 (adj +2.84) on $32.11, P(profit) 0.4348, adj growth 22.9 bp · B EV +5.78 (adj +3.71) on $21.58, P(profit) 0.5709, adj growth 32.8 bp · C EV +4.82 (adj +2.86) on $22.51, P(profit) 0.2276, adj growth 24.6 bp · R EV +1.03 (adj +0.71) on $3.00, P(profit) 0.2276, adj growth 24.0 bp

## MTL @ WPG  ·  10000 joint draws  ·  446 bet sides mapped, 6 +EV candidates, 4 on card

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
| Alexandre Carrier: 1+ goals YES | 4 | 0.068 | 0.058 | +0.025 | +0.016 | $2.79 | FUNDED_RESEARCH | $1 | MTL:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Dylan Samberg: 1+ goals YES | 4 | 0.061 | 0.053 | +0.018 | +0.011 | $1.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 29 | 0.335 | 0.323 | +0.031 | +0.018 | $5.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
| Phillip Danault: 1+ goals YES | 11 | 0.141 | 0.129 | +0.024 | +0.012 | $2.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Alexandre Carrier: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes; why: higher confidence-adjusted growth (12.50 vs 2.12 bp); relationships: KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT25MTLWPG-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: MTL offense suppressed (<= 2 goals)
- **Dylan Samberg: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (5.81 vs 3.39 bp); despite a smaller raw edge (+0.018 vs +0.031/contract); relationships: KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MTLWPG-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26OCT25MTLWPG-WPGDSAMBERG54-1|yes; why: higher confidence-adjusted growth (3.39 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MTLWPG-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: WPG offense suppressed (<= 2 goals)
- **Phillip Danault: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes; why: higher confidence-adjusted growth (3.24 vs 2.12 bp); relationships: KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WPG:OFFENSE_4PLUS (p 0.3703): highest fidelity KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.3953): highest fidelity KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes (same contract)
- KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3782, phi -0.108)
- KXNHLGOAL-26OCT25MTLWPG-WPGDSAMBERG54-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.116)
- KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.28)
- KXNHLGOAL-26OCT25MTLWPG-MTLPDANAULT24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3782, phi -0.183)

portfolios: A EV +5.43 (adj +2.93) on $21.55, P(profit) 0.5546, adj growth 23.6 bp · B EV +3.55 (adj +2.10) on $12.70, P(profit) 0.4983, adj growth 18.5 bp · C EV +1.08 (adj +0.63) on $10.27, P(profit) 0.4808, adj growth 5.5 bp · R EV +0.59 (adj +0.37) on $1.00, P(profit) 0.0677, adj growth 12.0 bp

## COL @ NSH  ·  10000 joint draws  ·  464 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.325 / away 0.675

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_COL_win | p_overtime | goals | shots NSH/COL | NSH/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.127 | 0.28 | 0.72 | 0.00 | 6.03 | 22.7/35.2 | 30.1/20.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.34 | 0.66 | 0.00 | 6.0 | 28.6/29.3 | 25.0/25.7 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.45 | 0.55 | 0.46 | 5.87 | 23.1/35.6 | 32.1/19.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.46 | 0.54 | 0.48 | 5.95 | 28.7/29.4 | 26.1/25.3 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.095 | 0.27 | 0.73 | 0.00 | 9.29 | 24.2/37.0 | 28.1/19.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.35 | 0.65 | 0.00 | 9.23 | 30.0/30.8 | 23.8/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mavrik Bourque: 1+ assists NO | 79 | 0.866 | 0.821 | +0.065 | +0.019 | $15.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Taylor Makar: 1+ goals NO | 91 | 0.937 | 0.928 | +0.021 | +0.012 | $15.07 | FUNDED_RESEARCH | $4 | COL:SUPPRESSED | DIRECT (0.98) | EVIDENCE_STRONGER | D |
| Colorado wins by over 1.5 goals NO | 53 | 0.609 | 0.567 | +0.062 | +0.020 | $5.26 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 66 | 0.732 | 0.694 | +0.057 | +0.018 | $6.49 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT25COLNSH-4|no; why: higher confidence-adjusted growth (5.00 vs 0.04 bp); wins across more scripts (relative breadth 0.998 vs 0.365); alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT25COLNSH-COLTMAKAR16-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT25COLNSH-COL2|no: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLSPREAD-26OCT25COLNSH-COL3|no: INTENTIONAL_DIVERSIFIER (phi -0.092); failure: NSH offense succeeds (4+ goals)
- **Taylor Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (4.05 vs 3.92 bp); despite a smaller raw edge (+0.021 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT25COLNSH-COL2|no: MOSTLY_INDEPENDENT (phi 0.087); KXNHLSPREAD-26OCT25COLNSH-COL3|no: MOSTLY_INDEPENDENT (phi 0.084); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL3|no; why: higher confidence-adjusted growth (3.38 vs 3.24 bp); relationships: KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLGOAL-26OCT25COLNSH-COLTMAKAR16-1|no: MOSTLY_INDEPENDENT (phi 0.087); KXNHLSPREAD-26OCT25COLNSH-COL3|no: DUPLICATIVE (phi 0.754); failure: COL wins by 2+
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: Broad expression KXNHLSPREAD-26OCT25COLNSH-COL3|no selected over player prop KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.092); KXNHLGOAL-26OCT25COLNSH-COLTMAKAR16-1|no: MOSTLY_INDEPENDENT (phi 0.084); KXNHLSPREAD-26OCT25COLNSH-COL2|no: DUPLICATIVE (phi 0.754); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:SUPPRESSED (p 0.3001): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no — Broad expression KXNHLSPREAD-26OCT25COLNSH-COL3|no selected over player prop KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:TIGHT (p 0.4215): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no (same contract)
- thesis NSH:SUPPRESSED (p 0.4609): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3199, phi -0.162)
- KXNHLGOAL-26OCT25COLNSH-COLTMAKAR16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4914, phi -0.116)
- KXNHLSPREAD-26OCT25COLNSH-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.391, phi -1.0)
- KXNHLSPREAD-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.391, phi -0.754)
- override: Broad expression KXNHLSPREAD-26OCT25COLNSH-COL3|no selected over player prop KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.52 (adj +1.09) on $32.11, P(profit) 0.6142, adj growth 9.5 bp · B EV +2.70 (adj +0.91) on $41.90, P(profit) 0.589, adj growth 8.5 bp · C EV +2.22 (adj +0.69) on $16.48, P(profit) 0.4958, adj growth 6.0 bp · R EV +0.48 (adj +0.18) on $8.00, P(profit) 0.5809, adj growth 6.2 bp

## MIN @ VAN  ·  10000 joint draws  ·  432 bet sides mapped, 23 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.368 / away 0.632

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_MIN_win | p_overtime | goals | shots VAN/MIN | VAN/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| MIN shot control · normal event (5-7) · decided (2+) | 0.117 | 0.50 | 0.50 | 0.00 | 6.01 | 22.0/34.4 | 30.5/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.56 | 0.44 | 0.00 | 6.08 | 27.8/28.5 | 25.1/24.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.47 | 0.53 | 0.45 | 5.9 | 22.4/34.4 | 30.9/19.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.54 | 0.46 | 0.47 | 5.98 | 27.9/28.7 | 25.5/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.57 | 0.43 | 0.00 | 9.41 | 29.4/30.3 | 24.4/23.0 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.084 | 0.48 | 0.52 | 0.00 | 9.26 | 23.9/35.8 | 29.3/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Linus Karlsson: 1+ goals YES | 16 | 0.224 | 0.204 | +0.054 | +0.035 | $7.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Matt Boldy: 1+ goals NO | 58 | 0.659 | 0.638 | +0.062 | +0.041 | $16.76 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.232 | 0.217 | +0.041 | +0.027 | $6.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ goals YES | 19 | 0.241 | 0.226 | +0.040 | +0.025 | $6.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: higher confidence-adjusted growth (18.20 vs 14.00 bp); despite a smaller raw edge (+0.054 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.889 vs 0.466); relationships: KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT25MINVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: VAN offense suppressed (<= 2 goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: higher confidence-adjusted growth (15.48 vs 14.00 bp); despite a smaller raw edge (+0.062 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.995 vs 0.466); relationships: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT25MINVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: MIN offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (18.20 vs 10.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT25MINVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (18.20 vs 8.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4186): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3975): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.3031): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3594, phi -0.202)
- KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.264)
- KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3594, phi -0.199)
- KXNHLGOAL-26OCT25MINVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3594, phi -0.23)

portfolios: A EV +8.36 (adj +1.66) on $32.11, P(profit) 0.6469, adj growth 13.9 bp · B EV +6.91 (adj +4.46) on $37.27, P(profit) 0.4548, adj growth 39.8 bp · C EV +7.87 (adj +4.24) on $34.65, P(profit) 0.3852, adj growth 37.0 bp · R EV +0.52 (adj +0.34) on $5.00, P(profit) 0.6593, adj growth 12.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT25MINVAN-VAN|yes == KXNHLGAME-26OCT25MINVAN-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
