# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-13T15:44:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.29 | +23.74 | +6.60 | +23.23 | 0.854 | -4.81 | -12.27 | 63.52 |
| B thesis-diversified (joint) ← optimiser card | 138.65 | +17.78 | +6.96 | +17.59 | 0.825 | -6.09 | -12.30 | 67.84 |
| C best expression per thesis | 149.24 | +19.04 | +7.19 | +18.88 | 0.808 | -8.95 | -16.97 | 69.43 |
| R FUNDED research stakes | 20.00 | +1.72 | +0.98 | +0.76 | 0.590 | -4.05 | -5.47 | 0.00 |

## NJD @ DET  ·  10000 joint draws  ·  392 bet sides mapped, 19 +EV candidates, 3 on card


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
| Timo Meier: 1+ goals NO | 74 | 0.790 | 0.777 | +0.037 | +0.023 | $3.76 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 65 | 0.704 | 0.689 | +0.038 | +0.024 | $3.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Viktor Arvidsson: 1+ assists NO | 62 | 0.730 | 0.652 | +0.093 | +0.015 | $2.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13NJDET-NJAMANTHA39-1|no; why: Player prop expression KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13NJDET-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT13NJDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: NJD offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no has the higher standalone adjusted growth (6.36 vs 5.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT13NJDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NJD offense succeeds (4+ goals)
- **Viktor Arvidsson: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT13NJDET-4|no; why: KXNHLTOTAL-26OCT13NJDET-4|no has the higher standalone adjusted growth (2.42 vs 2.26 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.150); relationships: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT13NJDET-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.07.
- thesis NJD:SUPPRESSED (p 0.4877): highest fidelity KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13NJDET-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis GAME:LOW_EVENT (p 0.2976): highest fidelity KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT13NJDET-NJ4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:WINS (p 0.5528): highest fidelity KXNHLSPREAD-26OCT13NJDET-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.2933, phi -0.243)
- KXNHLGOAL-26OCT13NJDET-NJJHUGHES86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.2933, phi -0.241)
- KXNHLAST-26OCT13NJDET-DETVARVIDSSON33-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3637, phi -0.226)
- override: Player prop expression KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.46 (adj +0.27) on $9.61, P(profit) 0.7343, adj growth 2.6 bp · B EV +0.75 (adj +0.29) on $9.47, P(profit) 0.5569, adj growth 2.8 bp · C EV +0.72 (adj +0.36) on $10.27, P(profit) 0.7449, adj growth 3.4 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.7905, adj growth 1.2 bp

## FLA @ CBJ  ·  10000 joint draws  ·  408 bet sides mapped, 11 +EV candidates, 3 on card


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
| Sam Reinhart: 1+ goals NO | 69 | 0.755 | 0.737 | +0.050 | +0.032 | $4.57 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 84 | 0.894 | 0.865 | +0.045 | +0.015 | $4.57 | FUNDED_RESEARCH | $2 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sean Monahan: 1+ goals YES | 19 | 0.229 | 0.217 | +0.029 | +0.016 | $1.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13FLACBJ-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (10.57 vs 4.47 bp); relationships: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT13FLACBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13FLACBJ-FLA2|no; why: higher confidence-adjusted growth (4.01 vs 3.30 bp); despite a smaller raw edge (+0.045 vs +0.051/contract); relationships: KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT13FLACBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.097); failure: FLA wins by 2+
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no has the higher standalone adjusted growth (4.01 vs 3.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.097); they share one thesis budget; relationships: KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.097); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4996): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS (p 0.6142): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13FLACBJ-FLA2|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.4413): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT13FLACBJ-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2872, phi -0.238)
- KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.1858, phi -0.72)
- KXNHLGOAL-26OCT13FLACBJ-CBJSMONAHAN23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3401, phi -0.202)

portfolios: A EV +1.28 (adj +0.26) on $9.61, P(profit) 0.6761, adj growth 2.5 bp · B EV +0.71 (adj +0.37) on $10.15, P(profit) 0.7514, adj growth 3.6 bp · C EV +0.74 (adj +0.37) on $11.93, P(profit) 0.6948, adj growth 3.6 bp · R EV +0.25 (adj +0.13) on $4.00, P(profit) 0.6948, adj growth 4.8 bp

## BUF @ MTL  ·  10000 joint draws  ·  406 bet sides mapped, 5 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_BUF_win | p_overtime | goals | shots MTL/BUF | MTL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.62 | 0.38 | 0.00 | 6.03 | 26.9/27.4 | 24.3/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.49 | 5.93 | 26.9/27.5 | 24.3/23.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.100 | 0.54 | 0.46 | 0.00 | 6.01 | 21.8/33.0 | 29.3/18.3 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.54 | 0.46 | 0.46 | 5.88 | 21.3/32.5 | 29.3/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.59 | 0.41 | 0.00 | 9.29 | 28.4/29.0 | 23.4/21.9 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.068 | 0.57 | 0.43 | 0.00 | 9.18 | 23.4/34.7 | 28.6/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Owen Power: 1+ goals NO | 88 | 0.921 | 0.905 | +0.033 | +0.018 | $4.57 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 69 | 0.753 | 0.719 | +0.048 | +0.014 | $3.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13BUFMTL-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (7.26 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: BUF offense succeeds (4+ goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13BUFMTL-MTLNSUZUKI14-1|no; why: higher confidence-adjusted growth (2.09 vs 1.84 bp); despite a smaller raw edge (+0.048 vs +0.051/contract); relationships: KXNHLGOAL-26OCT13BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.10.
- thesis MTL:WINS_BY_2PLUS (p 0.3343): highest fidelity KXNHLGOAL-26OCT13BUFMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BUFMTL-MTLJEVANS71-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4323): highest fidelity KXNHLGOAL-26OCT13BUFMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BUFMTL-MTLJEVANS71-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3452): highest fidelity KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13BUFMTL-MTLNSUZUKI14-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13BUFMTL-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3475, phi -0.127)
- KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4323, phi -0.219)

portfolios: A EV +0.76 (adj +0.28) on $9.61, P(profit) 0.5584, adj growth 2.7 bp · B EV +0.41 (adj +0.16) on $8.04, P(profit) 0.6923, adj growth 1.6 bp · C EV +0.49 (adj +0.21) on $5.17, P(profit) 0.7948, adj growth 2.1 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.9206, adj growth 1.6 bp

## WSH @ CAR  ·  10000 joint draws  ·  462 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WSH_win | p_overtime | goals | shots CAR/WSH | CAR/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.155 | 0.68 | 0.32 | 0.00 | 6.01 | 33.6/20.9 | 18.3/28.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.132 | 0.53 | 0.47 | 0.46 | 5.92 | 33.8/21.2 | 18.1/30.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.108 | 0.67 | 0.33 | 0.00 | 9.27 | 35.1/22.4 | 17.7/27.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.089 | 0.58 | 0.42 | 0.00 | 6.03 | 27.5/26.4 | 23.3/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.50 | 0.50 | 0.48 | 5.96 | 27.5/26.5 | 23.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.58 | 0.42 | 0.00 | 9.31 | 29.2/28.2 | 22.6/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ethen Frank: 1+ goals YES | 9 | 0.129 | 0.116 | +0.033 | +0.020 | $1.14 | FUNDED_RESEARCH | $1 | WSH:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 27 | 0.346 | 0.305 | +0.062 | +0.022 | $1.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
| Jordan Kyrou: 1+ assists NO | 74 | 0.800 | 0.767 | +0.046 | +0.014 | $4.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Ethen Frank: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (9.66 vs 5.00 bp); despite a smaller raw edge (+0.033 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT13WSHCAR-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.076); failure: WSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes; why: higher confidence-adjusted growth (5.00 vs 2.82 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT13WSHCAR-WSHEFRANK53-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT13WSHCAR-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: WSH offense suppressed (<= 2 goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13WSHCAR-WSHATUCH89-1|no; why: higher confidence-adjusted growth (2.28 vs 0.08 bp); alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13WSHCAR-WSHEFRANK53-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.076); KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: WSH offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.11.
- thesis WSH:OFFENSE_4PLUS (p 0.3385): highest fidelity KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes (same contract)
- thesis WSH:SUPPRESSED (p 0.4469): highest fidelity KXNHLAST-26OCT13WSHCAR-WSHJKYROU25-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13WSHCAR-WSHJKYROU25-1|no (same contract)
- KXNHLGOAL-26OCT13WSHCAR-WSHEFRANK53-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4469, phi -0.174)
- KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4469, phi -0.277)
- KXNHLAST-26OCT13WSHCAR-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.3385, phi -0.232)

portfolios: A EV +1.72 (adj +0.74) on $9.61, P(profit) 0.5172, adj growth 7.0 bp · B EV +1.03 (adj +0.44) on $7.32, P(profit) 0.3574, adj growth 4.3 bp · C EV +0.81 (adj +0.27) on $7.46, P(profit) 0.3458, adj growth 2.6 bp · R EV +0.35 (adj +0.21) on $1.00, P(profit) 0.129, adj growth 7.3 bp

## SEA @ PHI  ·  10000 joint draws  ·  446 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_SEA_win | p_overtime | goals | shots PHI/SEA | PHI/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.54 | 0.46 | 0.00 | 5.93 | 26.6/26.5 | 23.2/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.55 | 0.45 | 0.48 | 5.86 | 26.8/26.7 | 23.6/23.4 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.080 | 0.64 | 0.36 | 0.00 | 6.03 | 31.4/21.2 | 18.5/26.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.54 | 0.46 | 0.00 | 9.12 | 28.1/28.1 | 22.6/22.1 | even strength |
| PHI shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.55 | 0.45 | 0.45 | 5.85 | 31.7/21.3 | 18.2/28.2 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.067 | 0.52 | 0.48 | 0.45 | 2.78 | 25.3/25.3 | 23.9/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 9 | 0.127 | 0.115 | +0.031 | +0.019 | $1.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Bobby McMann: 1+ goals NO | 72 | 0.774 | 0.758 | +0.040 | +0.024 | $3.43 | FUNDED_RESEARCH | $1 | SEA:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Jared McCann: 1+ goals NO | 73 | 0.782 | 0.767 | +0.038 | +0.023 | $3.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ assists YES | 25 | 0.316 | 0.280 | +0.052 | +0.017 | $1.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (9.21 vs 3.31 bp); despite a smaller raw edge (+0.031 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.027); failure: SEA offense suppressed (<= 2 goals)
- **Bobby McMann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (6.64 vs 6.08 bp); relationships: KXNHLGOAL-26OCT13SEAPHI-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.063); failure: SEA offense succeeds (4+ goals)
- **Jared McCann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no has the higher standalone adjusted growth (6.64 vs 6.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT13SEAPHI-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.067); failure: SEA offense succeeds (4+ goals)
- **Kaapo Kakko: 1+ assists YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13SEAPHI-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (3.31 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13SEAPHI-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: INTENTIONAL_DIVERSIFIER (phi -0.067); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, PHI shot control · normal event (5-7) · decided (2+) 0.08.
- thesis SEA:SUPPRESSED (p 0.4619): highest fidelity KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.3224): highest fidelity KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes (same contract)
- KXNHLGOAL-26OCT13SEAPHI-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4619, phi -0.164)
- KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.3224, phi -0.234)
- KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.3224, phi -0.232)
- KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4619, phi -0.283)

portfolios: A EV +0.87 (adj +0.35) on $9.61, P(profit) 0.6317, adj growth 3.4 bp · B EV +0.97 (adj +0.52) on $9.22, P(profit) 0.765, adj growth 5.0 bp · C EV +0.81 (adj +0.38) on $13.66, P(profit) 0.7496, adj growth 3.7 bp · R EV +0.06 (adj +0.03) on $1.00, P(profit) 0.7745, adj growth 1.3 bp

## TBL @ NYR  ·  10000 joint draws  ·  444 bet sides mapped, 18 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_TBL_win | p_overtime | goals | shots NYR/TBL | NYR/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.54 | 0.46 | 0.00 | 5.97 | 25.8/26.3 | 23.0/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.49 | 5.92 | 25.9/26.5 | 23.1/22.6 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.104 | 0.46 | 0.54 | 0.00 | 5.98 | 20.3/31.1 | 27.1/17.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.47 | 0.53 | 0.47 | 5.88 | 20.6/31.7 | 28.2/17.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.58 | 0.42 | 0.00 | 9.29 | 27.3/27.9 | 22.2/20.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.53 | 0.47 | 0.49 | 2.79 | 24.6/25.1 | 23.7/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| John Carlson: 1+ assists NO | 55 | 0.708 | 0.602 | +0.140 | +0.035 | $4.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 76 | 0.839 | 0.797 | +0.066 | +0.024 | $4.57 | FUNDED_RESEARCH | $2 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: higher confidence-adjusted growth (10.66 vs 7.41 bp); wins across more scripts (relative breadth 0.994 vs 0.545); relationships: KXNHLSPREAD-26OCT13TBNYR-TB3|no: MOSTLY_INDEPENDENT (phi 0.139); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes has the higher standalone adjusted growth (7.41 vs 7.29 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.278); relationships: KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.139); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:SUPPRESSED (p 0.4385): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:WINS_BY_2PLUS (p 0.2868): highest fidelity KXNHLSPREAD-26OCT13TBNYR-NYR2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT13TBNYR-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:WINS (p 0.5182): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT13TBNYR-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.3 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3459, phi -0.234)
- KXNHLSPREAD-26OCT13TBNYR-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2605, phi -0.739)
- override: Broad expression KXNHLSPREAD-26OCT13TBNYR-NYR2|yes selected over player prop KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes because adjusted EV is 0.8 pts higher while thesis capture is 0.62 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.41 (adj +0.34) on $9.61, P(profit) 0.6578, adj growth 3.2 bp · B EV +1.44 (adj +0.40) on $8.80, P(profit) 0.6167, adj growth 3.9 bp · C EV +2.36 (adj +0.66) on $12.66, P(profit) 0.6566, adj growth 6.3 bp · R EV +0.17 (adj +0.06) on $2.00, P(profit) 0.8387, adj growth 2.4 bp

## STL @ OTT  ·  10000 joint draws  ·  430 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_STL_win | p_overtime | goals | shots OTT/STL | OTT/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.49 | 0.51 | 0.00 | 5.96 | 26.7/26.2 | 22.8/23.2 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.109 | 0.62 | 0.38 | 0.00 | 6.03 | 31.5/20.5 | 17.6/27.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.50 | 0.50 | 0.45 | 5.91 | 26.6/26.3 | 23.1/23.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.52 | 0.48 | 0.47 | 5.89 | 32.1/21.0 | 17.7/28.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.48 | 0.52 | 0.00 | 9.24 | 28.1/27.8 | 21.6/22.1 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.070 | 0.57 | 0.43 | 0.00 | 9.16 | 33.4/22.1 | 17.0/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Jiricek: 2+ assists NO | 94 | 0.974 | 0.955 | +0.030 | +0.011 | $3.83 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (1.00) | EVIDENCE_MIXED | D |
| Adam Jiricek: 1+ assists NO | 67 | 0.780 | 0.705 | +0.094 | +0.020 | $3.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
| Andre Burakovsky: 1+ assists NO | 71 | 0.830 | 0.742 | +0.106 | +0.018 | $4.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
- **Adam Jiricek: 2+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13STLOTT-STLAJIRICEK36-1|no; why: higher confidence-adjusted growth (4.89 vs 0.10 bp); despite a smaller raw edge (+0.030 vs +0.093/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0033 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no: DUPLICATIVE (phi 0.305); KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: STL offense succeeds (4+ goals)
- **Adam Jiricek: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13STLOTT-STLAJIRICEK36-1|no; why: higher confidence-adjusted growth (3.93 vs 0.10 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0033 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-2|no: DUPLICATIVE (phi 0.305); KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: STL offense succeeds (4+ goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (3.56 vs 0.53 bp); alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-2|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis STL:SUPPRESSED (p 0.4196): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis OTT:SUPPRESSED (p 0.3926): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 0% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.3587, phi -0.131)
- KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.5 pts; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.3587, phi -0.203)
- KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.5 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3887, phi -0.175)

portfolios: A EV +1.01 (adj +0.21) on $9.61, P(profit) 0.6482, adj growth 2.0 bp · B EV +1.14 (adj +0.23) on $10.95, P(profit) 0.6482, adj growth 2.3 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ NYI  ·  10000 joint draws  ·  422 bet sides mapped, 14 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_VAN_win | p_overtime | goals | shots NYI/VAN | NYI/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NYI shot control · normal event (5-7) · decided (2+) | 0.132 | 0.67 | 0.33 | 0.00 | 6.0 | 33.1/21.4 | 18.7/28.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.63 | 0.37 | 0.00 | 6.01 | 27.5/26.7 | 23.7/23.5 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.57 | 0.43 | 0.45 | 5.92 | 33.2/21.6 | 18.5/29.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.53 | 0.47 | 0.45 | 5.88 | 27.6/27.0 | 23.6/24.2 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.083 | 0.71 | 0.29 | 0.00 | 9.33 | 34.8/22.8 | 18.3/26.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.59 | 0.41 | 0.00 | 9.31 | 29.0/28.3 | 22.8/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aatu Raty: 1+ goals YES | 10 | 0.138 | 0.125 | +0.032 | +0.019 | $1.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Paul Cotter: 1+ goals NO | 83 | 0.870 | 0.859 | +0.030 | +0.019 | $4.57 | FUNDED_RESEARCH | $2 | VAN:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Kyle Palmieri: 1+ goals NO | 70 | 0.750 | 0.735 | +0.035 | +0.020 | $4.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Aatu Raty: 1+ goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT13VANNYI-NYI3|no; why: higher confidence-adjusted growth (7.82 vs 2.42 bp); despite a smaller raw edge (+0.032 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13VANNYI-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Paul Cotter: 1+ goals NO** — thesis: VAN offense suppressed (<= 2 goals); alternative: KXNHL3PTOTAL-26OCT13VANNYI-2|no; why: higher confidence-adjusted growth (5.91 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13VANNYI-VANARATY54-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi -0.027); failure: VAN offense succeeds (4+ goals)
- **Kyle Palmieri: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13VANNYI-NYIBHORVAT14-1|no; why: Player prop expression KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIVEKLUND73-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.89 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13VANNYI-VANARATY54-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13VANNYI-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi -0.027); failure: NYI offense succeeds (4+ goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.2136): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13VANNYI-VANARATY54-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.3191): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13VANNYI-VANARATY54-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:SUPPRESSED (p 0.3359): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no — Player prop expression KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIVEKLUND73-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.89 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT13VANNYI-VANARATY54-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4632, phi -0.201)
- KXNHLGOAL-26OCT13VANNYI-VANPCOTTER47-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:OFFENSE_4PLUS (p 0.3191, phi -0.17)
- KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.4516, phi -0.219)
- override: Player prop expression KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIVEKLUND73-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.89 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.17 (adj +0.25) on $9.61, P(profit) 0.7072, adj growth 2.5 bp · B EV +0.69 (adj +0.41) on $9.81, P(profit) 0.6982, adj growth 4.0 bp · C EV +0.83 (adj +0.43) on $8.86, P(profit) 0.6392, adj growth 4.1 bp · R EV +0.07 (adj +0.05) on $2.00, P(profit) 0.8701, adj growth 1.8 bp

## PIT @ CHI  ·  10000 joint draws  ·  410 bet sides mapped, 16 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_PIT_win | p_overtime | goals | shots CHI/PIT | CHI/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.44 | 0.56 | 0.00 | 6.04 | 26.7/27.4 | 23.5/23.5 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.115 | 0.38 | 0.62 | 0.00 | 6.0 | 21.3/32.8 | 28.5/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.50 | 0.50 | 0.46 | 5.98 | 26.9/27.4 | 24.1/23.4 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.44 | 0.56 | 0.45 | 5.87 | 21.3/32.6 | 29.1/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.45 | 0.55 | 0.00 | 9.33 | 28.5/28.9 | 22.3/22.5 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.078 | 0.37 | 0.63 | 0.00 | 9.29 | 22.8/34.4 | 26.7/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 14 | 0.216 | 0.193 | +0.068 | +0.045 | $2.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 52 | 0.701 | 0.580 | +0.164 | +0.043 | $4.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 29 | 0.348 | 0.331 | +0.043 | +0.026 | $2.46 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
| Cole Smith: 1+ goals YES | 10 | 0.137 | 0.124 | +0.030 | +0.018 | $1.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13PITCHI-CHIAFRONDELL16-1|yes; why: higher confidence-adjusted growth (34.01 vs 11.40 bp); relationships: KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.078); KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT13PITCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13PITCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (16.12 vs 0.49 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.078); KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.157); KXNHLGOAL-26OCT13PITCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: CHI offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes; why: Player prop expression KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes selected over player prop KXNHLGOAL-26OCT13PITCHI-CHIAFRONDELL16-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.51 vs 0.45 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.157); KXNHLGOAL-26OCT13PITCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: CHI offense suppressed (<= 2 goals)
- **Cole Smith: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes has the higher standalone adjusted growth (34.01 vs 6.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.3723): highest fidelity KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes — Player prop expression KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes selected over player prop KXNHLGOAL-26OCT13PITCHI-CHIAFRONDELL16-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.51 vs 0.45 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis CHI:WINS_BY_2PLUS (p 0.242): highest fidelity KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4203): highest fidelity KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4203, phi -0.249)
- KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.6 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3723, phi -0.265)
- KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4203, phi -0.27)
- KXNHLGOAL-26OCT13PITCHI-CHICSMITH22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4203, phi -0.185)
- override: Player prop expression KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes selected over player prop KXNHLGOAL-26OCT13PITCHI-CHIAFRONDELL16-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.51 vs 0.45 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +3.27 (adj +1.30) on $9.61, P(profit) 0.5645, adj growth 12.6 bp · B EV +3.30 (adj +1.58) on $10.82, P(profit) 0.4518, adj growth 15.4 bp · C EV +3.59 (adj +1.52) on $14.91, P(profit) 0.7243, adj growth 14.8 bp · R EV +0.14 (adj +0.09) on $1.00, P(profit) 0.3476, adj growth 3.3 bp

## MIN @ WPG  ·  10000 joint draws  ·  388 bet sides mapped, 7 +EV candidates, 3 on card


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
| Neal Pionk: 1+ goals NO | 86 | 0.932 | 0.912 | +0.064 | +0.043 | $4.57 | FUNDED_RESEARCH | $2 | WPG:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 59 | 0.646 | 0.631 | +0.040 | +0.024 | $4.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 23 | 0.305 | 0.260 | +0.063 | +0.018 | $1.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13MINWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (37.02 vs 1.74 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13MINWPG-MINKKAPRIZOV97-1|no; why: higher confidence-adjusted growth (5.35 vs 3.85 bp); despite a smaller raw edge (+0.040 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.19); failure: MIN offense succeeds (4+ goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13MINWPG-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (3.71 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.19); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.4173): highest fidelity KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.3661): highest fidelity KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes (same contract)
- thesis WPG:SUPPRESSED (p 0.3874): highest fidelity KXNHLAST-26OCT13MINWPG-WPGNPIONK4-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13MINWPG-WPGNPIONK4-1|no (same contract)
- KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3878, phi -0.116)
- KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3661, phi -0.304)
- KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4173, phi -0.274)

portfolios: A EV +1.30 (adj +0.44) on $9.61, P(profit) 0.5782, adj growth 4.3 bp · B EV +1.01 (adj +0.51) on $10.32, P(profit) 0.7513, adj growth 5.0 bp · C EV +1.14 (adj +0.45) on $14.91, P(profit) 0.5625, adj growth 4.4 bp · R EV +0.15 (adj +0.10) on $2.00, P(profit) 0.9322, adj growth 4.0 bp

## COL @ DAL  ·  10000 joint draws  ·  410 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_COL_win | p_overtime | goals | shots DAL/COL | DAL/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.47 | 0.53 | 0.00 | 6.03 | 27.0/27.5 | 23.9/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.48 | 5.92 | 27.2/27.7 | 24.4/23.8 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.105 | 0.40 | 0.60 | 0.00 | 5.98 | 21.3/32.4 | 28.1/18.5 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.49 | 0.51 | 0.43 | 5.88 | 21.5/32.8 | 29.4/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.47 | 0.53 | 0.00 | 9.24 | 28.4/28.9 | 22.9/22.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.065 | 0.41 | 0.59 | 0.00 | 9.18 | 22.8/34.2 | 27.1/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 1+ goals NO | 57 | 0.648 | 0.627 | +0.061 | +0.040 | $3.85 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 20 | 0.247 | 0.234 | +0.036 | +0.023 | $1.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 81 | 0.843 | 0.833 | +0.022 | +0.012 | $3.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLMNECAS88-1|no; why: higher confidence-adjusted growth (14.45 vs 0.26 bp); alternative not eligible: confidence-adjusted EV +0.0049 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT13COLDAL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: COL offense succeeds (4+ goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (6.72 vs 0.32 bp); alternative not eligible: confidence-adjusted EV +0.0049 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT13COLDAL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.025); failure: COL offense suppressed (<= 2 goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no has the higher standalone adjusted growth (14.45 vs 2.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.025); failure: COL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:SUPPRESSED (p 0.3874): highest fidelity KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no (same contract)
- thesis COL:OFFENSE_4PLUS (p 0.3957): highest fidelity KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes (same contract)
- KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3957, phi -0.272)
- KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3874, phi -0.225)
- KXNHLGOAL-26OCT13COLDAL-COLCMAKAR8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3957, phi -0.184)

portfolios: A EV +0.85 (adj +0.54) on $9.61, P(profit) 0.6566, adj growth 5.2 bp · B EV +0.75 (adj +0.47) on $8.42, P(profit) 0.645, adj growth 4.6 bp · C EV +0.97 (adj +0.63) on $8.04, P(profit) 0.7365, adj growth 6.1 bp · R EV +0.10 (adj +0.07) on $1.00, P(profit) 0.6478, adj growth 2.7 bp

## VGK @ NSH  ·  10000 joint draws  ·  418 bet sides mapped, 4 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_VGK_win | p_overtime | goals | shots NSH/VGK | NSH/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.53 | 0.47 | 0.00 | 5.97 | 27.6/28.1 | 24.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.48 | 0.52 | 0.46 | 5.94 | 27.4/27.9 | 24.5/24.1 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.097 | 0.48 | 0.52 | 0.00 | 5.93 | 21.9/33.2 | 29.5/18.6 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.48 | 0.52 | 0.50 | 5.91 | 22.2/33.6 | 30.3/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.57 | 0.43 | 0.00 | 9.26 | 29.4/29.8 | 24.3/22.9 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.066 | 0.45 | 0.55 | 0.00 | 9.28 | 23.7/35.3 | 28.8/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 71 | 0.759 | 0.745 | +0.034 | +0.021 | $2.81 | FUNDED_RESEARCH | $1 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ goals NO | 68 | 0.730 | 0.717 | +0.035 | +0.021 | $2.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (4.76 vs 4.68 bp); despite a smaller raw edge (+0.034 vs +0.035/contract); relationships: KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: VGK offense succeeds (4+ goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no has the higher standalone adjusted growth (4.76 vs 4.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.4021): highest fidelity KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3689, phi -0.212)
- KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3689, phi -0.243)

portfolios: A EV +1.03 (adj +0.27) on $9.61, P(profit) 0.5861, adj growth 2.6 bp · B EV +0.26 (adj +0.16) on $5.35, P(profit) 0.554, adj growth 1.6 bp · C EV +0.27 (adj +0.17) on $5.80, P(profit) 0.7586, adj growth 1.6 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.7586, adj growth 1.1 bp

## TOR @ UTA  ·  10000 joint draws  ·  428 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TOR_win | p_overtime | goals | shots UTA/TOR | UTA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| UTA shot control · normal event (5-7) · decided (2+) | 0.148 | 0.69 | 0.31 | 0.00 | 6.0 | 34.4/22.0 | 19.4/29.6 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.56 | 0.44 | 0.47 | 5.96 | 34.7/22.0 | 18.8/31.1 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.110 | 0.72 | 0.28 | 0.00 | 9.23 | 36.1/23.3 | 18.9/27.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.67 | 0.33 | 0.00 | 6.07 | 28.7/28.0 | 25.1/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.65 | 0.35 | 0.00 | 9.4 | 30.3/29.3 | 24.0/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.52 | 0.48 | 0.49 | 5.96 | 28.6/27.7 | 24.3/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dylan Guenther: 1+ goals NO | 61 | 0.669 | 0.653 | +0.042 | +0.026 | $3.83 | FUNDED_RESEARCH | $1 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Kirill Marchenko: 1+ assists NO | 63 | 0.717 | 0.671 | +0.071 | +0.025 | $3.20 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Auston Matthews: 1+ assists NO | 57 | 0.648 | 0.607 | +0.061 | +0.020 | $1.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Darren Raddysh: 1+ assists NO | 58 | 0.686 | 0.614 | +0.089 | +0.017 | $1.74 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TORUTA-UTACKELLER9-1|no; why: higher confidence-adjusted growth (6.40 vs 0.00 bp); despite a smaller raw edge (+0.042 vs +0.056/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT13TORUTA-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: UTA offense succeeds (4+ goals)
- **Kirill Marchenko: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TORUTA-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (5.90 vs 3.47 bp); relationships: KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT13TORUTA-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.109); KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi 0.079); failure: TOR offense succeeds (4+ goals)
- **Auston Matthews: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no; why: second expression of the same thesis: KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no has the higher standalone adjusted growth (5.90 vs 3.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.109); they share one thesis budget; relationships: KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi 0.109); KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi 0.099); failure: TOR offense succeeds (4+ goals)
- **Darren Raddysh: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no; why: second expression of the same thesis: KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no has the higher standalone adjusted growth (5.90 vs 2.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.079); they share one thesis budget; relationships: KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi 0.079); KXNHLAST-26OCT13TORUTA-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.099); failure: TOR offense succeeds (4+ goals)

**Review**: scripts UTA shot control · normal event (5-7) · decided (2+) 0.15, UTA shot control · normal event (5-7) · tight (1-goal/OT) 0.12, UTA shot control · high event (8+) · decided (2+) 0.11.
- thesis UTA:SUPPRESSED (p 0.294): highest fidelity KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no (same contract)
- thesis TOR:SUPPRESSED (p 0.4585): highest fidelity KXNHLAST-26OCT13TORUTA-TORJTAVARES91-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.5024, phi -0.222)
- KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3291, phi -0.246)
- KXNHLAST-26OCT13TORUTA-TORAMATTHEWS34-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3291, phi -0.28)
- KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.1 pts; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3291, phi -0.255)

portfolios: A EV +1.13 (adj +0.28) on $9.61, P(profit) 0.6546, adj growth 2.7 bp · B EV +1.07 (adj +0.40) on $10.69, P(profit) 0.6695, adj growth 3.9 bp · C EV +0.97 (adj +0.44) on $10.90, P(profit) 0.4794, adj growth 4.2 bp · R EV +0.07 (adj +0.04) on $1.00, P(profit) 0.6687, adj growth 1.6 bp

## CGY @ ANA  ·  10000 joint draws  ·  408 bet sides mapped, 3 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_CGY_win | p_overtime | goals | shots ANA/CGY | ANA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.130 | 0.70 | 0.30 | 0.00 | 6.02 | 35.2/22.5 | 20.0/30.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.68 | 0.32 | 0.00 | 6.04 | 29.0/28.3 | 25.5/24.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.56 | 0.44 | 0.49 | 5.94 | 35.1/23.0 | 19.9/31.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.52 | 0.48 | 0.48 | 5.96 | 29.0/28.3 | 25.2/25.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.093 | 0.71 | 0.29 | 0.00 | 9.22 | 36.6/24.0 | 19.6/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.68 | 0.32 | 0.00 | 9.34 | 30.8/30.2 | 25.0/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Killorn: 1+ assists YES | 30 | 0.366 | 0.331 | +0.052 | +0.016 | $1.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
- **Alex Killorn: 1+ assists YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13CGYANA-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (2.57 vs 0.13 bp); alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4821): highest fidelity KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes (same contract)
- KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3045, phi -0.252)

portfolios: A EV +1.00 (adj +0.41) on $5.14, P(profit) 0.4508, adj growth 3.9 bp · B EV +0.17 (adj +0.05) on $1.06, P(profit) 0.3663, adj growth 0.5 bp · C EV +0.27 (adj +0.08) on $1.64, P(profit) 0.3663, adj growth 0.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ LAK  ·  10000 joint draws  ·  420 bet sides mapped, 6 +EV candidates, 4 on card


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
| Kasperi Kapanen: 1+ assists YES | 25 | 0.336 | 0.288 | +0.073 | +0.025 | $1.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 48 | 0.614 | 0.520 | +0.116 | +0.023 | $2.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ assists YES | 28 | 0.351 | 0.313 | +0.057 | +0.019 | $1.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
| Leon Draisaitl: 1+ assists NO | 41 | 0.568 | 0.446 | +0.141 | +0.019 | $2.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.77) | CALIBRATION_WARNING | D |
- **Kasperi Kapanen: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (6.85 vs 3.72 bp); relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.089); failure: EDM offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (4.53 vs 1.09 bp); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: LAK offense succeeds (4+ goals)
- **Mattias Ekholm: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes has the higher standalone adjusted growth (6.85 vs 3.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.045); they share one thesis budget; relationships: KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.074); failure: EDM offense suppressed (<= 2 goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (3.12 vs 1.96 bp); relationships: KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.089); KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.074); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis EDM:OFFENSE_4PLUS (p 0.3973): highest fidelity KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.4172): highest fidelity KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no (same contract)
- thesis EDM:SUPPRESSED (p 0.3821): highest fidelity KXNHLPTS-26OCT13EDMLA-EDMLDRAISAITL29-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3821, phi -0.271)
- KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3619, phi -0.277)
- KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3821, phi -0.256)
- KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.2 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.3973, phi -0.309)

portfolios: A EV +2.62 (adj +0.35) on $9.61, P(profit) 0.7103, adj growth 3.3 bp · B EV +2.12 (adj +0.48) on $8.11, P(profit) 0.65, adj growth 4.7 bp · C EV +2.36 (adj +0.50) on $8.55, P(profit) 0.5799, adj growth 4.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ SJS  ·  10000 joint draws  ·  422 bet sides mapped, 11 +EV candidates, 3 on card


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
| Charlie McAvoy: 1+ assists NO | 55 | 0.708 | 0.595 | +0.140 | +0.028 | $4.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ assists NO | 69 | 0.808 | 0.728 | +0.103 | +0.023 | $4.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Kiefer Sherwood: 1+ goals YES | 17 | 0.215 | 0.198 | +0.035 | +0.018 | $1.30 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no; why: higher confidence-adjusted growth (7.03 vs 2.50 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLAST-26OCT13BOSSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: BOS offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no; why: higher confidence-adjusted growth (5.67 vs 3.46 bp); relationships: KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.143); failure: SJS offense succeeds (4+ goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13BOSSJ-SJCGRAF51-1|yes; why: KXNHLGOAL-26OCT13BOSSJ-SJCGRAF51-1|yes has the higher standalone adjusted growth (4.93 vs 4.56 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.014); relationships: KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT13BOSSJ-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.143); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:SUPPRESSED (p 0.3884): highest fidelity KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no (same contract)
- thesis SJS:SUPPRESSED (p 0.3723): highest fidelity KXNHLAST-26OCT13BOSSJ-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13BOSSJ-SJISTENBERG41-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.414): highest fidelity KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes (same contract)
- KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.2 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3995, phi -0.229)
- KXNHLAST-26OCT13BOSSJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.3 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.414, phi -0.189)
- KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3723, phi -0.202)

portfolios: A EV +1.86 (adj +0.31) on $9.61, P(profit) 0.6375, adj growth 3.0 bp · B EV +1.97 (adj +0.49) on $10.12, P(profit) 0.6615, adj growth 4.8 bp · C EV +2.71 (adj +0.72) on $14.48, P(profit) 0.7266, adj growth 6.9 bp · R EV +0.20 (adj +0.10) on $1.00, P(profit) 0.215, adj growth 3.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
