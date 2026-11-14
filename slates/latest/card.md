# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-14T15:35:07Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.97 | +28.59 | +10.22 | +27.79 | 0.777 | -17.91 | -30.47 | 95.68 |
| B thesis-diversified (joint) ← optimiser card | 147.54 | +29.65 | +14.15 | +28.37 | 0.782 | -18.11 | -29.32 | 134.48 |
| C best expression per thesis | 148.32 | +27.82 | +12.96 | +24.97 | 0.730 | -25.75 | -38.01 | 120.32 |
| R FUNDED research stakes | 19.00 | +3.75 | +1.78 | +2.83 | 0.659 | -6.37 | -8.68 | 0.00 |

## SEA @ CAR  ·  10000 joint draws  ·  428 bet sides mapped, 48 +EV candidates, 3 on card


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
| Carolina wins by over 1.5 goals NO | 41 | 0.637 | 0.486 | +0.210 | +0.059 | $6.29 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 55 | 0.753 | 0.618 | +0.185 | +0.050 | $5.15 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikolaj Ehlers: 1+ goals NO | 72 | 0.782 | 0.764 | +0.048 | +0.030 | $7.47 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Carolina wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes has the higher standalone adjusted growth (55.23 vs 31.17 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.299); relationships: KXNHLSPREAD-26NOV14SEACAR-CAR3|no: DUPLICATIVE (phi 0.759); KXNHLGOAL-26NOV14SEACAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.131); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes has the higher standalone adjusted growth (55.23 vs 22.66 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.227); relationships: KXNHLSPREAD-26NOV14SEACAR-CAR2|no: DUPLICATIVE (phi 0.759); KXNHLGOAL-26NOV14SEACAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.123); failure: CAR wins by 2+
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes has the higher standalone adjusted growth (55.23 vs 10.30 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.096); relationships: KXNHLSPREAD-26NOV14SEACAR-CAR2|no: MOSTLY_INDEPENDENT (phi 0.131); KXNHLSPREAD-26NOV14SEACAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.123); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.19, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.16, CAR shot control · high event (8+) · decided (2+) 0.15.
- thesis SEA:WINS_BY_2PLUS (p 0.2217): highest fidelity KXNHLSPREAD-26NOV14SEACAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.3656): highest fidelity KXNHLTEAMTOTAL-26NOV14SEACAR-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4187): highest fidelity KXNHLSPREAD-26NOV14SEACAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no (same contract)
- KXNHLSPREAD-26NOV14SEACAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 23.2 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3633, phi -1.0)
- KXNHLSPREAD-26NOV14SEACAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 20.8 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3633, phi -0.759)
- KXNHLGOAL-26NOV14SEACAR-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4853, phi -0.193)

portfolios: A EV +6.14 (adj +1.41) on $11.92, P(profit) 0.6367, adj growth 13.2 bp · B EV +5.26 (adj +1.64) on $18.91, P(profit) 0.7234, adj growth 15.7 bp · C EV +4.45 (adj +2.00) on $2.88, P(profit) 0.1357, adj growth 18.3 bp · R EV +1.77 (adj +0.54) on $6.00, P(profit) 0.7234, adj growth 20.3 bp
equivalent contracts collapsed: KXNHLGAME-26NOV14SEACAR-CAR|no == KXNHLGAME-26NOV14SEACAR-SEA|yes

## WPG @ CHI  ·  10000 joint draws  ·  428 bet sides mapped, 8 +EV candidates, 4 on card


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
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.263 | 0.249 | +0.042 | +0.027 | $3.39 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Mario Ferraro: 1+ goals YES | 5 | 0.074 | 0.067 | +0.021 | +0.013 | $1.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:WINS_BY_2PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 11 | 0.139 | 0.131 | +0.022 | +0.014 | $1.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 61 | 0.733 | 0.647 | +0.107 | +0.020 | $6.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14WPGCHI-WPG2|no; why: higher confidence-adjusted growth (9.12 vs 2.04 bp); despite a smaller raw edge (+0.042 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14WPGCHI-WPGMFERRARO38-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV14WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); failure: CHI offense suppressed (<= 2 goals)
- **Mario Ferraro: 1+ goals YES** — thesis: WPG wins by 2+; alternative: KXNHLAST-26NOV14WPGCHI-WPGCPERFETTI91-1|yes; why: higher confidence-adjusted growth (7.51 vs 0.10 bp); despite a smaller raw edge (+0.021 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0033 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV14WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: WPG offense suppressed (<= 2 goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (9.12 vs 4.03 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV14WPGCHI-WPGMFERRARO38-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV14WPGCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (3.75 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLGOAL-26NOV14WPGCHI-WPGMFERRARO38-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.367): highest fidelity KXNHLSPREAD-26NOV14WPGCHI-WPG2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4142): highest fidelity KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no (same contract)
- thesis WPG:SUPPRESSED (p 0.3806): highest fidelity KXNHLSPREAD-26NOV14WPGCHI-WPG2|no [DIRECT], best adjusted EV KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4142, phi -0.244)
- KXNHLGOAL-26NOV14WPGCHI-WPGMFERRARO38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3806, phi -0.136)
- KXNHLGOAL-26NOV14WPGCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4142, phi -0.175)
- KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.3 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.367, phi -0.231)

portfolios: A EV +1.46 (adj +0.30) on $11.92, P(profit) 0.7506, adj growth 2.9 bp · B EV +2.51 (adj +1.10) on $12.67, P(profit) 0.3915, adj growth 10.4 bp · C EV +3.78 (adj +1.12) on $23.42, P(profit) 0.6341, adj growth 10.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ BOS  ·  10000 joint draws  ·  394 bet sides mapped, 14 +EV candidates, 4 on card


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
| William Borgen: 1+ goals YES | 5 | 0.086 | 0.073 | +0.033 | +0.020 | $1.65 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:WINS_BY_2PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Danila Yurov: 1+ goals YES | 16 | 0.217 | 0.202 | +0.048 | +0.032 | $3.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.140 | 0.129 | +0.034 | +0.022 | $2.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Fraser Minten: 1+ goals YES | 17 | 0.209 | 0.197 | +0.029 | +0.017 | $1.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV14MINBOS-BOS4|yes; why: higher confidence-adjusted growth (16.89 vs 1.32 bp); despite a smaller raw edge (+0.033 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14MINBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: MIN wins (incl. OT/SO)
- **Danila Yurov: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14MINBOS-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (15.81 vs 2.44 bp); relationships: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV14MINBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: MIN offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes has the higher standalone adjusted growth (15.81 vs 11.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV14MINBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: MIN offense suppressed (<= 2 goals)
- **Fraser Minten: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV14MINBOS-9|yes; why: higher confidence-adjusted growth (4.11 vs 1.97 bp); despite a smaller raw edge (+0.029 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.849 vs 0.362); relationships: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:WINS_BY_2PLUS (p 0.3199): highest fidelity KXNHLSPREAD-26NOV14MINBOS-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.3733): highest fidelity KXNHLTOTAL-26NOV14MINBOS-9|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4371): highest fidelity KXNHLTEAMTOTAL-26NOV14MINBOS-BOS4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14MINBOS-BOSFMINTEN93-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:WINS (p 0.4542, phi -0.167)
- KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4114, phi -0.224)
- KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4114, phi -0.175)
- KXNHLGOAL-26NOV14MINBOS-BOSFMINTEN93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3489, phi -0.21)

portfolios: A EV +1.60 (adj +0.67) on $11.92, P(profit) 0.5641, adj growth 6.4 bp · B EV +2.98 (adj +1.91) on $9.12, P(profit) 0.5142, adj growth 18.1 bp · C EV +3.76 (adj +2.15) on $14.89, P(profit) 0.3817, adj growth 19.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ TOR  ·  10000 joint draws  ·  444 bet sides mapped, 9 +EV candidates, 4 on card


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
| Teddy Blueger: 1+ goals YES | 11 | 0.163 | 0.147 | +0.046 | +0.030 | $2.95 | FUNDED_RESEARCH | $1 | TOR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 10 | 0.137 | 0.123 | +0.031 | +0.017 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 66 | 0.775 | 0.697 | +0.099 | +0.021 | $7.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| John Tavares: 1+ assists NO | 64 | 0.720 | 0.675 | +0.064 | +0.019 | $5.93 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14EDMTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (18.99 vs 3.16 bp); relationships: KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no: MOSTLY_INDEPENDENT (phi -0.024); failure: TOR offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (6.24 vs 3.13 bp); despite a smaller raw edge (+0.031 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (4.54 vs 1.60 bp); relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: EDM offense succeeds (4+ goals)
- **John Tavares: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV14EDMTOR-TORWNYLANDER88-2|no; why: higher confidence-adjusted growth (3.52 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.002); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:OFFENSE_4PLUS (p 0.4039): highest fidelity KXNHLAST-26NOV14EDMTOR-TORECOWAN53-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3044): highest fidelity KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no (same contract)
- thesis TOR:SUPPRESSED (p 0.3716): highest fidelity KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no (same contract)
- KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3716, phi -0.201)
- KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3044, phi -0.149)
- KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4905, phi -0.357)
- KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4039, phi -0.222)

portfolios: A EV +2.15 (adj +0.48) on $11.92, P(profit) 0.6072, adj growth 4.5 bp · B EV +3.30 (adj +1.42) on $17.91, P(profit) 0.6762, adj growth 13.5 bp · C EV +4.61 (adj +1.80) on $25.60, P(profit) 0.6895, adj growth 16.7 bp · R EV +0.39 (adj +0.26) on $1.00, P(profit) 0.1629, adj growth 9.6 bp

## COL @ MTL  ·  10000 joint draws  ·  378 bet sides mapped, 11 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_COL_win | p_overtime | goals | shots MTL/COL | MTL/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.121 | 0.38 | 0.62 | 0.00 | 6.08 | 22.0/34.0 | 29.6/19.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.42 | 0.58 | 0.00 | 6.06 | 28.0/28.5 | 24.6/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.43 | 0.57 | 0.00 | 9.47 | 29.5/30.1 | 23.3/23.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.45 | 0.55 | 0.45 | 5.98 | 22.4/34.2 | 30.6/19.2 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.093 | 0.38 | 0.62 | 0.00 | 9.41 | 23.7/35.8 | 28.1/18.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.47 | 0.53 | 0.48 | 6.0 | 28.0/28.5 | 25.1/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Martin Necas: 1+ goals YES | 32 | 0.400 | 0.378 | +0.064 | +0.043 | $5.38 | FUNDED_RESEARCH | $2 | COL:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 32 | 0.391 | 0.372 | +0.056 | +0.037 | $4.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Devon Toews: 1+ goals YES | 11 | 0.149 | 0.134 | +0.032 | +0.017 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Martin Necas: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (18.14 vs 13.08 bp); relationships: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV14COLMTL-COLDTOEWS7-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: COL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes has the higher standalone adjusted growth (18.14 vs 13.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV14COLMTL-COLDTOEWS7-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: COL offense suppressed (<= 2 goals)
- **Devon Toews: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes has the higher standalone adjusted growth (18.14 vs 6.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.484): highest fidelity KXNHLTEAMTOTAL-26NOV14COLMTL-COL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:WINS_BY_2PLUS (p 0.338): highest fidelity KXNHLSPREAD-26NOV14COLMTL-COL2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:WINS (p 0.5538): highest fidelity KXNHLSPREAD-26NOV14COLMTL-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3186, phi -0.309)
- KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3186, phi -0.262)
- KXNHLGOAL-26NOV14COLMTL-COLDTOEWS7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3186, phi -0.162)

portfolios: A EV +2.40 (adj +1.11) on $11.92, P(profit) 0.4245, adj growth 10.3 bp · B EV +2.20 (adj +1.41) on $11.44, P(profit) 0.6846, adj growth 13.5 bp · C EV +1.51 (adj +1.01) on $7.86, P(profit) 0.3995, adj growth 9.5 bp · R EV +0.38 (adj +0.26) on $2.00, P(profit) 0.3995, adj growth 9.6 bp

## DET @ TBL  ·  10000 joint draws  ·  364 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_DET_win | p_overtime | goals | shots TBL/DET | TBL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.72 | 0.28 | 0.00 | 6.02 | 27.2/26.8 | 24.2/22.7 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.100 | 0.75 | 0.25 | 0.00 | 5.99 | 32.4/21.4 | 19.2/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.56 | 0.44 | 0.48 | 5.89 | 27.2/27.3 | 24.1/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.72 | 0.28 | 0.00 | 9.3 | 29.3/28.9 | 24.2/21.8 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.56 | 0.44 | 0.49 | 5.95 | 32.6/21.7 | 18.5/29.1 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.069 | 0.77 | 0.23 | 0.00 | 9.21 | 34.1/22.9 | 18.8/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Conor Geekie: 1+ goals NO | 82 | 0.880 | 0.864 | +0.050 | +0.033 | $7.63 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Jake Guentzel: 1+ goals YES | 38 | 0.439 | 0.422 | +0.043 | +0.025 | $4.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_STRONGER | D |
| Sheldon Dries: 1+ goals YES | 7 | 0.100 | 0.087 | +0.026 | +0.012 | $1.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ assists NO | 37 | 0.468 | 0.398 | +0.081 | +0.011 | $2.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
- **Conor Geekie: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no; why: higher confidence-adjusted growth (17.60 vs 2.41 bp); despite a smaller raw edge (+0.050 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV14DETTB-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: TBL offense succeeds (4+ goals)
- **Jake Guentzel: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14DETTB-TBCDASTOUS51-1|yes; why: higher confidence-adjusted growth (5.85 vs 1.12 bp); despite a smaller raw edge (+0.043 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV14DETTB-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: INTENTIONAL_DIVERSIFIER (phi -0.278); failure: TBL offense suppressed (<= 2 goals)
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14DETTB-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (4.48 vs 0.64 bp); alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.018); failure: DET offense suppressed (<= 2 goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no; why: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no has the higher standalone adjusted growth (2.41 vs 1.19 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.433); relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.278); KXNHLGOAL-26NOV14DETTB-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, TBL shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.4972): highest fidelity KXNHLAST-26NOV14DETTB-TBCDASTOUS51-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.2911): highest fidelity KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.2882): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4972, phi -0.151)
- KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.2911, phi -0.266)
- KXNHLGOAL-26NOV14DETTB-DETSDRIES15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.5054, phi -0.168)
- KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.8 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4972, phi -0.31)

portfolios: A EV +1.40 (adj +0.34) on $11.92, P(profit) 0.5927, adj growth 3.3 bp · B EV +1.94 (adj +0.86) on $16.30, P(profit) 0.7224, adj growth 8.3 bp · C EV +1.52 (adj +0.60) on $16.76, P(profit) 0.3192, adj growth 5.6 bp · R EV +0.12 (adj +0.08) on $2.00, P(profit) 0.8799, adj growth 3.2 bp

## OTT @ PIT  ·  10000 joint draws  ·  416 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_OTT_win | p_overtime | goals | shots PIT/OTT | PIT/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.49 | 0.51 | 0.00 | 6.02 | 26.9/27.0 | 23.3/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.48 | 0.52 | 0.45 | 5.99 | 27.0/27.0 | 23.6/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.51 | 0.49 | 0.00 | 9.32 | 28.7/28.7 | 22.5/22.5 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.074 | 0.58 | 0.42 | 0.00 | 6.03 | 31.8/21.6 | 18.5/27.8 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.072 | 0.43 | 0.57 | 0.00 | 6.04 | 21.3/31.5 | 27.4/18.2 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.46 | 0.54 | 0.48 | 5.87 | 21.7/31.7 | 28.5/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 12 | 0.161 | 0.147 | +0.034 | +0.020 | $1.98 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Fabian Zetterlund: 1+ goals YES | 19 | 0.227 | 0.216 | +0.026 | +0.015 | $1.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14OTTPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (7.51 vs 0.34 bp); alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14OTTPIT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: PIT offense suppressed (<= 2 goals)
- **Fabian Zetterlund: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14OTTPIT-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (3.25 vs 0.41 bp); alternative not eligible: confidence-adjusted EV +0.0052 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis PIT:OFFENSE_4PLUS (p 0.4004): highest fidelity KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4018): highest fidelity KXNHLGOAL-26NOV14OTTPIT-OTTFZETTERLUND20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14OTTPIT-OTTFZETTERLUND20-1|yes (same contract)
- KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3848, phi -0.193)
- KXNHLGOAL-26NOV14OTTPIT-OTTFZETTERLUND20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3765, phi -0.199)

portfolios: A EV +1.33 (adj +0.73) on $5.63, P(profit) 0.4091, adj growth 6.8 bp · B EV +0.76 (adj +0.45) on $3.79, P(profit) 0.3529, adj growth 4.2 bp · C EV +1.03 (adj +0.61) on $5.15, P(profit) 0.3529, adj growth 5.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ WSH  ·  10000 joint draws  ·  436 bet sides mapped, 7 +EV candidates, 4 on card


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
| Aliaksei Protas: 1+ goals YES | 17 | 0.241 | 0.220 | +0.061 | +0.040 | $4.22 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 18 | 0.231 | 0.216 | +0.041 | +0.025 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 11 | 0.145 | 0.130 | +0.029 | +0.013 | $1.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Arseny Gritsyuk: 1+ goals YES | 20 | 0.236 | 0.224 | +0.025 | +0.013 | $1.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (23.08 vs 8.96 bp); relationships: KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV14NJWSH-NJAGRITSYUK81-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: WSH offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (23.08 vs 8.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV14NJWSH-NJAGRITSYUK81-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: WSH offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-NJAGRITSYUK81-1|yes; why: higher confidence-adjusted growth (3.79 vs 2.23 bp); relationships: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV14NJWSH-NJAGRITSYUK81-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NJD offense suppressed (<= 2 goals)
- **Arseny Gritsyuk: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-NJCBROWN16-1|yes; why: higher confidence-adjusted growth (2.23 vs 0.17 bp); alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3958): highest fidelity KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:OFFENSE_4PLUS (p 0.3768): highest fidelity KXNHLGOAL-26NOV14NJWSH-NJAGRITSYUK81-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14NJWSH-NJAGRITSYUK81-1|yes (same contract)
- thesis NJD:SUPPRESSED (p 0.4001): highest fidelity KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no (same contract)
- KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3864, phi -0.242)
- KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3864, phi -0.223)
- KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4001, phi -0.187)
- KXNHLGOAL-26NOV14NJWSH-NJAGRITSYUK81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4001, phi -0.212)

portfolios: A EV +3.21 (adj +1.59) on $11.92, P(profit) 0.6325, adj growth 14.9 bp · B EV +2.52 (adj +1.55) on $9.80, P(profit) 0.5019, adj growth 14.6 bp · C EV +2.42 (adj +1.52) on $14.01, P(profit) 0.3742, adj growth 14.1 bp · R EV +0.68 (adj +0.44) on $2.00, P(profit) 0.2413, adj growth 15.9 bp

## PHI @ CBJ  ·  10000 joint draws  ·  396 bet sides mapped, 7 +EV candidates, 3 on card


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
| Mathieu Olivier: 1+ goals YES | 17 | 0.218 | 0.203 | +0.038 | +0.023 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 16 | 0.198 | 0.185 | +0.029 | +0.016 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Matvei Michkov: 1+ goals NO | 73 | 0.766 | 0.755 | +0.022 | +0.012 | $4.16 | FUNDED_RESEARCH | $2 | PHI:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14PHICBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (7.97 vs 2.43 bp); relationships: KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: CBJ offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14PHICBJ-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (3.77 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: PHI offense suppressed (<= 2 goals)
- **Matvei Michkov: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no; why: Player prop expression KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no selected over player prop KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.88 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.3564): highest fidelity KXNHLGOAL-26NOV14PHICBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.306): highest fidelity KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes (same contract)
- thesis PHI:SUPPRESSED (p 0.4762): highest fidelity KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no — Player prop expression KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no selected over player prop KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.88 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4262, phi -0.248)
- KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4762, phi -0.22)
- KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.306, phi -0.226)
- override: Player prop expression KXNHLGOAL-26NOV14PHICBJ-PHIMMICHKOV39-1|no selected over player prop KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.88 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.56 (adj +0.76) on $11.74, P(profit) 0.507, adj growth 7.2 bp · B EV +0.94 (adj +0.55) on $8.40, P(profit) 0.3749, adj growth 5.2 bp · C EV +1.83 (adj +0.85) on $13.85, P(profit) 0.3749, adj growth 7.9 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.7656, adj growth 1.1 bp

## FLA @ STL  ·  10000 joint draws  ·  422 bet sides mapped, 7 +EV candidates, 4 on card


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
| Ross Johnston: 1+ goals YES | 5 | 0.083 | 0.073 | +0.029 | +0.020 | $1.69 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $2.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Sam Bennett: 1+ goals YES | 24 | 0.291 | 0.276 | +0.038 | +0.023 | $2.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 25 | 0.294 | 0.282 | +0.031 | +0.019 | $2.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Ross Johnston: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (16.32 vs 3.86 bp); despite a smaller raw edge (+0.029 vs +0.031/contract); relationships: KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (7.42 vs 3.86 bp); relationships: KXNHLGOAL-26NOV14FLASTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: STL offense suppressed (<= 2 goals)
- **Sam Bennett: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV14FLASTL-9|yes; why: higher confidence-adjusted growth (5.96 vs 1.92 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.925 vs 0.373); relationships: KXNHLGOAL-26NOV14FLASTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: FLA offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (3.86 vs 3.15 bp); relationships: KXNHLGOAL-26NOV14FLASTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:OFFENSE_4PLUS (p 0.362): highest fidelity KXNHLTOTAL-26NOV14FLASTL-9|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.4299): highest fidelity KXNHLTEAMTOTAL-26NOV14FLASTL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2809): highest fidelity KXNHLTEAMTOTAL-26NOV14FLASTL-STL3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV14FLASTL-STL3|yes (same contract)
- KXNHLGOAL-26NOV14FLASTL-STLRJOHNSTON49-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.132)
- KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.18)
- KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4104, phi -0.249)
- KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.249)

portfolios: A EV +1.78 (adj +0.81) on $11.92, P(profit) 0.4063, adj growth 7.4 bp · B EV +2.08 (adj +1.34) on $8.83, P(profit) 0.4604, adj growth 12.7 bp · C EV +0.90 (adj +0.54) on $6.69, P(profit) 0.5006, adj growth 5.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ DAL  ·  10000 joint draws  ·  414 bet sides mapped, 2 +EV candidates, 2 on card


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
| Arttu Hyry: 1+ goals YES | 16 | 0.199 | 0.186 | +0.029 | +0.017 | $1.87 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Jiri Kulich: 1+ goals YES | 13 | 0.164 | 0.149 | +0.026 | +0.011 | $1.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14BUFDAL-DALTHARLEY55-2|yes; why: higher confidence-adjusted growth (4.47 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: DAL offense suppressed (<= 2 goals)
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14BUFDAL-BUFOPOWER25-1|yes; why: higher confidence-adjusted growth (2.41 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis DAL:OFFENSE_4PLUS (p 0.424): highest fidelity KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.3335): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3642, phi -0.226)
- KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.4516, phi -0.204)

portfolios: A EV +0.71 (adj +0.36) on $3.91, P(profit) 0.3322, adj growth 3.4 bp · B EV +0.55 (adj +0.29) on $3.05, P(profit) 0.3322, adj growth 2.7 bp · C EV +0.43 (adj +0.25) on $2.52, P(profit) 0.1986, adj growth 2.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Daniil But: 1+ goals NO | 79 | 0.856 | 0.838 | +0.054 | +0.036 | $6.21 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 58 | 0.667 | 0.619 | +0.070 | +0.021 | $3.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Clayton Keller: 1+ assists NO | 40 | 0.472 | 0.431 | +0.055 | +0.014 | $1.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
- **Daniil But: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (18.62 vs 4.19 bp); despite a smaller raw edge (+0.054 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: MOSTLY_INDEPENDENT (phi 0.062); failure: UTA offense succeeds (4+ goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no; why: higher confidence-adjusted growth (4.19 vs 1.84 bp); relationships: KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: MOSTLY_INDEPENDENT (phi 0.082); failure: UTA offense succeeds (4+ goals)
- **Clayton Keller: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no; why: second expression of the same thesis: KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no has the higher standalone adjusted growth (4.19 vs 1.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.082); they share one thesis budget; relationships: KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.082); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, UTA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis UTA:SUPPRESSED (p 0.3243): highest fidelity KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no (same contract)
- KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.164)
- KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.263)
- KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.325)

portfolios: A EV +1.26 (adj +0.46) on $11.92, P(profit) 0.4517, adj growth 4.4 bp · B EV +1.06 (adj +0.47) on $11.44, P(profit) 0.5782, adj growth 4.6 bp · C EV +0.85 (adj +0.26) on $7.27, P(profit) 0.667, adj growth 2.4 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.8558, adj growth 3.6 bp

## NYI @ ANA  ·  10000 joint draws  ·  440 bet sides mapped, 5 +EV candidates, 4 on card


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
| Jeff Malott: 1+ goals YES | 11 | 0.149 | 0.134 | +0.032 | +0.018 | $1.70 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Pavel Mintyukov: 1+ goals YES | 7 | 0.098 | 0.088 | +0.024 | +0.013 | $1.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Sam Colangelo: 1+ goals YES | 12 | 0.156 | 0.143 | +0.029 | +0.016 | $1.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Anaheim wins by over 1.5 goals YES | 30 | 0.370 | 0.332 | +0.055 | +0.018 | $1.30 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14NYIANA-ANA2|yes; why: higher confidence-adjusted growth (6.37 vs 3.17 bp); despite a smaller raw edge (+0.032 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.866 vs 0.503); relationships: KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLSPREAD-26NOV14NYIANA-ANA2|yes: MOSTLY_INDEPENDENT (phi 0.115); failure: ANA offense suppressed (<= 2 goals)
- **Pavel Mintyukov: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14NYIANA-ANA2|yes; why: higher confidence-adjusted growth (5.25 vs 3.17 bp); despite a smaller raw edge (+0.024 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.857 vs 0.503); relationships: KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26NOV14NYIANA-ANA2|yes: MOSTLY_INDEPENDENT (phi 0.114); failure: ANA offense suppressed (<= 2 goals)
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14NYIANA-ANA2|yes; why: higher confidence-adjusted growth (4.89 vs 3.17 bp); despite a smaller raw edge (+0.029 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.503); relationships: KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26NOV14NYIANA-ANA2|yes: MOSTLY_INDEPENDENT (phi 0.132); failure: ANA offense suppressed (<= 2 goals)
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV14NYIANA-ANA4|yes; why: higher confidence-adjusted growth (3.17 vs 2.59 bp); despite a smaller raw edge (+0.055 vs +0.057/contract); relationships: KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.114); KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.132); failure: NYI wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.5141): highest fidelity KXNHLTEAMTOTAL-26NOV14NYIANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14NYIANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3698): highest fidelity KXNHLSPREAD-26NOV14NYIANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14NYIANA-ANA2|yes (same contract)
- KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2867, phi -0.136)
- KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2867, phi -0.126)
- KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2867, phi -0.138)
- KXNHLSPREAD-26NOV14NYIANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:WINS (p 0.4178, phi -0.649)

portfolios: A EV +2.14 (adj +0.88) on $11.92, P(profit) 0.5139, adj growth 7.9 bp · B EV +1.41 (adj +0.72) on $5.70, P(profit) 0.358, adj growth 6.8 bp · C EV +0.56 (adj +0.18) on $3.17, P(profit) 0.3698, adj growth 1.7 bp · R EV +0.18 (adj +0.06) on $1.00, P(profit) 0.3698, adj growth 2.1 bp

## CGY @ LAK  ·  10000 joint draws  ·  410 bet sides mapped, 2 +EV candidates, 2 on card


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
| Kevin Fiala: 1+ assists NO | 63 | 0.819 | 0.680 | +0.173 | +0.034 | $7.63 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ goals NO | 66 | 0.701 | 0.686 | +0.026 | +0.010 | $2.55 | FUNDED_RESEARCH | $1 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Kevin Fiala: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (10.87 vs 1.07 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.078); failure: LAK offense succeeds (4+ goals)
- **Artemi Panarin: 1+ goals NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV14CGYLA-LAKFIALA22-1|no; why: higher confidence-adjusted growth (1.07 vs 0.09 bp); despite a smaller raw edge (+0.026 vs +0.140/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: KXNHLAST-26NOV14CGYLA-LAKFIALA22-1|no: MOSTLY_INDEPENDENT (phi 0.078); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis LAK:SUPPRESSED (p 0.3629): highest fidelity KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no (same contract)
- KXNHLAST-26NOV14CGYLA-LAKFIALA22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4201, phi -0.191)
- KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4201, phi -0.228)

portfolios: A EV +1.45 (adj +0.32) on $9.49, P(profit) 0.5883, adj growth 3.1 bp · B EV +2.14 (adj +0.44) on $10.18, P(profit) 0.8191, adj growth 4.2 bp · C EV +0.16 (adj +0.07) on $4.25, P(profit) 0.7014, adj growth 0.6 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.7014, adj growth 0.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
