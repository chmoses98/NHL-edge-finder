# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-28T06:55:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 70.00 | +7.40 | +1.69 | +31.32 | 0.730 | -45.35 | -45.35 | 12.34 |
| B thesis-diversified (joint) ← optimiser card | 42.45 | +3.84 | +1.15 | +12.89 | 0.662 | -18.81 | -18.81 | 10.14 |
| C best expression per thesis | 39.17 | +3.02 | +0.96 | +12.83 | 0.662 | -15.54 | -15.54 | 8.57 |
| R FUNDED research stakes | 12.00 | +1.17 | +0.35 | +3.02 | 0.697 | -5.84 | -5.84 | 0.00 |

## PHI @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PHI_win | p_overtime | goals | shots WSH/PHI | WSH/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.60 | 0.40 | 0.00 | 5.96 | 26.5/26.4 | 23.2/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.50 | 5.88 | 26.8/26.5 | 23.4/23.6 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.093 | 0.63 | 0.37 | 0.00 | 5.97 | 31.5/21.0 | 18.2/27.3 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.56 | 0.44 | 0.47 | 5.86 | 31.9/21.2 | 18.2/28.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.59 | 0.41 | 0.00 | 9.25 | 28.3/28.0 | 22.6/21.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.58 | 0.42 | 0.00 | 3.47 | 25.4/25.1 | 23.5/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Washington over 4.5 goals scored NO | 69 | 0.777 | 0.728 | +0.072 | +0.023 | $17.77 | FUNDED_RESEARCH | $5 | WSH:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Washington wins by over 1.5 goals NO | 55 | 0.664 | 0.587 | +0.097 | +0.019 | $3.69 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Philadelphia wins by over 1.5 goals YES | 17 | 0.222 | 0.193 | +0.042 | +0.013 | $1.82 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Washington over 4.5 goals scored NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT28PHIWSH-WSH2|no; why: higher confidence-adjusted growth (5.78 vs 3.37 bp); despite a smaller raw edge (+0.072 vs +0.097/contract); relationships: KXNHLSPREAD-26OCT28PHIWSH-WSH2|no: REINFORCING (phi 0.494); KXNHLSPREAD-26OCT28PHIWSH-PHI2|yes: REINFORCING (phi 0.267); failure: WSH offense succeeds (4+ goals)
- **Washington wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no has the higher standalone adjusted growth (5.78 vs 3.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.494); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no: REINFORCING (phi 0.494); KXNHLSPREAD-26OCT28PHIWSH-PHI2|yes: DUPLICATIVE (phi 0.379); failure: WSH wins by 2+
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no has the higher standalone adjusted growth (5.78 vs 2.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.267); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no: REINFORCING (phi 0.267); KXNHLSPREAD-26OCT28PHIWSH-WSH2|no: DUPLICATIVE (phi 0.379); failure: WSH wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:SUPPRESSED (p 0.3834): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no (same contract)
- thesis GAME:TIGHT (p 0.4427): highest fidelity KXNHLSPREAD-26OCT28PHIWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2216): highest fidelity KXNHLSPREAD-26OCT28PHIWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4038, phi -0.652)
- KXNHLSPREAD-26OCT28PHIWSH-WSH2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.9 pts; opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.3357, phi -1.0)
- KXNHLSPREAD-26OCT28PHIWSH-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS (p 0.5698, phi -0.614)

portfolios: A EV +6.37 (adj +1.38) on $50.00, P(profit) 0.6643, adj growth 9.6 bp · B EV +2.86 (adj +0.85) on $23.28, P(profit) 0.7767, adj growth 7.5 bp · C EV +2.03 (adj +0.66) on $20.00, P(profit) 0.7767, adj growth 5.9 bp · R EV +0.91 (adj +0.27) on $7.00, P(profit) 0.78, adj growth 9.2 bp

## CGY @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CGY_win | p_overtime | goals | shots EDM/CGY | EDM/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.75 | 0.25 | 0.00 | 6.07 | 28.9/28.5 | 25.9/24.2 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.112 | 0.77 | 0.23 | 0.00 | 6.11 | 34.1/22.3 | 20.0/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.109 | 0.74 | 0.26 | 0.00 | 9.47 | 30.7/30.1 | 25.2/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.57 | 0.43 | 0.47 | 5.98 | 28.9/28.3 | 25.2/25.4 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.097 | 0.78 | 0.22 | 0.00 | 9.44 | 36.2/24.0 | 19.8/27.0 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.59 | 0.41 | 0.44 | 5.99 | 34.8/22.9 | 19.7/30.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, EDM shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NJD_win | p_overtime | goals | shots COL/NJD | COL/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.68 | 0.32 | 0.00 | 6.04 | 28.7/28.7 | 26.0/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.54 | 0.46 | 0.48 | 5.93 | 28.7/28.6 | 25.3/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.68 | 0.32 | 0.00 | 9.34 | 30.4/30.2 | 25.1/23.2 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.086 | 0.73 | 0.27 | 0.00 | 6.01 | 33.8/22.8 | 20.3/29.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.57 | 0.43 | 0.47 | 5.89 | 33.6/23.0 | 20.0/30.2 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.060 | 0.60 | 0.40 | 0.00 | 5.97 | 22.9/33.2 | 30.1/19.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_TOR_win | p_overtime | goals | shots SEA/TOR | SEA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.57 | 0.43 | 0.00 | 6.07 | 29.2/29.0 | 25.7/25.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.45 | 6.02 | 29.2/29.2 | 25.8/25.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.56 | 0.44 | 0.00 | 9.43 | 30.9/30.8 | 24.8/24.1 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.082 | 0.64 | 0.36 | 0.00 | 6.06 | 34.7/23.3 | 20.4/30.1 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.53 | 0.47 | 0.50 | 6.0 | 34.8/23.3 | 19.9/31.4 | even strength |
| SEA shot control · high event (8+) · decided (2+) | 0.062 | 0.59 | 0.41 | 0.00 | 9.32 | 36.2/24.9 | 19.6/28.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Toronto wins by over 2.5 goals NO | 80 | 0.853 | 0.824 | +0.042 | +0.013 | $19.17 | FUNDED_RESEARCH | $5 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Toronto wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT28TORSEA-SEA2|yes; why: higher confidence-adjusted growth (2.32 vs 0.90 bp); wins across more scripts (relative breadth 1.029 vs 0.526); alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: TOR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis SEA:WINS (p 0.5451): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR3|no (same contract)
- KXNHLSPREAD-26OCT28TORSEA-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2467, phi -0.726)

portfolios: A EV +1.03 (adj +0.31) on $20.00, P(profit) 0.8528, adj growth 2.7 bp · B EV +0.98 (adj +0.30) on $19.17, P(profit) 0.8528, adj growth 2.6 bp · C EV +0.98 (adj +0.30) on $19.17, P(profit) 0.8528, adj growth 2.6 bp · R EV +0.26 (adj +0.08) on $5.00, P(profit) 0.8528, adj growth 2.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
