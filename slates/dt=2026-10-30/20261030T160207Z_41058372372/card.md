# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T16:02:07Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 124.25 | +13.19 | +4.37 | +18.54 | 0.660 | -37.70 | -45.50 | 37.11 |
| B thesis-diversified (joint) ← optimiser card | 99.52 | +12.62 | +6.42 | +10.24 | 0.609 | -30.79 | -41.22 | 57.35 |
| C best expression per thesis | 96.79 | +8.31 | +3.86 | +10.07 | 0.667 | -28.27 | -41.54 | 34.85 |
| R FUNDED research stakes | 12.00 | +1.02 | +0.66 | +0.44 | 0.629 | -5.99 | -7.80 | 0.00 |

## NJD @ VGK  ·  10000 joint draws  ·  436 bet sides mapped, 11 +EV candidates, 4 on card


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
| Jack Hughes: 1+ goals NO | 65 | 0.722 | 0.702 | +0.056 | +0.036 | $15.00 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Brayden McNabb: 1+ goals YES | 5 | 0.082 | 0.070 | +0.029 | +0.017 | $3.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 64 | 0.774 | 0.683 | +0.117 | +0.027 | $15.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Connor Brown: 1+ goals YES | 13 | 0.163 | 0.153 | +0.025 | +0.015 | $4.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (13.15 vs 7.30 bp); despite a smaller raw edge (+0.056 vs +0.117/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.072); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NJD offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30NJVGK-NJ2|no; why: higher confidence-adjusted growth (11.89 vs 1.87 bp); despite a smaller raw edge (+0.029 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VGK offense suppressed (<= 2 goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no has the higher standalone adjusted growth (13.15 vs 7.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.072); they share one thesis budget; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.072); KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.036); failure: NJD offense succeeds (4+ goals)
- **Connor Brown: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT30NJVGK-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (4.21 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.033/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.036); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NJD:SUPPRESSED (p 0.4741): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:WINS (p 0.5832): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:OFFENSE_4PLUS (p 0.4259): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ2|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT30NJVGK-NJ2|no (same contract)
- KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3165, phi -0.238)
- KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3515, phi -0.127)
- KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.9 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3165, phi -0.242)
- KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4741, phi -0.199)

portfolios: A EV +7.01 (adj +1.77) on $50.00, P(profit) 0.6285, adj growth 15.7 bp · B EV +6.66 (adj +3.07) on $37.93, P(profit) 0.6605, adj growth 27.3 bp · C EV +3.53 (adj +1.45) on $39.09, P(profit) 0.692, adj growth 13.1 bp · R EV +0.33 (adj +0.22) on $4.00, P(profit) 0.7215, adj growth 8.2 bp

## WPG @ FLA  ·  10000 joint draws  ·  408 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_WPG_win | p_overtime | goals | shots FLA/WPG | FLA/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.65 | 0.35 | 0.00 | 6.01 | 26.9/26.7 | 23.8/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.54 | 0.46 | 0.49 | 5.94 | 26.9/26.7 | 23.5/23.5 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.103 | 0.68 | 0.32 | 0.00 | 6.01 | 31.9/21.1 | 18.5/27.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.61 | 0.39 | 0.00 | 9.3 | 28.8/28.3 | 22.9/21.8 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.57 | 0.43 | 0.47 | 5.94 | 32.4/21.5 | 18.2/29.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.57 | 0.43 | 0.00 | 3.46 | 25.5/25.3 | 23.6/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 59 | 0.679 | 0.656 | +0.072 | +0.049 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 11 | 0.149 | 0.137 | +0.032 | +0.020 | $5.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Elias Salomonsson: 1+ assists NO | 75 | 0.810 | 0.777 | +0.047 | +0.014 | $19.59 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Mark Scheifele: 1+ goals YES | 28 | 0.315 | 0.305 | +0.021 | +0.011 | $4.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (22.02 vs 6.02 bp); relationships: KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT30WPGFLA-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: FLA offense succeeds (4+ goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: higher confidence-adjusted growth (8.19 vs 2.99 bp); despite a smaller raw edge (+0.032 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26OCT30WPGFLA-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: WPG offense suppressed (<= 2 goals)
- **Elias Salomonsson: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT30WPGFLA-WPGESALOMONSSON57-1|no; why: higher confidence-adjusted growth (2.48 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26OCT30WPGFLA-WPGMSCHEIFELE55-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); failure: WPG offense succeeds (4+ goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no has the higher standalone adjusted growth (2.99 vs 1.31 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.175); relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis FLA:SUPPRESSED (p 0.3408): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3124): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4253): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no (same contract)
- KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4462, phi -0.229)
- KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4761, phi -0.193)
- KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3124, phi -0.223)
- KXNHLGOAL-26OCT30WPGFLA-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4761, phi -0.276)

portfolios: A EV +4.99 (adj +2.00) on $50.00, P(profit) 0.632, adj growth 17.0 bp · B EV +5.38 (adj +3.06) on $49.37, P(profit) 0.6189, adj growth 27.5 bp · C EV +4.51 (adj +2.27) on $48.34, P(profit) 0.6561, adj growth 20.6 bp · R EV +0.60 (adj +0.40) on $5.00, P(profit) 0.6794, adj growth 14.9 bp

## SEA @ CGY  ·  10000 joint draws  ·  446 bet sides mapped, 2 +EV candidates, 2 on card


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
| Berkly Catton: 1+ goals YES | 18 | 0.211 | 0.201 | +0.020 | +0.010 | $2.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Bobby McMann: 1+ goals NO | 70 | 0.735 | 0.725 | +0.021 | +0.010 | $9.23 | FUNDED_RESEARCH | $3 | SEA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT30SEACGY-SEABMONTOUR62-1|yes; why: higher confidence-adjusted growth (1.47 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30SEACGY-SEABMCMANN74-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: SEA offense suppressed (<= 2 goals)
- **Bobby McMann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT30SEACGY-SEAVDUNN29-1|no; why: higher confidence-adjusted growth (1.18 vs 0.00 bp); despite a smaller raw edge (+0.021 vs +0.022/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: SEA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:SUPPRESSED (p 0.3685): highest fidelity KXNHLGOAL-26OCT30SEACGY-SEABMCMANN74-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT30SEACGY-SEABMCMANN74-1|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.4077): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3685, phi -0.193)
- KXNHLGOAL-26OCT30SEACGY-SEABMCMANN74-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.4077, phi -0.222)

portfolios: A EV +1.19 (adj +0.60) on $24.25, P(profit) 0.7887, adj growth 4.5 bp · B EV +0.58 (adj +0.29) on $12.22, P(profit) 0.7887, adj growth 2.6 bp · C EV +0.27 (adj +0.14) on $9.36, P(profit) 0.7352, adj growth 1.2 bp · R EV +0.09 (adj +0.04) on $3.00, P(profit) 0.7352, adj growth 1.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
