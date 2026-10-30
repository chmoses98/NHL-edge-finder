# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T06:27:46Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 70.00 | +8.96 | +2.04 | +9.91 | 0.604 | -43.11 | -46.36 | 10.81 |
| B thesis-diversified (joint) ← optimiser card | 22.93 | +3.20 | +0.89 | +4.28 | 0.572 | -10.47 | -22.93 | 7.79 |
| C best expression per thesis | 22.82 | +3.19 | +0.88 | +5.69 | 0.572 | -9.06 | -22.82 | 7.72 |
| R FUNDED research stakes | 7.00 | +1.01 | +0.28 | +0.56 | 0.579 | -3.47 | -7.00 | 0.00 |

## NJD @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


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
| New Jersey wins by over 1.5 goals NO | 73 | 0.783 | 0.754 | +0.040 | +0.010 | $10.97 | FUNDED_RESEARCH | $3 | VGK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: VGK wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT30NJVGK-NJ2|no; why: higher confidence-adjusted growth (1.23 vs 0.88 bp); wins across more scripts (relative breadth 0.986 vs 0.61); alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: NJD wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis VGK:WINS (p 0.5781): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30NJVGK-NJ2|no (same contract)
- KXNHLSPREAD-26OCT30NJVGK-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2167, phi -1.0)

portfolios: A EV +1.06 (adj +0.28) on $20.00, P(profit) 0.7833, adj growth 2.2 bp · B EV +0.58 (adj +0.15) on $10.97, P(profit) 0.7833, adj growth 1.3 bp · C EV +0.58 (adj +0.15) on $10.97, P(profit) 0.7833, adj growth 1.3 bp · R EV +0.16 (adj +0.04) on $3.00, P(profit) 0.7833, adj growth 1.4 bp

## WPG @ FLA  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


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
| Winnipeg wins by over 1.5 goals YES | 16 | 0.223 | 0.189 | +0.053 | +0.019 | $3.81 | FUNDED_RESEARCH | $1 | WPG:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 55 | 0.664 | 0.587 | +0.097 | +0.019 | $7.07 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida over 2.5 goals scored NO | 28 | 0.351 | 0.311 | +0.057 | +0.017 | $1.08 | FUNDED_RESEARCH | $1 | FLA:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Winnipeg wins by over 1.5 goals YES** — thesis: WPG wins by 2+; alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: higher confidence-adjusted growth (5.81 vs 3.39 bp); despite a smaller raw edge (+0.053 vs +0.097/contract); relationships: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: DUPLICATIVE (phi 0.38); KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA3|no: REINFORCING (phi 0.463); failure: FLA wins (incl. OT/SO)
- **Florida wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA3|no; why: higher confidence-adjusted growth (3.39 vs 1.18 bp); relationships: KXNHLSPREAD-26OCT30WPGFLA-WPG2|yes: DUPLICATIVE (phi 0.38); KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA3|no: DUPLICATIVE (phi 0.48); failure: FLA wins by 2+
- **Florida over 2.5 goals scored NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT30WPGFLA-WPG2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT30WPGFLA-WPG2|yes has the higher standalone adjusted growth (5.81 vs 2.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.463); they share one thesis budget; relationships: KXNHLSPREAD-26OCT30WPGFLA-WPG2|yes: REINFORCING (phi 0.463); KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: DUPLICATIVE (phi 0.48); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:WINS_BY_2PLUS (p 0.2227): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no (same contract)
- thesis FLA:SUPPRESSED (p 0.3625): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT30WPGFLA-FLA3|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA3|no kept
- thesis GAME:TIGHT (p 0.4418): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no (same contract)
- KXNHLSPREAD-26OCT30WPGFLA-WPG2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS (p 0.5648, phi -0.61)
- KXNHLSPREAD-26OCT30WPGFLA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.0 pts; opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3355, phi -1.0)
- KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4112, phi -0.615)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT30WPGFLA-FLA3|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA3|no kept

portfolios: A EV +7.90 (adj +1.76) on $50.00, P(profit) 0.6742, adj growth 8.6 bp · B EV +2.62 (adj +0.74) on $11.96, P(profit) 0.6645, adj growth 6.5 bp · C EV +2.61 (adj +0.73) on $11.85, P(profit) 0.6645, adj growth 6.4 bp · R EV +0.85 (adj +0.24) on $4.00, P(profit) 0.3941, adj growth 7.9 bp

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
