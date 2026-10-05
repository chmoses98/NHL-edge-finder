# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-05T11:08:48Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +4.90 | +1.43 | +31.37 | 0.714 | -50.00 | -50.00 | 9.05 |
| B thesis-diversified (joint) ← optimiser card | 22.47 | +2.06 | +0.71 | +9.69 | 0.788 | -22.47 | -22.47 | 6.26 |
| C best expression per thesis | 20.00 | +1.77 | +0.62 | +7.61 | 0.788 | -20.00 | -20.00 | 5.51 |
| R FUNDED research stakes | 6.00 | +0.55 | +0.19 | +2.58 | 0.788 | -6.00 | -6.00 | 0.00 |

## PHI @ TBL  ·  10000 joint draws  ·  342 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_PHI_win | p_overtime | goals | shots TBL/PHI | TBL/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.123 | 0.69 | 0.31 | 0.00 | 5.98 | 31.6/20.2 | 17.6/27.0 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.55 | 0.45 | 0.49 | 5.84 | 31.7/20.6 | 17.6/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.58 | 0.42 | 0.00 | 5.96 | 26.3/25.7 | 22.5/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.52 | 0.48 | 0.50 | 5.89 | 26.4/26.1 | 22.9/23.3 | even strength |
| TBL shot control · low event (<=4) · decided (2+) | 0.069 | 0.65 | 0.35 | 0.00 | 3.44 | 30.1/19.2 | 17.9/27.6 | even strength |
| TBL shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.53 | 0.47 | 0.45 | 2.71 | 30.0/19.2 | 17.9/28.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 2.5 goals NO | 71 | 0.788 | 0.747 | +0.064 | +0.022 | $18.61 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 58 | 0.662 | 0.618 | +0.065 | +0.021 | $3.86 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT05PHITB-TB2|no; why: higher confidence-adjusted growth (5.48 vs 4.15 bp); despite a smaller raw edge (+0.064 vs +0.065/contract); wins across more scripts (relative breadth 0.989 vs 0.86); relationships: KXNHLSPREAD-26OCT05PHITB-TB2|no: DUPLICATIVE (phi 0.725); failure: TBL wins by 2+
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT05PHITB-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT05PHITB-TB3|no has the higher standalone adjusted growth (5.48 vs 4.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.725); they share one thesis budget; relationships: KXNHLSPREAD-26OCT05PHITB-TB3|no: DUPLICATIVE (phi 0.725); failure: TBL wins by 2+

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis GAME:TIGHT (p 0.4514): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT05PHITB-TB3|no (same contract)
- thesis TBL:SUPPRESSED (p 0.3877): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT05PHITB-TB3|no (same contract)
- KXNHLSPREAD-26OCT05PHITB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3382, phi -0.725)
- KXNHLSPREAD-26OCT05PHITB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3382, phi -1.0)

portfolios: A EV +4.90 (adj +1.43) on $50.00, P(profit) 0.7142, adj growth 9.1 bp · B EV +2.06 (adj +0.71) on $22.47, P(profit) 0.7884, adj growth 6.3 bp · C EV +1.77 (adj +0.62) on $20.00, P(profit) 0.7884, adj growth 5.5 bp · R EV +0.55 (adj +0.19) on $6.00, P(profit) 0.7884, adj growth 6.6 bp

## OTT @ BOS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_OTT_win | p_overtime | goals | shots BOS/OTT | BOS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.54 | 0.46 | 0.00 | 6.01 | 27.3/27.9 | 24.5/23.5 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.45 | 0.55 | 0.47 | 5.89 | 21.9/33.2 | 29.9/18.7 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.104 | 0.50 | 0.50 | 0.00 | 6.01 | 21.7/33.0 | 29.1/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.50 | 0.50 | 0.48 | 5.89 | 27.3/27.7 | 24.3/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.53 | 0.47 | 0.00 | 9.18 | 28.9/29.4 | 23.3/22.6 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.061 | 0.44 | 0.56 | 0.00 | 9.23 | 23.2/35.1 | 28.2/17.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_WPG_win | p_overtime | goals | shots PIT/WPG | PIT/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.68 | 0.32 | 0.00 | 6.01 | 27.1/26.8 | 24.1/22.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.102 | 0.73 | 0.27 | 0.00 | 6.06 | 32.1/21.2 | 18.8/27.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.51 | 0.49 | 0.46 | 5.97 | 27.5/27.2 | 24.0/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.68 | 0.32 | 0.00 | 9.43 | 29.0/28.5 | 23.3/21.7 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.57 | 0.43 | 0.46 | 5.95 | 32.5/21.6 | 18.4/29.0 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.077 | 0.75 | 0.25 | 0.00 | 9.31 | 34.2/22.6 | 18.4/26.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, PIT shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_SJS_win | p_overtime | goals | shots DAL/SJS | DAL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.58 | 0.42 | 0.00 | 6.02 | 26.5/26.2 | 23.1/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.48 | 5.94 | 26.7/26.3 | 23.1/23.4 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.100 | 0.64 | 0.36 | 0.00 | 6.01 | 31.4/20.8 | 17.9/27.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.55 | 0.45 | 0.49 | 5.9 | 31.6/21.0 | 17.9/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.55 | 0.45 | 0.00 | 9.21 | 28.1/27.6 | 22.1/21.8 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.066 | 0.65 | 0.35 | 0.00 | 9.28 | 33.0/22.2 | 17.5/25.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
