# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-01T10:55:06Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +18.01 | +6.55 | +17.20 | 0.608 | -48.02 | -65.69 | 51.49 |
| B thesis-diversified (joint) ← optimiser card | 114.06 | +23.51 | +12.83 | +15.93 | 0.607 | -45.88 | -59.58 | 110.47 |
| C best expression per thesis | 112.49 | +18.25 | +9.54 | +11.87 | 0.573 | -39.99 | -51.27 | 82.67 |
| R FUNDED research stakes | 25.00 | +3.82 | +1.84 | +0.93 | 0.582 | -10.88 | -12.92 | 0.00 |

## WPG @ CAR  ·  10000 joint draws  ·  414 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WPG_win | p_overtime | goals | shots CAR/WPG | CAR/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.168 | 0.74 | 0.26 | 0.00 | 6.01 | 33.8/20.8 | 18.4/29.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.138 | 0.57 | 0.43 | 0.45 | 5.92 | 33.8/21.0 | 17.8/30.4 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.118 | 0.76 | 0.24 | 0.00 | 9.33 | 35.5/22.3 | 18.0/26.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.092 | 0.66 | 0.34 | 0.00 | 6.02 | 27.6/26.5 | 23.6/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.52 | 0.48 | 0.47 | 5.97 | 27.6/26.5 | 23.2/24.2 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.074 | 0.71 | 0.29 | 0.00 | 3.45 | 32.2/19.7 | 18.5/29.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Winnipeg over 3.5 goals scored YES | 23 | 0.301 | 0.263 | +0.059 | +0.021 | $3.79 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Alex Iafallo: 1+ goals YES | 11 | 0.146 | 0.131 | +0.029 | +0.014 | $2.95 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 65 | 0.716 | 0.680 | +0.050 | +0.015 | $5.65 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mark Scheifele: 1+ goals YES | 27 | 0.308 | 0.296 | +0.025 | +0.013 | $2.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
- **Winnipeg over 3.5 goals scored YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG5|yes; why: higher confidence-adjusted growth (5.09 vs 3.06 bp); wins across more scripts (relative breadth 0.842 vs 0.62); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: REINFORCING (phi 0.184); KXNHLSPREAD-26NOV01WPGCAR-CAR3|no: REINFORCING (phi 0.336); KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes: REINFORCING (phi 0.267); failure: WPG offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes has the higher standalone adjusted growth (5.09 vs 4.13 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.184); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes: REINFORCING (phi 0.184); KXNHLSPREAD-26NOV01WPGCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.099); KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: WPG offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV01WPGCAR-CAR2|no; why: higher confidence-adjusted growth (2.08 vs 1.60 bp); wins across more scripts (relative breadth 1.021 vs 0.857); relationships: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes: REINFORCING (phi 0.336); KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.099); KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes: REINFORCING (phi 0.159); failure: CAR wins by 2+
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes has the higher standalone adjusted growth (5.09 vs 1.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.267); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes: REINFORCING (phi 0.267); KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26NOV01WPGCAR-CAR3|no: REINFORCING (phi 0.159); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis WPG:OFFENSE_4PLUS (p 0.2935): highest fidelity KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes (same contract)
- thesis WPG:WINS (p 0.3601): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4137): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01WPGCAR-CAR3|no (same contract)
- KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:SUPPRESSED (p 0.4925, phi -0.647)
- KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4925, phi -0.182)
- KXNHLSPREAD-26NOV01WPGCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.4131, phi -0.751)
- KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4925, phi -0.284)

portfolios: A EV +4.20 (adj +1.31) on $35.28, P(profit) 0.5638, adj growth 9.2 bp · B EV +2.31 (adj +0.91) on $14.93, P(profit) 0.4754, adj growth 8.0 bp · C EV +1.82 (adj +0.61) on $12.11, P(profit) 0.3013, adj growth 5.3 bp · R EV +0.64 (adj +0.25) on $4.00, P(profit) 0.3737, adj growth 8.5 bp

## MIN @ WSH  ·  10000 joint draws  ·  416 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_MIN_win | p_overtime | goals | shots WSH/MIN | WSH/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 6.06 | 28.5/28.4 | 25.1/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.46 | 5.96 | 28.3/28.6 | 25.4/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.58 | 0.42 | 0.00 | 9.3 | 29.7/29.7 | 23.9/23.4 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.078 | 0.53 | 0.47 | 0.00 | 6.01 | 22.8/33.5 | 29.9/19.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.49 | 0.51 | 0.46 | 5.84 | 22.2/33.0 | 29.6/19.0 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.058 | 0.59 | 0.41 | 0.00 | 6.02 | 33.4/22.9 | 19.8/29.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 19 | 0.248 | 0.225 | +0.048 | +0.024 | $6.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 57 | 0.634 | 0.615 | +0.046 | +0.028 | $17.19 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.79) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.134 | 0.119 | +0.028 | +0.013 | $3.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV01MINWSH-MIN3|no; why: higher confidence-adjusted growth (7.90 vs 0.24 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0040 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: WSH offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV01MINWSH-MIN3|no; why: higher confidence-adjusted growth (7.11 vs 0.24 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0040 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: MIN offense succeeds (4+ goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (3.77 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4163): highest fidelity KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.425): highest fidelity KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.3542): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3634, phi -0.246)
- KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3542, phi -0.277)
- KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.425, phi -0.176)

portfolios: A EV +5.01 (adj +2.60) on $30.05, P(profit) 0.3489, adj growth 21.3 bp · B EV +3.84 (adj +2.05) on $27.36, P(profit) 0.762, adj growth 17.8 bp · C EV +2.98 (adj +1.65) on $23.94, P(profit) 0.7228, adj growth 14.4 bp · R EV +0.40 (adj +0.24) on $5.00, P(profit) 0.6336, adj growth 8.2 bp

## UTA @ PHI  ·  10000 joint draws  ·  404 bet sides mapped, 20 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_UTA_win | p_overtime | goals | shots PHI/UTA | PHI/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.51 | 0.49 | 0.00 | 6.0 | 26.6/26.9 | 23.4/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.47 | 5.93 | 26.4/26.9 | 23.7/23.2 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.093 | 0.44 | 0.56 | 0.00 | 5.98 | 21.1/31.7 | 27.7/18.0 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.44 | 0.56 | 0.45 | 5.88 | 21.1/31.8 | 28.4/18.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.50 | 0.50 | 0.00 | 9.15 | 27.9/28.2 | 22.2/21.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.53 | 0.47 | 0.00 | 3.47 | 25.0/25.1 | 23.2/23.0 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Noah Cates: 1+ goals YES | 11 | 0.178 | 0.153 | +0.061 | +0.037 | $8.58 | FUNDED_RESEARCH | $3 | PHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 12 | 0.181 | 0.165 | +0.054 | +0.037 | $9.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Travis Sanheim: 1+ goals YES | 8 | 0.134 | 0.113 | +0.049 | +0.028 | $5.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Cam York: 1+ goals YES | 6 | 0.093 | 0.084 | +0.029 | +0.020 | $4.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
- **Noah Cates: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (27.48 vs 26.54 bp); relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV01UTAPHI-PHICYORK8-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: PHI offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes has the higher standalone adjusted growth (27.48 vs 26.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.019); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV01UTAPHI-PHICYORK8-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: PHI offense suppressed (<= 2 goals)
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes has the higher standalone adjusted growth (27.48 vs 20.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV01UTAPHI-PHICYORK8-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: PHI offense suppressed (<= 2 goals)
- **Cam York: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes has the higher standalone adjusted growth (27.48 vs 13.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.3669): highest fidelity KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2802): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.5009): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01UTAPHI-UTA3|no (same contract)
- KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4142, phi -0.207)
- KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4142, phi -0.21)
- KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4142, phi -0.169)
- KXNHLGOAL-26NOV01UTAPHI-PHICYORK8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4142, phi -0.152)

portfolios: A EV +3.84 (adj +1.12) on $35.28, P(profit) 0.7027, adj growth 9.7 bp · B EV +13.74 (adj +8.64) on $28.08, P(profit) 0.4662, adj growth 73.7 bp · C EV +11.25 (adj +6.53) on $42.75, P(profit) 0.4069, adj growth 56.1 bp · R EV +1.57 (adj +0.94) on $3.00, P(profit) 0.1779, adj growth 30.1 bp

## EDM @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_EDM_win | p_overtime | goals | shots NYR/EDM | NYR/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.48 | 0.52 | 0.00 | 6.07 | 27.2/27.4 | 23.6/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.52 | 0.48 | 0.45 | 5.99 | 27.1/27.5 | 24.2/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.47 | 0.53 | 0.00 | 9.53 | 28.7/29.1 | 22.8/22.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.096 | 0.41 | 0.59 | 0.00 | 6.05 | 21.4/32.6 | 28.4/18.4 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.46 | 0.54 | 0.47 | 5.96 | 21.8/33.0 | 29.6/18.7 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.079 | 0.40 | 0.60 | 0.00 | 9.47 | 23.2/34.6 | 27.3/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York R wins by over 2.5 goals NO | 78 | 0.830 | 0.802 | +0.037 | +0.010 | $13.69 | FUNDED_RESEARCH | $4 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New York R wins by over 2.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM4|yes; why: higher confidence-adjusted growth (1.40 vs 0.81 bp); despite a smaller raw edge (+0.037 vs +0.046/contract); wins across more scripts (relative breadth 1.028 vs 0.732); alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: NYR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis EDM:WINS (p 0.5223): highest fidelity KXNHLSPREAD-26NOV01EDMNYR-NYR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01EDMNYR-NYR3|no (same contract)
- KXNHLSPREAD-26NOV01EDMNYR-NYR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.2699, phi -0.746)

portfolios: A EV +0.67 (adj +0.18) on $14.11, P(profit) 0.8295, adj growth 1.6 bp · B EV +0.65 (adj +0.18) on $13.69, P(profit) 0.8295, adj growth 1.6 bp · C EV +0.65 (adj +0.18) on $13.69, P(profit) 0.8295, adj growth 1.6 bp · R EV +0.19 (adj +0.05) on $4.00, P(profit) 0.8295, adj growth 1.8 bp

## OTT @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_OTT_win | p_overtime | goals | shots ANA/OTT | ANA/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.61 | 0.39 | 0.00 | 6.05 | 27.5/27.4 | 24.5/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.48 | 6.04 | 27.5/27.4 | 24.0/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.61 | 0.39 | 0.00 | 9.44 | 29.0/29.2 | 23.6/22.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.076 | 0.65 | 0.35 | 0.00 | 6.01 | 32.3/21.8 | 19.0/27.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.58 | 0.42 | 0.49 | 5.94 | 32.9/22.0 | 18.8/29.4 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.060 | 0.71 | 0.29 | 0.00 | 9.4 | 33.8/23.1 | 18.5/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ottawa wins by over 2.5 goals NO | 79 | 0.864 | 0.825 | +0.062 | +0.023 | $18.71 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa wins by over 1.5 goals NO | 69 | 0.773 | 0.729 | +0.068 | +0.024 | $7.97 | FUNDED_RESEARCH | $2 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 1.5 goals YES | 29 | 0.359 | 0.322 | +0.054 | +0.018 | $1.55 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa over 1.5 goals scored NO | 15 | 0.201 | 0.173 | +0.042 | +0.014 | $1.77 | FUNDED_RESEARCH | $1 | OTT:SUPPRESSED | FRAGILE (0.49) | EVIDENCE_MIXED | D |
- **Ottawa wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT2|no; why: higher confidence-adjusted growth (7.25 vs 6.16 bp); despite a smaller raw edge (+0.062 vs +0.068/contract); relationships: KXNHLSPREAD-26NOV01OTTANA-OTT2|no: DUPLICATIVE (phi 0.733); KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: REINFORCING (phi 0.297); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no: REINFORCING (phi 0.199); failure: OTT wins by 2+
- **Ottawa wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV01OTTANA-OTT3|no has the higher standalone adjusted growth (7.25 vs 6.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.733); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: DUPLICATIVE (phi 0.733); KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: DUPLICATIVE (phi 0.405); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no: REINFORCING (phi 0.271); failure: OTT wins by 2+
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV01OTTANA-OTT3|no has the higher standalone adjusted growth (7.25 vs 3.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.297); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.297); KXNHLSPREAD-26NOV01OTTANA-OTT2|no: DUPLICATIVE (phi 0.405); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no: REINFORCING (phi 0.438); failure: OTT wins (incl. OT/SO)
- **Ottawa over 1.5 goals scored NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV01OTTANA-OTT3|no has the higher standalone adjusted growth (7.25 vs 3.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.199); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.199); KXNHLSPREAD-26NOV01OTTANA-OTT2|no: REINFORCING (phi 0.271); KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: REINFORCING (phi 0.438); failure: OTT wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:WINS (p 0.5761): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT2|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3588): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT2|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4107): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT2|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no kept
- KXNHLSPREAD-26NOV01OTTANA-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2268, phi -0.733)
- KXNHLSPREAD-26NOV01OTTANA-OTT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2268, phi -1.0)
- KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS (p 0.4239, phi -0.642)
- KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no: FUNDED_RESEARCH; family MIXED; loses 51% of the draws where the thesis happens; opposing: failure thesis OTT:WINS (p 0.4239, phi -0.406)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no kept

portfolios: A EV +4.29 (adj +1.34) on $35.28, P(profit) 0.4954, adj growth 9.7 bp · B EV +2.97 (adj +1.05) on $30.00, P(profit) 0.7732, adj growth 9.4 bp · C EV +1.55 (adj +0.57) on $20.00, P(profit) 0.8639, adj growth 5.3 bp · R EV +1.02 (adj +0.36) on $9.00, P(profit) 0.7732, adj growth 11.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
