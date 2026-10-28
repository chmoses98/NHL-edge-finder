# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-28T04:08:09Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 70.00 | +9.74 | +1.67 | +7.17 | 0.632 | -45.35 | -45.35 | 7.29 |
| B thesis-diversified (joint) ← optimiser card | 36.15 | +3.04 | +0.83 | +9.19 | 0.664 | -14.45 | -21.02 | 7.26 |
| C best expression per thesis | 35.02 | +2.36 | +0.66 | +10.79 | 0.662 | -12.85 | -12.85 | 5.80 |
| R FUNDED research stakes | 10.00 | +0.90 | +0.25 | +2.09 | 0.697 | -4.07 | -5.80 | 0.00 |

## PHI @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PHI_win | p_overtime | goals | shots WSH/PHI | WSH/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.59 | 0.41 | 0.00 | 5.96 | 26.6/26.5 | 23.4/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.52 | 0.48 | 0.49 | 5.89 | 27.0/26.8 | 23.6/23.7 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.094 | 0.64 | 0.36 | 0.00 | 5.98 | 31.5/20.9 | 18.2/27.1 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.56 | 0.44 | 0.47 | 5.83 | 31.6/21.1 | 18.1/28.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.59 | 0.41 | 0.00 | 9.23 | 28.3/28.0 | 22.6/21.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.58 | 0.42 | 0.00 | 3.49 | 25.4/25.3 | 23.7/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Washington over 4.5 goals scored NO | 70 | 0.777 | 0.731 | +0.062 | +0.016 | $10.82 | FUNDED_RESEARCH | $3 | WSH:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Philadelphia wins by over 1.5 goals YES | 17 | 0.222 | 0.193 | +0.042 | +0.013 | $2.37 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Washington wins by over 1.5 goals NO | 56 | 0.664 | 0.593 | +0.087 | +0.016 | $3.79 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Washington over 4.5 goals scored NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT28PHIWSH-PHI2|yes; why: higher confidence-adjusted growth (2.81 vs 2.65 bp); wins across more scripts (relative breadth 0.883 vs 0.528); relationships: KXNHLSPREAD-26OCT28PHIWSH-PHI2|yes: REINFORCING (phi 0.267); KXNHLSPREAD-26OCT28PHIWSH-WSH2|no: REINFORCING (phi 0.494); failure: WSH offense succeeds (4+ goals)
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no has the higher standalone adjusted growth (2.81 vs 2.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.267); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no: REINFORCING (phi 0.267); KXNHLSPREAD-26OCT28PHIWSH-WSH2|no: DUPLICATIVE (phi 0.379); failure: WSH wins (incl. OT/SO)
- **Washington wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no has the higher standalone adjusted growth (2.81 vs 2.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.494); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no: REINFORCING (phi 0.494); KXNHLSPREAD-26OCT28PHIWSH-PHI2|yes: DUPLICATIVE (phi 0.379); failure: WSH wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:SUPPRESSED (p 0.3834): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no (same contract)
- thesis PHI:WINS_BY_2PLUS (p 0.2216): highest fidelity KXNHLSPREAD-26OCT28PHIWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4427): highest fidelity KXNHLSPREAD-26OCT28PHIWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4038, phi -0.652)
- KXNHLSPREAD-26OCT28PHIWSH-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS (p 0.5698, phi -0.614)
- KXNHLSPREAD-26OCT28PHIWSH-WSH2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.9 pts; opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.3357, phi -1.0)

portfolios: A EV +8.72 (adj +1.36) on $50.00, P(profit) 0.6761, adj growth 4.5 bp · B EV +2.06 (adj +0.53) on $16.98, P(profit) 0.6165, adj growth 4.6 bp · C EV +1.37 (adj +0.36) on $15.85, P(profit) 0.7767, adj growth 3.1 bp · R EV +0.64 (adj +0.17) on $5.00, P(profit) 0.6165, adj growth 5.7 bp

## CGY @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CGY_win | p_overtime | goals | shots EDM/CGY | EDM/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.73 | 0.27 | 0.00 | 6.07 | 28.8/28.5 | 25.9/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.73 | 0.27 | 0.00 | 9.49 | 30.6/30.0 | 25.1/22.7 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.109 | 0.77 | 0.23 | 0.00 | 6.09 | 34.1/22.3 | 20.0/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.56 | 0.44 | 0.47 | 5.98 | 29.0/28.3 | 25.1/25.4 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.096 | 0.79 | 0.21 | 0.00 | 9.45 | 36.3/24.0 | 19.9/27.2 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.58 | 0.42 | 0.45 | 6.0 | 34.8/23.0 | 19.9/31.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, EDM shot control · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NJD_win | p_overtime | goals | shots COL/NJD | COL/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.68 | 0.32 | 0.00 | 6.02 | 28.5/28.5 | 25.8/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.57 | 0.43 | 0.49 | 5.95 | 28.6/28.4 | 25.3/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.67 | 0.33 | 0.00 | 9.33 | 30.4/30.2 | 25.0/22.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.085 | 0.71 | 0.29 | 0.00 | 6.04 | 34.0/23.0 | 20.6/29.2 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.53 | 0.47 | 0.45 | 5.91 | 33.7/22.9 | 19.8/30.1 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.059 | 0.77 | 0.23 | 0.00 | 9.25 | 35.2/24.0 | 19.9/26.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_TOR_win | p_overtime | goals | shots SEA/TOR | SEA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.59 | 0.41 | 0.00 | 6.05 | 29.3/29.2 | 26.0/25.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.50 | 0.50 | 0.47 | 5.98 | 29.4/29.4 | 25.9/26.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.58 | 0.42 | 0.00 | 9.36 | 31.0/30.9 | 25.0/24.4 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.083 | 0.59 | 0.41 | 0.00 | 6.06 | 34.9/23.5 | 20.4/30.6 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.44 | 6.0 | 34.4/23.0 | 19.8/30.8 | even strength |
| SEA shot control · high event (8+) · decided (2+) | 0.064 | 0.61 | 0.39 | 0.00 | 9.34 | 36.0/24.5 | 19.4/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Toronto wins by over 2.5 goals NO | 80 | 0.853 | 0.824 | +0.042 | +0.013 | $19.17 | FUNDED_RESEARCH | $5 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Toronto wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT28TORSEA-SEA2|yes; why: higher confidence-adjusted growth (2.32 vs 0.90 bp); wins across more scripts (relative breadth 1.02 vs 0.521); alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: TOR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis SEA:WINS (p 0.5451): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR3|no (same contract)
- KXNHLSPREAD-26OCT28TORSEA-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2467, phi -0.726)

portfolios: A EV +1.03 (adj +0.31) on $20.00, P(profit) 0.8528, adj growth 2.7 bp · B EV +0.98 (adj +0.30) on $19.17, P(profit) 0.8528, adj growth 2.6 bp · C EV +0.98 (adj +0.30) on $19.17, P(profit) 0.8528, adj growth 2.6 bp · R EV +0.26 (adj +0.08) on $5.00, P(profit) 0.8528, adj growth 2.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
