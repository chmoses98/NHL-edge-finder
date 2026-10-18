# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T14:24:20Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 89.78 | +16.85 | +4.54 | +9.10 | 0.531 | -50.75 | -72.04 | 30.44 |
| B thesis-diversified (joint) ← optimiser card | 43.51 | +6.42 | +2.76 | +7.55 | 0.551 | -25.16 | -30.70 | 24.05 |
| C best expression per thesis | 15.55 | +4.37 | +1.61 | -1.91 | 0.372 | -15.55 | -15.55 | 14.01 |
| R FUNDED research stakes | 9.00 | +1.20 | +0.57 | +2.83 | 0.557 | -9.00 | -9.00 | 0.00 |

## CBJ @ MIN  ·  10000 joint draws  ·  428 bet sides mapped, 3 +EV candidates, 3 on card


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
| Mathieu Olivier: 1+ goals YES | 13 | 0.177 | 0.159 | +0.039 | +0.021 | $5.42 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 20 | 0.238 | 0.224 | +0.027 | +0.012 | $3.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ assists NO | 33 | 0.432 | 0.359 | +0.086 | +0.014 | $4.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.67) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT18CBJMIN-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (7.83 vs 2.02 bp); relationships: KXNHLGOAL-26OCT18CBJMIN-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (7.83 vs 2.02 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: CBJ offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-2|no; why: higher confidence-adjusted growth (1.80 vs 0.79 bp); alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT18CBJMIN-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3023): highest fidelity KXNHLGOAL-26OCT18CBJMIN-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3328): highest fidelity KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no (same contract)
- KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4857, phi -0.228)
- KXNHLGOAL-26OCT18CBJMIN-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4857, phi -0.24)
- KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 33% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.2 pts; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4478, phi -0.318)

portfolios: A EV +9.24 (adj +2.99) on $39.78, P(profit) 0.6421, adj growth 19.5 bp · B EV +3.18 (adj +1.22) on $13.88, P(profit) 0.3733, adj growth 10.6 bp · C EV +2.70 (adj +1.00) on $10.12, P(profit) 0.5297, adj growth 8.7 bp · R EV +0.56 (adj +0.30) on $2.00, P(profit) 0.1766, adj growth 9.7 bp

## CAR @ CGY  ·  10000 joint draws  ·  418 bet sides mapped, 12 +EV candidates, 4 on card


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
| Carolina over 3.5 goals scored NO | 49 | 0.579 | 0.532 | +0.072 | +0.025 | $10.54 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jonathan Castagna: 1+ goals YES | 9 | 0.118 | 0.110 | +0.022 | +0.014 | $3.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 66 | 0.711 | 0.696 | +0.036 | +0.020 | $12.40 | FUNDED_RESEARCH | $4 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Morgan Frost: 1+ goals YES | 23 | 0.263 | 0.253 | +0.021 | +0.010 | $3.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Carolina over 3.5 goals scored NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes has the higher standalone adjusted growth (6.09 vs 5.28 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.399); relationships: KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: REINFORCING (phi 0.226); KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CAR offense succeeds (4+ goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes has the higher standalone adjusted growth (6.09 vs 4.94 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.093); relationships: KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: CGY offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes has the higher standalone adjusted growth (6.09 vs 4.15 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.145); relationships: KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: REINFORCING (phi 0.226); KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CAR offense succeeds (4+ goals)
- **Morgan Frost: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: Player prop expression KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes selected over broad KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.42 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CGY:WINS_BY_2PLUS (p 0.2355): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.3691): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3361): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CARCGY-CGY2|yes — Player prop expression KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes selected over broad KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.42 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4111, phi -0.98)
- KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.446, phi -0.149)
- KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4111, phi -0.225)
- KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.446, phi -0.262)
- override: Player prop expression KXNHLGOAL-26OCT18CARCGY-CGYMFROST16-1|yes selected over broad KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.42 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.61 (adj +1.55) on $50.00, P(profit) 0.6301, adj growth 10.9 bp · B EV +3.25 (adj +1.54) on $29.63, P(profit) 0.6115, adj growth 13.4 bp · C EV +1.68 (adj +0.61) on $5.43, P(profit) 0.2355, adj growth 5.3 bp · R EV +0.63 (adj +0.27) on $7.00, P(profit) 0.4626, adj growth 9.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
