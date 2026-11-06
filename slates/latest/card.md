# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-06T22:37:13Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +29.39 | +9.12 | +23.44 | 0.619 | -72.60 | -95.02 | 59.41 |
| B thesis-diversified (joint) ← optimiser card | 100.51 | +22.89 | +13.39 | +14.02 | 0.598 | -54.78 | -57.98 | 115.63 |
| C best expression per thesis | 88.55 | +10.93 | +4.30 | +8.70 | 0.596 | -27.98 | -38.07 | 37.95 |
| R FUNDED research stakes | 14.00 | +3.24 | +1.89 | -0.80 | 0.299 | -8.42 | -14.00 | 0.00 |

## CBJ @ BUF  ·  10000 joint draws  ·  442 bet sides mapped, 5 +EV candidates, 4 on card

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
| Mathieu Olivier: 1+ goals YES | 15 | 0.195 | 0.183 | +0.036 | +0.024 | $6.37 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 21 | 0.257 | 0.244 | +0.035 | +0.022 | $6.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 26 | 0.301 | 0.289 | +0.028 | +0.015 | $6.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Buffalo over 3.5 goals scored NO | 52 | 0.588 | 0.549 | +0.050 | +0.011 | $8.20 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (9.08 vs 6.26 bp); relationships: KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no: MOSTLY_INDEPENDENT (phi 0.058); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (9.08 vs 6.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.028); they share one thesis budget; relationships: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no: MOSTLY_INDEPENDENT (phi 0.016); failure: CBJ offense suppressed (<= 2 goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26NOV06CBJBUF-BUFMSAMUELSSON23-1|yes; why: higher confidence-adjusted growth (2.52 vs 0.41 bp); despite a smaller raw edge (+0.028 vs +0.031/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no: INTENTIONAL_DIVERSIFIER (phi -0.266); failure: BUF offense suppressed (<= 2 goals)
- **Buffalo over 3.5 goals scored NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV06CBJBUF-BUF3|no; why: higher confidence-adjusted growth (1.15 vs 1.10 bp); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.058); KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.266); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3404): highest fidelity KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.4029): highest fidelity KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.4514): highest fidelity KXNHLGOAL-26NOV06CBJBUF-CBJKJOHNSON91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV06CBJBUF-CBJKJOHNSON91-1|no (same contract)
- KXNHLGOAL-26NOV06CBJBUF-CBJMOLIVIER24-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4514, phi -0.236)
- KXNHLGOAL-26NOV06CBJBUF-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4514, phi -0.266)
- KXNHLGOAL-26NOV06CBJBUF-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3714, phi -0.268)
- KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4029, phi -0.981)

portfolios: A EV +6.88 (adj +3.58) on $50.00, P(profit) 0.4184, adj growth 27.9 bp · B EV +3.95 (adj +2.16) on $27.77, P(profit) 0.4665, adj growth 18.7 bp · C EV +3.22 (adj +1.66) on $32.43, P(profit) 0.4099, adj growth 14.4 bp · R EV +0.28 (adj +0.06) on $3.00, P(profit) 0.5878, adj growth 1.9 bp

## SJS @ MIN  ·  10000 joint draws  ·  420 bet sides mapped, 19 +EV candidates, 4 on card

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
| Yakov Trenin: 1+ goals YES | 11 | 0.163 | 0.148 | +0.046 | +0.031 | $8.51 | FUNDED_RESEARCH | $3 | MIN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Minnesota wins by over 2.5 goals NO | 64 | 0.735 | 0.685 | +0.079 | +0.029 | $20.00 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Olli Maatta: 1+ goals YES | 5 | 0.077 | 0.067 | +0.024 | +0.013 | $3.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Macklin Celebrini: 1+ assists NO | 52 | 0.608 | 0.559 | +0.070 | +0.021 | $14.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.77) | EVIDENCE_MIXED | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (20.28 vs 1.91 bp); relationships: KXNHLSPREAD-26NOV06SJMIN-MIN3|no: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLGOAL-26NOV06SJMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV06SJMIN-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: MIN offense suppressed (<= 2 goals)
- **Minnesota wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV06SJMIN-MIN2|no; why: higher confidence-adjusted growth (8.06 vs 2.72 bp); despite a smaller raw edge (+0.079 vs +0.092/contract); wins across more scripts (relative breadth 1.017 vs 0.88); relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLGOAL-26NOV06SJMIN-MINOMAATTA3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.085); KXNHLAST-26NOV06SJMIN-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.172); failure: MIN wins by 2+
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV06SJMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (7.65 vs 1.91 bp); despite a smaller raw edge (+0.024 vs +0.025/contract); relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26NOV06SJMIN-MIN3|no: INTENTIONAL_DIVERSIFIER (phi -0.085); KXNHLAST-26NOV06SJMIN-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: MIN offense suppressed (<= 2 goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV06SJMIN-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (4.03 vs 0.55 bp); despite a smaller raw edge (+0.070 vs +0.076/contract); alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26NOV06SJMIN-MIN3|no: INTENTIONAL_DIVERSIFIER (phi -0.172); KXNHLGOAL-26NOV06SJMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:TIGHT (p 0.4175): highest fidelity KXNHLSPREAD-26NOV06SJMIN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06SJMIN-MIN3|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3107): highest fidelity KXNHLTEAMTOTAL-26NOV06SJMIN-SJ3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06SJMIN-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3095): highest fidelity KXNHLSPREAD-26NOV06SJMIN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06SJMIN-MIN3|no (same contract)
- KXNHLGOAL-26NOV06SJMIN-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.157)
- KXNHLSPREAD-26NOV06SJMIN-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3904, phi -0.751)
- KXNHLGOAL-26NOV06SJMIN-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3095, phi -0.114)
- KXNHLAST-26NOV06SJMIN-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 23% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3107, phi -0.282)

portfolios: A EV +12.03 (adj +2.10) on $50.00, P(profit) 0.5861, adj growth 12.5 bp · B EV +9.09 (adj +4.55) on $46.38, P(profit) 0.5628, adj growth 39.8 bp · C EV +6.08 (adj +2.05) on $50.00, P(profit) 0.6814, adj growth 18.4 bp · R EV +1.77 (adj +1.02) on $8.00, P(profit) 0.1626, adj growth 33.7 bp

## ANA @ CGY  ·  10000 joint draws  ·  462 bet sides mapped, 16 +EV candidates, 4 on card

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
| Sam Colangelo: 1+ goals YES | 11 | 0.163 | 0.148 | +0.046 | +0.032 | $8.04 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Pavel Mintyukov: 1+ goals YES | 6 | 0.099 | 0.088 | +0.035 | +0.024 | $5.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 9 | 0.130 | 0.119 | +0.035 | +0.023 | $5.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 16 | 0.207 | 0.194 | +0.038 | +0.025 | $6.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5|yes; why: higher confidence-adjusted growth (20.66 vs 5.67 bp); despite a smaller raw edge (+0.046 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.874 vs 0.526); relationships: KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV06ANACGY-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: ANA offense suppressed (<= 2 goals)
- **Pavel Mintyukov: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5|yes; why: higher confidence-adjusted growth (20.06 vs 5.67 bp); despite a smaller raw edge (+0.035 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.848 vs 0.526); relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV06ANACGY-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5|yes; why: higher confidence-adjusted growth (13.31 vs 5.67 bp); despite a smaller raw edge (+0.035 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.823 vs 0.526); relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV06ANACGY-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5|yes; why: higher confidence-adjusted growth (9.33 vs 5.67 bp); despite a smaller raw edge (+0.038 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.856 vs 0.526); relationships: KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4621): highest fidelity KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06ANACGY-CGY2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5319): highest fidelity KXNHLSPREAD-26NOV06ANACGY-CGY2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06ANACGY-CGY2|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3229): highest fidelity KXNHLSPREAD-26NOV06ANACGY-CGY2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06ANACGY-CGY2|no (same contract)
- KXNHLGOAL-26NOV06ANACGY-ANASCOLANGELO12-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.159)
- KXNHLGOAL-26NOV06ANACGY-ANAPMINTYUKOV98-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.124)
- KXNHLGOAL-26NOV06ANACGY-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.148)
- KXNHLGOAL-26NOV06ANACGY-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3248, phi -0.169)

portfolios: A EV +10.48 (adj +3.44) on $50.00, P(profit) 0.536, adj growth 19.1 bp · B EV +9.85 (adj +6.68) on $26.36, P(profit) 0.4822, adj growth 57.0 bp · C EV +1.63 (adj +0.59) on $6.12, P(profit) 0.2807, adj growth 5.1 bp · R EV +1.18 (adj +0.81) on $3.00, P(profit) 0.163, adj growth 25.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
