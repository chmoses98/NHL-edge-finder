# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T21:54:59Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 131.36 | +18.22 | +6.84 | +14.96 | 0.605 | -45.05 | -52.88 | 56.09 |
| B thesis-diversified (joint) ← optimiser card | 97.39 | +16.32 | +10.89 | +3.19 | 0.577 | -37.97 | -49.43 | 93.20 |
| C best expression per thesis | 87.07 | +10.18 | +4.69 | +9.89 | 0.618 | -28.25 | -38.50 | 42.34 |
| R FUNDED research stakes | 14.00 | +1.49 | +0.88 | +0.10 | 0.560 | -7.41 | -9.68 | 0.00 |

## NJD @ VGK  ·  10000 joint draws  ·  438 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.507 / away 0.493

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_NJD_win | p_overtime | goals | shots VGK/NJD | VGK/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.61 | 0.39 | 0.00 | 6.03 | 27.7/27.8 | 24.8/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.52 | 0.48 | 0.49 | 5.86 | 27.6/27.8 | 24.7/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.65 | 0.35 | 0.00 | 9.22 | 29.1/29.2 | 24.1/22.4 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.075 | 0.60 | 0.40 | 0.00 | 6.06 | 22.0/32.5 | 29.2/18.2 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.49 | 0.51 | 0.45 | 5.86 | 22.3/32.8 | 29.5/19.1 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.063 | 0.67 | 0.33 | 0.00 | 5.99 | 31.8/21.8 | 19.1/27.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.092 | 0.080 | +0.039 | +0.027 | $5.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Anthony Mantha: 2+ goals YES | 1 | 0.022 | 0.021 | +0.011 | +0.011 | $2.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.05) | EVIDENCE_STRONGER | D |
| Braeden Bowman: 1+ goals YES | 14 | 0.182 | 0.169 | +0.034 | +0.021 | $5.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 65 | 0.703 | 0.688 | +0.037 | +0.022 | $17.04 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30NJVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (29.77 vs 3.06 bp); relationships: KXNHLGOAL-26OCT30NJVGK-NJAMANTHA39-2|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT30NJVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: VGK offense suppressed (<= 2 goals)
- **Anthony Mantha: 2+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes; why: higher confidence-adjusted growth (20.82 vs 5.08 bp); despite a smaller raw edge (+0.011 vs +0.027/contract); relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT30NJVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: NJD offense suppressed (<= 2 goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30NJVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (7.44 vs 3.06 bp); relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT30NJVGK-NJAMANTHA39-2|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: VGK offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT30NJVGK-NJAMANTHA39-2|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT30NJVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NJD:SUPPRESSED (p 0.4764): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ2|no [DIRECT], best adjusted EV KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VGK:WINS (p 0.5798): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:OFFENSE_4PLUS (p 0.3147): highest fidelity KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes (same contract)
- KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3591, phi -0.127)
- KXNHLGOAL-26OCT30NJVGK-NJAMANTHA39-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 95% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4764, phi -0.123)
- KXNHLGOAL-26OCT30NJVGK-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3591, phi -0.161)
- KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3147, phi -0.251)
- override: Player prop expression KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.37 (adj +1.49) on $50.00, P(profit) 0.6463, adj growth 12.9 bp · B EV +9.11 (adj +6.85) on $31.07, P(profit) 0.2737, adj growth 56.6 bp · C EV +5.13 (adj +1.99) on $34.56, P(profit) 0.5932, adj growth 17.4 bp · R EV +0.28 (adj +0.17) on $5.00, P(profit) 0.7029, adj growth 5.8 bp

## WPG @ FLA  ·  10000 joint draws  ·  438 bet sides mapped, 24 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.664 / away 0.336

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
| Brady Tkachuk: 1+ goals NO | 59 | 0.679 | 0.656 | +0.072 | +0.049 | $14.47 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 63 | 0.698 | 0.680 | +0.052 | +0.033 | $14.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 68 | 0.758 | 0.716 | +0.063 | +0.021 | $9.18 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Elias Salomonsson: 1+ assists NO | 75 | 0.810 | 0.777 | +0.047 | +0.014 | $11.88 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (22.02 vs 10.75 bp); relationships: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: REINFORCING (phi 0.152); KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense succeeds (4+ goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no has the higher standalone adjusted growth (22.02 vs 10.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: REINFORCING (phi 0.188); KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no has the higher standalone adjusted growth (4.79 vs 4.65 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.747); relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: REINFORCING (phi 0.152); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: REINFORCING (phi 0.188); KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: INTENTIONAL_DIVERSIFIER (phi -0.112); failure: FLA wins by 2+
- **Elias Salomonsson: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT30WPGFLA-3|no; why: higher confidence-adjusted growth (2.48 vs 1.91 bp); wins across more scripts (relative breadth 0.985 vs 0.389); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.112); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis FLA:SUPPRESSED (p 0.3408): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.411): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3124): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4462, phi -0.229)
- KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4462, phi -0.251)
- KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.364, phi -0.747)
- KXNHLAST-26OCT30WPGFLA-WPGESALOMONSSON57-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3124, phi -0.223)

portfolios: A EV +6.61 (adj +2.33) on $50.00, P(profit) 0.5744, adj growth 20.5 bp · B EV +4.44 (adj +2.41) on $50.00, P(profit) 0.7059, adj growth 22.5 bp · C EV +4.61 (adj +2.50) on $49.65, P(profit) 0.6475, adj growth 23.2 bp · R EV +0.75 (adj +0.41) on $7.00, P(profit) 0.5452, adj growth 15.3 bp

## SEA @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 4 +EV candidates, 4 on card

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
| Ben Meyers: 1+ goals YES | 12 | 0.157 | 0.146 | +0.029 | +0.019 | $5.03 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 18 | 0.221 | 0.208 | +0.031 | +0.018 | $5.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 19 | 0.222 | 0.213 | +0.021 | +0.012 | $3.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 14 | 0.172 | 0.159 | +0.023 | +0.010 | $2.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:WINS_BY_2PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (6.97 vs 1.87 bp); relationships: KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (4.52 vs 1.87 bp); relationships: KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: SEA offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLAST-26OCT30SEACGY-CGYYSHARANGOVICH17-1|yes; why: higher confidence-adjusted growth (1.92 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CGY offense suppressed (<= 2 goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA wins by 2+; alternative: KXNHLPTS-26OCT30SEACGY-CGYJFARABEE86-1|no; why: higher confidence-adjusted growth (1.87 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4144): highest fidelity KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.3033): highest fidelity KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3744): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3603, phi -0.183)
- KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3603, phi -0.204)
- KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.407, phi -0.194)
- KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3603, phi -0.202)

portfolios: A EV +5.25 (adj +3.02) on $31.36, P(profit) 0.5717, adj growth 22.7 bp · B EV +2.78 (adj +1.63) on $16.32, P(profit) 0.5717, adj growth 14.1 bp · C EV +0.45 (adj +0.20) on $2.86, P(profit) 0.1718, adj growth 1.7 bp · R EV +0.46 (adj +0.30) on $2.00, P(profit) 0.1568, adj growth 9.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
