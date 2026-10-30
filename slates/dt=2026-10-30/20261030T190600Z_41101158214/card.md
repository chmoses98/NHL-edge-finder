# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T19:06:00Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 106.61 | +14.62 | +4.62 | +18.60 | 0.644 | -26.16 | -44.24 | 40.42 |
| B thesis-diversified (joint) ← optimiser card | 92.23 | +11.62 | +6.23 | +4.14 | 0.643 | -30.87 | -35.93 | 56.36 |
| C best expression per thesis | 91.07 | +8.65 | +4.04 | +9.03 | 0.641 | -27.89 | -36.42 | 37.02 |
| R FUNDED research stakes | 11.00 | +1.16 | +0.68 | +1.60 | 0.560 | -4.99 | -7.47 | 0.00 |

## NJD @ VGK  ·  10000 joint draws  ·  448 bet sides mapped, 14 +EV candidates, 4 on card

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
| Brayden McNabb: 1+ goals YES | 5 | 0.082 | 0.073 | +0.029 | +0.019 | $4.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 65 | 0.722 | 0.702 | +0.056 | +0.036 | $15.00 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 64 | 0.774 | 0.683 | +0.117 | +0.027 | $15.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Connor Brown: 1+ goals YES | 13 | 0.163 | 0.153 | +0.025 | +0.015 | $4.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30NJVGK-NJ2|no; why: higher confidence-adjusted growth (15.60 vs 1.87 bp); despite a smaller raw edge (+0.029 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VGK offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (13.15 vs 7.30 bp); despite a smaller raw edge (+0.056 vs +0.117/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.072); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NJD offense succeeds (4+ goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no has the higher standalone adjusted growth (13.15 vs 7.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.072); they share one thesis budget; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.072); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.036); failure: NJD offense succeeds (4+ goals)
- **Connor Brown: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT30NJVGK-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (4.21 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.043/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.036); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NJD:SUPPRESSED (p 0.4741): highest fidelity KXNHLAST-26OCT30NJVGK-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:WINS (p 0.5832): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3515): highest fidelity KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no (same contract)
- KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3515, phi -0.127)
- KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3165, phi -0.238)
- KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.9 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3165, phi -0.242)
- KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4741, phi -0.199)

portfolios: A EV +7.29 (adj +1.86) on $50.00, P(profit) 0.6285, adj growth 16.5 bp · B EV +7.03 (adj +3.50) on $38.63, P(profit) 0.6605, adj growth 30.9 bp · C EV +4.05 (adj +1.56) on $41.41, P(profit) 0.692, adj growth 14.1 bp · R EV +0.33 (adj +0.22) on $4.00, P(profit) 0.7215, adj growth 8.2 bp

## WPG @ FLA  ·  10000 joint draws  ·  438 bet sides mapped, 21 +EV candidates, 4 on card

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
| Brady Tkachuk: 1+ goals NO | 59 | 0.679 | 0.656 | +0.072 | +0.049 | $14.62 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Elias Salomonsson: 1+ goals NO | 91 | 0.950 | 0.939 | +0.034 | +0.023 | $14.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 63 | 0.698 | 0.678 | +0.052 | +0.032 | $14.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 55 | 0.636 | 0.591 | +0.069 | +0.023 | $6.20 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (22.02 vs 9.96 bp); relationships: KXNHLGOAL-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: REINFORCING (phi 0.157); failure: FLA offense succeeds (4+ goals)
- **Elias Salomonsson: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no; why: higher confidence-adjusted growth (15.38 vs 2.48 bp); despite a smaller raw edge (+0.034 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: INTENTIONAL_DIVERSIFIER (phi -0.064); failure: WPG offense succeeds (4+ goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no has the higher standalone adjusted growth (22.02 vs 9.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: REINFORCING (phi 0.207); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA3|no; why: higher confidence-adjusted growth (4.79 vs 2.85 bp); relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: REINFORCING (phi 0.157); KXNHLGOAL-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: INTENTIONAL_DIVERSIFIER (phi -0.064); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: REINFORCING (phi 0.207); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis FLA:SUPPRESSED (p 0.3408): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.411): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3124): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4462, phi -0.229)
- KXNHLGOAL-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3124, phi -0.088)
- KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4462, phi -0.251)
- KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.364, phi -1.0)

portfolios: A EV +6.63 (adj +2.37) on $50.00, P(profit) 0.5744, adj growth 20.9 bp · B EV +4.21 (adj +2.52) on $50.00, P(profit) 0.5727, adj growth 23.6 bp · C EV +4.61 (adj +2.48) on $49.66, P(profit) 0.6475, adj growth 22.9 bp · R EV +0.72 (adj +0.40) on $6.00, P(profit) 0.6794, adj growth 15.0 bp

## SEA @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 1 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.489 / away 0.511

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_SEA_win | p_overtime | goals | shots CGY/SEA | CGY/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.44 | 0.56 | 0.00 | 6.05 | 28.9/28.7 | 24.7/25.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.48 | 0.52 | 0.46 | 5.97 | 28.7/28.5 | 25.3/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.46 | 0.54 | 0.00 | 9.35 | 30.1/30.0 | 23.6/24.1 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.086 | 0.51 | 0.49 | 0.00 | 5.98 | 33.9/22.7 | 19.3/30.3 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.50 | 0.50 | 0.49 | 5.89 | 34.0/23.0 | 19.7/30.8 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.056 | 0.53 | 0.47 | 0.00 | 9.27 | 35.4/23.8 | 18.2/28.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aydar Suniev: 1+ goals YES | 19 | 0.222 | 0.213 | +0.021 | +0.012 | $3.60 | FUNDED_RESEARCH | $1 | CGY:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLAST-26OCT30SEACGY-CGYYSHARANGOVICH17-1|yes; why: higher confidence-adjusted growth (1.92 vs 0.00 bp); despite a smaller raw edge (+0.021 vs +0.022/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CGY:OFFENSE_4PLUS (p 0.3744): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.407, phi -0.194)

portfolios: A EV +0.70 (adj +0.39) on $6.61, P(profit) 0.2219, adj growth 3.0 bp · B EV +0.38 (adj +0.21) on $3.60, P(profit) 0.2219, adj growth 1.9 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.11 (adj +0.06) on $1.00, P(profit) 0.2219, adj growth 2.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
