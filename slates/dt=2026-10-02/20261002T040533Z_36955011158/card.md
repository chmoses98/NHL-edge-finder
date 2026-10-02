# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T04:05:33Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +5.54 | +1.75 | -0.57 | 0.451 | -50.00 | -50.00 | 10.44 |
| B thesis-diversified (joint) ← card | 13.30 | +1.72 | +0.57 | -1.18 | 0.451 | -13.30 | -13.30 | 4.98 |
| C best expression per thesis | 8.63 | +1.45 | +0.49 | -8.63 | 0.451 | -8.63 | -8.63 | 4.27 |

## NYR @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_NYR_win | p_overtime | goals | shots DET/NYR | DET/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.51 | 0.49 | 0.00 | 6.0 | 27.2/27.0 | 23.6/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.48 | 0.52 | 0.48 | 5.88 | 27.4/26.8 | 23.6/24.2 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.099 | 0.52 | 0.48 | 0.00 | 5.96 | 32.3/21.0 | 17.9/28.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.53 | 0.47 | 0.49 | 5.88 | 33.0/21.7 | 18.4/29.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.49 | 0.51 | 0.00 | 9.23 | 28.7/28.3 | 22.2/22.8 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.059 | 0.56 | 0.45 | 0.00 | 9.12 | 33.8/22.5 | 17.4/27.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ CAR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WSH_win | p_overtime | goals | shots CAR/WSH | CAR/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.147 | 0.64 | 0.36 | 0.00 | 6.01 | 33.3/20.9 | 18.0/29.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.124 | 0.55 | 0.45 | 0.44 | 5.89 | 33.3/21.1 | 17.9/29.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.56 | 0.44 | 0.00 | 6.06 | 27.3/26.4 | 23.1/23.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.095 | 0.65 | 0.35 | 0.00 | 9.25 | 34.6/22.1 | 17.3/27.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.52 | 0.48 | 0.49 | 6.01 | 27.2/26.5 | 23.2/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.068 | 0.57 | 0.43 | 0.00 | 9.24 | 29.1/28.3 | 22.6/22.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_BOS_win | p_overtime | goals | shots WPG/BOS | WPG/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.52 | 0.48 | 0.00 | 5.95 | 27.3/27.1 | 23.8/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.49 | 0.51 | 0.47 | 5.88 | 27.5/27.3 | 24.0/24.2 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.088 | 0.57 | 0.43 | 0.00 | 5.99 | 32.2/21.7 | 18.6/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.52 | 0.48 | 0.00 | 9.18 | 28.7/28.6 | 22.8/22.5 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.56 | 0.44 | 0.49 | 5.83 | 32.6/21.9 | 18.7/29.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.46 | 0.54 | 0.00 | 3.5 | 26.0/25.7 | 23.6/24.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_STL_win | p_overtime | goals | shots DAL/STL | DAL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.59 | 0.41 | 0.00 | 6.01 | 25.8/25.7 | 22.5/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.47 | 5.92 | 26.0/25.7 | 22.5/22.6 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.092 | 0.62 | 0.38 | 0.00 | 6.02 | 30.8/20.5 | 17.6/26.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.56 | 0.44 | 0.46 | 5.89 | 31.3/20.7 | 17.6/27.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.56 | 0.44 | 0.00 | 9.26 | 27.5/27.3 | 21.7/21.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.54 | 0.46 | 0.00 | 3.41 | 24.7/24.3 | 22.6/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Dallas wins NO | 37 | 0.451 | 0.408 | +0.065 | +0.022 | $5.82 | STL:WINS | 0.2346 | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 60 | 0.678 | 0.636 | +0.061 | +0.020 | $7.48 | STL:WINS | 0.2917 | EVIDENCE_MIXED | D |
- **Dallas wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT02STLDAL-DAL2|no; why: higher confidence-adjusted growth (4.41 vs 3.62 bp); wins across more scripts (relative breadth 1.035 vs 0.904); relationships: KXNHLSPREAD-26OCT02STLDAL-DAL2|no: DUPLICATIVE (phi 0.625); failure: DAL wins (incl. OT/SO)
- **Dallas wins by over 1.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: second expression of the same thesis: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (4.41 vs 3.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.625); they share one thesis budget; relationships: KXNHLGAME-26OCT02STLDAL-DAL|no: DUPLICATIVE (phi 0.625); failure: DAL wins by 2+

portfolios: A EV +5.54 (adj +1.75) on $50.00, P(profit) 0.4514, adj growth 10.4 bp · B EV +1.72 (adj +0.57) on $13.30, P(profit) 0.4514, adj growth 5.0 bp · C EV +1.45 (adj +0.49) on $8.63, P(profit) 0.4514, adj growth 4.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02STLDAL-STL|yes == KXNHLGAME-26OCT02STLDAL-DAL|no

## ANA @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_ANA_win | p_overtime | goals | shots VGK/ANA | VGK/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.67 | 0.33 | 0.00 | 6.04 | 28.0/28.2 | 25.4/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.54 | 0.46 | 0.46 | 5.94 | 27.8/27.8 | 24.6/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.64 | 0.36 | 0.00 | 9.3 | 29.5/29.7 | 24.5/22.9 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.078 | 0.59 | 0.41 | 0.00 | 6.02 | 22.7/33.4 | 30.2/19.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.50 | 0.50 | 0.50 | 5.92 | 22.7/33.6 | 30.4/19.5 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.059 | 0.70 | 0.30 | 0.00 | 6.05 | 32.4/22.3 | 19.8/27.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
