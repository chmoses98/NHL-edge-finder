# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-20T08:11:10Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +26.25 | +6.75 | +23.38 | 0.641 | -54.27 | -74.25 | 47.52 |
| B thesis-diversified (joint) ← optimiser card | 121.76 | +15.77 | +4.94 | +15.52 | 0.681 | -29.55 | -44.25 | 43.39 |
| C best expression per thesis | 86.30 | +13.73 | +4.21 | +19.20 | 0.657 | -33.84 | -38.51 | 37.19 |
| R FUNDED research stakes | 37.00 | +5.03 | +1.62 | +4.53 | 0.663 | -10.22 | -14.11 | 0.00 |

## SJS @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_SJS_win | p_overtime | goals | shots MTL/SJS | MTL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 6.05 | 27.2/27.0 | 23.6/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.44 | 5.87 | 27.1/27.2 | 23.9/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.59 | 0.41 | 0.00 | 9.42 | 28.8/28.8 | 23.2/22.0 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.076 | 0.63 | 0.37 | 0.00 | 6.05 | 31.7/21.4 | 18.5/27.3 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.56 | 0.44 | 0.46 | 5.87 | 32.0/21.7 | 18.5/28.5 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.065 | 0.52 | 0.48 | 0.00 | 6.05 | 21.9/32.1 | 28.5/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Montreal wins by over 2.5 goals NO | 69 | 0.778 | 0.732 | +0.073 | +0.027 | $17.80 | FUNDED_RESEARCH | $5 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Montreal over 4.5 goals scored NO | 66 | 0.746 | 0.698 | +0.070 | +0.022 | $5.55 | FUNDED_RESEARCH | $2 | SJS:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Montreal over 2.5 goals scored NO | 26 | 0.338 | 0.294 | +0.064 | +0.020 | $1.82 | FUNDED_RESEARCH | $1 | MTL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| San Jose wins by over 1.5 goals YES | 18 | 0.239 | 0.207 | +0.049 | +0.017 | $1.92 | FUNDED_RESEARCH | $1 | SJS:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Montreal wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no; why: higher confidence-adjusted growth (7.56 vs 4.89 bp); wins across more scripts (relative breadth 1.01 vs 0.901); relationships: KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no: REINFORCING (phi 0.55); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3|no: DUPLICATIVE (phi 0.381); KXNHLSPREAD-26OCT20SJMTL-SJ2|yes: REINFORCING (phi 0.299); failure: MTL wins by 2+
- **Montreal over 4.5 goals scored NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20SJMTL-MTL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT20SJMTL-MTL3|no has the higher standalone adjusted growth (7.56 vs 4.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.550); they share one thesis budget; relationships: KXNHLSPREAD-26OCT20SJMTL-MTL3|no: REINFORCING (phi 0.55); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3|no: DUPLICATIVE (phi 0.417); KXNHLSPREAD-26OCT20SJMTL-SJ2|yes: DUPLICATIVE (phi 0.301); failure: MTL offense succeeds (4+ goals)
- **Montreal over 2.5 goals scored NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20SJMTL-MTL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT20SJMTL-MTL3|no has the higher standalone adjusted growth (7.56 vs 4.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.381); they share one thesis budget; relationships: KXNHLSPREAD-26OCT20SJMTL-MTL3|no: DUPLICATIVE (phi 0.381); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no: DUPLICATIVE (phi 0.417); KXNHLSPREAD-26OCT20SJMTL-SJ2|yes: REINFORCING (phi 0.474); failure: MTL offense succeeds (4+ goals)
- **San Jose wins by over 1.5 goals YES** — thesis: SJS wins by 2+; alternative: KXNHLSPREAD-26OCT20SJMTL-MTL3|no; why: Broad expression KXNHLSPREAD-26OCT20SJMTL-SJ2|yes selected over broad KXNHLSPREAD-26OCT20SJMTL-SJ3|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.61 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT20SJMTL-MTL3|no: REINFORCING (phi 0.299); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no: DUPLICATIVE (phi 0.301); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3|no: REINFORCING (phi 0.474); failure: MTL wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:WINS (p 0.445): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20SJMTL-MTL3|no (same contract)
- thesis MTL:SUPPRESSED (p 0.3476): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20SJMTL-MTL3|no (same contract)
- thesis SJS:WINS_BY_2PLUS (p 0.2394): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20SJMTL-MTL3|no (same contract)
- KXNHLSPREAD-26OCT20SJMTL-MTL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.3311, phi -0.758)
- KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4381, phi -0.662)
- KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4381, phi -0.63)
- KXNHLSPREAD-26OCT20SJMTL-SJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS (p 0.555, phi -0.627)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT20SJMTL-MTL2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no kept
- override: Broad expression KXNHLSPREAD-26OCT20SJMTL-SJ2|yes selected over broad KXNHLSPREAD-26OCT20SJMTL-SJ3|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.61 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.29 (adj +1.25) on $28.55, P(profit) 0.6117, adj growth 10.2 bp · B EV +3.35 (adj +1.16) on $27.09, P(profit) 0.6849, adj growth 10.2 bp · C EV +2.08 (adj +0.76) on $20.00, P(profit) 0.7784, adj growth 6.9 bp · R EV +1.22 (adj +0.42) on $9.00, P(profit) 0.6849, adj growth 13.7 bp

## COL @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_COL_win | p_overtime | goals | shots NJD/COL | NJD/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.43 | 0.57 | 0.00 | 5.98 | 28.6/28.9 | 24.9/25.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.48 | 0.52 | 0.47 | 5.96 | 28.6/28.8 | 25.3/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.43 | 0.57 | 0.00 | 9.31 | 30.3/30.6 | 24.2/24.7 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.069 | 0.38 | 0.62 | 0.00 | 5.95 | 23.0/34.1 | 29.8/20.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.44 | 0.56 | 0.47 | 5.87 | 23.1/34.3 | 30.9/20.0 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.060 | 0.49 | 0.51 | 0.00 | 5.95 | 33.8/23.1 | 19.7/30.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## ANA @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_ANA_win | p_overtime | goals | shots NYI/ANA | NYI/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.54 | 0.46 | 0.00 | 6.03 | 27.6/27.7 | 24.4/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.48 | 5.93 | 27.7/27.9 | 24.6/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.57 | 0.43 | 0.00 | 9.38 | 29.5/29.6 | 23.7/22.5 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.074 | 0.54 | 0.46 | 0.00 | 6.0 | 22.4/32.8 | 29.3/18.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.48 | 0.52 | 0.47 | 5.86 | 22.5/33.4 | 30.2/19.2 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.064 | 0.62 | 0.38 | 0.00 | 6.04 | 32.7/22.5 | 19.6/28.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## LAK @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_LAK_win | p_overtime | goals | shots WSH/LAK | WSH/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.62 | 0.38 | 0.00 | 5.99 | 27.3/27.5 | 24.5/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.45 | 5.84 | 27.2/27.5 | 24.3/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.64 | 0.36 | 0.00 | 9.11 | 29.2/29.2 | 24.0/22.3 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.50 | 0.50 | 0.47 | 5.87 | 21.7/32.3 | 29.1/18.6 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.072 | 0.54 | 0.46 | 0.00 | 5.97 | 22.3/32.8 | 29.4/18.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.53 | 0.47 | 0.52 | 2.83 | 26.1/26.4 | 24.9/24.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_TOR_win | p_overtime | goals | shots CBJ/TOR | CBJ/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CBJ shot control · normal event (5-7) · decided (2+) | 0.127 | 0.67 | 0.33 | 0.00 | 6.01 | 34.7/22.1 | 19.4/30.2 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.49 | 5.86 | 34.5/22.7 | 19.6/31.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.65 | 0.35 | 0.00 | 5.99 | 28.9/28.2 | 25.3/24.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.51 | 0.49 | 0.50 | 5.91 | 28.8/28.1 | 24.9/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.61 | 0.39 | 0.00 | 9.19 | 30.3/29.6 | 24.2/23.4 | even strength |
| CBJ shot control · high event (8+) · decided (2+) | 0.073 | 0.70 | 0.30 | 0.00 | 9.22 | 36.4/23.8 | 19.4/28.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 4.5 goals scored NO | 19 | 0.244 | 0.215 | +0.044 | +0.014 | $3.94 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | DIRECT (0.92) | EVIDENCE_MIXED | D |
- **Full Game: Over 4.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT20TORCBJ-6|no; why: higher confidence-adjusted growth (2.63 vs 0.41 bp); alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: CBJ offense succeeds (4+ goals)

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.13, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis GAME:LOW_EVENT (p 0.2655): highest fidelity KXNHLTOTAL-26OCT20TORCBJ-5|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT20TORCBJ-5|no (same contract)
- KXNHLTOTAL-26OCT20TORCBJ-5|no: FUNDED_RESEARCH; family MIXED; loses 8% of the draws where the thesis happens; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4212, phi -0.428)

portfolios: A EV +1.69 (adj +0.54) on $7.79, P(profit) 0.2444, adj growth 4.0 bp · B EV +0.86 (adj +0.27) on $3.94, P(profit) 0.2444, adj growth 2.4 bp · C EV +0.86 (adj +0.27) on $3.94, P(profit) 0.2444, adj growth 2.4 bp · R EV +0.22 (adj +0.07) on $1.00, P(profit) 0.2444, adj growth 2.4 bp

## WPG @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_WPG_win | p_overtime | goals | shots STL/WPG | STL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.64 | 0.36 | 0.00 | 6.01 | 26.5/26.5 | 23.6/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.48 | 5.92 | 26.6/26.7 | 23.4/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.63 | 0.37 | 0.00 | 9.23 | 28.1/28.0 | 22.7/21.3 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.081 | 0.71 | 0.29 | 0.00 | 5.99 | 31.2/20.9 | 18.5/26.8 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.55 | 0.45 | 0.45 | 5.91 | 31.1/21.2 | 18.1/27.8 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.063 | 0.61 | 0.39 | 0.00 | 5.98 | 21.2/31.3 | 28.1/17.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_BOS_win | p_overtime | goals | shots DAL/BOS | DAL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.54 | 0.46 | 0.00 | 6.0 | 26.5/26.1 | 22.8/22.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.113 | 0.58 | 0.42 | 0.00 | 5.99 | 31.6/20.7 | 17.7/27.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.47 | 5.94 | 26.6/26.3 | 23.0/23.2 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.54 | 0.46 | 0.48 | 5.88 | 31.5/21.0 | 17.7/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.52 | 0.48 | 0.00 | 9.25 | 28.1/27.8 | 21.9/22.2 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.064 | 0.59 | 0.41 | 0.00 | 9.15 | 33.2/22.0 | 16.9/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Boston over 2.5 goals scored YES | 51 | 0.590 | 0.545 | +0.063 | +0.018 | $5.18 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Boston over 3.5 goals scored YES | 30 | 0.369 | 0.330 | +0.054 | +0.015 | $1.90 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 75 | 0.808 | 0.776 | +0.045 | +0.013 | $10.03 | FUNDED_RESEARCH | $3 | BOS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Boston over 2.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes; why: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes has the higher standalone adjusted growth (3.16 vs 2.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.409); relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes: DUPLICATIVE (phi 0.637); KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: REINFORCING (phi 0.403); failure: BOS offense suppressed (<= 2 goals)
- **Boston over 3.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes selected over broad KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: DUPLICATIVE (phi 0.637); KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: DUPLICATIVE (phi 0.327); failure: BOS offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: BOS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes; why: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes has the higher standalone adjusted growth (3.16 vs 2.16 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.226); relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: REINFORCING (phi 0.403); KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes: DUPLICATIVE (phi 0.327); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.3574): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes (same contract)
- thesis BOS:WINS (p 0.4716): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:WINS_BY_2PLUS (p 0.2606): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.4217, phi -0.976)
- KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.4217, phi -0.653)
- KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3054, phi -0.735)
- override: Broad expression KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes selected over broad KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.32 (adj +1.52) on $28.55, P(profit) 0.3691, adj growth 7.8 bp · B EV +1.53 (adj +0.44) on $17.12, P(profit) 0.5548, adj growth 3.8 bp · C EV +1.05 (adj +0.31) on $3.41, P(profit) 0.194, adj growth 2.7 bp · R EV +0.59 (adj +0.17) on $6.00, P(profit) 0.5635, adj growth 5.4 bp

## MIN @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_MIN_win | p_overtime | goals | shots EDM/MIN | EDM/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.64 | 0.36 | 0.00 | 6.04 | 28.6/28.5 | 25.5/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.49 | 6.0 | 28.6/28.5 | 25.1/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.63 | 0.37 | 0.00 | 9.42 | 30.2/30.0 | 24.6/23.0 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.086 | 0.70 | 0.30 | 0.00 | 6.02 | 33.6/22.6 | 20.0/28.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.069 | 0.69 | 0.31 | 0.00 | 9.5 | 35.7/24.3 | 19.6/27.5 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.53 | 0.47 | 0.46 | 6.0 | 34.1/23.0 | 19.7/30.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_DET_win | p_overtime | goals | shots SEA/DET | SEA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.63 | 0.37 | 0.00 | 5.99 | 27.7/28.1 | 25.0/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.48 | 5.91 | 28.0/28.5 | 25.1/24.7 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.097 | 0.56 | 0.44 | 0.00 | 6.02 | 22.3/33.4 | 29.9/18.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.65 | 0.35 | 0.00 | 9.26 | 29.2/29.6 | 24.6/22.3 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.49 | 0.51 | 0.48 | 5.91 | 22.2/33.5 | 30.1/18.9 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.058 | 0.59 | 0.41 | 0.00 | 9.3 | 24.2/35.5 | 29.5/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Detroit wins by over 2.5 goals NO | 82 | 0.873 | 0.844 | +0.042 | +0.013 | $14.89 | FUNDED_RESEARCH | $4 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit wins by over 1.5 goals NO | 72 | 0.784 | 0.750 | +0.050 | +0.015 | $8.02 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Detroit wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20DETSEA-DET2|no; why: higher confidence-adjusted growth (2.82 vs 2.72 bp); despite a smaller raw edge (+0.042 vs +0.050/contract); relationships: KXNHLSPREAD-26OCT20DETSEA-DET2|no: DUPLICATIVE (phi 0.729); failure: DET wins by 2+
- **Detroit wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20DETSEA-DET3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT20DETSEA-DET3|no has the higher standalone adjusted growth (2.82 vs 2.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.729); they share one thesis budget; relationships: KXNHLSPREAD-26OCT20DETSEA-DET3|no: DUPLICATIVE (phi 0.729); failure: DET wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:WINS (p 0.575): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no (same contract)
- thesis DET:SUPPRESSED (p 0.4607): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT20DETSEA-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2157, phi -0.729)
- KXNHLSPREAD-26OCT20DETSEA-DET2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2157, phi -1.0)

portfolios: A EV +1.86 (adj +0.51) on $28.55, P(profit) 0.6245, adj growth 4.1 bp · B EV +1.30 (adj +0.41) on $22.91, P(profit) 0.7843, adj growth 3.6 bp · C EV +1.02 (adj +0.32) on $20.00, P(profit) 0.8725, adj growth 2.9 bp · R EV +0.41 (adj +0.13) on $7.00, P(profit) 0.7843, adj growth 4.4 bp

## CAR @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 15 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CAR_win | p_overtime | goals | shots VAN/CAR | VAN/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.169 | 0.38 | 0.62 | 0.00 | 6.03 | 20.9/34.0 | 29.8/18.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.147 | 0.44 | 0.56 | 0.47 | 5.96 | 21.3/34.7 | 31.2/18.1 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.127 | 0.39 | 0.61 | 0.00 | 9.39 | 22.4/36.1 | 28.4/17.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.074 | 0.45 | 0.55 | 0.00 | 6.09 | 26.9/28.0 | 24.2/23.5 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.073 | 0.39 | 0.61 | 0.00 | 3.44 | 19.6/33.4 | 31.1/18.1 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.069 | 0.44 | 0.56 | 0.48 | 2.85 | 19.4/32.4 | 30.9/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 49 | 0.663 | 0.547 | +0.155 | +0.040 | $13.64 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 4.5 goals scored YES | 12 | 0.195 | 0.153 | +0.068 | +0.025 | $4.26 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| Carolina over 5.5 goals scored NO | 81 | 0.873 | 0.839 | +0.052 | +0.018 | $15.45 | FUNDED_RESEARCH | $4 | VAN:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: higher confidence-adjusted growth (13.78 vs 12.31 bp); wins across more scripts (relative breadth 0.927 vs 0.564); relationships: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes: REINFORCING (phi 0.313); KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no: DUPLICATIVE (phi 0.421); failure: CAR wins by 2+
- **Vancouver over 4.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20CARVAN-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT20CARVAN-CAR2|no has the higher standalone adjusted growth (13.78 vs 12.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.313); they share one thesis budget; relationships: KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.313); KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no: INTENTIONAL_DIVERSIFIER (phi -0.003); failure: CAR wins (incl. OT/SO)
- **Carolina over 5.5 goals scored NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20CARVAN-CAR2|no; why: Broad expression KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-CAR2|no because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.43 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT20CARVAN-CAR2|no: DUPLICATIVE (phi 0.421); KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes: INTENTIONAL_DIVERSIFIER (phi -0.003); failure: high-event game (8+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:WINS (p 0.4338): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3558): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20CARVAN-VAN4|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes kept
- thesis VAN:WINS_BY_2PLUS (p 0.2322): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- KXNHLSPREAD-26OCT20CARVAN-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 17.8 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3374, phi -1.0)
- KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes: FUNDED_RESEARCH; family MIXED; loses 45% of the draws where the thesis happens; opposing: failure thesis CAR:WINS (p 0.5662, phi -0.459)
- KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2928, phi -0.501)
- override: Broad expression KXNHLSPREAD-26OCT20CARVAN-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20CARVAN-VAN4|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes kept
- override: Broad expression KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-CAR2|no because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.43 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.19 (adj +1.83) on $28.55, P(profit) 0.6626, adj growth 14.7 bp · B EV +7.41 (adj +2.25) on $33.35, P(profit) 0.6698, adj growth 19.7 bp · C EV +7.48 (adj +2.15) on $21.55, P(profit) 0.6698, adj growth 18.8 bp · R EV +2.24 (adj +0.72) on $9.00, P(profit) 0.6698, adj growth 23.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT20CARVAN-VAN|yes == KXNHLGAME-26OCT20CARVAN-CAR|no

## TBL @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TBL_win | p_overtime | goals | shots VGK/TBL | VGK/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.65 | 0.35 | 0.00 | 6.01 | 26.9/26.8 | 23.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.54 | 0.46 | 0.47 | 5.92 | 27.1/27.3 | 24.0/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.64 | 0.36 | 0.00 | 9.19 | 28.4/28.5 | 23.3/21.5 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.072 | 0.57 | 0.43 | 0.00 | 5.97 | 21.5/31.8 | 28.5/17.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.070 | 0.65 | 0.35 | 0.00 | 6.0 | 31.5/21.2 | 18.4/26.8 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.47 | 0.53 | 0.47 | 5.84 | 21.5/31.8 | 28.3/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 1.5 goals NO | 72 | 0.787 | 0.751 | +0.053 | +0.017 | $16.22 | FUNDED_RESEARCH | $5 | VGK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 1.5 goals YES | 30 | 0.355 | 0.325 | +0.040 | +0.010 | $1.13 | SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS | $0 | VGK:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: VGK wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no; why: higher confidence-adjusted growth (3.17 vs 2.43 bp); wins across more scripts (relative breadth 0.981 vs 0.609); relationships: KXNHLSPREAD-26OCT20TBVGK-VGK2|yes: DUPLICATIVE (phi 0.386); failure: TBL wins by 2+
- **Vegas wins by over 1.5 goals YES** — thesis: VGK wins by 2+; alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: Broad expression KXNHLSPREAD-26OCT20TBVGK-VGK2|yes selected over broad KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.59 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT20TBVGK-TB2|no: DUPLICATIVE (phi 0.386); failure: tight game (one-goal final or OT)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis VGK:WINS (p 0.5853): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis TBL:SUPPRESSED (p 0.4748): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis VGK:WINS_BY_2PLUS (p 0.3549): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- KXNHLSPREAD-26OCT20TBVGK-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2132, phi -1.0)
- KXNHLSPREAD-26OCT20TBVGK-VGK2|yes: SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:TIGHT (p 0.4319, phi -0.647)
- override: Broad expression KXNHLSPREAD-26OCT20TBVGK-VGK2|yes selected over broad KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.59 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.90 (adj +1.10) on $28.00, P(profit) 0.4164, adj growth 6.7 bp · B EV +1.31 (adj +0.41) on $17.35, P(profit) 0.7868, adj growth 3.6 bp · C EV +1.25 (adj +0.40) on $17.40, P(profit) 0.7868, adj growth 3.5 bp · R EV +0.36 (adj +0.11) on $5.00, P(profit) 0.7868, adj growth 3.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
