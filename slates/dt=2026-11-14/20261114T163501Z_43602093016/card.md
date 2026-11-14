# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-14T16:35:01Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.06 | +25.91 | +10.15 | +25.16 | 0.789 | -13.97 | -23.78 | 96.70 |
| B thesis-diversified (joint) ← optimiser card | 147.48 | +29.75 | +14.79 | +27.92 | 0.799 | -13.76 | -25.33 | 141.83 |
| C best expression per thesis | 148.68 | +28.06 | +13.44 | +25.93 | 0.751 | -21.26 | -32.90 | 126.49 |
| R FUNDED research stakes | 15.00 | +2.79 | +1.41 | +1.46 | 0.634 | -4.61 | -5.87 | 0.00 |

## SEA @ CAR  ·  10000 joint draws  ·  430 bet sides mapped, 46 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_SEA_win | p_overtime | goals | shots CAR/SEA | CAR/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.187 | 0.65 | 0.35 | 0.00 | 6.06 | 34.7/20.7 | 17.9/30.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.152 | 0.54 | 0.46 | 0.45 | 5.95 | 34.6/20.8 | 17.6/31.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.147 | 0.65 | 0.35 | 0.00 | 9.44 | 36.6/22.2 | 17.3/28.9 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.077 | 0.61 | 0.39 | 0.00 | 3.46 | 33.5/19.7 | 18.2/31.2 | even strength |
| CAR shot control · high event (8+) · tight (1-goal/OT) | 0.070 | 0.54 | 0.46 | 0.59 | 9.61 | 36.7/22.7 | 17.1/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.069 | 0.57 | 0.43 | 0.00 | 6.07 | 27.7/26.5 | 23.2/23.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 42 | 0.639 | 0.493 | +0.202 | +0.057 | $3.99 | FUNDED_RESEARCH | $1 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 55 | 0.759 | 0.620 | +0.192 | +0.052 | $5.88 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikolaj Ehlers: 1+ goals NO | 71 | 0.779 | 0.760 | +0.054 | +0.036 | $6.14 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Carolina wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes has the higher standalone adjusted growth (53.95 vs 28.25 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.296); relationships: KXNHLSPREAD-26NOV14SEACAR-CAR3|no: DUPLICATIVE (phi 0.75); KXNHLGOAL-26NOV14SEACAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.145); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: Broad expression KXNHLSPREAD-26NOV14SEACAR-CAR3|no selected over player prop KXNHLAST-26NOV14SEACAR-CARSAHO20-1|no because adjusted EV is 2.0 pts higher while thesis capture is 1.00 vs 0.84 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV14SEACAR-CAR2|no: DUPLICATIVE (phi 0.75); KXNHLGOAL-26NOV14SEACAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.129); failure: CAR wins by 2+
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes has the higher standalone adjusted growth (53.95 vs 14.17 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.099); relationships: KXNHLSPREAD-26NOV14SEACAR-CAR2|no: MOSTLY_INDEPENDENT (phi 0.145); KXNHLSPREAD-26NOV14SEACAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.129); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.19, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15, CAR shot control · high event (8+) · decided (2+) 0.15.
- thesis SEA:OFFENSE_4PLUS (p 0.3738): highest fidelity KXNHLTEAMTOTAL-26NOV14SEACAR-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.223): highest fidelity KXNHLSPREAD-26NOV14SEACAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no (same contract)
- thesis CAR:SUPPRESSED (p 0.3053): highest fidelity KXNHLSPREAD-26NOV14SEACAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no — Broad expression KXNHLSPREAD-26NOV14SEACAR-CAR3|no selected over player prop KXNHLAST-26NOV14SEACAR-CARSAHO20-1|no because adjusted EV is 2.0 pts higher while thesis capture is 1.00 vs 0.84 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLSPREAD-26NOV14SEACAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 22.4 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3607, phi -1.0)
- KXNHLSPREAD-26NOV14SEACAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 21.4 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3607, phi -0.75)
- KXNHLGOAL-26NOV14SEACAR-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4885, phi -0.189)
- override: Broad expression KXNHLSPREAD-26NOV14SEACAR-CAR3|no selected over player prop KXNHLAST-26NOV14SEACAR-CARSAHO20-1|no because adjusted EV is 2.0 pts higher while thesis capture is 1.00 vs 0.84 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.03 (adj +0.95) on $11.17, P(profit) 0.7315, adj growth 9.2 bp · B EV +4.29 (adj +1.36) on $16.01, P(profit) 0.7264, adj growth 13.2 bp · C EV +6.33 (adj +3.82) on $7.70, P(profit) 0.307, adj growth 35.7 bp · R EV +1.29 (adj +0.41) on $5.00, P(profit) 0.7264, adj growth 15.9 bp
equivalent contracts collapsed: KXNHLGAME-26NOV14SEACAR-CAR|no == KXNHLGAME-26NOV14SEACAR-SEA|yes

## WPG @ CHI  ·  10000 joint draws  ·  424 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.46 | 0.54 | 0.00 | 6.04 | 26.8/27.3 | 23.7/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.47 | 5.95 | 26.7/27.0 | 23.8/23.4 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.098 | 0.39 | 0.61 | 0.00 | 6.04 | 21.2/32.2 | 27.8/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.47 | 0.53 | 0.00 | 9.25 | 27.9/28.2 | 22.2/22.0 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.48 | 0.52 | 0.49 | 5.91 | 21.3/32.3 | 28.7/18.1 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.060 | 0.39 | 0.61 | 0.00 | 9.29 | 22.5/34.1 | 26.5/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.263 | 0.249 | +0.042 | +0.027 | $2.96 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Mario Ferraro: 1+ goals YES | 5 | 0.074 | 0.067 | +0.021 | +0.013 | $1.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:WINS_BY_2PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 60 | 0.733 | 0.640 | +0.117 | +0.023 | $6.58 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Oliver Moore: 1+ goals YES | 12 | 0.150 | 0.141 | +0.023 | +0.014 | $1.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14WPGCHI-WPG2|no; why: higher confidence-adjusted growth (9.12 vs 2.04 bp); despite a smaller raw edge (+0.042 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14WPGCHI-WPGMFERRARO38-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLGOAL-26NOV14WPGCHI-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CHI offense suppressed (<= 2 goals)
- **Mario Ferraro: 1+ goals YES** — thesis: WPG wins by 2+; alternative: KXNHLPTS-26NOV14WPGCHI-CHICBEDARD98-2|no; why: higher confidence-adjusted growth (7.51 vs 0.00 bp); despite a smaller raw edge (+0.021 vs +0.026/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14WPGCHI-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV14WPGCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (5.06 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLGOAL-26NOV14WPGCHI-WPGMFERRARO38-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14WPGCHI-CHIOMOORE11-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.105); failure: CHI offense succeeds (4+ goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (9.12 vs 3.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV14WPGCHI-WPGMFERRARO38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.105); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.367): highest fidelity KXNHLSPREAD-26NOV14WPGCHI-WPG2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4142): highest fidelity KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no (same contract)
- thesis WPG:SUPPRESSED (p 0.3806): highest fidelity KXNHLSPREAD-26NOV14WPGCHI-WPG2|no [DIRECT], best adjusted EV KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4142, phi -0.244)
- KXNHLGOAL-26NOV14WPGCHI-WPGMFERRARO38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3806, phi -0.136)
- KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.367, phi -0.231)
- KXNHLGOAL-26NOV14WPGCHI-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4142, phi -0.172)

portfolios: A EV +1.45 (adj +0.32) on $11.17, P(profit) 0.7574, adj growth 3.1 bp · B EV +2.46 (adj +1.03) on $12.03, P(profit) 0.3844, adj growth 9.9 bp · C EV +3.46 (adj +1.01) on $20.48, P(profit) 0.6341, adj growth 9.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ BOS  ·  10000 joint draws  ·  396 bet sides mapped, 18 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_MIN_win | p_overtime | goals | shots BOS/MIN | BOS/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.57 | 0.43 | 0.00 | 6.07 | 28.5/28.7 | 25.3/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.45 | 5.95 | 28.2/28.5 | 25.1/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.58 | 0.42 | 0.00 | 9.43 | 29.7/29.8 | 24.1/22.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.075 | 0.51 | 0.49 | 0.00 | 6.05 | 22.7/33.9 | 30.2/19.1 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.49 | 0.51 | 0.46 | 5.94 | 22.5/33.7 | 30.2/19.5 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.058 | 0.65 | 0.35 | 0.00 | 6.04 | 32.8/22.4 | 19.6/28.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Danila Yurov: 1+ goals YES | 16 | 0.217 | 0.202 | +0.048 | +0.032 | $2.96 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| William Borgen: 1+ goals YES | 5 | 0.084 | 0.071 | +0.030 | +0.018 | $1.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:WINS_BY_2PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.140 | 0.129 | +0.034 | +0.022 | $1.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Mark Kastelic: 1+ goals YES | 9 | 0.122 | 0.113 | +0.027 | +0.017 | $1.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Danila Yurov: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14MINBOS-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (15.81 vs 2.44 bp); relationships: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV14MINBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN offense suppressed (<= 2 goals)
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV14MINBOS-BOS5|yes; why: higher confidence-adjusted growth (13.61 vs 2.80 bp); despite a smaller raw edge (+0.030 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.802 vs 0.518); relationships: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV14MINBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: MIN wins (incl. OT/SO)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes has the higher standalone adjusted growth (15.81 vs 11.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV14MINBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: MIN offense suppressed (<= 2 goals)
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14MINBOS-BOSCMITTELSTADT11-1|yes; why: higher confidence-adjusted growth (7.50 vs 3.82 bp); despite a smaller raw edge (+0.027 vs +0.028/contract); relationships: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.3733): highest fidelity KXNHLTOTAL-26NOV14MINBOS-9|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:WINS_BY_2PLUS (p 0.3199): highest fidelity KXNHLTEAMTOTAL-26NOV14MINBOS-BOS3|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4371): highest fidelity KXNHLTEAMTOTAL-26NOV14MINBOS-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV14MINBOS-BOS3|yes (same contract)
- KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4114, phi -0.224)
- KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:WINS (p 0.4542, phi -0.171)
- KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4114, phi -0.175)
- KXNHLGOAL-26NOV14MINBOS-BOSMKASTELIC47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3489, phi -0.157)

portfolios: A EV +1.56 (adj +0.44) on $11.17, P(profit) 0.447, adj growth 3.9 bp · B EV +2.57 (adj +1.66) on $7.57, P(profit) 0.4587, adj growth 15.8 bp · C EV +2.96 (adj +1.67) on $12.73, P(profit) 0.3779, adj growth 15.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ TOR  ·  10000 joint draws  ·  446 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_EDM_win | p_overtime | goals | shots TOR/EDM | TOR/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.42 | 0.58 | 0.00 | 6.08 | 28.3/28.6 | 24.5/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.119 | 0.43 | 0.57 | 0.00 | 9.55 | 30.0/30.5 | 23.7/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.49 | 6.01 | 28.5/28.9 | 25.6/25.2 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.091 | 0.38 | 0.62 | 0.00 | 6.07 | 22.4/34.2 | 29.9/19.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.082 | 0.38 | 0.62 | 0.00 | 9.44 | 24.4/36.2 | 28.7/19.3 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.44 | 0.56 | 0.46 | 5.91 | 22.9/34.7 | 31.0/19.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.166 | 0.149 | +0.049 | +0.032 | $2.71 | FUNDED_RESEARCH | $1 | TOR:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 10 | 0.143 | 0.130 | +0.036 | +0.023 | $2.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 31 | 0.403 | 0.354 | +0.078 | +0.029 | $3.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.65) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ assists YES | 27 | 0.347 | 0.306 | +0.063 | +0.022 | $2.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14EDMTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (21.67 vs 3.54 bp); relationships: KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: TOR offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (12.07 vs 5.25 bp); despite a smaller raw edge (+0.036 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (8.44 vs 4.94 bp); despite a smaller raw edge (+0.078 vs +0.102/contract); relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.089); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (5.25 vs 2.59 bp); relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.089); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:OFFENSE_4PLUS (p 0.408): highest fidelity KXNHLAST-26NOV14EDMTOR-TORECOWAN53-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3045): highest fidelity KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.488): highest fidelity KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes (same contract)
- KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3755, phi -0.213)
- KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3045, phi -0.149)
- KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 35% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.488, phi -0.313)
- KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3045, phi -0.238)

portfolios: A EV +2.01 (adj +0.65) on $11.17, P(profit) 0.6072, adj growth 6.3 bp · B EV +3.27 (adj +1.72) on $10.95, P(profit) 0.3763, adj growth 16.4 bp · C EV +4.11 (adj +1.90) on $18.87, P(profit) 0.5803, adj growth 17.9 bp · R EV +0.42 (adj +0.28) on $1.00, P(profit) 0.1657, adj growth 10.3 bp

## COL @ MTL  ·  10000 joint draws  ·  376 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_COL_win | p_overtime | goals | shots MTL/COL | MTL/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.46 | 0.54 | 0.00 | 6.07 | 28.0/28.7 | 24.9/24.4 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.114 | 0.39 | 0.61 | 0.00 | 6.05 | 22.2/34.0 | 29.7/19.2 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.45 | 0.55 | 0.49 | 5.95 | 22.5/34.4 | 31.0/19.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.51 | 0.49 | 0.47 | 5.97 | 28.0/28.6 | 25.3/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.49 | 0.51 | 0.00 | 9.44 | 29.2/30.0 | 23.8/22.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.094 | 0.41 | 0.59 | 0.00 | 9.42 | 23.7/35.8 | 28.6/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Artturi Lehkonen: 1+ goals YES | 32 | 0.386 | 0.369 | +0.051 | +0.033 | $3.98 | FUNDED_RESEARCH | $1 | COL:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Martin Necas: 1+ goals YES | 32 | 0.385 | 0.368 | +0.050 | +0.032 | $3.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_STRONGER | D |
| Logan O'Connor: 1+ goals YES | 9 | 0.120 | 0.110 | +0.025 | +0.014 | $1.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Oliver Kapanen: 1+ goals YES | 15 | 0.183 | 0.173 | +0.024 | +0.015 | $1.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes; why: higher confidence-adjusted growth (10.83 vs 10.26 bp); relationships: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV14COLMTL-COLLOCONNOR25-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV14COLMTL-MTLOKAPANEN91-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: COL offense suppressed (<= 2 goals)
- **Martin Necas: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (10.83 vs 10.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV14COLMTL-COLLOCONNOR25-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV14COLMTL-MTLOKAPANEN91-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: COL offense suppressed (<= 2 goals)
- **Logan O'Connor: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (10.83 vs 5.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV14COLMTL-MTLOKAPANEN91-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: COL offense suppressed (<= 2 goals)
- **Oliver Kapanen: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-MTLPDANAULT24-1|yes; why: higher confidence-adjusted growth (3.41 vs 1.62 bp); alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV14COLMTL-COLLOCONNOR25-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4486): highest fidelity KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:OFFENSE_4PLUS (p 0.4021): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3361, phi -0.268)
- KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 45% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3361, phi -0.308)
- KXNHLGOAL-26NOV14COLMTL-COLLOCONNOR25-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3361, phi -0.154)
- KXNHLGOAL-26NOV14COLMTL-MTLOKAPANEN91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3853, phi -0.189)

portfolios: A EV +1.61 (adj +1.01) on $11.17, P(profit) 0.6444, adj growth 9.6 bp · B EV +1.70 (adj +1.08) on $10.46, P(profit) 0.6682, adj growth 10.3 bp · C EV +0.81 (adj +0.52) on $5.28, P(profit) 0.3864, adj growth 5.0 bp · R EV +0.15 (adj +0.10) on $1.00, P(profit) 0.3864, adj growth 3.8 bp

## DET @ TBL  ·  10000 joint draws  ·  364 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_DET_win | p_overtime | goals | shots TBL/DET | TBL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.134 | 0.71 | 0.29 | 0.00 | 6.04 | 27.5/27.2 | 24.5/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.49 | 5.9 | 27.5/27.2 | 24.0/24.2 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.103 | 0.78 | 0.22 | 0.00 | 6.01 | 32.0/21.2 | 19.1/27.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.73 | 0.27 | 0.00 | 9.26 | 28.9/28.5 | 23.8/20.9 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.55 | 0.45 | 0.50 | 5.95 | 32.6/21.6 | 18.4/29.3 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.065 | 0.80 | 0.20 | 0.00 | 9.32 | 34.0/22.6 | 18.4/25.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Conor Geekie: 1+ goals NO | 82 | 0.873 | 0.858 | +0.043 | +0.028 | $5.81 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Jake Guentzel: 1+ goals YES | 38 | 0.445 | 0.427 | +0.048 | +0.031 | $4.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | DIRECT (0.58) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ assists NO | 37 | 0.463 | 0.414 | +0.077 | +0.028 | $4.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
| Alex DeBrincat: 1+ goals YES | 31 | 0.346 | 0.336 | +0.021 | +0.011 | $1.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_STRONGER | D |
- **Conor Geekie: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (12.39 vs 7.10 bp); despite a smaller raw edge (+0.042 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV14DETTB-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: TBL offense succeeds (4+ goals)
- **Jake Guentzel: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-2|yes; why: higher confidence-adjusted growth (8.55 vs 2.53 bp); wins across more scripts (relative breadth 0.904 vs 0.729); relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: INTENTIONAL_DIVERSIFIER (phi -0.282); KXNHLGOAL-26NOV14DETTB-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: TBL offense suppressed (<= 2 goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no; why: higher confidence-adjusted growth (7.10 vs 0.75 bp); alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.282); KXNHLGOAL-26NOV14DETTB-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: TBL offense succeeds (4+ goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV14DETTB-7|yes; why: higher confidence-adjusted growth (1.19 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.946 vs 0.689); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.5014): highest fidelity KXNHLAST-26NOV14DETTB-TBCDASTOUS51-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.2927): highest fidelity KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.2873): highest fidelity KXNHLGOAL-26NOV14DETTB-DETADEBRINCAT93-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14DETTB-DETADEBRINCAT93-1|yes (same contract)
- KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5014, phi -0.145)
- KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 42% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.2927, phi -0.268)
- KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5014, phi -0.307)
- KXNHLGOAL-26NOV14DETTB-DETADEBRINCAT93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.5025, phi -0.3)

portfolios: A EV +1.38 (adj +0.59) on $11.17, P(profit) 0.4282, adj growth 5.8 bp · B EV +1.76 (adj +0.90) on $15.87, P(profit) 0.6945, adj growth 8.7 bp · C EV +2.31 (adj +1.10) on $15.64, P(profit) 0.7717, adj growth 10.4 bp · R EV +0.10 (adj +0.07) on $2.00, P(profit) 0.8728, adj growth 2.6 bp

## OTT @ PIT  ·  10000 joint draws  ·  422 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_OTT_win | p_overtime | goals | shots PIT/OTT | PIT/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.49 | 0.51 | 0.00 | 6.02 | 26.9/26.9 | 23.3/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.48 | 5.93 | 26.9/26.8 | 23.4/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.49 | 0.51 | 0.00 | 9.25 | 28.7/28.7 | 22.6/22.6 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.071 | 0.52 | 0.48 | 0.00 | 6.03 | 31.8/21.6 | 18.3/28.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.065 | 0.42 | 0.58 | 0.00 | 6.06 | 21.5/31.6 | 27.5/18.4 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.50 | 0.50 | 0.50 | 5.93 | 31.7/21.6 | 18.4/28.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Fabian Zetterlund: 1+ goals YES | 18 | 0.224 | 0.210 | +0.033 | +0.020 | $1.98 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 12 | 0.152 | 0.142 | +0.025 | +0.014 | $1.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Justin Brazeau: 1+ goals YES | 13 | 0.160 | 0.151 | +0.022 | +0.013 | $1.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Fabian Zetterlund: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14OTTPIT-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (5.59 vs 1.01 bp); alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV14OTTPIT-PITJBRAZEAU16-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: OTT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14OTTPIT-OTT3|no; why: higher confidence-adjusted growth (3.91 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0002 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14OTTPIT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV14OTTPIT-PITJBRAZEAU16-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: PIT offense suppressed (<= 2 goals)
- **Justin Brazeau: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (3.91 vs 3.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26NOV14OTTPIT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis PIT:OFFENSE_4PLUS (p 0.3812): highest fidelity KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:WINS_BY_2PLUS (p 0.2736): highest fidelity KXNHLGOAL-26NOV14OTTPIT-PITBLIZOTTE46-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14OTTPIT-PITBLIZOTTE46-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3918): highest fidelity KXNHLAST-26NOV14OTTPIT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14OTTPIT-OTTJSANDERSON85-1|no (same contract)
- KXNHLGOAL-26NOV14OTTPIT-OTTFZETTERLUND20-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3918, phi -0.203)
- KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4032, phi -0.192)
- KXNHLGOAL-26NOV14OTTPIT-PITJBRAZEAU16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4032, phi -0.185)

portfolios: A EV +1.61 (adj +0.76) on $9.76, P(profit) 0.4026, adj growth 7.1 bp · B EV +0.78 (adj +0.46) on $4.42, P(profit) 0.449, adj growth 4.4 bp · C EV +0.75 (adj +0.34) on $5.46, P(profit) 0.2579, adj growth 3.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ WSH  ·  10000 joint draws  ·  436 bet sides mapped, 8 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NJD_win | p_overtime | goals | shots WSH/NJD | WSH/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.51 | 0.49 | 0.00 | 6.03 | 27.5/28.0 | 24.5/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.47 | 5.98 | 27.9/28.3 | 25.1/24.7 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.101 | 0.44 | 0.56 | 0.00 | 5.96 | 22.1/33.4 | 29.6/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.52 | 0.48 | 0.00 | 9.36 | 29.2/29.8 | 23.6/22.8 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.47 | 0.53 | 0.48 | 5.97 | 22.0/33.5 | 30.1/18.8 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.068 | 0.39 | 0.61 | 0.00 | 9.35 | 23.5/35.0 | 27.9/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cody Glass: 1+ goals YES | 10 | 0.151 | 0.132 | +0.045 | +0.026 | $2.06 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 19 | 0.230 | 0.219 | +0.029 | +0.018 | $1.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 15 | 0.188 | 0.174 | +0.029 | +0.015 | $1.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-NJLEVANGELISTA77-1|yes; why: higher confidence-adjusted growth (15.01 vs 0.98 bp); alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV14NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: NJD offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes; why: KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes has the higher standalone adjusted growth (5.87 vs 4.44 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.126); relationships: KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV14NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes; why: Player prop expression KXNHLGOAL-26NOV14NJWSH-WSHBJENNER38-1|yes selected over player prop KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.28 vs 0.47 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4072): highest fidelity KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes (same contract)
- thesis WSH:SUPPRESSED (p 0.3824): highest fidelity KXNHLAST-26NOV14NJWSH-WSHJKYROU25-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14NJWSH-WSHJKYROU25-1|no (same contract)
- thesis NJD:SUPPRESSED (p 0.3763): highest fidelity KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no (same contract)
- KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3763, phi -0.178)
- KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3824, phi -0.222)
- KXNHLGOAL-26NOV14NJWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3824, phi -0.189)
- override: Player prop expression KXNHLGOAL-26NOV14NJWSH-WSHBJENNER38-1|yes selected over player prop KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.28 vs 0.47 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.53 (adj +1.11) on $11.17, P(profit) 0.4827, adj growth 10.5 bp · B EV +1.37 (adj +0.78) on $5.15, P(profit) 0.4703, adj growth 7.5 bp · C EV +1.40 (adj +0.49) on $13.03, P(profit) 0.6405, adj growth 4.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PHI @ CBJ  ·  10000 joint draws  ·  396 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_PHI_win | p_overtime | goals | shots CBJ/PHI | CBJ/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 5.96 | 26.4/26.1 | 22.9/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.50 | 0.50 | 0.44 | 5.82 | 26.6/26.2 | 23.1/23.4 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.095 | 0.63 | 0.37 | 0.00 | 5.95 | 31.6/20.9 | 18.1/27.4 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.56 | 0.44 | 0.47 | 5.84 | 31.8/21.0 | 17.9/28.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.069 | 0.60 | 0.40 | 0.00 | 3.46 | 25.6/25.3 | 23.7/23.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.49 | 0.51 | 0.49 | 2.8 | 25.1/24.9 | 23.5/23.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Christian Dvorak: 1+ goals YES | 15 | 0.199 | 0.184 | +0.040 | +0.025 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Kent Johnson: 1+ goals NO | 72 | 0.770 | 0.757 | +0.036 | +0.022 | $6.58 | FUNDED_RESEARCH | $2 | CBJ:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Matvei Michkov: 1+ goals NO | 73 | 0.775 | 0.763 | +0.032 | +0.019 | $6.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 17 | 0.204 | 0.193 | +0.025 | +0.013 | $1.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV14PHICBJ-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (10.40 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14PHICBJ-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: PHI offense suppressed (<= 2 goals)
- **Kent Johnson: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26NOV14PHICBJ-6|no; why: higher confidence-adjusted growth (5.72 vs 0.15 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.997 vs 0.763); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: CBJ offense succeeds (4+ goals)
- **Matvei Michkov: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no; why: Player prop expression KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no selected over player prop KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no because adjusted EV is 0.3 pts higher while thesis capture is 0.88 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14PHICBJ-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: PHI offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLPTS-26NOV14PHICBJ-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (2.68 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.066/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14PHICBJ-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:OFFENSE_4PLUS (p 0.2883): highest fidelity KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.4217): highest fidelity KXNHLGOAL-26NOV14PHICBJ-CBJKJOHNSON91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14PHICBJ-CBJKJOHNSON91-1|no (same contract)
- thesis PHI:SUPPRESSED (p 0.4995): highest fidelity KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no (same contract)
- KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4995, phi -0.232)
- KXNHLGOAL-26NOV14PHICBJ-CBJKJOHNSON91-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3562, phi -0.212)
- KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.2883, phi -0.211)
- KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4217, phi -0.236)
- override: Player prop expression KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no selected over player prop KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no because adjusted EV is 0.3 pts higher while thesis capture is 0.88 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.03 (adj +0.54) on $11.17, P(profit) 0.5787, adj growth 5.3 bp · B EV +1.34 (adj +0.82) on $16.45, P(profit) 0.6662, adj growth 7.9 bp · C EV +1.76 (adj +1.08) on $21.57, P(profit) 0.6662, adj growth 10.2 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7705, adj growth 2.3 bp

## FLA @ STL  ·  10000 joint draws  ·  422 bet sides mapped, 7 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_FLA_win | p_overtime | goals | shots STL/FLA | STL/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 6.06 | 27.2/27.6 | 24.4/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.47 | 5.89 | 27.4/27.7 | 24.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.59 | 0.41 | 0.00 | 9.35 | 29.0/29.1 | 23.5/22.2 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.080 | 0.50 | 0.50 | 0.00 | 6.02 | 21.9/32.5 | 28.8/18.5 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.47 | 0.53 | 0.44 | 5.93 | 21.9/32.3 | 29.0/18.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.055 | 0.56 | 0.44 | 0.00 | 3.48 | 26.1/26.1 | 24.3/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pius Suter: 1+ goals YES | 12 | 0.169 | 0.153 | +0.042 | +0.026 | $2.16 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 25 | 0.294 | 0.282 | +0.031 | +0.019 | $1.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 30 | 0.345 | 0.331 | +0.030 | +0.016 | $1.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (12.80 vs 3.86 bp); relationships: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (3.86 vs 2.72 bp); relationships: KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (3.86 vs 2.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.4299): highest fidelity KXNHLTEAMTOTAL-26NOV14FLASTL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:OFFENSE_4PLUS (p 0.362): highest fidelity KXNHLTOTAL-26NOV14FLASTL-9|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2809): highest fidelity KXNHLTEAMTOTAL-26NOV14FLASTL-STL3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV14FLASTL-STL3|yes (same contract)
- KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.18)
- KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.249)
- KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.271)

portfolios: A EV +1.89 (adj +0.89) on $11.17, P(profit) 0.4556, adj growth 8.2 bp · B EV +1.12 (adj +0.67) on $6.02, P(profit) 0.6147, adj growth 6.4 bp · C EV +0.46 (adj +0.27) on $4.23, P(profit) 0.4843, adj growth 2.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ DAL  ·  10000 joint draws  ·  414 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_BUF_win | p_overtime | goals | shots DAL/BUF | DAL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.59 | 0.41 | 0.00 | 6.01 | 26.6/26.5 | 23.3/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.47 | 5.94 | 26.7/26.6 | 23.3/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 9.23 | 28.1/28.1 | 22.9/21.7 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.079 | 0.66 | 0.34 | 0.00 | 6.0 | 31.1/20.7 | 17.9/26.6 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.51 | 0.49 | 0.47 | 5.95 | 31.3/21.0 | 17.8/28.0 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.061 | 0.54 | 0.46 | 0.00 | 6.0 | 21.4/31.3 | 27.6/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Arttu Hyry: 1+ goals YES | 15 | 0.199 | 0.185 | +0.040 | +0.026 | $2.42 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Jiri Kulich: 1+ goals YES | 13 | 0.164 | 0.154 | +0.026 | +0.017 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Roope Hintz: 1+ goals YES | 28 | 0.318 | 0.307 | +0.024 | +0.013 | $1.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes; why: higher confidence-adjusted growth (11.12 vs 1.90 bp); relationships: KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: DAL offense suppressed (<= 2 goals)
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14BUFDAL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (4.94 vs 0.14 bp); alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: BUF offense suppressed (<= 2 goals)
- **Roope Hintz: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes has the higher standalone adjusted growth (11.12 vs 1.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis DAL:OFFENSE_4PLUS (p 0.424): highest fidelity KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.3335): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3642, phi -0.226)
- KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.4516, phi -0.204)
- KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3642, phi -0.253)

portfolios: A EV +1.14 (adj +0.73) on $6.26, P(profit) 0.5466, adj growth 6.9 bp · B EV +1.02 (adj +0.65) on $5.48, P(profit) 0.3322, adj growth 6.2 bp · C EV +0.79 (adj +0.52) on $3.16, P(profit) 0.1986, adj growth 4.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ UTA  ·  10000 joint draws  ·  398 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_SJS_win | p_overtime | goals | shots UTA/SJS | UTA/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.65 | 0.35 | 0.00 | 6.05 | 28.0/27.5 | 24.7/23.8 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.113 | 0.69 | 0.31 | 0.00 | 6.06 | 33.2/22.0 | 19.3/28.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.52 | 0.48 | 0.47 | 5.89 | 28.1/27.6 | 24.4/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.70 | 0.30 | 0.00 | 9.43 | 29.6/29.1 | 24.0/22.2 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.57 | 0.43 | 0.45 | 5.92 | 33.2/22.1 | 19.0/29.9 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.079 | 0.72 | 0.28 | 0.00 | 9.34 | 35.6/23.5 | 19.0/27.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Daniil But: 1+ goals NO | 79 | 0.856 | 0.838 | +0.054 | +0.036 | $6.58 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 67 | 0.751 | 0.703 | +0.066 | +0.018 | $5.01 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Clayton Keller: 1+ assists NO | 40 | 0.472 | 0.431 | +0.055 | +0.014 | $1.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
- **Daniil But: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no; why: higher confidence-adjusted growth (18.62 vs 1.84 bp); despite a smaller raw edge (+0.054 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: MOSTLY_INDEPENDENT (phi 0.062); failure: UTA offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV14SJUTA-SJMCELEBRINI71-2|no; why: higher confidence-adjusted growth (3.15 vs 0.14 bp); despite a smaller raw edge (+0.066 vs +0.078/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: SJS offense succeeds (4+ goals)
- **Clayton Keller: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV14SJUTA-UTACKELLER9-2|no; why: higher confidence-adjusted growth (1.84 vs 0.29 bp); despite a smaller raw edge (+0.055 vs +0.089/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, UTA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis SJS:SUPPRESSED (p 0.4652): highest fidelity KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no (same contract)
- thesis UTA:SUPPRESSED (p 0.3243): highest fidelity KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no (same contract)
- KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.164)
- KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3148, phi -0.233)
- KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.325)

portfolios: A EV +1.10 (adj +0.39) on $11.17, P(profit) 0.4571, adj growth 3.8 bp · B EV +1.17 (adj +0.49) on $13.41, P(profit) 0.6451, adj growth 4.8 bp · C EV +0.98 (adj +0.26) on $9.27, P(profit) 0.7511, adj growth 2.5 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.8558, adj growth 3.6 bp

## NYI @ ANA  ·  10000 joint draws  ·  440 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_NYI_win | p_overtime | goals | shots ANA/NYI | ANA/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.63 | 0.37 | 0.00 | 6.08 | 27.7/27.4 | 24.5/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.121 | 0.60 | 0.40 | 0.00 | 9.48 | 29.3/29.0 | 23.3/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.50 | 0.50 | 0.46 | 5.99 | 27.7/27.5 | 24.1/24.4 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.097 | 0.66 | 0.34 | 0.00 | 6.08 | 33.2/22.0 | 19.2/28.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.085 | 0.69 | 0.31 | 0.00 | 9.37 | 34.8/23.3 | 18.5/26.9 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.54 | 0.46 | 0.47 | 6.01 | 33.2/22.1 | 18.9/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pavel Mintyukov: 1+ goals YES | 6 | 0.098 | 0.088 | +0.035 | +0.024 | $1.85 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 10 | 0.149 | 0.133 | +0.043 | +0.027 | $2.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Troy Terry: 1+ assists NO | 67 | 0.839 | 0.716 | +0.154 | +0.031 | $6.58 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Sam Colangelo: 1+ goals YES | 12 | 0.156 | 0.144 | +0.029 | +0.017 | $1.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Pavel Mintyukov: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14NYIANA-ANA2|yes; why: higher confidence-adjusted growth (19.57 vs 3.17 bp); despite a smaller raw edge (+0.034 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.857 vs 0.503); relationships: KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLAST-26NOV14NYIANA-ANATTERRY19-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14NYIANA-ANA2|yes; why: higher confidence-adjusted growth (16.09 vs 3.17 bp); despite a smaller raw edge (+0.043 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.866 vs 0.503); relationships: KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLAST-26NOV14NYIANA-ANATTERRY19-1|no: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.031); failure: ANA offense suppressed (<= 2 goals)
- **Troy Terry: 1+ assists NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV14NYIANA-ANACGAUTHIER61-1|no; why: higher confidence-adjusted growth (9.63 vs 0.01 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.032); failure: ANA offense succeeds (4+ goals)
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14NYIANA-ANA2|yes; why: higher confidence-adjusted growth (5.68 vs 3.17 bp); despite a smaller raw edge (+0.029 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.503); relationships: KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLAST-26NOV14NYIANA-ANATTERRY19-1|no: MOSTLY_INDEPENDENT (phi -0.032); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.5141): highest fidelity KXNHLTEAMTOTAL-26NOV14NYIANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14NYIANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3698): highest fidelity KXNHLSPREAD-26NOV14NYIANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14NYIANA-ANA2|yes (same contract)
- thesis NYI:SUPPRESSED (p 0.3931): highest fidelity KXNHLAST-26NOV14NYIANA-NYIMMACCELLI63-1|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV14NYIANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2867, phi -0.126)
- KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2867, phi -0.136)
- KXNHLAST-26NOV14NYIANA-ANATTERRY19-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.9 pts; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.5141, phi -0.166)
- KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2867, phi -0.138)

portfolios: A EV +1.64 (adj +0.42) on $11.17, P(profit) 0.4818, adj growth 4.0 bp · B EV +3.75 (adj +1.77) on $12.30, P(profit) 0.358, adj growth 16.9 bp · C EV +0.46 (adj +0.15) on $2.63, P(profit) 0.3698, adj growth 1.4 bp · R EV +0.54 (adj +0.37) on $1.00, P(profit) 0.0984, adj growth 13.1 bp

## CGY @ LAK  ·  10000 joint draws  ·  410 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_CGY_win | p_overtime | goals | shots LAK/CGY | LAK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.63 | 0.37 | 0.00 | 6.0 | 28.4/28.0 | 25.1/24.3 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.107 | 0.67 | 0.33 | 0.00 | 5.99 | 33.9/22.1 | 19.5/29.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.48 | 5.86 | 28.5/28.2 | 24.8/25.1 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.57 | 0.43 | 0.43 | 5.87 | 34.1/22.5 | 19.5/30.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.61 | 0.39 | 0.00 | 9.31 | 30.0/29.6 | 24.4/23.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.60 | 0.40 | 0.00 | 3.49 | 27.4/26.8 | 25.2/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 4 | 0.078 | 0.068 | +0.035 | +0.025 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Kevin Fiala: 1+ assists NO | 61 | 0.819 | 0.677 | +0.192 | +0.050 | $3.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Mats Zuccarello: 1+ assists NO | 68 | 0.813 | 0.720 | +0.118 | +0.025 | $3.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ goals NO | 65 | 0.701 | 0.686 | +0.035 | +0.020 | $2.35 | FUNDED_RESEARCH | $1 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLPTS-26NOV14CGYLA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (32.68 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV14CGYLA-LAKFIALA22-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: LAK offense suppressed (<= 2 goals)
- **Kevin Fiala: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no; why: higher confidence-adjusted growth (23.56 vs 6.47 bp); relationships: KXNHLGOAL-26NOV14CGYLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.057); KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.078); failure: LAK offense succeeds (4+ goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (6.47 vs 4.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV14CGYLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26NOV14CGYLA-LAKFIALA22-1|no: MOSTLY_INDEPENDENT (phi 0.057); KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.035); failure: LAK offense succeeds (4+ goals)
- **Artemi Panarin: 1+ goals NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no; why: second expression of the same thesis: KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no has the higher standalone adjusted growth (6.47 vs 4.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.035); they share one thesis budget; relationships: KXNHLGOAL-26NOV14CGYLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26NOV14CGYLA-LAKFIALA22-1|no: MOSTLY_INDEPENDENT (phi 0.078); KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.035); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis LAK:SUPPRESSED (p 0.3629): highest fidelity KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no (same contract)
- thesis LAK:WINS_BY_2PLUS (p 0.3611): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14CGYLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3629, phi -0.137)
- KXNHLAST-26NOV14CGYLA-LAKFIALA22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.9 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4201, phi -0.191)
- KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4201, phi -0.202)
- KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4201, phi -0.228)

portfolios: A EV +2.92 (adj +1.35) on $11.17, P(profit) 0.5334, adj growth 13.0 bp · B EV +3.14 (adj +1.40) on $11.36, P(profit) 0.7033, adj growth 13.5 bp · C EV +1.47 (adj +0.31) on $8.63, P(profit) 0.8134, adj growth 3.0 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.7014, adj growth 1.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
