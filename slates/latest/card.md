# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T04:40:05Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 70.00 | +7.72 | +1.58 | +15.23 | 0.666 | -43.11 | -46.36 | 9.30 |
| B thesis-diversified (joint) ← optimiser card | 12.96 | +1.18 | +0.35 | +1.79 | 0.820 | -12.96 | -12.96 | 3.21 |
| C best expression per thesis | 23.05 | +2.65 | +0.57 | +12.99 | 0.522 | -8.30 | -23.05 | 4.99 |
| R FUNDED research stakes | 4.00 | +0.46 | +0.14 | +0.03 | 0.820 | -4.00 | -4.00 | 0.00 |

## NJD @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_NJD_win | p_overtime | goals | shots VGK/NJD | VGK/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.135 | 0.62 | 0.38 | 0.00 | 6.01 | 27.5/27.7 | 24.6/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.54 | 0.46 | 0.48 | 5.95 | 27.7/27.9 | 24.6/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.63 | 0.37 | 0.00 | 9.19 | 28.9/29.2 | 24.1/21.9 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.070 | 0.61 | 0.39 | 0.00 | 5.94 | 22.3/32.8 | 29.5/18.6 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.068 | 0.68 | 0.32 | 0.00 | 5.95 | 32.2/21.7 | 19.3/27.5 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.49 | 0.51 | 0.46 | 5.86 | 22.2/32.9 | 29.7/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 1.5 goals NO | 73 | 0.783 | 0.754 | +0.040 | +0.010 | $10.97 | FUNDED_RESEARCH | $3 | VGK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: VGK wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT30NJVGK-NJ3|no; why: higher confidence-adjusted growth (1.23 vs 0.63 bp); wins across more scripts (relative breadth 0.989 vs 0.767); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: NJD wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:WINS (p 0.5781): highest fidelity KXNHLSPREAD-26OCT30NJVGK-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30NJVGK-NJ2|no (same contract)
- KXNHLSPREAD-26OCT30NJVGK-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2167, phi -1.0)

portfolios: A EV +1.06 (adj +0.28) on $20.00, P(profit) 0.7833, adj growth 2.2 bp · B EV +0.58 (adj +0.15) on $10.97, P(profit) 0.7833, adj growth 1.3 bp · C EV +0.58 (adj +0.15) on $10.97, P(profit) 0.7833, adj growth 1.3 bp · R EV +0.16 (adj +0.04) on $3.00, P(profit) 0.7833, adj growth 1.4 bp

## WPG @ FLA  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_WPG_win | p_overtime | goals | shots FLA/WPG | FLA/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.59 | 0.41 | 0.00 | 6.0 | 26.8/26.4 | 23.4/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.47 | 5.86 | 27.0/26.7 | 23.4/23.7 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.095 | 0.66 | 0.34 | 0.00 | 5.99 | 32.3/21.4 | 18.6/27.8 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.54 | 0.46 | 0.49 | 5.85 | 32.2/21.4 | 18.3/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.60 | 0.40 | 0.00 | 9.3 | 28.5/28.2 | 22.4/21.9 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.057 | 0.66 | 0.34 | 0.00 | 9.1 | 33.7/22.6 | 18.0/25.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Winnipeg over 4.5 goals scored YES | 12 | 0.166 | 0.140 | +0.038 | +0.013 | $1.99 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Winnipeg over 4.5 goals scored YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no has the higher standalone adjusted growth (3.39 vs 3.30 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.289); relationships: only recommended bet in this game; failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.09.
- thesis GAME:TIGHT (p 0.4418): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3242): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.3625): highest fidelity KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG5|yes: FUNDED_RESEARCH; family MIXED; loses 49% of the draws where the thesis happens; opposing: failure thesis WPG:SUPPRESSED (p 0.4638, phi -0.415)

portfolios: A EV +6.66 (adj +1.30) on $50.00, P(profit) 0.7073, adj growth 7.1 bp · B EV +0.60 (adj +0.20) on $1.99, P(profit) 0.1658, adj growth 1.9 bp · C EV +2.07 (adj +0.42) on $12.08, P(profit) 0.6645, adj growth 3.6 bp · R EV +0.30 (adj +0.10) on $1.00, P(profit) 0.1658, adj growth 3.4 bp

## SEA @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_SEA_win | p_overtime | goals | shots CGY/SEA | CGY/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.45 | 0.55 | 0.00 | 6.0 | 28.5/28.4 | 24.6/25.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.45 | 5.92 | 28.8/28.6 | 25.1/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.46 | 0.54 | 0.00 | 9.29 | 30.4/30.1 | 23.7/24.6 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.49 | 0.51 | 0.45 | 5.91 | 34.1/22.7 | 19.4/30.7 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.082 | 0.50 | 0.50 | 0.00 | 6.01 | 34.2/22.9 | 19.5/30.4 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.059 | 0.55 | 0.45 | 0.00 | 9.22 | 35.6/24.5 | 18.8/28.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
