# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T12:23:20Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 80.32 | +14.87 | +3.77 | +4.40 | 0.690 | -48.11 | -80.32 | 25.94 |
| B thesis-diversified (joint) ← optimiser card | 34.85 | +5.51 | +1.91 | +13.21 | 0.545 | -15.16 | -34.86 | 16.88 |
| C best expression per thesis | 30.40 | +4.31 | +1.47 | -2.03 | 0.438 | -10.71 | -30.40 | 13.22 |
| R FUNDED research stakes | 8.00 | +1.26 | +0.45 | +1.06 | 0.613 | -8.00 | -8.00 | 0.00 |

## CBJ @ MIN  ·  10000 joint draws  ·  428 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_CBJ_win | p_overtime | goals | shots MIN/CBJ | MIN/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.65 | 0.35 | 0.00 | 5.99 | 28.6/28.6 | 25.7/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.47 | 5.92 | 28.6/28.7 | 25.5/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.65 | 0.35 | 0.00 | 9.2 | 29.9/30.0 | 25.1/22.7 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.074 | 0.70 | 0.30 | 0.00 | 6.02 | 33.6/23.0 | 20.5/29.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.068 | 0.59 | 0.41 | 0.00 | 5.96 | 22.7/33.5 | 30.4/19.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.63 | 0.37 | 0.00 | 3.47 | 27.4/27.5 | 26.0/25.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Quinn Hughes: 1+ assists NO | 36 | 0.443 | 0.396 | +0.067 | +0.020 | $7.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.68) | EVIDENCE_MIXED | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.173 | 0.149 | +0.036 | +0.011 | $2.72 | FUNDED_RESEARCH | $1 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT18CBJMIN-4|no; why: higher confidence-adjusted growth (3.78 vs 0.07 bp); wins across more scripts (relative breadth 0.999 vs 0.368); alternative not eligible: confidence-adjusted EV +0.0019 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: MIN offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT18CBJMIN-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (2.19 vs 0.36 bp); alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.3464): highest fidelity KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.3025): highest fidelity KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes (same contract)
- KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 32% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4355, phi -0.317)
- KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.487, phi -0.233)

portfolios: A EV +6.20 (adj +1.89) on $30.32, P(profit) 0.5365, adj growth 11.5 bp · B EV +2.06 (adj +0.63) on $10.40, P(profit) 0.5365, adj growth 5.5 bp · C EV +2.06 (adj +0.63) on $10.40, P(profit) 0.5365, adj growth 5.5 bp · R EV +0.26 (adj +0.08) on $1.00, P(profit) 0.1735, adj growth 2.6 bp

## CAR @ CGY  ·  10000 joint draws  ·  418 bet sides mapped, 10 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_CAR_win | p_overtime | goals | shots CGY/CAR | CGY/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.147 | 0.39 | 0.61 | 0.00 | 6.03 | 21.9/34.6 | 30.3/19.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.124 | 0.48 | 0.52 | 0.50 | 5.91 | 22.1/34.8 | 31.3/19.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.100 | 0.44 | 0.56 | 0.00 | 6.01 | 27.6/28.5 | 24.6/24.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.093 | 0.36 | 0.64 | 0.00 | 9.38 | 23.4/36.3 | 28.6/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.50 | 0.50 | 0.49 | 5.94 | 27.7/28.5 | 25.3/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.47 | 0.53 | 0.00 | 9.27 | 29.1/30.2 | 23.8/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 2.5 goals NO | 69 | 0.784 | 0.735 | +0.079 | +0.030 | $20.00 | FUNDED_RESEARCH | $5 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Calgary wins by over 1.5 goals YES | 17 | 0.237 | 0.201 | +0.057 | +0.021 | $3.34 | FUNDED_RESEARCH | $1 | CGY:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina over 3.5 goals scored NO | 49 | 0.572 | 0.528 | +0.064 | +0.021 | $1.11 | FUNDED_RESEARCH | $1 | CAR:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: higher confidence-adjusted growth (9.36 vs 6.42 bp); wins across more scripts (relative breadth 1.021 vs 0.554); relationships: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes: REINFORCING (phi 0.292); KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: REINFORCING (phi 0.512); failure: CAR wins by 2+
- **Calgary wins by over 1.5 goals YES** — thesis: CGY wins by 2+; alternative: KXNHLSPREAD-26OCT18CARCGY-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT18CARCGY-CAR3|no has the higher standalone adjusted growth (9.36 vs 6.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.292); they share one thesis budget; relationships: KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.292); KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: REINFORCING (phi 0.385); failure: CAR wins (incl. OT/SO)
- **Carolina over 3.5 goals scored NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CAR3|no; why: Broad expression KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.512); KXNHLSPREAD-26OCT18CARCGY-CGY2|yes: REINFORCING (phi 0.385); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CGY:WINS (p 0.4452): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CARCGY-CAR3|no (same contract)
- thesis CGY:WINS_BY_2PLUS (p 0.2366): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CARCGY-CAR3|no (same contract)
- thesis CAR:SUPPRESSED (p 0.3623): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CARCGY-CAR3|no (same contract)
- KXNHLSPREAD-26OCT18CARCGY-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3314, phi -0.745)
- KXNHLSPREAD-26OCT18CARCGY-CGY2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5548, phi -0.621)
- KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4189, phi -0.981)
- override: Broad expression KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +8.67 (adj +1.88) on $50.00, P(profit) 0.7343, adj growth 14.5 bp · B EV +3.45 (adj +1.28) on $24.45, P(profit) 0.7844, adj growth 11.4 bp · C EV +2.25 (adj +0.84) on $20.00, P(profit) 0.7844, adj growth 7.7 bp · R EV +1.00 (adj +0.37) on $7.00, P(profit) 0.7844, adj growth 12.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
