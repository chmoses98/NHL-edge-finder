# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-14T15:04:36Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +29.45 | +9.56 | +27.90 | 0.759 | -23.68 | -37.46 | 87.05 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +25.88 | +11.45 | +25.08 | 0.766 | -18.34 | -30.10 | 108.39 |
| C best expression per thesis | 150.00 | +28.05 | +12.62 | +24.38 | 0.710 | -28.14 | -41.69 | 115.44 |
| R FUNDED research stakes | 20.00 | +3.80 | +1.72 | +2.53 | 0.663 | -5.95 | -7.58 | 0.00 |

## SEA @ CAR  ·  10000 joint draws  ·  434 bet sides mapped, 44 +EV candidates, 3 on card


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
| Sebastian Aho: 2+ goals NO | 90 | 0.956 | 0.941 | +0.050 | +0.034 | $8.25 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 41 | 0.637 | 0.486 | +0.210 | +0.059 | $6.82 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 55 | 0.753 | 0.618 | +0.185 | +0.050 | $6.33 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sebastian Aho: 2+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes has the higher standalone adjusted growth (55.23 vs 31.85 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.052); relationships: KXNHLSPREAD-26NOV14SEACAR-CAR2|no: MOSTLY_INDEPENDENT (phi 0.095); KXNHLSPREAD-26NOV14SEACAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.094); failure: CAR offense succeeds (4+ goals)
- **Carolina wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes has the higher standalone adjusted growth (55.23 vs 31.17 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.299); relationships: KXNHLGOAL-26NOV14SEACAR-CARSAHO20-2|no: MOSTLY_INDEPENDENT (phi 0.095); KXNHLSPREAD-26NOV14SEACAR-CAR3|no: DUPLICATIVE (phi 0.759); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes has the higher standalone adjusted growth (55.23 vs 22.66 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.227); relationships: KXNHLGOAL-26NOV14SEACAR-CARSAHO20-2|no: MOSTLY_INDEPENDENT (phi 0.094); KXNHLSPREAD-26NOV14SEACAR-CAR2|no: DUPLICATIVE (phi 0.759); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.19, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.16, CAR shot control · high event (8+) · decided (2+) 0.15.
- thesis SEA:WINS_BY_2PLUS (p 0.2217): highest fidelity KXNHLSPREAD-26NOV14SEACAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.3656): highest fidelity KXNHLTEAMTOTAL-26NOV14SEACAR-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.3): highest fidelity KXNHLSPREAD-26NOV14SEACAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14SEACAR-CARSAHO20-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4853, phi -0.14)
- KXNHLSPREAD-26NOV14SEACAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 23.2 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3633, phi -1.0)
- KXNHLSPREAD-26NOV14SEACAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 20.8 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3633, phi -0.759)

portfolios: A EV +7.33 (adj +1.68) on $14.22, P(profit) 0.6367, adj growth 15.5 bp · B EV +5.87 (adj +1.82) on $21.40, P(profit) 0.6367, adj growth 17.5 bp · C EV +5.21 (adj +2.34) on $3.37, P(profit) 0.1357, adj growth 21.1 bp · R EV +1.80 (adj +0.57) on $7.00, P(profit) 0.6367, adj growth 21.6 bp
equivalent contracts collapsed: KXNHLGAME-26NOV14SEACAR-CAR|no == KXNHLGAME-26NOV14SEACAR-SEA|yes

## WPG @ CHI  ·  10000 joint draws  ·  428 bet sides mapped, 4 +EV candidates, 4 on card


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
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.263 | 0.249 | +0.042 | +0.027 | $3.66 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 61 | 0.733 | 0.647 | +0.107 | +0.020 | $7.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Josh Morrissey: 1+ assists NO | 55 | 0.675 | 0.587 | +0.108 | +0.020 | $4.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
| Winnipeg wins by over 1.5 goals NO | 63 | 0.697 | 0.661 | +0.051 | +0.015 | $3.57 | FUNDED_RESEARCH | $1 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14WPGCHI-WPG2|no; why: higher confidence-adjusted growth (9.12 vs 2.04 bp); despite a smaller raw edge (+0.042 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26NOV14WPGCHI-WPG2|no: MOSTLY_INDEPENDENT (phi 0.14); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV14WPGCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (3.75 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLSPREAD-26NOV14WPGCHI-WPG2|no: INTENTIONAL_DIVERSIFIER (phi -0.137); failure: CHI offense succeeds (4+ goals)
- **Josh Morrissey: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV14WPGCHI-WPG2|no; why: higher confidence-adjusted growth (3.57 vs 2.04 bp); relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLSPREAD-26NOV14WPGCHI-WPG2|no: REINFORCING (phi 0.178); failure: WPG offense succeeds (4+ goals)
- **Winnipeg wins by over 1.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV14WPGCHI-CHI3|yes; why: higher confidence-adjusted growth (2.04 vs 0.58 bp); alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.14); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.137); KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no: REINFORCING (phi 0.178); failure: WPG wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.367): highest fidelity KXNHLSPREAD-26NOV14WPGCHI-WPG2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4142): highest fidelity KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no (same contract)
- thesis WPG:SUPPRESSED (p 0.3806): highest fidelity KXNHLSPREAD-26NOV14WPGCHI-WPG2|no [DIRECT], best adjusted EV KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4142, phi -0.244)
- KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.3 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.367, phi -0.231)
- KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.5 pts; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4042, phi -0.257)
- KXNHLSPREAD-26NOV14WPGCHI-WPG2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:WINS_BY_2PLUS (p 0.3032, phi -1.0)

portfolios: A EV +2.18 (adj +0.66) on $14.22, P(profit) 0.5129, adj growth 6.3 bp · B EV +3.19 (adj +0.94) on $19.77, P(profit) 0.6341, adj growth 8.9 bp · C EV +4.42 (adj +1.31) on $27.40, P(profit) 0.6341, adj growth 12.0 bp · R EV +0.08 (adj +0.02) on $1.00, P(profit) 0.6968, adj growth 0.9 bp

## MIN @ BOS  ·  10000 joint draws  ·  394 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_MIN_win | p_overtime | goals | shots BOS/MIN | BOS/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.55 | 0.45 | 0.00 | 6.01 | 28.1/28.3 | 25.0/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.45 | 5.99 | 28.3/28.5 | 25.1/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.59 | 0.41 | 0.00 | 9.41 | 29.6/29.9 | 24.1/22.6 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.082 | 0.48 | 0.52 | 0.00 | 6.02 | 22.7/33.6 | 29.6/19.5 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.48 | 0.52 | 0.49 | 5.87 | 22.5/33.5 | 30.0/19.3 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.059 | 0.48 | 0.52 | 0.00 | 9.24 | 24.0/35.4 | 29.1/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Borgen: 1+ goals YES | 5 | 0.088 | 0.075 | +0.035 | +0.022 | $2.05 | FUNDED_RESEARCH | $1 | BOS:WINS_BY_2PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.146 | 0.133 | +0.040 | +0.027 | $3.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Danila Yurov: 1+ goals YES | 16 | 0.206 | 0.194 | +0.037 | +0.024 | $3.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ assists NO | 52 | 0.603 | 0.554 | +0.066 | +0.017 | $4.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLSPREAD-26NOV14MINBOS-BOS3|yes; why: higher confidence-adjusted growth (19.31 vs 3.04 bp); despite a smaller raw edge (+0.035 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.771 vs 0.467); relationships: KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26NOV14MINBOS-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: MIN wins (incl. OT/SO)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes; why: higher confidence-adjusted growth (16.21 vs 8.94 bp); relationships: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26NOV14MINBOS-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.036); failure: MIN offense suppressed (<= 2 goals)
- **Danila Yurov: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV14MINBOS-9|yes; why: higher confidence-adjusted growth (8.94 vs 2.44 bp); despite a smaller raw edge (+0.037 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.874 vs 0.37); relationships: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26NOV14MINBOS-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.038); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV14MINBOS-BOS3|yes; why: KXNHLSPREAD-26NOV14MINBOS-BOS3|yes has the higher standalone adjusted growth (3.04 vs 2.46 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.150); relationships: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi -0.038); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:WINS_BY_2PLUS (p 0.3179): highest fidelity KXNHLTEAMTOTAL-26NOV14MINBOS-BOS3|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.3765): highest fidelity KXNHLTOTAL-26NOV14MINBOS-9|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4007): highest fidelity KXNHLAST-26NOV14MINBOS-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14MINBOS-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:WINS (p 0.4618, phi -0.166)
- KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4007, phi -0.177)
- KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4007, phi -0.22)
- KXNHLAST-26NOV14MINBOS-MINKKAPRIZOV97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3765, phi -0.278)

portfolios: A EV +1.84 (adj +0.48) on $14.22, P(profit) 0.3585, adj growth 4.3 bp · B EV +3.70 (adj +2.18) on $12.69, P(profit) 0.3857, adj growth 20.4 bp · C EV +3.54 (adj +2.04) on $16.27, P(profit) 0.3555, adj growth 18.6 bp · R EV +0.65 (adj +0.40) on $1.00, P(profit) 0.0882, adj growth 14.0 bp

## EDM @ TOR  ·  10000 joint draws  ·  444 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_EDM_win | p_overtime | goals | shots TOR/EDM | TOR/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.41 | 0.59 | 0.00 | 6.09 | 28.6/29.1 | 25.0/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.40 | 0.60 | 0.00 | 9.59 | 30.2/30.4 | 23.6/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.49 | 0.51 | 0.47 | 6.01 | 28.6/29.0 | 25.4/25.3 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.096 | 0.35 | 0.65 | 0.00 | 6.06 | 22.7/34.5 | 29.8/20.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.083 | 0.30 | 0.70 | 0.00 | 9.52 | 24.2/36.3 | 28.0/19.4 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.47 | 0.53 | 0.47 | 5.98 | 22.9/34.3 | 30.8/19.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.161 | 0.146 | +0.044 | +0.029 | $3.22 | FUNDED_RESEARCH | $1 | TOR:WINS_BY_2PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 66 | 0.773 | 0.696 | +0.098 | +0.021 | $8.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Alex Formenton: 1+ goals YES | 11 | 0.145 | 0.129 | +0.029 | +0.012 | $1.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Zach Hyman: 1+ goals YES | 32 | 0.358 | 0.348 | +0.023 | +0.012 | $2.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR wins by 2+; alternative: KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (17.36 vs 3.33 bp); despite a smaller raw edge (+0.044 vs +0.098/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV14EDMTOR-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: TOR offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (4.28 vs 3.33 bp); despite a smaller raw edge (+0.098 vs +0.098/contract); relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26NOV14EDMTOR-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.145); failure: EDM offense succeeds (4+ goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes; why: KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (3.65 vs 3.16 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.013); relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26NOV14EDMTOR-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: EDM offense suppressed (<= 2 goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes; why: Player prop expression KXNHLGOAL-26NOV14EDMTOR-EDMZHYMAN18-1|yes selected over player prop KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.48 vs 0.47 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.145); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:WINS_BY_2PLUS (p 0.2288): highest fidelity KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:OFFENSE_4PLUS (p 0.4036): highest fidelity KXNHLAST-26NOV14EDMTOR-TORECOWAN53-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2925): highest fidelity KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no (same contract)
- KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.379, phi -0.189)
- KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.8 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5103, phi -0.349)
- KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2925, phi -0.145)
- KXNHLGOAL-26NOV14EDMTOR-EDMZHYMAN18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2925, phi -0.248)
- override: Player prop expression KXNHLGOAL-26NOV14EDMTOR-EDMZHYMAN18-1|yes selected over player prop KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.48 vs 0.47 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.01 (adj +0.69) on $14.22, P(profit) 0.6689, adj growth 6.4 bp · B EV +3.01 (adj +1.31) on $15.98, P(profit) 0.4502, adj growth 12.3 bp · C EV +4.40 (adj +1.75) on $20.73, P(profit) 0.3711, adj growth 16.0 bp · R EV +0.38 (adj +0.25) on $1.00, P(profit) 0.1611, adj growth 9.1 bp

## COL @ MTL  ·  10000 joint draws  ·  378 bet sides mapped, 10 +EV candidates, 4 on card


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
| Artturi Lehkonen: 1+ goals YES | 32 | 0.391 | 0.372 | +0.056 | +0.037 | $5.19 | FUNDED_RESEARCH | $2 | COL:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Martin Necas: 1+ goals YES | 33 | 0.400 | 0.380 | +0.054 | +0.034 | $4.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_STRONGER | D |
| Montreal wins by over 1.5 goals NO | 68 | 0.749 | 0.712 | +0.054 | +0.017 | $1.44 | FUNDED_RESEARCH | $1 | COL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nazem Kadri: 1+ goals YES | 27 | 0.303 | 0.294 | +0.020 | +0.010 | $1.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes; why: higher confidence-adjusted growth (13.08 vs 11.22 bp); relationships: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26NOV14COLMTL-MTL2|no: REINFORCING (phi 0.161); KXNHLGOAL-26NOV14COLMTL-COLNKADRI91-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: COL offense suppressed (<= 2 goals)
- **Martin Necas: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (13.08 vs 11.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26NOV14COLMTL-MTL2|no: REINFORCING (phi 0.217); KXNHLGOAL-26NOV14COLMTL-COLNKADRI91-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: COL offense suppressed (<= 2 goals)
- **Montreal wins by over 1.5 goals NO** — thesis: COL wins (incl. OT/SO); alternative: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (13.08 vs 2.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.161); they share one thesis budget; relationships: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: REINFORCING (phi 0.161); KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: REINFORCING (phi 0.217); KXNHLGOAL-26NOV14COLMTL-COLNKADRI91-1|yes: MOSTLY_INDEPENDENT (phi 0.137); failure: MTL wins by 2+
- **Nazem Kadri: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (13.08 vs 1.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSPREAD-26NOV14COLMTL-MTL2|no: MOSTLY_INDEPENDENT (phi 0.137); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.484): highest fidelity KXNHLTEAMTOTAL-26NOV14COLMTL-COL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:WINS (p 0.5538): highest fidelity KXNHLSPREAD-26NOV14COLMTL-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:WINS_BY_2PLUS (p 0.338): highest fidelity KXNHLSPREAD-26NOV14COLMTL-COL2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3186, phi -0.262)
- KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3186, phi -0.309)
- KXNHLSPREAD-26NOV14COLMTL-MTL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.2511, phi -1.0)
- KXNHLGOAL-26NOV14COLMTL-COLNKADRI91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3186, phi -0.219)

portfolios: A EV +2.95 (adj +1.01) on $14.22, P(profit) 0.4394, adj growth 8.7 bp · B EV +1.82 (adj +1.13) on $12.73, P(profit) 0.631, adj growth 10.7 bp · C EV +2.52 (adj +1.63) on $15.61, P(profit) 0.631, adj growth 15.0 bp · R EV +0.41 (adj +0.24) on $3.00, P(profit) 0.3908, adj growth 8.9 bp

## DET @ TBL  ·  10000 joint draws  ·  364 bet sides mapped, 4 +EV candidates, 4 on card


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
| Conor Geekie: 1+ goals NO | 83 | 0.880 | 0.866 | +0.040 | +0.026 | $6.20 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Jake Guentzel: 1+ goals YES | 38 | 0.439 | 0.422 | +0.043 | +0.025 | $4.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 2+ assists NO | 75 | 0.824 | 0.777 | +0.061 | +0.014 | $5.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ assists NO | 37 | 0.468 | 0.398 | +0.081 | +0.011 | $1.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
- **Conor Geekie: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no; why: higher confidence-adjusted growth (11.43 vs 2.41 bp); despite a smaller raw edge (+0.040 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: TBL offense succeeds (4+ goals)
- **Jake Guentzel: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14DETTB-TBCDASTOUS51-1|yes; why: higher confidence-adjusted growth (5.85 vs 0.67 bp); despite a smaller raw edge (+0.043 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no: INTENTIONAL_DIVERSIFIER (phi -0.227); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: INTENTIONAL_DIVERSIFIER (phi -0.278); failure: TBL offense suppressed (<= 2 goals)
- **Nikita Kucherov: 2+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (2.41 vs 1.19 bp); despite a smaller raw edge (+0.061 vs +0.081/contract); relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.227); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: DUPLICATIVE (phi 0.433); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no; why: second expression of the same thesis: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no has the higher standalone adjusted growth (2.41 vs 1.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.433); they share one thesis budget; relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.278); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no: DUPLICATIVE (phi 0.433); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, TBL shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.4972): highest fidelity KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.2911): highest fidelity KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no (same contract)
- KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4972, phi -0.151)
- KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.2911, phi -0.266)
- KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4972, phi -0.286)
- KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.8 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4972, phi -0.31)

portfolios: A EV +1.59 (adj +0.50) on $14.22, P(profit) 0.6316, adj growth 4.8 bp · B EV +1.56 (adj +0.65) on $17.98, P(profit) 0.7142, adj growth 6.2 bp · C EV +1.78 (adj +0.70) on $19.61, P(profit) 0.3192, adj growth 6.5 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.8799, adj growth 2.5 bp

## OTT @ PIT  ·  10000 joint draws  ·  416 bet sides mapped, 1 +EV candidates, 1 on card


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
| Connor Dewar: 1+ goals YES | 13 | 0.161 | 0.148 | +0.023 | +0.010 | $1.23 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14OTTPIT-PIT2|yes; why: higher confidence-adjusted growth (1.98 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.839 vs 0.512); alternative not eligible: confidence-adjusted EV +0.0010 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis PIT:OFFENSE_4PLUS (p 0.4004): highest fidelity KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes (same contract)
- KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3848, phi -0.193)

portfolios: A EV +0.32 (adj +0.14) on $1.91, P(profit) 0.1611, adj growth 1.3 bp · B EV +0.21 (adj +0.09) on $1.23, P(profit) 0.1611, adj growth 0.9 bp · C EV +0.29 (adj +0.13) on $1.70, P(profit) 0.1611, adj growth 1.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Aliaksei Protas: 1+ goals YES | 18 | 0.241 | 0.220 | +0.051 | +0.029 | $3.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 11 | 0.145 | 0.130 | +0.029 | +0.013 | $1.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 19 | 0.231 | 0.217 | +0.030 | +0.016 | $2.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Nico Hischier: 1+ goals NO | 70 | 0.740 | 0.727 | +0.025 | +0.013 | $4.87 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (12.10 vs 3.50 bp); relationships: KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: WSH offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-NJAGRITSYUK81-1|yes; why: higher confidence-adjusted growth (3.79 vs 0.34 bp); alternative not eligible: confidence-adjusted EV +0.0052 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: NJD offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (12.10 vs 3.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: WSH offense suppressed (<= 2 goals)
- **Nico Hischier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV14NJWSH-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (1.68 vs 1.39 bp); relationships: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3958): highest fidelity KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4001): highest fidelity KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.3768): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3864, phi -0.242)
- KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4001, phi -0.187)
- KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3864, phi -0.223)
- KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3768, phi -0.222)

portfolios: A EV +3.35 (adj +1.47) on $14.22, P(profit) 0.5422, adj growth 13.2 bp · B EV +1.83 (adj +0.99) on $12.10, P(profit) 0.4627, adj growth 9.3 bp · C EV +1.59 (adj +0.90) on $11.74, P(profit) 0.2413, adj growth 8.3 bp · R EV +0.07 (adj +0.03) on $2.00, P(profit) 0.7396, adj growth 1.3 bp

## PHI @ CBJ  ·  10000 joint draws  ·  396 bet sides mapped, 2 +EV candidates, 2 on card


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
| Mathieu Olivier: 1+ goals YES | 18 | 0.218 | 0.206 | +0.027 | +0.015 | $1.97 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Travis Konecny: 1+ assists NO | 67 | 0.742 | 0.699 | +0.057 | +0.013 | $4.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14PHICBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (3.33 vs 0.50 bp); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV14PHICBJ-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (1.76 vs 0.47 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.3564): highest fidelity KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes (same contract)
- thesis PHI:SUPPRESSED (p 0.4762): highest fidelity KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no (same contract)
- KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4262, phi -0.248)
- KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.306, phi -0.227)

portfolios: A EV +0.81 (adj +0.30) on $8.08, P(profit) 0.796, adj growth 2.8 bp · B EV +0.69 (adj +0.25) on $6.89, P(profit) 0.796, adj growth 2.4 bp · C EV +0.96 (adj +0.35) on $9.55, P(profit) 0.796, adj growth 3.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## FLA @ STL  ·  10000 joint draws  ·  422 bet sides mapped, 5 +EV candidates, 4 on card


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
| Pius Suter: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $2.37 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Sam Bennett: 1+ goals YES | 24 | 0.291 | 0.276 | +0.038 | +0.023 | $3.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Ross Johnston: 1+ goals YES | 6 | 0.083 | 0.074 | +0.019 | +0.010 | $1.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 30 | 0.345 | 0.332 | +0.030 | +0.018 | $2.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (7.42 vs 3.15 bp); relationships: KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14FLASTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)
- **Sam Bennett: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV14FLASTL-9|yes; why: higher confidence-adjusted growth (5.96 vs 1.92 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.925 vs 0.373); relationships: KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14FLASTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: FLA offense suppressed (<= 2 goals)
- **Ross Johnston: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (3.90 vs 3.15 bp); despite a smaller raw edge (+0.019 vs +0.030/contract); relationships: KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV14FLASTL-9|yes; why: higher confidence-adjusted growth (3.15 vs 1.92 bp); despite a smaller raw edge (+0.030 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.914 vs 0.373); relationships: KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV14FLASTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:OFFENSE_4PLUS (p 0.362): highest fidelity KXNHLTOTAL-26NOV14FLASTL-9|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.4299): highest fidelity KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2809): highest fidelity KXNHLTOTAL-26NOV14FLASTL-9|yes [DIRECT], best adjusted EV KXNHLTOTAL-26NOV14FLASTL-9|yes (same contract)
- KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.18)
- KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4104, phi -0.249)
- KXNHLGOAL-26NOV14FLASTL-STLRJOHNSTON49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.132)
- KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.271)

portfolios: A EV +2.11 (adj +1.09) on $12.46, P(profit) 0.5006, adj growth 9.8 bp · B EV +1.57 (adj +0.95) on $9.25, P(profit) 0.4604, adj growth 9.0 bp · C EV +1.20 (adj +0.65) on $8.86, P(profit) 0.5353, adj growth 6.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Jiri Kulich: 1+ goals YES | 13 | 0.164 | 0.154 | +0.026 | +0.017 | $2.00 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Arttu Hyry: 1+ goals YES | 16 | 0.199 | 0.186 | +0.029 | +0.017 | $2.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14BUFDAL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (4.94 vs 0.14 bp); alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: BUF offense suppressed (<= 2 goals)
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes; why: higher confidence-adjusted growth (4.47 vs 0.20 bp); alternative not eligible: confidence-adjusted EV +0.0044 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis DAL:OFFENSE_4PLUS (p 0.424): highest fidelity KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.3335): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.4516, phi -0.204)
- KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3642, phi -0.226)

portfolios: A EV +0.84 (adj +0.51) on $4.67, P(profit) 0.3322, adj growth 4.8 bp · B EV +0.75 (adj +0.46) on $4.15, P(profit) 0.3322, adj growth 4.3 bp · C EV +0.51 (adj +0.30) on $2.95, P(profit) 0.1986, adj growth 2.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Daniil But: 1+ goals NO | 79 | 0.856 | 0.837 | +0.054 | +0.035 | $7.14 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 58 | 0.667 | 0.619 | +0.070 | +0.021 | $4.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Clayton Keller: 1+ assists NO | 40 | 0.472 | 0.431 | +0.055 | +0.014 | $1.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
- **Daniil But: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (17.36 vs 4.19 bp); despite a smaller raw edge (+0.054 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: MOSTLY_INDEPENDENT (phi 0.062); failure: UTA offense succeeds (4+ goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no; why: higher confidence-adjusted growth (4.19 vs 1.84 bp); relationships: KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: MOSTLY_INDEPENDENT (phi 0.082); failure: UTA offense succeeds (4+ goals)
- **Clayton Keller: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no; why: second expression of the same thesis: KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no has the higher standalone adjusted growth (4.19 vs 1.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.082); they share one thesis budget; relationships: KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.082); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, UTA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis UTA:SUPPRESSED (p 0.3243): highest fidelity KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no (same contract)
- KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.164)
- KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.263)
- KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.325)

portfolios: A EV +1.51 (adj +0.54) on $14.22, P(profit) 0.4517, adj growth 5.1 bp · B EV +1.21 (adj +0.53) on $13.15, P(profit) 0.5782, adj growth 5.1 bp · C EV +1.00 (adj +0.31) on $8.50, P(profit) 0.667, adj growth 2.8 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.8558, adj growth 3.5 bp

## NYI @ ANA  ·  10000 joint draws  ·  224 bet sides mapped, 2 +EV candidates, 1 on card


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
| Anaheim wins by over 1.5 goals YES | 30 | 0.370 | 0.332 | +0.055 | +0.018 | $2.68 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26NOV14NYIANA-ANA3|yes; why: higher confidence-adjusted growth (3.17 vs 1.52 bp); relationships: only recommended bet in this game; failure: NYI wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:WINS_BY_2PLUS (p 0.3698): highest fidelity KXNHLSPREAD-26NOV14NYIANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14NYIANA-ANA2|yes (same contract)
- KXNHLSPREAD-26NOV14NYIANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:WINS (p 0.4178, phi -0.649)

portfolios: A EV +1.61 (adj +0.49) on $9.10, P(profit) 0.3698, adj growth 3.9 bp · B EV +0.47 (adj +0.15) on $2.68, P(profit) 0.3698, adj growth 1.4 bp · C EV +0.65 (adj +0.21) on $3.71, P(profit) 0.3698, adj growth 1.9 bp · R EV +0.18 (adj +0.06) on $1.00, P(profit) 0.3698, adj growth 2.1 bp

## CGY @ LAK  ·  10000 joint draws  ·  410 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_CGY_win | p_overtime | goals | shots LAK/CGY | LAK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.63 | 0.37 | 0.00 | 6.0 | 28.4/28.0 | 25.1/24.3 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.107 | 0.67 | 0.33 | 0.00 | 5.99 | 33.9/22.1 | 19.5/29.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.48 | 5.86 | 28.5/28.2 | 24.8/25.1 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.57 | 0.43 | 0.43 | 5.87 | 34.1/22.5 | 19.5/30.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.61 | 0.39 | 0.00 | 9.31 | 30.0/29.6 | 24.4/23.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.60 | 0.40 | 0.00 | 3.49 | 27.4/26.8 | 25.2/25.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
