# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-20T04:25:03Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +25.22 | +5.83 | +21.93 | 0.639 | -55.61 | -77.77 | 37.77 |
| B thesis-diversified (joint) ← optimiser card | 68.98 | +12.36 | +4.09 | +8.73 | 0.634 | -26.43 | -37.04 | 35.65 |
| C best expression per thesis | 45.48 | +9.83 | +3.63 | -2.47 | 0.500 | -26.61 | -31.51 | 31.43 |
| R FUNDED research stakes | 21.00 | +3.97 | +1.34 | +1.35 | 0.619 | -7.83 | -11.65 | 0.00 |

## SJS @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 2 on card


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
| Montreal wins by over 2.5 goals NO | 70 | 0.778 | 0.737 | +0.064 | +0.022 | $18.70 | FUNDED_RESEARCH | $5 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| San Jose wins by over 1.5 goals YES | 18 | 0.239 | 0.205 | +0.049 | +0.014 | $2.35 | FUNDED_RESEARCH | $1 | SJS:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Montreal wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20SJMTL-SJ3|yes; why: higher confidence-adjusted growth (5.22 vs 4.42 bp); wins across more scripts (relative breadth 1.01 vs 0.459); relationships: KXNHLSPREAD-26OCT20SJMTL-SJ2|yes: REINFORCING (phi 0.299); failure: MTL wins by 2+
- **San Jose wins by over 1.5 goals YES** — thesis: SJS wins by 2+; alternative: KXNHLSPREAD-26OCT20SJMTL-MTL3|no; why: Broad expression KXNHLSPREAD-26OCT20SJMTL-SJ2|yes selected over broad KXNHLSPREAD-26OCT20SJMTL-SJ3|yes because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.61 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT20SJMTL-MTL3|no: REINFORCING (phi 0.299); failure: MTL wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:WINS (p 0.445): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20SJMTL-MTL3|no (same contract)
- thesis SJS:WINS_BY_2PLUS (p 0.2394): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20SJMTL-MTL3|no (same contract)
- thesis MTL:SUPPRESSED (p 0.3476): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20SJMTL-MTL3|no (same contract)
- KXNHLSPREAD-26OCT20SJMTL-MTL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.3311, phi -0.758)
- KXNHLSPREAD-26OCT20SJMTL-SJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS (p 0.555, phi -0.627)
- override: Broad expression KXNHLSPREAD-26OCT20SJMTL-SJ2|yes selected over broad KXNHLSPREAD-26OCT20SJMTL-SJ3|yes because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.61 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.22 (adj +1.04) on $37.68, P(profit) 0.6689, adj growth 8.0 bp · B EV +2.27 (adj +0.75) on $21.06, P(profit) 0.7784, adj growth 6.6 bp · C EV +1.78 (adj +0.62) on $20.00, P(profit) 0.7784, adj growth 5.5 bp · R EV +0.70 (adj +0.23) on $6.00, P(profit) 0.7784, adj growth 7.8 bp

## COL @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_COL_win | p_overtime | goals | shots NJD/COL | NJD/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.45 | 0.55 | 0.00 | 6.03 | 28.6/28.8 | 25.0/25.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.52 | 0.48 | 0.48 | 5.95 | 28.8/29.0 | 25.8/25.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.43 | 0.57 | 0.00 | 9.13 | 29.9/30.2 | 23.9/24.4 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.076 | 0.38 | 0.62 | 0.00 | 6.04 | 22.9/33.9 | 29.7/19.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.47 | 0.53 | 0.49 | 5.95 | 22.9/33.8 | 30.5/19.6 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.062 | 0.49 | 0.51 | 0.00 | 5.98 | 33.7/23.2 | 19.7/30.0 | even strength |

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
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.62 | 0.38 | 0.00 | 6.0 | 27.3/27.5 | 24.5/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.46 | 5.85 | 27.2/27.5 | 24.3/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.64 | 0.36 | 0.00 | 9.11 | 29.2/29.3 | 24.1/22.2 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.50 | 0.50 | 0.46 | 5.86 | 21.7/32.3 | 29.1/18.6 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.073 | 0.54 | 0.46 | 0.00 | 5.96 | 22.3/32.9 | 29.4/18.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.54 | 0.46 | 0.52 | 2.82 | 26.2/26.4 | 24.9/24.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_TOR_win | p_overtime | goals | shots CBJ/TOR | CBJ/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CBJ shot control · normal event (5-7) · decided (2+) | 0.128 | 0.65 | 0.35 | 0.00 | 5.98 | 34.1/22.0 | 19.3/29.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.61 | 0.39 | 0.00 | 6.0 | 29.0/28.3 | 25.1/25.1 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.56 | 0.44 | 0.48 | 5.84 | 34.6/22.4 | 19.3/30.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.49 | 0.51 | 0.48 | 5.89 | 28.5/27.9 | 24.5/25.2 | even strength |
| CBJ shot control · high event (8+) · decided (2+) | 0.082 | 0.68 | 0.32 | 0.00 | 9.17 | 36.4/23.9 | 19.4/28.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.60 | 0.40 | 0.00 | 9.13 | 30.6/29.9 | 24.6/24.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_WPG_win | p_overtime | goals | shots STL/WPG | STL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.64 | 0.36 | 0.00 | 6.01 | 26.5/26.6 | 23.6/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.48 | 5.92 | 26.6/26.7 | 23.5/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.63 | 0.37 | 0.00 | 9.24 | 28.2/28.0 | 22.7/21.3 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.081 | 0.71 | 0.29 | 0.00 | 5.99 | 31.2/20.9 | 18.5/26.7 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.55 | 0.45 | 0.46 | 5.91 | 31.1/21.2 | 18.1/27.7 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.064 | 0.61 | 0.39 | 0.00 | 5.98 | 21.2/31.2 | 28.1/17.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 1 on card


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
| Dallas wins by over 2.5 goals NO | 75 | 0.808 | 0.776 | +0.045 | +0.013 | $3.12 | FUNDED_RESEARCH | $1 | BOS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 2.5 goals NO** — thesis: BOS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes; why: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes has the higher standalone adjusted growth (3.16 vs 2.16 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.226); relationships: only recommended bet in this game; failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.3574): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes (same contract)
- thesis BOS:WINS (p 0.4716): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:WINS_BY_2PLUS (p 0.2606): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3054, phi -0.735)

portfolios: A EV +4.60 (adj +1.27) on $37.68, P(profit) 0.5391, adj growth 7.1 bp · B EV +0.18 (adj +0.05) on $3.12, P(profit) 0.8079, adj growth 0.5 bp · C EV +1.05 (adj +0.31) on $3.41, P(profit) 0.194, adj growth 2.7 bp · R EV +0.06 (adj +0.02) on $1.00, P(profit) 0.8079, adj growth 0.7 bp

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

## DET @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


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
| Detroit over 3.5 goals scored NO | 60 | 0.664 | 0.629 | +0.047 | +0.013 | $8.62 | FUNDED_RESEARCH | $3 | DET:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Detroit over 3.5 goals scored NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20DETSEA-DET3|no; why: higher confidence-adjusted growth (1.50 vs 1.29 bp); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DET:SUPPRESSED (p 0.4607): highest fidelity KXNHLTEAMTOTAL-26OCT20DETSEA-DET4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20DETSEA-DET4|no (same contract)
- KXNHLTEAMTOTAL-26OCT20DETSEA-DET4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3257, phi -0.977)

portfolios: A EV +1.15 (adj +0.31) on $15.07, P(profit) 0.664, adj growth 2.4 bp · B EV +0.66 (adj +0.18) on $8.62, P(profit) 0.664, adj growth 1.6 bp · C EV +0.66 (adj +0.18) on $8.62, P(profit) 0.664, adj growth 1.6 bp · R EV +0.23 (adj +0.06) on $3.00, P(profit) 0.664, adj growth 2.0 bp

## CAR @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 14 +EV candidates, 4 on card


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
| Vancouver wins by over 1.5 goals YES | 14 | 0.232 | 0.184 | +0.084 | +0.035 | $5.17 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 4.5 goals scored YES | 12 | 0.195 | 0.155 | +0.068 | +0.028 | $3.14 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 63 | 0.778 | 0.678 | +0.131 | +0.032 | $15.89 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina over 5.5 goals scored NO | 81 | 0.873 | 0.836 | +0.052 | +0.015 | $7.29 | FUNDED_RESEARCH | $2 | VAN:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: higher confidence-adjusted growth (20.93 vs 14.84 bp); relationships: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes: REINFORCING (phi 0.506); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: REINFORCING (phi 0.294); KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no: REINFORCING (phi 0.204); failure: CAR wins (incl. OT/SO)
- **Vancouver over 4.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20CARVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT20CARVAN-VAN2|yes has the higher standalone adjusted growth (20.93 vs 14.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.506); they share one thesis budget; relationships: KXNHLSPREAD-26OCT20CARVAN-VAN2|yes: REINFORCING (phi 0.506); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: REINFORCING (phi 0.242); KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no: INTENTIONAL_DIVERSIFIER (phi -0.003); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20CARVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT20CARVAN-VAN2|yes has the higher standalone adjusted growth (20.93 vs 9.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.294); they share one thesis budget; relationships: KXNHLSPREAD-26OCT20CARVAN-VAN2|yes: REINFORCING (phi 0.294); KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes: REINFORCING (phi 0.242); KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no: REINFORCING (phi 0.481); failure: CAR wins by 2+
- **Carolina over 5.5 goals scored NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20CARVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT20CARVAN-VAN2|yes has the higher standalone adjusted growth (20.93 vs 3.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.204); they share one thesis budget; relationships: KXNHLSPREAD-26OCT20CARVAN-VAN2|yes: REINFORCING (phi 0.204); KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes: INTENTIONAL_DIVERSIFIER (phi -0.003); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: REINFORCING (phi 0.481); failure: high-event game (8+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:WINS_BY_2PLUS (p 0.2322): highest fidelity KXNHLSPREAD-26OCT20CARVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-VAN2|yes (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3558): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.4338): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-VAN2|yes — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT20CARVAN-CAR2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no kept
- KXNHLSPREAD-26OCT20CARVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5662, phi -0.628)
- KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes: FUNDED_RESEARCH; family MIXED; loses 45% of the draws where the thesis happens; opposing: failure thesis CAR:WINS (p 0.5662, phi -0.459)
- KXNHLSPREAD-26OCT20CARVAN-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.3 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3374, phi -0.749)
- KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2928, phi -0.501)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT20CARVAN-CAR2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no kept

portfolios: A EV +11.19 (adj +2.10) on $37.68, P(profit) 0.5493, adj growth 15.2 bp · B EV +8.28 (adj +2.84) on $31.50, P(profit) 0.7669, adj growth 24.6 bp · C EV +5.46 (adj +2.27) on $9.86, P(profit) 0.2975, adj growth 19.5 bp · R EV +2.60 (adj +0.93) on $9.00, P(profit) 0.2939, adj growth 30.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT20CARVAN-VAN|yes == KXNHLGAME-26OCT20CARVAN-CAR|no

## TBL @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


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
| Tampa Bay over 1.5 goals scored NO | 18 | 0.237 | 0.203 | +0.047 | +0.013 | $3.11 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | FRAGILE (0.50) | EVIDENCE_MIXED | D |
| Vegas wins by over 1.5 goals YES | 30 | 0.355 | 0.325 | +0.040 | +0.010 | $1.57 | FUNDED_RESEARCH | $1 | VGK:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay over 1.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20TBVGK-VGK2|yes; why: higher confidence-adjusted growth (2.43 vs 1.06 bp); relationships: KXNHLSPREAD-26OCT20TBVGK-VGK2|yes: REINFORCING (phi 0.449); failure: TBL wins (incl. OT/SO)
- **Vegas wins by over 1.5 goals YES** — thesis: VGK wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no has the higher standalone adjusted growth (2.43 vs 1.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.449); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no: REINFORCING (phi 0.449); failure: tight game (one-goal final or OT)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis TBL:SUPPRESSED (p 0.4748): highest fidelity KXNHLSPREAD-26OCT20TBVGK-VGK2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:WINS_BY_2PLUS (p 0.3549): highest fidelity KXNHLSPREAD-26OCT20TBVGK-VGK2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no: FUNDED_RESEARCH; family MIXED; loses 50% of the draws where the thesis happens; opposing: failure thesis TBL:WINS (p 0.4147, phi -0.437)
- KXNHLSPREAD-26OCT20TBVGK-VGK2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:TIGHT (p 0.4319, phi -0.647)

portfolios: A EV +4.06 (adj +1.11) on $21.89, P(profit) 0.4164, adj growth 5.0 bp · B EV +0.96 (adj +0.27) on $4.68, P(profit) 0.4164, adj growth 2.3 bp · C EV +0.88 (adj +0.25) on $3.59, P(profit) 0.2369, adj growth 2.2 bp · R EV +0.37 (adj +0.10) on $2.00, P(profit) 0.4164, adj growth 3.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
