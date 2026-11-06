# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-06T23:58:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.61 | +6.97 | +23.56 | 0.628 | -60.64 | -82.97 | 45.73 |
| B thesis-diversified (joint) ← optimiser card | 103.70 | +18.68 | +12.13 | +12.06 | 0.591 | -53.27 | -57.17 | 104.55 |
| C best expression per thesis | 106.01 | +11.30 | +5.14 | +12.41 | 0.589 | -33.06 | -51.07 | 44.89 |
| R FUNDED research stakes | 12.00 | +1.73 | +1.15 | +1.72 | 0.581 | -6.48 | -6.48 | 0.00 |

## CBJ @ BUF  ·  10000 joint draws  ·  468 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.609 / away 0.392

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_CBJ_win | p_overtime | goals | shots BUF/CBJ | BUF/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.59 | 0.41 | 0.00 | 6.0 | 27.4/27.3 | 24.3/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.52 | 0.48 | 0.45 | 5.96 | 27.7/27.4 | 24.2/24.2 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.083 | 0.64 | 0.36 | 0.00 | 6.01 | 32.5/21.9 | 19.2/28.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.56 | 0.44 | 0.00 | 9.29 | 29.3/29.1 | 23.3/22.8 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.58 | 0.42 | 0.45 | 5.87 | 32.7/22.2 | 19.0/29.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.59 | 0.41 | 0.00 | 3.47 | 26.5/26.4 | 24.8/24.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 15 | 0.194 | 0.180 | +0.035 | +0.021 | $5.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Tage Thompson: 2+ goals NO | 90 | 0.932 | 0.922 | +0.025 | +0.016 | $20.00 | FUNDED_RESEARCH | $5 | BUF:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Kent Johnson: 1+ goals NO | 75 | 0.792 | 0.780 | +0.029 | +0.017 | $18.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 22 | 0.256 | 0.245 | +0.024 | +0.013 | $3.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no; why: higher confidence-adjusted growth (7.47 vs 1.71 bp); despite a smaller raw edge (+0.035 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV06CBJBUF-BUFTTHOMPSON72-2|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV06CBJBUF-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: CBJ offense suppressed (<= 2 goals)
- **Tage Thompson: 2+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV06CBJBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (6.91 vs 3.14 bp); despite a smaller raw edge (+0.025 vs +0.032/contract); relationships: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV06CBJBUF-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: BUF offense succeeds (4+ goals)
- **Kent Johnson: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV06CBJBUF-CBJAFANTILLI19-1|no; why: higher confidence-adjusted growth (3.63 vs 0.36 bp); alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV06CBJBUF-BUFTTHOMPSON72-2|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: CBJ offense succeeds (4+ goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (7.47 vs 1.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV06CBJBUF-BUFTTHOMPSON72-2|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV06CBJBUF-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CBJ:WINS_BY_2PLUS (p 0.2384): highest fidelity KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF5|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:OFFENSE_4PLUS (p 0.3404): highest fidelity KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:SUPPRESSED (p 0.4514): highest fidelity KXNHLGOAL-26NOV06CBJBUF-CBJKJOHNSON91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV06CBJBUF-CBJKJOHNSON91-1|no (same contract)
- KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4514, phi -0.248)
- KXNHLGOAL-26NOV06CBJBUF-BUFTTHOMPSON72-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4029, phi -0.204)
- KXNHLGOAL-26NOV06CBJBUF-CBJKJOHNSON91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3404, phi -0.206)
- KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4514, phi -0.24)

portfolios: A EV +4.48 (adj +2.00) on $50.00, P(profit) 0.5142, adj growth 15.1 bp · B EV +2.98 (adj +1.79) on $48.40, P(profit) 0.3453, adj growth 15.9 bp · C EV +2.61 (adj +1.57) on $36.54, P(profit) 0.6018, adj growth 13.7 bp · R EV +0.14 (adj +0.09) on $5.00, P(profit) 0.9317, adj growth 3.4 bp

## SJS @ MIN  ·  10000 joint draws  ·  420 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.705 / away 0.295

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_SJS_win | p_overtime | goals | shots MIN/SJS | MIN/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.68 | 0.32 | 0.00 | 6.03 | 28.5/27.9 | 25.1/24.2 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.115 | 0.69 | 0.31 | 0.00 | 6.01 | 33.9/22.1 | 19.5/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.54 | 0.46 | 0.47 | 5.96 | 28.8/28.4 | 25.0/25.4 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.57 | 0.43 | 0.46 | 5.87 | 34.1/22.7 | 19.6/30.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.69 | 0.31 | 0.00 | 9.27 | 29.9/29.3 | 24.5/22.5 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.079 | 0.72 | 0.28 | 0.00 | 9.32 | 35.4/23.4 | 18.9/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 11 | 0.163 | 0.148 | +0.046 | +0.031 | $7.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 47 | 0.536 | 0.517 | +0.049 | +0.030 | $13.82 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.75) | EVIDENCE_STRONGER | D |
| Olli Maatta: 1+ goals YES | 5 | 0.077 | 0.067 | +0.024 | +0.013 | $2.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Blake Coleman: 1+ goals YES | 23 | 0.278 | 0.264 | +0.035 | +0.022 | $7.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (20.28 vs 5.71 bp); relationships: KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV06SJMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV06SJMIN-MIN3|no; why: higher confidence-adjusted growth (7.84 vs 4.34 bp); despite a smaller raw edge (+0.049 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.03 vs 0.793); relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV06SJMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: MIN offense succeeds (4+ goals)
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (7.65 vs 5.71 bp); despite a smaller raw edge (+0.024 vs +0.035/contract); relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: MIN offense suppressed (<= 2 goals)
- **Blake Coleman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26NOV06SJMIN-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (5.71 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV06SJMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis MIN:SUPPRESSED (p 0.3095): highest fidelity KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS (p 0.381): highest fidelity KXNHLSPREAD-26NOV06SJMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.4816): highest fidelity KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes (same contract)
- KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.157)
- KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 25% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4816, phi -0.286)
- KXNHLGOAL-26NOV06SJMIN-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.114)
- KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.232)

portfolios: A EV +14.61 (adj +2.32) on $50.00, P(profit) 0.5733, adj growth 11.8 bp · B EV +6.83 (adj +4.35) on $31.71, P(profit) 0.3428, adj growth 37.5 bp · C EV +5.67 (adj +2.59) on $39.68, P(profit) 0.5508, adj growth 22.6 bp · R EV +0.40 (adj +0.25) on $4.00, P(profit) 0.5365, adj growth 8.5 bp

## ANA @ CGY  ·  10000 joint draws  ·  468 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.569 / away 0.431

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_ANA_win | p_overtime | goals | shots CGY/ANA | CGY/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.47 | 0.53 | 0.00 | 6.04 | 28.3/28.7 | 25.0/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.112 | 0.44 | 0.56 | 0.00 | 9.47 | 30.2/30.5 | 24.0/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.50 | 0.50 | 0.47 | 5.98 | 28.4/28.7 | 25.5/25.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.090 | 0.41 | 0.59 | 0.00 | 6.07 | 22.7/33.9 | 29.6/19.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.078 | 0.39 | 0.61 | 0.00 | 9.36 | 24.2/35.9 | 28.6/19.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.45 | 0.55 | 0.47 | 5.98 | 22.8/34.1 | 30.7/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Colangelo: 1+ goals YES | 11 | 0.163 | 0.148 | +0.046 | +0.032 | $8.09 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Pavel Mintyukov: 1+ goals YES | 6 | 0.099 | 0.088 | +0.035 | +0.024 | $5.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 11 | 0.149 | 0.138 | +0.032 | +0.021 | $5.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Nico Myatovic: 1+ goals YES | 10 | 0.134 | 0.124 | +0.028 | +0.018 | $4.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV06ANACGY-CGY2|no; why: higher confidence-adjusted growth (20.66 vs 4.90 bp); despite a smaller raw edge (+0.046 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV06ANACGY-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV06ANACGY-ANANMYATOVIC48-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: ANA offense suppressed (<= 2 goals)
- **Pavel Mintyukov: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV06ANACGY-CGY2|no; why: higher confidence-adjusted growth (20.06 vs 4.90 bp); despite a smaller raw edge (+0.035 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV06ANACGY-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV06ANACGY-ANANMYATOVIC48-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: ANA offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV06ANACGY-CGY2|no; why: higher confidence-adjusted growth (9.18 vs 4.90 bp); despite a smaller raw edge (+0.032 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV06ANACGY-ANANMYATOVIC48-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)
- **Nico Myatovic: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV06ANACGY-CGY2|no; why: higher confidence-adjusted growth (7.17 vs 4.90 bp); despite a smaller raw edge (+0.027 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV06ANACGY-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4621): highest fidelity KXNHLTEAMTOTAL-26NOV06ANACGY-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06ANACGY-CGY2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5319): highest fidelity KXNHLSPREAD-26NOV06ANACGY-CGY2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06ANACGY-CGY2|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3229): highest fidelity KXNHLSPREAD-26NOV06ANACGY-CGY2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06ANACGY-CGY2|no (same contract)
- KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.159)
- KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.124)
- KXNHLGOAL-26NOV06ANACGY-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.168)
- KXNHLGOAL-26NOV06ANACGY-ANANMYATOVIC48-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.153)

portfolios: A EV +8.53 (adj +2.65) on $50.00, P(profit) 0.4896, adj growth 18.9 bp · B EV +8.86 (adj +5.99) on $23.59, P(profit) 0.4454, adj growth 51.2 bp · C EV +3.02 (adj +0.98) on $29.79, P(profit) 0.3835, adj growth 8.6 bp · R EV +1.18 (adj +0.81) on $3.00, P(profit) 0.163, adj growth 25.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
