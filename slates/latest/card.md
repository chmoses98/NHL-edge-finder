# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-02T05:14:48Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 30.30 | +6.39 | +1.71 | -30.30 | 0.355 | -30.30 | -30.30 | 2.57 |
| B thesis-diversified (joint) ← optimiser card | 4.29 | +0.94 | +0.25 | -4.29 | 0.355 | -4.29 | -4.29 | 2.20 |
| C best expression per thesis | 2.89 | +0.80 | +0.22 | -2.89 | 0.190 | -2.89 | -2.89 | 1.94 |
| R FUNDED research stakes | 2.00 | +0.44 | +0.12 | -2.00 | 0.355 | -2.00 | -2.00 | 0.00 |

## VGK @ BOS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_VGK_win | p_overtime | goals | shots BOS/VGK | BOS/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.53 | 0.47 | 0.00 | 6.04 | 27.2/27.5 | 24.1/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.47 | 5.99 | 27.5/27.8 | 24.5/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.54 | 0.46 | 0.00 | 9.4 | 28.9/29.4 | 23.7/22.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.090 | 0.45 | 0.55 | 0.00 | 6.02 | 21.7/32.6 | 28.6/18.6 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.47 | 0.53 | 0.48 | 5.89 | 21.9/32.7 | 29.4/18.7 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.070 | 0.47 | 0.53 | 0.00 | 9.24 | 23.1/34.2 | 27.6/17.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ FLA  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_DET_win | p_overtime | goals | shots FLA/DET | FLA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.59 | 0.41 | 0.00 | 6.03 | 26.9/26.9 | 23.7/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.53 | 0.47 | 0.45 | 5.9 | 27.1/27.0 | 23.8/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.60 | 0.40 | 0.00 | 9.22 | 28.4/28.4 | 23.0/21.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.074 | 0.66 | 0.34 | 0.00 | 6.03 | 31.6/21.3 | 18.6/26.9 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.064 | 0.49 | 0.51 | 0.00 | 6.01 | 21.7/31.8 | 28.1/18.4 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.57 | 0.43 | 0.44 | 5.9 | 32.0/21.7 | 18.6/28.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Detroit over 4.5 goals scored YES | 14 | 0.190 | 0.160 | +0.041 | +0.011 | $2.00 | FUNDED_RESEARCH | $1 | DET:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| Detroit over 3.5 goals scored YES | 29 | 0.355 | 0.318 | +0.051 | +0.013 | $2.29 | FUNDED_RESEARCH | $1 | DET:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Detroit over 4.5 goals scored YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes; why: higher confidence-adjusted growth (2.24 vs 1.76 bp); despite a smaller raw edge (+0.041 vs +0.051/contract); relationships: KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes: DUPLICATIVE (phi 0.652); failure: FLA wins (incl. OT/SO)
- **Detroit over 3.5 goals scored YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes has the higher standalone adjusted growth (2.24 vs 1.76 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.652); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes: DUPLICATIVE (phi 0.652); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis DET:OFFENSE_4PLUS (p 0.3451): highest fidelity KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes (same contract)
- KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes: FUNDED_RESEARCH; family MIXED; loses 45% of the draws where the thesis happens; opposing: failure thesis FLA:WINS (p 0.5619, phi -0.455)
- KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:SUPPRESSED (p 0.437, phi -0.654)

portfolios: A EV +6.39 (adj +1.71) on $30.30, P(profit) 0.355, adj growth 2.6 bp · B EV +0.94 (adj +0.25) on $4.29, P(profit) 0.355, adj growth 2.2 bp · C EV +0.80 (adj +0.22) on $2.89, P(profit) 0.1897, adj growth 1.9 bp · R EV +0.44 (adj +0.12) on $2.00, P(profit) 0.355, adj growth 3.6 bp

## COL @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_COL_win | p_overtime | goals | shots CHI/COL | CHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.156 | 0.27 | 0.73 | 0.00 | 6.05 | 21.7/34.5 | 29.4/19.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.42 | 0.58 | 0.47 | 5.94 | 22.3/34.9 | 31.4/19.1 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.114 | 0.26 | 0.74 | 0.00 | 9.38 | 23.0/36.0 | 27.6/18.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.32 | 0.68 | 0.00 | 6.06 | 27.6/28.4 | 24.0/24.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.47 | 0.53 | 0.47 | 5.95 | 27.7/28.5 | 25.1/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.34 | 0.66 | 0.00 | 9.39 | 29.1/30.3 | 22.9/24.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.16, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_CGY_win | p_overtime | goals | shots SJS/CGY | SJS/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.58 | 0.42 | 0.00 | 6.03 | 28.8/28.7 | 25.6/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.47 | 5.94 | 28.8/28.6 | 25.4/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.58 | 0.41 | 0.00 | 9.28 | 30.0/29.9 | 24.2/23.0 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.076 | 0.64 | 0.36 | 0.00 | 5.97 | 33.5/22.6 | 19.9/29.2 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.55 | 0.45 | 0.48 | 5.97 | 33.7/22.8 | 19.7/30.0 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.059 | 0.56 | 0.44 | 0.00 | 6.03 | 22.8/33.3 | 29.7/19.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
