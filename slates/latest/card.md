# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-13T21:01:01Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.93 | +29.58 | +6.54 | +29.36 | 0.894 | -0.81 | -9.20 | 62.53 |
| B thesis-diversified (joint) ← optimiser card | 143.39 | +23.09 | +11.04 | +21.87 | 0.820 | -7.84 | -15.09 | 107.33 |
| C best expression per thesis | 146.24 | +22.50 | +8.77 | +21.63 | 0.850 | -5.00 | -12.14 | 85.12 |
| R FUNDED research stakes | 18.00 | +1.91 | +1.19 | +1.15 | 0.589 | -4.18 | -5.49 | 0.00 |

## NJD @ DET  ·  10000 joint draws  ·  408 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.505 / away 0.495

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
| Anthony Mantha: 1+ assists NO | 73 | 0.825 | 0.775 | +0.081 | +0.031 | $3.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Nico Hischier: 1+ goals NO | 70 | 0.758 | 0.743 | +0.044 | +0.028 | $3.46 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Andrew Copp: 1+ goals YES | 16 | 0.198 | 0.187 | +0.028 | +0.018 | $1.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Full Game: Over 6.5 goals scored NO | 55 | 0.623 | 0.584 | +0.055 | +0.016 | $1.72 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Anthony Mantha: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no; why: higher confidence-adjusted growth (11.14 vs 8.43 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.058); KXNHLGOAL-26OCT13NJDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLTOTAL-26OCT13NJDET-7|no: MOSTLY_INDEPENDENT (phi 0.14); failure: NJD offense succeeds (4+ goals)
- **Nico Hischier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13NJDET-NJAMANTHA39-1|no; why: second expression of the same thesis: KXNHLAST-26OCT13NJDET-NJAMANTHA39-1|no has the higher standalone adjusted growth (11.14 vs 8.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.058); they share one thesis budget; relationships: KXNHLAST-26OCT13NJDET-NJAMANTHA39-1|no: MOSTLY_INDEPENDENT (phi 0.058); KXNHLGOAL-26OCT13NJDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTOTAL-26OCT13NJDET-7|no: REINFORCING (phi 0.165); failure: NJD offense succeeds (4+ goals)
- **Andrew Copp: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT13NJDET-NJ3|no; why: higher confidence-adjusted growth (4.82 vs 1.71 bp); despite a smaller raw edge (+0.028 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT13NJDET-NJAMANTHA39-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTOTAL-26OCT13NJDET-7|no: INTENTIONAL_DIVERSIFIER (phi -0.127); failure: DET offense suppressed (<= 2 goals)
- **Full Game: Over 6.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT13NJDET-4|no; why: KXNHLTOTAL-26OCT13NJDET-4|no has the higher standalone adjusted growth (2.42 vs 2.41 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.372); relationships: KXNHLAST-26OCT13NJDET-NJAMANTHA39-1|no: MOSTLY_INDEPENDENT (phi 0.14); KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no: REINFORCING (phi 0.165); KXNHLGOAL-26OCT13NJDET-DETACOPP18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.127); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.07.
- thesis NJD:SUPPRESSED (p 0.4877): highest fidelity KXNHLSPREAD-26OCT13NJDET-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13NJDET-NJAMANTHA39-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:OFFENSE_4PLUS (p 0.3637): highest fidelity KXNHLSPREAD-26OCT13NJDET-NJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13NJDET-DETACOPP18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:WINS (p 0.5528): highest fidelity KXNHLSPREAD-26OCT13NJDET-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT13NJDET-NJAMANTHA39-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.2933, phi -0.208)
- KXNHLGOAL-26OCT13NJDET-NJNHISCHIER13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.2933, phi -0.229)
- KXNHLGOAL-26OCT13NJDET-DETACOPP18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4155, phi -0.221)
- KXNHLTOTAL-26OCT13NJDET-7|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2013, phi -0.645)

portfolios: A EV +1.36 (adj +0.29) on $9.37, P(profit) 0.691, adj growth 2.8 bp · B EV +0.94 (adj +0.45) on $9.77, P(profit) 0.5583, adj growth 4.4 bp · C EV +1.21 (adj +0.42) on $8.36, P(profit) 0.6131, adj growth 4.1 bp · R EV +0.16 (adj +0.07) on $2.00, P(profit) 0.5065, adj growth 2.6 bp

## FLA @ CBJ  ·  10000 joint draws  ·  412 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.547 / away 0.453

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_FLA_win | p_overtime | goals | shots CBJ/FLA | CBJ/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.68 | 0.32 | 0.00 | 6.04 | 27.4/27.1 | 24.2/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.48 | 5.9 | 27.4/27.3 | 24.1/24.2 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.089 | 0.71 | 0.29 | 0.00 | 5.94 | 32.2/21.4 | 19.0/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.63 | 0.37 | 0.00 | 9.29 | 28.9/28.7 | 23.2/22.0 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.58 | 0.42 | 0.47 | 5.84 | 32.5/21.9 | 18.9/29.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.62 | 0.38 | 0.00 | 3.46 | 25.8/25.6 | 24.2/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 16 | 0.211 | 0.197 | +0.041 | +0.027 | $1.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Danton Heinen: 1+ goals YES | 10 | 0.137 | 0.127 | +0.031 | +0.020 | $1.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 69 | 0.750 | 0.734 | +0.045 | +0.029 | $4.61 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Sandis Vilmanis: 1+ goals YES | 9 | 0.123 | 0.114 | +0.028 | +0.018 | $1.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLAST-26OCT13FLACBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (11.47 vs 6.49 bp); despite a smaller raw edge (+0.041 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13FLACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT13FLACBJ-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: CBJ offense suppressed (<= 2 goals)
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13FLACBJ-CBJCCOYLE3-2|yes; why: KXNHLAST-26OCT13FLACBJ-CBJCCOYLE3-2|yes has the higher standalone adjusted growth (13.06 vs 9.28 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.026); relationships: KXNHLGOAL-26OCT13FLACBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT13FLACBJ-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: CBJ offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13FLACBJ-FLABTKACHUK8-1|no; why: KXNHLGOAL-26OCT13FLACBJ-FLABTKACHUK8-1|no has the higher standalone adjusted growth (9.03 vs 8.77 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.002); relationships: KXNHLGOAL-26OCT13FLACBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT13FLACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT13FLACBJ-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense succeeds (4+ goals)
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13FLACBJ-FLAELUOSTARINEN27-1|yes; why: higher confidence-adjusted growth (8.15 vs 0.91 bp); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13FLACBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT13FLACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.442): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13FLACBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.3759): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13FLACBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.5): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13FLACBJ-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13FLACBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3366, phi -0.224)
- KXNHLGOAL-26OCT13FLACBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3366, phi -0.159)
- KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2887, phi -0.247)
- KXNHLGOAL-26OCT13FLACBJ-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.5, phi -0.173)

portfolios: A EV +1.39 (adj +0.40) on $9.37, P(profit) 0.6661, adj growth 3.9 bp · B EV +1.39 (adj +0.91) on $8.68, P(profit) 0.406, adj growth 8.8 bp · C EV +0.66 (adj +0.43) on $6.30, P(profit) 0.8089, adj growth 4.2 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.75, adj growth 3.1 bp

## BUF @ MTL  ·  10000 joint draws  ·  512 bet sides mapped, 6 +EV candidates, 3 on card

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
| Jiri Kulich: 1+ goals YES | 15 | 0.196 | 0.183 | +0.037 | +0.024 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ goals NO | 72 | 0.768 | 0.754 | +0.034 | +0.020 | $4.61 | FUNDED_RESEARCH | $2 | MTL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Jacob Fowler: 23+ saves YES | 48 | 0.655 | 0.516 | +0.157 | +0.019 | $2.47 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BUF:SHOT_CONTROL | DIRECT (0.88) | CALIBRATION_WARNING | D |
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13BUFMTL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (9.43 vs 0.97 bp); alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSAVE-26OCT13BUFMTL-MTLJFOWLER32-23|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: BUF offense suppressed (<= 2 goals)
- **Chris Kreider: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13BUFMTL-MTLCCAUFIELD13-1|no; why: higher confidence-adjusted growth (4.66 vs 0.69 bp); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13BUFMTL-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSAVE-26OCT13BUFMTL-MTLJFOWLER32-23|yes: MOSTLY_INDEPENDENT (phi -0.028); failure: MTL offense succeeds (4+ goals)
- **Jacob Fowler: 23+ saves YES** — thesis: BUF controls shots (share >= 0.55); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT13BUFMTL-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.028); failure: MTL net faces light volume (<= 25 shots; BUF suppressed)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.3475): highest fidelity KXNHLGOAL-26OCT13BUFMTL-BUFJKULICH20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BUFMTL-BUFJKULICH20-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3452): highest fidelity KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.3343): highest fidelity KXNHLGOAL-26OCT13BUFMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BUFMTL-MTLJEVANS71-1|yes (same contract)
- KXNHLGOAL-26OCT13BUFMTL-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.4412, phi -0.223)
- KXNHLGOAL-26OCT13BUFMTL-MTLCKREIDER22-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4323, phi -0.223)
- KXNHLSAVE-26OCT13BUFMTL-MTLJFOWLER32-23|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.5 pts; fragile player expression; opposing: failure thesis MTL:NET_LOW_VOLUME (p 0.324, phi -0.768)

portfolios: A EV +1.50 (adj +0.46) on $9.37, P(profit) 0.499, adj growth 4.5 bp · B EV +1.36 (adj +0.46) on $8.68, P(profit) 0.6019, adj growth 4.5 bp · C EV +1.43 (adj +0.49) on $9.08, P(profit) 0.6019, adj growth 4.7 bp · R EV +0.09 (adj +0.06) on $2.00, P(profit) 0.7676, adj growth 2.1 bp

## WSH @ CAR  ·  10000 joint draws  ·  460 bet sides mapped, 7 +EV candidates, 3 on card

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
| Sebastian Aho: 2+ assists NO | 87 | 0.937 | 0.901 | +0.059 | +0.023 | $4.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CAR:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Boone Jenner: 1+ goals YES | 14 | 0.177 | 0.166 | +0.029 | +0.018 | $1.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13WSHCAR-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (11.66 vs 6.10 bp); despite a smaller raw edge (+0.043 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT13WSHCAR-CARSAHO20-2|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT13WSHCAR-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: WSH offense suppressed (<= 2 goals)
- **Sebastian Aho: 2+ assists NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no; why: higher confidence-adjusted growth (11.14 vs 3.64 bp); despite a smaller raw edge (+0.059 vs +0.109/contract); relationships: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT13WSHCAR-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: CAR offense succeeds (4+ goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (11.66 vs 5.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT13WSHCAR-CARSAHO20-2|no: MOSTLY_INDEPENDENT (phi -0.011); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.339): highest fidelity KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes — Player prop expression KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes selected over player prop KXNHLAST-26OCT13WSHCAR-WSHAOVECHKIN8-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.53 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CAR:SUPPRESSED (p 0.3382): highest fidelity KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no (same contract)
- KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4482, phi -0.221)
- KXNHLAST-26OCT13WSHCAR-CARSAHO20-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4425, phi -0.201)
- KXNHLGOAL-26OCT13WSHCAR-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4482, phi -0.185)
- override: Player prop expression KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes selected over player prop KXNHLAST-26OCT13WSHCAR-WSHAOVECHKIN8-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.53 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.62 (adj +0.47) on $9.37, P(profit) 0.5292, adj growth 4.5 bp · B EV +0.95 (adj +0.54) on $7.53, P(profit) 0.3507, adj growth 5.3 bp · C EV +1.02 (adj +0.41) on $4.82, P(profit) 0.7373, adj growth 4.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ PHI  ·  10000 joint draws  ·  510 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.516 / away 0.484

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
| Ryan Winterton: 1+ goals YES | 10 | 0.143 | 0.131 | +0.037 | +0.025 | $1.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jared McCann: 1+ goals NO | 72 | 0.785 | 0.767 | +0.051 | +0.033 | $4.42 | FUNDED_RESEARCH | $2 | SEA:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 75 | 0.805 | 0.790 | +0.042 | +0.027 | $4.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 16 | 0.202 | 0.190 | +0.032 | +0.021 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:WINS_BY_2PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (13.72 vs 2.64 bp); despite a smaller raw edge (+0.037 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT13SEAPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: SEA offense suppressed (<= 2 goals)
- **Jared McCann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no; why: higher confidence-adjusted growth (12.56 vs 9.20 bp); relationships: KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT13SEAPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: SEA offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13SEAPHI-PHIDJIRICEK55-1|no; why: higher confidence-adjusted growth (8.63 vs 1.43 bp); despite a smaller raw edge (+0.042 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: PHI offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI wins by 2+; alternative: KXNHLPTS-26OCT13SEAPHI-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (6.58 vs 0.00 bp); despite a smaller raw edge (+0.032 vs +0.069/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0003 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT13SEAPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, PHI shot control · normal event (5-7) · decided (2+) 0.08.
- thesis SEA:SUPPRESSED (p 0.4596): highest fidelity KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no (same contract)
- thesis PHI:SUPPRESSED (p 0.4097): highest fidelity KXNHLGOAL-26OCT13SEAPHI-PHIPMARTONE94-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13SEAPHI-PHIPMARTONE94-1|no (same contract)
- thesis PHI:WINS_BY_2PLUS (p 0.3043): highest fidelity KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes (same contract)
- KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4596, phi -0.194)
- KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.324, phi -0.214)
- KXNHLGOAL-26OCT13SEAPHI-PHIPMARTONE94-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3719, phi -0.194)
- KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4097, phi -0.222)

portfolios: A EV +1.32 (adj +0.39) on $9.37, P(profit) 0.516, adj growth 3.8 bp · B EV +1.27 (adj +0.84) on $11.52, P(profit) 0.742, adj growth 8.1 bp · C EV +1.10 (adj +0.62) on $12.05, P(profit) 0.6981, adj growth 6.1 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.7849, adj growth 3.5 bp

## TBL @ NYR  ·  10000 joint draws  ·  462 bet sides mapped, 20 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.412 / away 0.588

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
| Gabe Perreault: 1+ assists YES | 22 | 0.310 | 0.263 | +0.078 | +0.031 | $1.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 76 | 0.841 | 0.798 | +0.068 | +0.025 | $4.61 | FUNDED_RESEARCH | $2 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ assists NO | 71 | 0.767 | 0.736 | +0.042 | +0.011 | $3.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (11.40 vs 8.11 bp); relationships: KXNHLSPREAD-26OCT13TBNYR-TB3|no: MOSTLY_INDEPENDENT (phi 0.124); KXNHLAST-26OCT13TBNYR-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.059); failure: NYR offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR3|yes; why: Broad expression KXNHLSPREAD-26OCT13TBNYR-TB3|no selected over player prop KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.124); KXNHLAST-26OCT13TBNYR-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.1); failure: TBL wins by 2+
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT13TBNYR-4|no; why: higher confidence-adjusted growth (1.45 vs 0.15 bp); wins across more scripts (relative breadth 0.992 vs 0.366); alternative not eligible: confidence-adjusted EV +0.0029 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.059); KXNHLSPREAD-26OCT13TBNYR-TB3|no: INTENTIONAL_DIVERSIFIER (phi -0.1); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis NYR:OFFENSE_4PLUS (p 0.3635): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [DIRECT], best adjusted EV KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes — Broad expression KXNHLSPREAD-26OCT13TBNYR-NYR2|yes selected over player prop KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.62 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis TBL:SUPPRESSED (p 0.4344): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no — Broad expression KXNHLSPREAD-26OCT13TBNYR-TB3|no selected over player prop KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYR:WINS (p 0.5102): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13TBNYR-TB3|no (same contract)
- KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4186, phi -0.267)
- KXNHLSPREAD-26OCT13TBNYR-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2646, phi -0.725)
- KXNHLAST-26OCT13TBNYR-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3635, phi -0.208)
- override: Broad expression KXNHLSPREAD-26OCT13TBNYR-TB3|no selected over player prop KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26OCT13TBNYR-NYR2|yes selected over player prop KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.62 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.27 (adj +0.31) on $9.37, P(profit) 0.5764, adj growth 2.9 bp · B EV +1.24 (adj +0.45) on $10.12, P(profit) 0.7319, adj growth 4.4 bp · C EV +1.96 (adj +0.61) on $12.05, P(profit) 0.6125, adj growth 5.9 bp · R EV +0.18 (adj +0.07) on $2.00, P(profit) 0.8409, adj growth 2.5 bp

## STL @ OTT  ·  10000 joint draws  ·  452 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.490 / away 0.510

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
| Michael Amadio: 1+ goals YES | 13 | 0.176 | 0.164 | +0.038 | +0.026 | $1.66 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 71 | 0.842 | 0.753 | +0.117 | +0.028 | $4.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Philip Broberg: 1+ assists YES | 25 | 0.338 | 0.289 | +0.075 | +0.026 | $1.78 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Tim Stutzle: 1+ assists NO | 53 | 0.605 | 0.565 | +0.058 | +0.018 | $2.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13STLOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (11.87 vs 1.42 bp); despite a smaller raw edge (+0.038 vs +0.083/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT13STLOTT-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no: INTENTIONAL_DIVERSIFIER (phi -0.068); failure: OTT offense suppressed (<= 2 goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (8.93 vs 2.71 bp); relationships: KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT13STLOTT-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.067); failure: OTT offense succeeds (4+ goals)
- **Philip Broberg: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13STLOTT-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (7.50 vs 2.25 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: STL offense suppressed (<= 2 goals)
- **Tim Stutzle: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-2|no; why: higher confidence-adjusted growth (2.71 vs 0.28 bp); alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.067); KXNHLAST-26OCT13STLOTT-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.3804): highest fidelity KXNHLPTS-26OCT13STLOTT-OTTJSPENCE10-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3574): highest fidelity KXNHLAST-26OCT13STLOTT-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13STLOTT-STLPBROBERG6-1|yes (same contract)
- thesis STL:SUPPRESSED (p 0.4246): highest fidelity KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no (same contract)
- KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3905, phi -0.204)
- KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3804, phi -0.19)
- KXNHLAST-26OCT13STLOTT-STLPBROBERG6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4246, phi -0.27)
- KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3804, phi -0.282)

portfolios: A EV +2.63 (adj +0.51) on $9.37, P(profit) 0.5633, adj growth 4.7 bp · B EV +1.95 (adj +0.74) on $10.35, P(profit) 0.7283, adj growth 7.2 bp · C EV +1.73 (adj +0.71) on $10.84, P(profit) 0.6974, adj growth 6.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ NYI  ·  10000 joint draws  ·  414 bet sides mapped, 17 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.647 / away 0.352

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
| Drew O'Connor: 1+ goals YES | 13 | 0.185 | 0.170 | +0.047 | +0.032 | $1.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Bo Horvat: 1+ goals NO | 61 | 0.663 | 0.648 | +0.036 | +0.022 | $3.35 | FUNDED_RESEARCH | $1 | NYI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (18.69 vs 3.94 bp); relationships: KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: VAN offense suppressed (<= 2 goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no; why: higher confidence-adjusted growth (4.45 vs 3.86 bp); relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: NYI offense succeeds (4+ goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:SUPPRESSED (p 0.3313): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.3174): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT13VANNYI-NYI3|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.4506): highest fidelity KXNHLAST-26OCT13VANNYI-NYICRITCHIE64-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13VANNYI-NYICRITCHIE64-1|yes (same contract)
- KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.465, phi -0.202)
- KXNHLGOAL-26OCT13VANNYI-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.4506, phi -0.264)

portfolios: A EV +1.05 (adj +0.23) on $9.37, P(profit) 0.6974, adj growth 2.2 bp · B EV +0.88 (adj +0.58) on $5.34, P(profit) 0.7279, adj growth 5.6 bp · C EV +0.91 (adj +0.38) on $9.09, P(profit) 0.7171, adj growth 3.7 bp · R EV +0.06 (adj +0.03) on $1.00, P(profit) 0.6629, adj growth 1.3 bp

## PIT @ CHI  ·  10000 joint draws  ·  408 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.413 / away 0.587

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_PIT_win | p_overtime | goals | shots CHI/PIT | CHI/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.43 | 0.57 | 0.00 | 6.01 | 26.8/27.3 | 23.4/23.6 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.112 | 0.38 | 0.62 | 0.00 | 6.03 | 21.2/32.7 | 28.2/18.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.46 | 5.95 | 26.9/27.4 | 24.2/23.6 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.42 | 0.58 | 0.49 | 5.94 | 21.2/32.6 | 29.2/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.46 | 0.54 | 0.00 | 9.33 | 28.2/28.9 | 22.1/22.2 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.076 | 0.32 | 0.68 | 0.00 | 9.28 | 22.7/34.4 | 26.3/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 12 | 0.190 | 0.171 | +0.063 | +0.044 | $2.64 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 53 | 0.722 | 0.591 | +0.174 | +0.043 | $4.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Anton Frondell: 1+ assists YES | 27 | 0.352 | 0.308 | +0.068 | +0.025 | $1.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Connor Dewar: 1+ goals YES | 13 | 0.165 | 0.155 | +0.027 | +0.017 | $1.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes; why: higher confidence-adjusted growth (36.84 vs 6.45 bp); despite a smaller raw edge (+0.063 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.059); KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.034); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13PITCHI-CHIRKANTSEROV80-1|no; why: higher confidence-adjusted growth (16.45 vs 3.45 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.076); KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CHI offense succeeds (4+ goals)
- **Anton Frondell: 1+ assists YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes has the higher standalone adjusted growth (36.84 vs 6.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.059); they share one thesis budget; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.059); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.076); KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: CHI offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13PITCHI-PITECHINAKHOV59-1|yes; why: higher confidence-adjusted growth (5.08 vs 1.85 bp); despite a smaller raw edge (+0.027 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.034); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.362): highest fidelity KXNHLAST-26OCT13PITCHI-CHITBERTUZZI59-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4247): highest fidelity KXNHLGOAL-26OCT13PITCHI-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.4347): highest fidelity KXNHLAST-26OCT13PITCHI-PITECHINAKHOV59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4247, phi -0.235)
- KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.2 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.362, phi -0.247)
- KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4247, phi -0.292)
- KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3451, phi -0.192)

portfolios: A EV +2.36 (adj +0.56) on $9.37, P(profit) 0.7065, adj growth 5.4 bp · B EV +3.41 (adj +1.56) on $10.15, P(profit) 0.4627, adj growth 15.2 bp · C EV +3.50 (adj +1.60) on $11.83, P(profit) 0.634, adj growth 15.5 bp · R EV +0.49 (adj +0.35) on $1.00, P(profit) 0.1902, adj growth 13.1 bp

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
| Neal Pionk: 1+ goals NO | 87 | 0.932 | 0.915 | +0.054 | +0.037 | $4.61 | FUNDED_RESEARCH | $2 | WPG:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Rieger Lorenz: 1+ goals YES | 10 | 0.135 | 0.125 | +0.029 | +0.019 | $1.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 23 | 0.305 | 0.260 | +0.063 | +0.018 | $1.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Matt Boldy: 1+ goals NO | 63 | 0.678 | 0.665 | +0.032 | +0.018 | $3.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13MINWPG-WPGNPIONK4-2|no; why: higher confidence-adjusted growth (29.63 vs 0.51 bp); despite a smaller raw edge (+0.054 vs +0.065/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: WPG offense succeeds (4+ goals)
- **Rieger Lorenz: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (8.10 vs 3.71 bp); despite a smaller raw edge (+0.029 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13MINWPG-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (3.71 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no: INTENTIONAL_DIVERSIFIER (phi -0.068); failure: MIN offense suppressed (<= 2 goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no; why: higher confidence-adjusted growth (3.21 vs 2.23 bp); relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.068); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:OFFENSE_4PLUS (p 0.3661): highest fidelity KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.4173): highest fidelity KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no (same contract)
- thesis WPG:SUPPRESSED (p 0.3874): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3878, phi -0.116)
- KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4173, phi -0.146)
- KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4173, phi -0.274)
- KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3661, phi -0.268)

portfolios: A EV +1.09 (adj +0.39) on $9.37, P(profit) 0.6307, adj growth 3.8 bp · B EV +1.08 (adj +0.58) on $10.22, P(profit) 0.3918, adj growth 5.7 bp · C EV +0.62 (adj +0.27) on $9.56, P(profit) 0.771, adj growth 2.6 bp · R EV +0.12 (adj +0.09) on $2.00, P(profit) 0.9322, adj growth 3.4 bp

## COL @ DAL  ·  10000 joint draws  ·  406 bet sides mapped, 11 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.517 / away 0.483

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
| Zachary L'Heureux: 1+ goals YES | 9 | 0.136 | 0.123 | +0.040 | +0.027 | $1.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 20 | 0.256 | 0.241 | +0.045 | +0.030 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 59 | 0.630 | 0.618 | +0.023 | +0.011 | $1.58 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Zachary L'Heureux: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (18.08 vs 11.33 bp); despite a smaller raw edge (+0.040 vs +0.045/contract); relationships: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: COL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (11.33 vs 2.51 bp); relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: COL offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no; why: Player prop expression KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.81 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: COL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4057): highest fidelity KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.4216): highest fidelity KXNHLAST-26OCT13COLDAL-DALMRANTANEN96-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT13COLDAL-DALMHEISKANEN4-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.3802): highest fidelity KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no (same contract)
- KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3802, phi -0.18)
- KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3802, phi -0.232)
- KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4057, phi -0.286)
- override: Player prop expression KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.81 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +0.96 (adj +0.40) on $9.37, P(profit) 0.5428, adj growth 3.9 bp · B EV +1.13 (adj +0.75) on $5.15, P(profit) 0.3561, adj growth 7.2 bp · C EV +0.98 (adj +0.45) on $9.92, P(profit) 0.7191, adj growth 4.4 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6302, adj growth 0.7 bp

## VGK @ NSH  ·  10000 joint draws  ·  466 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.467 / away 0.533

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
| Mitch Marner: 1+ goals NO | 71 | 0.762 | 0.748 | +0.037 | +0.023 | $3.86 | FUNDED_RESEARCH | $1 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Brady Skjei: 1+ assists YES | 23 | 0.308 | 0.264 | +0.066 | +0.022 | $1.47 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Shea Theodore: 1+ assists YES | 28 | 0.350 | 0.313 | +0.056 | +0.019 | $1.71 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
| Jack Eichel: 1+ goals NO | 68 | 0.726 | 0.713 | +0.030 | +0.018 | $3.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13VGKNSH-VGKTCONNELLY24-1|no; why: higher confidence-adjusted growth (5.85 vs 5.05 bp); despite a smaller raw edge (+0.037 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.101); KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: VGK offense succeeds (4+ goals)
- **Brady Skjei: 1+ assists YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT13VGKNSH-VGK3|no; why: higher confidence-adjusted growth (5.52 vs 0.81 bp); alternative not eligible: confidence-adjusted EV +0.0076 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: NSH offense suppressed (<= 2 goals)
- **Shea Theodore: 1+ assists YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13VGKNSH-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (3.64 vs 0.10 bp); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.101); KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: VGK offense suppressed (<= 2 goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no; why: Player prop expression KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.86 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.4121): highest fidelity KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no — Player prop expression KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.86 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NSH:OFFENSE_4PLUS (p 0.3848): highest fidelity KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.3696): highest fidelity KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes (same contract)
- KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3696, phi -0.231)
- KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3975, phi -0.259)
- KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.4121, phi -0.284)
- KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3696, phi -0.24)
- override: Player prop expression KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.86 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.82 (adj +0.39) on $9.37, P(profit) 0.5595, adj growth 3.7 bp · B EV +1.06 (adj +0.44) on $10.10, P(profit) 0.5166, adj growth 4.3 bp · C EV +0.99 (adj +0.40) on $8.04, P(profit) 0.4417, adj growth 3.9 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.7616, adj growth 1.2 bp

## TOR @ UTA  ·  10000 joint draws  ·  444 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.590 / away 0.410

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
| Vincent Trocheck: 1+ assists NO | 70 | 0.788 | 0.739 | +0.073 | +0.024 | $4.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Easton Cowan: 1+ assists YES | 24 | 0.310 | 0.270 | +0.057 | +0.017 | $1.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
| Dylan Guenther: 1+ goals NO | 62 | 0.669 | 0.655 | +0.032 | +0.019 | $2.63 | FUNDED_RESEARCH | $1 | UTA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Darren Raddysh: 1+ assists NO | 58 | 0.681 | 0.612 | +0.084 | +0.015 | $2.44 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (6.43 vs 3.32 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: UTA offense succeeds (4+ goals)
- **Easton Cowan: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13TORUTA-TORWNYLANDER88-1|yes; why: higher confidence-adjusted growth (3.44 vs 0.02 bp); alternative not eligible: confidence-adjusted EV +0.0015 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi -0.036); failure: TOR offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13TORUTA-UTANSCHMALTZ8-1|no; why: higher confidence-adjusted growth (3.32 vs 0.45 bp); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi -0.022); failure: UTA offense succeeds (4+ goals)
- **Darren Raddysh: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no; why: higher confidence-adjusted growth (2.02 vs 1.50 bp); relationships: KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.022); failure: TOR offense succeeds (4+ goals)

**Review**: scripts UTA shot control · normal event (5-7) · decided (2+) 0.14, UTA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · high event (8+) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3266): highest fidelity KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3113): highest fidelity KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no (same contract)
- thesis TOR:SUPPRESSED (p 0.4531): highest fidelity KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4845, phi -0.189)
- KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4531, phi -0.283)
- KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4845, phi -0.243)
- KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.6 pts; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3266, phi -0.263)

portfolios: A EV +1.27 (adj +0.34) on $9.38, P(profit) 0.5885, adj growth 3.3 bp · B EV +1.19 (adj +0.37) on $10.59, P(profit) 0.5234, adj growth 3.6 bp · C EV +0.82 (adj +0.25) on $7.06, P(profit) 0.5916, adj growth 2.4 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.6686, adj growth 1.1 bp

## CGY @ ANA  ·  10000 joint draws  ·  480 bet sides mapped, 11 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.612 / away 0.388

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
| Tim Washe: 1+ goals YES | 10 | 0.149 | 0.136 | +0.043 | +0.029 | $1.73 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 10 | 0.140 | 0.127 | +0.033 | +0.021 | $1.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Nikita Nesterenko: 1+ assists NO | 74 | 0.807 | 0.766 | +0.054 | +0.013 | $4.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | ANA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (19.09 vs 7.49 bp); despite a smaller raw edge (+0.043 vs +0.092/contract); relationships: KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT13CGYANA-ANANNESTERENKO13-1|no: MOSTLY_INDEPENDENT (phi -0.034); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (9.79 vs 7.49 bp); despite a smaller raw edge (+0.033 vs +0.092/contract); relationships: KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT13CGYANA-ANANNESTERENKO13-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: ANA offense suppressed (<= 2 goals)
- **Nikita Nesterenko: 1+ assists NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13CGYANA-ANANNESTERENKO13-1|no; why: higher confidence-adjusted growth (1.90 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: ANA offense succeeds (4+ goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.497): highest fidelity KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:SUPPRESSED (p 0.4821): highest fidelity KXNHLAST-26OCT13CGYANA-CGYSNEMEC71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13CGYANA-CGYSNEMEC71-1|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3057): highest fidelity KXNHLPTS-26OCT13CGYANA-CGYZWHITECLOUD28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13CGYANA-CGYASUNIEV61-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.137)
- KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.147)
- KXNHLAST-26OCT13CGYANA-ANANNESTERENKO13-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.497, phi -0.181)

portfolios: A EV +4.27 (adj +0.71) on $9.37, P(profit) 0.6299, adj growth 6.5 bp · B EV +1.37 (adj +0.78) on $6.98, P(profit) 0.2687, adj growth 7.6 bp · C EV +0.95 (adj +0.24) on $5.19, P(profit) 0.8364, adj growth 2.3 bp · R EV +0.40 (adj +0.27) on $1.00, P(profit) 0.149, adj growth 10.1 bp

## EDM @ LAK  ·  10000 joint draws  ·  424 bet sides mapped, 13 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.464 / away 0.536

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
| Artemi Panarin: 2+ assists NO | 82 | 0.910 | 0.862 | +0.080 | +0.032 | $4.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Kasperi Kapanen: 1+ assists YES | 25 | 0.334 | 0.289 | +0.070 | +0.026 | $1.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 48 | 0.613 | 0.523 | +0.115 | +0.026 | $2.37 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Artemi Panarin: 2+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (16.26 vs 5.80 bp); despite a smaller raw edge (+0.080 vs +0.115/contract); relationships: KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: DUPLICATIVE (phi 0.396); failure: LAK offense succeeds (4+ goals)
- **Kasperi Kapanen: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (7.64 vs 1.54 bp); relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: EDM offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no; why: second expression of the same thesis: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no has the higher standalone adjusted growth (16.26 vs 5.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.396); they share one thesis budget; relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: DUPLICATIVE (phi 0.396); KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4138): highest fidelity KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.395): highest fidelity KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3893): highest fidelity KXNHLPTS-26OCT13EDMLA-EDMLDRAISAITL29-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3679, phi -0.251)
- KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3893, phi -0.258)
- KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.8 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3679, phi -0.265)

portfolios: A EV +2.51 (adj +0.36) on $9.37, P(profit) 0.7121, adj growth 3.4 bp · B EV +1.48 (adj +0.48) on $8.78, P(profit) 0.7128, adj growth 4.7 bp · C EV +2.10 (adj +0.54) on $10.00, P(profit) 0.7627, adj growth 5.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ SJS  ·  10000 joint draws  ·  536 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.468 / away 0.532

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_BOS_win | p_overtime | goals | shots SJS/BOS | SJS/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.51 | 0.49 | 0.00 | 6.04 | 27.2/27.2 | 23.6/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.49 | 0.51 | 0.47 | 5.98 | 27.3/27.2 | 23.9/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.47 | 0.53 | 0.00 | 9.37 | 28.6/28.6 | 22.3/22.8 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.081 | 0.54 | 0.46 | 0.00 | 6.03 | 32.1/21.6 | 18.4/28.3 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.55 | 0.45 | 0.45 | 5.94 | 32.3/21.7 | 18.6/29.0 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.059 | 0.44 | 0.56 | 0.00 | 6.04 | 21.7/31.9 | 27.8/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kiefer Sherwood: 1+ goals YES | 16 | 0.215 | 0.200 | +0.046 | +0.031 | $1.96 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Casey Mittelstadt: 1+ goals YES | 14 | 0.185 | 0.172 | +0.036 | +0.024 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Charlie McAvoy: 1+ assists NO | 55 | 0.703 | 0.600 | +0.136 | +0.033 | $4.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Marat Khusnutdinov: 1+ goals YES | 11 | 0.148 | 0.137 | +0.031 | +0.020 | $1.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13BOSSJ-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (14.59 vs 5.38 bp); despite a smaller raw edge (+0.046 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SJS offense suppressed (<= 2 goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13BOSSJ-BOSNZADOROV91-1|yes; why: higher confidence-adjusted growth (9.81 vs 0.01 bp); despite a smaller raw edge (+0.036 vs +0.052/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0006 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: BOS offense suppressed (<= 2 goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (9.75 vs 2.84 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.047); failure: BOS offense succeeds (4+ goals)
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes has the higher standalone adjusted growth (9.81 vs 8.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi -0.047); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4005): highest fidelity KXNHLAST-26OCT13BOSSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.401): highest fidelity KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.385): highest fidelity KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3796, phi -0.207)
- KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.385, phi -0.189)
- KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.401, phi -0.228)
- KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.385, phi -0.171)

portfolios: A EV +2.15 (adj +0.33) on $9.37, P(profit) 0.6023, adj growth 3.2 bp · B EV +2.37 (adj +1.11) on $9.43, P(profit) 0.4519, adj growth 10.7 bp · C EV +2.54 (adj +0.95) on $12.05, P(profit) 0.7267, adj growth 9.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
