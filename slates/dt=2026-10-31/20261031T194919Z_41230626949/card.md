# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T19:49:19Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +25.97 | +8.25 | +24.68 | 0.687 | -37.58 | -52.05 | 70.23 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +33.47 | +20.13 | +27.46 | 0.664 | -47.72 | -67.01 | 179.32 |
| C best expression per thesis | 150.00 | +25.50 | +13.26 | +21.66 | 0.654 | -42.91 | -57.63 | 116.98 |
| R FUNDED research stakes | 24.00 | +3.70 | +2.04 | +0.38 | 0.626 | -7.99 | -12.19 | 0.00 |

## BUF @ LAK  ·  10000 joint draws  ·  502 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.446 / away 0.554

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BUF_win | p_overtime | goals | shots LAK/BUF | LAK/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.57 | 0.43 | 0.00 | 6.01 | 27.9/27.9 | 24.7/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.48 | 5.92 | 28.2/28.2 | 24.9/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 9.21 | 29.5/29.3 | 23.7/23.0 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.075 | 0.61 | 0.39 | 0.00 | 5.98 | 32.7/22.2 | 19.4/28.3 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.55 | 0.45 | 0.46 | 5.87 | 32.9/22.4 | 19.2/29.6 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.063 | 0.49 | 0.51 | 0.00 | 6.0 | 22.3/32.6 | 29.0/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Laferriere: 2+ goals YES | 3 | 0.055 | 0.046 | +0.023 | +0.014 | $2.24 | FUNDED_RESEARCH | $1 | LAK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.085 | 0.071 | +0.031 | +0.018 | $2.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Andre Lee: 1+ goals YES | 9 | 0.130 | 0.115 | +0.034 | +0.019 | $3.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Scott Laughton: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $4.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Alex Laferriere: 2+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes; why: higher confidence-adjusted growth (13.15 vs 7.15 bp); despite a smaller raw edge (+0.023 vs +0.031/contract); relationships: KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: LAK offense suppressed (<= 2 goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes; why: higher confidence-adjusted growth (12.88 vs 7.15 bp); relationships: KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.03); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: LAK offense suppressed (<= 2 goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes; why: higher confidence-adjusted growth (9.19 vs 7.15 bp); relationships: KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.03); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: LAK offense suppressed (<= 2 goals)
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31BUFLA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (7.15 vs 4.80 bp); despite a smaller raw edge (+0.031 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.4051): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF3|no [DIRECT], best adjusted EV KXNHLAST-26OCT31BUFLA-LATMOORE12-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS_BY_2PLUS (p 0.3228): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no (same contract)
- thesis LAK:WINS (p 0.5429): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT31BUFLA-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3744, phi -0.157)
- KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3744, phi -0.144)
- KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3744, phi -0.163)
- KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3744, phi -0.211)

portfolios: A EV +3.91 (adj +1.09) on $26.35, P(profit) 0.5412, adj growth 9.8 bp · B EV +5.49 (adj +3.25) on $12.88, P(profit) 0.3678, adj growth 28.6 bp · C EV +4.09 (adj +1.38) on $31.09, P(profit) 0.529, adj growth 12.2 bp · R EV +0.71 (adj +0.44) on $1.00, P(profit) 0.0547, adj growth 13.7 bp

## OTT @ SJS  ·  10000 joint draws  ·  446 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.420 / away 0.580

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_OTT_win | p_overtime | goals | shots SJS/OTT | SJS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.52 | 0.48 | 0.00 | 6.03 | 26.9/27.3 | 23.8/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.48 | 0.52 | 0.45 | 5.98 | 27.1/27.4 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.53 | 0.47 | 0.00 | 9.34 | 28.3/28.8 | 22.7/22.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.089 | 0.46 | 0.54 | 0.00 | 6.04 | 21.7/32.5 | 28.7/18.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.49 | 0.51 | 0.44 | 5.92 | 21.4/32.2 | 28.9/18.2 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.063 | 0.42 | 0.58 | 0.00 | 9.25 | 23.1/34.3 | 27.3/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mason Marchment: 1+ goals YES | 22 | 0.272 | 0.257 | +0.040 | +0.025 | $5.74 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Tyler Kleven: 1+ goals YES | 4 | 0.062 | 0.054 | +0.019 | +0.011 | $2.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Ottawa wins by over 2.5 goals NO | 76 | 0.822 | 0.788 | +0.049 | +0.016 | $13.56 | FUNDED_RESEARCH | $4 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Kiefer Sherwood: 1+ goals YES | 21 | 0.241 | 0.232 | +0.019 | +0.010 | $2.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31OTTSJ-OTT3|no; why: higher confidence-adjusted growth (7.48 vs 3.08 bp); despite a smaller raw edge (+0.040 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31OTTSJ-OTTTKLEVEN43-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT31OTTSJ-OTT3|no: MOSTLY_INDEPENDENT (phi 0.136); KXNHLGOAL-26OCT31OTTSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: SJS offense suppressed (<= 2 goals)
- **Tyler Kleven: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31OTTSJ-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (6.39 vs 1.36 bp); alternative not eligible: confidence-adjusted EV +0.0094 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31OTTSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT31OTTSJ-OTT3|no: INTENTIONAL_DIVERSIFIER (phi -0.091); KXNHLGOAL-26OCT31OTTSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: OTT offense suppressed (<= 2 goals)
- **Ottawa wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31OTTSJ-SJ2|yes; why: higher confidence-adjusted growth (3.08 vs 1.17 bp); wins across more scripts (relative breadth 1.027 vs 0.52); relationships: KXNHLGOAL-26OCT31OTTSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.136); KXNHLGOAL-26OCT31OTTSJ-OTTTKLEVEN43-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.091); KXNHLGOAL-26OCT31OTTSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.119); failure: OTT wins by 2+
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31OTTSJ-SJMMARCHMENT27-1|yes; why: Player prop expression KXNHLGOAL-26OCT31OTTSJ-SJKSHERWOOD44-1|yes selected over player prop KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.36 vs 0.45 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT31OTTSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT31OTTSJ-OTTTKLEVEN43-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLSPREAD-26OCT31OTTSJ-OTT3|no: MOSTLY_INDEPENDENT (phi 0.119); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4197): highest fidelity KXNHLSPREAD-26OCT31OTTSJ-OTT3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT31OTTSJ-SJMMARCHMENT27-1|yes — Player prop expression KXNHLGOAL-26OCT31OTTSJ-SJKSHERWOOD44-1|yes selected over player prop KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.36 vs 0.45 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis SJS:WINS (p 0.5092): highest fidelity KXNHLSPREAD-26OCT31OTTSJ-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31OTTSJ-OTT3|no (same contract)
- thesis OTT:SUPPRESSED (p 0.3748): highest fidelity KXNHLSPREAD-26OCT31OTTSJ-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31OTTSJ-OTT3|no (same contract)
- KXNHLGOAL-26OCT31OTTSJ-SJMMARCHMENT27-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3634, phi -0.226)
- KXNHLGOAL-26OCT31OTTSJ-OTTTKLEVEN43-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3748, phi -0.116)
- KXNHLSPREAD-26OCT31OTTSJ-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2817, phi -0.743)
- KXNHLGOAL-26OCT31OTTSJ-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3634, phi -0.225)
- override: Player prop expression KXNHLGOAL-26OCT31OTTSJ-SJKSHERWOOD44-1|yes selected over player prop KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.36 vs 0.45 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.43 (adj +1.25) on $26.35, P(profit) 0.4553, adj growth 10.9 bp · B EV +2.99 (adj +1.54) on $23.58, P(profit) 0.4644, adj growth 13.7 bp · C EV +2.03 (adj +0.98) on $20.73, P(profit) 0.2724, adj growth 8.6 bp · R EV +0.25 (adj +0.08) on $4.00, P(profit) 0.8219, adj growth 2.9 bp

## PIT @ MTL  ·  10000 joint draws  ·  504 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.535 / away 0.465

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_PIT_win | p_overtime | goals | shots MTL/PIT | MTL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.55 | 0.45 | 0.00 | 6.06 | 27.2/27.5 | 24.2/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.55 | 0.45 | 0.00 | 9.4 | 28.8/29.0 | 23.0/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.45 | 5.91 | 27.1/27.4 | 24.0/23.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.084 | 0.50 | 0.50 | 0.00 | 6.1 | 21.8/32.6 | 28.8/18.3 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.50 | 0.50 | 0.47 | 5.93 | 21.6/32.3 | 29.0/18.4 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.066 | 0.47 | 0.53 | 0.00 | 9.24 | 23.1/34.3 | 27.4/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Blake Lizotte: 1+ goals YES | 9 | 0.121 | 0.111 | +0.025 | +0.015 | $3.05 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.159 | 0.149 | +0.021 | +0.011 | $2.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 30 | 0.337 | 0.326 | +0.022 | +0.012 | $3.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Zachary Bolduc: 1+ assists YES | 25 | 0.303 | 0.274 | +0.040 | +0.011 | $2.94 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_MIXED | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (5.50 vs 2.41 bp); relationships: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi -0.041); failure: MTL wins (incl. OT/SO)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (2.41 vs 1.39 bp); despite a smaller raw edge (+0.021 vs +0.022/contract); relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes has the higher standalone adjusted growth (2.41 vs 1.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: PIT offense suppressed (<= 2 goals)
- **Zachary Bolduc: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes; why: higher confidence-adjusted growth (1.31 vs 0.80 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.041); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4051): highest fidelity KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4375): highest fidelity KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes (same contract)
- KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:WINS (p 0.5282, phi -0.172)
- KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3817, phi -0.201)
- KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3817, phi -0.243)
- KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3469, phi -0.243)

portfolios: A EV +2.83 (adj +1.29) on $18.26, P(profit) 0.4871, adj growth 10.8 bp · B EV +1.85 (adj +0.92) on $11.76, P(profit) 0.3357, adj growth 8.2 bp · C EV +0.90 (adj +0.36) on $5.91, P(profit) 0.4133, adj growth 3.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ VAN  ·  10000 joint draws  ·  418 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.371 / away 0.629

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_TOR_win | p_overtime | goals | shots VAN/TOR | VAN/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.50 | 0.50 | 0.00 | 6.05 | 28.3/28.4 | 24.9/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.47 | 5.96 | 28.5/28.7 | 25.3/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.109 | 0.51 | 0.49 | 0.00 | 9.38 | 29.9/30.0 | 23.7/23.6 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.073 | 0.47 | 0.53 | 0.00 | 6.06 | 22.3/33.3 | 29.2/19.0 | even strength |
| TOR shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.46 | 0.54 | 0.47 | 6.0 | 22.9/33.4 | 30.1/19.7 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.061 | 0.55 | 0.45 | 0.00 | 6.05 | 33.0/22.8 | 19.6/29.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Linus Karlsson: 1+ goals YES | 19 | 0.269 | 0.248 | +0.069 | +0.048 | $10.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.247 | 0.228 | +0.056 | +0.037 | $8.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 71 | 0.784 | 0.764 | +0.059 | +0.040 | $15.89 | FUNDED_RESEARCH | $4 | TOR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 16 | 0.211 | 0.196 | +0.042 | +0.027 | $5.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (30.17 vs 19.30 bp); relationships: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (30.17 vs 19.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: VAN offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31TORVAN-TORWNYLANDER88-2|no; why: higher confidence-adjusted growth (17.38 vs 8.86 bp); despite a smaller raw edge (+0.059 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: TOR offense succeeds (4+ goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (30.17 vs 10.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4305): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLSPREAD-26OCT31TORVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3557): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.239)
- KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.223)
- KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4235, phi -0.203)
- KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.212)

portfolios: A EV +4.75 (adj +0.89) on $26.35, P(profit) 0.6466, adj growth 7.6 bp · B EV +8.69 (adj +5.82) on $40.13, P(profit) 0.5372, adj growth 52.4 bp · C EV +6.51 (adj +4.15) on $33.13, P(profit) 0.4143, adj growth 36.8 bp · R EV +0.33 (adj +0.22) on $4.00, P(profit) 0.7837, adj growth 8.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT31TORVAN-VAN|yes == KXNHLGAME-26OCT31TORVAN-TOR|no

## CBJ @ DAL  ·  10000 joint draws  ·  458 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.625 / away 0.375

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_CBJ_win | p_overtime | goals | shots DAL/CBJ | DAL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.56 | 0.44 | 0.00 | 5.97 | 26.1/25.9 | 22.7/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.47 | 5.89 | 26.2/25.9 | 22.7/23.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.085 | 0.57 | 0.43 | 0.00 | 5.98 | 31.3/20.7 | 17.6/27.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.58 | 0.42 | 0.46 | 5.86 | 30.9/20.5 | 17.3/27.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.57 | 0.43 | 0.00 | 9.23 | 27.9/27.8 | 21.9/21.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.54 | 0.46 | 0.00 | 3.44 | 25.0/24.8 | 23.0/22.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 18 | 0.254 | 0.234 | +0.063 | +0.043 | $9.99 | FUNDED_RESEARCH | $3 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 6 | 0.107 | 0.091 | +0.043 | +0.027 | $4.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.187 | 0.170 | +0.049 | +0.032 | $6.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan Lomberg: 1+ goals YES | 5 | 0.077 | 0.069 | +0.024 | +0.016 | $2.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (26.37 vs 18.71 bp); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense suppressed (<= 2 goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (26.37 vs 25.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (26.37 vs 18.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Ryan Lomberg: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (26.37 vs 10.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3151): highest fidelity KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.249): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.4138): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-DALMRANTANEN96-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.241)
- KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.155)
- KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.225)
- KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.125)

portfolios: A EV +4.38 (adj +2.24) on $26.35, P(profit) 0.4766, adj growth 20.5 bp · B EV +10.11 (adj +6.70) on $24.23, P(profit) 0.4991, adj growth 59.0 bp · C EV +7.92 (adj +5.09) on $41.41, P(profit) 0.3933, adj growth 44.6 bp · R EV +1.00 (adj +0.69) on $3.00, P(profit) 0.2535, adj growth 23.7 bp

## CGY @ COL  ·  10000 joint draws  ·  454 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.777 / away 0.223

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_CGY_win | p_overtime | goals | shots COL/CGY | COL/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.156 | 0.81 | 0.19 | 0.00 | 6.02 | 35.6/22.7 | 20.6/30.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.119 | 0.83 | 0.17 | 0.00 | 9.37 | 37.8/24.3 | 20.4/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.78 | 0.22 | 0.00 | 6.04 | 29.7/28.9 | 26.5/24.7 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.60 | 0.40 | 0.47 | 5.95 | 36.6/23.2 | 20.2/33.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.74 | 0.26 | 0.00 | 9.38 | 31.3/30.4 | 25.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.56 | 0.44 | 0.51 | 5.99 | 30.0/29.1 | 25.8/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cale Makar: 1+ goals NO | 74 | 0.803 | 0.786 | +0.050 | +0.033 | $16.15 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Calgary over 3.5 goals scored YES | 20 | 0.283 | 0.239 | +0.072 | +0.028 | $6.10 | FUNDED_RESEARCH | $2 | CGY:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado over 5.5 goals scored NO | 74 | 0.810 | 0.773 | +0.057 | +0.019 | $13.06 | FUNDED_RESEARCH | $4 | CGY:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Colorado over 4.5 goals scored NO | 56 | 0.638 | 0.597 | +0.061 | +0.019 | $2.10 | FUNDED_RESEARCH | $1 | CGY:WINS | DIRECT (0.95) | EVIDENCE_MIXED | D |
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT31CGYCOL-COL|no; why: higher confidence-adjusted growth (12.60 vs 6.67 bp); despite a smaller raw edge (+0.050 vs +0.083/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5|no: REINFORCING (phi 0.161); failure: COL offense succeeds (4+ goals)
- **Calgary over 3.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT31CGYCOL-COL|no; why: higher confidence-adjusted growth (10.00 vs 6.67 bp); despite a smaller raw edge (+0.072 vs +0.083/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.025); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5|no: MOSTLY_INDEPENDENT (phi 0.015); failure: CGY offense suppressed (<= 2 goals)
- **Colorado over 5.5 goals scored NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes has the higher standalone adjusted growth (10.00 vs 4.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5|no: DUPLICATIVE (phi 0.642); failure: high-event game (8+ goals)
- **Colorado over 4.5 goals scored NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes has the higher standalone adjusted growth (10.00 vs 3.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: REINFORCING (phi 0.161); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: DUPLICATIVE (phi 0.642); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.16, COL shot control · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CGY:OFFENSE_4PLUS (p 0.2746): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes (same contract)
- thesis CGY:WINS (p 0.3041): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT31CGYCOL-COL2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no kept
- thesis COL:SUPPRESSED (p 0.2363): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5689, phi -0.172)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:SUPPRESSED (p 0.5111, phi -0.642)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.3114, phi -0.579)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5|no: FUNDED_RESEARCH; family MIXED; loses 5% of the draws where the thesis happens; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5689, phi -0.655)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT31CGYCOL-COL2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no kept
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT31CGYCOL-COL2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5|no kept

portfolios: A EV +6.67 (adj +1.49) on $26.35, P(profit) 0.5695, adj growth 10.7 bp · B EV +4.34 (adj +1.90) on $37.42, P(profit) 0.7451, adj growth 17.4 bp · C EV +4.05 (adj +1.30) on $17.73, P(profit) 0.3446, adj growth 11.4 bp · R EV +1.42 (adj +0.61) on $12.00, P(profit) 0.6483, adj growth 21.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
