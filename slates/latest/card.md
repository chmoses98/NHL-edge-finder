# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-04T05:26:45Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 39.79 | +13.74 | +4.93 | +1.24 | 0.531 | -39.79 | -39.79 | 9.30 |
| B thesis-diversified (joint) ← optimiser card | 4.30 | +2.14 | +0.80 | -1.36 | 0.159 | -4.30 | -4.30 | 6.80 |
| C best expression per thesis | 1.98 | +1.91 | +0.74 | -1.98 | 0.063 | -1.98 | -1.98 | 6.30 |
| R FUNDED research stakes | 3.00 | +1.41 | +0.52 | -0.95 | 0.159 | -3.00 | -3.00 | 0.00 |

## OTT @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_OTT_win | p_overtime | goals | shots BUF/OTT | BUF/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.53 | 0.47 | 0.00 | 5.99 | 27.3/27.3 | 23.8/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.51 | 0.49 | 0.46 | 5.96 | 27.4/27.3 | 24.0/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.54 | 0.46 | 0.00 | 9.32 | 29.1/29.1 | 23.3/22.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.073 | 0.61 | 0.39 | 0.00 | 6.08 | 32.1/21.8 | 18.9/27.9 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.063 | 0.52 | 0.48 | 0.00 | 6.07 | 22.1/32.4 | 28.7/18.5 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.52 | 0.48 | 0.45 | 5.92 | 32.5/21.8 | 18.7/29.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ FLA  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_CHI_win | p_overtime | goals | shots FLA/CHI | FLA/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.141 | 0.73 | 0.27 | 0.00 | 6.0 | 32.5/20.8 | 18.3/27.7 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.54 | 0.46 | 0.47 | 5.89 | 32.9/21.0 | 17.9/29.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.67 | 0.33 | 0.00 | 6.04 | 26.9/26.3 | 23.5/22.5 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.101 | 0.73 | 0.27 | 0.00 | 9.25 | 34.5/22.3 | 17.9/26.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.54 | 0.46 | 0.48 | 5.91 | 27.2/26.5 | 23.2/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.64 | 0.36 | 0.00 | 9.35 | 28.5/27.9 | 22.7/21.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Chicago over 5.5 goals scored YES | 3 | 0.063 | 0.044 | +0.031 | +0.012 | $1.62 | FUNDED_RESEARCH | $1 | CHI:WINS_BY_2PLUS | FRAGILE (0.26) | EVIDENCE_MIXED | D |
| Chicago over 4.5 goals scored YES | 11 | 0.159 | 0.132 | +0.042 | +0.015 | $1.24 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
| Chicago over 2.5 goals scored YES | 47 | 0.531 | 0.498 | +0.044 | +0.011 | $1.43 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Chicago over 5.5 goals scored YES** — thesis: CHI wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes; why: higher confidence-adjusted growth (9.69 vs 4.64 bp); despite a smaller raw edge (+0.031 vs +0.042/contract); relationships: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes: DUPLICATIVE (phi 0.597); KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI3|yes: REINFORCING (phi 0.243); failure: FLA wins (incl. OT/SO)
- **Chicago over 4.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6|yes has the higher standalone adjusted growth (9.69 vs 4.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.597); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6|yes: DUPLICATIVE (phi 0.597); KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI3|yes: DUPLICATIVE (phi 0.407); failure: FLA wins (incl. OT/SO)
- **Chicago over 2.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6|yes has the higher standalone adjusted growth (9.69 vs 1.02 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.243); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6|yes: REINFORCING (phi 0.243); KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes: DUPLICATIVE (phi 0.407); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.14, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:WINS_BY_2PLUS (p 0.1851): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.3076): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6|yes: FUNDED_RESEARCH; family MIXED; loses 74% of the draws where the thesis happens; opposing: failure thesis FLA:WINS (p 0.626, phi -0.298)
- KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes: FUNDED_RESEARCH; family MIXED; loses 48% of the draws where the thesis happens; opposing: failure thesis FLA:WINS (p 0.626, phi -0.432)
- KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CHI:SUPPRESSED (p 0.4775, phi -0.982)

portfolios: A EV +13.74 (adj +4.93) on $39.79, P(profit) 0.5315, adj growth 9.3 bp · B EV +2.14 (adj +0.80) on $4.30, P(profit) 0.1585, adj growth 6.8 bp · C EV +1.91 (adj +0.74) on $1.98, P(profit) 0.063, adj growth 6.3 bp · R EV +1.41 (adj +0.52) on $3.00, P(profit) 0.1585, adj growth 13.3 bp

## SJS @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_SJS_win | p_overtime | goals | shots LAK/SJS | LAK/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.61 | 0.39 | 0.00 | 5.99 | 27.9/27.6 | 24.5/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.46 | 5.91 | 28.0/27.7 | 24.5/24.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.099 | 0.66 | 0.34 | 0.00 | 5.99 | 33.2/21.9 | 19.3/28.7 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.54 | 0.46 | 0.46 | 5.87 | 33.1/21.9 | 18.7/29.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.63 | 0.37 | 0.00 | 9.17 | 29.6/29.0 | 23.8/22.9 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.064 | 0.65 | 0.35 | 0.00 | 9.24 | 34.8/23.2 | 18.4/27.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.64 | 0.36 | 0.00 | 6.01 | 28.4/28.4 | 25.4/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.46 | 5.92 | 28.7/28.6 | 25.3/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.67 | 0.33 | 0.00 | 9.32 | 30.0/30.0 | 25.0/22.7 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.067 | 0.58 | 0.42 | 0.00 | 6.0 | 22.6/33.5 | 30.3/18.8 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.065 | 0.69 | 0.31 | 0.00 | 6.07 | 33.1/22.6 | 19.9/28.5 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.48 | 0.52 | 0.48 | 5.89 | 23.0/33.7 | 30.4/19.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
