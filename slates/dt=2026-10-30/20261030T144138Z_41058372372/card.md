# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T14:41:38Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 137.19 | +14.02 | +3.69 | +15.27 | 0.637 | -31.16 | -48.88 | 30.50 |
| B thesis-diversified (joint) ← optimiser card | 107.27 | +12.44 | +5.87 | +8.49 | 0.584 | -33.13 | -46.19 | 51.65 |
| C best expression per thesis | 60.80 | +5.14 | +2.18 | +7.59 | 0.605 | -22.45 | -34.22 | 19.54 |
| R FUNDED research stakes | 14.00 | +1.05 | +0.53 | +1.58 | 0.642 | -7.90 | -8.71 | 0.00 |

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
| Brayden McNabb: 1+ goals YES | 5 | 0.082 | 0.071 | +0.029 | +0.018 | $3.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 65 | 0.722 | 0.702 | +0.056 | +0.036 | $15.00 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 64 | 0.774 | 0.683 | +0.117 | +0.027 | $15.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Connor Brown: 1+ goals YES | 13 | 0.163 | 0.153 | +0.025 | +0.015 | $4.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30NJVGK-NJ3|no; why: higher confidence-adjusted growth (13.68 vs 1.63 bp); despite a smaller raw edge (+0.029 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0100 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VGK offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (13.15 vs 7.30 bp); despite a smaller raw edge (+0.056 vs +0.117/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.072); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NJD offense succeeds (4+ goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no has the higher standalone adjusted growth (13.15 vs 7.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.072); they share one thesis budget; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.072); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.036); failure: NJD offense succeeds (4+ goals)
- **Connor Brown: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT30NJVGK-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (4.21 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.036); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NJD:SUPPRESSED (p 0.4741): highest fidelity KXNHLGOAL-26OCT30NJVGK-NJTMEIER28-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3515): highest fidelity KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.4259): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3515, phi -0.127)
- KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3165, phi -0.238)
- KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.9 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3165, phi -0.242)
- KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4741, phi -0.199)

portfolios: A EV +7.01 (adj +1.70) on $50.00, P(profit) 0.6285, adj growth 15.0 bp · B EV +6.84 (adj +3.27) on $38.28, P(profit) 0.6605, adj growth 29.0 bp · C EV +2.65 (adj +1.23) on $26.21, P(profit) 0.7215, adj growth 11.2 bp · R EV +0.33 (adj +0.22) on $4.00, P(profit) 0.7215, adj growth 8.2 bp

## WPG @ FLA  ·  10000 joint draws  ·  406 bet sides mapped, 12 +EV candidates, 4 on card


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
| Alex Iafallo: 1+ goals YES | 11 | 0.152 | 0.139 | +0.035 | +0.022 | $5.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 55 | 0.640 | 0.593 | +0.073 | +0.025 | $11.87 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sam Reinhart: 1+ goals NO | 64 | 0.696 | 0.678 | +0.040 | +0.022 | $13.59 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Elias Salomonsson: 1+ assists NO | 75 | 0.809 | 0.777 | +0.046 | +0.014 | $18.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: higher confidence-adjusted growth (10.06 vs 5.75 bp); despite a smaller raw edge (+0.035 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: MOSTLY_INDEPENDENT (phi 0.127); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: WPG offense suppressed (<= 2 goals)
- **Florida wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA3|no; why: higher confidence-adjusted growth (5.75 vs 2.75 bp); relationships: KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.127); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: REINFORCING (phi 0.217); KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: INTENTIONAL_DIVERSIFIER (phi -0.116); failure: FLA wins by 2+
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no has the higher standalone adjusted growth (5.75 vs 4.76 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.217); they share one thesis budget; relationships: KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: REINFORCING (phi 0.217); KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: FLA offense succeeds (4+ goals)
- **Elias Salomonsson: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT30WPGFLA-WPGESALOMONSSON57-1|no; why: higher confidence-adjusted growth (2.31 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: INTENTIONAL_DIVERSIFIER (phi -0.116); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.3135): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4331): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no (same contract)
- thesis FLA:SUPPRESSED (p 0.3396): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4714, phi -0.187)
- KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3596, phi -1.0)
- KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4409, phi -0.264)
- KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3135, phi -0.181)

portfolios: A EV +5.98 (adj +1.47) on $50.00, P(profit) 0.6311, adj growth 11.5 bp · B EV +5.07 (adj +2.33) on $49.60, P(profit) 0.4641, adj growth 20.3 bp · C EV +1.96 (adj +0.68) on $15.20, P(profit) 0.6404, adj growth 6.0 bp · R EV +0.63 (adj +0.27) on $7.00, P(profit) 0.4937, adj growth 9.4 bp

## SEA @ CGY  ·  10000 joint draws  ·  444 bet sides mapped, 2 +EV candidates, 2 on card


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
| Bobby McMann: 1+ goals NO | 70 | 0.735 | 0.725 | +0.021 | +0.010 | $9.33 | FUNDED_RESEARCH | $3 | SEA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Matvei Gridin: 1+ goals NO | 73 | 0.763 | 0.754 | +0.020 | +0.010 | $10.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Bobby McMann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT30SEACGY-SEAVDUNN29-1|no; why: higher confidence-adjusted growth (1.18 vs 0.00 bp); despite a smaller raw edge (+0.021 vs +0.022/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30SEACGY-CGYMGRIDIN92-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: SEA offense succeeds (4+ goals)
- **Matvei Gridin: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30SEACGY-CGYMCORONATO27-1|no; why: higher confidence-adjusted growth (1.17 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0008 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT30SEACGY-SEABMCMANN74-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: CGY offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:SUPPRESSED (p 0.3685): highest fidelity KXNHLGOAL-26OCT30SEACGY-SEABMCMANN74-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT30SEACGY-SEABMCMANN74-1|no (same contract)
- thesis CGY:SUPPRESSED (p 0.4006): highest fidelity KXNHLGOAL-26OCT30SEACGY-CGYMGRIDIN92-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT30SEACGY-CGYMGRIDIN92-1|no (same contract)
- KXNHLGOAL-26OCT30SEACGY-SEABMCMANN74-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.4077, phi -0.222)
- KXNHLGOAL-26OCT30SEACGY-CGYMGRIDIN92-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.3836, phi -0.214)

portfolios: A EV +1.02 (adj +0.52) on $37.19, P(profit) 0.5618, adj growth 4.0 bp · B EV +0.53 (adj +0.27) on $19.39, P(profit) 0.5618, adj growth 2.4 bp · C EV +0.53 (adj +0.27) on $19.39, P(profit) 0.5618, adj growth 2.4 bp · R EV +0.09 (adj +0.04) on $3.00, P(profit) 0.7352, adj growth 1.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
