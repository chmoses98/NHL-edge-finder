# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T12:06:54Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +12.76 | +3.46 | +17.11 | 0.649 | -25.55 | -43.37 | 29.79 |
| B thesis-diversified (joint) ← optimiser card | 88.79 | +9.70 | +3.72 | +9.66 | 0.644 | -26.33 | -39.93 | 33.03 |
| C best expression per thesis | 100.00 | +8.03 | +3.28 | +4.84 | 0.667 | -27.05 | -40.60 | 29.51 |
| R FUNDED research stakes | 15.00 | +1.30 | +0.59 | -0.32 | 0.495 | -7.60 | -8.29 | 0.00 |

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
| Jack Hughes: 1+ goals NO | 66 | 0.719 | 0.702 | +0.043 | +0.026 | $20.00 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.083 | 0.075 | +0.019 | +0.011 | $2.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ assists NO | 50 | 0.614 | 0.536 | +0.096 | +0.019 | $10.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ assists NO | 55 | 0.651 | 0.582 | +0.084 | +0.015 | $9.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (6.84 vs 1.95 bp); despite a smaller raw edge (+0.043 vs +0.084/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: NJD offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30NJVGK-NJ3|no; why: higher confidence-adjusted growth (4.30 vs 1.58 bp); despite a smaller raw edge (+0.019 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0098 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT30NJVGK-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (3.15 vs 0.22 bp); despite a smaller raw edge (+0.096 vs +0.098/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0048 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: VGK offense succeeds (4+ goals)
- **Jack Hughes: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no has the higher standalone adjusted growth (6.84 vs 1.95 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NJD:SUPPRESSED (p 0.4761): highest fidelity KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no (same contract)
- thesis VGK:SUPPRESSED (p 0.3585): highest fidelity KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.4259): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT30NJVGK-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3114, phi -0.255)
- KXNHLGOAL-26OCT30NJVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3585, phi -0.123)
- KXNHLAST-26OCT30NJVGK-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.9 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4259, phi -0.286)
- KXNHLAST-26OCT30NJVGK-NJJHUGHES86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.6 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3114, phi -0.272)

portfolios: A EV +5.32 (adj +1.45) on $50.00, P(profit) 0.692, adj growth 12.8 bp · B EV +5.46 (adj +1.88) on $42.66, P(profit) 0.6597, adj growth 16.5 bp · C EV +3.55 (adj +1.39) on $50.00, P(profit) 0.6997, adj growth 12.5 bp · R EV +0.32 (adj +0.19) on $5.00, P(profit) 0.7191, adj growth 6.8 bp

## WPG @ FLA  ·  10000 joint draws  ·  400 bet sides mapped, 14 +EV candidates, 4 on card


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
| Brady Tkachuk: 1+ goals NO | 61 | 0.686 | 0.662 | +0.059 | +0.035 | $16.83 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 65 | 0.711 | 0.691 | +0.045 | +0.025 | $13.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 67 | 0.782 | 0.706 | +0.096 | +0.020 | $10.96 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida over 5.5 goals scored NO | 85 | 0.896 | 0.870 | +0.037 | +0.011 | $5.17 | FUNDED_RESEARCH | $2 | WPG:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (11.74 vs 6.12 bp); relationships: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.144); KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA6|no: REINFORCING (phi 0.172); failure: FLA offense succeeds (4+ goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no; why: Player prop expression KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT30WPGFLA-FLASREINHART13-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: REINFORCING (phi 0.193); KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA6|no: REINFORCING (phi 0.167); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: higher confidence-adjusted growth (4.21 vs 3.39 bp); despite a smaller raw edge (+0.096 vs +0.097/contract); wins across more scripts (relative breadth 0.997 vs 0.887); relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: REINFORCING (phi 0.193); KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA6|no: REINFORCING (phi 0.433); failure: FLA wins by 2+
- **Florida over 5.5 goals scored NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT30WPGFLA-WPG2|yes; why: KXNHLSPREAD-26OCT30WPGFLA-WPG2|yes has the higher standalone adjusted growth (5.81 vs 2.38 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.180); relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: REINFORCING (phi 0.172); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: REINFORCING (phi 0.167); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: REINFORCING (phi 0.433); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis FLA:SUPPRESSED (p 0.3625): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no — Player prop expression KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT30WPGFLA-FLASREINHART13-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WPG:WINS_BY_2PLUS (p 0.2227): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA3|no (same contract)
- thesis WPG:WINS (p 0.4352): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA3|no (same contract)
- KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4112, phi -0.232)
- KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4112, phi -0.268)
- KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.7 pts; opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3355, phi -0.744)
- KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2453, phi -0.494)
- override: Player prop expression KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT30WPGFLA-FLASREINHART13-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT30WPGFLA-FLA2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA6|no kept

portfolios: A EV +7.44 (adj +2.01) on $50.00, P(profit) 0.6481, adj growth 17.0 bp · B EV +4.25 (adj +1.84) on $46.13, P(profit) 0.6213, adj growth 16.6 bp · C EV +4.49 (adj +1.89) on $50.00, P(profit) 0.5924, adj growth 17.0 bp · R EV +0.98 (adj +0.40) on $10.00, P(profit) 0.651, adj growth 14.2 bp

## SEA @ CGY  ·  10000 joint draws  ·  428 bet sides mapped, 0 +EV candidates, 0 on card


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
