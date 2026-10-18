# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T23:05:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +10.14 | +1.85 | +10.07 | 0.719 | -31.23 | -33.82 | 15.89 |
| B thesis-diversified (joint) ← optimiser card | 43.41 | +6.92 | +2.18 | +9.24 | 0.707 | -18.94 | -21.09 | 19.53 |
| C best expression per thesis | 20.48 | +6.25 | +1.67 | +10.84 | 0.695 | -20.48 | -20.48 | 14.63 |
| R FUNDED research stakes | 9.00 | +0.88 | +0.38 | -0.18 | 0.414 | -7.58 | -9.00 | 0.00 |

## CAR @ CGY  ·  10000 joint draws  ·  466 bet sides mapped, 26 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.339 / away 0.661

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_CAR_win | p_overtime | goals | shots CGY/CAR | CGY/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.140 | 0.39 | 0.61 | 0.00 | 5.96 | 21.9/34.6 | 30.2/19.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.47 | 0.53 | 0.48 | 5.84 | 21.9/34.4 | 31.1/18.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.47 | 0.53 | 0.00 | 6.05 | 27.6/28.6 | 24.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.49 | 0.51 | 0.46 | 5.92 | 27.6/28.6 | 25.1/24.1 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.088 | 0.36 | 0.64 | 0.00 | 9.21 | 23.3/36.0 | 28.5/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.44 | 0.56 | 0.00 | 9.19 | 29.1/30.2 | 23.6/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sebastian Aho: 1+ assists NO | 48 | 0.644 | 0.531 | +0.147 | +0.034 | $13.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CAR:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 66 | 0.719 | 0.703 | +0.044 | +0.028 | $16.54 | FUNDED_RESEARCH | $5 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Calgary over 2.5 goals scored YES | 48 | 0.569 | 0.522 | +0.071 | +0.024 | $11.11 | FUNDED_RESEARCH | $3 | CGY:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 69 | 0.792 | 0.723 | +0.087 | +0.018 | $2.31 | FUNDED_RESEARCH | $1 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sebastian Aho: 1+ assists NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: higher confidence-adjusted growth (9.84 vs 7.67 bp); wins across more scripts (relative breadth 1.003 vs 0.548); relationships: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.198); failure: CAR offense succeeds (4+ goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no; why: second expression of the same thesis: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no has the higher standalone adjusted growth (9.84 vs 7.60 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.023); they share one thesis budget; relationships: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.164); failure: CAR offense succeeds (4+ goals)
- **Calgary over 2.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes has the higher standalone adjusted growth (7.67 vs 5.20 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.449); relationships: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.402); failure: CGY offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no; why: Broad expression KXNHLSPREAD-26OCT18CARCGY-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no: REINFORCING (phi 0.198); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: REINFORCING (phi 0.164); KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: REINFORCING (phi 0.402); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CAR:SUPPRESSED (p 0.3809): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.454): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CAR2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no — Broad expression KXNHLSPREAD-26OCT18CARCGY-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CGY:WINS_BY_2PLUS (p 0.2405): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.4 pts; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4107, phi -0.286)
- KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4107, phi -0.233)
- KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:SUPPRESSED (p 0.4421, phi -0.978)
- KXNHLSPREAD-26OCT18CARCGY-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.7 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3216, phi -0.744)
- override: Broad expression KXNHLSPREAD-26OCT18CARCGY-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +10.14 (adj +1.85) on $50.00, P(profit) 0.7187, adj growth 15.9 bp · B EV +6.92 (adj +2.18) on $43.41, P(profit) 0.7072, adj growth 19.5 bp · C EV +6.25 (adj +1.67) on $20.48, P(profit) 0.695, adj growth 14.6 bp · R EV +0.88 (adj +0.38) on $9.00, P(profit) 0.4142, adj growth 13.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
