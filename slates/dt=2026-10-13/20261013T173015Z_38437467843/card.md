# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-13T17:30:15Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.03 | +28.76 | +7.77 | +27.81 | 0.875 | -3.28 | -11.79 | 74.52 |
| B thesis-diversified (joint) ← optimiser card | 142.88 | +19.50 | +9.21 | +18.67 | 0.812 | -7.60 | -15.16 | 89.51 |
| C best expression per thesis | 147.66 | +20.44 | +8.07 | +19.85 | 0.806 | -8.92 | -16.81 | 77.72 |
| R FUNDED research stakes | 22.00 | +2.15 | +1.26 | +1.00 | 0.566 | -4.47 | -5.94 | 0.00 |

## NJD @ DET  ·  10000 joint draws  ·  416 bet sides mapped, 16 +EV candidates, 4 on card

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
| Timo Meier: 1+ goals NO | 74 | 0.790 | 0.777 | +0.037 | +0.023 | $3.39 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Nico Hischier: 1+ goals NO | 71 | 0.762 | 0.748 | +0.037 | +0.023 | $3.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Viktor Arvidsson: 1+ assists NO | 62 | 0.730 | 0.652 | +0.093 | +0.015 | $2.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Dylan Larkin: 1+ assists NO | 58 | 0.659 | 0.610 | +0.062 | +0.012 | $1.38 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no; why: Player prop expression KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26OCT13NJDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: NJD offense succeeds (4+ goals)
- **Nico Hischier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no has the higher standalone adjusted growth (6.36 vs 5.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26OCT13NJDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: NJD offense succeeds (4+ goals)
- **Viktor Arvidsson: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT13NJDET-4|no; why: KXNHLTOTAL-26OCT13NJDET-4|no has the higher standalone adjusted growth (2.42 vs 2.26 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.150); relationships: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.093); failure: DET offense succeeds (4+ goals)
- **Dylan Larkin: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT13NJDET-4|no; why: KXNHLTOTAL-26OCT13NJDET-4|no has the higher standalone adjusted growth (2.42 vs 1.41 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.176); relationships: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT13NJDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi 0.093); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.07.
- thesis NJD:SUPPRESSED (p 0.4877): highest fidelity KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis DET:WINS (p 0.5528): highest fidelity KXNHLSPREAD-26OCT13NJDET-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:LOW_EVENT (p 0.2976): highest fidelity KXNHLTOTAL-26OCT13NJDET-7|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT13NJDET-7|no (same contract)
- KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.2933, phi -0.243)
- KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.2933, phi -0.233)
- KXNHLAST-26OCT13NJDET-DETVARVIDSSON33-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3637, phi -0.226)
- KXNHLAST-26OCT13NJDET-DETDLARKIN71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3637, phi -0.269)
- override: Player prop expression KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.46 (adj +0.30) on $9.37, P(profit) 0.7343, adj growth 2.9 bp · B EV +0.79 (adj +0.29) on $10.24, P(profit) 0.6172, adj growth 2.9 bp · C EV +0.93 (adj +0.31) on $8.56, P(profit) 0.5194, adj growth 3.0 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.7905, adj growth 1.2 bp

## FLA @ CBJ  ·  10000 joint draws  ·  410 bet sides mapped, 11 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.543 / away 0.457

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
| Sam Reinhart: 1+ goals NO | 69 | 0.755 | 0.738 | +0.050 | +0.033 | $4.49 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Sandis Vilmanis: 1+ goals YES | 9 | 0.128 | 0.117 | +0.032 | +0.021 | $1.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 75 | 0.814 | 0.780 | +0.051 | +0.017 | $3.67 | FUNDED_RESEARCH | $1 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13FLACBJ-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (11.42 vs 4.47 bp); relationships: KXNHLGOAL-26OCT13FLACBJ-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT13FLACBJ-FLA2|no: REINFORCING (phi 0.174); failure: FLA offense succeeds (4+ goals)
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT13FLACBJ-10|yes; why: higher confidence-adjusted growth (11.12 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.925 vs 0.32); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT13FLACBJ-FLA2|no: INTENTIONAL_DIVERSIFIER (phi -0.112); failure: FLA offense suppressed (<= 2 goals)
- **Florida wins by over 1.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no; why: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no has the higher standalone adjusted growth (4.01 vs 3.30 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.720); relationships: KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: REINFORCING (phi 0.174); KXNHLGOAL-26OCT13FLACBJ-FLASVILMANIS95-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.112); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4996): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS (p 0.6142): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13FLACBJ-FLA2|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.4413): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13FLACBJ-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2872, phi -0.238)
- KXNHLGOAL-26OCT13FLACBJ-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4996, phi -0.172)
- KXNHLSPREAD-26OCT13FLACBJ-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.1858, phi -1.0)

portfolios: A EV +1.25 (adj +0.25) on $9.37, P(profit) 0.6761, adj growth 2.4 bp · B EV +0.99 (adj +0.57) on $9.43, P(profit) 0.6999, adj growth 5.5 bp · C EV +0.71 (adj +0.37) on $11.41, P(profit) 0.6948, adj growth 3.6 bp · R EV +0.21 (adj +0.11) on $3.00, P(profit) 0.6441, adj growth 4.4 bp

## BUF @ MTL  ·  10000 joint draws  ·  454 bet sides mapped, 4 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

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
| Owen Power: 1+ goals NO | 88 | 0.918 | 0.906 | +0.030 | +0.018 | $3.90 | FUNDED_RESEARCH | $1 | BUF:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ goals NO | 72 | 0.768 | 0.754 | +0.034 | +0.020 | $3.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 69 | 0.761 | 0.723 | +0.056 | +0.018 | $3.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13BUFMTL-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (7.59 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: BUF offense succeeds (4+ goals)
- **Chris Kreider: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13BUFMTL-MTLCCAUFIELD13-1|no; why: higher confidence-adjusted growth (4.66 vs 0.69 bp); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: MTL offense succeeds (4+ goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no has the higher standalone adjusted growth (4.66 vs 3.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT13BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.10.
- thesis MTL:SUPPRESSED (p 0.3452): highest fidelity KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.3343): highest fidelity KXNHLGOAL-26OCT13BUFMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BUFMTL-MTLJEVANS71-1|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.4412): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT13BUFMTL-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3475, phi -0.123)
- KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4323, phi -0.223)
- KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4323, phi -0.198)

portfolios: A EV +0.45 (adj +0.21) on $8.47, P(profit) 0.5377, adj growth 2.1 bp · B EV +0.55 (adj +0.26) on $10.64, P(profit) 0.5377, adj growth 2.6 bp · C EV +0.26 (adj +0.16) on $5.71, P(profit) 0.7676, adj growth 1.5 bp · R EV +0.03 (adj +0.02) on $1.00, P(profit) 0.9178, adj growth 0.8 bp

## WSH @ CAR  ·  10000 joint draws  ·  460 bet sides mapped, 5 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.580 / away 0.420

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WSH_win | p_overtime | goals | shots CAR/WSH | CAR/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.158 | 0.64 | 0.36 | 0.00 | 6.04 | 33.4/21.0 | 18.2/29.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.132 | 0.54 | 0.46 | 0.48 | 5.93 | 33.9/21.3 | 18.1/30.5 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.109 | 0.69 | 0.31 | 0.00 | 9.25 | 35.2/22.2 | 17.5/27.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 6.03 | 28.0/27.0 | 23.8/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.50 | 0.50 | 0.47 | 5.95 | 27.8/26.9 | 23.6/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.59 | 0.41 | 0.00 | 9.28 | 29.1/28.0 | 22.6/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ethen Frank: 1+ goals YES | 9 | 0.131 | 0.119 | +0.035 | +0.024 | $1.34 | FUNDED_RESEARCH | $1 | WSH:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.224 | 0.209 | +0.044 | +0.029 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ assists NO | 53 | 0.659 | 0.569 | +0.112 | +0.021 | $2.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CAR:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Ethen Frank: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes; why: higher confidence-adjusted growth (13.74 vs 12.54 bp); despite a smaller raw edge (+0.035 vs +0.044/contract); relationships: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: WSH offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (12.54 vs 3.88 bp); despite a smaller raw edge (+0.044 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13WSHCAR-WSHEFRANK53-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: WSH offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ assists NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13WSHCAR-CARSAHO20-1|no; why: higher confidence-adjusted growth (3.99 vs 0.05 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0023 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13WSHCAR-WSHEFRANK53-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.11.
- thesis WSH:OFFENSE_4PLUS (p 0.3376): highest fidelity KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes — Player prop expression KXNHLGOAL-26OCT13WSHCAR-WSHRLEONARD9-1|yes selected over player prop KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.33 vs 0.53 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis CAR:SUPPRESSED (p 0.3346): highest fidelity KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no (same contract)
- KXNHLGOAL-26OCT13WSHCAR-WSHEFRANK53-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.445, phi -0.179)
- KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.445, phi -0.225)
- KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.9 pts; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4514, phi -0.229)
- override: Player prop expression KXNHLGOAL-26OCT13WSHCAR-WSHRLEONARD9-1|yes selected over player prop KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.33 vs 0.53 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.25 (adj +0.99) on $9.37, P(profit) 0.5578, adj growth 9.5 bp · B EV +1.53 (adj +0.75) on $6.03, P(profit) 0.3289, adj growth 7.3 bp · C EV +1.32 (adj +0.53) on $5.97, P(profit) 0.7355, adj growth 5.1 bp · R EV +0.37 (adj +0.25) on $1.00, P(profit) 0.1308, adj growth 8.9 bp

## SEA @ PHI  ·  10000 joint draws  ·  446 bet sides mapped, 11 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

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
| Bobby McMann: 1+ goals NO | 71 | 0.780 | 0.761 | +0.056 | +0.037 | $4.48 | FUNDED_RESEARCH | $2 | SEA:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 10 | 0.143 | 0.131 | +0.037 | +0.025 | $1.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 75 | 0.805 | 0.790 | +0.042 | +0.027 | $4.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Bobby McMann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (15.14 vs 3.21 bp); relationships: KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13SEAPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: SEA offense succeeds (4+ goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (13.72 vs 1.85 bp); despite a smaller raw edge (+0.037 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13SEAPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: SEA offense suppressed (<= 2 goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13SEAPHI-PHIDJIRICEK55-1|no; why: higher confidence-adjusted growth (8.63 vs 1.55 bp); despite a smaller raw edge (+0.042 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, PHI shot control · normal event (5-7) · decided (2+) 0.08.
- thesis SEA:SUPPRESSED (p 0.4596): highest fidelity KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SUPPRESSED (p 0.4097): highest fidelity KXNHLGOAL-26OCT13SEAPHI-PHIPMARTONE94-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13SEAPHI-PHIPMARTONE94-1|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.324): highest fidelity KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes (same contract)
- KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.324, phi -0.211)
- KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4596, phi -0.194)
- KXNHLGOAL-26OCT13SEAPHI-PHIPMARTONE94-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3719, phi -0.194)

portfolios: A EV +1.04 (adj +0.31) on $9.38, P(profit) 0.6679, adj growth 3.0 bp · B EV +1.06 (adj +0.70) on $10.33, P(profit) 0.6798, adj growth 6.9 bp · C EV +1.01 (adj +0.55) on $12.70, P(profit) 0.6736, adj growth 5.4 bp · R EV +0.15 (adj +0.10) on $2.00, P(profit) 0.7802, adj growth 4.0 bp

## TBL @ NYR  ·  10000 joint draws  ·  462 bet sides mapped, 16 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.416 / away 0.584

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
| Vladislav Gavrikov: 1+ assists YES | 23 | 0.317 | 0.269 | +0.075 | +0.026 | $1.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 76 | 0.841 | 0.798 | +0.068 | +0.025 | $3.90 | FUNDED_RESEARCH | $1 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 4.5 goals scored NO | 75 | 0.824 | 0.784 | +0.060 | +0.021 | $2.71 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes; why: KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes has the higher standalone adjusted growth (11.40 vs 8.11 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.037); relationships: KXNHLSPREAD-26OCT13TBNYR-TB3|no: MOSTLY_INDEPENDENT (phi 0.145); KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no: MOSTLY_INDEPENDENT (phi -0.002); failure: NYR offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes has the higher standalone adjusted growth (8.45 vs 7.97 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.278); relationships: KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.145); KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no: REINFORCING (phi 0.509); failure: TBL wins by 2+
- **Tampa Bay over 4.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no selected over player prop KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSPREAD-26OCT13TBNYR-TB3|no: REINFORCING (phi 0.509); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis NYR:OFFENSE_4PLUS (p 0.3635): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [DIRECT], best adjusted EV KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes — Broad expression KXNHLSPREAD-26OCT13TBNYR-NYR2|yes selected over player prop KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.62 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis TBL:SUPPRESSED (p 0.4344): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no — Broad expression KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no selected over player prop KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYR:WINS_BY_2PLUS (p 0.2901): highest fidelity KXNHLSPREAD-26OCT13TBNYR-NYR2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13TBNYR-NYR2|yes (same contract)
- KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4186, phi -0.261)
- KXNHLSPREAD-26OCT13TBNYR-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2646, phi -0.725)
- KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3373, phi -0.649)
- override: Broad expression KXNHLTEAMTOTAL-26OCT13TBNYR-TB5|no selected over player prop KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26OCT13TBNYR-NYR2|yes selected over player prop KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.62 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.32 (adj +0.31) on $9.37, P(profit) 0.6512, adj growth 2.9 bp · B EV +1.00 (adj +0.36) on $8.03, P(profit) 0.802, adj growth 3.5 bp · C EV +1.62 (adj +0.59) on $8.74, P(profit) 0.4205, adj growth 5.7 bp · R EV +0.17 (adj +0.06) on $2.00, P(profit) 0.7635, adj growth 2.4 bp

## STL @ OTT  ·  10000 joint draws  ·  452 bet sides mapped, 6 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.508 / away 0.492

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
| Andre Burakovsky: 1+ assists NO | 71 | 0.842 | 0.753 | +0.117 | +0.028 | $4.49 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Michael Amadio: 1+ goals YES | 14 | 0.176 | 0.165 | +0.028 | +0.016 | $1.00 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Adam Jiricek: 1+ assists NO | 67 | 0.780 | 0.705 | +0.095 | +0.020 | $4.18 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (8.93 vs 0.75 bp); alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: OTT offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13STLOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (4.59 vs 1.31 bp); despite a smaller raw edge (+0.028 vs +0.102/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: OTT offense suppressed (<= 2 goals)
- **Adam Jiricek: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13STLOTT-STLAJIRICEK36-1|no; why: higher confidence-adjusted growth (4.04 vs 0.18 bp); despite a smaller raw edge (+0.095 vs +0.097/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0044 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.3804): highest fidelity KXNHLPTS-26OCT13STLOTT-OTTJSPENCE10-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:SUPPRESSED (p 0.4246): highest fidelity KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no (same contract)
- thesis OTT:SUPPRESSED (p 0.3905): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3804, phi -0.19)
- KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3905, phi -0.204)
- KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.5 pts; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.3574, phi -0.214)

portfolios: A EV +1.60 (adj +0.27) on $9.37, P(profit) 0.3938, adj growth 2.6 bp · B EV +1.49 (adj +0.41) on $9.67, P(profit) 0.7141, adj growth 4.0 bp · C EV +1.18 (adj +0.36) on $12.29, P(profit) 0.8105, adj growth 3.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ NYI  ·  10000 joint draws  ·  414 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.653 / away 0.347

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
| Drew O'Connor: 1+ goals YES | 14 | 0.185 | 0.171 | +0.037 | +0.023 | $1.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| New York I wins by over 2.5 goals NO | 69 | 0.759 | 0.722 | +0.054 | +0.017 | $3.21 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Calum Ritchie: 1+ assists YES | 26 | 0.327 | 0.286 | +0.053 | +0.012 | $1.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Bo Horvat: 1+ goals NO | 62 | 0.663 | 0.650 | +0.026 | +0.013 | $1.67 | FUNDED_RESEARCH | $1 | NYI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT13VANNYI-NYI3|no; why: higher confidence-adjusted growth (9.00 vs 3.15 bp); despite a smaller raw edge (+0.037 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT13VANNYI-NYI3|no: MOSTLY_INDEPENDENT (phi 0.1); KXNHLAST-26OCT13VANNYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: VAN offense suppressed (<= 2 goals)
- **New York I wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT13VANNYI-NYI2|no; why: Broad expression KXNHLSPREAD-26OCT13VANNYI-NYI3|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIMMACCELLI63-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.87 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.1); KXNHLAST-26OCT13VANNYI-NYICRITCHIE64-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.183); KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no: REINFORCING (phi 0.178); failure: NYI wins by 2+
- **Calum Ritchie: 1+ assists YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13VANNYI-NYIAPELECH3-1|yes; why: higher confidence-adjusted growth (1.70 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26OCT13VANNYI-NYI3|no: INTENTIONAL_DIVERSIFIER (phi -0.183); KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.024); failure: NYI offense suppressed (<= 2 goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13VANNYI-NYIMMACCELLI63-1|no; why: Player prop expression KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIVEKLUND73-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT13VANNYI-NYI3|no: REINFORCING (phi 0.178); KXNHLAST-26OCT13VANNYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi -0.024); failure: NYI offense succeeds (4+ goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:SUPPRESSED (p 0.3313): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13VANNYI-NYIMMACCELLI63-1|no — Player prop expression KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIVEKLUND73-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VAN:OFFENSE_4PLUS (p 0.3174): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT13VANNYI-NYI3|no (same contract)
- thesis GAME:TIGHT (p 0.4291): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13VANNYI-NYI3|no (same contract)
- KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.465, phi -0.202)
- KXNHLSPREAD-26OCT13VANNYI-NYI3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:WINS_BY_2PLUS (p 0.3678, phi -0.738)
- KXNHLAST-26OCT13VANNYI-NYICRITCHIE64-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3313, phi -0.243)
- KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.4506, phi -0.264)
- override: Player prop expression KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIVEKLUND73-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLSPREAD-26OCT13VANNYI-NYI3|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIMMACCELLI63-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.87 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.13 (adj +0.25) on $9.37, P(profit) 0.6974, adj growth 2.5 bp · B EV +0.86 (adj +0.37) on $7.30, P(profit) 0.3496, adj growth 3.6 bp · C EV +1.06 (adj +0.31) on $10.15, P(profit) 0.7072, adj growth 3.0 bp · R EV +0.12 (adj +0.05) on $2.00, P(profit) 0.5395, adj growth 1.7 bp

## PIT @ CHI  ·  10000 joint draws  ·  412 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.411 / away 0.589

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_PIT_win | p_overtime | goals | shots CHI/PIT | CHI/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.46 | 0.54 | 0.00 | 6.04 | 26.5/27.0 | 23.2/23.1 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.113 | 0.36 | 0.64 | 0.00 | 6.01 | 21.3/32.7 | 28.3/18.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.49 | 0.51 | 0.47 | 5.95 | 27.0/27.5 | 24.0/23.8 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.44 | 0.56 | 0.45 | 5.89 | 21.4/32.4 | 29.0/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.44 | 0.56 | 0.00 | 9.28 | 28.3/28.8 | 22.3/22.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.082 | 0.34 | 0.66 | 0.00 | 9.31 | 22.9/34.6 | 27.2/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 13 | 0.217 | 0.193 | +0.079 | +0.055 | $3.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 29 | 0.352 | 0.336 | +0.048 | +0.031 | $2.64 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 53 | 0.703 | 0.581 | +0.156 | +0.034 | $4.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Connor Dewar: 1+ goals YES | 13 | 0.172 | 0.159 | +0.034 | +0.021 | $1.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (53.26 vs 10.00 bp); relationships: KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.082); KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes has the higher standalone adjusted growth (53.26 vs 10.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.156); KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13PITCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (9.91 vs 0.44 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.082); KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.156); KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: CHI offense succeeds (4+ goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13PITCHI-PITECHINAKHOV59-1|yes; why: higher confidence-adjusted growth (8.23 vs 2.31 bp); despite a smaller raw edge (+0.034 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.3613): highest fidelity KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.421): highest fidelity KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4379): highest fidelity KXNHLAST-26OCT13PITCHI-PITECHINAKHOV59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.421, phi -0.241)
- KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.421, phi -0.272)
- KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.8 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3613, phi -0.243)
- KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3472, phi -0.198)

portfolios: A EV +3.19 (adj +1.31) on $9.37, P(profit) 0.4737, adj growth 12.8 bp · B EV +3.70 (adj +1.94) on $11.23, P(profit) 0.4804, adj growth 18.8 bp · C EV +4.71 (adj +2.29) on $13.55, P(profit) 0.6475, adj growth 21.9 bp · R EV +0.16 (adj +0.10) on $1.00, P(profit) 0.3525, adj growth 3.9 bp

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
| Neal Pionk: 1+ goals NO | 86 | 0.932 | 0.912 | +0.064 | +0.043 | $4.49 | FUNDED_RESEARCH | $2 | WPG:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Rieger Lorenz: 1+ goals YES | 10 | 0.135 | 0.125 | +0.029 | +0.019 | $1.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 59 | 0.646 | 0.630 | +0.040 | +0.023 | $3.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 23 | 0.305 | 0.260 | +0.063 | +0.018 | $1.49 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13MINWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (37.02 vs 1.08 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense succeeds (4+ goals)
- **Rieger Lorenz: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (8.10 vs 3.71 bp); despite a smaller raw edge (+0.029 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no; why: higher confidence-adjusted growth (4.81 vs 2.78 bp); relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.19); failure: MIN offense succeeds (4+ goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13MINWPG-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (3.71 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.19); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.4173): highest fidelity KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.3661): highest fidelity KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes (same contract)
- thesis WPG:SUPPRESSED (p 0.3874): highest fidelity KXNHLAST-26OCT13MINWPG-WPGNPIONK4-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13MINWPG-WPGNPIONK4-1|no (same contract)
- KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3878, phi -0.116)
- KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4173, phi -0.146)
- KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3661, phi -0.304)
- KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4173, phi -0.274)

portfolios: A EV +1.17 (adj +0.39) on $9.37, P(profit) 0.5767, adj growth 3.7 bp · B EV +1.27 (adj +0.68) on $11.04, P(profit) 0.7842, adj growth 6.6 bp · C EV +0.97 (adj +0.37) on $9.08, P(profit) 0.5766, adj growth 3.5 bp · R EV +0.15 (adj +0.10) on $2.00, P(profit) 0.9322, adj growth 4.0 bp

## COL @ DAL  ·  10000 joint draws  ·  406 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

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
| Zachary L'Heureux: 1+ goals YES | 9 | 0.136 | 0.122 | +0.040 | +0.026 | $1.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Parker Kelly: 1+ goals YES | 9 | 0.127 | 0.116 | +0.031 | +0.021 | $1.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 21 | 0.256 | 0.242 | +0.034 | +0.020 | $1.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 58 | 0.630 | 0.616 | +0.033 | +0.019 | $2.70 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Zachary L'Heureux: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (16.47 vs 5.23 bp); relationships: KXNHLGOAL-26OCT13COLDAL-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: COL offense suppressed (<= 2 goals)
- **Parker Kelly: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (10.43 vs 5.23 bp); despite a smaller raw edge (+0.031 vs +0.034/contract); relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: COL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (5.23 vs 0.15 bp); alternative not eligible: confidence-adjusted EV +0.0035 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13COLDAL-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: COL offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13COLDAL-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (3.41 vs 0.01 bp); despite a smaller raw edge (+0.033 vs +0.068/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0009 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13COLDAL-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: COL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4057): highest fidelity KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.3802): highest fidelity KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no (same contract)
- thesis DAL:SUPPRESSED (p 0.4216): highest fidelity KXNHLGOAL-26OCT13COLDAL-DALMRANTANEN96-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13COLDAL-DALMRANTANEN96-1|no (same contract)
- KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3802, phi -0.18)
- KXNHLGOAL-26OCT13COLDAL-COLPKELLY17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3802, phi -0.164)
- KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3802, phi -0.232)
- KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4057, phi -0.286)

portfolios: A EV +1.54 (adj +0.75) on $9.37, P(profit) 0.6229, adj growth 7.2 bp · B EV +1.33 (adj +0.85) on $6.67, P(profit) 0.3664, adj growth 8.2 bp · C EV +0.55 (adj +0.32) on $8.02, P(profit) 0.6005, adj growth 3.1 bp · R EV +0.06 (adj +0.03) on $1.00, P(profit) 0.6302, adj growth 1.2 bp

## VGK @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 6 +EV candidates, 4 on card

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
| Mitch Marner: 1+ goals NO | 71 | 0.762 | 0.746 | +0.037 | +0.022 | $3.29 | FUNDED_RESEARCH | $1 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ goals NO | 68 | 0.726 | 0.712 | +0.030 | +0.017 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Shea Theodore: 1+ assists YES | 28 | 0.350 | 0.310 | +0.056 | +0.016 | $1.47 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
| Mitch Marner: 1+ assists NO | 53 | 0.600 | 0.563 | +0.053 | +0.015 | $1.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13VGKNSH-VGKTCONNELLY24-1|no; why: higher confidence-adjusted growth (5.23 vs 3.91 bp); despite a smaller raw edge (+0.037 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.101); KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: VGK offense succeeds (4+ goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no has the higher standalone adjusted growth (5.23 vs 2.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.117); KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.108); failure: VGK offense succeeds (4+ goals)
- **Shea Theodore: 1+ assists YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13VGKNSH-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (2.73 vs 0.10 bp); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.101); KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: INTENTIONAL_DIVERSIFIER (phi -0.117); KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.065); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no has the higher standalone adjusted growth (5.23 vs 2.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.108); KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.065); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.4121): highest fidelity KXNHLAST-26OCT13VGKNSH-VGKTCONNELLY24-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:OFFENSE_4PLUS (p 0.3696): highest fidelity KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes (same contract)
- KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3696, phi -0.231)
- KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3696, phi -0.24)
- KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.4121, phi -0.284)
- KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3696, phi -0.279)

portfolios: A EV +1.41 (adj +0.30) on $9.37, P(profit) 0.5565, adj growth 2.9 bp · B EV +0.67 (adj +0.27) on $8.21, P(profit) 0.5453, adj growth 2.6 bp · C EV +0.63 (adj +0.27) on $7.44, P(profit) 0.7616, adj growth 2.6 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.7616, adj growth 1.2 bp

## TOR @ UTA  ·  10000 joint draws  ·  428 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.593 / away 0.407

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
| John Tavares: 1+ assists NO | 63 | 0.706 | 0.665 | +0.059 | +0.019 | $3.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Dylan Guenther: 1+ goals NO | 62 | 0.669 | 0.655 | +0.032 | +0.019 | $2.76 | FUNDED_RESEARCH | $1 | UTA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 69 | 0.788 | 0.721 | +0.083 | +0.016 | $3.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Easton Cowan: 1+ assists YES | 24 | 0.310 | 0.268 | +0.057 | +0.015 | $1.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
- **John Tavares: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no; why: higher confidence-adjusted growth (3.50 vs 2.85 bp); despite a smaller raw edge (+0.059 vs +0.060/contract); relationships: KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.079); failure: TOR offense succeeds (4+ goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TORUTA-UTALCOOLEY92-1|no; why: higher confidence-adjusted growth (3.32 vs 0.13 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13TORUTA-TORJTAVARES91-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: UTA offense succeeds (4+ goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no has the higher standalone adjusted growth (3.32 vs 2.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.036); they share one thesis budget; relationships: KXNHLAST-26OCT13TORUTA-TORJTAVARES91-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: UTA offense succeeds (4+ goals)
- **Easton Cowan: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13TORUTA-TORWNYLANDER88-1|yes; why: higher confidence-adjusted growth (2.52 vs 0.02 bp); alternative not eligible: confidence-adjusted EV +0.0015 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13TORUTA-TORJTAVARES91-1|no: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts UTA shot control · normal event (5-7) · decided (2+) 0.14, UTA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · high event (8+) · decided (2+) 0.11.
- thesis TOR:SUPPRESSED (p 0.4531): highest fidelity KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13TORUTA-TORJTAVARES91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3113): highest fidelity KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no (same contract)
- thesis TOR:OFFENSE_4PLUS (p 0.3266): highest fidelity KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes (same contract)
- KXNHLAST-26OCT13TORUTA-TORJTAVARES91-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3266, phi -0.249)
- KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4845, phi -0.243)
- KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.3 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4845, phi -0.189)
- KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4531, phi -0.283)

portfolios: A EV +1.04 (adj +0.24) on $9.37, P(profit) 0.6837, adj growth 2.4 bp · B EV +1.10 (adj +0.32) on $10.65, P(profit) 0.513, adj growth 3.1 bp · C EV +0.90 (adj +0.32) on $9.35, P(profit) 0.608, adj growth 3.1 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.6686, adj growth 1.1 bp

## CGY @ ANA  ·  10000 joint draws  ·  402 bet sides mapped, 5 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.609 / away 0.391

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_CGY_win | p_overtime | goals | shots ANA/CGY | ANA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.130 | 0.70 | 0.30 | 0.00 | 6.02 | 35.2/22.5 | 20.0/30.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.68 | 0.32 | 0.00 | 6.04 | 29.0/28.3 | 25.5/24.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.56 | 0.44 | 0.49 | 5.94 | 35.1/23.0 | 19.9/31.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.52 | 0.48 | 0.48 | 5.96 | 29.0/28.3 | 25.2/25.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.093 | 0.71 | 0.29 | 0.00 | 9.22 | 36.6/24.0 | 19.6/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.68 | 0.32 | 0.00 | 9.34 | 30.8/30.2 | 25.0/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jeff Malott: 1+ goals YES | 9 | 0.139 | 0.122 | +0.043 | +0.026 | $1.39 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (16.82 vs 3.56 bp); despite a smaller raw edge (+0.043 vs +0.091/contract); relationships: only recommended bet in this game; failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4821): highest fidelity KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes (same contract)
- KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3045, phi -0.148)
- override: override declined: the joint re-optimisation gives KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes less than the minimum stake; KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes kept

portfolios: A EV +3.57 (adj +1.10) on $9.37, P(profit) 0.6506, adj growth 10.2 bp · B EV +0.63 (adj +0.38) on $1.39, P(profit) 0.1392, adj growth 3.7 bp · C EV +0.53 (adj +0.09) on $1.05, P(profit) 0.2705, adj growth 0.9 bp · R EV +0.45 (adj +0.27) on $1.00, P(profit) 0.1392, adj growth 9.9 bp

## EDM @ LAK  ·  10000 joint draws  ·  420 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.457 / away 0.543

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_EDM_win | p_overtime | goals | shots LAK/EDM | LAK/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.45 | 0.55 | 0.00 | 5.99 | 27.7/27.7 | 24.0/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.48 | 0.52 | 0.46 | 5.92 | 28.0/28.1 | 24.9/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.47 | 0.53 | 0.00 | 9.31 | 29.5/29.6 | 23.5/23.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.072 | 0.42 | 0.58 | 0.00 | 6.03 | 22.2/32.8 | 28.4/19.1 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.46 | 0.54 | 0.47 | 5.93 | 22.1/33.0 | 29.7/18.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.061 | 0.51 | 0.49 | 0.00 | 5.96 | 32.8/22.3 | 19.0/28.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Artemi Panarin: 2+ assists NO | 82 | 0.912 | 0.864 | +0.082 | +0.033 | $4.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 48 | 0.614 | 0.523 | +0.116 | +0.026 | $2.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Kasperi Kapanen: 1+ goals NO | 79 | 0.829 | 0.818 | +0.028 | +0.017 | $4.06 | FUNDED_RESEARCH | $2 | EDM:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Kasperi Kapanen: 1+ assists YES | 26 | 0.336 | 0.290 | +0.062 | +0.017 | $1.03 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
- **Artemi Panarin: 2+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (17.36 vs 5.92 bp); despite a smaller raw edge (+0.082 vs +0.116/contract); relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: DUPLICATIVE (phi 0.392); KXNHLGOAL-26OCT13EDMLA-EDMKKAPANEN42-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: LAK offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no; why: second expression of the same thesis: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no has the higher standalone adjusted growth (17.36 vs 5.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.392); they share one thesis budget; relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: DUPLICATIVE (phi 0.392); KXNHLGOAL-26OCT13EDMLA-EDMKKAPANEN42-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: LAK offense succeeds (4+ goals)
- **Kasperi Kapanen: 1+ goals NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no; why: higher confidence-adjusted growth (3.82 vs 1.99 bp); despite a smaller raw edge (+0.028 vs +0.141/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: EDM offense succeeds (4+ goals)
- **Kasperi Kapanen: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (3.12 vs 1.25 bp); relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT13EDMLA-EDMKKAPANEN42-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4172): highest fidelity KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.3973): highest fidelity KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3821): highest fidelity KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no (same contract)
- KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3619, phi -0.248)
- KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.9 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3619, phi -0.277)
- KXNHLGOAL-26OCT13EDMLA-EDMKKAPANEN42-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.3973, phi -0.172)
- KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3821, phi -0.271)

portfolios: A EV +2.99 (adj +0.40) on $9.37, P(profit) 0.6267, adj growth 3.7 bp · B EV +1.26 (adj +0.42) on $11.23, P(profit) 0.6298, adj growth 4.1 bp · C EV +1.60 (adj +0.40) on $9.37, P(profit) 0.6858, adj growth 3.9 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.8293, adj growth 1.6 bp

## BOS @ SJS  ·  10000 joint draws  ·  422 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.470 / away 0.530

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_BOS_win | p_overtime | goals | shots SJS/BOS | SJS/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.51 | 0.49 | 0.00 | 6.03 | 27.1/27.1 | 23.5/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.46 | 5.91 | 27.3/27.2 | 23.9/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.54 | 0.46 | 0.00 | 9.39 | 29.0/28.8 | 22.6/22.7 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.079 | 0.57 | 0.43 | 0.00 | 5.98 | 32.0/21.6 | 18.5/28.1 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.55 | 0.45 | 0.45 | 5.94 | 32.5/21.9 | 18.8/29.1 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.060 | 0.43 | 0.57 | 0.00 | 6.02 | 21.9/32.0 | 27.9/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Luca Cagnoni: 1+ assists NO | 65 | 0.739 | 0.692 | +0.073 | +0.026 | $4.49 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Marat Khusnutdinov: 1+ goals YES | 11 | 0.146 | 0.135 | +0.029 | +0.018 | $1.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: 1+ goals YES | 17 | 0.215 | 0.200 | +0.035 | +0.020 | $1.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 62 | 0.678 | 0.661 | +0.042 | +0.025 | $3.88 | FUNDED_RESEARCH | $1 | BOS:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Luca Cagnoni: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13BOSSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (6.61 vs 5.67 bp); despite a smaller raw edge (+0.073 vs +0.103/contract); relationships: KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: SJS offense succeeds (4+ goals)
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13BOSSJ-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (6.61 vs 2.07 bp); relationships: KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: BOS offense suppressed (<= 2 goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13BOSSJ-SJCGRAF51-1|yes; why: higher confidence-adjusted growth (5.94 vs 4.93 bp); relationships: KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: SJS offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no; why: Player prop expression KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.84 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:SUPPRESSED (p 0.3884): highest fidelity KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no — Player prop expression KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.84 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis SJS:SUPPRESSED (p 0.3723): highest fidelity KXNHLAST-26OCT13BOSSJ-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:OFFENSE_4PLUS (p 0.414): highest fidelity KXNHLAST-26OCT13BOSSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.414, phi -0.215)
- KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3884, phi -0.172)
- KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3723, phi -0.202)
- KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3995, phi -0.269)
- override: Player prop expression KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.84 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.37 (adj +0.39) on $9.37, P(profit) 0.6502, adj growth 3.7 bp · B EV +1.28 (adj +0.64) on $10.79, P(profit) 0.6416, adj growth 6.2 bp · C EV +2.47 (adj +0.83) on $14.27, P(profit) 0.6968, adj growth 8.0 bp · R EV +0.07 (adj +0.04) on $1.00, P(profit) 0.6783, adj growth 1.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
