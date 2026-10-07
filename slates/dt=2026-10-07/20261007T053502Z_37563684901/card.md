# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-07T05:35:02Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 40.00 | +3.54 | +0.91 | -1.35 | 0.396 | -40.00 | -40.00 | 6.24 |
| B thesis-diversified (joint) ← optimiser card | 15.79 | +1.40 | +0.36 | -0.57 | 0.396 | -15.79 | -15.79 | 3.15 |
| C best expression per thesis | 15.79 | +1.40 | +0.36 | -0.57 | 0.396 | -15.79 | -15.79 | 3.15 |
| R FUNDED research stakes | 4.00 | +0.35 | +0.09 | -0.14 | 0.396 | -4.00 | -4.00 | 0.00 |

## PIT @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PIT_win | p_overtime | goals | shots WSH/PIT | WSH/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.55 | 0.45 | 0.00 | 6.01 | 27.2/27.5 | 24.2/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.44 | 5.98 | 27.3/27.7 | 24.3/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.56 | 0.44 | 0.00 | 9.36 | 28.6/29.0 | 23.4/22.2 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.082 | 0.48 | 0.52 | 0.00 | 6.04 | 21.8/32.7 | 28.7/18.3 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.48 | 0.52 | 0.46 | 5.92 | 22.1/33.1 | 29.6/18.8 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.059 | 0.47 | 0.53 | 0.00 | 9.22 | 23.2/34.1 | 27.3/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Washington wins by over 1.5 goals NO | 63 | 0.689 | 0.657 | +0.043 | +0.011 | $7.91 | FUNDED_RESEARCH | $2 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Washington wins by over 1.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT07PITWSH-WSH3|no; why: higher confidence-adjusted growth (1.09 vs 0.57 bp); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: WSH wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:WINS (p 0.4729): highest fidelity KXNHLSPREAD-26OCT07PITWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT07PITWSH-WSH2|no (same contract)
- KXNHLSPREAD-26OCT07PITWSH-WSH2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.311, phi -1.0)

portfolios: A EV +1.32 (adj +0.33) on $20.00, P(profit) 0.689, adj growth 2.3 bp · B EV +0.52 (adj +0.13) on $7.91, P(profit) 0.689, adj growth 1.1 bp · C EV +0.52 (adj +0.13) on $7.91, P(profit) 0.689, adj growth 1.1 bp · R EV +0.13 (adj +0.03) on $2.00, P(profit) 0.689, adj growth 1.2 bp

## COL @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_COL_win | p_overtime | goals | shots WPG/COL | WPG/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.118 | 0.38 | 0.62 | 0.00 | 5.97 | 21.9/33.9 | 29.7/19.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.42 | 0.58 | 0.00 | 6.04 | 27.8/28.4 | 24.5/24.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.49 | 0.51 | 0.47 | 5.94 | 28.1/28.8 | 25.5/24.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.46 | 0.54 | 0.46 | 5.83 | 22.3/34.5 | 31.0/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.44 | 0.56 | 0.00 | 9.28 | 29.7/30.3 | 23.8/24.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.069 | 0.32 | 0.68 | 0.00 | 9.22 | 23.5/35.5 | 27.6/18.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado over 3.5 goals scored NO | 50 | 0.575 | 0.532 | +0.058 | +0.015 | $7.88 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado over 3.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT07COLWPG-COL2|no; why: higher confidence-adjusted growth (1.97 vs 1.12 bp); wins across more scripts (relative breadth 0.87 vs 0.605); alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:SUPPRESSED (p 0.3645): highest fidelity KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no (same contract)
- KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4142, phi -0.978)

portfolios: A EV +2.22 (adj +0.58) on $20.00, P(profit) 0.575, adj growth 4.0 bp · B EV +0.88 (adj +0.23) on $7.88, P(profit) 0.575, adj growth 2.0 bp · C EV +0.88 (adj +0.23) on $7.88, P(profit) 0.575, adj growth 2.0 bp · R EV +0.22 (adj +0.06) on $2.00, P(profit) 0.575, adj growth 2.0 bp

## EDM @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_EDM_win | p_overtime | goals | shots ANA/EDM | ANA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.134 | 0.47 | 0.53 | 0.00 | 6.05 | 28.7/28.6 | 24.9/25.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.46 | 6.04 | 28.9/28.8 | 25.5/25.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.47 | 0.53 | 0.00 | 9.37 | 30.5/30.4 | 23.9/24.6 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.077 | 0.54 | 0.46 | 0.00 | 6.0 | 33.9/23.0 | 19.8/30.1 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.064 | 0.53 | 0.47 | 0.00 | 9.4 | 36.2/24.7 | 19.0/29.1 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.51 | 0.49 | 0.47 | 5.98 | 34.2/23.2 | 19.9/30.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
