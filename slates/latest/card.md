# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-06T20:33:00Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.04 | +9.85 | +21.55 | 0.603 | -69.66 | -89.79 | 70.50 |
| B thesis-diversified (joint) ← optimiser card | 82.63 | +20.18 | +12.87 | +12.56 | 0.590 | -54.72 | -67.99 | 110.53 |
| C best expression per thesis | 76.02 | +11.21 | +5.09 | +7.19 | 0.565 | -31.12 | -46.00 | 44.56 |
| R FUNDED research stakes | 11.00 | +2.55 | +1.63 | -1.25 | 0.328 | -11.00 | -11.00 | 0.00 |

## CBJ @ BUF  ·  10000 joint draws  ·  440 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.605 / away 0.395

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_CBJ_win | p_overtime | goals | shots BUF/CBJ | BUF/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 6.01 | 27.5/27.5 | 24.2/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.52 | 0.48 | 0.44 | 5.95 | 27.7/27.6 | 24.2/24.2 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.084 | 0.66 | 0.34 | 0.00 | 5.98 | 32.3/21.7 | 18.9/27.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.55 | 0.45 | 0.00 | 9.25 | 29.0/29.0 | 23.4/22.5 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.59 | 0.41 | 0.45 | 5.85 | 32.9/22.3 | 19.3/29.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.058 | 0.52 | 0.48 | 0.50 | 2.85 | 26.1/26.0 | 24.6/24.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 14 | 0.195 | 0.180 | +0.047 | +0.032 | $8.37 | FUNDED_RESEARCH | $3 | CBJ:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 21 | 0.257 | 0.243 | +0.035 | +0.021 | $6.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 26 | 0.301 | 0.289 | +0.028 | +0.015 | $6.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Buffalo over 3.5 goals scored NO | 52 | 0.588 | 0.549 | +0.050 | +0.011 | $7.87 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (17.06 vs 5.58 bp); relationships: KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no: MOSTLY_INDEPENDENT (phi 0.058); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (17.06 vs 5.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.028); they share one thesis budget; relationships: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no: MOSTLY_INDEPENDENT (phi 0.016); failure: CBJ offense suppressed (<= 2 goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26NOV06CBJBUF-BUFMSAMUELSSON23-1|yes; why: higher confidence-adjusted growth (2.52 vs 0.41 bp); despite a smaller raw edge (+0.028 vs +0.031/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no: INTENTIONAL_DIVERSIFIER (phi -0.266); failure: BUF offense suppressed (<= 2 goals)
- **Buffalo over 3.5 goals scored NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV06CBJBUF-BUF3|no; why: higher confidence-adjusted growth (1.15 vs 1.10 bp); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.058); KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.266); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3404): highest fidelity KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.4029): highest fidelity KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.3714): highest fidelity KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no (same contract)
- KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4514, phi -0.236)
- KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4514, phi -0.266)
- KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3714, phi -0.268)
- KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4029, phi -0.981)

portfolios: A EV +8.22 (adj +4.54) on $50.00, P(profit) 0.4184, adj growth 35.7 bp · B EV +5.03 (adj +2.90) on $28.93, P(profit) 0.4184, adj growth 25.1 bp · C EV +4.09 (adj +2.34) on $22.92, P(profit) 0.4413, adj growth 20.2 bp · R EV +1.13 (adj +0.68) on $5.00, P(profit) 0.1952, adj growth 22.0 bp

## SJS @ MIN  ·  10000 joint draws  ·  414 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.700 / away 0.300

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
| Yakov Trenin: 1+ goals YES | 12 | 0.163 | 0.149 | +0.035 | +0.022 | $5.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Olli Maatta: 1+ goals YES | 5 | 0.077 | 0.068 | +0.024 | +0.015 | $3.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Blake Coleman: 1+ goals YES | 23 | 0.278 | 0.264 | +0.035 | +0.022 | $7.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 48 | 0.536 | 0.520 | +0.039 | +0.022 | $10.55 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.75) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (9.41 vs 5.71 bp); relationships: KXNHLGOAL-26NOV06SJMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: MIN offense suppressed (<= 2 goals)
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (9.12 vs 5.71 bp); despite a smaller raw edge (+0.024 vs +0.035/contract); relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: MIN offense suppressed (<= 2 goals)
- **Blake Coleman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26NOV06SJMIN-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (5.71 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0009 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV06SJMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV06SJMIN-MIN3|no; why: Player prop expression KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no selected over broad KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.75 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV06SJMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4816): highest fidelity KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes (same contract)
- thesis GAME:TIGHT (p 0.4175): highest fidelity KXNHLSPREAD-26NOV06SJMIN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3095): highest fidelity KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no (same contract)
- KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.157)
- KXNHLGOAL-26NOV06SJMIN-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.114)
- KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.232)
- KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 25% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4816, phi -0.286)
- override: Player prop expression KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no selected over broad KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.75 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +9.29 (adj +2.09) on $50.00, P(profit) 0.5833, adj growth 14.7 bp · B EV +4.92 (adj +3.02) on $26.63, P(profit) 0.4439, adj growth 26.0 bp · C EV +5.13 (adj +2.04) on $42.49, P(profit) 0.5669, adj growth 18.1 bp · R EV +0.24 (adj +0.14) on $3.00, P(profit) 0.5365, adj growth 4.7 bp

## ANA @ CGY  ·  10000 joint draws  ·  460 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.572 / away 0.428

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
| Sam Colangelo: 1+ goals YES | 11 | 0.163 | 0.148 | +0.046 | +0.032 | $8.05 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Pavel Mintyukov: 1+ goals YES | 6 | 0.099 | 0.088 | +0.035 | +0.024 | $5.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 9 | 0.130 | 0.119 | +0.035 | +0.023 | $5.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 16 | 0.213 | 0.198 | +0.043 | +0.029 | $7.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4|yes; why: higher confidence-adjusted growth (20.66 vs 6.43 bp); despite a smaller raw edge (+0.046 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.874 vs 0.729); relationships: KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV06ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: ANA offense suppressed (<= 2 goals)
- **Pavel Mintyukov: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4|yes; why: higher confidence-adjusted growth (20.06 vs 6.43 bp); despite a smaller raw edge (+0.035 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.848 vs 0.729); relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV06ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4|yes; why: higher confidence-adjusted growth (13.31 vs 6.43 bp); despite a smaller raw edge (+0.035 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV06ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: ANA offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4|yes; why: higher confidence-adjusted growth (12.75 vs 6.43 bp); despite a smaller raw edge (+0.043 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.862 vs 0.729); relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4621): highest fidelity KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4|yes (same contract)
- thesis ANA:WINS (p 0.5319): highest fidelity KXNHLSPREAD-26NOV06ANACGY-CGY2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3229): highest fidelity KXNHLSPREAD-26NOV06ANACGY-CGY2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.159)
- KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.124)
- KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.148)
- KXNHLGOAL-26NOV06ANACGY-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.198)

portfolios: A EV +9.53 (adj +3.22) on $50.00, P(profit) 0.5911, adj growth 20.1 bp · B EV +10.23 (adj +6.95) on $27.07, P(profit) 0.4824, adj growth 59.4 bp · C EV +2.00 (adj +0.71) on $10.61, P(profit) 0.4711, adj growth 6.2 bp · R EV +1.18 (adj +0.81) on $3.00, P(profit) 0.163, adj growth 25.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
