# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T04:32:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 80.00 | +6.34 | +1.90 | +9.29 | 0.584 | -52.02 | -80.00 | 12.26 |
| B thesis-diversified (joint) ← optimiser card | 29.79 | +2.25 | +0.68 | +6.77 | 0.584 | -14.85 | -29.79 | 5.95 |
| C best expression per thesis | 29.94 | +2.05 | +0.63 | +11.35 | 0.599 | -10.80 | -29.94 | 5.49 |
| R FUNDED research stakes | 10.00 | +0.77 | +0.23 | +1.69 | 0.584 | -5.80 | -10.00 | 0.00 |

## CBJ @ MIN  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_CBJ_win | p_overtime | goals | shots MIN/CBJ | MIN/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.61 | 0.39 | 0.00 | 6.03 | 28.6/28.6 | 25.4/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.46 | 5.91 | 28.5/28.5 | 25.2/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.61 | 0.39 | 0.00 | 9.33 | 30.0/30.1 | 24.9/23.2 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.073 | 0.67 | 0.33 | 0.00 | 5.99 | 33.6/22.9 | 20.2/29.1 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.062 | 0.52 | 0.48 | 0.00 | 5.95 | 22.7/33.4 | 29.8/19.3 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.52 | 0.48 | 0.49 | 5.95 | 22.8/33.4 | 30.1/19.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Minnesota wins by over 2.5 goals NO | 72 | 0.785 | 0.750 | +0.051 | +0.016 | $10.97 | FUNDED_RESEARCH | $3 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 1.5 goals NO | 59 | 0.662 | 0.624 | +0.056 | +0.017 | $5.21 | FUNDED_RESEARCH | $2 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 2.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT18CBJMIN-MIN2|no; why: higher confidence-adjusted growth (2.79 vs 2.58 bp); despite a smaller raw edge (+0.051 vs +0.056/contract); wins across more scripts (relative breadth 1.015 vs 0.903); relationships: KXNHLSPREAD-26OCT18CBJMIN-MIN2|no: DUPLICATIVE (phi 0.734); failure: MIN wins by 2+
- **Minnesota wins by over 1.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT18CBJMIN-MIN3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT18CBJMIN-MIN3|no has the higher standalone adjusted growth (2.79 vs 2.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.734); they share one thesis budget; relationships: KXNHLSPREAD-26OCT18CBJMIN-MIN3|no: DUPLICATIVE (phi 0.734); failure: MIN wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:WINS (p 0.437): highest fidelity KXNHLSPREAD-26OCT18CBJMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CBJMIN-MIN2|no (same contract)
- KXNHLSPREAD-26OCT18CBJMIN-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3376, phi -0.734)
- KXNHLSPREAD-26OCT18CBJMIN-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3376, phi -1.0)

portfolios: A EV +3.21 (adj +0.98) on $40.00, P(profit) 0.6624, adj growth 6.6 bp · B EV +1.23 (adj +0.38) on $16.18, P(profit) 0.6624, adj growth 3.3 bp · C EV +1.12 (adj +0.35) on $16.26, P(profit) 0.7847, adj growth 3.1 bp · R EV +0.39 (adj +0.12) on $5.00, P(profit) 0.6624, adj growth 4.0 bp

## CAR @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_CAR_win | p_overtime | goals | shots CGY/CAR | CGY/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.143 | 0.31 | 0.69 | 0.00 | 6.07 | 21.9/34.4 | 29.7/19.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.46 | 0.54 | 0.47 | 5.9 | 22.1/34.7 | 31.1/18.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.39 | 0.61 | 0.00 | 6.06 | 27.9/28.8 | 24.8/24.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.094 | 0.30 | 0.69 | 0.00 | 9.18 | 23.1/36.0 | 28.0/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.47 | 0.53 | 0.48 | 5.93 | 27.6/28.5 | 25.1/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.43 | 0.57 | 0.00 | 9.27 | 29.1/30.1 | 23.6/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 2.5 goals NO | 70 | 0.763 | 0.729 | +0.049 | +0.014 | $9.32 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 1.5 goals NO | 57 | 0.639 | 0.602 | +0.052 | +0.015 | $4.30 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT18CARCGY-CAR2|no; why: higher confidence-adjusted growth (2.23 vs 2.04 bp); despite a smaller raw edge (+0.049 vs +0.052/contract); wins across more scripts (relative breadth 1.017 vs 0.893); relationships: KXNHLSPREAD-26OCT18CARCGY-CAR2|no: DUPLICATIVE (phi 0.742); failure: CAR wins by 2+
- **Carolina wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT18CARCGY-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT18CARCGY-CAR3|no has the higher standalone adjusted growth (2.23 vs 2.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.742); they share one thesis budget; relationships: KXNHLSPREAD-26OCT18CARCGY-CAR3|no: DUPLICATIVE (phi 0.742); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4314): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CARCGY-CAR2|no (same contract)
- KXNHLSPREAD-26OCT18CARCGY-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3606, phi -0.742)
- KXNHLSPREAD-26OCT18CARCGY-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3606, phi -1.0)

portfolios: A EV +3.14 (adj +0.92) on $40.00, P(profit) 0.6394, adj growth 5.6 bp · B EV +1.01 (adj +0.30) on $13.61, P(profit) 0.6394, adj growth 2.6 bp · C EV +0.93 (adj +0.28) on $13.68, P(profit) 0.7632, adj growth 2.4 bp · R EV +0.38 (adj +0.11) on $5.00, P(profit) 0.6394, adj growth 3.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
