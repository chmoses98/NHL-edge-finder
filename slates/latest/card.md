# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T04:18:20Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +9.15 | +2.31 | +2.51 | 0.692 | -50.00 | -50.00 | 14.57 |
| B thesis-diversified (joint) ← optimiser card | 22.06 | +3.18 | +0.86 | +1.64 | 0.718 | -22.06 | -22.06 | 7.55 |
| C best expression per thesis | 19.54 | +3.21 | +0.85 | -0.37 | 0.377 | -19.54 | -19.54 | 7.44 |
| R FUNDED research stakes | 7.00 | +1.05 | +0.29 | +0.02 | 0.718 | -7.00 | -7.00 | 0.00 |

## ANA @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_ANA_win | p_overtime | goals | shots NYR/ANA | NYR/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.57 | 0.43 | 0.00 | 6.03 | 26.8/27.3 | 24.1/22.8 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.104 | 0.49 | 0.51 | 0.00 | 6.03 | 21.2/32.6 | 28.9/17.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.51 | 0.49 | 0.47 | 5.96 | 26.5/27.0 | 23.8/23.2 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.45 | 0.55 | 0.46 | 5.98 | 21.3/32.8 | 29.3/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.59 | 0.41 | 0.00 | 9.36 | 28.5/29.0 | 23.5/22.0 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.079 | 0.51 | 0.49 | 0.00 | 9.32 | 22.8/34.3 | 28.0/17.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_COL_win | p_overtime | goals | shots PHI/COL | PHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.138 | 0.39 | 0.61 | 0.00 | 5.99 | 21.4/33.3 | 29.1/18.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.129 | 0.46 | 0.54 | 0.47 | 5.86 | 21.5/33.9 | 30.6/18.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.101 | 0.45 | 0.55 | 0.00 | 5.95 | 26.9/27.9 | 24.2/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.49 | 0.51 | 0.48 | 5.87 | 27.0/28.0 | 24.9/23.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.081 | 0.36 | 0.64 | 0.00 | 9.09 | 22.6/35.0 | 27.7/18.0 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.070 | 0.42 | 0.58 | 0.00 | 3.46 | 20.0/32.2 | 29.9/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado over 2.5 goals scored NO | 29 | 0.377 | 0.329 | +0.073 | +0.024 | $5.17 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 69 | 0.798 | 0.724 | +0.093 | +0.019 | $10.40 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado over 4.5 goals scored NO | 71 | 0.790 | 0.742 | +0.065 | +0.018 | $6.48 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado over 2.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT19COLPHI-COL3|no; why: higher confidence-adjusted growth (5.96 vs 3.99 bp); despite a smaller raw edge (+0.073 vs +0.093/contract); relationships: KXNHLSPREAD-26OCT19COLPHI-COL3|no: DUPLICATIVE (phi 0.392); KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: DUPLICATIVE (phi 0.402); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no; why: higher confidence-adjusted growth (3.99 vs 3.52 bp); wins across more scripts (relative breadth 1.0 vs 0.897); relationships: KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no: DUPLICATIVE (phi 0.392); KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: REINFORCING (phi 0.536); failure: COL wins by 2+
- **Colorado over 4.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no has the higher standalone adjusted growth (5.96 vs 3.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.402); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no: DUPLICATIVE (phi 0.402); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.536); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis COL:SUPPRESSED (p 0.3909): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2312): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4494): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL3|no (same contract)
- KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.618)
- KXNHLSPREAD-26OCT19COLPHI-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.3 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3194, phi -0.735)
- KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.649)

portfolios: A EV +9.15 (adj +2.31) on $50.00, P(profit) 0.6921, adj growth 14.6 bp · B EV +3.18 (adj +0.86) on $22.06, P(profit) 0.7175, adj growth 7.5 bp · C EV +3.21 (adj +0.85) on $19.54, P(profit) 0.377, adj growth 7.4 bp · R EV +1.05 (adj +0.29) on $7.00, P(profit) 0.7175, adj growth 9.7 bp

## SJS @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_SJS_win | p_overtime | goals | shots TOR/SJS | TOR/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.58 | 0.42 | 0.00 | 6.05 | 28.0/28.4 | 25.2/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.53 | 0.47 | 0.45 | 5.91 | 28.0/28.3 | 25.1/24.5 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.088 | 0.48 | 0.52 | 0.00 | 5.98 | 22.2/33.6 | 29.8/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.53 | 0.47 | 0.00 | 9.37 | 29.8/30.0 | 24.0/23.4 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.45 | 0.55 | 0.51 | 5.92 | 22.6/33.9 | 30.4/19.5 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.059 | 0.51 | 0.49 | 0.00 | 9.32 | 24.1/35.2 | 28.6/18.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, SJS shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_PIT_win | p_overtime | goals | shots UTA/PIT | UTA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.63 | 0.37 | 0.00 | 6.05 | 27.2/27.0 | 24.0/23.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.62 | 0.38 | 0.00 | 9.45 | 28.9/28.5 | 23.0/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.47 | 6.03 | 27.4/27.3 | 23.9/23.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.085 | 0.68 | 0.32 | 0.00 | 6.0 | 32.2/21.3 | 18.7/27.6 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.54 | 0.46 | 0.47 | 5.96 | 32.2/21.7 | 18.3/28.8 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.071 | 0.70 | 0.30 | 0.00 | 9.38 | 34.0/23.2 | 18.6/26.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
