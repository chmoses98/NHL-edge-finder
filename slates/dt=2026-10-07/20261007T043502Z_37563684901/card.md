# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-07T04:35:02Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 60.00 | +4.59 | +1.18 | +5.54 | 0.568 | -33.11 | -60.00 | 7.22 |
| B thesis-diversified (joint) ← optimiser card | 19.37 | +1.49 | +0.38 | -0.22 | 0.396 | -12.46 | -19.37 | 3.36 |
| C best expression per thesis | 15.79 | +1.40 | +0.36 | -0.57 | 0.396 | -15.79 | -15.79 | 3.15 |
| R FUNDED research stakes | 6.00 | +0.46 | +0.12 | +0.55 | 0.568 | -3.31 | -6.00 | 0.00 |

## PIT @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PIT_win | p_overtime | goals | shots WSH/PIT | WSH/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.55 | 0.45 | 0.00 | 6.0 | 27.2/27.4 | 24.2/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.50 | 0.50 | 0.44 | 5.97 | 27.5/27.7 | 24.3/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.56 | 0.44 | 0.00 | 9.37 | 28.7/29.0 | 23.4/22.2 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.082 | 0.48 | 0.52 | 0.00 | 6.05 | 21.7/32.6 | 28.6/18.3 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.48 | 0.52 | 0.47 | 5.92 | 22.0/33.0 | 29.6/18.7 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.060 | 0.47 | 0.53 | 0.00 | 9.23 | 23.2/34.0 | 27.2/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Washington wins by over 1.5 goals NO | 63 | 0.689 | 0.657 | +0.043 | +0.011 | $7.91 | FUNDED_RESEARCH | $2 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Washington wins by over 1.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT07PITWSH-WSH3|no; why: higher confidence-adjusted growth (1.09 vs 0.57 bp); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: WSH wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:WINS (p 0.4729): highest fidelity KXNHLSPREAD-26OCT07PITWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT07PITWSH-WSH2|no (same contract)
- KXNHLSPREAD-26OCT07PITWSH-WSH2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.311, phi -1.0)

portfolios: A EV +1.32 (adj +0.33) on $20.00, P(profit) 0.689, adj growth 2.3 bp · B EV +0.52 (adj +0.13) on $7.91, P(profit) 0.689, adj growth 1.1 bp · C EV +0.52 (adj +0.13) on $7.91, P(profit) 0.689, adj growth 1.1 bp · R EV +0.13 (adj +0.03) on $2.00, P(profit) 0.689, adj growth 1.2 bp

## COL @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_COL_win | p_overtime | goals | shots WPG/COL | WPG/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.118 | 0.38 | 0.62 | 0.00 | 5.99 | 21.9/34.0 | 29.6/19.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.42 | 0.57 | 0.00 | 6.03 | 27.8/28.3 | 24.4/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.49 | 0.51 | 0.47 | 5.94 | 28.2/28.8 | 25.4/24.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.47 | 0.53 | 0.46 | 5.84 | 22.3/34.5 | 31.1/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.44 | 0.56 | 0.00 | 9.25 | 29.6/30.2 | 23.4/23.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.069 | 0.32 | 0.68 | 0.00 | 9.25 | 23.5/35.5 | 27.6/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado over 3.5 goals scored NO | 50 | 0.575 | 0.532 | +0.058 | +0.015 | $6.32 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 73 | 0.783 | 0.754 | +0.039 | +0.010 | $5.14 | FUNDED_RESEARCH | $2 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado over 3.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT07COLWPG-COL3|no; why: higher confidence-adjusted growth (1.97 vs 1.18 bp); relationships: KXNHLSPREAD-26OCT07COLWPG-COL3|no: REINFORCING (phi 0.516); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no has the higher standalone adjusted growth (1.97 vs 1.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.516); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no: REINFORCING (phi 0.516); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:SUPPRESSED (p 0.3645): highest fidelity KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no (same contract)
- thesis WPG:WINS (p 0.4439): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4142, phi -0.978)
- KXNHLSPREAD-26OCT07COLWPG-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3321, phi -0.747)

portfolios: A EV +3.27 (adj +0.85) on $40.00, P(profit) 0.5552, adj growth 4.9 bp · B EV +0.97 (adj +0.25) on $11.46, P(profit) 0.575, adj growth 2.2 bp · C EV +0.88 (adj +0.23) on $7.88, P(profit) 0.575, adj growth 2.0 bp · R EV +0.33 (adj +0.09) on $4.00, P(profit) 0.5552, adj growth 2.8 bp

## EDM @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_EDM_win | p_overtime | goals | shots ANA/EDM | ANA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.47 | 0.53 | 0.00 | 6.04 | 28.9/28.5 | 24.9/25.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.46 | 6.04 | 28.8/28.8 | 25.4/25.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.48 | 0.52 | 0.00 | 9.37 | 30.4/30.4 | 24.0/24.4 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.077 | 0.54 | 0.46 | 0.00 | 6.02 | 33.9/22.9 | 19.6/30.2 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.48 | 5.97 | 34.2/23.3 | 20.0/30.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.064 | 0.51 | 0.49 | 0.00 | 9.4 | 36.3/24.7 | 19.0/29.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
