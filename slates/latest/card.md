# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T20:37:02Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 125.90 | +16.55 | +6.45 | +13.92 | 0.593 | -42.85 | -62.79 | 52.68 |
| B thesis-diversified (joint) ← optimiser card | 91.52 | +13.23 | +7.73 | +5.96 | 0.569 | -36.11 | -48.79 | 67.82 |
| C best expression per thesis | 81.31 | +8.45 | +4.63 | +6.91 | 0.558 | -29.23 | -41.41 | 41.65 |
| R FUNDED research stakes | 14.00 | +1.36 | +0.78 | +0.82 | 0.589 | -7.41 | -9.68 | 0.00 |

## NJD @ VGK  ·  10000 joint draws  ·  436 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.507 / away 0.493

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_NJD_win | p_overtime | goals | shots VGK/NJD | VGK/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.63 | 0.37 | 0.00 | 6.05 | 27.4/27.6 | 24.6/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.57 | 0.43 | 0.46 | 5.89 | 27.6/27.8 | 24.6/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.61 | 0.39 | 0.00 | 9.2 | 29.2/29.2 | 23.9/22.7 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.076 | 0.59 | 0.41 | 0.00 | 5.98 | 22.2/32.8 | 29.7/18.3 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.068 | 0.68 | 0.32 | 0.00 | 6.04 | 32.0/22.0 | 19.4/27.5 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.47 | 0.53 | 0.49 | 5.9 | 22.1/32.6 | 29.3/19.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.089 | 0.078 | +0.035 | +0.024 | $5.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 65 | 0.705 | 0.690 | +0.039 | +0.024 | $18.51 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Braeden Bowman: 1+ goals YES | 15 | 0.191 | 0.177 | +0.032 | +0.018 | $4.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Connor Brown: 1+ goals YES | 13 | 0.164 | 0.154 | +0.026 | +0.016 | $4.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30NJVGK-VGKBBOWMAN42-1|yes; why: higher confidence-adjusted growth (24.66 vs 5.20 bp); relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT30NJVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: VGK offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (5.62 vs 4.63 bp); despite a smaller raw edge (+0.039 vs +0.102/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT30NJVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: NJD offense succeeds (4+ goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30NJVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (5.20 vs 3.15 bp); relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: VGK offense suppressed (<= 2 goals)
- **Connor Brown: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT30NJVGK-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (4.68 vs 0.00 bp); despite a smaller raw edge (+0.026 vs +0.046/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT30NJVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NJD:SUPPRESSED (p 0.4757): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:WINS (p 0.5832): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:OFFENSE_4PLUS (p 0.4235): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT30NJVGK-VGKBBOWMAN42-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3528, phi -0.129)
- KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3101, phi -0.251)
- KXNHLGOAL-26OCT30NJVGK-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3528, phi -0.2)
- KXNHLGOAL-26OCT30NJVGK-NJCBROWN16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4757, phi -0.205)

portfolios: A EV +5.04 (adj +1.58) on $50.00, P(profit) 0.6154, adj growth 13.5 bp · B EV +6.45 (adj +4.20) on $33.19, P(profit) 0.3039, adj growth 35.8 bp · C EV +2.91 (adj +1.74) on $27.83, P(profit) 0.3247, adj growth 15.2 bp · R EV +0.29 (adj +0.18) on $5.00, P(profit) 0.7047, adj growth 6.2 bp

## WPG @ FLA  ·  10000 joint draws  ·  438 bet sides mapped, 22 +EV candidates, 4 on card

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
| Brady Tkachuk: 1+ goals NO | 59 | 0.679 | 0.656 | +0.072 | +0.049 | $15.04 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 63 | 0.698 | 0.678 | +0.052 | +0.032 | $14.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 68 | 0.758 | 0.716 | +0.063 | +0.021 | $10.89 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Akira Schmid: 23+ saves YES | 41 | 0.484 | 0.440 | +0.057 | +0.013 | $5.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:NET_HIGH_VOLUME | DIRECT (0.95) | EVIDENCE_MIXED | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (22.02 vs 9.96 bp); relationships: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: REINFORCING (phi 0.152); KXNHLSAVE-26OCT30WPGFLA-FLAASCHMID40-23|yes: MOSTLY_INDEPENDENT (phi -0.033); failure: FLA offense succeeds (4+ goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no; why: Player prop expression KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT30WPGFLA-FLASREINHART13-1|no because adjusted EV is 1.0 pts higher while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: REINFORCING (phi 0.188); KXNHLSAVE-26OCT30WPGFLA-FLAASCHMID40-23|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no has the higher standalone adjusted growth (4.79 vs 4.65 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.747); relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: REINFORCING (phi 0.152); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: REINFORCING (phi 0.188); KXNHLSAVE-26OCT30WPGFLA-FLAASCHMID40-23|yes: INTENTIONAL_DIVERSIFIER (phi -0.086); failure: FLA wins by 2+
- **Akira Schmid: 23+ saves YES** — thesis: FLA net faces heavy volume (33+ shots; WPG pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.086); failure: FLA net faces light volume (<= 25 shots; WPG suppressed)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis FLA:SUPPRESSED (p 0.3408): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no — Player prop expression KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT30WPGFLA-FLASREINHART13-1|no because adjusted EV is 1.0 pts higher while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WPG:WINS (p 0.411): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3124): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4462, phi -0.229)
- KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4462, phi -0.251)
- KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.364, phi -0.747)
- KXNHLSAVE-26OCT30WPGFLA-FLAASCHMID40-23|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family MIXED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:NET_LOW_VOLUME (p 0.5197, phi -0.774)
- override: Player prop expression KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT30WPGFLA-FLASREINHART13-1|no because adjusted EV is 1.0 pts higher while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.87 (adj +2.54) on $50.00, P(profit) 0.5744, adj growth 22.5 bp · B EV +4.65 (adj +2.44) on $45.99, P(profit) 0.6128, adj growth 22.5 bp · C EV +4.61 (adj +2.48) on $49.66, P(profit) 0.6475, adj growth 22.9 bp · R EV +0.75 (adj +0.41) on $7.00, P(profit) 0.5452, adj growth 15.3 bp

## SEA @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 3 +EV candidates, 3 on card

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
| Berkly Catton: 1+ goals YES | 18 | 0.221 | 0.208 | +0.031 | +0.018 | $5.15 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 13 | 0.172 | 0.153 | +0.034 | +0.015 | $3.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:WINS_BY_2PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 19 | 0.222 | 0.213 | +0.021 | +0.012 | $3.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (4.52 vs 3.92 bp); despite a smaller raw edge (+0.031 vs +0.034/contract); relationships: KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.028); failure: SEA offense suppressed (<= 2 goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA wins by 2+; alternative: KXNHLPTS-26OCT30SEACGY-CGYJFARABEE86-1|no; why: higher confidence-adjusted growth (3.92 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: SEA offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLAST-26OCT30SEACGY-CGYYSHARANGOVICH17-1|yes; why: higher confidence-adjusted growth (1.92 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4144): highest fidelity KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.3033): highest fidelity KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3744): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3603, phi -0.204)
- KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3603, phi -0.202)
- KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.407, phi -0.194)

portfolios: A EV +4.64 (adj +2.33) on $25.90, P(profit) 0.4925, adj growth 16.6 bp · B EV +2.12 (adj +1.09) on $12.34, P(profit) 0.4925, adj growth 9.5 bp · C EV +0.94 (adj +0.41) on $3.82, P(profit) 0.1718, adj growth 3.5 bp · R EV +0.32 (adj +0.19) on $2.00, P(profit) 0.221, adj growth 6.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
