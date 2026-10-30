# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T17:43:35Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 108.37 | +15.93 | +5.15 | +18.73 | 0.590 | -26.78 | -46.27 | 43.62 |
| B thesis-diversified (joint) ← optimiser card | 91.27 | +9.16 | +5.55 | +9.47 | 0.571 | -30.80 | -42.11 | 50.44 |
| C best expression per thesis | 91.07 | +8.65 | +4.04 | +9.03 | 0.641 | -27.89 | -36.42 | 37.02 |
| R FUNDED research stakes | 11.00 | +1.35 | +0.89 | +3.10 | 0.573 | -4.41 | -11.00 | 0.00 |

## NJD @ VGK  ·  10000 joint draws  ·  448 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.507 / away 0.493

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
| Jack Hughes: 1+ goals NO | 65 | 0.722 | 0.702 | +0.056 | +0.036 | $17.28 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Connor Brown: 1+ goals YES | 13 | 0.163 | 0.153 | +0.025 | +0.015 | $4.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ goals YES | 20 | 0.236 | 0.226 | +0.025 | +0.015 | $4.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 76 | 0.796 | 0.786 | +0.024 | +0.013 | $12.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (13.15 vs 5.73 bp); despite a smaller raw edge (+0.056 vs +0.108/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT30NJVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT30NJVGK-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: NJD offense succeeds (4+ goals)
- **Connor Brown: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT30NJVGK-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (4.21 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.043/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT30NJVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT30NJVGK-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: NJD offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30NJVGK-NJ2|no; why: higher confidence-adjusted growth (2.88 vs 1.87 bp); despite a smaller raw edge (+0.025 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT30NJVGK-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: VGK offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT30NJVGK-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT30NJVGK-NJJBRATT63-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.90 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT30NJVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NJD:SUPPRESSED (p 0.4741): highest fidelity KXNHLAST-26OCT30NJVGK-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT30NJVGK-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT30NJVGK-NJJBRATT63-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.90 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VGK:WINS (p 0.5832): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3515): highest fidelity KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no (same contract)
- KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3165, phi -0.238)
- KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4741, phi -0.199)
- KXNHLGOAL-26OCT30NJVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3515, phi -0.21)
- KXNHLGOAL-26OCT30NJVGK-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3165, phi -0.224)
- override: Player prop expression KXNHLGOAL-26OCT30NJVGK-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT30NJVGK-NJJBRATT63-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.90 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.37 (adj +1.54) on $50.00, P(profit) 0.6026, adj growth 13.1 bp · B EV +3.09 (adj +1.93) on $38.51, P(profit) 0.669, adj growth 17.4 bp · C EV +4.05 (adj +1.56) on $41.41, P(profit) 0.692, adj growth 14.1 bp · R EV +0.42 (adj +0.27) on $5.00, P(profit) 0.7215, adj growth 10.0 bp

## WPG @ FLA  ·  10000 joint draws  ·  408 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.667 / away 0.333

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
| Brady Tkachuk: 1+ goals NO | 59 | 0.679 | 0.656 | +0.072 | +0.049 | $15.00 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 63 | 0.698 | 0.678 | +0.052 | +0.032 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 11 | 0.149 | 0.137 | +0.032 | +0.020 | $3.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Elias Salomonsson: 1+ assists NO | 75 | 0.810 | 0.777 | +0.047 | +0.014 | $13.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (22.02 vs 9.96 bp); relationships: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense succeeds (4+ goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no; why: Player prop expression KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT30WPGFLA-FLASREINHART13-1|no because adjusted EV is 1.0 pts higher while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: FLA offense succeeds (4+ goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: higher confidence-adjusted growth (8.19 vs 4.79 bp); despite a smaller raw edge (+0.032 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); failure: WPG offense suppressed (<= 2 goals)
- **Elias Salomonsson: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT30WPGFLA-WPGESALOMONSSON57-1|no; why: higher confidence-adjusted growth (2.48 vs 0.00 bp); despite a smaller raw edge (+0.047 vs +0.065/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis FLA:SUPPRESSED (p 0.3408): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no — Player prop expression KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT30WPGFLA-FLASREINHART13-1|no because adjusted EV is 1.0 pts higher while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WPG:WINS (p 0.411): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3124): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4462, phi -0.229)
- KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4462, phi -0.251)
- KXNHLGOAL-26OCT30WPGFLA-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4761, phi -0.193)
- KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3124, phi -0.223)
- override: Player prop expression KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT30WPGFLA-FLASREINHART13-1|no because adjusted EV is 1.0 pts higher while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.63 (adj +2.37) on $50.00, P(profit) 0.5744, adj growth 20.9 bp · B EV +4.91 (adj +2.88) on $47.72, P(profit) 0.5458, adj growth 26.6 bp · C EV +4.61 (adj +2.48) on $49.66, P(profit) 0.6475, adj growth 22.9 bp · R EV +0.48 (adj +0.32) on $4.00, P(profit) 0.6794, adj growth 12.1 bp

## SEA @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 1 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.489 / away 0.511

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_SEA_win | p_overtime | goals | shots CGY/SEA | CGY/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.45 | 0.55 | 0.00 | 6.05 | 28.8/28.6 | 24.8/25.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.48 | 0.52 | 0.43 | 6.0 | 28.6/28.3 | 25.0/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.44 | 0.56 | 0.00 | 9.33 | 30.3/30.0 | 23.1/24.5 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.085 | 0.50 | 0.50 | 0.00 | 6.03 | 34.1/22.9 | 19.5/30.3 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.51 | 0.49 | 0.42 | 5.95 | 34.3/23.1 | 19.9/30.9 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.056 | 0.54 | 0.46 | 0.00 | 9.29 | 35.3/24.0 | 18.6/28.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 12 | 0.157 | 0.146 | +0.029 | +0.019 | $5.04 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT30SEACGY-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (6.86 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0007 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4189): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3674, phi -0.191)

portfolios: A EV +1.92 (adj +1.24) on $8.37, P(profit) 0.1566, adj growth 9.6 bp · B EV +1.16 (adj +0.74) on $5.04, P(profit) 0.1566, adj growth 6.4 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.46 (adj +0.30) on $2.00, P(profit) 0.1566, adj growth 9.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
