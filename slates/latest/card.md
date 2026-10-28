# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-28T05:07:59Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 90.00 | +8.18 | +1.72 | +10.49 | 0.624 | -36.98 | -43.04 | 11.11 |
| B thesis-diversified (joint) ← optimiser card | 34.14 | +2.77 | +0.81 | +7.84 | 0.607 | -16.82 | -17.94 | 7.08 |
| C best expression per thesis | 35.02 | +2.36 | +0.66 | +10.79 | 0.662 | -12.85 | -12.85 | 5.80 |
| R FUNDED research stakes | 11.00 | +0.92 | +0.27 | +2.36 | 0.639 | -5.40 | -6.07 | 0.00 |

## PHI @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PHI_win | p_overtime | goals | shots WSH/PHI | WSH/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.60 | 0.40 | 0.00 | 5.97 | 26.6/26.4 | 23.3/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.52 | 0.48 | 0.48 | 5.89 | 26.9/26.7 | 23.5/23.6 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.093 | 0.65 | 0.35 | 0.00 | 5.98 | 31.5/21.0 | 18.3/27.1 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.56 | 0.44 | 0.47 | 5.83 | 31.5/21.0 | 18.0/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.60 | 0.40 | 0.00 | 9.23 | 28.4/28.1 | 22.7/21.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.57 | 0.43 | 0.00 | 3.49 | 25.7/25.5 | 23.9/23.4 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Washington over 4.5 goals scored NO | 70 | 0.777 | 0.731 | +0.062 | +0.016 | $12.38 | FUNDED_RESEARCH | $4 | WSH:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Philadelphia wins by over 1.5 goals YES | 17 | 0.222 | 0.193 | +0.042 | +0.013 | $2.66 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Washington over 4.5 goals scored NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT28PHIWSH-PHI2|yes; why: higher confidence-adjusted growth (2.81 vs 2.65 bp); wins across more scripts (relative breadth 0.884 vs 0.531); relationships: KXNHLSPREAD-26OCT28PHIWSH-PHI2|yes: REINFORCING (phi 0.267); failure: WSH offense succeeds (4+ goals)
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no has the higher standalone adjusted growth (2.81 vs 2.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.267); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no: REINFORCING (phi 0.267); failure: WSH wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:SUPPRESSED (p 0.3834): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no (same contract)
- thesis PHI:WINS_BY_2PLUS (p 0.2216): highest fidelity KXNHLSPREAD-26OCT28PHIWSH-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4427): highest fidelity KXNHLSPREAD-26OCT28PHIWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4038, phi -0.652)
- KXNHLSPREAD-26OCT28PHIWSH-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS (p 0.5698, phi -0.614)

portfolios: A EV +5.79 (adj +1.00) on $50.00, P(profit) 0.6643, adj growth 5.9 bp · B EV +1.69 (adj +0.48) on $15.04, P(profit) 0.7767, adj growth 4.2 bp · C EV +1.37 (adj +0.36) on $15.85, P(profit) 0.7767, adj growth 3.1 bp · R EV +0.58 (adj +0.17) on $5.00, P(profit) 0.78, adj growth 5.5 bp

## CGY @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CGY_win | p_overtime | goals | shots EDM/CGY | EDM/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.74 | 0.26 | 0.00 | 6.09 | 28.7/28.4 | 25.9/23.9 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.109 | 0.77 | 0.23 | 0.00 | 6.08 | 34.1/22.4 | 20.0/28.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.73 | 0.27 | 0.00 | 9.47 | 30.5/29.9 | 25.1/22.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.099 | 0.79 | 0.21 | 0.00 | 9.46 | 36.2/24.1 | 19.9/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.56 | 0.44 | 0.47 | 5.99 | 28.8/28.3 | 25.0/25.2 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.58 | 0.42 | 0.44 | 5.98 | 34.8/22.9 | 19.8/31.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, EDM shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NJD_win | p_overtime | goals | shots COL/NJD | COL/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.68 | 0.32 | 0.00 | 6.03 | 28.6/28.6 | 25.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.57 | 0.43 | 0.48 | 5.91 | 28.6/28.5 | 25.4/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.69 | 0.31 | 0.00 | 9.3 | 30.4/30.3 | 25.2/22.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.085 | 0.72 | 0.28 | 0.00 | 6.03 | 33.8/22.8 | 20.4/29.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.53 | 0.47 | 0.46 | 5.94 | 33.7/22.9 | 19.7/30.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.060 | 0.62 | 0.38 | 0.00 | 5.97 | 23.0/33.8 | 30.4/19.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_TOR_win | p_overtime | goals | shots SEA/TOR | SEA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.58 | 0.42 | 0.00 | 6.07 | 29.2/29.1 | 25.9/25.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.49 | 0.51 | 0.45 | 6.02 | 29.4/29.3 | 25.8/26.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.109 | 0.54 | 0.46 | 0.00 | 9.4 | 31.1/30.8 | 24.6/24.7 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 6.05 | 34.9/23.4 | 20.3/30.5 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.53 | 0.47 | 0.47 | 5.96 | 34.5/23.3 | 20.1/31.0 | even strength |
| SEA shot control · high event (8+) · decided (2+) | 0.062 | 0.65 | 0.35 | 0.00 | 9.3 | 36.3/24.7 | 19.7/28.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Toronto wins by over 2.5 goals NO | 80 | 0.853 | 0.824 | +0.042 | +0.013 | $13.14 | FUNDED_RESEARCH | $4 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Toronto wins by over 1.5 goals NO | 69 | 0.753 | 0.719 | +0.048 | +0.014 | $5.96 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Toronto wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (2.32 vs 2.12 bp); despite a smaller raw edge (+0.042 vs +0.048/contract); relationships: KXNHLSPREAD-26OCT28TORSEA-TOR2|no: DUPLICATIVE (phi 0.726); failure: TOR wins by 2+
- **Toronto wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT28TORSEA-TOR3|no has the higher standalone adjusted growth (2.32 vs 2.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.726); they share one thesis budget; relationships: KXNHLSPREAD-26OCT28TORSEA-TOR3|no: DUPLICATIVE (phi 0.726); failure: TOR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis SEA:WINS (p 0.5451): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no (same contract)
- KXNHLSPREAD-26OCT28TORSEA-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2467, phi -0.726)
- KXNHLSPREAD-26OCT28TORSEA-TOR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2467, phi -1.0)

portfolios: A EV +2.40 (adj +0.72) on $40.00, P(profit) 0.7533, adj growth 5.2 bp · B EV +1.08 (adj +0.33) on $19.10, P(profit) 0.7533, adj growth 2.9 bp · C EV +0.98 (adj +0.30) on $19.17, P(profit) 0.8528, adj growth 2.6 bp · R EV +0.34 (adj +0.10) on $6.00, P(profit) 0.7533, adj growth 3.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
