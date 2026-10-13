# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-13T07:55:50Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 120.27 | +16.63 | +4.82 | +20.88 | 0.549 | -65.10 | -70.93 | 29.22 |
| B thesis-diversified (joint) ← optimiser card | 63.35 | +6.09 | +2.06 | +7.47 | 0.694 | -18.41 | -37.47 | 18.14 |
| C best expression per thesis | 44.87 | +4.91 | +1.67 | -0.58 | 0.372 | -21.32 | -24.13 | 14.64 |
| R FUNDED research stakes | 17.00 | +1.79 | +0.61 | +1.32 | 0.650 | -5.15 | -10.53 | 0.00 |

## NJD @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_NJD_win | p_overtime | goals | shots DET/NJD | DET/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.53 | 0.47 | 0.00 | 5.95 | 28.1/28.4 | 25.0/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.49 | 0.51 | 0.46 | 5.89 | 28.2/28.4 | 25.0/24.9 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.48 | 0.52 | 0.44 | 5.84 | 22.4/33.3 | 30.1/19.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.071 | 0.45 | 0.55 | 0.00 | 5.93 | 22.8/33.6 | 29.7/19.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.069 | 0.48 | 0.52 | 0.48 | 2.79 | 26.7/26.7 | 25.2/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.55 | 0.45 | 0.00 | 9.15 | 29.8/30.0 | 24.0/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 3.5 goals scored NO | 14 | 0.183 | 0.159 | +0.035 | +0.011 | $2.80 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | DIRECT (0.62) | EVIDENCE_MIXED | D |
- **Full Game: Over 3.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT13NJDET-6|no; why: higher confidence-adjusted growth (1.99 vs 0.68 bp); despite a smaller raw edge (+0.035 vs +0.040/contract); alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.07.
- thesis GAME:LOW_EVENT (p 0.2954): highest fidelity KXNHLTOTAL-26OCT13NJDET-4|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT13NJDET-4|no (same contract)
- KXNHLTOTAL-26OCT13NJDET-4|no: FUNDED_RESEARCH; family MIXED; loses 38% of the draws where the thesis happens; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3421, phi -0.342)

portfolios: A EV +2.42 (adj +0.75) on $10.27, P(profit) 0.1834, adj growth 4.0 bp · B EV +0.66 (adj +0.20) on $2.80, P(profit) 0.1834, adj growth 1.8 bp · C EV +0.66 (adj +0.20) on $2.80, P(profit) 0.1834, adj growth 1.8 bp · R EV +0.24 (adj +0.07) on $1.00, P(profit) 0.1834, adj growth 2.4 bp

## FLA @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_FLA_win | p_overtime | goals | shots CBJ/FLA | CBJ/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.67 | 0.33 | 0.00 | 5.94 | 27.2/27.2 | 24.5/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.46 | 5.9 | 27.3/27.1 | 23.9/24.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.092 | 0.68 | 0.33 | 0.00 | 5.94 | 32.3/21.6 | 19.0/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.63 | 0.37 | 0.00 | 9.18 | 28.6/28.4 | 23.1/21.7 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.57 | 0.43 | 0.52 | 5.9 | 32.1/21.9 | 18.8/28.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.61 | 0.39 | 0.00 | 3.38 | 26.0/25.9 | 24.4/23.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 2.5 goals NO | 84 | 0.886 | 0.861 | +0.037 | +0.011 | $20.00 | FUNDED_RESEARCH | $5 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13FLACBJ-FLA2|no; why: higher confidence-adjusted growth (2.14 vs 1.03 bp); alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:WINS (p 0.5966): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13FLACBJ-FLA3|no (same contract)
- KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2003, phi -0.716)

portfolios: A EV +0.86 (adj +0.26) on $20.00, P(profit) 0.8861, adj growth 2.3 bp · B EV +0.86 (adj +0.26) on $20.00, P(profit) 0.8861, adj growth 2.3 bp · C EV +0.86 (adj +0.26) on $20.00, P(profit) 0.8861, adj growth 2.3 bp · R EV +0.22 (adj +0.07) on $5.00, P(profit) 0.8861, adj growth 2.3 bp

## BUF @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_BUF_win | p_overtime | goals | shots MTL/BUF | MTL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.58 | 0.42 | 0.00 | 6.01 | 27.0/27.6 | 24.4/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.52 | 0.48 | 0.47 | 5.93 | 27.1/27.5 | 24.2/23.8 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.098 | 0.50 | 0.50 | 0.00 | 6.02 | 21.3/32.1 | 28.6/18.0 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.46 | 0.54 | 0.47 | 5.92 | 21.6/32.8 | 29.5/18.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.55 | 0.45 | 0.00 | 9.31 | 28.2/28.8 | 23.1/21.6 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.064 | 0.52 | 0.48 | 0.00 | 9.13 | 22.9/34.2 | 28.1/17.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, BUF shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ CAR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WSH_win | p_overtime | goals | shots CAR/WSH | CAR/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.159 | 0.68 | 0.32 | 0.00 | 6.02 | 33.5/20.9 | 18.4/28.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.129 | 0.52 | 0.48 | 0.46 | 5.88 | 33.6/21.3 | 18.2/30.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.111 | 0.67 | 0.33 | 0.00 | 9.29 | 35.3/22.2 | 17.6/27.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.090 | 0.60 | 0.40 | 0.00 | 5.98 | 27.3/26.4 | 23.3/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.50 | 0.50 | 0.44 | 5.92 | 27.5/26.7 | 23.4/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.62 | 0.38 | 0.00 | 9.26 | 29.4/28.2 | 22.8/22.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_SEA_win | p_overtime | goals | shots PHI/SEA | PHI/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.53 | 0.47 | 0.00 | 6.0 | 26.7/26.8 | 23.5/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.49 | 5.91 | 26.6/26.6 | 23.4/23.4 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.081 | 0.61 | 0.39 | 0.00 | 5.96 | 31.3/21.0 | 18.2/27.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.56 | 0.44 | 0.00 | 9.22 | 28.1/28.1 | 22.3/21.7 | even strength |
| PHI shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.55 | 0.45 | 0.48 | 5.86 | 31.5/21.4 | 18.4/28.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.068 | 0.55 | 0.45 | 0.00 | 3.44 | 25.6/25.4 | 23.7/23.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, PHI shot control · normal event (5-7) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TBL @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_TBL_win | p_overtime | goals | shots NYR/TBL | NYR/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.54 | 0.46 | 0.00 | 5.96 | 25.8/26.3 | 23.0/22.1 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.105 | 0.45 | 0.55 | 0.00 | 5.97 | 20.4/31.3 | 27.3/17.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.51 | 0.49 | 0.50 | 5.91 | 26.1/26.6 | 23.3/22.7 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.48 | 0.52 | 0.48 | 5.87 | 20.5/31.2 | 27.9/17.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.56 | 0.44 | 0.00 | 9.22 | 27.3/27.9 | 22.3/21.1 | even strength |
| TBL shot control · low event (<=4) · tight (1-goal/OT) | 0.060 | 0.48 | 0.52 | 0.44 | 2.79 | 19.1/29.9 | 28.2/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York R wins by over 1.5 goals YES | 21 | 0.290 | 0.248 | +0.069 | +0.026 | $5.98 | FUNDED_RESEARCH | $2 | NYR:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 76 | 0.834 | 0.794 | +0.061 | +0.021 | $20.00 | FUNDED_RESEARCH | $5 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New York R wins by over 1.5 goals YES** — thesis: NYR wins by 2+; alternative: KXNHLSPREAD-26OCT13TBNYR-TB3|no; why: higher confidence-adjusted growth (8.58 vs 5.82 bp); relationships: KXNHLSPREAD-26OCT13TBNYR-TB3|no: REINFORCING (phi 0.286); failure: TBL wins (incl. OT/SO)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes has the higher standalone adjusted growth (8.58 vs 5.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.286); they share one thesis budget; relationships: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: REINFORCING (phi 0.286); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NYR:WINS_BY_2PLUS (p 0.2905): highest fidelity KXNHLSPREAD-26OCT13TBNYR-NYR2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13TBNYR-NYR2|yes (same contract)
- thesis NYR:WINS (p 0.5197): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13TBNYR-NYR2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.4436): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13TBNYR-NYR2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS (p 0.4803, phi -0.615)
- KXNHLSPREAD-26OCT13TBNYR-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2606, phi -0.753)

portfolios: A EV +9.91 (adj +2.84) on $50.00, P(profit) 0.609, adj growth 16.9 bp · B EV +3.43 (adj +1.26) on $25.98, P(profit) 0.2905, adj growth 11.1 bp · C EV +2.31 (adj +0.88) on $7.45, P(profit) 0.2905, adj growth 7.6 bp · R EV +1.02 (adj +0.38) on $7.00, P(profit) 0.2905, adj growth 12.8 bp

## STL @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_STL_win | p_overtime | goals | shots OTT/STL | OTT/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.58 | 0.42 | 0.00 | 5.99 | 26.9/26.5 | 23.3/23.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.110 | 0.66 | 0.34 | 0.00 | 5.95 | 31.5/20.6 | 18.0/26.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.49 | 5.92 | 26.9/26.3 | 23.1/23.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.55 | 0.45 | 0.47 | 5.89 | 31.8/20.9 | 17.7/28.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.60 | 0.40 | 0.00 | 9.2 | 28.0/27.5 | 22.4/21.4 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.072 | 0.71 | 0.29 | 0.00 | 9.2 | 33.7/22.1 | 17.8/25.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_VAN_win | p_overtime | goals | shots NYI/VAN | NYI/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NYI shot control · normal event (5-7) · decided (2+) | 0.126 | 0.70 | 0.30 | 0.00 | 6.01 | 32.8/21.2 | 18.7/28.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.59 | 0.41 | 0.00 | 6.06 | 27.6/27.2 | 24.0/23.6 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.55 | 0.45 | 0.46 | 5.89 | 33.0/21.6 | 18.4/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.50 | 0.50 | 0.46 | 5.91 | 27.6/27.2 | 23.9/24.3 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.078 | 0.70 | 0.30 | 0.00 | 9.24 | 34.5/22.7 | 18.3/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.60 | 0.40 | 0.00 | 9.27 | 29.2/28.5 | 23.3/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York I wins by over 2.5 goals NO | 69 | 0.757 | 0.721 | +0.052 | +0.016 | $11.99 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I wins by over 1.5 goals NO | 57 | 0.645 | 0.602 | +0.058 | +0.015 | $2.58 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New York I wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT13VANNYI-NYI2|no; why: higher confidence-adjusted growth (2.68 vs 2.09 bp); despite a smaller raw edge (+0.052 vs +0.058/contract); wins across more scripts (relative breadth 1.007 vs 0.891); relationships: KXNHLSPREAD-26OCT13VANNYI-NYI2|no: DUPLICATIVE (phi 0.764); failure: NYI wins by 2+
- **New York I wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT13VANNYI-NYI3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT13VANNYI-NYI3|no has the higher standalone adjusted growth (2.68 vs 2.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.764); they share one thesis budget; relationships: KXNHLSPREAD-26OCT13VANNYI-NYI3|no: DUPLICATIVE (phi 0.764); failure: NYI wins by 2+

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:TIGHT (p 0.4329): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13VANNYI-NYI3|no (same contract)
- KXNHLSPREAD-26OCT13VANNYI-NYI3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:WINS_BY_2PLUS (p 0.3553, phi -0.764)
- KXNHLSPREAD-26OCT13VANNYI-NYI2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:WINS_BY_2PLUS (p 0.3553, phi -1.0)

portfolios: A EV +3.43 (adj +0.97) on $40.00, P(profit) 0.6447, adj growth 6.1 bp · B EV +1.13 (adj +0.34) on $14.57, P(profit) 0.7568, adj growth 3.0 bp · C EV +1.07 (adj +0.33) on $14.62, P(profit) 0.7568, adj growth 2.9 bp · R EV +0.32 (adj +0.09) on $4.00, P(profit) 0.7568, adj growth 3.2 bp

## PIT @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_PIT_win | p_overtime | goals | shots CHI/PIT | CHI/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.45 | 0.55 | 0.00 | 6.03 | 27.0/27.4 | 23.4/23.7 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.111 | 0.38 | 0.62 | 0.00 | 6.0 | 21.6/32.8 | 28.4/18.8 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.47 | 0.53 | 0.46 | 5.91 | 21.4/32.6 | 29.2/18.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.49 | 0.51 | 0.45 | 5.98 | 26.7/27.3 | 24.0/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.43 | 0.57 | 0.00 | 9.36 | 28.1/28.8 | 22.2/22.5 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.083 | 0.38 | 0.62 | 0.00 | 9.32 | 22.8/34.3 | 26.5/17.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, PIT shot control · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_MIN_win | p_overtime | goals | shots WPG/MIN | WPG/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.50 | 0.50 | 0.00 | 5.98 | 27.9/28.1 | 24.5/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.47 | 5.91 | 28.0/28.1 | 24.8/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.47 | 0.53 | 0.00 | 9.29 | 29.7/29.7 | 23.5/23.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.069 | 0.45 | 0.55 | 0.00 | 5.97 | 22.2/33.2 | 29.1/19.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.065 | 0.56 | 0.44 | 0.00 | 5.99 | 32.7/22.3 | 19.1/28.7 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.47 | 0.53 | 0.45 | 5.89 | 22.8/33.4 | 30.0/19.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_COL_win | p_overtime | goals | shots DAL/COL | DAL/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.47 | 0.53 | 0.00 | 6.01 | 27.0/27.5 | 24.0/23.5 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.106 | 0.41 | 0.59 | 0.00 | 6.03 | 21.4/32.8 | 29.0/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.48 | 0.52 | 0.49 | 5.92 | 27.0/27.4 | 24.1/23.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.47 | 0.53 | 0.48 | 5.94 | 21.5/32.6 | 29.3/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.46 | 0.54 | 0.00 | 9.26 | 28.5/28.9 | 22.7/22.6 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.060 | 0.37 | 0.63 | 0.00 | 9.24 | 22.9/34.5 | 27.3/18.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_VGK_win | p_overtime | goals | shots NSH/VGK | NSH/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.49 | 0.51 | 0.00 | 6.02 | 27.7/28.1 | 24.3/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.49 | 0.51 | 0.47 | 5.92 | 27.5/28.0 | 24.7/24.3 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.101 | 0.42 | 0.58 | 0.00 | 6.0 | 21.8/32.8 | 28.7/18.8 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.47 | 0.53 | 0.47 | 5.88 | 22.2/33.3 | 29.9/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.46 | 0.54 | 0.00 | 9.27 | 29.3/29.9 | 23.8/23.4 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.061 | 0.38 | 0.62 | 0.00 | 9.3 | 23.5/35.3 | 27.8/18.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TOR_win | p_overtime | goals | shots UTA/TOR | UTA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| UTA shot control · normal event (5-7) · decided (2+) | 0.144 | 0.69 | 0.31 | 0.00 | 6.03 | 34.5/21.8 | 19.2/29.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.56 | 0.44 | 0.47 | 5.96 | 34.7/22.2 | 18.9/31.2 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.106 | 0.71 | 0.29 | 0.00 | 9.39 | 36.4/23.4 | 18.9/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.099 | 0.66 | 0.34 | 0.00 | 6.04 | 28.4/27.6 | 24.6/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.53 | 0.47 | 0.47 | 5.93 | 28.7/28.0 | 24.8/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.64 | 0.36 | 0.00 | 9.34 | 30.1/29.3 | 24.1/22.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts UTA shot control · normal event (5-7) · decided (2+) 0.14, UTA shot control · normal event (5-7) · tight (1-goal/OT) 0.12, UTA shot control · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_CGY_win | p_overtime | goals | shots ANA/CGY | ANA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.131 | 0.71 | 0.29 | 0.00 | 6.02 | 34.9/22.4 | 20.0/29.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.64 | 0.36 | 0.00 | 6.03 | 29.2/28.5 | 25.6/24.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.53 | 0.47 | 0.52 | 5.94 | 35.0/22.7 | 19.5/31.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.53 | 0.47 | 0.48 | 5.97 | 29.2/28.6 | 25.4/25.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.093 | 0.73 | 0.27 | 0.00 | 9.37 | 36.7/24.0 | 19.5/27.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.65 | 0.35 | 0.00 | 9.35 | 30.9/30.1 | 24.9/23.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_EDM_win | p_overtime | goals | shots LAK/EDM | LAK/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.43 | 0.57 | 0.00 | 5.98 | 27.9/28.0 | 24.1/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.51 | 0.49 | 0.50 | 5.9 | 27.9/28.2 | 24.9/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.48 | 0.52 | 0.00 | 9.24 | 29.3/29.5 | 23.2/23.4 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.073 | 0.41 | 0.59 | 0.00 | 5.99 | 22.3/32.9 | 28.9/19.4 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.45 | 0.55 | 0.46 | 5.88 | 22.2/32.9 | 29.5/19.0 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.062 | 0.52 | 0.48 | 0.00 | 5.95 | 32.7/22.1 | 19.0/28.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_BOS_win | p_overtime | goals | shots SJS/BOS | SJS/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.51 | 0.49 | 0.00 | 6.0 | 27.3/27.2 | 23.5/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.48 | 0.52 | 0.48 | 6.04 | 27.4/27.2 | 23.8/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.50 | 0.50 | 0.00 | 9.39 | 28.9/28.9 | 22.7/22.6 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.078 | 0.60 | 0.40 | 0.00 | 5.98 | 31.9/21.4 | 18.5/27.8 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.52 | 0.48 | 0.49 | 5.85 | 32.2/21.8 | 18.5/28.9 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.061 | 0.41 | 0.59 | 0.00 | 6.03 | 21.7/31.8 | 27.6/18.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
