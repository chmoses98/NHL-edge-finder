# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-04T12:08:23Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +5.79 | +1.69 | -5.78 | 0.467 | -50.00 | -50.00 | 7.91 |
| B thesis-diversified (joint) ← optimiser card | 11.20 | +1.74 | +0.57 | -1.01 | 0.318 | -11.20 | -11.20 | 4.99 |
| C best expression per thesis | 7.51 | +1.51 | +0.51 | +0.48 | 0.604 | -7.51 | -7.51 | 4.40 |
| R FUNDED research stakes | 5.00 | +0.77 | +0.25 | -0.41 | 0.318 | -5.00 | -5.00 | 0.00 |

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

## CHI @ FLA  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 4 on card


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
| Chicago over 4.5 goals scored YES | 11 | 0.159 | 0.132 | +0.042 | +0.015 | $2.34 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
| Chicago over 3.5 goals scored YES | 25 | 0.318 | 0.281 | +0.055 | +0.018 | $2.19 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 53 | 0.597 | 0.561 | +0.049 | +0.013 | $2.17 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Chicago over 1.5 goals scored YES | 71 | 0.766 | 0.736 | +0.042 | +0.011 | $4.50 | FUNDED_RESEARCH | $2 | CHI:WINS | DIRECT (0.98) | EVIDENCE_MIXED | D |
- **Chicago over 4.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes; why: higher confidence-adjusted growth (4.64 vs 3.77 bp); despite a smaller raw edge (+0.042 vs +0.055/contract); relationships: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes: DUPLICATIVE (phi 0.636); KXNHLSPREAD-26NOV04CHIFLA-FLA2|no: REINFORCING (phi 0.317); KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2|yes: REINFORCING (phi 0.24); failure: FLA wins (incl. OT/SO)
- **Chicago over 3.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes has the higher standalone adjusted growth (4.64 vs 3.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.636); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes: DUPLICATIVE (phi 0.636); KXNHLSPREAD-26NOV04CHIFLA-FLA2|no: REINFORCING (phi 0.419); KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2|yes: DUPLICATIVE (phi 0.377); failure: CHI offense suppressed (<= 2 goals)
- **Florida wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2|yes; why: higher confidence-adjusted growth (1.60 vs 1.40 bp); relationships: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes: REINFORCING (phi 0.317); KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes: REINFORCING (phi 0.419); KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2|yes: REINFORCING (phi 0.428); failure: FLA wins by 2+
- **Chicago over 1.5 goals scored YES** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes has the higher standalone adjusted growth (4.64 vs 1.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.240); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes: REINFORCING (phi 0.24); KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes: DUPLICATIVE (phi 0.377); KXNHLSPREAD-26NOV04CHIFLA-FLA2|no: REINFORCING (phi 0.428); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.14, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3076): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes (same contract)
- thesis CHI:WINS (p 0.374): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4117): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV04CHIFLA-FLA2|no (same contract)
- KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes: FUNDED_RESEARCH; family MIXED; loses 48% of the draws where the thesis happens; opposing: failure thesis FLA:WINS (p 0.626, phi -0.432)
- KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CHI:SUPPRESSED (p 0.4775, phi -0.653)
- KXNHLSPREAD-26NOV04CHIFLA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.4032, phi -1.0)
- KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2|yes: FUNDED_RESEARCH; family MIXED; loses 2% of the draws where the thesis happens; opposing: failure thesis CHI:SUPPRESSED (p 0.4775, phi -0.578)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI3|yes less than the minimum stake; KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5|yes kept

portfolios: A EV +5.79 (adj +1.69) on $50.00, P(profit) 0.4669, adj growth 7.9 bp · B EV +1.74 (adj +0.57) on $11.20, P(profit) 0.3179, adj growth 5.0 bp · C EV +1.51 (adj +0.51) on $7.51, P(profit) 0.604, adj growth 4.4 bp · R EV +0.77 (adj +0.25) on $5.00, P(profit) 0.3179, adj growth 7.8 bp

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
