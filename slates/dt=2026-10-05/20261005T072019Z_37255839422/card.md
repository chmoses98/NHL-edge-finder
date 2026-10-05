# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-05T07:20:19Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +4.44 | +1.28 | +30.61 | 0.714 | -50.00 | -50.00 | 7.68 |
| B thesis-diversified (joint) ← optimiser card | 17.53 | +1.41 | +0.44 | +8.39 | 0.714 | -17.53 | -17.53 | 3.84 |
| C best expression per thesis | 17.40 | +1.25 | +0.40 | +6.30 | 0.787 | -17.40 | -17.40 | 3.50 |
| R FUNDED research stakes | 6.00 | +0.50 | +0.15 | +3.21 | 0.665 | -6.00 | -6.00 | 0.00 |

## PHI @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_PHI_win | p_overtime | goals | shots TBL/PHI | TBL/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.125 | 0.65 | 0.35 | 0.00 | 5.94 | 31.5/20.4 | 17.8/27.0 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.55 | 0.45 | 0.46 | 5.84 | 31.8/20.7 | 17.6/28.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.60 | 0.40 | 0.00 | 5.96 | 26.2/25.9 | 22.7/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.51 | 0.49 | 0.47 | 5.88 | 26.4/25.8 | 22.6/23.0 | even strength |
| TBL shot control · low event (<=4) · decided (2+) | 0.068 | 0.63 | 0.37 | 0.00 | 3.39 | 30.6/19.4 | 18.0/28.3 | even strength |
| TBL shot control · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.57 | 0.43 | 0.47 | 2.77 | 30.1/19.0 | 17.7/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 2.5 goals NO | 72 | 0.787 | 0.751 | +0.053 | +0.017 | $11.20 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 59 | 0.665 | 0.625 | +0.058 | +0.018 | $5.03 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 3.5 goals scored NO | 53 | 0.602 | 0.561 | +0.054 | +0.013 | $1.30 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT05PHITB-TB2|no; why: higher confidence-adjusted growth (3.17 vs 2.95 bp); despite a smaller raw edge (+0.053 vs +0.058/contract); wins across more scripts (relative breadth 0.985 vs 0.858); relationships: KXNHLSPREAD-26OCT05PHITB-TB2|no: DUPLICATIVE (phi 0.733); KXNHLTEAMTOTAL-26OCT05PHITB-TB4|no: REINFORCING (phi 0.524); failure: TBL wins by 2+
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT05PHITB-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT05PHITB-TB3|no has the higher standalone adjusted growth (3.17 vs 2.95 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.733); they share one thesis budget; relationships: KXNHLSPREAD-26OCT05PHITB-TB3|no: DUPLICATIVE (phi 0.733); KXNHLTEAMTOTAL-26OCT05PHITB-TB4|no: REINFORCING (phi 0.559); failure: TBL wins by 2+
- **Tampa Bay over 3.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT05PHITB-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT05PHITB-TB3|no has the higher standalone adjusted growth (3.17 vs 1.60 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.524); they share one thesis budget; relationships: KXNHLSPREAD-26OCT05PHITB-TB3|no: REINFORCING (phi 0.524); KXNHLSPREAD-26OCT05PHITB-TB2|no: REINFORCING (phi 0.559); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis GAME:TIGHT (p 0.4558): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT05PHITB-TB2|no (same contract)
- thesis TBL:SUPPRESSED (p 0.3879): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT05PHITB-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT05PHITB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3353, phi -0.733)
- KXNHLSPREAD-26OCT05PHITB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3353, phi -1.0)
- KXNHLTEAMTOTAL-26OCT05PHITB-TB4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3891, phi -0.981)

portfolios: A EV +4.44 (adj +1.28) on $50.00, P(profit) 0.7141, adj growth 7.7 bp · B EV +1.41 (adj +0.44) on $17.53, P(profit) 0.7141, adj growth 3.8 bp · C EV +1.25 (adj +0.40) on $17.40, P(profit) 0.7868, adj growth 3.5 bp · R EV +0.50 (adj +0.15) on $6.00, P(profit) 0.6647, adj growth 5.0 bp

## OTT @ BOS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_OTT_win | p_overtime | goals | shots BOS/OTT | BOS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.52 | 0.48 | 0.00 | 6.03 | 27.2/27.7 | 24.3/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.49 | 5.95 | 27.3/27.8 | 24.5/24.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.105 | 0.46 | 0.54 | 0.00 | 6.01 | 21.6/33.1 | 29.2/18.3 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.46 | 0.54 | 0.46 | 5.89 | 21.8/33.2 | 29.8/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.49 | 0.51 | 0.00 | 9.38 | 28.9/29.5 | 23.2/22.9 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.066 | 0.47 | 0.53 | 0.00 | 9.27 | 23.1/35.2 | 28.5/17.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_WPG_win | p_overtime | goals | shots PIT/WPG | PIT/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.63 | 0.37 | 0.00 | 6.04 | 27.2/26.7 | 23.7/23.1 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.105 | 0.67 | 0.33 | 0.00 | 6.04 | 32.4/21.6 | 19.0/27.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.62 | 0.38 | 0.00 | 9.4 | 28.6/28.2 | 23.0/21.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.47 | 5.96 | 27.2/27.1 | 23.8/23.8 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.55 | 0.45 | 0.49 | 5.94 | 32.5/21.6 | 18.3/29.3 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.080 | 0.71 | 0.29 | 0.00 | 9.34 | 34.4/22.9 | 18.4/26.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_SJS_win | p_overtime | goals | shots DAL/SJS | DAL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.59 | 0.41 | 0.00 | 6.05 | 26.6/26.2 | 23.0/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.48 | 5.95 | 26.5/26.4 | 23.1/23.2 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.096 | 0.63 | 0.37 | 0.00 | 5.98 | 31.5/20.6 | 17.8/27.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.51 | 0.49 | 0.44 | 5.88 | 31.5/20.9 | 17.8/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.58 | 0.42 | 0.00 | 9.3 | 27.9/27.3 | 21.7/21.5 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.066 | 0.66 | 0.34 | 0.00 | 9.24 | 33.2/22.3 | 17.8/25.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
