# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-06T23:33:09Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +30.51 | +8.33 | +28.33 | 0.647 | -65.68 | -87.85 | 56.37 |
| B thesis-diversified (joint) ← optimiser card | 88.47 | +17.82 | +11.35 | +11.54 | 0.591 | -54.08 | -65.16 | 97.80 |
| C best expression per thesis | 106.36 | +13.25 | +5.00 | +11.72 | 0.645 | -31.84 | -43.40 | 43.69 |
| R FUNDED research stakes | 11.00 | +1.93 | +1.15 | +2.79 | 0.534 | -11.00 | -11.00 | 0.00 |

## CBJ @ BUF  ·  10000 joint draws  ·  466 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.609 / away 0.392

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
| Mathieu Olivier: 1+ goals YES | 15 | 0.195 | 0.183 | +0.036 | +0.024 | $6.37 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 21 | 0.257 | 0.244 | +0.035 | +0.022 | $6.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 26 | 0.301 | 0.289 | +0.028 | +0.015 | $6.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Buffalo over 3.5 goals scored NO | 52 | 0.588 | 0.549 | +0.050 | +0.011 | $8.20 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (9.08 vs 6.26 bp); relationships: KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no: MOSTLY_INDEPENDENT (phi 0.058); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (9.08 vs 6.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.028); they share one thesis budget; relationships: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no: MOSTLY_INDEPENDENT (phi 0.016); failure: CBJ offense suppressed (<= 2 goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26NOV06CBJBUF-BUFMSAMUELSSON23-1|yes; why: higher confidence-adjusted growth (2.52 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0008 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no: INTENTIONAL_DIVERSIFIER (phi -0.266); failure: BUF offense suppressed (<= 2 goals)
- **Buffalo over 3.5 goals scored NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV06CBJBUF-BUF3|no; why: higher confidence-adjusted growth (1.15 vs 1.10 bp); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.058); KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.266); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3404): highest fidelity KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.4029): highest fidelity KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.4514): highest fidelity KXNHLGOAL-26NOV06CBJBUF-CBJKJOHNSON91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV06CBJBUF-CBJKJOHNSON91-1|no (same contract)
- KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4514, phi -0.236)
- KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4514, phi -0.266)
- KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3714, phi -0.268)
- KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4029, phi -0.981)

portfolios: A EV +6.88 (adj +3.58) on $50.00, P(profit) 0.4184, adj growth 27.9 bp · B EV +3.95 (adj +2.16) on $27.77, P(profit) 0.4665, adj growth 18.7 bp · C EV +3.22 (adj +1.66) on $32.43, P(profit) 0.4099, adj growth 14.4 bp · R EV +0.74 (adj +0.36) on $5.00, P(profit) 0.6569, adj growth 11.8 bp

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
| Yakov Trenin: 1+ goals YES | 11 | 0.163 | 0.148 | +0.046 | +0.031 | $7.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 47 | 0.536 | 0.517 | +0.049 | +0.030 | $12.84 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.75) | EVIDENCE_STRONGER | D |
| Blake Coleman: 1+ goals YES | 23 | 0.278 | 0.264 | +0.035 | +0.022 | $7.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 2+ goals NO | 84 | 0.873 | 0.861 | +0.024 | +0.011 | $6.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.98) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (20.28 vs 5.71 bp); relationships: KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.003); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV06SJMIN-MIN3|no; why: higher confidence-adjusted growth (7.84 vs 4.34 bp); despite a smaller raw edge (+0.049 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.03 vs 0.793); relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-2|no: DUPLICATIVE (phi 0.411); failure: MIN offense succeeds (4+ goals)
- **Blake Coleman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26NOV06SJMIN-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (5.71 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.007); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 2+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no; why: Player prop expression KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-2|no selected over broad KXNHLTEAMTOTAL-26NOV06SJMIN-MIN3|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.98 vs 0.96 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: DUPLICATIVE (phi 0.411); KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis MIN:SUPPRESSED (p 0.3095): highest fidelity KXNHLSPREAD-26NOV06SJMIN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no — Player prop expression KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-2|no selected over broad KXNHLTEAMTOTAL-26NOV06SJMIN-MIN3|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.98 vs 0.96 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis SJS:WINS (p 0.381): highest fidelity KXNHLSPREAD-26NOV06SJMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.4816): highest fidelity KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes (same contract)
- KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.157)
- KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 25% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4816, phi -0.286)
- KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.232)
- KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-2|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4816, phi -0.264)
- override: Player prop expression KXNHLGOAL-26NOV06SJMIN-MINKKAPRIZOV97-2|no selected over broad KXNHLTEAMTOTAL-26NOV06SJMIN-MIN3|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.98 vs 0.96 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +14.23 (adj +2.10) on $50.00, P(profit) 0.5733, adj growth 9.7 bp · B EV +5.61 (adj +3.65) on $34.64, P(profit) 0.3672, adj growth 31.5 bp · C EV +6.51 (adj +2.40) on $45.29, P(profit) 0.7155, adj growth 21.0 bp · R EV +0.40 (adj +0.25) on $4.00, P(profit) 0.5365, adj growth 8.5 bp

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
| Sam Colangelo: 1+ goals YES | 11 | 0.163 | 0.148 | +0.046 | +0.032 | $7.98 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 9 | 0.130 | 0.119 | +0.035 | +0.023 | $5.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 16 | 0.207 | 0.194 | +0.038 | +0.025 | $6.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 11 | 0.149 | 0.138 | +0.032 | +0.021 | $5.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV06ANACGY-CGY2|no; why: higher confidence-adjusted growth (20.66 vs 4.90 bp); despite a smaller raw edge (+0.046 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV06ANACGY-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV06ANACGY-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV06ANACGY-CGY2|no; why: higher confidence-adjusted growth (13.31 vs 4.90 bp); despite a smaller raw edge (+0.035 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV06ANACGY-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV06ANACGY-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV06ANACGY-CGY2|no; why: higher confidence-adjusted growth (9.33 vs 4.90 bp); despite a smaller raw edge (+0.038 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV06ANACGY-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: ANA offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV06ANACGY-CGY2|no; why: higher confidence-adjusted growth (9.18 vs 4.90 bp); despite a smaller raw edge (+0.032 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV06ANACGY-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4621): highest fidelity KXNHLTEAMTOTAL-26NOV06ANACGY-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06ANACGY-CGY2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5319): highest fidelity KXNHLSPREAD-26NOV06ANACGY-CGY2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06ANACGY-CGY2|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3229): highest fidelity KXNHLSPREAD-26NOV06ANACGY-CGY2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06ANACGY-CGY2|no (same contract)
- KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.159)
- KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.148)
- KXNHLGOAL-26NOV06ANACGY-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.169)
- KXNHLGOAL-26NOV06ANACGY-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.168)

portfolios: A EV +9.40 (adj +2.65) on $50.00, P(profit) 0.4896, adj growth 18.9 bp · B EV +8.25 (adj +5.54) on $26.06, P(profit) 0.5077, adj growth 47.6 bp · C EV +3.52 (adj +0.94) on $28.64, P(profit) 0.7314, adj growth 8.3 bp · R EV +0.79 (adj +0.54) on $2.00, P(profit) 0.163, adj growth 18.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
