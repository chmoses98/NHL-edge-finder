# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-07T00:48:31Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +17.12 | +3.58 | +22.73 | 0.680 | -45.89 | -54.72 | 26.24 |
| B thesis-diversified (joint) ← optimiser card | 69.15 | +18.99 | +11.21 | +4.64 | 0.555 | -40.14 | -69.15 | 96.62 |
| C best expression per thesis | 86.23 | +14.10 | +6.63 | +12.42 | 0.612 | -37.40 | -56.59 | 57.73 |
| R FUNDED research stakes | 9.00 | +1.98 | +1.08 | +1.70 | 0.618 | -9.00 | -9.00 | 0.00 |

## SJS @ MIN  ·  10000 joint draws  ·  420 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.710 / away 0.290

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
| Yakov Trenin: 1+ goals YES | 11 | 0.163 | 0.148 | +0.046 | +0.031 | $8.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 45 | 0.536 | 0.514 | +0.069 | +0.046 | $16.92 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.75) | EVIDENCE_STRONGER | D |
| Minnesota over 3.5 goals scored NO | 38 | 0.509 | 0.422 | +0.112 | +0.025 | $11.50 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Blake Coleman: 1+ goals YES | 23 | 0.278 | 0.264 | +0.035 | +0.022 | $8.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (20.28 vs 5.71 bp); relationships: KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no: INTENTIONAL_DIVERSIFIER (phi -0.161); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no; why: higher confidence-adjusted growth (18.81 vs 5.85 bp); despite a smaller raw edge (+0.069 vs +0.112/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.03 vs 0.867); relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no: REINFORCING (phi 0.285); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: MIN offense succeeds (4+ goals)
- **Minnesota over 3.5 goals scored NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no has the higher standalone adjusted growth (18.81 vs 5.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.285); they share one thesis budget; relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.161); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: REINFORCING (phi 0.285); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.237); failure: MIN offense succeeds (4+ goals)
- **Blake Coleman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26NOV06SJMIN-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (5.71 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no: INTENTIONAL_DIVERSIFIER (phi -0.237); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis MIN:SUPPRESSED (p 0.3095): highest fidelity KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS (p 0.381): highest fidelity KXNHLSPREAD-26NOV06SJMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS_BY_2PLUS (p 0.1921): highest fidelity KXNHLSPREAD-26NOV06SJMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.157)
- KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 25% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4816, phi -0.286)
- KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.4 pts; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4816, phi -0.981)
- KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.232)

portfolios: A EV +12.19 (adj +1.94) on $50.00, P(profit) 0.5753, adj growth 12.3 bp · B EV +10.41 (adj +5.52) on $45.84, P(profit) 0.5494, adj growth 47.9 bp · C EV +7.92 (adj +3.68) on $47.90, P(profit) 0.581, adj growth 32.2 bp · R EV +1.31 (adj +0.62) on $7.00, P(profit) 0.5365, adj growth 21.5 bp

## ANA @ CGY  ·  10000 joint draws  ·  462 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.569 / away 0.431

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_ANA_win | p_overtime | goals | shots CGY/ANA | CGY/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.44 | 0.56 | 0.00 | 6.04 | 28.3/28.7 | 24.7/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.112 | 0.46 | 0.54 | 0.00 | 9.44 | 30.1/30.4 | 24.0/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.51 | 0.49 | 0.47 | 6.01 | 28.4/28.7 | 25.3/25.0 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.096 | 0.39 | 0.61 | 0.00 | 6.01 | 22.6/33.8 | 29.6/19.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.45 | 0.55 | 0.48 | 5.98 | 23.0/34.3 | 30.7/19.8 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.071 | 0.38 | 0.62 | 0.00 | 9.43 | 24.6/36.2 | 28.3/19.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Colangelo: 1+ goals YES | 12 | 0.170 | 0.156 | +0.043 | +0.029 | $7.58 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Pavel Mintyukov: 1+ goals YES | 6 | 0.096 | 0.084 | +0.032 | +0.020 | $4.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 9 | 0.131 | 0.120 | +0.036 | +0.024 | $5.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Nico Myatovic: 1+ goals YES | 10 | 0.138 | 0.127 | +0.031 | +0.021 | $5.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV06ANACGY-CGY2|no; why: higher confidence-adjusted growth (16.19 vs 4.27 bp); despite a smaller raw edge (+0.043 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV06ANACGY-ANANMYATOVIC48-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: ANA offense suppressed (<= 2 goals)
- **Pavel Mintyukov: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes has the higher standalone adjusted growth (16.19 vs 14.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV06ANACGY-ANANMYATOVIC48-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes has the higher standalone adjusted growth (16.19 vs 14.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV06ANACGY-ANANMYATOVIC48-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)
- **Nico Myatovic: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes has the higher standalone adjusted growth (16.19 vs 9.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4641): highest fidelity KXNHLTEAMTOTAL-26NOV06ANACGY-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:NET_HIGH_VOLUME (p 0.3138): highest fidelity KXNHLSAVE-26NOV06ANACGY-CGYDWOLF32-25|yes [DIRECT], best adjusted EV KXNHLSAVE-26NOV06ANACGY-CGYDWOLF32-25|yes (same contract)
- thesis ANA:WINS (p 0.5312): highest fidelity KXNHLSPREAD-26NOV06ANACGY-CGY2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06ANACGY-CGY2|no (same contract)
- KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3198, phi -0.175)
- KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3198, phi -0.13)
- KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3198, phi -0.142)
- KXNHLGOAL-26NOV06ANACGY-ANANMYATOVIC48-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3198, phi -0.166)

portfolios: A EV +4.93 (adj +1.64) on $50.00, P(profit) 0.7105, adj growth 14.0 bp · B EV +8.58 (adj +5.69) on $23.31, P(profit) 0.4371, adj growth 48.7 bp · C EV +6.19 (adj +2.95) on $38.33, P(profit) 0.4887, adj growth 25.5 bp · R EV +0.67 (adj +0.46) on $2.00, P(profit) 0.1702, adj growth 15.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
