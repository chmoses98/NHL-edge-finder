# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T11:35:49Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +6.62 | +1.81 | +35.36 | 0.710 | -50.00 | -50.00 | 12.26 |
| B thesis-diversified (joint) ← optimiser card | 23.52 | +3.36 | +1.25 | +4.85 | 0.784 | -23.52 | -23.52 | 11.21 |
| C best expression per thesis | 20.00 | +2.25 | +0.84 | +8.37 | 0.784 | -20.00 | -20.00 | 7.74 |
| R FUNDED research stakes | 6.00 | +0.88 | +0.33 | +1.09 | 0.784 | -6.00 | -6.00 | 0.00 |

## CBJ @ MIN  ·  10000 joint draws  ·  428 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_CBJ_win | p_overtime | goals | shots MIN/CBJ | MIN/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.65 | 0.35 | 0.00 | 5.99 | 28.6/28.6 | 25.7/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.47 | 5.92 | 28.6/28.7 | 25.5/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.65 | 0.35 | 0.00 | 9.2 | 29.9/30.0 | 25.1/22.7 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.074 | 0.70 | 0.30 | 0.00 | 6.02 | 33.6/23.0 | 20.5/29.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.068 | 0.59 | 0.41 | 0.00 | 5.96 | 22.7/33.5 | 30.4/19.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.63 | 0.37 | 0.00 | 3.47 | 27.4/27.5 | 26.0/25.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 2 on card


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
| Calgary wins by over 1.5 goals YES | 17 | 0.237 | 0.201 | +0.057 | +0.021 | $3.52 | FUNDED_RESEARCH | $1 | CGY:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: higher confidence-adjusted growth (9.36 vs 6.42 bp); wins across more scripts (relative breadth 1.021 vs 0.554); relationships: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes: REINFORCING (phi 0.292); failure: CAR wins by 2+
- **Calgary wins by over 1.5 goals YES** — thesis: CGY wins by 2+; alternative: KXNHLSPREAD-26OCT18CARCGY-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT18CARCGY-CAR3|no has the higher standalone adjusted growth (9.36 vs 6.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.292); they share one thesis budget; relationships: KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.292); failure: CAR wins (incl. OT/SO)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CGY:WINS (p 0.4452): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CARCGY-CAR3|no (same contract)
- thesis CGY:WINS_BY_2PLUS (p 0.2366): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CARCGY-CAR3|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3455): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CARCGY-CAR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT18CARCGY-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3314, phi -0.745)
- KXNHLSPREAD-26OCT18CARCGY-CGY2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5548, phi -0.621)

portfolios: A EV +6.62 (adj +1.81) on $50.00, P(profit) 0.7098, adj growth 12.3 bp · B EV +3.36 (adj +1.25) on $23.52, P(profit) 0.7844, adj growth 11.2 bp · C EV +2.25 (adj +0.84) on $20.00, P(profit) 0.7844, adj growth 7.7 bp · R EV +0.88 (adj +0.33) on $6.00, P(profit) 0.7844, adj growth 11.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
