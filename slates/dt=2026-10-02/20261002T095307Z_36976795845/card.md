# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T09:53:07Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +5.54 | +1.80 | -0.57 | 0.451 | -50.00 | -50.00 | 11.00 |
| B thesis-diversified (joint) ← card | 15.08 | +1.76 | +0.58 | -1.14 | 0.451 | -15.08 | -15.08 | 5.06 |
| C best expression per thesis | 8.63 | +1.45 | +0.49 | -8.63 | 0.451 | -8.63 | -8.63 | 4.27 |

## NYR @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_NYR_win | p_overtime | goals | shots DET/NYR | DET/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.49 | 0.51 | 0.00 | 5.99 | 27.2/26.8 | 23.1/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.47 | 0.53 | 0.50 | 5.9 | 27.2/26.9 | 23.6/24.0 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.54 | 0.46 | 0.49 | 5.86 | 32.5/21.4 | 18.2/29.0 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.100 | 0.57 | 0.43 | 0.00 | 5.96 | 32.4/21.2 | 18.1/28.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.49 | 0.51 | 0.00 | 9.24 | 28.5/28.2 | 22.3/22.8 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.060 | 0.51 | 0.49 | 0.48 | 2.82 | 25.4/25.2 | 23.7/23.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ CAR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WSH_win | p_overtime | goals | shots CAR/WSH | CAR/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.146 | 0.64 | 0.36 | 0.00 | 6.01 | 33.4/20.8 | 18.0/28.8 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.124 | 0.55 | 0.45 | 0.45 | 5.91 | 33.3/21.1 | 18.0/29.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.56 | 0.44 | 0.00 | 6.06 | 27.3/26.5 | 23.0/23.5 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.097 | 0.65 | 0.35 | 0.00 | 9.27 | 34.5/22.2 | 17.5/27.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.51 | 0.49 | 0.48 | 5.99 | 27.4/26.7 | 23.2/24.1 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.068 | 0.56 | 0.44 | 0.47 | 2.85 | 31.8/19.7 | 18.2/30.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_BOS_win | p_overtime | goals | shots WPG/BOS | WPG/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.51 | 0.49 | 0.00 | 5.98 | 27.4/27.3 | 24.0/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.46 | 5.9 | 27.3/27.1 | 23.9/23.9 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.094 | 0.59 | 0.41 | 0.00 | 5.98 | 32.6/21.8 | 18.7/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.52 | 0.48 | 0.00 | 9.16 | 28.9/28.5 | 22.6/22.7 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.54 | 0.46 | 0.48 | 5.8 | 32.9/21.8 | 18.8/29.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.48 | 0.52 | 0.00 | 3.47 | 26.1/26.0 | 24.1/24.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_STL_win | p_overtime | goals | shots DAL/STL | DAL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 6.01 | 25.9/25.7 | 22.5/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.52 | 0.48 | 0.46 | 5.9 | 26.0/25.8 | 22.7/22.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.092 | 0.63 | 0.37 | 0.00 | 6.01 | 30.8/20.5 | 17.6/26.6 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.55 | 0.45 | 0.47 | 5.92 | 31.0/20.7 | 17.5/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.56 | 0.44 | 0.00 | 9.3 | 27.5/27.4 | 21.7/20.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.53 | 0.47 | 0.00 | 3.41 | 24.6/24.4 | 22.6/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Dallas wins NO | 37 | 0.451 | 0.408 | +0.065 | +0.022 | $5.82 | STL:WINS | 0.2379 | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 60 | 0.678 | 0.636 | +0.061 | +0.020 | $5.38 | STL:WINS | 0.2946 | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 73 | 0.792 | 0.758 | +0.048 | +0.015 | $3.88 | STL:WINS | 0.2524 | EVIDENCE_MIXED | D |
- **Dallas wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT02STLDAL-DAL2|no; why: higher confidence-adjusted growth (4.41 vs 3.62 bp); wins across more scripts (relative breadth 1.03 vs 0.898); relationships: KXNHLSPREAD-26OCT02STLDAL-DAL2|no: DUPLICATIVE (phi 0.625); KXNHLSPREAD-26OCT02STLDAL-DAL3|no: DUPLICATIVE (phi 0.465); failure: DAL wins (incl. OT/SO)
- **Dallas wins by over 1.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: second expression of the same thesis: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (4.41 vs 3.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.625); they share one thesis budget; relationships: KXNHLGAME-26OCT02STLDAL-DAL|no: DUPLICATIVE (phi 0.625); KXNHLSPREAD-26OCT02STLDAL-DAL3|no: DUPLICATIVE (phi 0.745); failure: DAL wins by 2+
- **Dallas wins by over 2.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: second expression of the same thesis: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (4.41 vs 2.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.465); they share one thesis budget; relationships: KXNHLGAME-26OCT02STLDAL-DAL|no: DUPLICATIVE (phi 0.465); KXNHLSPREAD-26OCT02STLDAL-DAL2|no: DUPLICATIVE (phi 0.745); failure: DAL wins by 2+

portfolios: A EV +5.54 (adj +1.80) on $50.00, P(profit) 0.4514, adj growth 11.0 bp · B EV +1.76 (adj +0.58) on $15.08, P(profit) 0.4514, adj growth 5.1 bp · C EV +1.45 (adj +0.49) on $8.63, P(profit) 0.4514, adj growth 4.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02STLDAL-STL|yes == KXNHLGAME-26OCT02STLDAL-DAL|no

## ANA @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_ANA_win | p_overtime | goals | shots VGK/ANA | VGK/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.65 | 0.35 | 0.00 | 6.05 | 28.0/28.2 | 25.4/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.55 | 0.45 | 0.46 | 5.95 | 27.8/27.9 | 24.6/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.66 | 0.34 | 0.00 | 9.3 | 29.6/29.7 | 24.5/22.5 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.077 | 0.60 | 0.40 | 0.00 | 6.01 | 22.6/33.4 | 30.3/18.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.49 | 0.51 | 0.49 | 5.91 | 22.6/33.6 | 30.3/19.3 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.060 | 0.71 | 0.29 | 0.00 | 6.04 | 32.5/22.5 | 20.0/27.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
