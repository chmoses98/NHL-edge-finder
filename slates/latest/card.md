# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-07T00:24:38Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +21.18 | +4.94 | +22.17 | 0.634 | -51.67 | -74.85 | 34.62 |
| B thesis-diversified (joint) ← optimiser card | 63.67 | +17.67 | +10.44 | +9.71 | 0.552 | -42.72 | -63.67 | 89.71 |
| C best expression per thesis | 76.89 | +9.92 | +3.71 | +8.08 | 0.713 | -23.42 | -46.86 | 32.52 |
| R FUNDED research stakes | 10.00 | +2.49 | +1.22 | -0.16 | 0.451 | -10.00 | -10.00 | 0.00 |

## SJS @ MIN  ·  10000 joint draws  ·  420 bet sides mapped, 24 +EV candidates, 4 on card

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
| Yakov Trenin: 1+ goals YES | 11 | 0.163 | 0.148 | +0.046 | +0.031 | $8.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 47 | 0.536 | 0.519 | +0.049 | +0.031 | $10.21 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.75) | EVIDENCE_STRONGER | D |
| Blake Coleman: 1+ goals YES | 23 | 0.278 | 0.264 | +0.035 | +0.022 | $8.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Minnesota over 3.5 goals scored NO | 39 | 0.509 | 0.428 | +0.102 | +0.022 | $12.21 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (20.28 vs 5.71 bp); relationships: KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no: INTENTIONAL_DIVERSIFIER (phi -0.161); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV06SJMIN-MINQHUGHES43-1|no; why: higher confidence-adjusted growth (8.51 vs 5.38 bp); despite a smaller raw edge (+0.049 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no: REINFORCING (phi 0.285); failure: MIN offense succeeds (4+ goals)
- **Blake Coleman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV06SJMIN-MINBCOLEMAN20-2|yes; why: higher confidence-adjusted growth (5.71 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; wins across more scripts (relative breadth 0.859 vs 0.703); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no: INTENTIONAL_DIVERSIFIER (phi -0.237); failure: MIN offense suppressed (<= 2 goals)
- **Minnesota over 3.5 goals scored NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no has the higher standalone adjusted growth (8.51 vs 4.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.285); they share one thesis budget; relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.161); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: REINFORCING (phi 0.285); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.237); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis MIN:SUPPRESSED (p 0.3095): highest fidelity KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS (p 0.381): highest fidelity KXNHLSPREAD-26NOV06SJMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.4816): highest fidelity KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes (same contract)
- KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.157)
- KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 25% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4816, phi -0.286)
- KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.232)
- KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.4 pts; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4816, phi -0.981)

portfolios: A EV +12.38 (adj +2.02) on $50.00, P(profit) 0.6793, adj growth 13.1 bp · B EV +8.80 (adj +4.45) on $40.08, P(profit) 0.5494, adj growth 38.5 bp · C EV +6.36 (adj +2.52) on $44.60, P(profit) 0.6241, adj growth 22.1 bp · R EV +1.31 (adj +0.41) on $7.00, P(profit) 0.5088, adj growth 12.8 bp

## ANA @ CGY  ·  10000 joint draws  ·  468 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.567 / away 0.433

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

portfolios: A EV +8.80 (adj +2.92) on $50.00, P(profit) 0.4896, adj growth 21.5 bp · B EV +8.86 (adj +5.99) on $23.59, P(profit) 0.4454, adj growth 51.2 bp · C EV +3.56 (adj +1.19) on $32.29, P(profit) 0.3835, adj growth 10.5 bp · R EV +1.18 (adj +0.81) on $3.00, P(profit) 0.163, adj growth 25.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
