# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T10:27:30Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +34.13 | +8.98 | +28.25 | 0.649 | -67.04 | -88.30 | 59.33 |
| B thesis-diversified (joint) ← optimiser card | 81.21 | +14.30 | +4.31 | +13.30 | 0.656 | -27.61 | -37.76 | 37.84 |
| C best expression per thesis | 44.69 | +10.51 | +3.27 | +3.52 | 0.662 | -25.26 | -28.87 | 28.40 |
| R FUNDED research stakes | 26.00 | +5.03 | +1.51 | +4.50 | 0.656 | -9.43 | -13.62 | 0.00 |

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

## CHI @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 3 on card


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
| Tampa Bay wins by over 2.5 goals NO | 54 | 0.674 | 0.584 | +0.117 | +0.026 | $11.01 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 41 | 0.541 | 0.453 | +0.114 | +0.025 | $4.07 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Chicago over 3.5 goals scored YES | 21 | 0.268 | 0.234 | +0.047 | +0.013 | $1.04 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: higher confidence-adjusted growth (6.12 vs 5.82 bp); wins across more scripts (relative breadth 1.022 vs 0.827); relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: DUPLICATIVE (phi 0.754); KXNHLTEAMTOTAL-26NOV05CHITB-CHI4|yes: REINFORCING (phi 0.332); failure: TBL wins by 2+
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV05CHITB-TB3|no; why: Broad expression KXNHLSPREAD-26NOV05CHITB-TB2|no selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no because adjusted EV is 0.9 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV05CHITB-TB3|no: DUPLICATIVE (phi 0.754); KXNHLTEAMTOTAL-26NOV05CHITB-CHI4|yes: REINFORCING (phi 0.406); failure: TBL wins by 2+
- **Chicago over 3.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB3|no; why: Broad expression KXNHLTEAMTOTAL-26NOV05CHITB-CHI4|yes selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-CHI5|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.46 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV05CHITB-TB3|no: REINFORCING (phi 0.332); KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.406); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.16, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, TBL shot control · high event (8+) · decided (2+) 0.12.
- thesis GAME:TIGHT (p 0.4022): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB3|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.2601): highest fidelity KXNHLTEAMTOTAL-26NOV05CHITB-CHI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB3|no — Broad expression KXNHLTEAMTOTAL-26NOV05CHITB-CHI4|yes selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-CHI5|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.46 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CHI:WINS (p 0.3132): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB3|no (same contract)
- KXNHLSPREAD-26NOV05CHITB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.9 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4594, phi -0.754)
- KXNHLSPREAD-26NOV05CHITB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.6 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4594, phi -1.0)
- KXNHLTEAMTOTAL-26NOV05CHITB-CHI4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CHI:SUPPRESSED (p 0.5354, phi -0.65)
- override: Broad expression KXNHLSPREAD-26NOV05CHITB-TB2|no selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no because adjusted EV is 0.9 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLTEAMTOTAL-26NOV05CHITB-CHI4|yes selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-CHI5|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.46 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.81 (adj +1.70) on $33.13, P(profit) 0.5406, adj growth 9.4 bp · B EV +3.60 (adj +0.82) on $16.11, P(profit) 0.674, adj growth 7.2 bp · C EV +3.36 (adj +0.76) on $16.04, P(profit) 0.674, adj growth 6.6 bp · R EV +1.37 (adj +0.32) on $6.00, P(profit) 0.5558, adj growth 10.1 bp

## STL @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_STL_win | p_overtime | goals | shots NJD/STL | NJD/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.126 | 0.64 | 0.36 | 0.00 | 6.0 | 33.7/21.4 | 18.5/29.4 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.57 | 0.43 | 0.50 | 5.88 | 33.4/21.5 | 18.5/29.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.55 | 0.45 | 0.00 | 6.02 | 27.6/27.0 | 23.7/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.46 | 5.96 | 28.0/27.4 | 24.1/24.7 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.083 | 0.64 | 0.36 | 0.00 | 9.24 | 35.4/23.0 | 18.0/27.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.57 | 0.43 | 0.00 | 9.33 | 29.0/28.5 | 22.8/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 1.5 goals NO | 60 | 0.674 | 0.634 | +0.057 | +0.018 | $9.92 | FUNDED_RESEARCH | $3 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| St. Louis over 4.5 goals scored YES | 13 | 0.179 | 0.149 | +0.041 | +0.011 | $2.03 | FUNDED_RESEARCH | $1 | STL:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes; why: higher confidence-adjusted growth (2.86 vs 2.43 bp); wins across more scripts (relative breadth 0.907 vs 0.573); relationships: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes: REINFORCING (phi 0.291); failure: NJD wins by 2+
- **St. Louis over 4.5 goals scored YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05STLNJ-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05STLNJ-NJ2|no has the higher standalone adjusted growth (2.86 vs 2.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.291); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05STLNJ-NJ2|no: REINFORCING (phi 0.291); failure: NJD wins (incl. OT/SO)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis STL:WINS (p 0.445): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05STLNJ-NJ2|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3382): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV05STLNJ-NJ2|no (same contract)
- KXNHLSPREAD-26NOV05STLNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3263, phi -1.0)
- KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes: FUNDED_RESEARCH; family MIXED; loses 47% of the draws where the thesis happens; opposing: failure thesis NJD:WINS (p 0.555, phi -0.425)

portfolios: A EV +3.56 (adj +1.04) on $21.13, P(profit) 0.6798, adj growth 6.9 bp · B EV +1.52 (adj +0.45) on $11.95, P(profit) 0.6798, adj growth 4.0 bp · C EV +1.11 (adj +0.34) on $11.99, P(profit) 0.6737, adj growth 3.0 bp · R EV +0.57 (adj +0.17) on $4.00, P(profit) 0.6798, adj growth 5.4 bp

## CAR @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 3 on card


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
| Carolina wins by over 1.5 goals NO | 62 | 0.704 | 0.660 | +0.068 | +0.023 | $11.35 | FUNDED_RESEARCH | $3 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I over 2.5 goals scored YES | 50 | 0.623 | 0.540 | +0.105 | +0.022 | $6.21 | FUNDED_RESEARCH | $2 | NYI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I wins by over 1.5 goals YES | 21 | 0.275 | 0.237 | +0.053 | +0.016 | $1.50 | FUNDED_RESEARCH | $1 | NYI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV05CARNYI-NYI3|yes; why: KXNHLSPREAD-26NOV05CARNYI-NYI3|yes has the higher standalone adjusted growth (5.45 vs 5.09 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.297); relationships: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes: REINFORCING (phi 0.491); KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: DUPLICATIVE (phi 0.399); failure: CAR wins by 2+
- **New York I over 2.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CARNYI-NYI3|yes; why: KXNHLSPREAD-26NOV05CARNYI-NYI3|yes has the higher standalone adjusted growth (5.45 vs 4.30 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.356); relationships: KXNHLSPREAD-26NOV05CARNYI-CAR2|no: REINFORCING (phi 0.491); KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: REINFORCING (phi 0.439); failure: NYI offense suppressed (<= 2 goals)
- **New York I wins by over 1.5 goals YES** — thesis: NYI wins by 2+; alternative: KXNHLSPREAD-26NOV05CARNYI-NYI3|yes; why: Broad expression KXNHLSPREAD-26NOV05CARNYI-NYI2|yes selected over broad KXNHLSPREAD-26NOV05CARNYI-NYI3|yes because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.63 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV05CARNYI-CAR2|no: DUPLICATIVE (phi 0.399); KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes: REINFORCING (phi 0.439); failure: CAR wins (incl. OT/SO)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:WINS_BY_2PLUS (p 0.2745): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR2|no (same contract)
- thesis NYI:WINS (p 0.4951): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR2|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3921): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV05CARNYI-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2957, phi -1.0)
- KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.8 pts; opposing: failure thesis NYI:SUPPRESSED (p 0.3875, phi -0.979)
- KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5049, phi -0.621)
- override: Broad expression KXNHLSPREAD-26NOV05CARNYI-NYI2|yes selected over broad KXNHLSPREAD-26NOV05CARNYI-NYI3|yes because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.63 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +7.05 (adj +1.91) on $33.13, P(profit) 0.5538, adj growth 12.9 bp · B EV +2.83 (adj +0.78) on $19.06, P(profit) 0.5557, adj growth 6.9 bp · C EV +1.46 (adj +0.53) on $4.04, P(profit) 0.1733, adj growth 4.6 bp · R EV +0.96 (adj +0.27) on $6.00, P(profit) 0.5557, adj growth 8.8 bp

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

## DAL @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_DAL_win | p_overtime | goals | shots CBJ/DAL | CBJ/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.56 | 0.44 | 0.00 | 6.02 | 25.7/25.6 | 22.3/21.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.95 | 26.0/26.0 | 22.7/22.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.56 | 0.44 | 0.00 | 9.25 | 27.2/27.3 | 21.7/20.7 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.072 | 0.60 | 0.40 | 0.00 | 5.98 | 30.7/20.5 | 17.5/26.4 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.57 | 0.43 | 0.49 | 5.92 | 30.5/20.6 | 17.5/27.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.066 | 0.45 | 0.55 | 0.00 | 5.97 | 20.5/30.7 | 26.8/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Columbus over 5.5 goals scored YES | 6 | 0.097 | 0.076 | +0.033 | +0.012 | $2.43 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | FRAGILE (0.34) | EVIDENCE_MIXED | D |
- **Columbus over 5.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ5|yes; why: higher confidence-adjusted growth (4.99 vs 0.82 bp); despite a smaller raw edge (+0.033 vs +0.035/contract); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: DAL wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis GAME:HIGH_EVENT (p 0.2474): highest fidelity KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes [FRAGILE], best adjusted EV KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes (same contract)
- KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes: FUNDED_RESEARCH; family MIXED; loses 66% of the draws where the thesis happens; opposing: failure thesis DAL:WINS (p 0.4724, phi -0.288)

portfolios: A EV +2.93 (adj +1.06) on $5.76, P(profit) 0.0965, adj growth 7.3 bp · B EV +1.24 (adj +0.45) on $2.43, P(profit) 0.0965, adj growth 3.9 bp · C EV +1.24 (adj +0.45) on $2.43, P(profit) 0.0965, adj growth 3.9 bp · R EV +0.51 (adj +0.18) on $1.00, P(profit) 0.0965, adj growth 5.7 bp

## VAN @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 2 on card


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
| Vancouver wins by over 1.5 goals YES | 17 | 0.247 | 0.206 | +0.067 | +0.026 | $5.34 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Winnipeg wins by over 2.5 goals NO | 70 | 0.793 | 0.744 | +0.078 | +0.029 | $20.00 | FUNDED_RESEARCH | $5 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26NOV05VANWPG-WPG3|no; why: higher confidence-adjusted growth (10.06 vs 9.22 bp); despite a smaller raw edge (+0.067 vs +0.078/contract); relationships: KXNHLSPREAD-26NOV05VANWPG-WPG3|no: REINFORCING (phi 0.293); failure: WPG wins (incl. OT/SO)
- **Winnipeg wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes has the higher standalone adjusted growth (10.06 vs 9.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.293); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes: REINFORCING (phi 0.293); failure: WPG wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, WPG shot control · normal event (5-7) · decided (2+) 0.11, WPG shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.2472): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no (same contract)
- thesis VAN:WINS (p 0.4565): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no (same contract)
- thesis WPG:SUPPRESSED (p 0.358): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no (same contract)
- KXNHLSPREAD-26NOV05VANWPG-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:WINS (p 0.5435, phi -0.625)
- KXNHLSPREAD-26NOV05VANWPG-WPG3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:WINS_BY_2PLUS (p 0.322, phi -0.742)

portfolios: A EV +7.27 (adj +2.46) on $33.13, P(profit) 0.678, adj growth 18.7 bp · B EV +4.19 (adj +1.60) on $25.34, P(profit) 0.7928, adj growth 14.1 bp · C EV +2.56 (adj +1.00) on $6.85, P(profit) 0.2472, adj growth 8.7 bp · R EV +1.29 (adj +0.50) on $7.00, P(profit) 0.2472, adj growth 16.7 bp

## ANA @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_ANA_win | p_overtime | goals | shots EDM/ANA | EDM/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.142 | 0.61 | 0.39 | 0.00 | 9.63 | 29.8/29.8 | 24.0/22.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.61 | 0.39 | 0.00 | 6.08 | 27.9/27.8 | 24.6/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.50 | 0.50 | 0.45 | 6.08 | 28.0/28.3 | 24.8/24.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 9.73 | 34.8/24.0 | 18.8/26.6 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.067 | 0.66 | 0.34 | 0.00 | 6.09 | 32.9/22.3 | 19.5/28.2 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.065 | 0.50 | 0.50 | 0.00 | 9.59 | 24.0/34.6 | 27.8/18.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim over 4.5 goals scored YES | 20 | 0.261 | 0.223 | +0.050 | +0.012 | $2.76 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_MIXED | D |
| Anaheim over 2.5 goals scored YES | 59 | 0.654 | 0.617 | +0.047 | +0.010 | $3.56 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Anaheim over 4.5 goals scored YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA3|yes; why: higher confidence-adjusted growth (1.83 vs 0.92 bp); relationships: KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA3|yes: DUPLICATIVE (phi 0.432); failure: EDM wins (incl. OT/SO)
- **Anaheim over 2.5 goals scored YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes has the higher standalone adjusted growth (1.83 vs 0.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.432); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes: DUPLICATIVE (phi 0.432); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4395): highest fidelity KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes: FUNDED_RESEARCH; family MIXED; loses 41% of the draws where the thesis happens; opposing: failure thesis EDM:WINS (p 0.5727, phi -0.492)
- KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis ANA:SUPPRESSED (p 0.3549, phi -0.981)

portfolios: A EV +3.50 (adj +0.81) on $23.73, P(profit) 0.2611, adj growth 4.2 bp · B EV +0.93 (adj +0.21) on $6.32, P(profit) 0.2611, adj growth 1.9 bp · C EV +0.79 (adj +0.19) on $3.34, P(profit) 0.2611, adj growth 1.6 bp · R EV +0.31 (adj +0.07) on $2.00, P(profit) 0.2611, adj growth 2.4 bp

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
