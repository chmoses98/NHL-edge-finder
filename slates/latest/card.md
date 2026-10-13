# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-13T13:43:43Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +17.55 | +5.04 | +18.09 | 0.615 | -56.55 | -75.73 | 34.95 |
| B thesis-diversified (joint) ← optimiser card | 98.72 | +10.09 | +3.57 | +10.15 | 0.636 | -27.54 | -39.40 | 31.67 |
| C best expression per thesis | 64.30 | +6.30 | +2.26 | +7.87 | 0.689 | -17.08 | -17.08 | 20.17 |
| R FUNDED research stakes | 29.00 | +3.15 | +1.10 | +2.80 | 0.633 | -8.49 | -11.77 | 0.00 |

## NJD @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_NJD_win | p_overtime | goals | shots DET/NJD | DET/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.58 | 0.42 | 0.00 | 5.95 | 27.9/28.1 | 24.9/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.49 | 5.92 | 28.2/28.4 | 25.1/24.9 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.073 | 0.51 | 0.49 | 0.48 | 2.78 | 26.7/26.9 | 25.4/25.3 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.48 | 0.52 | 0.47 | 5.84 | 22.6/33.4 | 30.0/19.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.072 | 0.52 | 0.48 | 0.00 | 5.97 | 22.4/33.4 | 29.9/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.59 | 0.41 | 0.00 | 9.06 | 29.9/29.9 | 24.2/23.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey over 4.5 goals scored NO | 79 | 0.851 | 0.818 | +0.049 | +0.016 | $19.95 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey over 3.5 goals scored NO | 61 | 0.685 | 0.643 | +0.059 | +0.016 | $1.20 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Full Game: Over 3.5 goals scored NO | 14 | 0.185 | 0.160 | +0.037 | +0.012 | $2.18 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | DIRECT (0.62) | EVIDENCE_MIXED | D |
- **New Jersey over 4.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no; why: higher confidence-adjusted growth (3.68 vs 2.43 bp); despite a smaller raw edge (+0.049 vs +0.059/contract); relationships: KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no: DUPLICATIVE (phi 0.618); KXNHLTOTAL-26OCT13NJDET-4|no: REINFORCING (phi 0.2); failure: NJD offense succeeds (4+ goals)
- **New Jersey over 3.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no has the higher standalone adjusted growth (3.68 vs 2.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.618); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no: DUPLICATIVE (phi 0.618); KXNHLTOTAL-26OCT13NJDET-4|no: DUPLICATIVE (phi 0.323); failure: NJD offense succeeds (4+ goals)
- **Full Game: Over 3.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no has the higher standalone adjusted growth (3.68 vs 2.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.200); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no: REINFORCING (phi 0.2); KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no: DUPLICATIVE (phi 0.323); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · low event (<=4) · tight (1-goal/OT) 0.07.
- thesis NJD:SUPPRESSED (p 0.4787): highest fidelity KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no (same contract)
- thesis GAME:LOW_EVENT (p 0.2998): highest fidelity KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no (same contract)
- KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3041, phi -0.633)
- KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3041, phi -0.976)
- KXNHLTOTAL-26OCT13NJDET-4|no: FUNDED_RESEARCH; family MIXED; loses 38% of the draws where the thesis happens; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.361, phi -0.358)

portfolios: A EV +3.57 (adj +1.03) on $39.47, P(profit) 0.4652, adj growth 6.7 bp · B EV +1.88 (adj +0.61) on $23.33, P(profit) 0.8508, adj growth 5.4 bp · C EV +1.23 (adj +0.41) on $20.00, P(profit) 0.8508, adj growth 3.7 bp · R EV +0.65 (adj +0.21) on $7.00, P(profit) 0.6855, adj growth 6.8 bp

## FLA @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_FLA_win | p_overtime | goals | shots CBJ/FLA | CBJ/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.70 | 0.30 | 0.00 | 5.96 | 27.2/27.0 | 24.4/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.47 | 5.88 | 27.4/27.2 | 23.8/24.1 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.094 | 0.75 | 0.25 | 0.00 | 5.95 | 32.5/21.7 | 19.3/27.7 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.56 | 0.44 | 0.50 | 5.88 | 32.6/21.6 | 18.4/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.70 | 0.30 | 0.00 | 9.21 | 28.8/28.7 | 24.0/21.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.66 | 0.34 | 0.00 | 3.47 | 26.1/25.7 | 24.3/23.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 2.5 goals NO | 84 | 0.906 | 0.871 | +0.057 | +0.021 | $15.01 | FUNDED_RESEARCH | $4 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 75 | 0.825 | 0.785 | +0.062 | +0.022 | $9.23 | FUNDED_RESEARCH | $3 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Columbus wins by over 1.5 goals YES | 31 | 0.393 | 0.349 | +0.068 | +0.024 | $3.93 | FUNDED_RESEARCH | $1 | CBJ:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida over 3.5 goals scored NO | 65 | 0.725 | 0.682 | +0.059 | +0.017 | $1.82 | FUNDED_RESEARCH | $1 | FLA:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13FLACBJ-FLA2|no; why: higher confidence-adjusted growth (7.86 vs 5.89 bp); despite a smaller raw edge (+0.057 vs +0.062/contract); relationships: KXNHLSPREAD-26OCT13FLACBJ-FLA2|no: DUPLICATIVE (phi 0.698); KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes: REINFORCING (phi 0.258); KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA4|no: DUPLICATIVE (phi 0.443); failure: FLA wins by 2+
- **Florida wins by over 1.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no has the higher standalone adjusted growth (7.86 vs 5.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.698); they share one thesis budget; relationships: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: DUPLICATIVE (phi 0.698); KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes: DUPLICATIVE (phi 0.37); KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA4|no: REINFORCING (phi 0.491); failure: FLA wins by 2+
- **Columbus wins by over 1.5 goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no has the higher standalone adjusted growth (7.86 vs 5.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.258); they share one thesis budget; relationships: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: REINFORCING (phi 0.258); KXNHLSPREAD-26OCT13FLACBJ-FLA2|no: DUPLICATIVE (phi 0.37); KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA4|no: REINFORCING (phi 0.394); failure: tight game (one-goal final or OT)
- **Florida over 3.5 goals scored NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no; why: Broad expression KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA4|no selected over broad KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA3|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: DUPLICATIVE (phi 0.443); KXNHLSPREAD-26OCT13FLACBJ-FLA2|no: REINFORCING (phi 0.491); KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes: REINFORCING (phi 0.394); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:WINS (p 0.6232): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.3927): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes (same contract)
- thesis FLA:SUPPRESSED (p 0.5184): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes — Broad expression KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA4|no selected over broad KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA3|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.1748, phi -0.698)
- KXNHLSPREAD-26OCT13FLACBJ-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.1748, phi -1.0)
- KXNHLSPREAD-26OCT13FLACBJ-CBJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:TIGHT (p 0.4325, phi -0.702)
- KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2644, phi -0.973)
- override: Broad expression KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA4|no selected over broad KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA3|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.09 (adj +1.69) on $39.47, P(profit) 0.5773, adj growth 12.5 bp · B EV +2.74 (adj +0.98) on $30.00, P(profit) 0.7035, adj growth 8.9 bp · C EV +1.34 (adj +0.50) on $20.00, P(profit) 0.9064, adj growth 4.8 bp · R EV +0.81 (adj +0.28) on $9.00, P(profit) 0.7035, adj growth 10.2 bp

## BUF @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_BUF_win | p_overtime | goals | shots MTL/BUF | MTL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.61 | 0.39 | 0.00 | 6.02 | 26.9/27.5 | 24.5/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.53 | 0.47 | 0.47 | 5.98 | 27.0/27.6 | 24.5/23.8 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.101 | 0.55 | 0.45 | 0.00 | 6.01 | 21.4/32.7 | 29.2/18.0 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.52 | 0.48 | 0.47 | 5.97 | 21.7/32.8 | 29.5/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.64 | 0.36 | 0.00 | 9.25 | 28.5/28.9 | 23.5/21.6 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.063 | 0.54 | 0.47 | 0.00 | 9.2 | 23.2/34.7 | 28.8/17.4 | even strength |

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
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.51 | 0.49 | 0.47 | 5.89 | 26.9/26.8 | 23.6/23.7 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.082 | 0.60 | 0.40 | 0.00 | 5.93 | 31.6/21.1 | 18.3/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.57 | 0.43 | 0.00 | 9.21 | 28.3/28.4 | 22.7/22.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.51 | 0.49 | 0.00 | 3.45 | 25.4/25.5 | 23.7/23.4 | even strength |
| PHI shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.54 | 0.46 | 0.46 | 5.87 | 31.6/21.2 | 18.1/28.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, PHI shot control · normal event (5-7) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TBL @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_TBL_win | p_overtime | goals | shots NYR/TBL | NYR/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.56 | 0.44 | 0.00 | 6.0 | 25.7/26.1 | 22.9/21.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.47 | 5.91 | 25.9/26.3 | 22.9/22.7 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.108 | 0.43 | 0.57 | 0.00 | 5.94 | 20.4/31.3 | 27.4/17.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.46 | 0.54 | 0.46 | 5.87 | 20.9/31.8 | 28.4/17.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.068 | 0.58 | 0.42 | 0.00 | 9.17 | 27.6/27.9 | 22.6/20.8 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.058 | 0.47 | 0.53 | 0.43 | 2.78 | 24.6/24.9 | 23.4/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York R wins by over 1.5 goals YES | 21 | 0.292 | 0.248 | +0.070 | +0.027 | $5.01 | FUNDED_RESEARCH | $2 | NYR:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 76 | 0.842 | 0.798 | +0.069 | +0.026 | $20.00 | FUNDED_RESEARCH | $5 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 2.5 goals scored NO | 34 | 0.430 | 0.382 | +0.074 | +0.027 | $3.70 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
- **New York R wins by over 1.5 goals YES** — thesis: NYR wins by 2+; alternative: KXNHLSPREAD-26OCT13TBNYR-TB3|no; why: higher confidence-adjusted growth (8.97 vs 8.33 bp); relationships: KXNHLSPREAD-26OCT13TBNYR-TB3|no: REINFORCING (phi 0.278); KXNHLTEAMTOTAL-26OCT13TBNYR-TB3|no: REINFORCING (phi 0.467); failure: TBL wins (incl. OT/SO)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes has the higher standalone adjusted growth (8.97 vs 8.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.278); they share one thesis budget; relationships: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: REINFORCING (phi 0.278); KXNHLTEAMTOTAL-26OCT13TBNYR-TB3|no: DUPLICATIVE (phi 0.376); failure: TBL wins by 2+
- **Tampa Bay over 2.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes has the higher standalone adjusted growth (8.97 vs 6.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.467); they share one thesis budget; relationships: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: REINFORCING (phi 0.467); KXNHLSPREAD-26OCT13TBNYR-TB3|no: DUPLICATIVE (phi 0.376); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.11.
- thesis NYR:WINS_BY_2PLUS (p 0.2917): highest fidelity KXNHLSPREAD-26OCT13TBNYR-NYR2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13TBNYR-NYR2|yes (same contract)
- thesis NYR:WINS (p 0.5147): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13TBNYR-NYR2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.4396): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13TBNYR-NYR2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS (p 0.4853, phi -0.623)
- KXNHLSPREAD-26OCT13TBNYR-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2612, phi -0.729)
- KXNHLTEAMTOTAL-26OCT13TBNYR-TB3|no: FUNDED_RESEARCH; family MIXED; loses 2% of the draws where the thesis happens; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3385, phi -0.621)

portfolios: A EV +6.34 (adj +1.57) on $39.47, P(profit) 0.6053, adj growth 10.5 bp · B EV +4.14 (adj +1.55) on $28.70, P(profit) 0.491, adj growth 13.7 bp · C EV +2.41 (adj +0.92) on $7.61, P(profit) 0.2917, adj growth 8.0 bp · R EV +1.29 (adj +0.48) on $8.00, P(profit) 0.491, adj growth 16.3 bp

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
