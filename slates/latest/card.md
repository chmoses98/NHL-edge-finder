# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-14T14:29:13Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.97 | +29.51 | +8.72 | +28.41 | 0.752 | -23.61 | -38.18 | 78.17 |
| B thesis-diversified (joint) ← optimiser card | 149.24 | +32.20 | +14.62 | +29.77 | 0.749 | -24.84 | -39.35 | 135.65 |
| C best expression per thesis | 149.28 | +33.99 | +15.29 | +29.84 | 0.718 | -31.65 | -47.03 | 138.61 |
| R FUNDED research stakes | 20.00 | +5.13 | +2.37 | +3.41 | 0.653 | -7.36 | -9.79 | 0.00 |

## SEA @ CAR  ·  10000 joint draws  ·  434 bet sides mapped, 39 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_SEA_win | p_overtime | goals | shots CAR/SEA | CAR/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.185 | 0.64 | 0.36 | 0.00 | 6.04 | 34.6/20.6 | 17.7/30.4 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.159 | 0.54 | 0.46 | 0.48 | 5.99 | 34.7/21.0 | 17.8/31.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.152 | 0.66 | 0.34 | 0.00 | 9.42 | 36.5/22.2 | 17.3/28.8 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.068 | 0.55 | 0.45 | 0.49 | 2.92 | 33.5/19.7 | 18.2/31.8 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.068 | 0.60 | 0.40 | 0.00 | 3.47 | 33.7/19.6 | 18.0/31.5 | even strength |
| CAR shot control · high event (8+) · tight (1-goal/OT) | 0.067 | 0.55 | 0.45 | 0.59 | 9.66 | 36.7/22.8 | 17.1/29.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Berkly Catton: 1+ goals YES | 14 | 0.227 | 0.203 | +0.078 | +0.054 | $6.61 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 41 | 0.640 | 0.487 | +0.213 | +0.060 | $7.77 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 55 | 0.754 | 0.618 | +0.187 | +0.051 | $5.77 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Seattle over 2.5 goals scored YES | 40 | 0.598 | 0.466 | +0.182 | +0.049 | $2.81 | FUNDED_RESEARCH | $1 | SEA:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: higher confidence-adjusted growth (49.07 vs 44.27 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.895 vs 0.481); relationships: KXNHLSPREAD-26NOV14SEACAR-CAR2|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLSPREAD-26NOV14SEACAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.13); KXNHLTEAMTOTAL-26NOV14SEACAR-SEA3|yes: REINFORCING (phi 0.238); failure: SEA offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV14SEACAR-CAR3|no; why: higher confidence-adjusted growth (32.51 vs 23.07 bp); relationships: KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.149); KXNHLSPREAD-26NOV14SEACAR-CAR3|no: DUPLICATIVE (phi 0.762); KXNHLTEAMTOTAL-26NOV14SEACAR-SEA3|yes: REINFORCING (phi 0.472); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV14SEACAR-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV14SEACAR-CAR2|no has the higher standalone adjusted growth (32.51 vs 23.07 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.762); they share one thesis budget; relationships: KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.13); KXNHLSPREAD-26NOV14SEACAR-CAR2|no: DUPLICATIVE (phi 0.762); KXNHLTEAMTOTAL-26NOV14SEACAR-SEA3|yes: REINFORCING (phi 0.42); failure: CAR wins by 2+
- **Seattle over 2.5 goals scored YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes has the higher standalone adjusted growth (49.07 vs 21.87 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.238); they share one thesis budget; relationships: KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes: REINFORCING (phi 0.238); KXNHLSPREAD-26NOV14SEACAR-CAR2|no: REINFORCING (phi 0.472); KXNHLSPREAD-26NOV14SEACAR-CAR3|no: REINFORCING (phi 0.42); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.18, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.16, CAR shot control · high event (8+) · decided (2+) 0.15.
- thesis SEA:OFFENSE_4PLUS (p 0.3638): highest fidelity KXNHLTEAMTOTAL-26NOV14SEACAR-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2165): highest fidelity KXNHLSPREAD-26NOV14SEACAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no (same contract)
- thesis CAR:SUPPRESSED (p 0.3062): highest fidelity KXNHLSPREAD-26NOV14SEACAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4114, phi -0.24)
- KXNHLSPREAD-26NOV14SEACAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 23.5 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3597, phi -1.0)
- KXNHLSPREAD-26NOV14SEACAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 20.9 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3597, phi -0.762)
- KXNHLTEAMTOTAL-26NOV14SEACAR-SEA3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 20.3 pts; opposing: failure thesis SEA:SUPPRESSED (p 0.4114, phi -0.98)

portfolios: A EV +7.37 (adj +1.77) on $14.89, P(profit) 0.6859, adj growth 16.4 bp · B EV +10.50 (adj +4.36) on $22.97, P(profit) 0.692, adj growth 40.3 bp · C EV +13.46 (adj +6.03) on $22.50, P(profit) 0.692, adj growth 54.4 bp · R EV +3.15 (adj +1.31) on $7.00, P(profit) 0.692, adj growth 47.7 bp
equivalent contracts collapsed: KXNHLGAME-26NOV14SEACAR-SEA|yes == KXNHLGAME-26NOV14SEACAR-CAR|no

## WPG @ CHI  ·  10000 joint draws  ·  428 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.46 | 0.54 | 0.00 | 6.03 | 26.9/27.2 | 23.7/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.46 | 5.93 | 26.7/27.0 | 23.8/23.4 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.099 | 0.39 | 0.61 | 0.00 | 6.05 | 21.0/32.1 | 27.8/18.2 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.48 | 0.52 | 0.50 | 5.95 | 21.5/32.4 | 28.9/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.47 | 0.53 | 0.00 | 9.25 | 28.0/28.4 | 22.3/22.2 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.060 | 0.38 | 0.62 | 0.00 | 9.32 | 22.8/34.2 | 26.7/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.263 | 0.249 | +0.042 | +0.027 | $4.46 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Winnipeg wins by over 1.5 goals NO | 63 | 0.697 | 0.661 | +0.051 | +0.015 | $4.35 | FUNDED_RESEARCH | $2 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Josh Morrissey: 1+ assists NO | 56 | 0.675 | 0.591 | +0.098 | +0.013 | $3.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
| Patrick Kane: 1+ assists NO | 62 | 0.733 | 0.647 | +0.097 | +0.010 | $5.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14WPGCHI-WPG2|no; why: higher confidence-adjusted growth (9.12 vs 2.04 bp); despite a smaller raw edge (+0.042 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV14WPGCHI-WPG2|no: MOSTLY_INDEPENDENT (phi 0.14); KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); failure: CHI offense suppressed (<= 2 goals)
- **Winnipeg wins by over 1.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV14WPGCHI-CHI3|yes; why: higher confidence-adjusted growth (2.04 vs 0.58 bp); alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.14); KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no: REINFORCING (phi 0.178); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.137); failure: WPG wins by 2+
- **Josh Morrissey: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV14WPGCHI-WPG2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV14WPGCHI-WPG2|no has the higher standalone adjusted growth (2.04 vs 1.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.178); they share one thesis budget; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26NOV14WPGCHI-WPG2|no: REINFORCING (phi 0.178); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: WPG offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV14WPGCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (0.98 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLSPREAD-26NOV14WPGCHI-WPG2|no: INTENTIONAL_DIVERSIFIER (phi -0.137); KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.367): highest fidelity KXNHLSPREAD-26NOV14WPGCHI-WPG2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.478): highest fidelity KXNHLSPREAD-26NOV14WPGCHI-WPG2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14WPGCHI-WPG2|no (same contract)
- thesis WPG:SUPPRESSED (p 0.3806): highest fidelity KXNHLSPREAD-26NOV14WPGCHI-WPG2|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV14WPGCHI-WPG2|no (same contract)
- KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4142, phi -0.244)
- KXNHLSPREAD-26NOV14WPGCHI-WPG2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:WINS_BY_2PLUS (p 0.3032, phi -1.0)
- KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.0 pts; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4042, phi -0.257)
- KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.3 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.367, phi -0.231)

portfolios: A EV +2.32 (adj +0.31) on $14.89, P(profit) 0.6093, adj growth 2.8 bp · B EV +2.71 (adj +0.82) on $18.49, P(profit) 0.5195, adj growth 7.6 bp · C EV +2.67 (adj +0.93) on $19.37, P(profit) 0.6083, adj growth 8.5 bp · R EV +0.16 (adj +0.05) on $2.00, P(profit) 0.6968, adj growth 1.6 bp

## MIN @ BOS  ·  10000 joint draws  ·  394 bet sides mapped, 14 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_MIN_win | p_overtime | goals | shots BOS/MIN | BOS/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.56 | 0.44 | 0.00 | 6.02 | 28.4/28.6 | 25.2/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.46 | 5.95 | 28.2/28.5 | 25.3/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.58 | 0.42 | 0.00 | 9.4 | 29.8/29.9 | 24.1/23.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.077 | 0.47 | 0.53 | 0.00 | 6.02 | 22.5/33.6 | 29.7/19.1 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.47 | 0.53 | 0.48 | 5.92 | 22.7/33.9 | 30.6/19.6 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.061 | 0.53 | 0.47 | 0.00 | 9.32 | 24.2/35.5 | 29.1/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Borgen: 1+ goals YES | 5 | 0.088 | 0.075 | +0.035 | +0.022 | $2.39 | FUNDED_RESEARCH | $1 | BOS:WINS_BY_2PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.146 | 0.133 | +0.040 | +0.027 | $3.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Danila Yurov: 1+ goals YES | 16 | 0.206 | 0.194 | +0.037 | +0.024 | $4.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Boston wins by over 2.5 goals YES | 16 | 0.212 | 0.183 | +0.043 | +0.014 | $2.05 | FUNDED_RESEARCH | $1 | BOS:WINS_BY_2PLUS | DIRECT (0.67) | EVIDENCE_MIXED | D |
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV14MINBOS-BOS5|yes; why: higher confidence-adjusted growth (19.31 vs 4.16 bp); despite a smaller raw edge (+0.035 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.737 vs 0.518); relationships: KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLSPREAD-26NOV14MINBOS-BOS3|yes: REINFORCING (phi 0.191); failure: MIN wins (incl. OT/SO)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes; why: higher confidence-adjusted growth (16.21 vs 8.94 bp); relationships: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26NOV14MINBOS-BOS3|yes: INTENTIONAL_DIVERSIFIER (phi -0.091); failure: MIN offense suppressed (<= 2 goals)
- **Danila Yurov: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV14MINBOS-9|yes; why: higher confidence-adjusted growth (8.94 vs 2.44 bp); despite a smaller raw edge (+0.037 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.878 vs 0.366); relationships: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26NOV14MINBOS-BOS3|yes: INTENTIONAL_DIVERSIFIER (phi -0.119); failure: MIN offense suppressed (<= 2 goals)
- **Boston wins by over 2.5 goals YES** — thesis: BOS wins by 2+; alternative: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes has the higher standalone adjusted growth (19.31 vs 3.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.191); they share one thesis budget; relationships: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: REINFORCING (phi 0.191); KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.091); KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.119); failure: MIN wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:WINS_BY_2PLUS (p 0.3179): highest fidelity KXNHLTEAMTOTAL-26NOV14MINBOS-BOS3|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.3765): highest fidelity KXNHLTOTAL-26NOV14MINBOS-8|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4355): highest fidelity KXNHLTEAMTOTAL-26NOV14MINBOS-BOS4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV14MINBOS-BOS5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:WINS (p 0.4618, phi -0.166)
- KXNHLGOAL-26NOV14MINBOS-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4007, phi -0.177)
- KXNHLGOAL-26NOV14MINBOS-MINDYUROV22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4007, phi -0.22)
- KXNHLSPREAD-26NOV14MINBOS-BOS3|yes: FUNDED_RESEARCH; family MIXED; loses 33% of the draws where the thesis happens; opposing: failure thesis MIN:WINS (p 0.4618, phi -0.48)

portfolios: A EV +2.25 (adj +0.61) on $14.89, P(profit) 0.4461, adj growth 5.2 bp · B EV +4.40 (adj +2.69) on $12.33, P(profit) 0.3857, adj growth 24.7 bp · C EV +4.04 (adj +2.27) on $18.60, P(profit) 0.3575, adj growth 20.5 bp · R EV +0.90 (adj +0.49) on $2.00, P(profit) 0.2593, adj growth 16.5 bp

## EDM @ TOR  ·  10000 joint draws  ·  444 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_EDM_win | p_overtime | goals | shots TOR/EDM | TOR/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.40 | 0.60 | 0.00 | 6.08 | 28.6/29.1 | 24.9/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.40 | 0.60 | 0.00 | 9.58 | 30.1/30.5 | 23.6/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.50 | 0.50 | 0.46 | 6.04 | 28.6/29.0 | 25.6/25.2 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.096 | 0.34 | 0.66 | 0.00 | 6.07 | 22.8/34.5 | 29.8/19.9 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.089 | 0.31 | 0.69 | 0.00 | 9.54 | 24.3/36.0 | 27.9/19.5 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.46 | 0.54 | 0.48 | 5.94 | 23.0/34.3 | 30.7/19.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.161 | 0.141 | +0.044 | +0.024 | $3.23 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TOR:WINS_BY_2PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 66 | 0.773 | 0.696 | +0.098 | +0.021 | $10.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ assists YES | 27 | 0.349 | 0.302 | +0.066 | +0.018 | $3.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Alex Formenton: 1+ goals YES | 11 | 0.145 | 0.129 | +0.029 | +0.012 | $1.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR wins by 2+; alternative: KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (11.93 vs 3.33 bp); despite a smaller raw edge (+0.044 vs +0.098/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: TOR offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (4.28 vs 3.33 bp); despite a smaller raw edge (+0.098 vs +0.098/contract); relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.102); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (3.65 vs 0.46 bp); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.102); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (3.65 vs 3.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:WINS_BY_2PLUS (p 0.2288): highest fidelity KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:OFFENSE_4PLUS (p 0.4036): highest fidelity KXNHLAST-26NOV14EDMTOR-TORECOWAN53-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2925): highest fidelity KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no (same contract)
- KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.379, phi -0.189)
- KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.8 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5103, phi -0.349)
- KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2925, phi -0.251)
- KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2925, phi -0.145)

portfolios: A EV +3.15 (adj +0.72) on $14.89, P(profit) 0.6689, adj growth 6.7 bp · B EV +4.09 (adj +1.42) on $19.61, P(profit) 0.4464, adj growth 13.2 bp · C EV +4.50 (adj +1.52) on $21.99, P(profit) 0.3711, adj growth 13.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ MTL  ·  10000 joint draws  ·  378 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_COL_win | p_overtime | goals | shots MTL/COL | MTL/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.126 | 0.38 | 0.62 | 0.00 | 6.11 | 22.1/34.0 | 29.6/19.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.43 | 0.57 | 0.00 | 6.03 | 28.1/28.6 | 24.7/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.45 | 0.55 | 0.00 | 9.53 | 29.6/30.3 | 23.6/23.4 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.45 | 0.55 | 0.47 | 5.94 | 22.3/34.2 | 30.7/19.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.47 | 0.53 | 0.47 | 6.0 | 28.0/28.7 | 25.2/24.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.091 | 0.37 | 0.63 | 0.00 | 9.36 | 23.3/35.8 | 27.9/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Martin Necas: 1+ goals YES | 31 | 0.400 | 0.376 | +0.074 | +0.051 | $7.86 | FUNDED_RESEARCH | $2 | COL:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 32 | 0.391 | 0.372 | +0.056 | +0.037 | $5.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Montreal wins by over 1.5 goals NO | 68 | 0.749 | 0.712 | +0.054 | +0.017 | $1.15 | FUNDED_RESEARCH | $1 | COL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nazem Kadri: 1+ goals YES | 27 | 0.303 | 0.294 | +0.020 | +0.010 | $1.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
- **Martin Necas: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (25.60 vs 13.08 bp); relationships: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26NOV14COLMTL-MTL2|no: REINFORCING (phi 0.217); KXNHLGOAL-26NOV14COLMTL-COLNKADRI91-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: COL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes has the higher standalone adjusted growth (25.60 vs 13.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26NOV14COLMTL-MTL2|no: REINFORCING (phi 0.161); KXNHLGOAL-26NOV14COLMTL-COLNKADRI91-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: COL offense suppressed (<= 2 goals)
- **Montreal wins by over 1.5 goals NO** — thesis: COL wins (incl. OT/SO); alternative: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes has the higher standalone adjusted growth (25.60 vs 2.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.217); they share one thesis budget; relationships: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: REINFORCING (phi 0.217); KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: REINFORCING (phi 0.161); KXNHLGOAL-26NOV14COLMTL-COLNKADRI91-1|yes: MOSTLY_INDEPENDENT (phi 0.137); failure: MTL wins by 2+
- **Nazem Kadri: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes has the higher standalone adjusted growth (25.60 vs 1.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26NOV14COLMTL-MTL2|no: MOSTLY_INDEPENDENT (phi 0.137); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.484): highest fidelity KXNHLTEAMTOTAL-26NOV14COLMTL-COL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:WINS_BY_2PLUS (p 0.338): highest fidelity KXNHLSPREAD-26NOV14COLMTL-COL2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:WINS (p 0.5538): highest fidelity KXNHLSPREAD-26NOV14COLMTL-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3186, phi -0.309)
- KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3186, phi -0.262)
- KXNHLSPREAD-26NOV14COLMTL-MTL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.2511, phi -1.0)
- KXNHLGOAL-26NOV14COLMTL-COLNKADRI91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3186, phi -0.219)

portfolios: A EV +3.23 (adj +1.41) on $14.89, P(profit) 0.4657, adj growth 12.8 bp · B EV +2.94 (adj +1.93) on $16.16, P(profit) 0.631, adj growth 18.2 bp · C EV +2.75 (adj +1.88) on $11.98, P(profit) 0.3995, adj growth 17.1 bp · R EV +0.54 (adj +0.34) on $3.00, P(profit) 0.3995, adj growth 12.7 bp

## DET @ TBL  ·  10000 joint draws  ·  364 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_DET_win | p_overtime | goals | shots TBL/DET | TBL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.70 | 0.30 | 0.00 | 6.02 | 27.3/27.0 | 24.3/22.9 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.104 | 0.76 | 0.24 | 0.00 | 5.99 | 32.1/21.2 | 19.0/26.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.54 | 0.46 | 0.50 | 5.89 | 27.4/27.2 | 24.0/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.73 | 0.27 | 0.00 | 9.3 | 29.3/29.0 | 24.3/21.8 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.58 | 0.42 | 0.48 | 5.93 | 32.8/21.9 | 18.8/29.3 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.069 | 0.77 | 0.23 | 0.00 | 9.24 | 34.2/23.0 | 18.9/25.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Conor Geekie: 1+ goals NO | 83 | 0.880 | 0.865 | +0.040 | +0.025 | $8.99 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 2+ assists NO | 75 | 0.824 | 0.777 | +0.061 | +0.014 | $6.37 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ assists NO | 37 | 0.468 | 0.398 | +0.081 | +0.011 | $1.01 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
- **Conor Geekie: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no; why: higher confidence-adjusted growth (10.36 vs 2.41 bp); despite a smaller raw edge (+0.040 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 2+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (2.41 vs 1.19 bp); despite a smaller raw edge (+0.061 vs +0.081/contract); relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: DUPLICATIVE (phi 0.433); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no; why: second expression of the same thesis: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no has the higher standalone adjusted growth (2.41 vs 1.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.433); they share one thesis budget; relationships: KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no: DUPLICATIVE (phi 0.433); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.2911): highest fidelity KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no (same contract)
- KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4972, phi -0.151)
- KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4972, phi -0.286)
- KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.8 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4972, phi -0.31)

portfolios: A EV +1.68 (adj +0.39) on $14.89, P(profit) 0.4676, adj growth 3.5 bp · B EV +1.15 (adj +0.42) on $16.37, P(profit) 0.7275, adj growth 4.0 bp · C EV +0.94 (adj +0.22) on $11.73, P(profit) 0.8244, adj growth 2.0 bp · R EV +0.14 (adj +0.09) on $3.00, P(profit) 0.8799, adj growth 3.5 bp

## OTT @ PIT  ·  10000 joint draws  ·  416 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_OTT_win | p_overtime | goals | shots PIT/OTT | PIT/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.48 | 0.52 | 0.00 | 6.02 | 26.9/27.0 | 23.3/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.48 | 0.52 | 0.46 | 5.98 | 27.1/27.0 | 23.6/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.50 | 0.50 | 0.00 | 9.32 | 28.8/28.8 | 22.7/22.6 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.071 | 0.60 | 0.40 | 0.00 | 6.04 | 31.9/21.8 | 18.6/27.8 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.069 | 0.42 | 0.58 | 0.00 | 6.02 | 21.4/31.4 | 27.2/18.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.46 | 0.54 | 0.48 | 5.92 | 21.7/31.6 | 28.4/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 13 | 0.161 | 0.148 | +0.023 | +0.010 | $1.53 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14OTTPIT-PIT2|yes; why: higher confidence-adjusted growth (1.98 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.849 vs 0.514); alternative not eligible: confidence-adjusted EV +0.0010 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis PIT:OFFENSE_4PLUS (p 0.4004): highest fidelity KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes (same contract)
- KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3848, phi -0.193)

portfolios: A EV +0.34 (adj +0.15) on $2.00, P(profit) 0.1611, adj growth 1.4 bp · B EV +0.26 (adj +0.12) on $1.53, P(profit) 0.1611, adj growth 1.1 bp · C EV +0.32 (adj +0.14) on $1.88, P(profit) 0.1611, adj growth 1.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ WSH  ·  10000 joint draws  ·  436 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NJD_win | p_overtime | goals | shots WSH/NJD | WSH/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.53 | 0.47 | 0.00 | 6.02 | 27.5/28.1 | 24.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.47 | 5.95 | 27.8/28.3 | 25.0/24.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.095 | 0.46 | 0.54 | 0.00 | 5.98 | 22.0/33.2 | 29.4/18.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.49 | 0.51 | 0.47 | 5.91 | 22.5/33.5 | 30.2/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.55 | 0.45 | 0.00 | 9.27 | 29.3/29.7 | 24.2/22.7 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.066 | 0.47 | 0.53 | 0.00 | 9.17 | 23.6/35.1 | 28.4/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.241 | 0.218 | +0.051 | +0.028 | $4.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 11 | 0.145 | 0.130 | +0.029 | +0.013 | $1.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 24 | 0.315 | 0.268 | +0.062 | +0.015 | $2.03 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_MIXED | D |
| Nico Hischier: 1+ goals NO | 70 | 0.740 | 0.727 | +0.025 | +0.013 | $6.09 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (11.10 vs 2.55 bp); despite a smaller raw edge (+0.051 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.071); KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: WSH offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV14NJWSH-NJAGRITSYUK81-1|yes; why: higher confidence-adjusted growth (3.79 vs 0.00 bp); despite a smaller raw edge (+0.029 vs +0.035/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: NJD offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (11.10 vs 2.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.071); they share one thesis budget; relationships: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.071); KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: WSH offense suppressed (<= 2 goals)
- **Nico Hischier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14NJWSH-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (1.68 vs 1.31 bp); despite a smaller raw edge (+0.025 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3958): highest fidelity KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4001): highest fidelity KXNHLAST-26NOV14NJWSH-NJLEVANGELISTA77-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:OFFENSE_4PLUS (p 0.3768): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14NJWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3864, phi -0.242)
- KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4001, phi -0.187)
- KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3864, phi -0.263)
- KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3768, phi -0.222)

portfolios: A EV +2.92 (adj +1.11) on $14.89, P(profit) 0.5422, adj growth 10.1 bp · B EV +2.30 (adj +1.07) on $14.22, P(profit) 0.492, adj growth 9.9 bp · C EV +1.69 (adj +0.92) on $12.72, P(profit) 0.2413, adj growth 8.4 bp · R EV +0.07 (adj +0.03) on $2.00, P(profit) 0.7396, adj growth 1.3 bp

## PHI @ CBJ  ·  10000 joint draws  ·  396 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_PHI_win | p_overtime | goals | shots CBJ/PHI | CBJ/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.55 | 0.45 | 0.00 | 5.95 | 26.6/26.3 | 23.0/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.48 | 0.52 | 0.47 | 5.85 | 27.1/26.7 | 23.5/23.8 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.095 | 0.64 | 0.36 | 0.00 | 5.99 | 32.0/21.2 | 18.3/27.7 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.52 | 0.48 | 0.49 | 5.84 | 31.5/21.0 | 17.9/28.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.55 | 0.45 | 0.00 | 3.39 | 25.2/25.0 | 23.2/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.063 | 0.55 | 0.45 | 0.00 | 9.13 | 28.3/27.8 | 22.3/22.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 18 | 0.218 | 0.202 | +0.027 | +0.012 | $1.82 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Travis Konecny: 1+ assists NO | 67 | 0.742 | 0.699 | +0.057 | +0.013 | $6.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26NOV14PHICBJ-CBJ2|yes; why: higher confidence-adjusted growth (1.91 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.922 vs 0.722); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV14PHICBJ-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (1.76 vs 0.47 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.3564): highest fidelity KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes (same contract)
- thesis PHI:SUPPRESSED (p 0.4762): highest fidelity KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no (same contract)
- KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4262, phi -0.248)
- KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.306, phi -0.227)

portfolios: A EV +0.85 (adj +0.27) on $8.47, P(profit) 0.796, adj growth 2.5 bp · B EV +0.77 (adj +0.23) on $7.97, P(profit) 0.796, adj growth 2.1 bp · C EV +0.95 (adj +0.28) on $9.81, P(profit) 0.796, adj growth 2.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## FLA @ STL  ·  10000 joint draws  ·  422 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_FLA_win | p_overtime | goals | shots STL/FLA | STL/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.60 | 0.40 | 0.00 | 6.07 | 27.4/27.7 | 24.4/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.49 | 0.51 | 0.46 | 5.92 | 27.3/27.6 | 24.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.60 | 0.40 | 0.00 | 9.34 | 28.9/29.0 | 23.4/22.1 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.080 | 0.49 | 0.51 | 0.00 | 6.01 | 21.8/32.6 | 28.8/18.4 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.47 | 0.53 | 0.45 | 5.92 | 21.9/32.5 | 29.3/18.7 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.054 | 0.53 | 0.47 | 0.47 | 5.9 | 32.1/22.0 | 18.7/28.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pius Suter: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $2.91 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 30 | 0.345 | 0.332 | +0.030 | +0.018 | $3.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Sam Bennett: 1+ goals YES | 25 | 0.291 | 0.277 | +0.028 | +0.014 | $2.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (7.42 vs 3.15 bp); relationships: KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV14FLASTL-9|yes; why: higher confidence-adjusted growth (3.15 vs 1.92 bp); despite a smaller raw edge (+0.030 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.901 vs 0.37); relationships: KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: STL offense suppressed (<= 2 goals)
- **Sam Bennett: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV14FLASTL-9|yes; why: higher confidence-adjusted growth (2.09 vs 1.92 bp); despite a smaller raw edge (+0.028 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.928 vs 0.37); relationships: KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.4299): highest fidelity KXNHLTEAMTOTAL-26NOV14FLASTL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:OFFENSE_4PLUS (p 0.362): highest fidelity KXNHLTOTAL-26NOV14FLASTL-9|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2809): highest fidelity KXNHLTEAMTOTAL-26NOV14FLASTL-STL3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV14FLASTL-STL3|yes (same contract)
- KXNHLGOAL-26NOV14FLASTL-STLPSUTER22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.18)
- KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3596, phi -0.271)
- KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4104, phi -0.249)

portfolios: A EV +2.04 (adj +0.76) on $14.89, P(profit) 0.5245, adj growth 6.4 bp · B EV +1.21 (adj +0.72) on $8.39, P(profit) 0.6128, adj growth 6.7 bp · C EV +0.96 (adj +0.45) on $8.02, P(profit) 0.596, adj growth 4.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ DAL  ·  10000 joint draws  ·  414 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_BUF_win | p_overtime | goals | shots DAL/BUF | DAL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.59 | 0.41 | 0.00 | 6.02 | 26.6/26.6 | 23.4/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.50 | 0.50 | 0.47 | 5.99 | 26.5/26.5 | 23.3/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 9.28 | 27.9/27.9 | 22.5/21.4 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.081 | 0.68 | 0.32 | 0.00 | 5.99 | 31.2/20.7 | 18.1/26.8 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.55 | 0.45 | 0.46 | 5.9 | 31.7/20.9 | 17.8/28.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.61 | 0.39 | 0.00 | 3.46 | 25.1/25.2 | 23.5/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jiri Kulich: 1+ goals YES | 13 | 0.164 | 0.154 | +0.026 | +0.017 | $2.49 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Arttu Hyry: 1+ goals YES | 16 | 0.199 | 0.186 | +0.029 | +0.017 | $2.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14BUFDAL-BUFOPOWER25-1|yes; why: higher confidence-adjusted growth (4.94 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: BUF offense suppressed (<= 2 goals)
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14BUFDAL-DALTHARLEY55-2|yes; why: higher confidence-adjusted growth (4.47 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis DAL:OFFENSE_4PLUS (p 0.424): highest fidelity KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.3335): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.4516, phi -0.204)
- KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3642, phi -0.226)

portfolios: A EV +0.88 (adj +0.53) on $4.89, P(profit) 0.3322, adj growth 5.0 bp · B EV +0.94 (adj +0.57) on $5.17, P(profit) 0.3322, adj growth 5.3 bp · C EV +0.56 (adj +0.33) on $3.26, P(profit) 0.1986, adj growth 3.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ UTA  ·  10000 joint draws  ·  398 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_SJS_win | p_overtime | goals | shots UTA/SJS | UTA/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.65 | 0.35 | 0.00 | 6.01 | 28.0/27.5 | 24.6/23.8 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.111 | 0.70 | 0.30 | 0.00 | 6.07 | 33.5/22.1 | 19.5/28.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.51 | 0.49 | 0.44 | 5.87 | 28.2/27.8 | 24.5/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.69 | 0.31 | 0.00 | 9.36 | 29.6/29.1 | 24.2/22.3 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.56 | 0.44 | 0.47 | 5.92 | 33.5/22.2 | 19.1/30.0 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.082 | 0.73 | 0.27 | 0.00 | 9.38 | 35.2/23.3 | 18.9/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Clayton Keller: 1+ assists NO | 40 | 0.472 | 0.429 | +0.055 | +0.012 | $2.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
- **Clayton Keller: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV14SJUTA-UTACKELLER9-2|no; why: higher confidence-adjusted growth (1.25 vs 0.29 bp); despite a smaller raw edge (+0.055 vs +0.089/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, UTA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis UTA:SUPPRESSED (p 0.3243): highest fidelity KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no (same contract)
- KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.325)

portfolios: A EV +0.79 (adj +0.17) on $5.96, P(profit) 0.4722, adj growth 1.4 bp · B EV +0.36 (adj +0.08) on $2.70, P(profit) 0.4722, adj growth 0.7 bp · C EV +0.44 (adj +0.09) on $3.32, P(profit) 0.4722, adj growth 0.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_NYI_win | p_overtime | goals | shots ANA/NYI | ANA/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.62 | 0.38 | 0.00 | 6.07 | 27.8/27.7 | 24.7/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.121 | 0.61 | 0.39 | 0.00 | 9.5 | 29.3/28.9 | 23.2/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.51 | 0.49 | 0.43 | 6.0 | 27.7/27.5 | 24.1/24.3 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.098 | 0.67 | 0.33 | 0.00 | 6.08 | 33.1/21.9 | 19.2/28.4 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.086 | 0.68 | 0.32 | 0.00 | 9.35 | 34.6/23.2 | 18.4/26.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.54 | 0.46 | 0.48 | 6.01 | 33.1/22.1 | 18.8/29.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim wins by over 1.5 goals YES | 30 | 0.370 | 0.332 | +0.055 | +0.018 | $3.33 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26NOV14NYIANA-ANA3|yes; why: higher confidence-adjusted growth (3.17 vs 1.52 bp); relationships: only recommended bet in this game; failure: NYI wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:WINS_BY_2PLUS (p 0.3698): highest fidelity KXNHLSPREAD-26NOV14NYIANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14NYIANA-ANA2|yes (same contract)
- KXNHLSPREAD-26NOV14NYIANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:WINS (p 0.4178, phi -0.649)

portfolios: A EV +1.68 (adj +0.52) on $9.53, P(profit) 0.3698, adj growth 4.0 bp · B EV +0.58 (adj +0.19) on $3.33, P(profit) 0.3698, adj growth 1.7 bp · C EV +0.72 (adj +0.23) on $4.10, P(profit) 0.3698, adj growth 2.1 bp · R EV +0.18 (adj +0.06) on $1.00, P(profit) 0.3698, adj growth 2.1 bp

## CGY @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_CGY_win | p_overtime | goals | shots LAK/CGY | LAK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.63 | 0.37 | 0.00 | 6.0 | 28.6/28.2 | 25.3/24.4 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.107 | 0.68 | 0.32 | 0.00 | 6.0 | 33.5/22.1 | 19.4/28.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.48 | 5.85 | 28.5/28.1 | 24.7/25.2 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.56 | 0.44 | 0.45 | 5.89 | 34.1/22.6 | 19.5/30.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.63 | 0.37 | 0.00 | 9.25 | 30.1/29.7 | 24.6/23.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.59 | 0.41 | 0.00 | 3.46 | 27.3/27.0 | 25.3/25.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
