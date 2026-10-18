# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T13:23:20Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 78.27 | +11.17 | +2.92 | +12.29 | 0.649 | -51.73 | -51.73 | 21.90 |
| B thesis-diversified (joint) ← optimiser card | 40.83 | +5.00 | +2.08 | -3.34 | 0.465 | -19.20 | -24.98 | 18.03 |
| C best expression per thesis | 26.00 | +3.85 | +1.38 | -4.36 | 0.373 | -25.99 | -25.99 | 11.95 |
| R FUNDED research stakes | 6.00 | +0.98 | +0.40 | -1.62 | 0.373 | -6.00 | -6.00 | 0.00 |

## CBJ @ MIN  ·  10000 joint draws  ·  428 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_CBJ_win | p_overtime | goals | shots MIN/CBJ | MIN/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.66 | 0.34 | 0.00 | 5.98 | 28.6/28.5 | 25.8/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.55 | 0.45 | 0.45 | 5.92 | 28.7/28.8 | 25.6/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.67 | 0.33 | 0.00 | 9.25 | 30.3/30.2 | 25.0/22.9 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.070 | 0.62 | 0.38 | 0.00 | 6.01 | 22.7/33.2 | 30.2/18.7 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.069 | 0.68 | 0.32 | 0.00 | 6.04 | 33.2/22.6 | 19.9/28.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.66 | 0.34 | 0.00 | 3.51 | 27.3/27.5 | 26.0/24.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 14 | 0.177 | 0.163 | +0.028 | +0.014 | $3.89 | FUNDED_RESEARCH | $1 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Valeri Nichushkin: 1+ assists NO | 74 | 0.809 | 0.767 | +0.056 | +0.014 | $16.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLAST-26OCT18CBJMIN-CBJCCOYLE3-2|yes; why: higher confidence-adjusted growth (3.37 vs 1.58 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: CBJ offense suppressed (<= 2 goals)
- **Valeri Nichushkin: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHL3PTOTAL-26OCT18CBJMIN-3|no; why: higher confidence-adjusted growth (2.25 vs 0.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3023): highest fidelity KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.4857): highest fidelity KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no (same contract)
- KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4857, phi -0.228)
- KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3023, phi -0.206)

portfolios: A EV +3.06 (adj +1.15) on $28.27, P(profit) 0.1766, adj growth 8.8 bp · B EV +1.95 (adj +0.67) on $20.19, P(profit) 0.8461, adj growth 5.8 bp · C EV +1.95 (adj +0.67) on $20.19, P(profit) 0.8461, adj growth 5.8 bp · R EV +0.19 (adj +0.09) on $1.00, P(profit) 0.1766, adj growth 3.3 bp

## CAR @ CGY  ·  10000 joint draws  ·  418 bet sides mapped, 16 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_CAR_win | p_overtime | goals | shots CGY/CAR | CGY/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.144 | 0.39 | 0.61 | 0.00 | 5.95 | 21.7/34.4 | 30.1/18.8 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.124 | 0.47 | 0.53 | 0.45 | 5.97 | 22.0/34.7 | 31.1/18.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.45 | 0.55 | 0.00 | 5.96 | 27.7/28.6 | 24.9/24.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.090 | 0.35 | 0.65 | 0.00 | 9.25 | 23.5/36.4 | 28.5/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.52 | 0.48 | 0.46 | 5.9 | 27.4/28.1 | 24.9/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.46 | 0.54 | 0.00 | 9.31 | 29.3/30.1 | 23.5/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Calgary wins by over 1.5 goals YES | 17 | 0.239 | 0.202 | +0.059 | +0.022 | $4.56 | FUNDED_RESEARCH | $2 | CGY:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jonathan Castagna: 1+ goals YES | 9 | 0.115 | 0.107 | +0.019 | +0.012 | $2.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Adam Klapka: 1+ goals YES | 10 | 0.129 | 0.118 | +0.022 | +0.011 | $2.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 67 | 0.717 | 0.702 | +0.032 | +0.016 | $10.87 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Calgary wins by over 1.5 goals YES** — thesis: CGY wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no; why: higher confidence-adjusted growth (7.05 vs 4.47 bp); despite a smaller raw edge (+0.059 vs +0.068/contract); relationships: KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26OCT18CARCGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi 0.124); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.148); failure: CAR wins (incl. OT/SO)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes has the higher standalone adjusted growth (7.05 vs 3.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.107); they share one thesis budget; relationships: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26OCT18CARCGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: CGY offense suppressed (<= 2 goals)
- **Adam Klapka: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes has the higher standalone adjusted growth (7.05 vs 2.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.124); they share one thesis budget; relationships: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes: MOSTLY_INDEPENDENT (phi 0.124); KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: CGY offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: Player prop expression KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.86 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes: MOSTLY_INDEPENDENT (phi 0.148); KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT18CARCGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CGY:WINS_BY_2PLUS (p 0.2386): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.3705): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3393): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CARCGY-CGY2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT18CARCGY-CGY2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5523, phi -0.622)
- KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4398, phi -0.157)
- KXNHLGOAL-26OCT18CARCGY-CGYAKLAPKA43-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4398, phi -0.172)
- KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4154, phi -0.232)
- override: Player prop expression KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.86 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +8.12 (adj +1.77) on $50.00, P(profit) 0.6298, adj growth 13.1 bp · B EV +3.05 (adj +1.41) on $20.64, P(profit) 0.3838, adj growth 12.2 bp · C EV +1.90 (adj +0.71) on $5.81, P(profit) 0.2386, adj growth 6.1 bp · R EV +0.79 (adj +0.31) on $5.00, P(profit) 0.2386, adj growth 10.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
