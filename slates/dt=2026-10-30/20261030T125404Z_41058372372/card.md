# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T12:54:04Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 106.36 | +15.60 | +4.31 | +16.63 | 0.628 | -27.06 | -45.29 | 36.40 |
| B thesis-diversified (joint) ← optimiser card | 89.65 | +11.17 | +5.49 | +9.60 | 0.627 | -31.78 | -41.74 | 49.10 |
| C best expression per thesis | 63.63 | +8.09 | +3.45 | +15.10 | 0.687 | -29.79 | -33.60 | 30.98 |
| R FUNDED research stakes | 13.00 | +1.44 | +0.74 | +0.99 | 0.560 | -6.51 | -8.62 | 0.00 |

## NJD @ VGK  ·  10000 joint draws  ·  436 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_NJD_win | p_overtime | goals | shots VGK/NJD | VGK/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.137 | 0.63 | 0.37 | 0.00 | 6.0 | 27.7/27.8 | 24.8/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.53 | 0.47 | 0.48 | 5.91 | 27.8/27.8 | 24.5/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.62 | 0.38 | 0.00 | 9.19 | 28.8/28.9 | 23.7/22.0 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.070 | 0.59 | 0.41 | 0.00 | 5.97 | 22.2/32.5 | 29.2/18.4 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.49 | 0.51 | 0.48 | 5.88 | 22.0/32.6 | 29.1/18.8 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.066 | 0.69 | 0.31 | 0.00 | 5.94 | 32.2/21.8 | 19.3/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.083 | 0.071 | +0.030 | +0.018 | $3.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 65 | 0.719 | 0.699 | +0.053 | +0.033 | $20.00 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ assists NO | 50 | 0.614 | 0.533 | +0.096 | +0.016 | $9.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Nico Hischier: 1+ goals NO | 70 | 0.737 | 0.725 | +0.022 | +0.010 | $9.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30NJVGK-NJ3|no; why: higher confidence-adjusted growth (13.28 vs 1.58 bp); despite a smaller raw edge (+0.030 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0098 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT30NJVGK-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (11.04 vs 2.48 bp); despite a smaller raw edge (+0.053 vs +0.103/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT30NJVGK-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: NJD offense succeeds (4+ goals)
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT30NJVGK-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (2.17 vs 0.54 bp); despite a smaller raw edge (+0.096 vs +0.108/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0076 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT30NJVGK-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: VGK offense succeeds (4+ goals)
- **Nico Hischier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT30NJVGK-NJNHISCHIER13-1|no selected over player prop KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NJD:SUPPRESSED (p 0.4761): highest fidelity KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT30NJVGK-NJNHISCHIER13-1|no selected over player prop KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VGK:SUPPRESSED (p 0.3585): highest fidelity KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.4259): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3585, phi -0.123)
- KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3114, phi -0.255)
- KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.4 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4259, phi -0.286)
- KXNHLGOAL-26OCT30NJVGK-NJNHISCHIER13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3114, phi -0.241)
- override: Player prop expression KXNHLGOAL-26OCT30NJVGK-NJNHISCHIER13-1|no selected over player prop KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.09 (adj +1.63) on $50.00, P(profit) 0.6306, adj growth 14.3 bp · B EV +5.83 (adj +2.75) on $42.45, P(profit) 0.6773, adj growth 24.1 bp · C EV +3.16 (adj +1.26) on $28.42, P(profit) 0.7191, adj growth 11.3 bp · R EV +0.40 (adj +0.25) on $5.00, P(profit) 0.7191, adj growth 9.1 bp

## WPG @ FLA  ·  10000 joint draws  ·  400 bet sides mapped, 17 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_WPG_win | p_overtime | goals | shots FLA/WPG | FLA/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.57 | 0.43 | 0.00 | 6.02 | 26.9/26.6 | 23.4/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.47 | 5.86 | 27.1/26.8 | 23.5/23.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.096 | 0.68 | 0.33 | 0.00 | 5.97 | 32.1/21.1 | 18.5/27.6 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.53 | 0.47 | 0.49 | 5.86 | 32.2/21.4 | 18.3/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.60 | 0.40 | 0.00 | 9.29 | 28.5/28.1 | 22.4/21.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.057 | 0.59 | 0.41 | 0.00 | 3.39 | 25.5/25.4 | 23.9/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 60 | 0.686 | 0.662 | +0.069 | +0.045 | $15.00 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 64 | 0.711 | 0.690 | +0.055 | +0.033 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 67 | 0.782 | 0.706 | +0.096 | +0.020 | $10.26 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Gabriel Vilardi: 1+ goals YES | 23 | 0.266 | 0.256 | +0.024 | +0.013 | $3.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (19.01 vs 10.91 bp); relationships: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT30WPGFLA-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: FLA offense succeeds (4+ goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no has the higher standalone adjusted growth (19.01 vs 10.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: REINFORCING (phi 0.193); KXNHLGOAL-26OCT30WPGFLA-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: higher confidence-adjusted growth (4.21 vs 3.39 bp); despite a smaller raw edge (+0.096 vs +0.097/contract); wins across more scripts (relative breadth 0.997 vs 0.887); relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: REINFORCING (phi 0.193); KXNHLGOAL-26OCT30WPGFLA-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.141); failure: FLA wins by 2+
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30WPGFLA-WPG2|yes; why: KXNHLSPREAD-26OCT30WPGFLA-WPG2|yes has the higher standalone adjusted growth (5.81 vs 2.12 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.170); relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.141); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis FLA:SUPPRESSED (p 0.3625): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS_BY_2PLUS (p 0.2227): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA3|no (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3242): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA3|no (same contract)
- KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4112, phi -0.232)
- KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4112, phi -0.268)
- KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.7 pts; opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3355, phi -0.744)
- KXNHLGOAL-26OCT30WPGFLA-WPGGVILARDI13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4638, phi -0.252)

portfolios: A EV +7.40 (adj +2.00) on $50.00, P(profit) 0.6481, adj growth 16.9 bp · B EV +4.70 (adj +2.35) on $43.53, P(profit) 0.582, adj growth 21.6 bp · C EV +4.93 (adj +2.19) on $35.21, P(profit) 0.6036, adj growth 19.6 bp · R EV +0.87 (adj +0.38) on $7.00, P(profit) 0.5638, adj growth 14.2 bp

## SEA @ CGY  ·  10000 joint draws  ·  428 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_SEA_win | p_overtime | goals | shots CGY/SEA | CGY/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.45 | 0.55 | 0.00 | 5.99 | 28.4/28.2 | 24.4/25.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.49 | 0.51 | 0.45 | 5.92 | 28.8/28.5 | 25.1/25.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.45 | 0.55 | 0.00 | 9.33 | 30.4/30.2 | 23.5/24.6 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.085 | 0.50 | 0.50 | 0.00 | 6.01 | 34.1/22.7 | 19.3/30.4 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.49 | 0.51 | 0.44 | 5.89 | 34.1/22.9 | 19.7/30.7 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.056 | 0.54 | 0.46 | 0.00 | 9.17 | 35.9/24.8 | 19.3/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 12 | 0.150 | 0.141 | +0.022 | +0.014 | $3.67 | FUNDED_RESEARCH | $1 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes; why: higher confidence-adjusted growth (3.58 vs 0.09 bp); alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4061): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3767, phi -0.18)

portfolios: A EV +1.11 (adj +0.68) on $6.36, P(profit) 0.1496, adj growth 5.2 bp · B EV +0.64 (adj +0.39) on $3.67, P(profit) 0.1496, adj growth 3.4 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.17 (adj +0.11) on $1.00, P(profit) 0.1496, adj growth 3.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
