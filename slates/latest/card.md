# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-13T18:26:35Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.05 | +28.37 | +7.47 | +27.72 | 0.874 | -3.13 | -10.63 | 71.66 |
| B thesis-diversified (joint) ← optimiser card | 142.34 | +20.48 | +9.61 | +19.95 | 0.819 | -7.48 | -15.12 | 93.60 |
| C best expression per thesis | 149.50 | +21.00 | +8.27 | +20.67 | 0.819 | -8.44 | -15.99 | 80.01 |
| R FUNDED research stakes | 21.00 | +2.20 | +1.28 | +1.73 | 0.609 | -4.82 | -6.26 | 0.00 |

## NJD @ DET  ·  10000 joint draws  ·  422 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.503 / away 0.497

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_NJD_win | p_overtime | goals | shots DET/NJD | DET/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.60 | 0.40 | 0.00 | 5.95 | 28.1/28.3 | 25.3/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.53 | 0.47 | 0.49 | 5.8 | 28.3/28.4 | 25.2/25.1 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.073 | 0.53 | 0.47 | 0.00 | 5.98 | 22.5/33.3 | 29.8/18.8 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.071 | 0.55 | 0.45 | 0.45 | 2.77 | 26.6/27.0 | 25.6/25.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.069 | 0.59 | 0.41 | 0.00 | 3.46 | 26.8/27.1 | 25.4/24.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.47 | 0.53 | 0.49 | 5.76 | 22.4/33.5 | 30.2/19.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nico Hischier: 1+ goals NO | 70 | 0.762 | 0.745 | +0.047 | +0.030 | $3.51 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 74 | 0.790 | 0.775 | +0.037 | +0.022 | $3.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Dylan Larkin: 1+ assists NO | 58 | 0.659 | 0.612 | +0.062 | +0.015 | $1.88 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
| Dylan Larkin: 1+ goals NO | 67 | 0.709 | 0.697 | +0.023 | +0.011 | $1.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Nico Hischier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no; why: higher confidence-adjusted growth (9.94 vs 5.69 bp); relationships: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: NJD offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no; why: Player prop expression KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: NJD offense succeeds (4+ goals)
- **Dylan Larkin: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT13NJDET-4|no; why: KXNHLTOTAL-26OCT13NJDET-4|no has the higher standalone adjusted growth (2.42 vs 2.04 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.176); relationships: KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: DET offense succeeds (4+ goals)
- **Dylan Larkin: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT13NJDET-4|no; why: KXNHLTOTAL-26OCT13NJDET-4|no has the higher standalone adjusted growth (2.42 vs 1.27 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.160); relationships: KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.07.
- thesis NJD:SUPPRESSED (p 0.4877): highest fidelity KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no — Player prop expression KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis DET:WINS (p 0.5528): highest fidelity KXNHLSPREAD-26OCT13NJDET-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:LOW_EVENT (p 0.2976): highest fidelity KXNHLTOTAL-26OCT13NJDET-7|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT13NJDET-7|no (same contract)
- KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.2933, phi -0.233)
- KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.2933, phi -0.243)
- KXNHLAST-26OCT13NJDET-DETDLARKIN71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3637, phi -0.269)
- KXNHLGOAL-26OCT13NJDET-DETDLARKIN71-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3637, phi -0.235)
- override: Player prop expression KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.40 (adj +0.29) on $9.37, P(profit) 0.7075, adj growth 2.9 bp · B EV +0.66 (adj +0.33) on $10.66, P(profit) 0.5416, adj growth 3.2 bp · C EV +0.96 (adj +0.36) on $8.30, P(profit) 0.5183, adj growth 3.5 bp · R EV +0.07 (adj +0.04) on $1.00, P(profit) 0.7617, adj growth 1.7 bp

## FLA @ CBJ  ·  10000 joint draws  ·  416 bet sides mapped, 9 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.546 / away 0.454

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_FLA_win | p_overtime | goals | shots CBJ/FLA | CBJ/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.65 | 0.35 | 0.00 | 6.02 | 27.3/27.0 | 24.1/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.45 | 5.9 | 27.2/27.1 | 23.9/23.9 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.090 | 0.72 | 0.28 | 0.00 | 5.97 | 32.2/21.6 | 19.2/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.68 | 0.32 | 0.00 | 9.21 | 28.8/28.5 | 23.6/21.9 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.58 | 0.42 | 0.49 | 5.89 | 32.4/21.9 | 18.7/29.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.64 | 0.36 | 0.00 | 3.53 | 26.2/26.0 | 24.5/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 69 | 0.755 | 0.738 | +0.050 | +0.033 | $4.68 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 17 | 0.209 | 0.196 | +0.029 | +0.016 | $1.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 23 | 0.273 | 0.260 | +0.030 | +0.017 | $1.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13FLACBJ-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (11.42 vs 5.04 bp); relationships: KXNHLGOAL-26OCT13FLACBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13FLACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: FLA offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13FLACBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (3.69 vs 3.44 bp); despite a smaller raw edge (+0.029 vs +0.030/contract); relationships: KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13FLACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13FLACBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13FLACBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (3.69 vs 3.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT13FLACBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4996): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:OFFENSE_4PLUS (p 0.4413): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13FLACBJ-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS (p 0.6142): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13FLACBJ-FLA2|no (same contract)
- KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2872, phi -0.238)
- KXNHLGOAL-26OCT13FLACBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3401, phi -0.214)
- KXNHLGOAL-26OCT13FLACBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3401, phi -0.224)

portfolios: A EV +1.29 (adj +0.28) on $9.37, P(profit) 0.6761, adj growth 2.7 bp · B EV +0.65 (adj +0.39) on $6.92, P(profit) 0.3386, adj growth 3.8 bp · C EV +0.82 (adj +0.43) on $10.19, P(profit) 0.6959, adj growth 4.2 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.7554, adj growth 3.6 bp

## BUF @ MTL  ·  10000 joint draws  ·  512 bet sides mapped, 4 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.586 / away 0.414

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_BUF_win | p_overtime | goals | shots MTL/BUF | MTL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.62 | 0.38 | 0.00 | 6.04 | 26.9/27.5 | 24.5/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.49 | 5.93 | 26.9/27.5 | 24.2/23.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.100 | 0.54 | 0.46 | 0.00 | 6.0 | 21.8/33.0 | 29.3/18.3 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.54 | 0.46 | 0.46 | 5.88 | 21.4/32.5 | 29.3/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.59 | 0.41 | 0.00 | 9.28 | 28.5/29.0 | 23.6/21.9 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.068 | 0.57 | 0.43 | 0.00 | 9.19 | 23.4/34.7 | 28.8/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Owen Power: 1+ goals NO | 88 | 0.918 | 0.906 | +0.030 | +0.018 | $4.14 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ goals NO | 72 | 0.768 | 0.754 | +0.034 | +0.020 | $3.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 69 | 0.761 | 0.721 | +0.056 | +0.015 | $2.89 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13BUFMTL-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (7.59 vs 0.00 bp); despite a smaller raw edge (+0.030 vs +0.034/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: BUF offense succeeds (4+ goals)
- **Chris Kreider: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13BUFMTL-MTLCCAUFIELD13-1|no; why: higher confidence-adjusted growth (4.66 vs 0.69 bp); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: MTL offense succeeds (4+ goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no has the higher standalone adjusted growth (4.66 vs 2.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT13BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.10.
- thesis MTL:SUPPRESSED (p 0.3452): highest fidelity KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.3343): highest fidelity KXNHLGOAL-26OCT13BUFMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BUFMTL-MTLJEVANS71-1|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.4412): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT13BUFMTL-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3475, phi -0.123)
- KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4323, phi -0.223)
- KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4323, phi -0.198)

portfolios: A EV +0.45 (adj +0.20) on $8.47, P(profit) 0.5377, adj growth 2.0 bp · B EV +0.55 (adj +0.26) on $10.95, P(profit) 0.5377, adj growth 2.5 bp · C EV +0.44 (adj +0.27) on $6.59, P(profit) 0.8058, adj growth 2.6 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.9178, adj growth 1.6 bp

## WSH @ CAR  ·  10000 joint draws  ·  460 bet sides mapped, 8 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.582 / away 0.418

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WSH_win | p_overtime | goals | shots CAR/WSH | CAR/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.155 | 0.65 | 0.35 | 0.00 | 6.03 | 33.4/20.8 | 18.0/28.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.134 | 0.55 | 0.45 | 0.45 | 5.92 | 33.7/21.2 | 17.9/30.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.104 | 0.66 | 0.34 | 0.00 | 9.27 | 35.2/22.4 | 17.7/27.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.092 | 0.57 | 0.43 | 0.00 | 6.02 | 27.9/26.9 | 23.7/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.51 | 0.49 | 0.47 | 5.9 | 27.6/26.7 | 23.5/24.3 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.070 | 0.60 | 0.40 | 0.00 | 3.46 | 32.4/20.1 | 18.6/30.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.223 | 0.208 | +0.043 | +0.028 | $1.84 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Ethen Frank: 1+ goals YES | 9 | 0.124 | 0.115 | +0.029 | +0.019 | $1.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ assists NO | 53 | 0.666 | 0.574 | +0.119 | +0.027 | $3.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CAR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (11.66 vs 2.10 bp); despite a smaller raw edge (+0.043 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13WSHCAR-WSHEFRANK53-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: WSH offense suppressed (<= 2 goals)
- **Ethen Frank: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (11.66 vs 8.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: WSH offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ assists NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13WSHCAR-CARNEHLERS27-1|no; why: higher confidence-adjusted growth (6.42 vs 1.34 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT13WSHCAR-WSHEFRANK53-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.339): highest fidelity KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.3382): highest fidelity KXNHLGOAL-26OCT13WSHCAR-CARNEHLERS27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4482, phi -0.221)
- KXNHLGOAL-26OCT13WSHCAR-WSHEFRANK53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4482, phi -0.186)
- KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.1 pts; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4425, phi -0.247)

portfolios: A EV +1.94 (adj +0.64) on $9.37, P(profit) 0.5122, adj growth 6.1 bp · B EV +1.56 (adj +0.69) on $6.61, P(profit) 0.7699, adj growth 6.7 bp · C EV +1.46 (adj +0.56) on $6.54, P(profit) 0.7373, adj growth 5.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ PHI  ·  10000 joint draws  ·  510 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.517 / away 0.483

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_SEA_win | p_overtime | goals | shots PHI/SEA | PHI/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.54 | 0.46 | 0.00 | 6.01 | 26.7/26.5 | 23.2/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.48 | 5.9 | 26.7/26.6 | 23.4/23.6 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.078 | 0.63 | 0.37 | 0.00 | 5.98 | 31.6/21.0 | 18.2/27.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.56 | 0.44 | 0.00 | 9.12 | 28.4/28.1 | 22.6/22.4 | even strength |
| PHI shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.53 | 0.47 | 0.47 | 5.87 | 31.4/21.5 | 18.3/28.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.52 | 0.48 | 0.00 | 3.5 | 25.3/25.3 | 23.4/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Bobby McMann: 1+ goals NO | 71 | 0.780 | 0.761 | +0.056 | +0.037 | $3.51 | FUNDED_RESEARCH | $1 | SEA:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 10 | 0.143 | 0.131 | +0.037 | +0.025 | $1.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jared McCann: 1+ goals NO | 72 | 0.785 | 0.767 | +0.051 | +0.033 | $3.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 16 | 0.202 | 0.190 | +0.032 | +0.021 | $1.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:WINS_BY_2PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Bobby McMann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (15.14 vs 12.56 bp); relationships: KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: SEA offense succeeds (4+ goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (13.72 vs 1.85 bp); despite a smaller raw edge (+0.037 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: SEA offense suppressed (<= 2 goals)
- **Jared McCann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no has the higher standalone adjusted growth (15.14 vs 12.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: SEA offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI wins by 2+; alternative: KXNHLPTS-26OCT13SEAPHI-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (6.58 vs 0.00 bp); despite a smaller raw edge (+0.032 vs +0.059/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, PHI shot control · normal event (5-7) · decided (2+) 0.08.
- thesis SEA:SUPPRESSED (p 0.4596): highest fidelity KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.3043): highest fidelity KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes (same contract)
- thesis PHI:SUPPRESSED (p 0.4097): highest fidelity KXNHLGOAL-26OCT13SEAPHI-PHIPMARTONE94-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13SEAPHI-PHIPMARTONE94-1|no (same contract)
- KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.324, phi -0.211)
- KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4596, phi -0.194)
- KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.324, phi -0.214)
- KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4097, phi -0.222)

portfolios: A EV +1.04 (adj +0.38) on $9.38, P(profit) 0.7058, adj growth 3.7 bp · B EV +1.25 (adj +0.83) on $9.75, P(profit) 0.3118, adj growth 8.1 bp · C EV +1.14 (adj +0.62) on $13.84, P(profit) 0.3858, adj growth 6.0 bp · R EV +0.08 (adj +0.05) on $1.00, P(profit) 0.7802, adj growth 2.0 bp

## TBL @ NYR  ·  10000 joint draws  ·  462 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.409 / away 0.591

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_TBL_win | p_overtime | goals | shots NYR/TBL | NYR/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.56 | 0.44 | 0.00 | 5.99 | 25.9/26.4 | 23.3/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.45 | 5.91 | 25.8/26.4 | 23.3/22.4 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.103 | 0.47 | 0.53 | 0.00 | 6.01 | 20.5/31.3 | 27.3/17.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.45 | 0.55 | 0.48 | 5.83 | 20.6/31.6 | 28.1/17.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.58 | 0.42 | 0.00 | 9.27 | 27.5/28.0 | 22.6/20.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.51 | 0.49 | 0.00 | 3.44 | 24.8/25.2 | 23.2/22.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York R wins by over 1.5 goals YES | 21 | 0.290 | 0.248 | +0.069 | +0.026 | $1.08 | FUNDED_RESEARCH | $1 | NYR:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vladislav Gavrikov: 1+ assists YES | 23 | 0.317 | 0.269 | +0.075 | +0.026 | $1.63 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Tampa Bay over 4.5 goals scored NO | 75 | 0.824 | 0.784 | +0.060 | +0.021 | $4.33 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ goals NO | 63 | 0.676 | 0.663 | +0.029 | +0.017 | $1.62 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **New York R wins by over 1.5 goals YES** — thesis: NYR wins by 2+; alternative: KXNHLSPREAD-26OCT13TBNYR-TB3|no; why: Broad expression KXNHLSPREAD-26OCT13TBNYR-NYR2|yes selected over player prop KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.62 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes: REINFORCING (phi 0.153); KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no: REINFORCING (phi 0.275); KXNHLGOAL-26OCT13TBNYR-TBNKUCHEROV86-1|no: REINFORCING (phi 0.175); failure: TBL wins (incl. OT/SO)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes; why: KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes has the higher standalone adjusted growth (11.40 vs 8.11 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.037); relationships: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: REINFORCING (phi 0.153); KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13TBNYR-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: NYR offense suppressed (<= 2 goals)
- **Tampa Bay over 4.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no selected over player prop KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: REINFORCING (phi 0.275); KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13TBNYR-TBNKUCHEROV86-1|no: REINFORCING (phi 0.211); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: Player prop expression KXNHLGOAL-26OCT13TBNYR-TBNKUCHEROV86-1|no selected over broad KXNHLSPREAD-26OCT13TBNYR-TB3|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.77 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: REINFORCING (phi 0.175); KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no: REINFORCING (phi 0.211); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis NYR:OFFENSE_4PLUS (p 0.3635): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [DIRECT], best adjusted EV KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes — Broad expression KXNHLSPREAD-26OCT13TBNYR-NYR2|yes selected over player prop KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.62 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis TBL:SUPPRESSED (p 0.4344): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no — Broad expression KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no selected over player prop KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYR:WINS_BY_2PLUS (p 0.2901): highest fidelity KXNHLSPREAD-26OCT13TBNYR-NYR2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13TBNYR-NYR2|yes (same contract)
- KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS (p 0.4898, phi -0.626)
- KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4186, phi -0.261)
- KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3373, phi -0.649)
- KXNHLGOAL-26OCT13TBNYR-TBNKUCHEROV86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3373, phi -0.252)
- override: Player prop expression KXNHLGOAL-26OCT13TBNYR-TBNKUCHEROV86-1|no selected over broad KXNHLSPREAD-26OCT13TBNYR-TB3|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.77 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no selected over player prop KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26OCT13TBNYR-NYR2|yes selected over player prop KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.62 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.27 (adj +0.34) on $9.37, P(profit) 0.5764, adj growth 3.2 bp · B EV +1.26 (adj +0.47) on $8.67, P(profit) 0.4529, adj growth 4.5 bp · C EV +1.57 (adj +0.58) on $8.48, P(profit) 0.4205, adj growth 5.6 bp · R EV +0.51 (adj +0.20) on $4.00, P(profit) 0.6525, adj growth 7.3 bp

## STL @ OTT  ·  10000 joint draws  ·  452 bet sides mapped, 8 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_STL_win | p_overtime | goals | shots OTT/STL | OTT/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.51 | 0.49 | 0.00 | 6.07 | 26.7/26.2 | 22.9/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.49 | 0.51 | 0.48 | 5.88 | 26.6/26.1 | 22.9/23.3 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.107 | 0.59 | 0.41 | 0.00 | 5.98 | 31.8/20.9 | 17.9/27.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.56 | 0.44 | 0.47 | 5.9 | 31.9/20.9 | 17.8/28.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.46 | 0.54 | 0.00 | 9.25 | 28.0/27.6 | 21.5/22.2 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.071 | 0.63 | 0.37 | 0.00 | 9.16 | 33.4/22.0 | 17.2/26.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Michael Amadio: 1+ goals YES | 13 | 0.176 | 0.164 | +0.038 | +0.026 | $1.71 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 71 | 0.842 | 0.753 | +0.117 | +0.028 | $4.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Tim Stutzle: 1+ assists NO | 51 | 0.605 | 0.555 | +0.077 | +0.028 | $3.01 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13STLOTT-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (11.87 vs 0.91 bp); alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no: INTENTIONAL_DIVERSIFIER (phi -0.068); failure: OTT offense suppressed (<= 2 goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (8.93 vs 6.62 bp); relationships: KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.067); failure: OTT offense succeeds (4+ goals)
- **Tim Stutzle: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13STLOTT-OTTABURAKOVSKY95-1|no; why: higher confidence-adjusted growth (6.62 vs 0.37 bp); despite a smaller raw edge (+0.077 vs +0.122/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.067); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.3804): highest fidelity KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3905): highest fidelity KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3574): highest fidelity KXNHLGOAL-26OCT13STLOTT-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13STLOTT-STLRTHOMAS18-1|yes (same contract)
- KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3905, phi -0.204)
- KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3804, phi -0.19)
- KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3804, phi -0.282)

portfolios: A EV +1.55 (adj +0.56) on $9.38, P(profit) 0.5223, adj growth 5.5 bp · B EV +1.57 (adj +0.63) on $8.74, P(profit) 0.6196, adj growth 6.2 bp · C EV +1.84 (adj +0.76) on $11.79, P(profit) 0.6178, adj growth 7.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ NYI  ·  10000 joint draws  ·  414 bet sides mapped, 14 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.652 / away 0.348

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_VAN_win | p_overtime | goals | shots NYI/VAN | NYI/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NYI shot control · normal event (5-7) · decided (2+) | 0.126 | 0.68 | 0.32 | 0.00 | 6.02 | 32.8/21.2 | 18.5/28.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.63 | 0.37 | 0.00 | 5.99 | 27.4/26.9 | 23.8/23.4 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.55 | 0.45 | 0.49 | 5.92 | 33.2/21.5 | 18.3/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.51 | 0.49 | 0.47 | 5.9 | 27.7/27.2 | 24.0/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.63 | 0.37 | 0.00 | 9.22 | 29.2/28.5 | 23.2/22.4 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.080 | 0.71 | 0.29 | 0.00 | 9.2 | 34.8/22.8 | 18.4/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 13 | 0.185 | 0.169 | +0.047 | +0.031 | $1.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Bo Horvat: 1+ goals NO | 61 | 0.663 | 0.648 | +0.036 | +0.022 | $3.34 | FUNDED_RESEARCH | $1 | NYI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Kyle Palmieri: 1+ goals NO | 70 | 0.747 | 0.734 | +0.032 | +0.019 | $3.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT13VANNYI-NYI3|no; why: higher confidence-adjusted growth (17.28 vs 3.15 bp); despite a smaller raw edge (+0.047 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: VAN offense suppressed (<= 2 goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no; why: higher confidence-adjusted growth (4.45 vs 3.86 bp); relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: NYI offense succeeds (4+ goals)
- **Kyle Palmieri: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no; why: Player prop expression KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIBHORVAT14-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.87 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: NYI offense succeeds (4+ goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:SUPPRESSED (p 0.3313): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no — Player prop expression KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIBHORVAT14-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.87 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VAN:OFFENSE_4PLUS (p 0.3174): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT13VANNYI-NYI3|no (same contract)
- thesis GAME:TIGHT (p 0.4291): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13VANNYI-NYI3|no (same contract)
- KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.465, phi -0.202)
- KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.4506, phi -0.264)
- KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.4506, phi -0.206)
- override: Player prop expression KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIBHORVAT14-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.87 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.09 (adj +0.24) on $9.37, P(profit) 0.6974, adj growth 2.3 bp · B EV +1.01 (adj +0.64) on $8.94, P(profit) 0.5873, adj growth 6.2 bp · C EV +0.81 (adj +0.29) on $9.23, P(profit) 0.6678, adj growth 2.8 bp · R EV +0.06 (adj +0.03) on $1.00, P(profit) 0.6629, adj growth 1.3 bp

## PIT @ CHI  ·  10000 joint draws  ·  432 bet sides mapped, 14 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.410 / away 0.590

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_PIT_win | p_overtime | goals | shots CHI/PIT | CHI/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.43 | 0.57 | 0.00 | 5.98 | 26.7/27.2 | 23.3/23.5 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.112 | 0.37 | 0.63 | 0.00 | 5.99 | 21.2/32.6 | 28.3/18.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.50 | 0.50 | 0.47 | 5.94 | 26.9/27.4 | 24.0/23.6 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.43 | 0.57 | 0.48 | 5.9 | 21.5/33.0 | 29.4/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.46 | 0.54 | 0.00 | 9.28 | 28.2/28.8 | 22.3/22.3 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.080 | 0.36 | 0.64 | 0.00 | 9.35 | 22.8/34.5 | 27.1/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 13 | 0.191 | 0.173 | +0.053 | +0.035 | $2.09 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 52 | 0.713 | 0.581 | +0.175 | +0.043 | $3.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Connor Bedard: 1+ assists NO | 53 | 0.709 | 0.586 | +0.162 | +0.039 | $3.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes; why: higher confidence-adjusted growth (22.22 vs 4.01 bp); despite a smaller raw edge (+0.053 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.037); KXNHLAST-26OCT13PITCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.134); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13PITCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (16.61 vs 13.26 bp); relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLAST-26OCT13PITCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.072); failure: CHI offense succeeds (4+ goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no; why: second expression of the same thesis: KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no has the higher standalone adjusted growth (16.61 vs 13.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.072); they share one thesis budget; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.134); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.072); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.3626): highest fidelity KXNHLAST-26OCT13PITCHI-CHITBERTUZZI59-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4227): highest fidelity KXNHLGOAL-26OCT13PITCHI-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.436): highest fidelity KXNHLAST-26OCT13PITCHI-PITECHINAKHOV59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4227, phi -0.226)
- KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.2 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3626, phi -0.245)
- KXNHLAST-26OCT13PITCHI-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.9 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3626, phi -0.237)

portfolios: A EV +2.67 (adj +0.49) on $9.37, P(profit) 0.581, adj growth 4.7 bp · B EV +2.98 (adj +1.06) on $9.11, P(profit) 0.6332, adj growth 10.4 bp · C EV +3.34 (adj +1.32) on $11.31, P(profit) 0.6297, adj growth 12.7 bp · R EV +0.38 (adj +0.26) on $1.00, P(profit) 0.1908, adj growth 9.6 bp

## MIN @ WPG  ·  10000 joint draws  ·  404 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_MIN_win | p_overtime | goals | shots WPG/MIN | WPG/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.54 | 0.46 | 0.00 | 5.99 | 28.2/28.1 | 24.7/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.47 | 5.88 | 28.3/28.4 | 25.1/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.55 | 0.45 | 0.00 | 9.28 | 30.0/30.0 | 24.2/23.6 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.070 | 0.56 | 0.44 | 0.00 | 5.98 | 33.1/22.4 | 19.2/29.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.070 | 0.45 | 0.55 | 0.00 | 5.96 | 22.7/33.4 | 29.5/19.5 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.45 | 0.55 | 0.47 | 5.83 | 22.4/32.9 | 29.4/19.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Neal Pionk: 1+ goals NO | 86 | 0.932 | 0.913 | +0.064 | +0.044 | $4.68 | FUNDED_RESEARCH | $2 | WPG:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Rieger Lorenz: 1+ goals YES | 10 | 0.135 | 0.125 | +0.029 | +0.019 | $1.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 59 | 0.646 | 0.631 | +0.040 | +0.024 | $4.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 23 | 0.305 | 0.260 | +0.063 | +0.018 | $1.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13MINWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (39.23 vs 0.64 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense succeeds (4+ goals)
- **Rieger Lorenz: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (8.10 vs 3.71 bp); despite a smaller raw edge (+0.029 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no; why: higher confidence-adjusted growth (5.35 vs 3.21 bp); relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.19); failure: MIN offense succeeds (4+ goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13MINWPG-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (3.71 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.19); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.4173): highest fidelity KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.3661): highest fidelity KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes (same contract)
- thesis WPG:SUPPRESSED (p 0.3874): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3878, phi -0.116)
- KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4173, phi -0.146)
- KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3661, phi -0.304)
- KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4173, phi -0.274)

portfolios: A EV +1.16 (adj +0.43) on $9.37, P(profit) 0.6004, adj growth 4.2 bp · B EV +1.34 (adj +0.73) on $11.71, P(profit) 0.7842, adj growth 7.1 bp · C EV +0.94 (adj +0.42) on $12.49, P(profit) 0.7747, adj growth 4.1 bp · R EV +0.15 (adj +0.10) on $2.00, P(profit) 0.9322, adj growth 4.1 bp

## COL @ DAL  ·  10000 joint draws  ·  406 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.516 / away 0.484

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_COL_win | p_overtime | goals | shots DAL/COL | DAL/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.46 | 0.54 | 0.00 | 6.0 | 26.8/27.2 | 23.6/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.48 | 5.9 | 26.9/27.4 | 24.2/23.5 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.101 | 0.40 | 0.60 | 0.00 | 6.01 | 21.2/32.7 | 28.7/18.2 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.44 | 0.56 | 0.48 | 5.88 | 21.5/32.8 | 29.3/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.45 | 0.55 | 0.00 | 9.29 | 28.4/28.9 | 22.6/22.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.067 | 0.41 | 0.59 | 0.00 | 9.18 | 22.7/34.3 | 27.4/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zachary L'Heureux: 1+ goals YES | 9 | 0.136 | 0.122 | +0.040 | +0.026 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 20 | 0.256 | 0.241 | +0.045 | +0.030 | $2.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Parker Kelly: 1+ goals YES | 9 | 0.127 | 0.116 | +0.031 | +0.021 | $1.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 59 | 0.630 | 0.619 | +0.023 | +0.012 | $1.78 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Zachary L'Heureux: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (16.47 vs 11.33 bp); despite a smaller raw edge (+0.040 vs +0.045/contract); relationships: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13COLDAL-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: COL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (11.33 vs 2.08 bp); relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13COLDAL-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: COL offense suppressed (<= 2 goals)
- **Parker Kelly: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (11.33 vs 10.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: COL offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no; why: Player prop expression KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.81 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT13COLDAL-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: COL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4057): highest fidelity KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.3802): highest fidelity KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no (same contract)
- thesis DAL:SUPPRESSED (p 0.4216): highest fidelity KXNHLAST-26OCT13COLDAL-DALRHINTZ24-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13COLDAL-DALRHINTZ24-1|no (same contract)
- KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3802, phi -0.18)
- KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3802, phi -0.232)
- KXNHLGOAL-26OCT13COLDAL-COLPKELLY17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3802, phi -0.164)
- KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4057, phi -0.286)
- override: Player prop expression KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.81 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.78 (adj +0.86) on $9.37, P(profit) 0.6785, adj growth 8.4 bp · B EV +1.51 (adj +0.98) on $6.53, P(profit) 0.4386, adj growth 9.5 bp · C EV +1.33 (adj +0.55) on $9.30, P(profit) 0.6234, adj growth 5.3 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6302, adj growth 0.7 bp

## VGK @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 8 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.464 / away 0.536

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_VGK_win | p_overtime | goals | shots NSH/VGK | NSH/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.53 | 0.47 | 0.00 | 6.02 | 27.5/28.0 | 24.5/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.48 | 5.87 | 27.7/28.2 | 24.9/24.5 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.105 | 0.47 | 0.53 | 0.00 | 5.97 | 22.1/33.5 | 29.9/18.9 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.47 | 0.53 | 0.47 | 5.89 | 22.1/33.3 | 29.8/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.55 | 0.45 | 0.00 | 9.37 | 29.2/29.5 | 23.8/22.6 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.060 | 0.48 | 0.52 | 0.00 | 9.18 | 23.8/35.0 | 28.2/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 71 | 0.762 | 0.746 | +0.037 | +0.022 | $4.08 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ goals NO | 68 | 0.726 | 0.712 | +0.030 | +0.017 | $2.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Shea Theodore: 1+ assists YES | 29 | 0.350 | 0.315 | +0.046 | +0.011 | $1.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13VGKNSH-VGKTCONNELLY24-1|no; why: higher confidence-adjusted growth (5.23 vs 5.05 bp); despite a smaller raw edge (+0.037 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.101); failure: VGK offense succeeds (4+ goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no; why: Player prop expression KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.86 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: VGK offense succeeds (4+ goals)
- **Shea Theodore: 1+ assists YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13VGKNSH-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (1.21 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0005 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.101); KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.4121): highest fidelity KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no — Player prop expression KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.86 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VGK:OFFENSE_4PLUS (p 0.3696): highest fidelity KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes (same contract)
- KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3696, phi -0.231)
- KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3696, phi -0.24)
- KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.4121, phi -0.284)
- override: Player prop expression KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.86 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.34 (adj +0.27) on $9.37, P(profit) 0.7166, adj growth 2.6 bp · B EV +0.51 (adj +0.23) on $8.19, P(profit) 0.6394, adj growth 2.3 bp · C EV +0.47 (adj +0.21) on $6.77, P(profit) 0.7616, adj growth 2.0 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7616, adj growth 2.3 bp

## TOR @ UTA  ·  10000 joint draws  ·  444 bet sides mapped, 7 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.591 / away 0.409

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TOR_win | p_overtime | goals | shots UTA/TOR | UTA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| UTA shot control · normal event (5-7) · decided (2+) | 0.140 | 0.68 | 0.32 | 0.00 | 6.02 | 34.5/21.9 | 19.3/29.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.57 | 0.43 | 0.49 | 5.95 | 34.7/22.1 | 18.9/31.1 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.106 | 0.71 | 0.29 | 0.00 | 9.33 | 36.2/23.3 | 18.7/27.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.63 | 0.37 | 0.00 | 6.03 | 28.6/27.7 | 24.6/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.54 | 0.46 | 0.47 | 5.97 | 28.7/27.8 | 24.6/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.61 | 0.39 | 0.00 | 9.32 | 30.3/29.3 | 23.8/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vincent Trocheck: 1+ assists NO | 70 | 0.788 | 0.739 | +0.073 | +0.024 | $3.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Dylan Guenther: 1+ goals NO | 61 | 0.669 | 0.653 | +0.042 | +0.026 | $3.11 | FUNDED_RESEARCH | $1 | UTA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Kirill Marchenko: 1+ assists NO | 64 | 0.717 | 0.676 | +0.060 | +0.020 | $3.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (6.43 vs 6.37 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: UTA offense succeeds (4+ goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13TORUTA-UTALCOOLEY92-1|no; why: higher confidence-adjusted growth (6.37 vs 0.13 bp); alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: UTA offense succeeds (4+ goals)
- **Kirill Marchenko: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TORUTA-TORJTAVARES91-1|no; why: higher confidence-adjusted growth (3.75 vs 3.50 bp); relationships: KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: TOR offense succeeds (4+ goals)

**Review**: scripts UTA shot control · normal event (5-7) · decided (2+) 0.14, UTA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · high event (8+) · decided (2+) 0.11.
- thesis UTA:SUPPRESSED (p 0.3113): highest fidelity KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no (same contract)
- thesis TOR:SUPPRESSED (p 0.4531): highest fidelity KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no (same contract)
- thesis TOR:OFFENSE_4PLUS (p 0.3266): highest fidelity KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes (same contract)
- KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4845, phi -0.189)
- KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4845, phi -0.243)
- KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3266, phi -0.25)

portfolios: A EV +1.00 (adj +0.28) on $9.37, P(profit) 0.6837, adj growth 2.7 bp · B EV +0.90 (adj +0.36) on $10.18, P(profit) 0.7135, adj growth 3.5 bp · C EV +1.01 (adj +0.40) on $10.38, P(profit) 0.6149, adj growth 3.9 bp · R EV +0.07 (adj +0.04) on $1.00, P(profit) 0.6686, adj growth 1.6 bp

## CGY @ ANA  ·  10000 joint draws  ·  406 bet sides mapped, 6 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.609 / away 0.391

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_CGY_win | p_overtime | goals | shots ANA/CGY | ANA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.132 | 0.72 | 0.28 | 0.00 | 6.0 | 34.5/22.4 | 19.9/29.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.69 | 0.31 | 0.00 | 6.0 | 29.6/28.8 | 26.2/25.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.55 | 0.45 | 0.44 | 5.96 | 35.1/22.8 | 19.7/31.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.52 | 0.48 | 0.49 | 5.96 | 29.2/28.5 | 25.1/25.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.092 | 0.75 | 0.25 | 0.00 | 9.3 | 36.4/23.8 | 19.6/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.69 | 0.31 | 0.00 | 9.37 | 30.9/30.0 | 24.8/23.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jeff Malott: 1+ goals YES | 9 | 0.140 | 0.125 | +0.044 | +0.029 | $1.66 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 11 | 0.149 | 0.137 | +0.032 | +0.020 | $1.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (20.45 vs 6.20 bp); despite a smaller raw edge (+0.044 vs +0.103/contract); relationships: KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: ANA offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (8.25 vs 6.20 bp); despite a smaller raw edge (+0.032 vs +0.103/contract); relationships: KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.497): highest fidelity KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes — Player prop expression KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes selected over player prop KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-2|yes because adjusted EV is 0.9 pts higher while thesis capture is 0.38 vs 0.16 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.147)
- KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.137)
- override: Player prop expression KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes selected over player prop KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-2|yes because adjusted EV is 0.9 pts higher while thesis capture is 0.38 vs 0.16 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.90 (adj +1.32) on $9.38, P(profit) 0.6546, adj growth 12.4 bp · B EV +1.10 (adj +0.71) on $2.89, P(profit) 0.2687, adj growth 6.9 bp · C EV +0.76 (adj +0.15) on $1.25, P(profit) 0.2721, adj growth 1.4 bp · R EV +0.46 (adj +0.30) on $1.00, P(profit) 0.1395, adj growth 11.0 bp

## EDM @ LAK  ·  10000 joint draws  ·  422 bet sides mapped, 9 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.457 / away 0.543

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_EDM_win | p_overtime | goals | shots LAK/EDM | LAK/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.47 | 0.53 | 0.00 | 6.01 | 27.8/27.9 | 24.2/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.51 | 0.49 | 0.48 | 5.91 | 28.1/28.1 | 24.7/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.45 | 0.55 | 0.00 | 9.36 | 29.4/29.4 | 22.9/23.7 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.077 | 0.43 | 0.57 | 0.00 | 6.02 | 22.2/33.1 | 29.0/19.2 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.46 | 0.54 | 0.48 | 5.96 | 22.3/33.1 | 29.6/19.1 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.059 | 0.54 | 0.46 | 0.00 | 6.03 | 32.6/22.2 | 19.1/28.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Artemi Panarin: 2+ assists NO | 82 | 0.910 | 0.862 | +0.080 | +0.032 | $4.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Kasperi Kapanen: 1+ goals NO | 79 | 0.835 | 0.822 | +0.033 | +0.021 | $4.29 | FUNDED_RESEARCH | $2 | EDM:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 48 | 0.613 | 0.523 | +0.115 | +0.026 | $2.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Artemi Panarin: 2+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (16.26 vs 5.80 bp); despite a smaller raw edge (+0.080 vs +0.115/contract); relationships: KXNHLGOAL-26OCT13EDMLA-EDMKKAPANEN42-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: DUPLICATIVE (phi 0.396); failure: LAK offense succeeds (4+ goals)
- **Kasperi Kapanen: 1+ goals NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (5.97 vs 2.70 bp); despite a smaller raw edge (+0.033 vs +0.133/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: EDM offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no; why: second expression of the same thesis: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no has the higher standalone adjusted growth (16.26 vs 5.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.396); they share one thesis budget; relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: DUPLICATIVE (phi 0.396); KXNHLGOAL-26OCT13EDMLA-EDMKKAPANEN42-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4138): highest fidelity KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.395): highest fidelity KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes — Player prop expression KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.50 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis EDM:SUPPRESSED (p 0.3893): highest fidelity KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3679, phi -0.251)
- KXNHLGOAL-26OCT13EDMLA-EDMKKAPANEN42-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.395, phi -0.184)
- KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.8 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3679, phi -0.265)
- override: Player prop expression KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.50 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.97 (adj +0.40) on $9.37, P(profit) 0.6254, adj growth 3.6 bp · B EV +1.10 (adj +0.39) on $10.78, P(profit) 0.5115, adj growth 3.8 bp · C EV +1.58 (adj +0.41) on $9.20, P(profit) 0.6455, adj growth 4.1 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.8348, adj growth 2.0 bp

## BOS @ SJS  ·  10000 joint draws  ·  418 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.467 / away 0.533

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_BOS_win | p_overtime | goals | shots SJS/BOS | SJS/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.50 | 0.50 | 0.00 | 6.03 | 27.3/27.3 | 23.8/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.46 | 5.96 | 27.4/27.4 | 24.1/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.50 | 0.50 | 0.00 | 9.36 | 28.9/28.9 | 22.7/22.9 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.074 | 0.56 | 0.44 | 0.00 | 6.01 | 32.2/21.5 | 18.4/28.2 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.061 | 0.59 | 0.41 | 0.00 | 9.35 | 33.9/23.2 | 17.8/27.1 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.49 | 0.51 | 0.47 | 5.95 | 32.0/21.6 | 18.4/28.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kiefer Sherwood: 1+ goals YES | 16 | 0.213 | 0.197 | +0.044 | +0.028 | $1.75 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Charlie McAvoy: 1+ assists NO | 55 | 0.710 | 0.603 | +0.143 | +0.035 | $4.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Collin Graf: 1+ goals YES | 14 | 0.182 | 0.170 | +0.034 | +0.022 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 69 | 0.816 | 0.731 | +0.111 | +0.026 | $4.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13BOSSJ-SJCGRAF51-1|yes; why: higher confidence-adjusted growth (12.00 vs 8.07 bp); relationships: KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT13BOSSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT13BOSSJ-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.141); failure: SJS offense suppressed (<= 2 goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (11.28 vs 5.94 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT13BOSSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT13BOSSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: BOS offense succeeds (4+ goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes has the higher standalone adjusted growth (12.00 vs 8.07 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT13BOSSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.031); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no; why: higher confidence-adjusted growth (7.12 vs 4.31 bp); relationships: KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.141); KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT13BOSSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.031); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4114): highest fidelity KXNHLAST-26OCT13BOSSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.3799): highest fidelity KXNHLAST-26OCT13BOSSJ-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.3757): highest fidelity KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no (same contract)
- KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3757, phi -0.21)
- KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.5 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4054, phi -0.248)
- KXNHLGOAL-26OCT13BOSSJ-SJCGRAF51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3757, phi -0.19)
- KXNHLAST-26OCT13BOSSJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.1 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4114, phi -0.209)

portfolios: A EV +2.54 (adj +0.49) on $9.37, P(profit) 0.6742, adj growth 4.7 bp · B EV +2.52 (adj +0.91) on $11.71, P(profit) 0.7246, adj growth 8.9 bp · C EV +2.53 (adj +0.94) on $13.84, P(profit) 0.696, adj growth 9.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
