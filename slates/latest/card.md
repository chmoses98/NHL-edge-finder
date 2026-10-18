# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T10:35:28Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 80.00 | +6.29 | +1.87 | +9.68 | 0.584 | -51.63 | -80.00 | 12.01 |
| B thesis-diversified (joint) ← optimiser card | 33.96 | +2.58 | +0.83 | +13.30 | 0.599 | -11.81 | -33.96 | 7.29 |
| C best expression per thesis | 33.96 | +2.58 | +0.83 | +13.30 | 0.599 | -11.81 | -33.96 | 7.29 |
| R FUNDED research stakes | 10.00 | +0.76 | +0.25 | +3.90 | 0.599 | -3.19 | -10.00 | 0.00 |

## CBJ @ MIN  ·  10000 joint draws  ·  428 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_CBJ_win | p_overtime | goals | shots MIN/CBJ | MIN/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.61 | 0.39 | 0.00 | 6.05 | 28.7/28.8 | 25.8/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.45 | 5.89 | 28.4/28.6 | 25.2/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.59 | 0.41 | 0.00 | 9.24 | 30.4/30.4 | 24.9/23.6 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.071 | 0.64 | 0.36 | 0.00 | 5.99 | 33.5/22.9 | 20.1/28.9 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.065 | 0.54 | 0.46 | 0.00 | 5.92 | 22.8/33.8 | 30.3/19.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.58 | 0.42 | 0.00 | 3.5 | 26.9/26.9 | 25.3/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Minnesota wins by over 2.5 goals NO | 72 | 0.785 | 0.750 | +0.051 | +0.016 | $16.26 | FUNDED_RESEARCH | $5 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 2.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT18CBJMIN-MIN2|no; why: higher confidence-adjusted growth (2.79 vs 1.31 bp); wins across more scripts (relative breadth 1.013 vs 0.901); relationships: only recommended bet in this game; failure: MIN wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:WINS (p 0.437): highest fidelity KXNHLSPREAD-26OCT18CBJMIN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CBJMIN-MIN3|no (same contract)
- KXNHLSPREAD-26OCT18CBJMIN-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3376, phi -0.734)

portfolios: A EV +2.86 (adj +0.81) on $40.00, P(profit) 0.6624, adj growth 5.0 bp · B EV +1.12 (adj +0.35) on $16.26, P(profit) 0.7847, adj growth 3.1 bp · C EV +1.12 (adj +0.35) on $16.26, P(profit) 0.7847, adj growth 3.1 bp · R EV +0.34 (adj +0.11) on $5.00, P(profit) 0.7847, adj growth 3.7 bp

## CAR @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_CAR_win | p_overtime | goals | shots CGY/CAR | CGY/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.139 | 0.31 | 0.69 | 0.00 | 6.08 | 22.0/34.8 | 30.0/19.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.46 | 0.54 | 0.47 | 5.89 | 22.0/34.6 | 31.3/18.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.39 | 0.61 | 0.00 | 6.04 | 27.7/28.7 | 24.5/24.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.092 | 0.32 | 0.68 | 0.00 | 9.19 | 23.1/36.1 | 28.4/18.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.46 | 0.54 | 0.47 | 5.93 | 27.9/28.8 | 25.5/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.41 | 0.59 | 0.00 | 9.28 | 29.2/30.2 | 23.6/23.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 2.5 goals NO | 69 | 0.763 | 0.724 | +0.058 | +0.019 | $17.70 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT18CARCGY-CAR2|no; why: higher confidence-adjusted growth (3.87 vs 2.04 bp); wins across more scripts (relative breadth 1.01 vs 0.883); relationships: only recommended bet in this game; failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis GAME:TIGHT (p 0.4314): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CARCGY-CAR3|no (same contract)
- KXNHLSPREAD-26OCT18CARCGY-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3606, phi -0.742)

portfolios: A EV +3.43 (adj +1.06) on $40.00, P(profit) 0.6394, adj growth 7.0 bp · B EV +1.46 (adj +0.48) on $17.70, P(profit) 0.7632, adj growth 4.2 bp · C EV +1.46 (adj +0.48) on $17.70, P(profit) 0.7632, adj growth 4.2 bp · R EV +0.41 (adj +0.14) on $5.00, P(profit) 0.7632, adj growth 4.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
