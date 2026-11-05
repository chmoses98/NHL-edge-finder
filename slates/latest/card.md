# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T08:40:20Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.34 | +7.60 | +28.02 | 0.571 | -73.23 | -95.63 | 43.46 |
| B thesis-diversified (joint) ← optimiser card | 48.48 | +8.58 | +2.47 | +5.49 | 0.609 | -23.20 | -32.37 | 21.64 |
| C best expression per thesis | 33.41 | +6.64 | +2.10 | +4.68 | 0.531 | -11.47 | -33.41 | 18.29 |
| R FUNDED research stakes | 18.00 | +3.14 | +0.91 | +2.96 | 0.619 | -8.83 | -11.81 | 0.00 |

## UTA @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_UTA_win | p_overtime | goals | shots MTL/UTA | MTL/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.55 | 0.45 | 0.00 | 6.06 | 27.1/27.6 | 24.1/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.52 | 0.48 | 0.00 | 9.38 | 28.8/29.1 | 23.0/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.52 | 0.48 | 0.47 | 6.0 | 27.2/27.7 | 24.6/23.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.096 | 0.50 | 0.50 | 0.00 | 6.01 | 21.6/32.9 | 29.1/18.3 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.47 | 0.53 | 0.48 | 5.99 | 21.6/33.2 | 29.9/18.4 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.078 | 0.45 | 0.55 | 0.00 | 9.4 | 23.3/35.1 | 27.8/17.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_VGK_win | p_overtime | goals | shots DET/VGK | DET/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.42 | 0.58 | 0.00 | 6.01 | 27.1/27.0 | 23.1/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.46 | 5.98 | 27.0/26.9 | 23.6/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.42 | 0.58 | 0.00 | 9.2 | 28.5/28.4 | 21.9/23.0 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.076 | 0.52 | 0.48 | 0.00 | 6.05 | 32.2/21.5 | 18.3/28.1 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.48 | 0.52 | 0.47 | 5.91 | 32.3/21.8 | 18.6/29.0 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.059 | 0.36 | 0.64 | 0.00 | 5.94 | 21.5/31.5 | 27.3/18.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_CHI_win | p_overtime | goals | shots TBL/CHI | TBL/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.163 | 0.79 | 0.21 | 0.00 | 5.99 | 32.8/20.4 | 18.3/27.4 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.58 | 0.42 | 0.46 | 5.92 | 33.2/20.9 | 17.8/29.9 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.115 | 0.81 | 0.19 | 0.00 | 9.24 | 34.5/21.9 | 18.0/25.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.099 | 0.78 | 0.22 | 0.00 | 6.05 | 27.1/26.2 | 23.7/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.53 | 0.47 | 0.48 | 5.92 | 27.4/26.4 | 23.2/23.9 | even strength |
| TBL shot control · low event (<=4) · decided (2+) | 0.071 | 0.73 | 0.27 | 0.00 | 3.45 | 31.4/19.6 | 18.4/28.8 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 1.5 goals NO | 42 | 0.541 | 0.459 | +0.103 | +0.022 | $5.91 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 56 | 0.674 | 0.597 | +0.097 | +0.019 | $3.27 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 4.5 goals scored NO | 59 | 0.673 | 0.624 | +0.066 | +0.017 | $3.08 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 5.5 goals scored NO | 77 | 0.834 | 0.794 | +0.051 | +0.012 | $4.77 | FUNDED_RESEARCH | $2 | CHI:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV05CHITB-TB3|no; why: higher confidence-adjusted growth (4.26 vs 3.38 bp); relationships: KXNHLSPREAD-26NOV05CHITB-TB3|no: DUPLICATIVE (phi 0.754); KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no: REINFORCING (phi 0.512); KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no: DUPLICATIVE (phi 0.399); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CHITB-TB2|no has the higher standalone adjusted growth (4.26 vs 3.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.754); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: DUPLICATIVE (phi 0.754); KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no: REINFORCING (phi 0.547); KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no: REINFORCING (phi 0.464); failure: TBL wins by 2+
- **Tampa Bay over 4.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CHITB-TB2|no has the higher standalone adjusted growth (4.26 vs 2.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.512); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.512); KXNHLSPREAD-26NOV05CHITB-TB3|no: REINFORCING (phi 0.547); KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no: DUPLICATIVE (phi 0.64); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay over 5.5 goals scored NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CHITB-TB2|no has the higher standalone adjusted growth (4.26 vs 1.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.399); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: DUPLICATIVE (phi 0.399); KXNHLSPREAD-26NOV05CHITB-TB3|no: REINFORCING (phi 0.464); KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no: DUPLICATIVE (phi 0.64); failure: high-event game (8+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.16, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, TBL shot control · high event (8+) · decided (2+) 0.12.
- thesis GAME:TIGHT (p 0.4022): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no (same contract)
- thesis TBL:SUPPRESSED (p 0.2684): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.3132): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no (same contract)
- KXNHLSPREAD-26NOV05CHITB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.6 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4594, phi -1.0)
- KXNHLSPREAD-26NOV05CHITB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.9 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4594, phi -0.754)
- KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5277, phi -0.66)
- KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2745, phi -0.579)

portfolios: A EV +7.23 (adj +1.59) on $50.00, P(profit) 0.631, adj growth 10.3 bp · B EV +2.59 (adj +0.56) on $17.03, P(profit) 0.5406, adj growth 5.0 bp · C EV +2.27 (adj +0.48) on $9.59, P(profit) 0.5406, adj growth 4.2 bp · R EV +0.88 (adj +0.19) on $6.00, P(profit) 0.5406, adj growth 6.4 bp

## STL @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_STL_win | p_overtime | goals | shots NJD/STL | NJD/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.126 | 0.64 | 0.36 | 0.00 | 6.0 | 33.7/21.4 | 18.5/29.4 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.57 | 0.43 | 0.50 | 5.88 | 33.4/21.5 | 18.5/29.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.55 | 0.45 | 0.00 | 6.02 | 27.6/27.0 | 23.7/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.46 | 5.96 | 28.0/27.4 | 24.1/24.7 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.083 | 0.64 | 0.36 | 0.00 | 9.24 | 35.4/23.0 | 18.0/27.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.57 | 0.43 | 0.00 | 9.33 | 29.0/28.5 | 22.8/22.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CAR_win | p_overtime | goals | shots NYI/CAR | NYI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.118 | 0.43 | 0.57 | 0.00 | 5.99 | 21.0/32.7 | 28.8/17.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.49 | 0.51 | 0.00 | 6.0 | 26.7/27.3 | 23.7/23.2 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.46 | 5.94 | 21.2/32.9 | 29.6/17.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.53 | 0.47 | 0.49 | 5.95 | 26.6/27.3 | 24.0/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.49 | 0.51 | 0.00 | 9.26 | 28.3/29.0 | 22.9/22.4 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.081 | 0.43 | 0.57 | 0.00 | 9.28 | 22.7/34.3 | 27.4/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 62 | 0.704 | 0.660 | +0.068 | +0.023 | $12.07 | FUNDED_RESEARCH | $4 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I over 4.5 goals scored YES | 15 | 0.215 | 0.175 | +0.056 | +0.016 | $2.41 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| New York I wins by over 1.5 goals YES | 21 | 0.275 | 0.237 | +0.053 | +0.016 | $1.02 | FUNDED_RESEARCH | $1 | NYI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 75 | 0.817 | 0.779 | +0.054 | +0.015 | $2.43 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes; why: higher confidence-adjusted growth (5.09 vs 4.16 bp); wins across more scripts (relative breadth 0.953 vs 0.563); relationships: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes: REINFORCING (phi 0.303); KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: DUPLICATIVE (phi 0.399); KXNHLSPREAD-26NOV05CARNYI-CAR3|no: DUPLICATIVE (phi 0.73); failure: CAR wins by 2+
- **New York I over 4.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CARNYI-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CARNYI-CAR2|no has the higher standalone adjusted growth (5.09 vs 4.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.303); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CARNYI-CAR2|no: REINFORCING (phi 0.303); KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: REINFORCING (phi 0.49); KXNHLSPREAD-26NOV05CARNYI-CAR3|no: REINFORCING (phi 0.234); failure: CAR wins (incl. OT/SO)
- **New York I wins by over 1.5 goals YES** — thesis: NYI wins by 2+; alternative: KXNHLSPREAD-26NOV05CARNYI-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CARNYI-CAR2|no has the higher standalone adjusted growth (5.09 vs 3.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.399); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CARNYI-CAR2|no: DUPLICATIVE (phi 0.399); KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes: REINFORCING (phi 0.49); KXNHLSPREAD-26NOV05CARNYI-CAR3|no: REINFORCING (phi 0.291); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 2.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV05CARNYI-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CARNYI-CAR2|no has the higher standalone adjusted growth (5.09 vs 2.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.730); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CARNYI-CAR2|no: DUPLICATIVE (phi 0.73); KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes: REINFORCING (phi 0.234); KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: REINFORCING (phi 0.291); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:WINS (p 0.4951): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR2|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3921): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS_BY_2PLUS (p 0.2745): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR2|no (same contract)
- KXNHLSPREAD-26NOV05CARNYI-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2957, phi -1.0)
- KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes: FUNDED_RESEARCH; family MIXED; loses 45% of the draws where the thesis happens; opposing: failure thesis CAR:WINS (p 0.5049, phi -0.43)
- KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5049, phi -0.621)
- KXNHLSPREAD-26NOV05CARNYI-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2957, phi -0.73)

portfolios: A EV +9.14 (adj +2.72) on $50.00, P(profit) 0.3405, adj growth 13.5 bp · B EV +2.55 (adj +0.80) on $17.94, P(profit) 0.7088, adj growth 7.0 bp · C EV +1.81 (adj +0.62) on $16.97, P(profit) 0.7043, adj growth 5.4 bp · R EV +1.09 (adj +0.34) on $7.00, P(profit) 0.7088, adj growth 10.6 bp

## PHI @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_PHI_win | p_overtime | goals | shots NYR/PHI | NYR/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.56 | 0.44 | 0.00 | 5.99 | 26.2/26.2 | 23.0/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.53 | 0.47 | 0.46 | 5.84 | 26.3/26.4 | 23.3/22.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.58 | 0.42 | 0.00 | 9.19 | 27.7/27.6 | 22.3/21.4 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.079 | 0.62 | 0.38 | 0.00 | 5.96 | 30.7/20.7 | 17.9/26.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.52 | 0.48 | 0.00 | 3.42 | 25.0/24.8 | 23.1/23.2 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.56 | 0.44 | 0.45 | 5.78 | 30.8/20.9 | 17.8/27.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_BOS_win | p_overtime | goals | shots PIT/BOS | PIT/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.51 | 0.49 | 0.00 | 6.05 | 27.7/27.0 | 23.6/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.50 | 0.50 | 0.00 | 9.43 | 29.2/28.8 | 22.6/23.1 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.103 | 0.57 | 0.42 | 0.00 | 6.0 | 33.1/21.7 | 18.7/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.52 | 0.48 | 0.48 | 5.99 | 27.9/27.4 | 24.1/24.6 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.46 | 0.46 | 5.92 | 32.8/21.7 | 18.5/29.4 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.084 | 0.62 | 0.38 | 0.00 | 9.4 | 34.8/23.3 | 18.2/27.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.10, PIT shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_DAL_win | p_overtime | goals | shots CBJ/DAL | CBJ/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.56 | 0.44 | 0.00 | 6.02 | 25.7/25.6 | 22.3/21.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.95 | 26.0/26.0 | 22.7/22.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.56 | 0.44 | 0.00 | 9.25 | 27.2/27.3 | 21.7/20.7 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.072 | 0.60 | 0.40 | 0.00 | 5.98 | 30.7/20.5 | 17.5/26.4 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.57 | 0.43 | 0.49 | 5.92 | 30.5/20.6 | 17.5/27.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.066 | 0.45 | 0.55 | 0.00 | 5.97 | 20.5/30.7 | 26.8/17.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_VAN_win | p_overtime | goals | shots WPG/VAN | WPG/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.54 | 0.46 | 0.00 | 6.02 | 27.4/26.8 | 23.5/23.6 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.114 | 0.63 | 0.37 | 0.00 | 6.03 | 32.7/21.2 | 18.4/28.4 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.47 | 5.93 | 32.8/21.5 | 18.3/29.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.51 | 0.49 | 0.48 | 5.88 | 27.6/27.0 | 23.6/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.52 | 0.48 | 0.00 | 9.29 | 28.7/28.1 | 22.1/22.5 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.079 | 0.64 | 0.36 | 0.00 | 9.26 | 34.3/22.6 | 17.7/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 17 | 0.247 | 0.206 | +0.067 | +0.026 | $5.86 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Winnipeg wins by over 1.5 goals NO | 56 | 0.678 | 0.598 | +0.101 | +0.021 | $6.62 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Winnipeg over 4.5 goals scored NO | 69 | 0.760 | 0.718 | +0.055 | +0.013 | $1.03 | FUNDED_RESEARCH | $1 | VAN:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26NOV05VANWPG-VAN3|yes; why: higher confidence-adjusted growth (10.06 vs 4.97 bp); relationships: KXNHLSPREAD-26NOV05VANWPG-WPG2|no: DUPLICATIVE (phi 0.395); KXNHLTEAMTOTAL-26NOV05VANWPG-WPG5|no: REINFORCING (phi 0.296); failure: WPG wins (incl. OT/SO)
- **Winnipeg wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes has the higher standalone adjusted growth (10.06 vs 3.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.395); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes: DUPLICATIVE (phi 0.395); KXNHLTEAMTOTAL-26NOV05VANWPG-WPG5|no: REINFORCING (phi 0.497); failure: WPG wins by 2+
- **Winnipeg over 4.5 goals scored NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes has the higher standalone adjusted growth (10.06 vs 1.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.296); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes: REINFORCING (phi 0.296); KXNHLSPREAD-26NOV05VANWPG-WPG2|no: REINFORCING (phi 0.497); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, WPG shot control · normal event (5-7) · decided (2+) 0.11, WPG shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.2472): highest fidelity KXNHLSPREAD-26NOV05VANWPG-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-VAN2|yes (same contract)
- thesis VAN:WINS (p 0.4565): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-VAN2|yes — override declined: the joint re-optimisation gives KXNHLSPREAD-26NOV05VANWPG-WPG3|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV05VANWPG-WPG5|no kept
- thesis VAN:OFFENSE_4PLUS (p 0.3569): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV05VANWPG-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:WINS (p 0.5435, phi -0.625)
- KXNHLSPREAD-26NOV05VANWPG-WPG2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.3 pts; opposing: failure thesis WPG:WINS_BY_2PLUS (p 0.322, phi -1.0)
- KXNHLTEAMTOTAL-26NOV05VANWPG-WPG5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4235, phi -0.656)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26NOV05VANWPG-WPG3|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV05VANWPG-WPG5|no kept

portfolios: A EV +10.97 (adj +3.29) on $50.00, P(profit) 0.678, adj growth 19.7 bp · B EV +3.43 (adj +1.11) on $13.51, P(profit) 0.2472, adj growth 9.7 bp · C EV +2.56 (adj +1.00) on $6.85, P(profit) 0.2472, adj growth 8.7 bp · R EV +1.18 (adj +0.38) on $5.00, P(profit) 0.2472, adj growth 12.5 bp

## ANA @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_ANA_win | p_overtime | goals | shots EDM/ANA | EDM/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.142 | 0.61 | 0.39 | 0.00 | 9.63 | 29.8/29.8 | 24.0/22.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.61 | 0.39 | 0.00 | 6.08 | 27.9/27.8 | 24.6/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.50 | 0.50 | 0.45 | 6.08 | 28.0/28.3 | 24.8/24.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 9.73 | 34.8/24.0 | 18.8/26.6 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.067 | 0.66 | 0.34 | 0.00 | 6.09 | 32.9/22.3 | 19.5/28.2 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.065 | 0.50 | 0.50 | 0.00 | 9.59 | 24.0/34.6 | 27.8/18.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NSH_win | p_overtime | goals | shots COL/NSH | COL/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.148 | 0.74 | 0.26 | 0.00 | 6.03 | 35.2/22.3 | 19.9/30.3 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.116 | 0.75 | 0.25 | 0.00 | 9.39 | 37.0/23.8 | 19.5/28.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.72 | 0.28 | 0.00 | 6.03 | 28.8/28.1 | 25.5/24.2 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.59 | 0.41 | 0.47 | 5.94 | 35.3/22.6 | 19.4/31.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.73 | 0.27 | 0.00 | 9.46 | 31.0/29.9 | 25.2/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.55 | 0.45 | 0.44 | 5.98 | 29.2/28.5 | 25.3/25.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
