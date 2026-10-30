# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T11:06:53Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +15.46 | +3.21 | +23.90 | 0.659 | -38.21 | -56.98 | 23.82 |
| B thesis-diversified (joint) ← optimiser card | 48.96 | +7.09 | +2.32 | +3.89 | 0.647 | -21.32 | -32.54 | 20.58 |
| C best expression per thesis | 54.52 | +6.74 | +2.14 | +7.22 | 0.650 | -25.77 | -32.56 | 18.71 |
| R FUNDED research stakes | 8.00 | +0.92 | +0.36 | +2.32 | 0.628 | -5.08 | -8.00 | 0.00 |

## NJD @ VGK  ·  10000 joint draws  ·  436 bet sides mapped, 8 +EV candidates, 4 on card


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
| Jack Hughes: 1+ goals NO | 66 | 0.719 | 0.702 | +0.043 | +0.026 | $20.00 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.083 | 0.076 | +0.019 | +0.012 | $3.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ assists NO | 49 | 0.614 | 0.527 | +0.106 | +0.019 | $10.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ assists NO | 54 | 0.651 | 0.572 | +0.094 | +0.015 | $9.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT30NJVGK-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (6.84 vs 2.48 bp); despite a smaller raw edge (+0.043 vs +0.103/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: NJD offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30NJVGK-NJ2|no; why: higher confidence-adjusted growth (5.33 vs 1.23 bp); despite a smaller raw edge (+0.019 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT30NJVGK-VGKMSTONE61-1|no; why: higher confidence-adjusted growth (3.24 vs 1.21 bp); relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: VGK offense succeeds (4+ goals)
- **Jack Hughes: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no has the higher standalone adjusted growth (6.84 vs 1.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NJD:SUPPRESSED (p 0.4761): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3585): highest fidelity KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no (same contract)
- thesis VGK:WINS (p 0.5781): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3114, phi -0.255)
- KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3585, phi -0.123)
- KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.4 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4259, phi -0.286)
- KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3114, phi -0.272)

portfolios: A EV +7.91 (adj +1.41) on $50.00, P(profit) 0.6084, adj growth 11.9 bp · B EV +5.99 (adj +2.02) on $42.95, P(profit) 0.6597, adj growth 17.7 bp · C EV +4.41 (adj +1.35) on $42.77, P(profit) 0.6386, adj growth 11.8 bp · R EV +0.32 (adj +0.19) on $5.00, P(profit) 0.7191, adj growth 6.8 bp

## WPG @ FLA  ·  10000 joint draws  ·  354 bet sides mapped, 7 +EV candidates, 2 on card


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
| Winnipeg wins by over 1.5 goals YES | 16 | 0.223 | 0.189 | +0.053 | +0.019 | $1.49 | FUNDED_RESEARCH | $1 | WPG:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 67 | 0.782 | 0.706 | +0.096 | +0.020 | $4.52 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Winnipeg wins by over 1.5 goals YES** — thesis: WPG wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4|no; why: higher confidence-adjusted growth (5.81 vs 4.32 bp); despite a smaller raw edge (+0.053 vs +0.072/contract); relationships: KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: REINFORCING (phi 0.283); failure: FLA wins (incl. OT/SO)
- **Florida wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4|no; why: KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4|no has the higher standalone adjusted growth (4.32 vs 4.21 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.515); relationships: KXNHLSPREAD-26OCT30WPGFLA-WPG2|yes: REINFORCING (phi 0.283); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:WINS_BY_2PLUS (p 0.2227): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.3625): highest fidelity KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4|no (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3242): highest fidelity KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT30WPGFLA-WPG2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS (p 0.5648, phi -0.61)
- KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.7 pts; opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3355, phi -0.744)

portfolios: A EV +7.55 (adj +1.80) on $50.00, P(profit) 0.7073, adj growth 12.0 bp · B EV +1.10 (adj +0.30) on $6.01, P(profit) 0.7816, adj growth 2.9 bp · C EV +2.33 (adj +0.79) on $11.75, P(profit) 0.5947, adj growth 6.9 bp · R EV +0.60 (adj +0.17) on $3.00, P(profit) 0.2227, adj growth 6.2 bp

## SEA @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_SEA_win | p_overtime | goals | shots CGY/SEA | CGY/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.45 | 0.55 | 0.00 | 5.99 | 28.4/28.2 | 24.4/25.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.49 | 0.51 | 0.45 | 5.92 | 28.8/28.5 | 25.1/25.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.45 | 0.55 | 0.00 | 9.33 | 30.4/30.2 | 23.5/24.6 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.085 | 0.50 | 0.50 | 0.00 | 6.01 | 34.1/22.7 | 19.3/30.4 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.49 | 0.51 | 0.44 | 5.89 | 34.1/22.9 | 19.7/30.7 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.056 | 0.54 | 0.46 | 0.00 | 9.17 | 35.9/24.8 | 19.3/29.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
