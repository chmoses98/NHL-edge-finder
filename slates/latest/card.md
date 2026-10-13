# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-13T16:34:43Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.24 | +26.33 | +6.46 | +25.78 | 0.868 | -3.90 | -11.85 | 61.74 |
| B thesis-diversified (joint) ← optimiser card | 144.53 | +19.05 | +7.93 | +18.07 | 0.822 | -6.41 | -13.73 | 77.11 |
| C best expression per thesis | 147.25 | +20.16 | +7.47 | +19.32 | 0.816 | -7.93 | -15.69 | 72.26 |
| R FUNDED research stakes | 24.00 | +2.23 | +1.20 | +1.49 | 0.608 | -4.85 | -6.59 | 0.00 |

## NJD @ DET  ·  10000 joint draws  ·  400 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

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
| Timo Meier: 1+ goals NO | 74 | 0.790 | 0.775 | +0.037 | +0.022 | $3.92 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 65 | 0.704 | 0.689 | +0.038 | +0.024 | $3.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Dylan Larkin: 1+ assists NO | 58 | 0.659 | 0.610 | +0.062 | +0.012 | $1.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
| Dylan Larkin: 1+ goals NO | 67 | 0.709 | 0.697 | +0.023 | +0.011 | $1.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13NJDET-NJAMANTHA39-1|no; why: Player prop expression KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13NJDET-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: NJD offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no has the higher standalone adjusted growth (5.69 vs 5.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: NJD offense succeeds (4+ goals)
- **Dylan Larkin: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13NJDET-DETVARVIDSSON33-1|no; why: KXNHLAST-26OCT13NJDET-DETVARVIDSSON33-1|no has the higher standalone adjusted growth (3.31 vs 1.41 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.093); relationships: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT13NJDET-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: DET offense succeeds (4+ goals)
- **Dylan Larkin: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13NJDET-DETVARVIDSSON33-1|no; why: Player prop expression KXNHLGOAL-26OCT13NJDET-DETDLARKIN71-1|no selected over player prop KXNHLAST-26OCT13NJDET-DETVARVIDSSON33-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.84 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13NJDET-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT13NJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.07.
- thesis NJD:SUPPRESSED (p 0.4877): highest fidelity KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13NJDET-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis GAME:LOW_EVENT (p 0.2976): highest fidelity KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT13NJDET-NJ5|no (same contract)
- thesis DET:WINS (p 0.5528): highest fidelity KXNHLSPREAD-26OCT13NJDET-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.2933, phi -0.243)
- KXNHLGOAL-26OCT13NJDET-NJJHUGHES86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.2933, phi -0.241)
- KXNHLAST-26OCT13NJDET-DETDLARKIN71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3637, phi -0.269)
- KXNHLGOAL-26OCT13NJDET-DETDLARKIN71-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3637, phi -0.235)
- override: Player prop expression KXNHLGOAL-26OCT13NJDET-DETDLARKIN71-1|no selected over player prop KXNHLAST-26OCT13NJDET-DETVARVIDSSON33-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.84 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT13NJDET-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT13NJDET-NJJHUGHES86-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.00 (adj +0.33) on $10.01, P(profit) 0.5522, adj growth 3.1 bp · B EV +0.63 (adj +0.30) on $10.92, P(profit) 0.6089, adj growth 2.9 bp · C EV +1.03 (adj +0.32) on $12.25, P(profit) 0.5157, adj growth 3.2 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.7905, adj growth 1.1 bp

## FLA @ CBJ  ·  10000 joint draws  ·  410 bet sides mapped, 10 +EV candidates, 3 on card

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
| Sam Reinhart: 1+ goals NO | 69 | 0.755 | 0.738 | +0.050 | +0.033 | $4.79 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 84 | 0.894 | 0.865 | +0.045 | +0.015 | $4.79 | FUNDED_RESEARCH | $2 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Charlie Coyle: 1+ goals YES | 23 | 0.273 | 0.260 | +0.030 | +0.017 | $1.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13FLACBJ-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (11.42 vs 4.47 bp); relationships: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT13FLACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13FLACBJ-FLA2|no; why: higher confidence-adjusted growth (4.01 vs 3.30 bp); despite a smaller raw edge (+0.045 vs +0.051/contract); relationships: KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT13FLACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.111); failure: FLA wins by 2+
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT13FLACBJ-FLA3|no has the higher standalone adjusted growth (4.01 vs 3.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.111); they share one thesis budget; relationships: KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.111); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4996): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS (p 0.6142): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13FLACBJ-FLA2|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.4413): highest fidelity KXNHLSPREAD-26OCT13FLACBJ-FLA3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13FLACBJ-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13FLACBJ-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2872, phi -0.238)
- KXNHLSPREAD-26OCT13FLACBJ-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.1858, phi -0.72)
- KXNHLGOAL-26OCT13FLACBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3401, phi -0.224)

portfolios: A EV +1.33 (adj +0.28) on $10.01, P(profit) 0.6761, adj growth 2.6 bp · B EV +0.74 (adj +0.39) on $10.71, P(profit) 0.702, adj growth 3.8 bp · C EV +0.70 (adj +0.36) on $11.27, P(profit) 0.6948, adj growth 3.5 bp · R EV +0.25 (adj +0.13) on $4.00, P(profit) 0.6948, adj growth 5.0 bp

## BUF @ MTL  ·  10000 joint draws  ·  408 bet sides mapped, 4 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

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
| Owen Power: 1+ goals NO | 88 | 0.921 | 0.908 | +0.033 | +0.021 | $4.79 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 69 | 0.753 | 0.719 | +0.048 | +0.014 | $3.01 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
| Nick Suzuki: 1+ assists NO | 43 | 0.498 | 0.462 | +0.051 | +0.014 | $1.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.72) | EVIDENCE_MIXED | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13BUFMTL-BUFTTHOMPSON72-2|no; why: higher confidence-adjusted growth (9.43 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT13BUFMTL-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: BUF offense succeeds (4+ goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13BUFMTL-MTLNSUZUKI14-1|no; why: higher confidence-adjusted growth (2.09 vs 1.84 bp); despite a smaller raw edge (+0.048 vs +0.051/contract); relationships: KXNHLGOAL-26OCT13BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT13BUFMTL-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.068); failure: MTL offense succeeds (4+ goals)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no; why: second expression of the same thesis: KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no has the higher standalone adjusted growth (2.09 vs 1.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.068); they share one thesis budget; relationships: KXNHLGOAL-26OCT13BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.068); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.10.
- thesis MTL:WINS_BY_2PLUS (p 0.3343): highest fidelity KXNHLGOAL-26OCT13BUFMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BUFMTL-MTLJEVANS71-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3452): highest fidelity KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13BUFMTL-MTLNSUZUKI14-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.4412): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT13BUFMTL-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3475, phi -0.127)
- KXNHLAST-26OCT13BUFMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4323, phi -0.219)
- KXNHLAST-26OCT13BUFMTL-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 28% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4323, phi -0.301)

portfolios: A EV +0.84 (adj +0.32) on $10.01, P(profit) 0.5714, adj growth 3.1 bp · B EV +0.55 (adj +0.22) on $9.27, P(profit) 0.6923, adj growth 2.1 bp · C EV +0.26 (adj +0.07) on $3.74, P(profit) 0.7531, adj growth 0.7 bp · R EV +0.07 (adj +0.05) on $2.00, P(profit) 0.9206, adj growth 1.8 bp

## WSH @ CAR  ·  10000 joint draws  ·  464 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

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
| Ethen Frank: 1+ goals YES | 9 | 0.129 | 0.116 | +0.033 | +0.020 | $1.21 | FUNDED_RESEARCH | $1 | WSH:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.224 | 0.204 | +0.044 | +0.025 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Jordan Kyrou: 1+ assists NO | 74 | 0.800 | 0.767 | +0.046 | +0.014 | $4.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Ryan Leonard: 1+ goals YES | 18 | 0.214 | 0.203 | +0.024 | +0.013 | $1.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Ethen Frank: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes; why: higher confidence-adjusted growth (9.66 vs 8.86 bp); despite a smaller raw edge (+0.033 vs +0.044/contract); relationships: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT13WSHCAR-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.076); KXNHLGOAL-26OCT13WSHCAR-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: WSH offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13WSHCAR-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (8.86 vs 2.24 bp); relationships: KXNHLGOAL-26OCT13WSHCAR-WSHEFRANK53-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT13WSHCAR-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.096); KXNHLGOAL-26OCT13WSHCAR-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: WSH offense suppressed (<= 2 goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13WSHCAR-WSHJKYROU25-1|no; why: higher confidence-adjusted growth (2.28 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13WSHCAR-WSHEFRANK53-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.076); KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.096); KXNHLGOAL-26OCT13WSHCAR-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.147); failure: WSH offense succeeds (4+ goals)
- **Ryan Leonard: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (8.86 vs 2.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT13WSHCAR-WSHEFRANK53-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT13WSHCAR-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.147); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.11.
- thesis WSH:OFFENSE_4PLUS (p 0.3385): highest fidelity KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:SUPPRESSED (p 0.4469): highest fidelity KXNHLAST-26OCT13WSHCAR-WSHJKYROU25-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13WSHCAR-WSHJKYROU25-1|no (same contract)
- thesis CAR:OFFENSE_4PLUS (p 0.4568): highest fidelity KXNHLAST-26OCT13WSHCAR-CARKMILLER19-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13WSHCAR-CARKMILLER19-1|yes (same contract)
- KXNHLGOAL-26OCT13WSHCAR-WSHEFRANK53-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4469, phi -0.174)
- KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4469, phi -0.248)
- KXNHLAST-26OCT13WSHCAR-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.3385, phi -0.232)
- KXNHLGOAL-26OCT13WSHCAR-WSHRLEONARD9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4469, phi -0.228)

portfolios: A EV +1.48 (adj +0.54) on $10.01, P(profit) 0.5913, adj growth 5.2 bp · B EV +1.29 (adj +0.65) on $8.87, P(profit) 0.4304, adj growth 6.3 bp · C EV +0.97 (adj +0.42) on $8.28, P(profit) 0.4405, adj growth 4.0 bp · R EV +0.35 (adj +0.21) on $1.00, P(profit) 0.129, adj growth 7.3 bp

## SEA @ PHI  ·  10000 joint draws  ·  446 bet sides mapped, 7 +EV candidates, 3 on card

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
| Bobby McMann: 1+ goals NO | 71 | 0.780 | 0.761 | +0.056 | +0.037 | $3.59 | FUNDED_RESEARCH | $1 | SEA:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Jared McCann: 1+ goals NO | 73 | 0.785 | 0.767 | +0.041 | +0.024 | $3.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ assists YES | 25 | 0.317 | 0.276 | +0.054 | +0.013 | $1.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
- **Bobby McMann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (15.14 vs 6.46 bp); relationships: KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.068); failure: SEA offense succeeds (4+ goals)
- **Jared McCann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no has the higher standalone adjusted growth (15.14 vs 6.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.057); failure: SEA offense succeeds (4+ goals)
- **Kaapo Kakko: 1+ assists YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13SEAPHI-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (1.85 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: INTENTIONAL_DIVERSIFIER (phi -0.057); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, PHI shot control · normal event (5-7) · decided (2+) 0.08.
- thesis SEA:SUPPRESSED (p 0.4596): highest fidelity KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.324): highest fidelity KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes (same contract)
- thesis PHI:WINS_BY_2PLUS (p 0.3043): highest fidelity KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes (same contract)
- KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.324, phi -0.211)
- KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.324, phi -0.214)
- KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4596, phi -0.277)

portfolios: A EV +1.11 (adj +0.34) on $10.01, P(profit) 0.6679, adj growth 3.2 bp · B EV +0.68 (adj +0.35) on $8.20, P(profit) 0.7348, adj growth 3.4 bp · C EV +0.70 (adj +0.35) on $6.93, P(profit) 0.7802, adj growth 3.4 bp · R EV +0.08 (adj +0.05) on $1.00, P(profit) 0.7802, adj growth 2.0 bp

## TBL @ NYR  ·  10000 joint draws  ·  452 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.416 / away 0.584

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_TBL_win | p_overtime | goals | shots NYR/TBL | NYR/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.56 | 0.44 | 0.00 | 5.98 | 25.8/26.4 | 23.2/22.0 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.107 | 0.46 | 0.54 | 0.00 | 5.97 | 20.4/31.5 | 27.4/17.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.52 | 0.48 | 0.49 | 5.9 | 25.9/26.4 | 23.1/22.6 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.45 | 0.55 | 0.45 | 5.84 | 20.6/31.3 | 28.0/17.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.53 | 0.47 | 0.00 | 9.25 | 27.4/27.8 | 21.7/21.1 | even strength |
| TBL shot control · low event (<=4) · tight (1-goal/OT) | 0.060 | 0.50 | 0.50 | 0.46 | 2.71 | 19.2/30.2 | 28.9/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| John Carlson: 1+ assists NO | 55 | 0.709 | 0.603 | +0.142 | +0.035 | $4.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| New York R wins by over 1.5 goals YES | 21 | 0.291 | 0.248 | +0.069 | +0.026 | $1.02 | FUNDED_RESEARCH | $1 | NYR:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 76 | 0.838 | 0.796 | +0.065 | +0.024 | $4.21 | FUNDED_RESEARCH | $2 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Gabe Perreault: 1+ assists YES | 21 | 0.313 | 0.243 | +0.092 | +0.021 | $1.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_MIXED | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: higher confidence-adjusted growth (11.08 vs 8.74 bp); wins across more scripts (relative breadth 0.987 vs 0.53); relationships: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLSPREAD-26OCT13TBNYR-TB3|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: TBL offense succeeds (4+ goals)
- **New York R wins by over 1.5 goals YES** — thesis: NYR wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT13TBNYR-TB3|no; why: Broad expression KXNHLSPREAD-26OCT13TBNYR-NYR2|yes selected over player prop KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes because adjusted EV differs by only 0.0 pts while thesis capture is 0.63 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLSPREAD-26OCT13TBNYR-TB3|no: REINFORCING (phi 0.282); KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes: REINFORCING (phi 0.165); failure: TBL wins (incl. OT/SO)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes has the higher standalone adjusted growth (8.74 vs 6.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.282); they share one thesis budget; relationships: KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: REINFORCING (phi 0.282); KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.134); failure: TBL wins by 2+
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT13TBNYR-NYR2|yes has the higher standalone adjusted growth (8.74 vs 5.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.165); they share one thesis budget; relationships: KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: REINFORCING (phi 0.165); KXNHLSPREAD-26OCT13TBNYR-TB3|no: MOSTLY_INDEPENDENT (phi 0.134); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.4414): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:WINS_BY_2PLUS (p 0.291): highest fidelity KXNHLSPREAD-26OCT13TBNYR-NYR2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT13TBNYR-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.3611): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [DIRECT], best adjusted EV KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes — Broad expression KXNHLSPREAD-26OCT13TBNYR-NYR2|yes selected over player prop KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes because adjusted EV differs by only 0.0 pts while thesis capture is 0.63 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.4 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3487, phi -0.231)
- KXNHLSPREAD-26OCT13TBNYR-NYR2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS (p 0.4848, phi -0.621)
- KXNHLSPREAD-26OCT13TBNYR-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2649, phi -0.734)
- KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 54% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.8 pts; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4178, phi -0.26)
- override: Broad expression KXNHLSPREAD-26OCT13TBNYR-NYR2|yes selected over player prop KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes because adjusted EV differs by only 0.0 pts while thesis capture is 0.63 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT13TBNYR-TB2|no less than the minimum stake; KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes kept

portfolios: A EV +2.52 (adj +0.36) on $10.01, P(profit) 0.6592, adj growth 3.4 bp · B EV +2.28 (adj +0.64) on $10.94, P(profit) 0.6609, adj growth 6.2 bp · C EV +2.31 (adj +0.66) on $12.07, P(profit) 0.6577, adj growth 6.4 bp · R EV +0.48 (adj +0.18) on $3.00, P(profit) 0.291, adj growth 6.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT13TBNYR-TB|no == KXNHLGAME-26OCT13TBNYR-NYR|yes

## STL @ OTT  ·  10000 joint draws  ·  452 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.511 / away 0.489

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
| Andre Burakovsky: 1+ assists NO | 71 | 0.842 | 0.753 | +0.117 | +0.028 | $4.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Michael Amadio: 1+ goals YES | 14 | 0.176 | 0.165 | +0.028 | +0.016 | $1.12 | FUNDED_RESEARCH | $1 | OTT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Adam Jiricek: 1+ assists NO | 67 | 0.780 | 0.702 | +0.095 | +0.017 | $4.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Robert Thomas: 1+ goals YES | 24 | 0.279 | 0.267 | +0.026 | +0.014 | $1.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13STLOTT-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (8.93 vs 0.75 bp); alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT13STLOTT-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: OTT offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13STLOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (4.59 vs 1.42 bp); despite a smaller raw edge (+0.028 vs +0.083/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT13STLOTT-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: OTT offense suppressed (<= 2 goals)
- **Adam Jiricek: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13STLOTT-STLAJIRICEK36-1|no; why: higher confidence-adjusted growth (2.83 vs 0.18 bp); despite a smaller raw edge (+0.095 vs +0.097/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0044 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT13STLOTT-STLRTHOMAS18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.106); failure: STL offense succeeds (4+ goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13STLOTT-STLPBROBERG6-1|yes; why: higher confidence-adjusted growth (2.25 vs 0.25 bp); despite a smaller raw edge (+0.026 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.106); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.3804): highest fidelity KXNHLPTS-26OCT13STLOTT-OTTJSPENCE10-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:SUPPRESSED (p 0.4246): highest fidelity KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3574): highest fidelity KXNHLGOAL-26OCT13STLOTT-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13STLOTT-STLRTHOMAS18-1|yes (same contract)
- KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3804, phi -0.19)
- KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3905, phi -0.204)
- KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.3574, phi -0.214)
- KXNHLGOAL-26OCT13STLOTT-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4246, phi -0.247)

portfolios: A EV +2.44 (adj +0.36) on $10.01, P(profit) 0.3942, adj growth 3.3 bp · B EV +1.69 (adj +0.48) on $11.28, P(profit) 0.773, adj growth 4.7 bp · C EV +1.07 (adj +0.34) on $7.63, P(profit) 0.3407, adj growth 3.3 bp · R EV +0.19 (adj +0.11) on $1.00, P(profit) 0.1764, adj growth 3.9 bp

## VAN @ NYI  ·  10000 joint draws  ·  412 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.658 / away 0.342

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
| Drew O'Connor: 1+ goals YES | 14 | 0.185 | 0.171 | +0.036 | +0.023 | $1.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Calum Ritchie: 1+ goals NO | 75 | 0.799 | 0.786 | +0.036 | +0.023 | $4.19 | FUNDED_RESEARCH | $2 | NYI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Matias Maccelli: 1+ assists NO | 65 | 0.733 | 0.687 | +0.067 | +0.021 | $2.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
| New York I wins by over 2.5 goals NO | 69 | 0.759 | 0.722 | +0.054 | +0.017 | $2.16 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT13VANNYI-NYI3|no; why: higher confidence-adjusted growth (8.77 vs 3.15 bp); despite a smaller raw edge (+0.036 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13VANNYI-NYICRITCHIE64-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT13VANNYI-NYIMMACCELLI63-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT13VANNYI-NYI3|no: MOSTLY_INDEPENDENT (phi 0.1); failure: VAN offense suppressed (<= 2 goals)
- **Calum Ritchie: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13VANNYI-NYIMMACCELLI63-1|no; why: higher confidence-adjusted growth (6.31 vs 4.24 bp); despite a smaller raw edge (+0.036 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT13VANNYI-NYIMMACCELLI63-1|no: MOSTLY_INDEPENDENT (phi 0.037); KXNHLSPREAD-26OCT13VANNYI-NYI3|no: MOSTLY_INDEPENDENT (phi 0.147); failure: NYI offense succeeds (4+ goals)
- **Matias Maccelli: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13VANNYI-NYIBHORVAT14-1|no; why: higher confidence-adjusted growth (4.24 vs 3.39 bp); relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT13VANNYI-NYICRITCHIE64-1|no: MOSTLY_INDEPENDENT (phi 0.037); KXNHLSPREAD-26OCT13VANNYI-NYI3|no: REINFORCING (phi 0.159); failure: NYI offense succeeds (4+ goals)
- **New York I wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT13VANNYI-NYI2|no; why: higher confidence-adjusted growth (3.15 vs 1.18 bp); wins across more scripts (relative breadth 1.014 vs 0.881); relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.1); KXNHLGOAL-26OCT13VANNYI-NYICRITCHIE64-1|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLAST-26OCT13VANNYI-NYIMMACCELLI63-1|no: REINFORCING (phi 0.159); failure: NYI wins by 2+

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:SUPPRESSED (p 0.3313): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13VANNYI-NYIMMACCELLI63-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.3174): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT13VANNYI-NYI3|no (same contract)
- thesis GAME:TIGHT (p 0.4291): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13VANNYI-NYI3|no (same contract)
- KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.465, phi -0.202)
- KXNHLGOAL-26OCT13VANNYI-NYICRITCHIE64-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.4506, phi -0.202)
- KXNHLAST-26OCT13VANNYI-NYIMMACCELLI63-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.4506, phi -0.232)
- KXNHLSPREAD-26OCT13VANNYI-NYI3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:WINS_BY_2PLUS (p 0.3678, phi -0.738)

portfolios: A EV +1.20 (adj +0.27) on $10.01, P(profit) 0.6974, adj growth 2.7 bp · B EV +1.02 (adj +0.49) on $10.77, P(profit) 0.573, adj growth 4.8 bp · C EV +1.11 (adj +0.34) on $14.09, P(profit) 0.697, adj growth 3.3 bp · R EV +0.17 (adj +0.08) on $3.00, P(profit) 0.6324, adj growth 3.2 bp

## PIT @ CHI  ·  10000 joint draws  ·  412 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.411 / away 0.589

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_PIT_win | p_overtime | goals | shots CHI/PIT | CHI/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.44 | 0.56 | 0.00 | 5.99 | 26.6/27.2 | 23.4/23.4 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.111 | 0.38 | 0.62 | 0.00 | 5.99 | 21.4/32.8 | 28.5/18.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.48 | 0.52 | 0.49 | 5.97 | 27.0/27.5 | 24.2/23.7 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.47 | 0.53 | 0.45 | 5.94 | 21.2/32.5 | 29.1/18.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.44 | 0.56 | 0.00 | 9.24 | 28.4/28.9 | 22.5/22.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.081 | 0.34 | 0.66 | 0.00 | 9.27 | 22.9/34.4 | 26.3/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 13 | 0.219 | 0.195 | +0.081 | +0.057 | $3.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 53 | 0.707 | 0.582 | +0.160 | +0.035 | $4.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 29 | 0.348 | 0.333 | +0.044 | +0.028 | $2.51 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
| Ryan Donato: 1+ goals YES | 17 | 0.214 | 0.201 | +0.034 | +0.021 | $1.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13PITCHI-CHIAFRONDELL16-1|yes; why: higher confidence-adjusted growth (56.59 vs 10.49 bp); relationships: KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.07); KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT13PITCHI-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13PITCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (10.67 vs 0.45 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.07); KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.159); KXNHLGOAL-26OCT13PITCHI-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi -0.047); failure: CHI offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes; why: Player prop expression KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes selected over player prop KXNHLGOAL-26OCT13PITCHI-CHIAFRONDELL16-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.51 vs 0.44 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.159); KXNHLGOAL-26OCT13PITCHI-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI offense suppressed (<= 2 goals)
- **Ryan Donato: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes has the higher standalone adjusted growth (56.59 vs 6.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3659): highest fidelity KXNHLAST-26OCT13PITCHI-CHITBERTUZZI59-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes — Player prop expression KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes selected over player prop KXNHLGOAL-26OCT13PITCHI-CHIAFRONDELL16-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.51 vs 0.44 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis CHI:SUPPRESSED (p 0.4142): highest fidelity KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4375): highest fidelity KXNHLAST-26OCT13PITCHI-PITECHINAKHOV59-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13PITCHI-PITECHINAKHOV59-1|yes (same contract)
- KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4142, phi -0.246)
- KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.2 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3659, phi -0.251)
- KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4142, phi -0.27)
- KXNHLGOAL-26OCT13PITCHI-CHIRDONATO8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4142, phi -0.219)
- override: Player prop expression KXNHLGOAL-26OCT13PITCHI-CHITBERTUZZI59-1|yes selected over player prop KXNHLGOAL-26OCT13PITCHI-CHIAFRONDELL16-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.51 vs 0.44 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +3.39 (adj +1.43) on $10.01, P(profit) 0.4689, adj growth 13.9 bp · B EV +3.92 (adj +2.03) on $11.84, P(profit) 0.4924, adj growth 19.7 bp · C EV +4.77 (adj +2.20) on $13.89, P(profit) 0.6683, adj growth 21.1 bp · R EV +0.14 (adj +0.09) on $1.00, P(profit) 0.3483, adj growth 3.5 bp

## MIN @ WPG  ·  10000 joint draws  ·  404 bet sides mapped, 8 +EV candidates, 3 on card

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
| Neal Pionk: 1+ goals NO | 86 | 0.932 | 0.912 | +0.064 | +0.043 | $4.79 | FUNDED_RESEARCH | $2 | WPG:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 59 | 0.646 | 0.630 | +0.040 | +0.023 | $4.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 23 | 0.305 | 0.260 | +0.063 | +0.018 | $1.59 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13MINWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (37.02 vs 1.59 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no; why: higher confidence-adjusted growth (4.81 vs 2.78 bp); relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.19); failure: MIN offense succeeds (4+ goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13MINWPG-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (3.71 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.19); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.4173): highest fidelity KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.3661): highest fidelity KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes (same contract)
- thesis WPG:SUPPRESSED (p 0.3874): highest fidelity KXNHLAST-26OCT13MINWPG-WPGNPIONK4-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13MINWPG-WPGNPIONK4-1|no (same contract)
- KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3878, phi -0.116)
- KXNHLGOAL-26OCT13MINWPG-MINKKAPRIZOV97-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3661, phi -0.304)
- KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4173, phi -0.274)

portfolios: A EV +1.29 (adj +0.41) on $10.01, P(profit) 0.5767, adj growth 4.0 bp · B EV +1.04 (adj +0.51) on $10.60, P(profit) 0.7513, adj growth 5.0 bp · C EV +1.08 (adj +0.42) on $14.09, P(profit) 0.5629, adj growth 4.0 bp · R EV +0.15 (adj +0.10) on $2.00, P(profit) 0.9322, adj growth 4.0 bp

## COL @ DAL  ·  10000 joint draws  ·  414 bet sides mapped, 2 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.488 / away 0.512

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
| Nathan MacKinnon: 1+ goals NO | 60 | 0.644 | 0.630 | +0.028 | +0.013 | $2.04 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13COLDAL-COLNMACKINNON29-3|no; why: higher confidence-adjusted growth (1.52 vs 0.14 bp); despite a smaller raw edge (+0.028 vs +0.053/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0028 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: COL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4057): highest fidelity KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.3802): highest fidelity KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no (same contract)
- KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4057, phi -0.284)

portfolios: A EV +0.37 (adj +0.18) on $5.33, P(profit) 0.7334, adj growth 1.7 bp · B EV +0.09 (adj +0.04) on $2.04, P(profit) 0.6445, adj growth 0.4 bp · C EV +0.25 (adj +0.12) on $3.57, P(profit) 0.7334, adj growth 1.2 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6445, adj growth 0.8 bp

## VGK @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 5 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.468 / away 0.532

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
| Mitch Marner: 1+ goals NO | 71 | 0.762 | 0.745 | +0.037 | +0.021 | $3.04 | FUNDED_RESEARCH | $1 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ goals NO | 68 | 0.726 | 0.712 | +0.030 | +0.017 | $2.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ assists NO | 53 | 0.600 | 0.563 | +0.053 | +0.015 | $1.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13VGKNSH-VGKTCONNELLY24-1|no; why: higher confidence-adjusted growth (4.65 vs 3.91 bp); despite a smaller raw edge (+0.037 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: VGK offense succeeds (4+ goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no; why: Player prop expression KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT13VGKNSH-VGKTCONNELLY24-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.86 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.108); failure: VGK offense succeeds (4+ goals)
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no has the higher standalone adjusted growth (4.65 vs 2.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.108); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.4121): highest fidelity KXNHLAST-26OCT13VGKNSH-VGKTCONNELLY24-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no — Player prop expression KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT13VGKNSH-VGKTCONNELLY24-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.86 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3696, phi -0.231)
- KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3696, phi -0.24)
- KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3696, phi -0.279)
- override: Player prop expression KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT13VGKNSH-VGKTCONNELLY24-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.86 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.22 (adj +0.27) on $10.01, P(profit) 0.6331, adj growth 2.6 bp · B EV +0.37 (adj +0.17) on $6.41, P(profit) 0.5531, adj growth 1.7 bp · C EV +0.28 (adj +0.15) on $5.46, P(profit) 0.7616, adj growth 1.5 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.7616, adj growth 1.1 bp

## TOR @ UTA  ·  10000 joint draws  ·  428 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.593 / away 0.407

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
| Vincent Trocheck: 1+ assists NO | 69 | 0.782 | 0.733 | +0.077 | +0.028 | $3.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Dylan Guenther: 1+ goals NO | 61 | 0.669 | 0.653 | +0.042 | +0.026 | $3.02 | FUNDED_RESEARCH | $1 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Kirill Marchenko: 1+ assists NO | 63 | 0.717 | 0.671 | +0.071 | +0.025 | $3.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Auston Matthews: 1+ assists NO | 57 | 0.648 | 0.607 | +0.061 | +0.020 | $1.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (8.56 vs 6.40 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.048); KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT13TORUTA-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: UTA offense succeeds (4+ goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TORUTA-UTALCOOLEY92-1|no; why: higher confidence-adjusted growth (6.40 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0002 below the 0.010/contract floor; relationships: KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.048); KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT13TORUTA-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: UTA offense succeeds (4+ goals)
- **Kirill Marchenko: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TORUTA-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (5.90 vs 3.47 bp); relationships: KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT13TORUTA-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.109); failure: TOR offense succeeds (4+ goals)
- **Auston Matthews: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no; why: second expression of the same thesis: KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no has the higher standalone adjusted growth (5.90 vs 3.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.109); they share one thesis budget; relationships: KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi 0.109); failure: TOR offense succeeds (4+ goals)

**Review**: scripts UTA shot control · normal event (5-7) · decided (2+) 0.15, UTA shot control · normal event (5-7) · tight (1-goal/OT) 0.12, UTA shot control · high event (8+) · decided (2+) 0.11.
- thesis UTA:SUPPRESSED (p 0.294): highest fidelity KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no (same contract)
- thesis TOR:SUPPRESSED (p 0.4585): highest fidelity KXNHLAST-26OCT13TORUTA-TORJTAVARES91-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.5024, phi -0.181)
- KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.5024, phi -0.222)
- KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3291, phi -0.246)
- KXNHLAST-26OCT13TORUTA-TORAMATTHEWS34-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3291, phi -0.28)

portfolios: A EV +1.18 (adj +0.35) on $10.01, P(profit) 0.6546, adj growth 3.4 bp · B EV +1.17 (adj +0.47) on $11.97, P(profit) 0.6556, adj growth 4.6 bp · C EV +0.92 (adj +0.41) on $10.30, P(profit) 0.4794, adj growth 4.0 bp · R EV +0.07 (adj +0.04) on $1.00, P(profit) 0.6687, adj growth 1.6 bp

## CGY @ ANA  ·  10000 joint draws  ·  408 bet sides mapped, 2 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.609 / away 0.391

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
| Alex Killorn: 1+ assists YES | 30 | 0.366 | 0.331 | +0.052 | +0.016 | $1.13 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
- **Alex Killorn: 1+ assists YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13CGYANA-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (2.57 vs 0.13 bp); alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4821): highest fidelity KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes (same contract)
- KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3045, phi -0.252)

portfolios: A EV +0.62 (adj +0.19) on $3.77, P(profit) 0.3663, adj growth 1.7 bp · B EV +0.18 (adj +0.06) on $1.13, P(profit) 0.3663, adj growth 0.6 bp · C EV +0.25 (adj +0.08) on $1.55, P(profit) 0.3663, adj growth 0.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ LAK  ·  10000 joint draws  ·  420 bet sides mapped, 7 +EV candidates, 4 on card

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
| Artemi Panarin: 1+ assists NO | 48 | 0.614 | 0.523 | +0.116 | +0.026 | $3.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ assists YES | 28 | 0.351 | 0.313 | +0.057 | +0.019 | $1.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
| Kasperi Kapanen: 1+ assists YES | 26 | 0.336 | 0.290 | +0.062 | +0.017 | $1.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
| Leon Draisaitl: 1+ assists NO | 41 | 0.568 | 0.446 | +0.141 | +0.019 | $2.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.77) | CALIBRATION_WARNING | D |
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13EDMLA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (5.92 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: LAK offense succeeds (4+ goals)
- **Mattias Ekholm: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (3.72 vs 3.12 bp); despite a smaller raw edge (+0.057 vs +0.062/contract); relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.074); failure: EDM offense suppressed (<= 2 goals)
- **Kasperi Kapanen: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes has the higher standalone adjusted growth (3.72 vs 3.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.045); they share one thesis budget; relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.089); failure: EDM offense suppressed (<= 2 goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (3.12 vs 1.96 bp); relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.074); KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.089); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4172): highest fidelity KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.3973): highest fidelity KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.3821): highest fidelity KXNHLPTS-26OCT13EDMLA-EDMLDRAISAITL29-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.9 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3619, phi -0.277)
- KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3821, phi -0.256)
- KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3821, phi -0.271)
- KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.2 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.3973, phi -0.309)

portfolios: A EV +2.73 (adj +0.38) on $10.01, P(profit) 0.7103, adj growth 3.6 bp · B EV +2.08 (adj +0.45) on $8.30, P(profit) 0.65, adj growth 4.3 bp · C EV +2.05 (adj +0.43) on $8.13, P(profit) 0.522, adj growth 4.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Marat Khusnutdinov: 1+ goals YES | 11 | 0.146 | 0.136 | +0.029 | +0.019 | $1.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Luca Cagnoni: 1+ assists NO | 65 | 0.739 | 0.692 | +0.073 | +0.026 | $4.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| David Pastrnak: 1+ goals NO | 62 | 0.678 | 0.661 | +0.042 | +0.025 | $4.10 | FUNDED_RESEARCH | $2 | BOS:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Collin Graf: 1+ goals YES | 14 | 0.177 | 0.165 | +0.029 | +0.017 | $1.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13BOSSJ-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (7.56 vs 2.07 bp); relationships: KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13BOSSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: BOS offense suppressed (<= 2 goals)
- **Luca Cagnoni: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13BOSSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (6.61 vs 5.67 bp); despite a smaller raw edge (+0.073 vs +0.103/contract); relationships: KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13BOSSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.03); failure: SJS offense succeeds (4+ goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no; why: Player prop expression KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.84 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13BOSSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: BOS offense succeeds (4+ goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13BOSSJ-SJICHERNYSHOV92-1|yes; why: higher confidence-adjusted growth (4.93 vs 1.92 bp); despite a smaller raw edge (+0.029 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:SUPPRESSED (p 0.3884): highest fidelity KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no — Player prop expression KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.84 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis SJS:SUPPRESSED (p 0.3723): highest fidelity KXNHLAST-26OCT13BOSSJ-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:OFFENSE_4PLUS (p 0.414): highest fidelity KXNHLAST-26OCT13BOSSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BOSSJ-SJCGRAF51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3884, phi -0.172)
- KXNHLAST-26OCT13BOSSJ-SJLCAGNONI42-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.414, phi -0.215)
- KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3995, phi -0.269)
- KXNHLGOAL-26OCT13BOSSJ-SJCGRAF51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3723, phi -0.201)
- override: Player prop expression KXNHLGOAL-26OCT13BOSSJ-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.84 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.60 (adj +0.45) on $10.01, P(profit) 0.6502, adj growth 4.3 bp · B EV +1.33 (adj +0.68) on $11.28, P(profit) 0.6271, adj growth 6.6 bp · C EV +2.41 (adj +0.80) on $14.00, P(profit) 0.6847, adj growth 7.7 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.6783, adj growth 2.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
