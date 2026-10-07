# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-07T10:28:59Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 70.00 | +11.21 | +3.67 | -0.57 | 0.353 | -70.00 | -70.00 | 12.39 |
| B thesis-diversified (joint) ← optimiser card | 19.22 | +2.43 | +0.77 | +2.63 | 0.510 | -19.22 | -19.22 | 6.76 |
| C best expression per thesis | 19.46 | +2.06 | +0.64 | +3.30 | 0.575 | -19.46 | -19.46 | 5.63 |
| R FUNDED research stakes | 6.00 | +0.91 | +0.29 | +1.04 | 0.510 | -6.00 | -6.00 | 0.00 |

## PIT @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PIT_win | p_overtime | goals | shots WSH/PIT | WSH/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.54 | 0.46 | 0.00 | 6.02 | 27.2/27.5 | 24.0/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.47 | 5.97 | 27.4/27.7 | 24.3/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.56 | 0.44 | 0.00 | 9.35 | 28.6/28.9 | 23.2/22.2 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.083 | 0.48 | 0.52 | 0.00 | 6.04 | 21.8/32.7 | 28.6/18.4 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.48 | 0.52 | 0.45 | 5.93 | 21.8/32.6 | 29.1/18.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.062 | 0.48 | 0.52 | 0.00 | 9.31 | 23.4/34.2 | 27.0/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Washington wins by over 1.5 goals NO | 63 | 0.689 | 0.657 | +0.043 | +0.011 | $7.91 | FUNDED_RESEARCH | $2 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Washington wins by over 1.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT07PITWSH-WSH3|no; why: higher confidence-adjusted growth (1.09 vs 0.06 bp); alternative not eligible: confidence-adjusted EV +0.0022 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: WSH wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:WINS (p 0.4729): highest fidelity KXNHLSPREAD-26OCT07PITWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT07PITWSH-WSH2|no (same contract)
- KXNHLSPREAD-26OCT07PITWSH-WSH2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.311, phi -1.0)

portfolios: A EV +1.32 (adj +0.33) on $20.00, P(profit) 0.689, adj growth 2.3 bp · B EV +0.52 (adj +0.13) on $7.91, P(profit) 0.689, adj growth 1.1 bp · C EV +0.52 (adj +0.13) on $7.91, P(profit) 0.689, adj growth 1.1 bp · R EV +0.13 (adj +0.03) on $2.00, P(profit) 0.689, adj growth 1.2 bp

## COL @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_COL_win | p_overtime | goals | shots WPG/COL | WPG/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.118 | 0.38 | 0.62 | 0.00 | 5.99 | 21.9/34.0 | 29.6/19.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.43 | 0.57 | 0.00 | 6.02 | 27.7/28.3 | 24.4/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.49 | 0.51 | 0.47 | 5.94 | 28.2/28.8 | 25.4/24.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.46 | 0.54 | 0.46 | 5.84 | 22.3/34.5 | 31.1/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.44 | 0.56 | 0.00 | 9.25 | 29.6/30.2 | 23.4/23.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.069 | 0.32 | 0.68 | 0.00 | 9.25 | 23.5/35.5 | 27.6/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado over 3.5 goals scored NO | 49 | 0.575 | 0.530 | +0.068 | +0.022 | $7.81 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado over 2.5 goals scored NO | 28 | 0.353 | 0.314 | +0.059 | +0.020 | $1.90 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Colorado over 1.5 goals scored NO | 12 | 0.167 | 0.141 | +0.039 | +0.013 | $1.60 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | FRAGILE (0.46) | EVIDENCE_MIXED | D |
- **Colorado over 3.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT07COLWPG-COL3|no; why: higher confidence-adjusted growth (4.43 vs 4.21 bp); relationships: KXNHLTEAMTOTAL-26OCT07COLWPG-COL3|no: DUPLICATIVE (phi 0.635); KXNHLTEAMTOTAL-26OCT07COLWPG-COL2|no: DUPLICATIVE (phi 0.384); failure: COL offense succeeds (4+ goals)
- **Colorado over 2.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no has the higher standalone adjusted growth (4.43 vs 4.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.635); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no: DUPLICATIVE (phi 0.635); KXNHLTEAMTOTAL-26OCT07COLWPG-COL2|no: DUPLICATIVE (phi 0.605); failure: COL offense succeeds (4+ goals)
- **Colorado over 1.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no has the higher standalone adjusted growth (4.43 vs 3.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.384); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no: DUPLICATIVE (phi 0.384); KXNHLTEAMTOTAL-26OCT07COLWPG-COL3|no: DUPLICATIVE (phi 0.605); failure: COL wins (incl. OT/SO)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:SUPPRESSED (p 0.3645): highest fidelity KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no (same contract)
- thesis WPG:WINS (p 0.4439): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4142, phi -0.978)
- KXNHLTEAMTOTAL-26OCT07COLWPG-COL3|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4142, phi -0.622)
- KXNHLTEAMTOTAL-26OCT07COLWPG-COL2|no: FUNDED_RESEARCH; family MIXED; loses 54% of the draws where the thesis happens; opposing: failure thesis COL:WINS (p 0.5561, phi -0.451)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT07COLWPG-COL3|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT07COLWPG-COL3|no kept
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT07COLWPG-COL3|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT07COLWPG-COL2|no kept

portfolios: A EV +9.89 (adj +3.34) on $50.00, P(profit) 0.3533, adj growth 10.1 bp · B EV +1.91 (adj +0.64) on $11.31, P(profit) 0.575, adj growth 5.6 bp · C EV +1.54 (adj +0.51) on $11.55, P(profit) 0.575, adj growth 4.5 bp · R EV +0.77 (adj +0.26) on $4.00, P(profit) 0.3533, adj growth 8.2 bp

## EDM @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_EDM_win | p_overtime | goals | shots ANA/EDM | ANA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.47 | 0.53 | 0.00 | 6.04 | 28.9/28.6 | 24.9/25.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.46 | 6.03 | 28.8/28.8 | 25.4/25.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.48 | 0.52 | 0.00 | 9.37 | 30.4/30.3 | 24.0/24.3 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.077 | 0.54 | 0.46 | 0.00 | 6.02 | 33.9/22.9 | 19.6/30.2 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.48 | 5.97 | 34.2/23.3 | 20.0/30.6 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.064 | 0.51 | 0.49 | 0.00 | 9.4 | 36.3/24.7 | 19.0/29.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
