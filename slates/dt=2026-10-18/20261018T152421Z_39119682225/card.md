# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T15:24:21Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +17.65 | +5.09 | +9.12 | 0.658 | -42.45 | -60.18 | 39.79 |
| B thesis-diversified (joint) ← optimiser card | 58.45 | +7.98 | +3.72 | +6.18 | 0.505 | -26.46 | -39.69 | 32.24 |
| C best expression per thesis | 46.11 | +9.66 | +3.61 | +4.22 | 0.646 | -27.99 | -27.99 | 31.21 |
| R FUNDED research stakes | 9.00 | +1.20 | +0.64 | +2.83 | 0.557 | -9.00 | -9.00 | 0.00 |

## CBJ @ MIN  ·  10000 joint draws  ·  442 bet sides mapped, 4 +EV candidates, 4 on card


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
| Mathieu Olivier: 1+ goals YES | 13 | 0.177 | 0.165 | +0.039 | +0.027 | $7.38 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Danton Heinen: 1+ goals YES | 9 | 0.114 | 0.108 | +0.018 | +0.012 | $3.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ assists NO | 33 | 0.432 | 0.359 | +0.086 | +0.014 | $4.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Valeri Nichushkin: 1+ assists NO | 74 | 0.809 | 0.765 | +0.056 | +0.011 | $14.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLAST-26OCT18CBJMIN-CBJCCOYLE3-2|yes; why: higher confidence-adjusted growth (13.19 vs 1.58 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: CBJ offense suppressed (<= 2 goals)
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (13.19 vs 3.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.022); failure: CBJ offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT18CBJMIN-MINQHUGHES43-2|no; why: higher confidence-adjusted growth (1.80 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT18CBJMIN-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: MIN offense succeeds (4+ goals)
- **Valeri Nichushkin: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHL3PTOTAL-26OCT18CBJMIN-3|no; why: higher confidence-adjusted growth (1.50 vs 0.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT18CBJMIN-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3023): highest fidelity KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.3328): highest fidelity KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no (same contract)
- thesis CBJ:SUPPRESSED (p 0.4857): highest fidelity KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no (same contract)
- KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4857, phi -0.228)
- KXNHLGOAL-26OCT18CBJMIN-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4857, phi -0.164)
- KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 33% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.2 pts; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4478, phi -0.318)
- KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3023, phi -0.206)

portfolios: A EV +9.39 (adj +3.47) on $50.00, P(profit) 0.5709, adj growth 26.3 bp · B EV +4.86 (adj +2.24) on $29.31, P(profit) 0.5278, adj growth 19.4 bp · C EV +4.22 (adj +1.83) on $25.60, P(profit) 0.4649, adj growth 15.8 bp · R EV +0.56 (adj +0.39) on $2.00, P(profit) 0.1766, adj growth 13.3 bp

## CAR @ CGY  ·  10000 joint draws  ·  426 bet sides mapped, 18 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_CAR_win | p_overtime | goals | shots CGY/CAR | CGY/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.139 | 0.40 | 0.60 | 0.00 | 6.0 | 22.0/34.8 | 30.6/19.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.45 | 0.55 | 0.49 | 5.85 | 21.9/34.6 | 31.2/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.43 | 0.57 | 0.00 | 5.97 | 27.5/28.4 | 24.5/24.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.090 | 0.36 | 0.64 | 0.00 | 9.18 | 23.3/36.5 | 28.8/18.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.50 | 0.50 | 0.46 | 5.98 | 27.7/28.6 | 25.2/24.4 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.068 | 0.49 | 0.51 | 0.47 | 2.84 | 20.5/33.3 | 31.8/19.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jonathan Castagna: 1+ goals YES | 9 | 0.118 | 0.110 | +0.022 | +0.014 | $3.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Carolina over 3.5 goals scored NO | 49 | 0.579 | 0.529 | +0.072 | +0.022 | $9.19 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 66 | 0.711 | 0.696 | +0.036 | +0.020 | $12.84 | FUNDED_RESEARCH | $4 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Morgan Frost: 1+ goals YES | 23 | 0.263 | 0.254 | +0.021 | +0.011 | $3.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT18CARCGY-CGYYSHARANGOVICH17-2|yes; why: KXNHLPTS-26OCT18CARCGY-CGYYSHARANGOVICH17-2|yes has the higher standalone adjusted growth (7.07 vs 4.94 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.022); relationships: KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: CGY offense suppressed (<= 2 goals)
- **Carolina over 3.5 goals scored NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: REINFORCING (phi 0.226); KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CAR offense succeeds (4+ goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no; why: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no has the higher standalone adjusted growth (8.31 vs 4.15 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.010); relationships: KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: REINFORCING (phi 0.226); KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CAR offense succeeds (4+ goals)
- **Morgan Frost: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT18CARCGY-CGYYSHARANGOVICH17-2|yes; why: Player prop expression KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes selected over player prop KXNHLPTS-26OCT18CARCGY-CGYYSHARANGOVICH17-2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.42 vs 0.23 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CAR:SUPPRESSED (p 0.3691): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no — Broad expression KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CGY:OFFENSE_4PLUS (p 0.3361): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CARCGY-CGY2|yes — Player prop expression KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes selected over player prop KXNHLPTS-26OCT18CARCGY-CGYYSHARANGOVICH17-2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.42 vs 0.23 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)
- thesis CGY:WINS_BY_2PLUS (p 0.2355): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.446, phi -0.149)
- KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4111, phi -0.98)
- KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4111, phi -0.225)
- KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.446, phi -0.262)
- override: Broad expression KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes selected over player prop KXNHLPTS-26OCT18CARCGY-CGYYSHARANGOVICH17-2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.42 vs 0.23 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +8.25 (adj +1.62) on $50.00, P(profit) 0.7039, adj growth 13.5 bp · B EV +3.12 (adj +1.48) on $29.14, P(profit) 0.6115, adj growth 12.9 bp · C EV +5.44 (adj +1.78) on $20.51, P(profit) 0.6822, adj growth 15.4 bp · R EV +0.63 (adj +0.25) on $7.00, P(profit) 0.4626, adj growth 8.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
