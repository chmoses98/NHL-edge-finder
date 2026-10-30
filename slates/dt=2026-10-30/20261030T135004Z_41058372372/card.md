# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T13:50:04Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 132.94 | +15.73 | +4.79 | +15.20 | 0.617 | -40.07 | -49.85 | 39.06 |
| B thesis-diversified (joint) ← optimiser card | 89.02 | +12.04 | +6.23 | +10.21 | 0.581 | -36.27 | -45.95 | 54.46 |
| C best expression per thesis | 53.26 | +5.15 | +2.13 | +5.45 | 0.670 | -24.58 | -38.15 | 19.11 |
| R FUNDED research stakes | 16.00 | +1.26 | +0.62 | +1.64 | 0.654 | -5.87 | -9.90 | 0.00 |

## NJD @ VGK  ·  10000 joint draws  ·  436 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_NJD_win | p_overtime | goals | shots VGK/NJD | VGK/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.134 | 0.62 | 0.38 | 0.00 | 6.0 | 27.5/27.7 | 24.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.48 | 5.93 | 27.7/27.9 | 24.6/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.65 | 0.35 | 0.00 | 9.2 | 29.0/29.0 | 23.9/22.0 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.072 | 0.56 | 0.44 | 0.00 | 5.96 | 22.0/32.5 | 29.2/18.5 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.51 | 0.49 | 0.49 | 5.87 | 22.2/32.9 | 29.6/19.0 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.065 | 0.66 | 0.34 | 0.00 | 5.96 | 32.2/22.1 | 19.3/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Hughes: 1+ goals NO | 65 | 0.722 | 0.702 | +0.056 | +0.036 | $20.00 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Brayden McNabb: 1+ goals YES | 5 | 0.082 | 0.070 | +0.029 | +0.017 | $3.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Amadeus Lombardi: 1+ goals YES | 11 | 0.136 | 0.127 | +0.019 | +0.010 | $2.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ assists NO | 51 | 0.611 | 0.542 | +0.083 | +0.014 | $8.86 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (13.15 vs 3.05 bp); despite a smaller raw edge (+0.056 vs +0.108/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT30NJVGK-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30NJVGK-NJ3|no; why: higher confidence-adjusted growth (11.89 vs 1.63 bp); despite a smaller raw edge (+0.029 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0100 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT30NJVGK-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.051); failure: VGK offense suppressed (<= 2 goals)
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT30NJVGK-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (2.26 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: NJD offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT30NJVGK-VGKMSTONE61-1|no; why: higher confidence-adjusted growth (1.83 vs 0.83 bp); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT30NJVGK-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NJD:SUPPRESSED (p 0.4741): highest fidelity KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3515): highest fidelity KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.4259): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3165, phi -0.238)
- KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3515, phi -0.127)
- KXNHLGOAL-26OCT30NJVGK-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4741, phi -0.183)
- KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.6 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4259, phi -0.289)

portfolios: A EV +6.80 (adj +1.58) on $50.00, P(profit) 0.6285, adj growth 13.8 bp · B EV +5.53 (adj +2.77) on $35.40, P(profit) 0.5475, adj growth 24.4 bp · C EV +2.92 (adj +1.31) on $27.97, P(profit) 0.7215, adj growth 11.9 bp · R EV +0.42 (adj +0.27) on $5.00, P(profit) 0.7215, adj growth 10.0 bp

## WPG @ FLA  ·  10000 joint draws  ·  400 bet sides mapped, 14 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_WPG_win | p_overtime | goals | shots FLA/WPG | FLA/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.64 | 0.36 | 0.00 | 5.99 | 26.9/26.8 | 23.8/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.46 | 5.92 | 27.1/26.8 | 23.5/23.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.099 | 0.70 | 0.30 | 0.00 | 5.98 | 31.7/21.0 | 18.4/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.62 | 0.38 | 0.00 | 9.21 | 28.6/28.1 | 22.9/21.9 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.58 | 0.42 | 0.49 | 5.93 | 31.9/21.4 | 18.3/28.4 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.060 | 0.69 | 0.31 | 0.00 | 9.25 | 33.6/22.4 | 17.7/25.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Iafallo: 1+ goals YES | 11 | 0.152 | 0.139 | +0.035 | +0.022 | $5.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 55 | 0.640 | 0.593 | +0.073 | +0.025 | $13.00 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sam Reinhart: 1+ goals NO | 64 | 0.696 | 0.678 | +0.040 | +0.022 | $13.42 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 11 | 0.141 | 0.131 | +0.025 | +0.014 | $4.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: higher confidence-adjusted growth (10.06 vs 5.75 bp); despite a smaller raw edge (+0.035 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: MOSTLY_INDEPENDENT (phi 0.127); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT30WPGFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: WPG offense suppressed (<= 2 goals)
- **Florida wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA3|no; why: higher confidence-adjusted growth (5.75 vs 2.75 bp); relationships: KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.127); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: REINFORCING (phi 0.217); KXNHLGOAL-26OCT30WPGFLA-FLACSCHWINDT79-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.18); failure: FLA wins by 2+
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no has the higher standalone adjusted growth (5.75 vs 4.76 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.217); they share one thesis budget; relationships: KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: REINFORCING (phi 0.217); KXNHLGOAL-26OCT30WPGFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT30WPGFLA-3|yes; why: higher confidence-adjusted growth (4.22 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: INTENTIONAL_DIVERSIFIER (phi -0.18); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.3135): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.3396): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4331): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no (same contract)
- KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4714, phi -0.187)
- KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3596, phi -1.0)
- KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4409, phi -0.264)
- KXNHLGOAL-26OCT30WPGFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3396, phi -0.18)

portfolios: A EV +6.24 (adj +1.62) on $50.00, P(profit) 0.6311, adj growth 13.0 bp · B EV +5.01 (adj +2.57) on $36.17, P(profit) 0.6401, adj growth 22.3 bp · C EV +1.96 (adj +0.68) on $15.20, P(profit) 0.6404, adj growth 6.0 bp · R EV +0.76 (adj +0.31) on $8.00, P(profit) 0.4937, adj growth 10.7 bp

## SEA @ CGY  ·  10000 joint draws  ·  428 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_SEA_win | p_overtime | goals | shots CGY/SEA | CGY/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.47 | 0.53 | 0.00 | 6.05 | 28.7/28.4 | 24.6/25.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.48 | 0.52 | 0.45 | 5.93 | 28.7/28.6 | 25.3/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.45 | 0.55 | 0.00 | 9.26 | 30.4/30.0 | 23.5/24.2 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.088 | 0.53 | 0.47 | 0.00 | 5.97 | 33.8/22.8 | 19.5/30.1 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.49 | 0.51 | 0.45 | 5.97 | 34.0/23.0 | 19.8/30.7 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.061 | 0.55 | 0.45 | 0.00 | 9.3 | 35.4/24.0 | 18.4/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 12 | 0.153 | 0.144 | +0.026 | +0.016 | $4.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 18 | 0.211 | 0.202 | +0.020 | +0.011 | $3.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Matvei Gridin: 1+ goals NO | 73 | 0.763 | 0.754 | +0.020 | +0.010 | $9.69 | FUNDED_RESEARCH | $3 | CGY:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT30SEACGY-SEABMONTOUR62-1|yes; why: higher confidence-adjusted growth (5.18 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT30SEACGY-CGYMGRIDIN92-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT30SEACGY-SEABMONTOUR62-1|yes; why: higher confidence-adjusted growth (1.85 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT30SEACGY-CGYMGRIDIN92-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: SEA offense suppressed (<= 2 goals)
- **Matvei Gridin: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHL3PTOTAL-26OCT30SEACGY-2|no; why: higher confidence-adjusted growth (1.17 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: CGY offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CGY:SUPPRESSED (p 0.4006): highest fidelity KXNHLGOAL-26OCT30SEACGY-CGYMGRIDIN92-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT30SEACGY-CGYMGRIDIN92-1|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.4077): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3685, phi -0.188)
- KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3685, phi -0.193)
- KXNHLGOAL-26OCT30SEACGY-CGYMGRIDIN92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.3836, phi -0.214)

portfolios: A EV +2.69 (adj +1.59) on $32.94, P(profit) 0.3317, adj growth 12.2 bp · B EV +1.51 (adj +0.89) on $17.45, P(profit) 0.3317, adj growth 7.8 bp · C EV +0.27 (adj +0.14) on $10.09, P(profit) 0.7635, adj growth 1.2 bp · R EV +0.08 (adj +0.04) on $3.00, P(profit) 0.7635, adj growth 1.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
