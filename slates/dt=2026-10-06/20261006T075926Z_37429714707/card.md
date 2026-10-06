# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-06T07:59:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +14.36 | +4.68 | +13.31 | 0.631 | -51.25 | -74.19 | 34.04 |
| B thesis-diversified (joint) ← optimiser card | 87.34 | +8.02 | +2.78 | +11.68 | 0.593 | -26.68 | -35.37 | 24.70 |
| C best expression per thesis | 73.59 | +5.95 | +2.07 | +4.29 | 0.669 | -27.13 | -28.05 | 18.72 |
| R FUNDED research stakes | 27.00 | +2.64 | +0.90 | +3.59 | 0.623 | -8.78 | -11.84 | 0.00 |

## NSH @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NSH_win | p_overtime | goals | shots TOR/NSH | TOR/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.52 | 0.48 | 0.00 | 6.03 | 28.8/29.0 | 25.7/25.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.52 | 0.48 | 0.47 | 5.92 | 28.6/28.9 | 25.7/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.53 | 0.47 | 0.00 | 9.32 | 30.1/30.6 | 24.5/23.6 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.086 | 0.45 | 0.55 | 0.00 | 5.98 | 22.9/34.2 | 30.0/19.6 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.45 | 0.55 | 0.46 | 5.97 | 23.1/34.1 | 30.7/19.8 | even strength |
| NSH shot control · high event (8+) · decided (2+) | 0.055 | 0.46 | 0.54 | 0.00 | 9.17 | 24.6/35.9 | 29.1/19.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Toronto wins by over 2.5 goals NO | 76 | 0.818 | 0.786 | +0.045 | +0.014 | $15.32 | FUNDED_RESEARCH | $4 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Toronto wins by over 1.5 goals NO | 65 | 0.712 | 0.679 | +0.046 | +0.013 | $1.52 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Toronto wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR2|no; why: higher confidence-adjusted growth (2.36 vs 1.61 bp); despite a smaller raw edge (+0.045 vs +0.046/contract); relationships: KXNHLSPREAD-26OCT06NSHTOR-TOR2|no: DUPLICATIVE (phi 0.742); failure: TOR wins by 2+
- **Toronto wins by over 1.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT06NSHTOR-TOR3|no has the higher standalone adjusted growth (2.36 vs 1.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.742); they share one thesis budget; relationships: KXNHLSPREAD-26OCT06NSHTOR-TOR3|no: DUPLICATIVE (phi 0.742); failure: TOR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:WINS (p 0.491): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06NSHTOR-TOR3|no (same contract)
- KXNHLSPREAD-26OCT06NSHTOR-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2876, phi -0.742)
- KXNHLSPREAD-26OCT06NSHTOR-TOR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2876, phi -1.0)

portfolios: A EV +2.41 (adj +0.69) on $37.50, P(profit) 0.7124, adj growth 4.8 bp · B EV +1.00 (adj +0.30) on $16.84, P(profit) 0.818, adj growth 2.7 bp · C EV +0.99 (adj +0.30) on $16.85, P(profit) 0.818, adj growth 2.6 bp · R EV +0.30 (adj +0.09) on $5.00, P(profit) 0.818, adj growth 3.1 bp

## CAR @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_CAR_win | p_overtime | goals | shots MTL/CAR | MTL/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.147 | 0.52 | 0.48 | 0.00 | 6.01 | 20.8/33.3 | 29.7/17.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.131 | 0.50 | 0.50 | 0.46 | 5.88 | 20.9/33.4 | 30.0/17.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.105 | 0.46 | 0.54 | 0.00 | 9.18 | 22.4/35.0 | 28.3/16.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.090 | 0.57 | 0.43 | 0.00 | 6.04 | 26.5/27.5 | 24.2/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.53 | 0.47 | 0.47 | 5.93 | 26.2/27.2 | 23.9/23.0 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.073 | 0.49 | 0.51 | 0.00 | 3.46 | 19.5/32.0 | 30.1/17.7 | late empty net |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_OTT_win | p_overtime | goals | shots DET/OTT | DET/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.52 | 0.48 | 0.00 | 5.97 | 27.1/27.3 | 23.9/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.46 | 5.91 | 27.1/27.3 | 24.1/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.51 | 0.49 | 0.00 | 9.24 | 28.6/28.8 | 22.9/22.5 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.077 | 0.43 | 0.57 | 0.00 | 5.95 | 21.1/31.9 | 28.0/18.2 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.45 | 0.55 | 0.47 | 5.88 | 21.6/32.2 | 28.9/18.4 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.062 | 0.55 | 0.45 | 0.00 | 5.95 | 31.6/21.8 | 18.6/27.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_UTA_win | p_overtime | goals | shots NJD/UTA | NJD/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.46 | 0.54 | 0.00 | 5.99 | 27.6/27.4 | 23.6/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.48 | 0.52 | 0.45 | 5.94 | 28.0/27.8 | 24.3/24.8 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.091 | 0.51 | 0.49 | 0.00 | 5.95 | 32.8/22.0 | 18.8/28.9 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.52 | 0.48 | 0.44 | 5.87 | 33.4/22.4 | 19.2/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.44 | 0.56 | 0.00 | 9.22 | 29.5/29.1 | 22.7/23.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.057 | 0.47 | 0.53 | 0.00 | 3.44 | 26.4/26.3 | 24.4/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 2.5 goals NO | 79 | 0.842 | 0.813 | +0.040 | +0.012 | $16.74 | FUNDED_RESEARCH | $5 | UTA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 2.5 goals NO** — thesis: UTA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06UTANJ-NJ2|no; why: higher confidence-adjusted growth (1.92 vs 0.48 bp); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: NJD wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis UTA:WINS (p 0.5222): highest fidelity KXNHLSPREAD-26OCT06UTANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06UTANJ-NJ3|no (same contract)
- KXNHLSPREAD-26OCT06UTANJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2616, phi -0.728)

portfolios: A EV +0.94 (adj +0.28) on $18.75, P(profit) 0.8418, adj growth 2.4 bp · B EV +0.84 (adj +0.25) on $16.74, P(profit) 0.8418, adj growth 2.2 bp · C EV +0.84 (adj +0.25) on $16.74, P(profit) 0.8418, adj growth 2.2 bp · R EV +0.25 (adj +0.07) on $5.00, P(profit) 0.8418, adj growth 2.5 bp

## MIN @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_MIN_win | p_overtime | goals | shots BUF/MIN | BUF/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.49 | 0.51 | 0.00 | 6.06 | 28.6/28.3 | 24.7/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.48 | 0.52 | 0.48 | 5.98 | 28.9/28.6 | 25.3/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.48 | 0.52 | 0.00 | 9.41 | 30.3/30.2 | 23.6/24.0 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.090 | 0.54 | 0.46 | 0.00 | 6.04 | 34.2/22.8 | 19.6/30.2 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.53 | 0.47 | 0.46 | 5.95 | 34.3/23.1 | 19.8/30.9 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.065 | 0.57 | 0.43 | 0.00 | 9.31 | 35.9/24.3 | 19.0/28.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_NYI_win | p_overtime | goals | shots NYR/NYI | NYR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.60 | 0.40 | 0.00 | 6.01 | 26.7/26.9 | 24.0/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.46 | 5.91 | 26.8/27.1 | 23.9/23.5 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.088 | 0.56 | 0.44 | 0.00 | 6.0 | 21.5/32.3 | 29.0/17.7 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.51 | 0.49 | 0.47 | 5.94 | 21.6/32.4 | 28.9/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.63 | 0.37 | 0.00 | 9.24 | 28.6/28.9 | 23.7/21.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.58 | 0.42 | 0.00 | 3.47 | 25.2/25.5 | 23.9/23.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYI shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_STL_win | p_overtime | goals | shots CHI/STL | CHI/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.40 | 0.60 | 0.00 | 6.03 | 26.3/26.7 | 22.7/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.47 | 0.53 | 0.46 | 6.0 | 26.5/26.7 | 23.4/23.1 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.089 | 0.34 | 0.66 | 0.00 | 6.01 | 21.0/31.5 | 27.0/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.42 | 0.58 | 0.00 | 9.29 | 28.0/28.2 | 21.7/22.5 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.42 | 0.58 | 0.46 | 5.92 | 20.9/31.4 | 28.0/17.8 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.056 | 0.30 | 0.70 | 0.00 | 9.22 | 22.5/33.2 | 24.9/18.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_VGK_win | p_overtime | goals | shots SEA/VGK | SEA/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.50 | 0.50 | 0.00 | 6.0 | 26.9/27.2 | 23.5/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.45 | 5.95 | 27.1/27.3 | 23.9/23.7 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.48 | 0.52 | 0.49 | 5.86 | 21.6/32.7 | 29.3/18.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.089 | 0.40 | 0.60 | 0.00 | 5.98 | 21.4/32.5 | 28.3/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.50 | 0.50 | 0.00 | 9.23 | 28.3/28.8 | 22.7/22.4 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.060 | 0.41 | 0.59 | 0.00 | 9.16 | 22.9/34.4 | 27.8/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vegas wins by over 1.5 goals NO | 62 | 0.715 | 0.665 | +0.078 | +0.028 | $16.38 | FUNDED_RESEARCH | $5 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 2.5 goals NO | 75 | 0.822 | 0.783 | +0.059 | +0.020 | $6.01 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Seattle wins by over 1.5 goals YES | 21 | 0.267 | 0.236 | +0.045 | +0.014 | $1.36 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vegas wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no; why: higher confidence-adjusted growth (7.66 vs 5.01 bp); relationships: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: DUPLICATIVE (phi 0.737); KXNHLSPREAD-26OCT06VGKSEA-SEA2|yes: DUPLICATIVE (phi 0.381); failure: VGK wins by 2+
- **Vegas wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no has the higher standalone adjusted growth (7.66 vs 5.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.737); they share one thesis budget; relationships: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: DUPLICATIVE (phi 0.737); KXNHLSPREAD-26OCT06VGKSEA-SEA2|yes: REINFORCING (phi 0.281); failure: VGK wins by 2+
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no has the higher standalone adjusted growth (7.66 vs 2.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.381); they share one thesis budget; relationships: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: DUPLICATIVE (phi 0.381); KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: REINFORCING (phi 0.281); failure: VGK wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.09.
- thesis SEA:WINS (p 0.4912): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.267): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no (same contract)
- thesis VGK:SUPPRESSED (p 0.395): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.2852, phi -1.0)
- KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.2852, phi -0.737)
- KXNHLSPREAD-26OCT06VGKSEA-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS (p 0.5088, phi -0.614)

portfolios: A EV +4.60 (adj +1.54) on $46.88, P(profit) 0.5931, adj growth 11.5 bp · B EV +2.76 (adj +0.98) on $23.76, P(profit) 0.7148, adj growth 8.6 bp · C EV +2.46 (adj +0.89) on $20.00, P(profit) 0.7148, adj growth 7.9 bp · R EV +0.97 (adj +0.34) on $8.00, P(profit) 0.7148, adj growth 11.3 bp

## FLA @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_FLA_win | p_overtime | goals | shots LAK/FLA | LAK/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.64 | 0.36 | 0.00 | 5.95 | 27.2/27.0 | 24.0/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.50 | 0.50 | 0.47 | 5.83 | 27.2/27.2 | 23.9/23.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.088 | 0.67 | 0.33 | 0.00 | 5.94 | 31.8/21.4 | 18.7/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.62 | 0.38 | 0.00 | 9.13 | 28.5/28.5 | 23.3/21.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.54 | 0.46 | 0.47 | 5.82 | 32.4/21.7 | 18.6/29.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.59 | 0.41 | 0.00 | 3.46 | 25.8/25.9 | 24.4/23.6 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 2.5 goals NO | 80 | 0.879 | 0.837 | +0.068 | +0.026 | $19.66 | FUNDED_RESEARCH | $5 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Los Angeles wins by over 1.5 goals YES | 27 | 0.350 | 0.307 | +0.066 | +0.024 | $3.47 | FUNDED_RESEARCH | $1 | LAK:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Los Angeles wins by over 2.5 goals YES | 17 | 0.232 | 0.199 | +0.052 | +0.019 | $1.91 | FUNDED_RESEARCH | $1 | LAK:WINS_BY_2PLUS | DIRECT (0.66) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 71 | 0.786 | 0.746 | +0.062 | +0.021 | $4.96 | FUNDED_RESEARCH | $2 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06FLALA-LA2|yes; why: higher confidence-adjusted growth (9.55 vs 5.96 bp); wins across more scripts (relative breadth 1.011 vs 0.512); relationships: KXNHLSPREAD-26OCT06FLALA-LA2|yes: REINFORCING (phi 0.272); KXNHLSPREAD-26OCT06FLALA-LA3|yes: REINFORCING (phi 0.204); KXNHLSPREAD-26OCT06FLALA-FLA2|no: DUPLICATIVE (phi 0.712); failure: FLA wins by 2+
- **Los Angeles wins by over 1.5 goals YES** — thesis: LAK wins by 2+; alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (9.55 vs 5.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.272); they share one thesis budget; relationships: KXNHLSPREAD-26OCT06FLALA-FLA3|no: REINFORCING (phi 0.272); KXNHLSPREAD-26OCT06FLALA-LA3|yes: DUPLICATIVE (phi 0.749); KXNHLSPREAD-26OCT06FLALA-FLA2|no: DUPLICATIVE (phi 0.382); failure: tight game (one-goal final or OT)
- **Los Angeles wins by over 2.5 goals YES** — thesis: LAK wins by 2+; alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (9.55 vs 5.07 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.204); they share one thesis budget; relationships: KXNHLSPREAD-26OCT06FLALA-FLA3|no: REINFORCING (phi 0.204); KXNHLSPREAD-26OCT06FLALA-LA2|yes: DUPLICATIVE (phi 0.749); KXNHLSPREAD-26OCT06FLALA-FLA2|no: REINFORCING (phi 0.286); failure: tight game (one-goal final or OT)
- **Florida wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (9.55 vs 4.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.712); they share one thesis budget; relationships: KXNHLSPREAD-26OCT06FLALA-FLA3|no: DUPLICATIVE (phi 0.712); KXNHLSPREAD-26OCT06FLALA-LA2|yes: DUPLICATIVE (phi 0.382); KXNHLSPREAD-26OCT06FLALA-LA3|yes: REINFORCING (phi 0.286); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:WINS (p 0.5717): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA3|no (same contract)
- thesis LAK:WINS_BY_2PLUS (p 0.3498): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA3|no (same contract)
- thesis FLA:SUPPRESSED (p 0.491): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA3|no (same contract)
- KXNHLSPREAD-26OCT06FLALA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2137, phi -0.712)
- KXNHLSPREAD-26OCT06FLALA-LA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:TIGHT (p 0.4365, phi -0.646)
- KXNHLSPREAD-26OCT06FLALA-LA3|yes: FUNDED_RESEARCH; family MIXED; loses 34% of the draws where the thesis happens; opposing: failure thesis GAME:TIGHT (p 0.4365, phi -0.484)
- KXNHLSPREAD-26OCT06FLALA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2137, phi -1.0)

portfolios: A EV +6.41 (adj +2.17) on $46.88, P(profit) 0.5349, adj growth 15.4 bp · B EV +3.42 (adj +1.25) on $30.00, P(profit) 0.7863, adj growth 11.3 bp · C EV +1.67 (adj +0.63) on $20.00, P(profit) 0.8788, adj growth 6.0 bp · R EV +1.11 (adj +0.40) on $9.00, P(profit) 0.3498, adj growth 13.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
