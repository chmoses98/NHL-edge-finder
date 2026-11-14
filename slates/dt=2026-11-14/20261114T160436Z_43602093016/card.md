# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-14T16:04:36Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +26.40 | +9.46 | +25.62 | 0.793 | -14.18 | -24.83 | 89.50 |
| B thesis-diversified (joint) ← optimiser card | 148.34 | +27.68 | +13.39 | +26.50 | 0.795 | -13.51 | -24.35 | 128.20 |
| C best expression per thesis | 148.32 | +28.59 | +13.69 | +25.41 | 0.738 | -22.46 | -34.72 | 127.97 |
| R FUNDED research stakes | 19.00 | +3.19 | +1.48 | +2.86 | 0.697 | -5.33 | -7.03 | 0.00 |

## SEA @ CAR  ·  10000 joint draws  ·  428 bet sides mapped, 45 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_SEA_win | p_overtime | goals | shots CAR/SEA | CAR/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.187 | 0.65 | 0.35 | 0.00 | 6.04 | 34.4/20.7 | 17.9/30.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.160 | 0.54 | 0.46 | 0.47 | 5.96 | 34.9/21.1 | 17.9/31.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.154 | 0.64 | 0.36 | 0.00 | 9.35 | 36.6/22.4 | 17.4/28.9 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.070 | 0.62 | 0.38 | 0.00 | 3.5 | 33.0/19.4 | 17.8/30.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.067 | 0.59 | 0.41 | 0.00 | 6.01 | 27.7/26.3 | 23.2/23.7 | even strength |
| CAR shot control · high event (8+) · tight (1-goal/OT) | 0.066 | 0.52 | 0.48 | 0.59 | 9.58 | 37.0/22.6 | 16.8/30.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 42 | 0.637 | 0.493 | +0.200 | +0.056 | $4.40 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 55 | 0.753 | 0.618 | +0.185 | +0.050 | $5.42 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikolaj Ehlers: 1+ goals NO | 71 | 0.782 | 0.763 | +0.058 | +0.039 | $6.35 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Carolina wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes has the higher standalone adjusted growth (55.23 vs 27.34 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.299); relationships: KXNHLSPREAD-26NOV14SEACAR-CAR3|no: DUPLICATIVE (phi 0.759); KXNHLGOAL-26NOV14SEACAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.131); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes has the higher standalone adjusted growth (55.23 vs 22.66 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.227); relationships: KXNHLSPREAD-26NOV14SEACAR-CAR2|no: DUPLICATIVE (phi 0.759); KXNHLGOAL-26NOV14SEACAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.123); failure: CAR wins by 2+
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes has the higher standalone adjusted growth (55.23 vs 16.53 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.096); relationships: KXNHLSPREAD-26NOV14SEACAR-CAR2|no: MOSTLY_INDEPENDENT (phi 0.131); KXNHLSPREAD-26NOV14SEACAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.123); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.19, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.16, CAR shot control · high event (8+) · decided (2+) 0.15.
- thesis SEA:OFFENSE_4PLUS (p 0.3656): highest fidelity KXNHLTEAMTOTAL-26NOV14SEACAR-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2217): highest fidelity KXNHLSPREAD-26NOV14SEACAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no (same contract)
- thesis SEA:WINS (p 0.4187): highest fidelity KXNHLSPREAD-26NOV14SEACAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no (same contract)
- KXNHLSPREAD-26NOV14SEACAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 22.2 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3633, phi -1.0)
- KXNHLSPREAD-26NOV14SEACAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 20.8 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3633, phi -0.759)
- KXNHLGOAL-26NOV14SEACAR-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4853, phi -0.193)

portfolios: A EV +5.73 (adj +1.30) on $11.38, P(profit) 0.6367, adj growth 12.2 bp · B EV +4.29 (adj +1.38) on $16.17, P(profit) 0.7234, adj growth 13.3 bp · C EV +7.16 (adj +4.22) on $8.49, P(profit) 0.3072, adj growth 39.0 bp · R EV +1.73 (adj +0.54) on $6.00, P(profit) 0.7234, adj growth 20.3 bp
equivalent contracts collapsed: KXNHLGAME-26NOV14SEACAR-CAR|no == KXNHLGAME-26NOV14SEACAR-SEA|yes

## WPG @ CHI  ·  10000 joint draws  ·  424 bet sides mapped, 8 +EV candidates, 4 on card


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
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.263 | 0.249 | +0.042 | +0.027 | $2.95 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Mario Ferraro: 1+ goals YES | 5 | 0.074 | 0.067 | +0.021 | +0.013 | $1.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:WINS_BY_2PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 60 | 0.733 | 0.640 | +0.117 | +0.023 | $6.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Oliver Moore: 1+ goals YES | 12 | 0.150 | 0.141 | +0.023 | +0.014 | $1.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14WPGCHI-WPG2|no; why: higher confidence-adjusted growth (9.12 vs 2.04 bp); despite a smaller raw edge (+0.042 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14WPGCHI-WPGMFERRARO38-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLGOAL-26NOV14WPGCHI-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CHI offense suppressed (<= 2 goals)
- **Mario Ferraro: 1+ goals YES** — thesis: WPG wins by 2+; alternative: KXNHLAST-26NOV14WPGCHI-WPGCPERFETTI91-1|yes; why: higher confidence-adjusted growth (7.51 vs 0.10 bp); despite a smaller raw edge (+0.021 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0033 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14WPGCHI-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense suppressed (<= 2 goals)
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

portfolios: A EV +1.47 (adj +0.32) on $11.38, P(profit) 0.7574, adj growth 3.1 bp · B EV +2.45 (adj +1.03) on $11.97, P(profit) 0.3844, adj growth 9.8 bp · C EV +3.68 (adj +1.08) on $21.79, P(profit) 0.6341, adj growth 10.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ BOS  ·  10000 joint draws  ·  388 bet sides mapped, 16 +EV candidates, 4 on card


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
| Danila Yurov: 1+ goals YES | 16 | 0.217 | 0.202 | +0.048 | +0.032 | $2.94 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| William Borgen: 1+ goals YES | 5 | 0.084 | 0.071 | +0.030 | +0.018 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:WINS_BY_2PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.140 | 0.129 | +0.034 | +0.022 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Mark Kastelic: 1+ goals YES | 9 | 0.122 | 0.113 | +0.027 | +0.017 | $1.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Danila Yurov: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14MINBOS-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (15.81 vs 2.44 bp); relationships: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV14MINBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN offense suppressed (<= 2 goals)
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV14MINBOS-BOS5|yes; why: higher confidence-adjusted growth (13.61 vs 2.80 bp); despite a smaller raw edge (+0.030 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.802 vs 0.518); relationships: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV14MINBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: MIN wins (incl. OT/SO)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes has the higher standalone adjusted growth (15.81 vs 11.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV14MINBOS-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: MIN offense suppressed (<= 2 goals)
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14MINBOS-BOSFMINTEN93-1|yes; why: higher confidence-adjusted growth (7.50 vs 4.60 bp); despite a smaller raw edge (+0.027 vs +0.030/contract); relationships: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.3733): highest fidelity KXNHLTOTAL-26NOV14MINBOS-9|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:WINS_BY_2PLUS (p 0.3199): highest fidelity KXNHLTEAMTOTAL-26NOV14MINBOS-BOS3|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4371): highest fidelity KXNHLTEAMTOTAL-26NOV14MINBOS-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14MINBOS-BOSFMINTEN93-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4114, phi -0.224)
- KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:WINS (p 0.4542, phi -0.171)
- KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4114, phi -0.175)
- KXNHLGOAL-26NOV14MINBOS-BOSMKASTELIC47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3489, phi -0.157)

portfolios: A EV +2.00 (adj +0.82) on $11.38, P(profit) 0.5736, adj growth 7.5 bp · B EV +2.55 (adj +1.65) on $7.53, P(profit) 0.4587, adj growth 15.7 bp · C EV +2.54 (adj +1.61) on $8.16, P(profit) 0.4354, adj growth 15.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ TOR  ·  10000 joint draws  ·  444 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_EDM_win | p_overtime | goals | shots TOR/EDM | TOR/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.42 | 0.58 | 0.00 | 6.08 | 28.5/28.9 | 24.8/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.116 | 0.42 | 0.58 | 0.00 | 9.45 | 29.9/30.3 | 23.5/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.50 | 0.50 | 0.47 | 6.0 | 28.5/28.9 | 25.5/25.1 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.088 | 0.39 | 0.61 | 0.00 | 6.13 | 22.4/33.9 | 29.5/19.4 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.086 | 0.33 | 0.67 | 0.00 | 9.4 | 24.4/36.2 | 28.0/19.5 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.44 | 0.56 | 0.45 | 6.04 | 23.1/34.7 | 31.3/19.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.163 | 0.147 | +0.046 | +0.030 | $2.54 | FUNDED_RESEARCH | $1 | TOR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 10 | 0.137 | 0.125 | +0.031 | +0.019 | $1.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ assists YES | 27 | 0.347 | 0.303 | +0.063 | +0.020 | $2.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| John Tavares: 1+ assists NO | 64 | 0.720 | 0.675 | +0.064 | +0.019 | $5.03 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14EDMTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (18.99 vs 3.16 bp); relationships: KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no: MOSTLY_INDEPENDENT (phi -0.024); failure: TOR offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (8.25 vs 4.12 bp); despite a smaller raw edge (+0.031 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (4.12 vs 0.87 bp); alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: EDM offense suppressed (<= 2 goals)
- **John Tavares: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14EDMTOR-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (3.52 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:OFFENSE_4PLUS (p 0.4039): highest fidelity KXNHLAST-26NOV14EDMTOR-TORECOWAN53-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.4905): highest fidelity KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.3716): highest fidelity KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no (same contract)
- KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3716, phi -0.201)
- KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3044, phi -0.149)
- KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3044, phi -0.251)
- KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4039, phi -0.222)

portfolios: A EV +2.00 (adj +0.45) on $11.38, P(profit) 0.6072, adj growth 4.3 bp · B EV +2.40 (adj +1.23) on $11.17, P(profit) 0.4608, adj growth 11.7 bp · C EV +3.73 (adj +1.50) on $20.90, P(profit) 0.7495, adj growth 14.1 bp · R EV +0.39 (adj +0.26) on $1.00, P(profit) 0.1629, adj growth 9.6 bp

## COL @ MTL  ·  10000 joint draws  ·  378 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_COL_win | p_overtime | goals | shots MTL/COL | MTL/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.117 | 0.39 | 0.61 | 0.00 | 6.05 | 22.3/34.3 | 29.9/19.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.47 | 0.53 | 0.00 | 6.08 | 28.1/28.6 | 24.9/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.50 | 0.50 | 0.46 | 5.93 | 27.9/28.5 | 25.2/24.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.46 | 0.54 | 0.49 | 5.97 | 22.4/34.3 | 30.9/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.48 | 0.52 | 0.00 | 9.44 | 29.2/30.0 | 23.8/23.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.094 | 0.41 | 0.59 | 0.00 | 9.42 | 23.7/35.8 | 28.7/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Martin Necas: 1+ goals YES | 32 | 0.387 | 0.369 | +0.051 | +0.034 | $3.81 | FUNDED_RESEARCH | $1 | COL:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 32 | 0.387 | 0.367 | +0.051 | +0.032 | $3.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_STRONGER | D |
| Gabriel Landeskog: 1+ goals YES | 21 | 0.263 | 0.246 | +0.041 | +0.024 | $2.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Nick Suzuki: 1+ assists NO | 51 | 0.626 | 0.541 | +0.099 | +0.013 | $2.37 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Martin Necas: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (10.93 vs 10.18 bp); despite a smaller raw edge (+0.051 vs +0.051/contract); relationships: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV14COLMTL-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV14COLMTL-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: COL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes has the higher standalone adjusted growth (10.93 vs 10.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV14COLMTL-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26NOV14COLMTL-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: COL offense suppressed (<= 2 goals)
- **Gabriel Landeskog: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes has the higher standalone adjusted growth (10.93 vs 7.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26NOV14COLMTL-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: COL offense suppressed (<= 2 goals)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV14COLMTL-COL3|yes; why: higher confidence-adjusted growth (1.61 vs 1.05 bp); wins across more scripts (relative breadth 0.997 vs 0.434); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV14COLMTL-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: MTL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4486): highest fidelity KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3853): highest fidelity KXNHLAST-26NOV14COLMTL-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14COLMTL-MTLNSUZUKI14-1|no (same contract)
- KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 45% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3361, phi -0.296)
- KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3361, phi -0.268)
- KXNHLGOAL-26NOV14COLMTL-COLGLANDESKOG92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3361, phi -0.214)
- KXNHLAST-26NOV14COLMTL-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.1 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4021, phi -0.265)

portfolios: A EV +1.92 (adj +0.91) on $11.38, P(profit) 0.5497, adj growth 8.8 bp · B EV +2.03 (adj +1.05) on $12.19, P(profit) 0.5497, adj growth 10.1 bp · C EV +1.49 (adj +0.65) on $8.99, P(profit) 0.3866, adj growth 6.1 bp · R EV +0.15 (adj +0.10) on $1.00, P(profit) 0.3866, adj growth 3.8 bp

## DET @ TBL  ·  10000 joint draws  ·  364 bet sides mapped, 5 +EV candidates, 4 on card


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
| Conor Geekie: 1+ goals NO | 82 | 0.873 | 0.858 | +0.043 | +0.028 | $6.55 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Jake Guentzel: 1+ goals YES | 38 | 0.445 | 0.427 | +0.048 | +0.031 | $3.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | DIRECT (0.58) | EVIDENCE_STRONGER | D |
| Charle-Edouard D'Astous: 1+ assists YES | 40 | 0.468 | 0.429 | +0.051 | +0.012 | $1.03 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:OFFENSE_4PLUS | DIRECT (0.61) | EVIDENCE_MIXED | D |
| Alex DeBrincat: 1+ goals YES | 31 | 0.346 | 0.336 | +0.021 | +0.011 | $1.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_STRONGER | D |
- **Conor Geekie: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (12.39 vs 0.89 bp); despite a smaller raw edge (+0.042 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0098 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV14DETTB-TBCDASTOUS51-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.053); KXNHLGOAL-26NOV14DETTB-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: TBL offense succeeds (4+ goals)
- **Jake Guentzel: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-2|yes; why: higher confidence-adjusted growth (8.55 vs 2.53 bp); wins across more scripts (relative breadth 0.904 vs 0.729); relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV14DETTB-TBCDASTOUS51-1|yes: REINFORCING (phi 0.193); KXNHLGOAL-26NOV14DETTB-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: TBL offense suppressed (<= 2 goals)
- **Charle-Edouard D'Astous: 1+ assists YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes has the higher standalone adjusted growth (8.55 vs 1.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.193); they share one thesis budget; relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: INTENTIONAL_DIVERSIFIER (phi -0.053); KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: REINFORCING (phi 0.193); KXNHLGOAL-26NOV14DETTB-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: TBL offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV14DETTB-7|yes; why: higher confidence-adjusted growth (1.19 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.946 vs 0.689); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV14DETTB-TBCDASTOUS51-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.5014): highest fidelity KXNHLAST-26NOV14DETTB-TBCDASTOUS51-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes — override declined: the joint re-optimisation gives KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-2|yes less than the minimum stake; KXNHLAST-26NOV14DETTB-TBCDASTOUS51-1|yes kept
- thesis DET:OFFENSE_4PLUS (p 0.2873): highest fidelity KXNHLGOAL-26NOV14DETTB-DETADEBRINCAT93-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14DETTB-DETADEBRINCAT93-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.2927): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5014, phi -0.145)
- KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 42% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.2927, phi -0.268)
- KXNHLAST-26NOV14DETTB-TBCDASTOUS51-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 39% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.2927, phi -0.297)
- KXNHLGOAL-26NOV14DETTB-DETADEBRINCAT93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.5025, phi -0.3)
- override: override declined: the joint re-optimisation gives KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-2|yes less than the minimum stake; KXNHLAST-26NOV14DETTB-TBCDASTOUS51-1|yes kept

portfolios: A EV +1.08 (adj +0.52) on $11.38, P(profit) 0.6222, adj growth 4.9 bp · B EV +0.99 (adj +0.58) on $12.59, P(profit) 0.4657, adj growth 5.6 bp · C EV +0.82 (adj +0.51) on $7.62, P(profit) 0.4445, adj growth 4.8 bp · R EV +0.10 (adj +0.07) on $2.00, P(profit) 0.8728, adj growth 2.6 bp

## OTT @ PIT  ·  10000 joint draws  ·  416 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_OTT_win | p_overtime | goals | shots PIT/OTT | PIT/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.49 | 0.51 | 0.00 | 6.04 | 27.1/27.1 | 23.6/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.48 | 0.52 | 0.45 | 5.89 | 27.0/27.0 | 23.6/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.48 | 0.52 | 0.00 | 9.39 | 28.6/28.6 | 22.3/22.4 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.071 | 0.56 | 0.44 | 0.00 | 5.99 | 32.0/21.6 | 18.5/28.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.065 | 0.44 | 0.56 | 0.00 | 6.01 | 21.3/31.8 | 27.8/18.2 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.53 | 0.47 | 0.47 | 5.97 | 31.6/21.5 | 18.3/28.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 12 | 0.163 | 0.150 | +0.035 | +0.022 | $1.94 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV14OTTPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (9.60 vs 0.97 bp); alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.2849): highest fidelity KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3957): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3871, phi -0.2)

portfolios: A EV +1.00 (adj +0.61) on $3.49, P(profit) 0.2341, adj growth 5.7 bp · B EV +0.54 (adj +0.34) on $1.94, P(profit) 0.1629, adj growth 3.2 bp · C EV +0.75 (adj +0.47) on $2.70, P(profit) 0.1629, adj growth 4.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ WSH  ·  10000 joint draws  ·  436 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NJD_win | p_overtime | goals | shots WSH/NJD | WSH/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.52 | 0.48 | 0.00 | 6.01 | 27.5/27.9 | 24.6/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.53 | 0.47 | 0.46 | 5.95 | 27.8/28.1 | 24.8/24.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.096 | 0.47 | 0.53 | 0.00 | 5.99 | 22.2/33.5 | 29.5/18.9 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.47 | 0.53 | 0.48 | 5.9 | 22.3/33.5 | 30.1/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.55 | 0.46 | 0.00 | 9.26 | 29.3/29.7 | 24.2/23.0 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.063 | 0.48 | 0.52 | 0.00 | 9.2 | 23.3/35.4 | 28.6/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.241 | 0.217 | +0.061 | +0.037 | $3.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 19 | 0.231 | 0.219 | +0.030 | +0.019 | $1.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Nico Hischier: 1+ goals NO | 69 | 0.740 | 0.726 | +0.035 | +0.021 | $5.88 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 11 | 0.145 | 0.130 | +0.029 | +0.013 | $1.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (20.30 vs 4.67 bp); relationships: KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: WSH offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (20.30 vs 4.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WSH offense suppressed (<= 2 goals)
- **Nico Hischier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV14NJWSH-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (4.65 vs 1.39 bp); relationships: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-NJCBROWN16-1|yes; why: higher confidence-adjusted growth (3.79 vs 0.17 bp); alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3958): highest fidelity KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4001): highest fidelity KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.3768): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3864, phi -0.242)
- KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3864, phi -0.223)
- KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3768, phi -0.222)
- KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4001, phi -0.187)

portfolios: A EV +2.29 (adj +1.12) on $11.38, P(profit) 0.5424, adj growth 10.6 bp · B EV +1.98 (adj +1.17) on $12.16, P(profit) 0.4394, adj growth 11.2 bp · C EV +2.02 (adj +1.23) on $12.93, P(profit) 0.2413, adj growth 11.5 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7396, adj growth 2.3 bp

## PHI @ CBJ  ·  10000 joint draws  ·  396 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_PHI_win | p_overtime | goals | shots CBJ/PHI | CBJ/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.57 | 0.43 | 0.00 | 5.96 | 26.7/26.3 | 23.1/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.47 | 0.53 | 0.46 | 5.86 | 26.9/26.6 | 23.3/23.6 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.097 | 0.63 | 0.37 | 0.00 | 5.95 | 31.5/20.9 | 18.1/27.2 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.54 | 0.46 | 0.49 | 5.83 | 31.9/21.0 | 18.0/28.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.52 | 0.48 | 0.00 | 3.39 | 25.3/25.1 | 23.3/23.3 | late empty net |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.53 | 0.47 | 0.50 | 2.82 | 25.0/24.7 | 23.2/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Christian Dvorak: 1+ goals YES | 16 | 0.201 | 0.187 | +0.032 | +0.018 | $1.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Kent Johnson: 1+ goals NO | 72 | 0.766 | 0.753 | +0.032 | +0.019 | $5.93 | FUNDED_RESEARCH | $2 | CBJ:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 17 | 0.206 | 0.195 | +0.026 | +0.015 | $1.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Matvei Michkov: 1+ goals NO | 73 | 0.764 | 0.754 | +0.020 | +0.011 | $3.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV14PHICBJ-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (4.89 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14PHICBJ-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: PHI offense suppressed (<= 2 goals)
- **Kent Johnson: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV14PHICBJ-CBJ4|no; why: higher confidence-adjusted growth (4.13 vs 0.07 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.996 vs 0.873); alternative not eligible: confidence-adjusted EV +0.0027 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: CBJ offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHL1PSPREAD-26NOV14PHICBJ-CBJ2|yes; why: higher confidence-adjusted growth (3.15 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.884 vs 0.721); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV14PHICBJ-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: CBJ offense suppressed (<= 2 goals)
- **Matvei Michkov: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no; why: Player prop expression KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no selected over player prop KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.87 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV14PHICBJ-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:OFFENSE_4PLUS (p 0.306): highest fidelity KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.4262): highest fidelity KXNHLGOAL-26NOV14PHICBJ-CBJKJOHNSON91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14PHICBJ-CBJKJOHNSON91-1|no (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.306): highest fidelity KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes (same contract)
- KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4762, phi -0.234)
- KXNHLGOAL-26NOV14PHICBJ-CBJKJOHNSON91-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3564, phi -0.218)
- KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4262, phi -0.242)
- KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.306, phi -0.238)
- override: Player prop expression KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no selected over player prop KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.87 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.10 (adj +0.51) on $11.38, P(profit) 0.3442, adj growth 4.9 bp · B EV +0.86 (adj +0.49) on $12.31, P(profit) 0.716, adj growth 4.7 bp · C EV +1.78 (adj +0.81) on $20.23, P(profit) 0.7232, adj growth 7.6 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.766, adj growth 2.0 bp

## FLA @ STL  ·  10000 joint draws  ·  422 bet sides mapped, 8 +EV candidates, 4 on card


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
| Ross Johnston: 1+ goals YES | 5 | 0.083 | 0.073 | +0.029 | +0.020 | $1.45 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $1.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 25 | 0.294 | 0.282 | +0.031 | +0.019 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 30 | 0.345 | 0.332 | +0.030 | +0.018 | $2.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Ross Johnston: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (16.32 vs 3.86 bp); despite a smaller raw edge (+0.029 vs +0.031/contract); relationships: KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (7.42 vs 3.86 bp); relationships: KXNHLGOAL-26NOV14FLASTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (3.86 vs 3.15 bp); relationships: KXNHLGOAL-26NOV14FLASTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (3.86 vs 3.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV14FLASTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.4299): highest fidelity KXNHLTEAMTOTAL-26NOV14FLASTL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:OFFENSE_4PLUS (p 0.362): highest fidelity KXNHLTOTAL-26NOV14FLASTL-9|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2809): highest fidelity KXNHLTEAMTOTAL-26NOV14FLASTL-STL3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV14FLASTL-STL3|yes (same contract)
- KXNHLGOAL-26NOV14FLASTL-STLRJOHNSTON49-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.132)
- KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.18)
- KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.249)
- KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.271)

portfolios: A EV +1.62 (adj +0.72) on $11.38, P(profit) 0.4556, adj growth 6.5 bp · B EV +1.61 (adj +1.05) on $7.18, P(profit) 0.4586, adj growth 10.0 bp · C EV +0.49 (adj +0.29) on $4.50, P(profit) 0.4843, adj growth 2.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ DAL  ·  10000 joint draws  ·  414 bet sides mapped, 4 +EV candidates, 4 on card


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
| Jiri Kulich: 1+ goals YES | 13 | 0.164 | 0.154 | +0.026 | +0.017 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Arttu Hyry: 1+ goals YES | 16 | 0.199 | 0.186 | +0.029 | +0.017 | $1.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 64 | 0.682 | 0.670 | +0.026 | +0.014 | $3.20 | FUNDED_RESEARCH | $1 | BUF:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Roope Hintz: 1+ goals YES | 28 | 0.318 | 0.307 | +0.024 | +0.013 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14BUFDAL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (4.94 vs 0.14 bp); alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV14BUFDAL-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: BUF offense suppressed (<= 2 goals)
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes; why: higher confidence-adjusted growth (4.47 vs 1.90 bp); relationships: KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV14BUFDAL-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: DAL offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV14BUFDAL-BUFNOSTLUND86-1|no; why: higher confidence-adjusted growth (1.96 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: BUF offense succeeds (4+ goals)
- **Roope Hintz: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes has the higher standalone adjusted growth (4.47 vs 1.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV14BUFDAL-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis DAL:OFFENSE_4PLUS (p 0.424): highest fidelity KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.4516): highest fidelity KXNHLGOAL-26NOV14BUFDAL-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14BUFDAL-BUFTTHOMPSON72-1|no (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.3335): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.4516, phi -0.204)
- KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3642, phi -0.226)
- KXNHLGOAL-26NOV14BUFDAL-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3335, phi -0.225)
- KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3642, phi -0.253)

portfolios: A EV +1.01 (adj +0.59) on $9.99, P(profit) 0.4788, adj growth 5.6 bp · B EV +0.81 (adj +0.48) on $7.79, P(profit) 0.4788, adj growth 4.5 bp · C EV +0.57 (adj +0.32) on $6.91, P(profit) 0.7422, adj growth 3.0 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6821, adj growth 0.8 bp

## SJS @ UTA  ·  10000 joint draws  ·  398 bet sides mapped, 4 +EV candidates, 4 on card


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
| Daniil But: 1+ goals NO | 79 | 0.856 | 0.838 | +0.054 | +0.036 | $5.34 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 58 | 0.667 | 0.619 | +0.070 | +0.021 | $3.22 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Clayton Keller: 1+ assists NO | 40 | 0.472 | 0.431 | +0.055 | +0.014 | $1.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ assists NO | 68 | 0.751 | 0.706 | +0.056 | +0.010 | $2.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Daniil But: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (18.62 vs 4.19 bp); despite a smaller raw edge (+0.054 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: UTA offense succeeds (4+ goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no; why: higher confidence-adjusted growth (4.19 vs 1.84 bp); relationships: KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: MOSTLY_INDEPENDENT (phi 0.082); KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: UTA offense succeeds (4+ goals)
- **Clayton Keller: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no; why: second expression of the same thesis: KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no has the higher standalone adjusted growth (4.19 vs 1.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.082); they share one thesis budget; relationships: KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.082); KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: UTA offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV14SJUTA-SJMCELEBRINI71-2|no; why: higher confidence-adjusted growth (1.10 vs 0.14 bp); despite a smaller raw edge (+0.056 vs +0.078/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, UTA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis UTA:SUPPRESSED (p 0.3243): highest fidelity KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no (same contract)
- thesis SJS:SUPPRESSED (p 0.4652): highest fidelity KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no (same contract)
- KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.164)
- KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.263)
- KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.325)
- KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3148, phi -0.233)

portfolios: A EV +1.13 (adj +0.37) on $11.38, P(profit) 0.6351, adj growth 3.6 bp · B EV +1.14 (adj +0.45) on $12.78, P(profit) 0.5984, adj growth 4.4 bp · C EV +1.08 (adj +0.29) on $10.57, P(profit) 0.667, adj growth 2.8 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.8558, adj growth 3.6 bp

## NYI @ ANA  ·  10000 joint draws  ·  440 bet sides mapped, 11 +EV candidates, 4 on card


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
| Jeff Malott: 1+ goals YES | 10 | 0.149 | 0.134 | +0.043 | +0.028 | $2.41 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Pavel Mintyukov: 1+ goals YES | 6 | 0.098 | 0.086 | +0.035 | +0.022 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Sam Colangelo: 1+ goals YES | 11 | 0.156 | 0.141 | +0.039 | +0.024 | $2.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Troy Terry: 1+ assists NO | 67 | 0.839 | 0.716 | +0.154 | +0.031 | $6.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14NYIANA-ANA2|yes; why: higher confidence-adjusted growth (17.61 vs 3.17 bp); despite a smaller raw edge (+0.043 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.866 vs 0.503); relationships: KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLAST-26NOV14NYIANA-ANATTERRY19-1|no: MOSTLY_INDEPENDENT (phi -0.021); failure: ANA offense suppressed (<= 2 goals)
- **Pavel Mintyukov: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14NYIANA-ANA2|yes; why: higher confidence-adjusted growth (17.59 vs 3.17 bp); despite a smaller raw edge (+0.034 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.857 vs 0.503); relationships: KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV14NYIANA-ANATTERRY19-1|no: MOSTLY_INDEPENDENT (phi -0.035); failure: ANA offense suppressed (<= 2 goals)
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14NYIANA-ANA2|yes; why: higher confidence-adjusted growth (11.86 vs 3.17 bp); despite a smaller raw edge (+0.039 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.503); relationships: KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV14NYIANA-ANATTERRY19-1|no: MOSTLY_INDEPENDENT (phi -0.032); failure: ANA offense suppressed (<= 2 goals)
- **Troy Terry: 1+ assists NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV14NYIANA-ANACGAUTHIER61-1|no; why: higher confidence-adjusted growth (9.63 vs 0.01 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.032); failure: ANA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.5141): highest fidelity KXNHLTEAMTOTAL-26NOV14NYIANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14NYIANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3698): highest fidelity KXNHLSPREAD-26NOV14NYIANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14NYIANA-ANA2|yes (same contract)
- thesis NYI:SUPPRESSED (p 0.3931): highest fidelity KXNHLAST-26NOV14NYIANA-NYIMMACCELLI63-1|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV14NYIANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2867, phi -0.136)
- KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2867, phi -0.126)
- KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2867, phi -0.138)
- KXNHLAST-26NOV14NYIANA-ANATTERRY19-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.9 pts; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.5141, phi -0.166)

portfolios: A EV +1.67 (adj +0.43) on $11.38, P(profit) 0.4818, adj growth 4.1 bp · B EV +4.05 (adj +1.95) on $12.74, P(profit) 0.358, adj growth 18.6 bp · C EV +0.76 (adj +0.29) on $5.34, P(profit) 0.5657, adj growth 2.7 bp · R EV +0.40 (adj +0.26) on $1.00, P(profit) 0.1491, adj growth 9.7 bp

## CGY @ LAK  ·  10000 joint draws  ·  410 bet sides mapped, 4 +EV candidates, 3 on card


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
| Kevin Fiala: 1+ assists NO | 61 | 0.819 | 0.677 | +0.192 | +0.050 | $3.75 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Mats Zuccarello: 1+ assists NO | 67 | 0.813 | 0.717 | +0.128 | +0.032 | $3.75 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ goals NO | 65 | 0.701 | 0.686 | +0.035 | +0.020 | $2.32 | FUNDED_RESEARCH | $1 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Kevin Fiala: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no; why: higher confidence-adjusted growth (23.56 vs 10.11 bp); relationships: KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.057); KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.078); failure: LAK offense succeeds (4+ goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (10.11 vs 4.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLAST-26NOV14CGYLA-LAKFIALA22-1|no: MOSTLY_INDEPENDENT (phi 0.057); KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.035); failure: LAK offense succeeds (4+ goals)
- **Artemi Panarin: 1+ goals NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no; why: second expression of the same thesis: KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no has the higher standalone adjusted growth (10.11 vs 4.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.035); they share one thesis budget; relationships: KXNHLAST-26NOV14CGYLA-LAKFIALA22-1|no: MOSTLY_INDEPENDENT (phi 0.078); KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.035); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis LAK:SUPPRESSED (p 0.3629): highest fidelity KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no (same contract)
- thesis LAK:WINS_BY_2PLUS (p 0.3611): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV14CGYLA-LAKFIALA22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.9 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4201, phi -0.191)
- KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.8 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4201, phi -0.202)
- KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4201, phi -0.228)

portfolios: A EV +2.37 (adj +0.79) on $11.38, P(profit) 0.5334, adj growth 7.7 bp · B EV +1.98 (adj +0.54) on $9.82, P(profit) 0.6748, adj growth 5.3 bp · C EV +1.71 (adj +0.42) on $9.19, P(profit) 0.8134, adj growth 4.1 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.7014, adj growth 1.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
