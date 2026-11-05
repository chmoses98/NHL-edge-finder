# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T06:51:45Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +29.74 | +8.82 | +22.42 | 0.623 | -65.91 | -87.07 | 58.93 |
| B thesis-diversified (joint) ← optimiser card | 68.83 | +11.00 | +3.31 | +12.61 | 0.648 | -24.85 | -35.54 | 29.03 |
| C best expression per thesis | 34.78 | +9.35 | +3.06 | +7.55 | 0.526 | -20.61 | -34.78 | 26.58 |
| R FUNDED research stakes | 22.00 | +4.00 | +1.24 | +3.12 | 0.587 | -8.66 | -11.85 | 0.00 |

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

## CHI @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 2 on card


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
| Tampa Bay wins by over 1.5 goals NO | 42 | 0.541 | 0.459 | +0.103 | +0.022 | $6.63 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 56 | 0.674 | 0.597 | +0.097 | +0.019 | $5.45 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no; why: Broad expression KXNHLSPREAD-26NOV05CHITB-TB2|no selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no because adjusted EV is 0.7 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV05CHITB-TB3|no: DUPLICATIVE (phi 0.754); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: Broad expression KXNHLSPREAD-26NOV05CHITB-TB3|no selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-CHI5|yes because adjusted EV is 0.7 pts higher while thesis capture is 0.93 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: DUPLICATIVE (phi 0.754); failure: TBL wins by 2+

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.16, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, TBL shot control · high event (8+) · decided (2+) 0.12.
- thesis CHI:OFFENSE_4PLUS (p 0.2601): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no — Broad expression KXNHLSPREAD-26NOV05CHITB-TB3|no selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-CHI5|yes because adjusted EV is 0.7 pts higher while thesis capture is 0.93 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CHI:WINS (p 0.3132): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no (same contract)
- thesis GAME:TIGHT (p 0.4022): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no (same contract)
- KXNHLSPREAD-26NOV05CHITB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.6 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4594, phi -1.0)
- KXNHLSPREAD-26NOV05CHITB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.9 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4594, phi -0.754)
- override: Broad expression KXNHLSPREAD-26NOV05CHITB-TB2|no selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no because adjusted EV is 0.7 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26NOV05CHITB-TB3|no selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-CHI5|yes because adjusted EV is 0.7 pts higher while thesis capture is 0.93 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +7.36 (adj +1.73) on $38.56, P(profit) 0.5877, adj growth 10.9 bp · B EV +2.48 (adj +0.52) on $12.08, P(profit) 0.5406, adj growth 4.5 bp · C EV +2.69 (adj +0.70) on $9.74, P(profit) 0.5478, adj growth 6.1 bp · R EV +0.81 (adj +0.17) on $4.00, P(profit) 0.5406, adj growth 5.6 bp

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
| New Jersey wins by over 1.5 goals NO | 61 | 0.674 | 0.639 | +0.047 | +0.013 | $6.72 | FUNDED_RESEARCH | $2 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| St. Louis wins by over 1.5 goals YES | 19 | 0.237 | 0.211 | +0.036 | +0.010 | $2.01 | FUNDED_RESEARCH | $1 | STL:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV05STLNJ-STL2|yes; why: higher confidence-adjusted growth (1.51 vs 1.45 bp); wins across more scripts (relative breadth 0.907 vs 0.556); relationships: KXNHLSPREAD-26NOV05STLNJ-STL2|yes: DUPLICATIVE (phi 0.388); failure: NJD wins by 2+
- **St. Louis wins by over 1.5 goals YES** — thesis: STL wins by 2+; alternative: KXNHLSPREAD-26NOV05STLNJ-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05STLNJ-NJ2|no has the higher standalone adjusted growth (1.51 vs 1.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.388); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05STLNJ-NJ2|no: DUPLICATIVE (phi 0.388); failure: NJD wins (incl. OT/SO)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis STL:WINS (p 0.445): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05STLNJ-NJ2|no (same contract)
- thesis STL:WINS_BY_2PLUS (p 0.2372): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05STLNJ-NJ2|no (same contract)
- KXNHLSPREAD-26NOV05STLNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3263, phi -1.0)
- KXNHLSPREAD-26NOV05STLNJ-STL2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.555, phi -0.623)

portfolios: A EV +2.75 (adj +0.76) on $24.21, P(profit) 0.6737, adj growth 4.4 bp · B EV +0.87 (adj +0.24) on $8.73, P(profit) 0.6737, adj growth 2.1 bp · C EV +0.67 (adj +0.18) on $8.88, P(profit) 0.6737, adj growth 1.6 bp · R EV +0.33 (adj +0.09) on $3.00, P(profit) 0.6737, adj growth 2.9 bp

## CAR @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 2 on card


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
| Carolina wins by over 1.5 goals NO | 62 | 0.704 | 0.660 | +0.068 | +0.023 | $12.33 | FUNDED_RESEARCH | $4 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I over 2.5 goals scored YES | 50 | 0.623 | 0.540 | +0.105 | +0.022 | $7.20 | FUNDED_RESEARCH | $2 | NYI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes has the higher standalone adjusted growth (9.83 vs 5.09 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.303); relationships: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes: REINFORCING (phi 0.491); failure: CAR wins by 2+
- **New York I over 2.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes selected over broad KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV05CARNYI-CAR2|no: REINFORCING (phi 0.491); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.3921): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes — Broad expression KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes selected over broad KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYI:WINS_BY_2PLUS (p 0.2745): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.4951): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV05CARNYI-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2957, phi -1.0)
- KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.8 pts; opposing: failure thesis NYI:SUPPRESSED (p 0.3875, phi -0.979)
- override: Broad expression KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes selected over broad KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.67 (adj +3.07) on $38.56, P(profit) 0.5538, adj growth 20.5 bp · B EV +2.78 (adj +0.76) on $19.54, P(profit) 0.5471, adj growth 6.7 bp · C EV +2.58 (adj +0.93) on $5.77, P(profit) 0.2149, adj growth 8.1 bp · R EV +0.83 (adj +0.23) on $6.00, P(profit) 0.7043, adj growth 7.9 bp

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
| Columbus wins by over 1.5 goals YES | 25 | 0.302 | 0.273 | +0.039 | +0.010 | $3.27 | FUNDED_RESEARCH | $1 | CBJ:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Columbus wins by over 1.5 goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLSPREAD-26NOV05DALCBJ-DAL2|no; why: higher confidence-adjusted growth (1.19 vs 0.92 bp); alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: DAL wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:WINS_BY_2PLUS (p 0.3018): highest fidelity KXNHLSPREAD-26NOV05DALCBJ-CBJ2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05DALCBJ-CBJ2|yes (same contract)
- KXNHLSPREAD-26NOV05DALCBJ-CBJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.4724, phi -0.622)

portfolios: A EV +1.49 (adj +0.40) on $10.12, P(profit) 0.3018, adj growth 2.4 bp · B EV +0.48 (adj +0.13) on $3.27, P(profit) 0.3018, adj growth 1.1 bp · C EV +0.48 (adj +0.13) on $3.27, P(profit) 0.3018, adj growth 1.1 bp · R EV +0.15 (adj +0.04) on $1.00, P(profit) 0.3018, adj growth 1.3 bp

## VAN @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 3 on card


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
| Vancouver wins by over 1.5 goals YES | 17 | 0.247 | 0.206 | +0.067 | +0.026 | $4.02 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Winnipeg wins by over 2.5 goals NO | 70 | 0.793 | 0.744 | +0.078 | +0.029 | $20.00 | FUNDED_RESEARCH | $5 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 5.5 goals scored YES | 5 | 0.085 | 0.065 | +0.031 | +0.011 | $1.19 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | FRAGILE (0.29) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26NOV05VANWPG-WPG3|no; why: higher confidence-adjusted growth (10.06 vs 9.22 bp); despite a smaller raw edge (+0.067 vs +0.078/contract); relationships: KXNHLSPREAD-26NOV05VANWPG-WPG3|no: REINFORCING (phi 0.293); KXNHLTEAMTOTAL-26NOV05VANWPG-VAN6|yes: REINFORCING (phi 0.381); failure: WPG wins (incl. OT/SO)
- **Winnipeg wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes has the higher standalone adjusted growth (10.06 vs 9.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.293); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes: REINFORCING (phi 0.293); KXNHLTEAMTOTAL-26NOV05VANWPG-VAN6|yes: REINFORCING (phi 0.154); failure: WPG wins by 2+
- **Vancouver over 5.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26NOV05VANWPG-VAN5|yes; why: higher confidence-adjusted growth (5.62 vs 1.16 bp); despite a smaller raw edge (+0.031 vs +0.036/contract); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes: REINFORCING (phi 0.381); KXNHLSPREAD-26NOV05VANWPG-WPG3|no: REINFORCING (phi 0.154); failure: WPG wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, WPG shot control · normal event (5-7) · decided (2+) 0.11, WPG shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.2472): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no (same contract)
- thesis VAN:WINS (p 0.4565): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no (same contract)
- thesis WPG:SUPPRESSED (p 0.358): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no (same contract)
- KXNHLSPREAD-26NOV05VANWPG-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:WINS (p 0.5435, phi -0.625)
- KXNHLSPREAD-26NOV05VANWPG-WPG3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:WINS_BY_2PLUS (p 0.322, phi -0.742)
- KXNHLTEAMTOTAL-26NOV05VANWPG-VAN6|yes: FUNDED_RESEARCH; family MIXED; loses 71% of the draws where the thesis happens; opposing: failure thesis WPG:WINS (p 0.5435, phi -0.301)

portfolios: A EV +8.46 (adj +2.86) on $38.56, P(profit) 0.678, adj growth 20.7 bp · B EV +4.39 (adj +1.66) on $25.21, P(profit) 0.7928, adj growth 14.6 bp · C EV +2.93 (adj +1.12) on $7.12, P(profit) 0.2652, adj growth 9.7 bp · R EV +1.88 (adj +0.71) on $8.00, P(profit) 0.2652, adj growth 21.5 bp

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
