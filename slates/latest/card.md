# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-04T07:22:33Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 19.79 | +11.93 | +4.49 | -19.79 | 0.159 | -19.79 | -19.79 | 12.05 |
| B thesis-diversified (joint) ← optimiser card | 3.06 | +2.08 | +0.79 | -3.06 | 0.159 | -3.06 | -3.06 | 6.74 |
| C best expression per thesis | 1.98 | +1.91 | +0.74 | -1.98 | 0.063 | -1.98 | -1.98 | 6.30 |
| R FUNDED research stakes | 2.00 | +1.32 | +0.50 | -2.00 | 0.159 | -2.00 | -2.00 | 0.00 |

## OTT @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_OTT_win | p_overtime | goals | shots BUF/OTT | BUF/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.53 | 0.47 | 0.00 | 6.04 | 27.4/27.4 | 23.9/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.47 | 5.96 | 27.3/27.4 | 24.1/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.54 | 0.46 | 0.00 | 9.36 | 29.1/29.1 | 23.1/22.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.073 | 0.60 | 0.40 | 0.00 | 6.04 | 32.1/21.7 | 18.8/27.8 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.54 | 0.46 | 0.45 | 5.95 | 32.5/21.8 | 18.6/29.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.061 | 0.52 | 0.48 | 0.00 | 6.02 | 21.9/32.1 | 28.6/18.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ FLA  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_CHI_win | p_overtime | goals | shots FLA/CHI | FLA/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.142 | 0.73 | 0.27 | 0.00 | 6.01 | 32.5/20.8 | 18.3/27.6 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.57 | 0.43 | 0.48 | 5.9 | 32.8/21.1 | 18.0/29.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.66 | 0.34 | 0.00 | 6.03 | 27.1/26.4 | 23.5/22.6 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.101 | 0.71 | 0.29 | 0.00 | 9.26 | 34.4/22.3 | 17.9/26.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.51 | 0.49 | 0.46 | 5.9 | 27.2/26.5 | 23.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.65 | 0.35 | 0.00 | 9.36 | 28.5/27.9 | 22.8/21.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Chicago over 5.5 goals scored YES | 3 | 0.063 | 0.044 | +0.031 | +0.012 | $1.62 | FUNDED_RESEARCH | $1 | CHI:WINS_BY_2PLUS | FRAGILE (0.26) | EVIDENCE_MIXED | D |
| Chicago over 4.5 goals scored YES | 11 | 0.159 | 0.132 | +0.042 | +0.015 | $1.43 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
- **Chicago over 5.5 goals scored YES** — thesis: CHI wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes; why: higher confidence-adjusted growth (9.69 vs 4.64 bp); despite a smaller raw edge (+0.031 vs +0.042/contract); relationships: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes: DUPLICATIVE (phi 0.597); failure: FLA wins (incl. OT/SO)
- **Chicago over 4.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6|yes has the higher standalone adjusted growth (9.69 vs 4.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.597); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6|yes: DUPLICATIVE (phi 0.597); failure: FLA wins (incl. OT/SO)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.14, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:WINS_BY_2PLUS (p 0.1851): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3076): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes (same contract)
- KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6|yes: FUNDED_RESEARCH; family MIXED; loses 74% of the draws where the thesis happens; opposing: failure thesis FLA:WINS (p 0.626, phi -0.298)
- KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes: FUNDED_RESEARCH; family MIXED; loses 48% of the draws where the thesis happens; opposing: failure thesis FLA:WINS (p 0.626, phi -0.432)

portfolios: A EV +11.93 (adj +4.49) on $19.79, P(profit) 0.1585, adj growth 12.0 bp · B EV +2.08 (adj +0.79) on $3.06, P(profit) 0.1585, adj growth 6.7 bp · C EV +1.91 (adj +0.74) on $1.98, P(profit) 0.063, adj growth 6.3 bp · R EV +1.32 (adj +0.50) on $2.00, P(profit) 0.1585, adj growth 13.0 bp

## SJS @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_SJS_win | p_overtime | goals | shots LAK/SJS | LAK/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.61 | 0.39 | 0.00 | 5.98 | 27.9/27.6 | 24.6/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.47 | 5.93 | 28.1/27.7 | 24.4/24.8 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.101 | 0.67 | 0.33 | 0.00 | 6.0 | 33.5/22.2 | 19.6/28.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.55 | 0.45 | 0.47 | 5.87 | 32.9/21.9 | 18.8/29.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.61 | 0.39 | 0.00 | 9.16 | 29.4/29.1 | 23.6/22.6 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.064 | 0.66 | 0.34 | 0.00 | 9.26 | 34.9/23.3 | 18.6/27.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.64 | 0.36 | 0.00 | 6.01 | 28.4/28.4 | 25.4/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.48 | 5.95 | 28.7/28.7 | 25.4/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.67 | 0.33 | 0.00 | 9.32 | 30.0/29.9 | 25.0/22.7 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.068 | 0.59 | 0.41 | 0.00 | 6.01 | 22.6/33.4 | 30.1/18.7 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.063 | 0.67 | 0.33 | 0.00 | 6.06 | 33.0/22.6 | 19.8/28.2 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.49 | 0.51 | 0.47 | 5.86 | 23.1/33.9 | 30.7/20.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
