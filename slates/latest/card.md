# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-13T14:43:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +15.88 | +4.98 | +17.35 | 0.643 | -51.54 | -71.07 | 36.90 |
| B thesis-diversified (joint) ← optimiser card | 98.77 | +9.35 | +3.20 | +11.90 | 0.653 | -27.90 | -42.05 | 28.13 |
| C best expression per thesis | 45.30 | +6.12 | +2.10 | +2.03 | 0.649 | -21.64 | -24.27 | 18.31 |
| R FUNDED research stakes | 31.00 | +3.26 | +1.12 | +3.62 | 0.640 | -9.47 | -13.22 | 0.00 |

## NJD @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_NJD_win | p_overtime | goals | shots DET/NJD | DET/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.59 | 0.41 | 0.00 | 5.97 | 28.2/28.4 | 25.2/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.52 | 0.48 | 0.47 | 5.83 | 28.4/28.4 | 25.1/25.1 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.076 | 0.52 | 0.48 | 0.00 | 5.91 | 22.3/33.2 | 29.5/18.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.071 | 0.56 | 0.44 | 0.00 | 3.4 | 27.1/27.1 | 25.5/25.0 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.48 | 0.52 | 0.49 | 5.79 | 22.7/33.2 | 30.0/19.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.066 | 0.57 | 0.43 | 0.00 | 9.13 | 29.7/29.7 | 24.3/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey over 3.5 goals scored NO | 61 | 0.690 | 0.648 | +0.064 | +0.021 | $5.72 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey over 4.5 goals scored NO | 79 | 0.850 | 0.818 | +0.049 | +0.016 | $13.17 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey over 2.5 goals scored NO | 40 | 0.477 | 0.436 | +0.060 | +0.019 | $2.34 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Full Game: Over 3.5 goals scored NO | 14 | 0.184 | 0.160 | +0.036 | +0.011 | $1.41 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | DIRECT (0.62) | EVIDENCE_MIXED | D |
- **New Jersey over 3.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no; why: higher confidence-adjusted growth (4.11 vs 3.52 bp); relationships: KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no: DUPLICATIVE (phi 0.627); KXNHLTEAMTOTAL-26OCT13NJDET-NJ3|no: DUPLICATIVE (phi 0.639); KXNHLTOTAL-26OCT13NJDET-4|no: DUPLICATIVE (phi 0.318); failure: NJD offense succeeds (4+ goals)
- **New Jersey over 4.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no has the higher standalone adjusted growth (4.11 vs 3.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.627); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no: DUPLICATIVE (phi 0.627); KXNHLTEAMTOTAL-26OCT13NJDET-NJ3|no: DUPLICATIVE (phi 0.401); KXNHLTOTAL-26OCT13NJDET-4|no: REINFORCING (phi 0.2); failure: NJD offense succeeds (4+ goals)
- **New Jersey over 2.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no has the higher standalone adjusted growth (4.11 vs 3.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.639); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no: DUPLICATIVE (phi 0.639); KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no: DUPLICATIVE (phi 0.401); KXNHLTOTAL-26OCT13NJDET-4|no: REINFORCING (phi 0.413); failure: NJD offense succeeds (4+ goals)
- **Full Game: Over 3.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no has the higher standalone adjusted growth (4.11 vs 2.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.318); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no: DUPLICATIVE (phi 0.318); KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no: REINFORCING (phi 0.2); KXNHLTEAMTOTAL-26OCT13NJDET-NJ3|no: REINFORCING (phi 0.413); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NJD:SUPPRESSED (p 0.4903): highest fidelity KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no (same contract)
- thesis GAME:LOW_EVENT (p 0.2974): highest fidelity KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no — override declined: the joint re-optimisation gives KXNHLTOTAL-26OCT13NJDET-6|no less than the minimum stake; KXNHLTOTAL-26OCT13NJDET-4|no kept
- KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.2984, phi -0.973)
- KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.2984, phi -0.644)
- KXNHLTEAMTOTAL-26OCT13NJDET-NJ3|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.2984, phi -0.622)
- KXNHLTOTAL-26OCT13NJDET-4|no: FUNDED_RESEARCH; family MIXED; loses 38% of the draws where the thesis happens; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.363, phi -0.359)
- override: override declined: the joint re-optimisation gives KXNHLTOTAL-26OCT13NJDET-6|no less than the minimum stake; KXNHLTOTAL-26OCT13NJDET-4|no kept

portfolios: A EV +4.04 (adj +1.25) on $39.47, P(profit) 0.5962, adj growth 8.8 bp · B EV +2.05 (adj +0.67) on $22.64, P(profit) 0.6902, adj growth 5.9 bp · C EV +1.50 (adj +0.50) on $14.83, P(profit) 0.6902, adj growth 4.4 bp · R EV +0.83 (adj +0.27) on $8.00, P(profit) 0.6902, adj growth 8.5 bp

## FLA @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_FLA_win | p_overtime | goals | shots CBJ/FLA | CBJ/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.66 | 0.34 | 0.00 | 6.02 | 27.2/27.0 | 24.1/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.47 | 5.89 | 27.6/27.3 | 24.1/24.5 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.093 | 0.72 | 0.28 | 0.00 | 5.97 | 32.4/21.3 | 18.8/27.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.67 | 0.33 | 0.00 | 9.33 | 29.1/28.8 | 23.7/21.9 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.56 | 0.44 | 0.46 | 5.88 | 32.6/21.8 | 18.7/29.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.66 | 0.34 | 0.00 | 3.41 | 25.9/25.6 | 24.1/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Columbus wins by over 1.5 goals YES | 31 | 0.384 | 0.344 | +0.059 | +0.019 | $5.16 | FUNDED_RESEARCH | $2 | CBJ:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 84 | 0.892 | 0.864 | +0.043 | +0.014 | $20.00 | FUNDED_RESEARCH | $5 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 75 | 0.811 | 0.778 | +0.048 | +0.015 | $1.53 | FUNDED_RESEARCH | $1 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Columbus wins by over 1.5 goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no; why: higher confidence-adjusted growth (3.77 vs 3.48 bp); relationships: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: REINFORCING (phi 0.274); KXNHLSPREAD-26OCT13FLACBJ-FLA2|no: DUPLICATIVE (phi 0.38); failure: tight game (one-goal final or OT)
- **Florida wins by over 2.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes has the higher standalone adjusted growth (3.77 vs 3.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.274); they share one thesis budget; relationships: KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes: REINFORCING (phi 0.274); KXNHLSPREAD-26OCT13FLACBJ-FLA2|no: DUPLICATIVE (phi 0.721); failure: FLA wins by 2+
- **Florida wins by over 1.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes has the higher standalone adjusted growth (3.77 vs 2.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.380); they share one thesis budget; relationships: KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes: DUPLICATIVE (phi 0.38); KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: DUPLICATIVE (phi 0.721); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:WINS_BY_2PLUS (p 0.3839): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes (same contract)
- thesis CBJ:WINS (p 0.6147): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:TIGHT (p 0.4276, phi -0.682)
- KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.1885, phi -0.721)
- KXNHLSPREAD-26OCT13FLACBJ-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.1885, phi -1.0)

portfolios: A EV +3.88 (adj +1.27) on $39.47, P(profit) 0.3839, adj growth 9.4 bp · B EV +2.04 (adj +0.67) on $26.69, P(profit) 0.3839, adj growth 5.9 bp · C EV +1.24 (adj +0.41) on $6.83, P(profit) 0.3839, adj growth 3.6 bp · R EV +0.68 (adj +0.22) on $8.00, P(profit) 0.3839, adj growth 7.5 bp

## BUF @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_BUF_win | p_overtime | goals | shots MTL/BUF | MTL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.62 | 0.38 | 0.00 | 6.03 | 26.9/27.4 | 24.3/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.49 | 5.93 | 26.9/27.5 | 24.3/23.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.100 | 0.54 | 0.46 | 0.00 | 6.01 | 21.8/33.0 | 29.3/18.3 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.54 | 0.46 | 0.46 | 5.88 | 21.3/32.5 | 29.3/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.59 | 0.41 | 0.00 | 9.29 | 28.4/29.0 | 23.4/21.9 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.068 | 0.57 | 0.43 | 0.00 | 9.18 | 23.4/34.7 | 28.6/17.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ CAR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WSH_win | p_overtime | goals | shots CAR/WSH | CAR/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.155 | 0.67 | 0.33 | 0.00 | 5.99 | 33.6/21.0 | 18.4/28.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.128 | 0.55 | 0.45 | 0.46 | 5.9 | 33.8/21.2 | 18.0/30.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.114 | 0.69 | 0.30 | 0.00 | 9.29 | 35.1/22.3 | 17.7/27.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.092 | 0.59 | 0.41 | 0.00 | 6.03 | 27.7/26.7 | 23.5/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.51 | 0.49 | 0.47 | 5.88 | 27.5/26.7 | 23.5/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.57 | 0.43 | 0.00 | 9.26 | 29.4/28.1 | 22.6/22.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_SEA_win | p_overtime | goals | shots PHI/SEA | PHI/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.55 | 0.45 | 0.00 | 5.96 | 26.7/26.6 | 23.3/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.51 | 0.49 | 0.47 | 5.88 | 26.9/26.8 | 23.6/23.7 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.082 | 0.59 | 0.41 | 0.00 | 5.93 | 31.6/21.1 | 18.3/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.068 | 0.57 | 0.43 | 0.00 | 9.21 | 28.3/28.4 | 22.8/22.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.51 | 0.49 | 0.00 | 3.44 | 25.5/25.4 | 23.7/23.5 | even strength |
| PHI shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.53 | 0.47 | 0.46 | 5.87 | 31.6/21.2 | 18.1/28.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, PHI shot control · normal event (5-7) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TBL @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_TBL_win | p_overtime | goals | shots NYR/TBL | NYR/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.54 | 0.46 | 0.00 | 5.97 | 25.8/26.3 | 23.0/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.49 | 5.92 | 25.9/26.5 | 23.1/22.6 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.104 | 0.46 | 0.54 | 0.00 | 5.98 | 20.3/31.1 | 27.1/17.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.47 | 0.53 | 0.47 | 5.88 | 20.6/31.7 | 28.2/17.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.58 | 0.42 | 0.00 | 9.29 | 27.3/27.9 | 22.2/20.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.53 | 0.47 | 0.49 | 2.79 | 24.6/25.1 | 23.7/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York R wins by over 1.5 goals YES | 21 | 0.287 | 0.246 | +0.065 | +0.024 | $4.44 | FUNDED_RESEARCH | $2 | NYR:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 76 | 0.839 | 0.797 | +0.066 | +0.024 | $19.37 | FUNDED_RESEARCH | $5 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 3.5 goals scored NO | 55 | 0.644 | 0.594 | +0.076 | +0.027 | $4.96 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 4.5 goals scored NO | 75 | 0.821 | 0.783 | +0.057 | +0.020 | $3.97 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New York R wins by over 1.5 goals YES** — thesis: NYR wins by 2+; alternative: KXNHLSPREAD-26OCT13TBNYR-TB3|no; why: higher confidence-adjusted growth (7.41 vs 7.29 bp); despite a smaller raw edge (+0.065 vs +0.066/contract); relationships: KXNHLSPREAD-26OCT13TBNYR-TB3|no: REINFORCING (phi 0.278); KXNHLTEAMTOTAL-26OCT13TBNYR-TB4|no: REINFORCING (phi 0.383); KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no: REINFORCING (phi 0.273); failure: TBL wins (incl. OT/SO)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes has the higher standalone adjusted growth (7.41 vs 7.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.278); they share one thesis budget; relationships: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: REINFORCING (phi 0.278); KXNHLTEAMTOTAL-26OCT13TBNYR-TB4|no: DUPLICATIVE (phi 0.493); KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no: REINFORCING (phi 0.513); failure: TBL wins by 2+
- **Tampa Bay over 3.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes has the higher standalone adjusted growth (7.41 vs 6.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.383); they share one thesis budget; relationships: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: REINFORCING (phi 0.383); KXNHLSPREAD-26OCT13TBNYR-TB3|no: DUPLICATIVE (phi 0.493); KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no: DUPLICATIVE (phi 0.629); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay over 4.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no selected over broad KXNHLTEAMTOTAL-26OCT13TBNYR-TB3|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: REINFORCING (phi 0.273); KXNHLSPREAD-26OCT13TBNYR-TB3|no: REINFORCING (phi 0.513); KXNHLTEAMTOTAL-26OCT13TBNYR-TB4|no: DUPLICATIVE (phi 0.629); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis NYR:WINS_BY_2PLUS (p 0.2868): highest fidelity KXNHLSPREAD-26OCT13TBNYR-NYR2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT13TBNYR-TB4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:WINS (p 0.5182): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT13TBNYR-TB4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.4385): highest fidelity KXNHLTEAMTOTAL-26OCT13TBNYR-TB4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT13TBNYR-TB4|no (same contract)
- KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS (p 0.4818, phi -0.611)
- KXNHLSPREAD-26OCT13TBNYR-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2605, phi -0.739)
- KXNHLTEAMTOTAL-26OCT13TBNYR-TB4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3459, phi -0.977)
- KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3459, phi -0.643)
- override: Broad expression KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no selected over broad KXNHLTEAMTOTAL-26OCT13TBNYR-TB3|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.41 (adj +1.71) on $39.47, P(profit) 0.5974, adj growth 13.4 bp · B EV +3.93 (adj +1.43) on $32.75, P(profit) 0.646, adj growth 12.6 bp · C EV +2.04 (adj +0.76) on $6.95, P(profit) 0.2868, adj growth 6.6 bp · R EV +1.36 (adj +0.50) on $10.00, P(profit) 0.646, adj growth 16.3 bp

## STL @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_STL_win | p_overtime | goals | shots OTT/STL | OTT/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.49 | 0.51 | 0.00 | 5.96 | 26.7/26.2 | 22.8/23.2 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.109 | 0.62 | 0.38 | 0.00 | 6.03 | 31.5/20.5 | 17.6/27.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.50 | 0.50 | 0.45 | 5.91 | 26.6/26.3 | 23.1/23.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.52 | 0.48 | 0.47 | 5.89 | 32.1/21.0 | 17.7/28.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.48 | 0.52 | 0.00 | 9.24 | 28.1/27.8 | 21.6/22.1 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.070 | 0.57 | 0.43 | 0.00 | 9.16 | 33.4/22.1 | 17.0/26.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_VAN_win | p_overtime | goals | shots NYI/VAN | NYI/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NYI shot control · normal event (5-7) · decided (2+) | 0.122 | 0.68 | 0.32 | 0.00 | 6.04 | 32.9/21.1 | 18.5/28.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.60 | 0.40 | 0.00 | 6.05 | 27.6/27.0 | 23.8/23.7 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.56 | 0.44 | 0.46 | 5.91 | 33.3/21.7 | 18.5/29.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.50 | 0.50 | 0.47 | 5.94 | 27.7/27.2 | 23.9/24.4 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.082 | 0.70 | 0.30 | 0.00 | 9.3 | 34.4/22.7 | 18.2/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.61 | 0.39 | 0.00 | 9.2 | 29.1/28.4 | 22.9/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York I wins by over 2.5 goals NO | 69 | 0.761 | 0.723 | +0.056 | +0.018 | $16.69 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New York I wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT13VANNYI-NYI2|no; why: higher confidence-adjusted growth (3.45 vs 1.51 bp); wins across more scripts (relative breadth 0.998 vs 0.866); relationships: only recommended bet in this game; failure: NYI wins by 2+

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:TIGHT (p 0.4273): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13VANNYI-NYI3|no (same contract)
- KXNHLSPREAD-26OCT13VANNYI-NYI3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:WINS_BY_2PLUS (p 0.3648, phi -0.739)

portfolios: A EV +2.55 (adj +0.75) on $31.58, P(profit) 0.6352, adj growth 5.3 bp · B EV +1.33 (adj +0.43) on $16.69, P(profit) 0.7611, adj growth 3.8 bp · C EV +1.33 (adj +0.43) on $16.69, P(profit) 0.7611, adj growth 3.8 bp · R EV +0.40 (adj +0.13) on $5.00, P(profit) 0.7611, adj growth 4.4 bp

## PIT @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_PIT_win | p_overtime | goals | shots CHI/PIT | CHI/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.44 | 0.56 | 0.00 | 6.04 | 26.7/27.4 | 23.5/23.5 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.115 | 0.38 | 0.62 | 0.00 | 6.0 | 21.3/32.8 | 28.5/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.50 | 0.50 | 0.46 | 5.98 | 26.9/27.4 | 24.1/23.4 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.44 | 0.56 | 0.45 | 5.87 | 21.3/32.6 | 29.1/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.45 | 0.55 | 0.00 | 9.33 | 28.5/28.9 | 22.3/22.5 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.078 | 0.37 | 0.63 | 0.00 | 9.29 | 22.8/34.4 | 26.7/17.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_MIN_win | p_overtime | goals | shots WPG/MIN | WPG/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.54 | 0.46 | 0.00 | 5.99 | 28.2/28.1 | 24.7/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.47 | 5.88 | 28.3/28.4 | 25.1/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.55 | 0.45 | 0.00 | 9.28 | 30.0/30.0 | 24.2/23.6 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.070 | 0.56 | 0.44 | 0.00 | 5.98 | 33.1/22.4 | 19.2/29.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.070 | 0.45 | 0.55 | 0.00 | 5.96 | 22.7/33.4 | 29.5/19.5 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.45 | 0.55 | 0.47 | 5.83 | 22.4/32.9 | 29.4/19.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_COL_win | p_overtime | goals | shots DAL/COL | DAL/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.47 | 0.53 | 0.00 | 6.03 | 27.0/27.5 | 23.9/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.48 | 5.92 | 27.2/27.7 | 24.4/23.8 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.105 | 0.40 | 0.60 | 0.00 | 5.98 | 21.3/32.4 | 28.1/18.5 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.49 | 0.51 | 0.43 | 5.88 | 21.5/32.8 | 29.4/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.47 | 0.53 | 0.00 | 9.24 | 28.4/28.9 | 22.9/22.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.065 | 0.41 | 0.59 | 0.00 | 9.18 | 22.8/34.2 | 27.1/18.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_VGK_win | p_overtime | goals | shots NSH/VGK | NSH/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.53 | 0.47 | 0.00 | 5.97 | 27.6/28.1 | 24.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.48 | 0.52 | 0.46 | 5.94 | 27.4/27.9 | 24.5/24.1 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.097 | 0.48 | 0.52 | 0.00 | 5.93 | 21.9/33.2 | 29.5/18.6 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.48 | 0.52 | 0.50 | 5.91 | 22.2/33.6 | 30.3/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.57 | 0.43 | 0.00 | 9.26 | 29.4/29.8 | 24.3/22.9 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.066 | 0.45 | 0.55 | 0.00 | 9.28 | 23.7/35.3 | 28.8/18.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TOR_win | p_overtime | goals | shots UTA/TOR | UTA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| UTA shot control · normal event (5-7) · decided (2+) | 0.148 | 0.69 | 0.31 | 0.00 | 6.0 | 34.4/22.0 | 19.4/29.6 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.56 | 0.44 | 0.47 | 5.96 | 34.7/22.0 | 18.8/31.1 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.110 | 0.72 | 0.28 | 0.00 | 9.23 | 36.1/23.3 | 18.9/27.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.67 | 0.33 | 0.00 | 6.07 | 28.7/28.0 | 25.1/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.65 | 0.35 | 0.00 | 9.4 | 30.3/29.3 | 24.0/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.52 | 0.48 | 0.49 | 5.96 | 28.6/27.7 | 24.3/25.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts UTA shot control · normal event (5-7) · decided (2+) 0.15, UTA shot control · normal event (5-7) · tight (1-goal/OT) 0.12, UTA shot control · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_CGY_win | p_overtime | goals | shots ANA/CGY | ANA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.130 | 0.70 | 0.30 | 0.00 | 6.02 | 35.2/22.5 | 20.0/30.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.68 | 0.32 | 0.00 | 6.04 | 29.0/28.3 | 25.5/24.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.56 | 0.44 | 0.49 | 5.94 | 35.1/23.0 | 19.9/31.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.52 | 0.48 | 0.48 | 5.96 | 29.0/28.3 | 25.2/25.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.093 | 0.71 | 0.29 | 0.00 | 9.22 | 36.6/24.0 | 19.6/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.68 | 0.32 | 0.00 | 9.34 | 30.8/30.2 | 25.0/23.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_EDM_win | p_overtime | goals | shots LAK/EDM | LAK/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.45 | 0.55 | 0.00 | 5.99 | 27.7/27.7 | 24.0/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.48 | 0.52 | 0.46 | 5.92 | 28.0/28.1 | 24.9/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.47 | 0.53 | 0.00 | 9.31 | 29.5/29.6 | 23.5/23.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.072 | 0.42 | 0.58 | 0.00 | 6.03 | 22.2/32.8 | 28.4/19.1 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.46 | 0.54 | 0.47 | 5.93 | 22.1/33.0 | 29.7/18.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.061 | 0.51 | 0.49 | 0.00 | 5.96 | 32.8/22.3 | 19.0/28.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_BOS_win | p_overtime | goals | shots SJS/BOS | SJS/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.51 | 0.49 | 0.00 | 6.03 | 27.1/27.1 | 23.5/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.46 | 5.91 | 27.3/27.2 | 23.9/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.54 | 0.46 | 0.00 | 9.39 | 29.0/28.8 | 22.6/22.7 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.079 | 0.57 | 0.43 | 0.00 | 5.98 | 32.0/21.6 | 18.5/28.1 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.55 | 0.45 | 0.45 | 5.94 | 32.5/21.9 | 18.8/29.1 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.060 | 0.43 | 0.57 | 0.00 | 6.02 | 21.9/32.0 | 27.9/18.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
