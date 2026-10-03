# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T04:49:06Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +25.82 | +7.06 | +26.32 | 0.588 | -70.18 | -99.01 | 40.25 |
| B thesis-diversified (joint) ← optimiser card | 37.78 | +6.70 | +2.50 | +6.78 | 0.595 | -18.73 | -27.33 | 22.48 |
| C best expression per thesis | 49.61 | +9.16 | +3.43 | +2.27 | 0.565 | -24.89 | -33.66 | 29.76 |
| R FUNDED research stakes | 13.00 | +2.38 | +0.89 | +2.53 | 0.589 | -6.43 | -8.89 | 0.00 |

## CHI @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_CHI_win | p_overtime | goals | shots BUF/CHI | BUF/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.135 | 0.74 | 0.26 | 0.00 | 6.02 | 33.5/21.3 | 18.9/28.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.66 | 0.34 | 0.00 | 6.02 | 28.0/27.4 | 24.6/23.7 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.57 | 0.43 | 0.46 | 5.88 | 33.5/21.7 | 18.6/30.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.58 | 0.42 | 0.46 | 5.95 | 27.9/27.3 | 24.1/24.6 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.094 | 0.73 | 0.27 | 0.00 | 9.3 | 35.0/22.7 | 18.2/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.68 | 0.32 | 0.00 | 9.26 | 29.5/28.7 | 23.6/22.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_OTT_win | p_overtime | goals | shots TOR/OTT | TOR/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.135 | 0.40 | 0.60 | 0.00 | 5.99 | 21.7/34.2 | 30.0/18.7 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.46 | 0.54 | 0.46 | 5.83 | 21.9/34.4 | 31.2/18.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.53 | 0.47 | 0.00 | 6.02 | 27.5/28.2 | 24.8/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.51 | 0.49 | 0.46 | 5.85 | 27.5/28.3 | 25.1/24.2 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.083 | 0.39 | 0.61 | 0.00 | 9.15 | 23.2/35.5 | 28.7/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.46 | 0.54 | 0.00 | 9.18 | 29.2/29.9 | 23.8/23.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.14, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WSH_win | p_overtime | goals | shots TBL/WSH | TBL/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.62 | 0.38 | 0.00 | 6.01 | 26.9/26.5 | 23.4/22.9 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.114 | 0.68 | 0.32 | 0.00 | 6.02 | 32.5/21.2 | 18.5/28.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.54 | 0.46 | 0.45 | 5.94 | 27.0/26.6 | 23.3/23.6 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.55 | 0.45 | 0.48 | 5.89 | 32.5/21.5 | 18.3/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.64 | 0.36 | 0.00 | 9.24 | 28.7/28.1 | 23.1/21.7 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.068 | 0.68 | 0.32 | 0.00 | 9.29 | 34.0/22.6 | 18.0/26.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.125 | 0.45 | 0.55 | 0.00 | 5.97 | 20.5/32.0 | 28.2/17.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.48 | 0.52 | 0.49 | 5.92 | 20.6/32.1 | 28.5/17.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.54 | 0.46 | 0.00 | 5.97 | 25.6/26.4 | 23.1/21.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.51 | 0.49 | 0.48 | 5.89 | 25.9/26.6 | 23.4/22.7 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.076 | 0.46 | 0.54 | 0.00 | 3.47 | 19.4/30.9 | 28.8/17.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.071 | 0.41 | 0.59 | 0.00 | 9.09 | 21.9/33.9 | 27.2/16.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MTL @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_MTL_win | p_overtime | goals | shots PIT/MTL | PIT/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| PIT shot control · normal event (5-7) · decided (2+) | 0.128 | 0.64 | 0.36 | 0.00 | 6.04 | 32.8/21.0 | 18.2/28.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.59 | 0.41 | 0.00 | 6.07 | 27.3/26.7 | 23.4/23.3 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.101 | 0.67 | 0.33 | 0.00 | 9.36 | 34.5/22.6 | 17.8/26.9 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.56 | 0.44 | 0.48 | 5.92 | 32.7/21.3 | 18.3/29.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.51 | 0.49 | 0.49 | 5.94 | 27.4/26.8 | 23.5/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.56 | 0.44 | 0.00 | 9.36 | 28.9/28.4 | 22.5/22.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Montreal wins NO | 47 | 0.564 | 0.514 | +0.076 | +0.027 | $8.01 | FUNDED_RESEARCH | $3 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pittsburgh wins by over 1.5 goals YES | 27 | 0.348 | 0.307 | +0.064 | +0.023 | $3.56 | FUNDED_RESEARCH | $1 | PIT:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Montreal wins by over 2.5 goals NO | 80 | 0.854 | 0.824 | +0.042 | +0.013 | $7.36 | FUNDED_RESEARCH | $2 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Montreal wins NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03MTLPIT-PIT|yes; why: best adjusted growth among the thesis's expressions; relationships: KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes: DUPLICATIVE (phi 0.643); KXNHLSPREAD-26OCT03MTLPIT-MTL3|no: DUPLICATIVE (phi 0.471); failure: MTL wins (incl. OT/SO)
- **Pittsburgh wins by over 1.5 goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGAME-26OCT03MTLPIT-MTL|no; why: Broad expression KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes selected over broad KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.67 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGAME-26OCT03MTLPIT-MTL|no: DUPLICATIVE (phi 0.643); KXNHLSPREAD-26OCT03MTLPIT-MTL3|no: DUPLICATIVE (phi 0.303); failure: MTL wins (incl. OT/SO)
- **Montreal wins by over 2.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03MTLPIT-MTL|no; why: second expression of the same thesis: KXNHLGAME-26OCT03MTLPIT-MTL|no has the higher standalone adjusted growth (6.39 vs 2.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.471); they share one thesis budget; relationships: KXNHLGAME-26OCT03MTLPIT-MTL|no: DUPLICATIVE (phi 0.471); KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes: DUPLICATIVE (phi 0.303); failure: MTL wins by 2+

**Review**: scripts PIT shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, PIT shot control · high event (8+) · decided (2+) 0.10.
- thesis PIT:WINS (p 0.5639): highest fidelity KXNHLGAME-26OCT03MTLPIT-PIT|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03MTLPIT-PIT|yes (same contract)
- thesis PIT:WINS_BY_2PLUS (p 0.3482): highest fidelity KXNHLGAME-26OCT03MTLPIT-PIT|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03MTLPIT-PIT|yes (same contract)
- KXNHLGAME-26OCT03MTLPIT-MTL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS (p 0.4361, phi -1.0)
- KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS (p 0.4361, phi -0.643)
- KXNHLSPREAD-26OCT03MTLPIT-MTL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.2383, phi -0.74)
- override: Broad expression KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes selected over broad KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.67 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +7.74 (adj +2.70) on $50.00, P(profit) 0.5639, adj growth 15.9 bp · B EV +2.45 (adj +0.85) on $18.93, P(profit) 0.5639, adj growth 7.4 bp · C EV +2.08 (adj +0.73) on $13.24, P(profit) 0.5639, adj growth 6.4 bp · R EV +0.80 (adj +0.28) on $6.00, P(profit) 0.5639, adj growth 9.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03MTLPIT-PIT|yes == KXNHLGAME-26OCT03MTLPIT-MTL|no

## UTA @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_UTA_win | p_overtime | goals | shots CBJ/UTA | CBJ/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.55 | 0.45 | 0.00 | 5.99 | 27.4/27.2 | 24.0/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.49 | 5.9 | 27.5/27.3 | 24.2/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.55 | 0.45 | 0.00 | 9.37 | 29.1/28.8 | 22.8/22.6 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.080 | 0.61 | 0.39 | 0.00 | 5.99 | 32.5/22.0 | 19.2/28.2 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.55 | 0.45 | 0.45 | 5.88 | 32.4/22.0 | 18.7/29.0 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.055 | 0.51 | 0.49 | 0.00 | 6.0 | 22.0/32.0 | 28.2/18.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_SEA_win | p_overtime | goals | shots EDM/SEA | EDM/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.126 | 0.73 | 0.27 | 0.00 | 6.0 | 33.8/21.8 | 19.3/29.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.67 | 0.33 | 0.00 | 6.08 | 28.3/27.8 | 24.9/24.0 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.58 | 0.42 | 0.49 | 5.93 | 33.9/22.1 | 19.0/30.4 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.099 | 0.71 | 0.29 | 0.00 | 9.32 | 36.0/23.5 | 18.9/27.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.54 | 0.46 | 0.50 | 5.93 | 28.3/27.7 | 24.3/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.64 | 0.36 | 0.00 | 9.4 | 29.9/29.2 | 23.9/22.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, EDM shot control · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_NJD_win | p_overtime | goals | shots NYI/NJD | NYI/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.56 | 0.44 | 0.00 | 5.96 | 27.9/27.9 | 24.7/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.51 | 0.49 | 0.44 | 5.91 | 28.0/28.0 | 24.7/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.55 | 0.45 | 0.00 | 9.14 | 29.4/29.4 | 23.9/23.1 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.48 | 0.52 | 0.45 | 5.83 | 22.4/32.8 | 29.5/19.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.53 | 0.47 | 0.49 | 2.77 | 26.8/26.9 | 25.5/25.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.066 | 0.52 | 0.48 | 0.00 | 5.95 | 22.3/32.9 | 29.4/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 1.5 goals NO | 68 | 0.754 | 0.715 | +0.059 | +0.019 | $5.97 | FUNDED_RESEARCH | $2 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 2.5 goals NO | 80 | 0.853 | 0.824 | +0.042 | +0.013 | $1.33 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03NJNYI-NYI|yes; why: higher confidence-adjusted growth (3.85 vs 2.58 bp); relationships: KXNHLSPREAD-26OCT03NJNYI-NJ3|no: DUPLICATIVE (phi 0.727); failure: NJD wins by 2+
- **New Jersey wins by over 2.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT03NJNYI-NJ2|no has the higher standalone adjusted growth (3.85 vs 2.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.727); they share one thesis budget; relationships: KXNHLSPREAD-26OCT03NJNYI-NJ2|no: DUPLICATIVE (phi 0.727); failure: NJD wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.07.
- thesis NYI:WINS (p 0.5341): highest fidelity KXNHLSPREAD-26OCT03NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03NJNYI-NJ2|no (same contract)
- thesis NJD:SUPPRESSED (p 0.4655): highest fidelity KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT03NJNYI-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.246, phi -1.0)
- KXNHLSPREAD-26OCT03NJNYI-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.246, phi -0.727)

portfolios: A EV +4.92 (adj +1.46) on $50.00, P(profit) 0.6651, adj growth 8.7 bp · B EV +0.57 (adj +0.19) on $7.30, P(profit) 0.754, adj growth 1.8 bp · C EV +1.45 (adj +0.48) on $17.18, P(profit) 0.754, adj growth 4.2 bp · R EV +0.22 (adj +0.07) on $3.00, P(profit) 0.754, adj growth 2.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03NJNYI-NJ|no == KXNHLGAME-26OCT03NJNYI-NYI|yes

## DAL @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_DAL_win | p_overtime | goals | shots NSH/DAL | NSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.49 | 0.51 | 0.00 | 5.95 | 27.0/27.3 | 23.7/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.47 | 5.94 | 26.8/26.9 | 23.5/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.48 | 0.52 | 0.00 | 9.25 | 28.6/28.8 | 22.6/22.7 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.078 | 0.42 | 0.58 | 0.00 | 5.99 | 21.3/32.0 | 28.0/18.2 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.49 | 0.51 | 0.47 | 5.92 | 21.8/32.5 | 29.2/18.6 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.061 | 0.61 | 0.39 | 0.00 | 6.06 | 31.6/21.6 | 18.6/27.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ MIN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_BOS_win | p_overtime | goals | shots MIN/BOS | MIN/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.60 | 0.40 | 0.00 | 6.02 | 28.6/28.3 | 25.2/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.52 | 0.48 | 0.48 | 5.96 | 28.7/28.6 | 25.2/25.4 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.105 | 0.69 | 0.31 | 0.00 | 6.01 | 34.1/22.7 | 20.1/29.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.63 | 0.37 | 0.00 | 9.39 | 30.7/30.2 | 24.9/23.7 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.55 | 0.45 | 0.46 | 5.91 | 34.6/23.2 | 20.0/31.1 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.073 | 0.72 | 0.28 | 0.00 | 9.31 | 35.9/23.9 | 19.2/27.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 10 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_STL_win | p_overtime | goals | shots COL/STL | COL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.142 | 0.68 | 0.32 | 0.00 | 6.01 | 33.9/21.5 | 18.9/29.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.125 | 0.55 | 0.45 | 0.47 | 5.95 | 34.0/21.7 | 18.5/30.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.110 | 0.72 | 0.28 | 0.00 | 9.29 | 36.0/23.0 | 18.5/27.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.097 | 0.62 | 0.38 | 0.00 | 5.98 | 28.3/27.3 | 24.3/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.51 | 0.49 | 0.45 | 5.91 | 28.0/27.2 | 24.0/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.63 | 0.37 | 0.00 | 9.45 | 29.6/28.7 | 23.1/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| St. Louis over 4.5 goals scored YES | 10 | 0.172 | 0.134 | +0.066 | +0.027 | $2.78 | FUNDED_RESEARCH | $1 | STL:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
| St. Louis wins by over 1.5 goals YES | 12 | 0.198 | 0.156 | +0.070 | +0.029 | $2.47 | FUNDED_RESEARCH | $1 | STL:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| St. Louis over 1.5 goals scored YES | 70 | 0.783 | 0.736 | +0.068 | +0.022 | $6.31 | FUNDED_RESEARCH | $2 | STL:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **St. Louis over 4.5 goals scored YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03STLCOL-STL2|yes; why: higher confidence-adjusted growth (16.60 vs 16.19 bp); despite a smaller raw edge (+0.066 vs +0.070/contract); relationships: KXNHLSPREAD-26OCT03STLCOL-STL2|yes: REINFORCING (phi 0.475); KXNHLTEAMTOTAL-26OCT03STLCOL-STL2|yes: REINFORCING (phi 0.24); failure: COL wins (incl. OT/SO)
- **St. Louis wins by over 1.5 goals YES** — thesis: STL wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT03STLCOL-STL5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT03STLCOL-STL5|yes has the higher standalone adjusted growth (16.60 vs 16.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.475); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT03STLCOL-STL5|yes: REINFORCING (phi 0.475); KXNHLTEAMTOTAL-26OCT03STLCOL-STL2|yes: REINFORCING (phi 0.262); failure: COL wins (incl. OT/SO)
- **St. Louis over 1.5 goals scored YES** — thesis: STL wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT03STLCOL-STL5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT03STLCOL-STL5|yes has the higher standalone adjusted growth (16.60 vs 5.03 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.240); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT03STLCOL-STL5|yes: REINFORCING (phi 0.24); KXNHLSPREAD-26OCT03STLCOL-STL2|yes: REINFORCING (phi 0.262); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis STL:OFFENSE_4PLUS (p 0.3335): highest fidelity KXNHLTEAMTOTAL-26OCT03STLCOL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03STLCOL-STL2|yes — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT03STLCOL-STL3|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT03STLCOL-STL5|yes kept
- thesis STL:WINS_BY_2PLUS (p 0.1978): highest fidelity KXNHLSPREAD-26OCT03STLCOL-STL2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03STLCOL-STL2|yes (same contract)
- thesis STL:WINS (p 0.3959): highest fidelity KXNHLGAME-26OCT03STLCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03STLCOL-STL2|yes — override declined: the joint re-optimisation gives KXNHLGAME-26OCT03STLCOL-COL|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT03STLCOL-STL2|yes kept
- KXNHLTEAMTOTAL-26OCT03STLCOL-STL5|yes: FUNDED_RESEARCH; family MIXED; loses 48% of the draws where the thesis happens; opposing: failure thesis COL:WINS (p 0.6041, phi -0.441)
- KXNHLSPREAD-26OCT03STLCOL-STL2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.6041, phi -0.613)
- KXNHLTEAMTOTAL-26OCT03STLCOL-STL2|yes: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.59)
- override: override declined: the joint re-optimisation gives KXNHLGAME-26OCT03STLCOL-COL|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT03STLCOL-STL2|yes kept
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT03STLCOL-STL3|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT03STLCOL-STL5|yes kept

portfolios: A EV +13.16 (adj +2.90) on $50.00, P(profit) 0.5107, adj growth 15.6 bp · B EV +3.68 (adj +1.46) on $11.55, P(profit) 0.2644, adj growth 13.3 bp · C EV +5.63 (adj +2.22) on $19.19, P(profit) 0.2644, adj growth 19.1 bp · R EV +1.36 (adj +0.54) on $4.00, P(profit) 0.2644, adj growth 18.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03STLCOL-STL|yes == KXNHLGAME-26OCT03STLCOL-COL|no

## CGY @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CGY_win | p_overtime | goals | shots VAN/CGY | VAN/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.61 | 0.39 | 0.00 | 6.04 | 28.1/28.1 | 24.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.48 | 5.95 | 28.3/28.2 | 25.0/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.62 | 0.38 | 0.00 | 9.33 | 30.1/30.1 | 24.6/23.2 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.066 | 0.65 | 0.35 | 0.00 | 6.04 | 33.0/22.6 | 19.8/28.8 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.065 | 0.55 | 0.45 | 0.00 | 6.07 | 22.5/33.0 | 29.6/18.8 | even strength |
| VAN shot control · normal event (5-7) · tight (1-goal/OT) | 0.057 | 0.58 | 0.42 | 0.49 | 5.9 | 33.1/22.3 | 19.1/29.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## LAK @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_LAK_win | p_overtime | goals | shots SJS/LAK | SJS/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.55 | 0.45 | 0.00 | 5.99 | 27.3/27.4 | 24.1/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.50 | 0.50 | 0.45 | 5.88 | 27.2/27.4 | 24.1/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.55 | 0.45 | 0.00 | 9.3 | 29.2/29.4 | 23.7/22.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.47 | 0.53 | 0.44 | 5.82 | 21.9/32.5 | 29.1/18.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.072 | 0.47 | 0.53 | 0.00 | 6.0 | 22.1/32.9 | 29.1/18.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.53 | 0.47 | 0.00 | 3.45 | 26.0/26.3 | 24.6/23.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
