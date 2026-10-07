# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-07T14:16:45Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 140.53 | +37.38 | +11.92 | +21.56 | 0.621 | -60.43 | -77.46 | 77.30 |
| B thesis-diversified (joint) ← optimiser card | 96.24 | +18.66 | +11.20 | +6.31 | 0.601 | -41.35 | -57.99 | 95.58 |
| C best expression per thesis | 68.91 | +9.21 | +4.96 | +3.12 | 0.573 | -28.38 | -37.85 | 43.26 |
| R FUNDED research stakes | 11.00 | +3.10 | +2.09 | -0.68 | 0.196 | -6.06 | -11.00 | 0.00 |

## PIT @ WSH  ·  10000 joint draws  ·  424 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PIT_win | p_overtime | goals | shots WSH/PIT | WSH/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.46 | 0.00 | 6.05 | 27.2/27.5 | 24.1/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.49 | 5.99 | 27.3/27.7 | 24.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.112 | 0.55 | 0.45 | 0.00 | 9.43 | 28.8/29.0 | 23.0/22.2 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.081 | 0.47 | 0.53 | 0.00 | 6.01 | 21.6/32.5 | 28.7/18.4 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.49 | 0.51 | 0.46 | 5.93 | 21.9/32.6 | 29.2/18.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.065 | 0.49 | 0.51 | 0.00 | 9.44 | 23.6/34.6 | 27.8/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 12 | 0.174 | 0.159 | +0.046 | +0.032 | $8.18 | FUNDED_RESEARCH | $3 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 27 | 0.346 | 0.325 | +0.062 | +0.041 | $13.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 20 | 0.257 | 0.242 | +0.046 | +0.030 | $9.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 14 | 0.180 | 0.169 | +0.031 | +0.020 | $5.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (19.39 vs 17.72 bp); despite a smaller raw edge (+0.046 vs +0.062/contract); relationships: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT07PITWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes has the higher standalone adjusted growth (19.39 vs 17.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT07PITWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: PIT offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT07PITWSH-7|yes; why: higher confidence-adjusted growth (12.09 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.894 vs 0.676); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT07PITWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (12.09 vs 6.95 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4131): highest fidelity KXNHLSPREAD-26OCT07PITWSH-WSH2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.4538): highest fidelity KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes (same contract)
- thesis PIT:WINS (p 0.4751): highest fidelity KXNHLSPREAD-26OCT07PITWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT07PITWSH-PITSCROSBY87-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3705, phi -0.208)
- KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3705, phi -0.261)
- KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.332, phi -0.222)
- KXNHLGOAL-26OCT07PITWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.332, phi -0.187)

portfolios: A EV +13.38 (adj +2.03) on $50.00, P(profit) 0.6607, adj growth 14.7 bp · B EV +9.19 (adj +6.10) on $36.69, P(profit) 0.6753, adj growth 52.7 bp · C EV +6.18 (adj +3.89) on $30.33, P(profit) 0.3873, adj growth 33.5 bp · R EV +1.10 (adj +0.75) on $3.00, P(profit) 0.1739, adj growth 23.8 bp

## COL @ WPG  ·  10000 joint draws  ·  416 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_COL_win | p_overtime | goals | shots WPG/COL | WPG/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.42 | 0.58 | 0.00 | 6.02 | 27.7/28.4 | 24.3/24.6 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.113 | 0.38 | 0.62 | 0.00 | 6.01 | 22.1/34.2 | 29.8/19.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.46 | 5.93 | 28.0/28.7 | 25.4/24.7 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.50 | 0.50 | 0.48 | 5.92 | 22.6/34.5 | 31.1/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.44 | 0.56 | 0.00 | 9.28 | 29.4/30.2 | 23.5/23.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.077 | 0.36 | 0.64 | 0.00 | 9.35 | 23.8/36.0 | 28.7/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Josh Morrissey: 2+ goals NO | 97 | 0.995 | 0.987 | +0.022 | +0.015 | $20.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Morgan Barron: 1+ goals YES | 10 | 0.135 | 0.120 | +0.029 | +0.014 | $3.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Colorado wins by over 1.5 goals NO | 59 | 0.667 | 0.626 | +0.061 | +0.019 | $10.10 | FUNDED_RESEARCH | $3 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nazem Kadri: 1+ goals NO | 73 | 0.770 | 0.759 | +0.026 | +0.015 | $13.15 | FUNDED_RESEARCH | $4 | COL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Josh Morrissey: 2+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT07COLWPG-COL2|no: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT07COLWPG-COLNKADRI91-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: WPG offense succeeds (4+ goals)
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT07COLWPG-COL2|no; why: higher confidence-adjusted growth (4.40 vs 3.43 bp); despite a smaller raw edge (+0.029 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT07COLWPG-COL2|no: MOSTLY_INDEPENDENT (phi 0.114); KXNHLGOAL-26OCT07COLWPG-COLNKADRI91-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: WPG offense suppressed (<= 2 goals)
- **Colorado wins by over 1.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no; why: higher confidence-adjusted growth (3.43 vs 1.80 bp); relationships: KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.114); KXNHLGOAL-26OCT07COLWPG-COLNKADRI91-1|no: MOSTLY_INDEPENDENT (phi 0.141); failure: COL wins by 2+
- **Nazem Kadri: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT07COLWPG-COL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT07COLWPG-COL2|no has the higher standalone adjusted growth (3.43 vs 2.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.141); they share one thesis budget; relationships: KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT07COLWPG-COL2|no: MOSTLY_INDEPENDENT (phi 0.141); failure: COL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis WPG:OFFENSE_4PLUS (p 0.3482): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT07COLWPG-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.4464): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT07COLWPG-COL2|no (same contract)
- thesis COL:SUPPRESSED (p 0.3522): highest fidelity KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT07COLWPG-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3482, phi -0.073)
- KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4303, phi -0.171)
- KXNHLSPREAD-26OCT07COLWPG-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3325, phi -1.0)
- KXNHLGOAL-26OCT07COLWPG-COLNKADRI91-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4302, phi -0.209)

portfolios: A EV +7.16 (adj +1.27) on $50.00, P(profit) 0.5879, adj growth 8.5 bp · B EV +2.81 (adj +1.32) on $46.46, P(profit) 0.5887, adj growth 11.9 bp · C EV +1.75 (adj +0.72) on $32.92, P(profit) 0.663, adj growth 6.7 bp · R EV +0.44 (adj +0.18) on $7.00, P(profit) 0.5419, adj growth 6.0 bp

## EDM @ ANA  ·  10000 joint draws  ·  410 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_EDM_win | p_overtime | goals | shots ANA/EDM | ANA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.47 | 0.53 | 0.00 | 6.07 | 29.0/28.9 | 24.9/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.120 | 0.49 | 0.51 | 0.00 | 9.56 | 30.6/30.3 | 23.8/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.51 | 0.49 | 0.48 | 6.04 | 29.0/28.7 | 25.3/25.7 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.079 | 0.55 | 0.45 | 0.00 | 6.08 | 34.0/23.0 | 19.6/29.7 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.45 | 5.98 | 33.9/23.0 | 19.9/30.4 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.064 | 0.54 | 0.46 | 0.00 | 9.41 | 35.9/24.6 | 18.8/28.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 2+ goals YES | 1 | 0.027 | 0.023 | +0.017 | +0.012 | $2.20 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.05) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 8 | 0.116 | 0.100 | +0.031 | +0.014 | $3.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 8 | 0.114 | 0.097 | +0.029 | +0.011 | $2.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ assists YES | 27 | 0.348 | 0.301 | +0.064 | +0.018 | $4.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Alex Formenton: 2+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (27.94 vs 3.34 bp); despite a smaller raw edge (+0.017 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07EDMANA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT07EDMANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.069); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (5.74 vs 3.34 bp); despite a smaller raw edge (+0.031 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-2|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT07EDMANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: EDM offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT07EDMANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (3.68 vs 0.33 bp); despite a smaller raw edge (+0.029 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-2|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT07EDMANA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: ANA offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes; why: higher confidence-adjusted growth (3.34 vs 0.00 bp); despite a smaller raw edge (+0.064 vs +0.069/contract); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-2|yes: MOSTLY_INDEPENDENT (phi 0.069); KXNHLGOAL-26OCT07EDMANA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT07EDMANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4544): highest fidelity KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4408): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 95% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3393, phi -0.103)
- KXNHLGOAL-26OCT07EDMANA-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3393, phi -0.148)
- KXNHLGOAL-26OCT07EDMANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3436, phi -0.143)
- KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3393, phi -0.253)

portfolios: A EV +16.84 (adj +8.62) on $40.53, P(profit) 0.4997, adj growth 54.1 bp · B EV +6.66 (adj +3.78) on $13.09, P(profit) 0.4997, adj growth 31.0 bp · C EV +1.28 (adj +0.35) on $5.66, P(profit) 0.3479, adj growth 3.1 bp · R EV +1.56 (adj +1.16) on $1.00, P(profit) 0.0274, adj growth 31.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
