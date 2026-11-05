# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T11:46:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +28.42 | +7.46 | +24.83 | 0.622 | -59.61 | -80.29 | 50.28 |
| B thesis-diversified (joint) ← optimiser card | 66.81 | +10.60 | +3.39 | +9.32 | 0.627 | -24.72 | -33.33 | 29.94 |
| C best expression per thesis | 35.41 | +9.40 | +3.17 | +5.98 | 0.640 | -18.42 | -35.41 | 27.55 |
| R FUNDED research stakes | 22.00 | +3.82 | +1.23 | +2.97 | 0.615 | -8.61 | -11.51 | 0.00 |

## UTA @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_UTA_win | p_overtime | goals | shots MTL/UTA | MTL/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.53 | 0.47 | 0.00 | 6.07 | 27.1/27.5 | 24.1/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.54 | 0.46 | 0.00 | 9.43 | 28.9/29.5 | 23.7/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.56 | 0.44 | 0.46 | 5.99 | 27.2/27.6 | 24.4/23.8 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.095 | 0.48 | 0.52 | 0.00 | 6.05 | 21.8/33.2 | 29.4/18.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.49 | 0.51 | 0.48 | 5.96 | 21.8/32.9 | 29.4/18.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.077 | 0.45 | 0.55 | 0.00 | 9.35 | 23.1/34.6 | 27.8/17.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_VGK_win | p_overtime | goals | shots DET/VGK | DET/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.43 | 0.57 | 0.00 | 6.02 | 27.2/27.2 | 23.3/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.48 | 5.93 | 27.0/27.0 | 23.6/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.41 | 0.59 | 0.00 | 9.28 | 28.6/28.5 | 21.8/23.1 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.075 | 0.47 | 0.53 | 0.00 | 6.05 | 32.0/21.6 | 18.1/28.5 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.50 | 0.50 | 0.48 | 5.93 | 32.1/21.8 | 18.4/28.6 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.058 | 0.38 | 0.62 | 0.00 | 5.95 | 21.4/31.5 | 26.9/18.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_CHI_win | p_overtime | goals | shots TBL/CHI | TBL/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.172 | 0.82 | 0.18 | 0.00 | 6.0 | 33.0/20.5 | 18.5/27.5 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.59 | 0.41 | 0.49 | 5.92 | 32.9/20.9 | 17.9/29.3 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.115 | 0.83 | 0.17 | 0.00 | 9.33 | 34.9/22.1 | 18.3/26.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.77 | 0.23 | 0.00 | 6.04 | 27.2/26.3 | 23.9/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.57 | 0.43 | 0.46 | 5.94 | 27.0/26.3 | 23.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.78 | 0.22 | 0.00 | 9.31 | 28.6/27.6 | 23.1/20.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay over 4.5 goals scored NO | 58 | 0.660 | 0.615 | +0.063 | +0.018 | $9.58 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 41 | 0.510 | 0.442 | +0.083 | +0.015 | $2.87 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay over 4.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no; why: higher confidence-adjusted growth (2.98 vs 2.02 bp); relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.515); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no; why: Broad expression KXNHLSPREAD-26NOV05CHITB-TB2|no selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no: REINFORCING (phi 0.515); failure: TBL wins by 2+

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.17, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, TBL shot control · high event (8+) · decided (2+) 0.11.
- thesis TBL:SUPPRESSED (p 0.2575): highest fidelity KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no (same contract)
- thesis GAME:TIGHT (p 0.3795): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no — Broad expression KXNHLSPREAD-26NOV05CHITB-TB2|no selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5419, phi -0.659)
- KXNHLSPREAD-26NOV05CHITB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.5 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4903, phi -1.0)
- override: Broad expression KXNHLSPREAD-26NOV05CHITB-TB2|no selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.62 (adj +0.94) on $31.06, P(profit) 0.6047, adj growth 6.2 bp · B EV +1.57 (adj +0.39) on $12.45, P(profit) 0.6603, adj growth 3.4 bp · C EV +1.25 (adj +0.36) on $11.76, P(profit) 0.6603, adj growth 3.1 bp · R EV +0.51 (adj +0.13) on $4.00, P(profit) 0.6603, adj growth 4.2 bp

## STL @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_STL_win | p_overtime | goals | shots NJD/STL | NJD/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.139 | 0.61 | 0.39 | 0.00 | 6.01 | 33.4/21.3 | 18.3/29.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.58 | 0.42 | 0.00 | 6.01 | 27.6/27.0 | 23.7/23.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.54 | 0.46 | 0.47 | 5.91 | 33.5/21.6 | 18.4/30.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.50 | 0.50 | 0.46 | 5.92 | 27.6/27.0 | 23.8/24.4 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.081 | 0.63 | 0.37 | 0.00 | 9.22 | 35.1/22.8 | 17.9/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.55 | 0.45 | 0.00 | 9.24 | 29.6/28.8 | 23.1/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| St. Louis over 4.5 goals scored YES | 13 | 0.180 | 0.150 | +0.042 | +0.012 | $2.38 | FUNDED_RESEARCH | $1 | STL:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| New Jersey wins by over 1.5 goals NO | 60 | 0.667 | 0.631 | +0.050 | +0.014 | $7.21 | FUNDED_RESEARCH | $2 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **St. Louis over 4.5 goals scored YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05STLNJ-NJ2|no; why: higher confidence-adjusted growth (2.69 vs 1.88 bp); despite a smaller raw edge (+0.042 vs +0.050/contract); relationships: KXNHLSPREAD-26NOV05STLNJ-NJ2|no: REINFORCING (phi 0.301); failure: NJD wins (incl. OT/SO)
- **New Jersey wins by over 1.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes has the higher standalone adjusted growth (2.69 vs 1.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.301); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes: REINFORCING (phi 0.301); failure: NJD wins by 2+

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis STL:OFFENSE_4PLUS (p 0.3375): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV05STLNJ-NJ2|no (same contract)
- thesis STL:WINS (p 0.4517): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05STLNJ-NJ2|no (same contract)
- KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes: FUNDED_RESEARCH; family MIXED; loses 47% of the draws where the thesis happens; opposing: failure thesis NJD:WINS (p 0.5483, phi -0.43)
- KXNHLSPREAD-26NOV05STLNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3329, phi -1.0)

portfolios: A EV +3.34 (adj +0.96) on $20.02, P(profit) 0.6726, adj growth 6.3 bp · B EV +1.32 (adj +0.38) on $9.59, P(profit) 0.6726, adj growth 3.3 bp · C EV +0.92 (adj +0.26) on $2.99, P(profit) 0.1801, adj growth 2.3 bp · R EV +0.47 (adj +0.13) on $3.00, P(profit) 0.6726, adj growth 4.4 bp

## CAR @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CAR_win | p_overtime | goals | shots NYI/CAR | NYI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.116 | 0.43 | 0.57 | 0.00 | 6.0 | 21.3/32.8 | 28.8/18.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.51 | 0.49 | 0.00 | 6.01 | 26.3/26.9 | 23.3/22.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.45 | 0.55 | 0.50 | 5.9 | 21.3/32.9 | 29.6/18.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.49 | 0.51 | 0.48 | 5.94 | 26.6/27.3 | 24.0/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.55 | 0.45 | 0.00 | 9.32 | 28.5/29.1 | 23.1/21.9 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.085 | 0.45 | 0.55 | 0.00 | 9.23 | 22.6/34.4 | 27.7/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York I wins by over 1.5 goals YES | 20 | 0.276 | 0.236 | +0.065 | +0.024 | $1.86 | FUNDED_RESEARCH | $1 | NYI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 1.5 goals NO | 62 | 0.714 | 0.665 | +0.078 | +0.028 | $9.18 | FUNDED_RESEARCH | $3 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I over 1.5 goals scored YES | 75 | 0.820 | 0.780 | +0.057 | +0.017 | $3.36 | FUNDED_RESEARCH | $1 | NYI:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **New York I wins by over 1.5 goals YES** — thesis: NYI wins by 2+; alternative: KXNHLSPREAD-26NOV05CARNYI-CAR2|no; why: higher confidence-adjusted growth (7.77 vs 7.55 bp); despite a smaller raw edge (+0.065 vs +0.078/contract); relationships: KXNHLSPREAD-26NOV05CARNYI-CAR2|no: DUPLICATIVE (phi 0.391); KXNHLTEAMTOTAL-26NOV05CARNYI-NYI2|yes: REINFORCING (phi 0.289); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes has the higher standalone adjusted growth (7.77 vs 7.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.391); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: DUPLICATIVE (phi 0.391); KXNHLTEAMTOTAL-26NOV05CARNYI-NYI2|yes: REINFORCING (phi 0.446); failure: CAR wins by 2+
- **New York I over 1.5 goals scored YES** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes has the higher standalone adjusted growth (7.77 vs 3.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.289); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: REINFORCING (phi 0.289); KXNHLSPREAD-26NOV05CARNYI-CAR2|no: REINFORCING (phi 0.446); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:WINS_BY_2PLUS (p 0.2763): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR2|no (same contract)
- thesis NYI:WINS (p 0.4887): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR2|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3918): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5113, phi -0.632)
- KXNHLSPREAD-26NOV05CARNYI-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2856, phi -1.0)
- KXNHLTEAMTOTAL-26NOV05CARNYI-NYI2|yes: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis NYI:SUPPRESSED (p 0.3925, phi -0.583)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26NOV05CARNYI-CAR3|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV05CARNYI-NYI2|yes kept

portfolios: A EV +6.41 (adj +1.33) on $31.06, P(profit) 0.5689, adj growth 9.3 bp · B EV +1.95 (adj +0.70) on $14.40, P(profit) 0.7144, adj growth 6.5 bp · C EV +2.66 (adj +0.93) on $7.88, P(profit) 0.3423, adj growth 8.1 bp · R EV +0.75 (adj +0.27) on $5.00, P(profit) 0.6632, adj growth 9.7 bp

## PHI @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_PHI_win | p_overtime | goals | shots NYR/PHI | NYR/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 5.98 | 26.1/26.1 | 22.9/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.54 | 0.46 | 0.47 | 5.92 | 26.4/26.3 | 23.0/23.1 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.078 | 0.62 | 0.38 | 0.00 | 6.01 | 30.9/20.8 | 18.0/26.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.58 | 0.42 | 0.00 | 9.16 | 27.8/27.8 | 22.3/21.5 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.55 | 0.45 | 0.45 | 5.86 | 31.2/21.1 | 17.9/27.9 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.065 | 0.46 | 0.54 | 0.00 | 6.0 | 20.9/30.8 | 27.1/17.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYR shot control · normal event (5-7) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_BOS_win | p_overtime | goals | shots PIT/BOS | PIT/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.52 | 0.48 | 0.00 | 6.04 | 27.5/27.2 | 23.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.47 | 0.53 | 0.47 | 6.01 | 27.5/27.2 | 23.8/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.50 | 0.50 | 0.00 | 9.46 | 29.2/28.8 | 22.7/22.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.103 | 0.59 | 0.41 | 0.00 | 6.01 | 33.4/21.7 | 18.6/29.2 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.51 | 0.49 | 0.49 | 5.93 | 32.9/21.9 | 18.6/29.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.085 | 0.58 | 0.42 | 0.00 | 9.38 | 34.9/23.1 | 17.9/27.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_DAL_win | p_overtime | goals | shots CBJ/DAL | CBJ/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.54 | 0.46 | 0.00 | 6.03 | 25.8/25.9 | 22.5/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.49 | 5.92 | 25.8/25.8 | 22.6/22.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.55 | 0.45 | 0.00 | 9.29 | 27.6/27.6 | 21.9/21.3 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.075 | 0.63 | 0.37 | 0.00 | 5.99 | 30.5/20.7 | 17.8/26.2 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.070 | 0.48 | 0.52 | 0.00 | 5.95 | 20.5/30.1 | 26.4/17.2 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.56 | 0.44 | 0.49 | 5.9 | 30.4/20.6 | 17.4/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Columbus over 5.5 goals scored YES | 6 | 0.095 | 0.075 | +0.031 | +0.011 | $2.07 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | FRAGILE (0.34) | EVIDENCE_MIXED | D |
| Columbus wins by over 1.5 goals YES | 25 | 0.306 | 0.273 | +0.043 | +0.010 | $1.33 | FUNDED_RESEARCH | $1 | CBJ:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Columbus over 5.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ5|yes; why: higher confidence-adjusted growth (4.22 vs 1.47 bp); despite a smaller raw edge (+0.031 vs +0.040/contract); alternative not eligible: confidence-adjusted EV +0.0100 below the 0.010/contract floor; relationships: KXNHLSPREAD-26NOV05DALCBJ-CBJ2|yes: REINFORCING (phi 0.374); failure: DAL wins (incl. OT/SO)
- **Columbus wins by over 1.5 goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes has the higher standalone adjusted growth (4.22 vs 1.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.374); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes: REINFORCING (phi 0.374); failure: DAL wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis GAME:HIGH_EVENT (p 0.2477): highest fidelity KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes [FRAGILE], best adjusted EV KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.3064): highest fidelity KXNHLSPREAD-26NOV05DALCBJ-CBJ2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes: FUNDED_RESEARCH; family MIXED; loses 66% of the draws where the thesis happens; opposing: failure thesis DAL:WINS (p 0.4675, phi -0.285)
- KXNHLSPREAD-26NOV05DALCBJ-CBJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.4675, phi -0.623)

portfolios: A EV +3.94 (adj +1.21) on $14.20, P(profit) 0.3215, adj growth 7.0 bp · B EV +1.21 (adj +0.40) on $3.40, P(profit) 0.3215, adj growth 3.5 bp · C EV +1.08 (adj +0.38) on $2.26, P(profit) 0.0946, adj growth 3.3 bp · R EV +0.64 (adj +0.21) on $2.00, P(profit) 0.3215, adj growth 6.0 bp

## VAN @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_VAN_win | p_overtime | goals | shots WPG/VAN | WPG/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.54 | 0.46 | 0.00 | 6.01 | 27.2/26.9 | 23.6/23.4 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.114 | 0.63 | 0.37 | 0.00 | 6.03 | 32.4/21.1 | 18.2/28.2 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.54 | 0.46 | 0.47 | 5.91 | 32.8/21.6 | 18.4/29.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.49 | 0.51 | 0.44 | 5.93 | 27.2/26.8 | 23.5/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.57 | 0.43 | 0.00 | 9.33 | 28.9/28.3 | 22.6/22.5 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.084 | 0.62 | 0.38 | 0.00 | 9.27 | 34.4/22.6 | 17.6/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 17 | 0.248 | 0.206 | +0.068 | +0.027 | $5.81 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Winnipeg wins by over 2.5 goals NO | 71 | 0.791 | 0.745 | +0.066 | +0.021 | $14.61 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26NOV05VANWPG-VAN3|yes; why: higher confidence-adjusted growth (10.33 vs 5.91 bp); relationships: KXNHLSPREAD-26NOV05VANWPG-WPG3|no: REINFORCING (phi 0.295); failure: WPG wins (incl. OT/SO)
- **Winnipeg wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes has the higher standalone adjusted growth (10.33 vs 4.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.295); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes: REINFORCING (phi 0.295); failure: WPG wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.11, WPG shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.2479): highest fidelity KXNHLSPREAD-26NOV05VANWPG-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-VAN2|yes (same contract)
- thesis VAN:WINS (p 0.4566): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:SUPPRESSED (p 0.366): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV05VANWPG-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:WINS (p 0.5434, phi -0.626)
- KXNHLSPREAD-26NOV05VANWPG-WPG3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:WINS_BY_2PLUS (p 0.3234, phi -0.744)

portfolios: A EV +6.64 (adj +2.19) on $31.06, P(profit) 0.6766, adj growth 16.8 bp · B EV +3.54 (adj +1.28) on $20.42, P(profit) 0.2479, adj growth 11.2 bp · C EV +2.62 (adj +1.02) on $6.93, P(profit) 0.2479, adj growth 8.9 bp · R EV +1.12 (adj +0.41) on $6.00, P(profit) 0.2479, adj growth 13.7 bp

## ANA @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_ANA_win | p_overtime | goals | shots EDM/ANA | EDM/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.140 | 0.59 | 0.41 | 0.00 | 9.64 | 29.5/29.4 | 23.7/22.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.60 | 0.40 | 0.00 | 6.1 | 28.0/28.2 | 24.9/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.51 | 0.49 | 0.47 | 6.04 | 28.1/28.2 | 24.8/24.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.073 | 0.67 | 0.33 | 0.00 | 9.59 | 34.8/23.9 | 18.9/26.6 | even strength |
| balanced shots · high event (8+) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.59 | 9.99 | 30.0/30.2 | 23.6/23.2 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.064 | 0.57 | 0.43 | 0.00 | 6.03 | 22.4/32.7 | 29.4/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim over 4.5 goals scored YES | 20 | 0.263 | 0.224 | +0.052 | +0.013 | $3.00 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | DIRECT (0.61) | EVIDENCE_MIXED | D |
| Anaheim over 2.5 goals scored YES | 59 | 0.655 | 0.617 | +0.048 | +0.010 | $3.55 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Anaheim over 4.5 goals scored YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA3|yes; why: higher confidence-adjusted growth (2.12 vs 1.00 bp); relationships: KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA3|yes: DUPLICATIVE (phi 0.434); failure: EDM wins (incl. OT/SO)
- **Anaheim over 2.5 goals scored YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes has the higher standalone adjusted growth (2.12 vs 1.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.434); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes: DUPLICATIVE (phi 0.434); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4305): highest fidelity KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes: FUNDED_RESEARCH; family MIXED; loses 39% of the draws where the thesis happens; opposing: failure thesis EDM:WINS (p 0.5694, phi -0.489)
- KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis ANA:SUPPRESSED (p 0.3533, phi -0.983)

portfolios: A EV +3.47 (adj +0.83) on $22.60, P(profit) 0.2629, adj growth 4.7 bp · B EV +1.01 (adj +0.24) on $6.55, P(profit) 0.2629, adj growth 2.1 bp · C EV +0.88 (adj +0.22) on $3.59, P(profit) 0.2629, adj growth 1.9 bp · R EV +0.32 (adj +0.08) on $2.00, P(profit) 0.2629, adj growth 2.6 bp

## NSH @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NSH_win | p_overtime | goals | shots COL/NSH | COL/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.152 | 0.76 | 0.24 | 0.00 | 6.01 | 34.8/22.2 | 20.0/29.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.117 | 0.79 | 0.21 | 0.00 | 9.31 | 36.8/23.6 | 19.5/27.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.59 | 0.41 | 0.47 | 5.97 | 35.3/22.6 | 19.5/31.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.71 | 0.29 | 0.00 | 6.07 | 29.2/28.4 | 25.7/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.71 | 0.29 | 0.00 | 9.44 | 30.9/30.0 | 25.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.51 | 0.49 | 0.47 | 5.98 | 29.2/28.5 | 25.2/25.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
