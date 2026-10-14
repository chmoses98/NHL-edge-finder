# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-14T01:01:45Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +54.93 | +11.39 | +49.19 | 0.717 | -50.95 | -68.32 | 78.71 |
| B thesis-diversified (joint) ← optimiser card | 101.91 | +28.85 | +15.13 | +16.03 | 0.585 | -42.58 | -58.12 | 129.99 |
| C best expression per thesis | 101.67 | +21.65 | +6.65 | +18.79 | 0.748 | -24.57 | -33.02 | 59.41 |
| R FUNDED research stakes | 5.00 | +2.16 | +1.49 | -5.00 | 0.307 | -5.00 | -5.00 | 0.00 |

## CGY @ ANA  ·  10000 joint draws  ·  494 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.604 / away 0.396

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
| Tim Washe: 1+ goals YES | 9 | 0.149 | 0.133 | +0.053 | +0.037 | $8.97 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| A.J. Greer: 2+ goals YES | 2 | 0.044 | 0.038 | +0.023 | +0.017 | $3.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.08) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 9 | 0.140 | 0.126 | +0.044 | +0.030 | $7.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Pavel Mintyukov: 1+ goals YES | 7 | 0.100 | 0.091 | +0.025 | +0.016 | $3.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (33.73 vs 5.88 bp); despite a smaller raw edge (+0.053 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT13CGYANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: ANA offense suppressed (<= 2 goals)
- **A.J. Greer: 2+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (27.05 vs 5.88 bp); despite a smaller raw edge (+0.023 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT13CGYANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (22.23 vs 5.88 bp); despite a smaller raw edge (+0.044 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT13CGYANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: ANA offense suppressed (<= 2 goals)
- **Pavel Mintyukov: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (8.32 vs 5.88 bp); despite a smaller raw edge (+0.025 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.497): highest fidelity KXNHLAST-26OCT13CGYANA-ANAJLACOMBE2-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.137)
- KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 92% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.13)
- KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.147)
- KXNHLGOAL-26OCT13CGYANA-ANAPMINTYUKOV98-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.134)

portfolios: A EV +23.59 (adj +7.09) on $50.00, P(profit) 0.5668, adj growth 49.7 bp · B EV +13.29 (adj +9.33) on $23.65, P(profit) 0.372, adj growth 78.5 bp · C EV +1.91 (adj +0.63) on $8.44, P(profit) 0.3986, adj growth 5.5 bp · R EV +1.67 (adj +1.17) on $3.00, P(profit) 0.149, adj growth 37.3 bp

## EDM @ LAK  ·  10000 joint draws  ·  480 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.460 / away 0.540

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
| Artemi Panarin: 2+ assists NO | 82 | 0.910 | 0.862 | +0.080 | +0.032 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ assists YES | 28 | 0.353 | 0.312 | +0.059 | +0.018 | $6.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
| Leon Draisaitl: 1+ assists NO | 41 | 0.565 | 0.445 | +0.138 | +0.018 | $8.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.76) | CALIBRATION_WARNING | D |
| Alex Laferriere: 1+ goals YES | 25 | 0.286 | 0.276 | +0.023 | +0.013 | $4.54 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Artemi Panarin: 2+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (16.26 vs 4.33 bp); despite a smaller raw edge (+0.080 vs +0.105/contract); relationships: KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT13EDMLA-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.059); failure: LAK offense succeeds (4+ goals)
- **Mattias Ekholm: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes; why: Player prop expression KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.50 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.069); KXNHLGOAL-26OCT13EDMLA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: EDM offense suppressed (<= 2 goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (2.89 vs 1.91 bp); relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.069); KXNHLGOAL-26OCT13EDMLA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: EDM offense succeeds (4+ goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes; why: Player prop expression KXNHLGOAL-26OCT13EDMLA-LAALAFERRIERE14-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.43 vs 0.49 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: INTENTIONAL_DIVERSIFIER (phi -0.059); KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4138): highest fidelity KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.395): highest fidelity KXNHLAST-26OCT13EDMLA-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes — Player prop expression KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.50 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis LAK:OFFENSE_4PLUS (p 0.3679): highest fidelity KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes (same contract)
- KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3679, phi -0.251)
- KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3893, phi -0.253)
- KXNHLAST-26OCT13EDMLA-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 24% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.0 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.395, phi -0.298)
- KXNHLGOAL-26OCT13EDMLA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4138, phi -0.251)
- override: Player prop expression KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.50 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26OCT13EDMLA-LAALAFERRIERE14-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.43 vs 0.49 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +21.36 (adj +2.56) on $50.00, P(profit) 0.7234, adj growth 14.9 bp · B EV +6.30 (adj +1.72) on $39.32, P(profit) 0.7543, adj growth 15.8 bp · C EV +9.79 (adj +2.58) on $43.23, P(profit) 0.7757, adj growth 23.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ SJS  ·  10000 joint draws  ·  536 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.464 / away 0.536

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
| Casey Mittelstadt: 1+ goals YES | 14 | 0.185 | 0.172 | +0.036 | +0.024 | $6.98 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Charlie McAvoy: 1+ assists NO | 55 | 0.703 | 0.600 | +0.136 | +0.033 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Marat Khusnutdinov: 1+ goals YES | 11 | 0.148 | 0.137 | +0.031 | +0.020 | $5.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: 1+ goals YES | 17 | 0.215 | 0.203 | +0.035 | +0.023 | $6.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13BOSSJ-BOSNZADOROV91-1|yes; why: higher confidence-adjusted growth (9.81 vs 0.00 bp); despite a smaller raw edge (+0.036 vs +0.050/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: BOS offense suppressed (<= 2 goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13BOSSJ-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (9.75 vs 2.71 bp); despite a smaller raw edge (+0.136 vs +0.137/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: BOS offense succeeds (4+ goals)
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes has the higher standalone adjusted growth (9.81 vs 8.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: BOS offense suppressed (<= 2 goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13BOSSJ-SJICHERNYSHOV92-1|yes; why: higher confidence-adjusted growth (7.70 vs 4.19 bp); despite a smaller raw edge (+0.035 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.401): highest fidelity KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.385): highest fidelity KXNHLPTS-26OCT13BOSSJ-BOSCMCAVOY73-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:OFFENSE_4PLUS (p 0.4005): highest fidelity KXNHLAST-26OCT13BOSSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.385, phi -0.189)
- KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.401, phi -0.228)
- KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.385, phi -0.171)
- KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3796, phi -0.207)

portfolios: A EV +9.98 (adj +1.74) on $50.00, P(profit) 0.6786, adj growth 14.2 bp · B EV +9.25 (adj +4.08) on $38.94, P(profit) 0.4127, adj growth 35.6 bp · C EV +9.95 (adj +3.44) on $50.00, P(profit) 0.7267, adj growth 30.7 bp · R EV +0.49 (adj +0.32) on $2.00, P(profit) 0.1849, adj growth 10.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
