# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-07T15:16:44Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +34.07 | +9.06 | +29.54 | 0.662 | -47.75 | -66.24 | 69.24 |
| B thesis-diversified (joint) ← optimiser card | 107.97 | +24.30 | +14.57 | +17.04 | 0.585 | -48.09 | -60.15 | 124.15 |
| C best expression per thesis | 103.81 | +13.73 | +5.51 | +12.26 | 0.622 | -32.82 | -42.44 | 48.55 |
| R FUNDED research stakes | 9.00 | +3.25 | +2.26 | +0.39 | 0.544 | -9.00 | -9.00 | 0.00 |

## PIT @ WSH  ·  10000 joint draws  ·  424 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PIT_win | p_overtime | goals | shots WSH/PIT | WSH/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.56 | 0.44 | 0.00 | 6.05 | 27.3/27.6 | 24.2/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.45 | 5.97 | 27.2/27.6 | 24.3/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.55 | 0.45 | 0.00 | 9.36 | 28.7/29.1 | 23.2/22.1 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.079 | 0.49 | 0.51 | 0.00 | 6.08 | 21.9/32.6 | 28.7/18.5 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.52 | 0.48 | 0.49 | 5.9 | 21.9/32.3 | 29.0/18.5 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.063 | 0.49 | 0.51 | 0.00 | 9.33 | 23.5/34.6 | 27.7/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Rickard Rakell: 2+ goals YES | 4 | 0.069 | 0.062 | +0.027 | +0.019 | $4.33 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 12 | 0.168 | 0.155 | +0.041 | +0.027 | $7.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 20 | 0.258 | 0.242 | +0.047 | +0.031 | $9.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 14 | 0.183 | 0.171 | +0.035 | +0.023 | $6.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Rickard Rakell: 2+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (18.96 vs 14.45 bp); despite a smaller raw edge (+0.027 vs +0.057/contract); relationships: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT07PITWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes; why: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes has the higher standalone adjusted growth (14.45 vs 14.42 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.003); relationships: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT07PITWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PIT offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT07PITWSH-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (12.62 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT07PITWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (12.62 vs 8.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.3916): highest fidelity KXNHLAST-26OCT07PITWSH-PITECHINAKHOV59-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.4519): highest fidelity KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes (same contract)
- thesis WSH:SUPPRESSED (p 0.334): highest fidelity KXNHLPTS-26OCT07PITWSH-WSHATUCH89-1|no [DIRECT], best adjusted EV KXNHLPTS-26OCT07PITWSH-WSHATUCH89-1|no (same contract)
- KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3841, phi -0.177)
- KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3841, phi -0.207)
- KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.334, phi -0.228)
- KXNHLGOAL-26OCT07PITWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.334, phi -0.169)

portfolios: A EV +13.36 (adj +2.19) on $50.00, P(profit) 0.6563, adj growth 16.3 bp · B EV +8.64 (adj +5.91) on $27.53, P(profit) 0.5358, adj growth 50.6 bp · C EV +6.04 (adj +3.17) on $27.53, P(profit) 0.5136, adj growth 27.5 bp · R EV +1.25 (adj +0.90) on $2.00, P(profit) 0.0693, adj growth 25.9 bp

## COL @ WPG  ·  10000 joint draws  ·  416 bet sides mapped, 8 +EV candidates, 4 on card


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
| Morgan Barron: 1+ goals YES | 8 | 0.134 | 0.117 | +0.049 | +0.032 | $7.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Josh Morrissey: 2+ goals NO | 97 | 0.995 | 0.987 | +0.022 | +0.015 | $20.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Martin Necas: 1+ goals NO | 64 | 0.695 | 0.679 | +0.039 | +0.023 | $15.18 | FUNDED_RESEARCH | $4 | COL:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Colorado wins by over 1.5 goals NO | 59 | 0.667 | 0.626 | +0.061 | +0.019 | $7.32 | FUNDED_RESEARCH | $2 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT07COLWPG-COL2|no; why: higher confidence-adjusted growth (27.10 vs 3.43 bp); despite a smaller raw edge (+0.049 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLSPREAD-26OCT07COLWPG-COL2|no: MOSTLY_INDEPENDENT (phi 0.116); failure: WPG offense suppressed (<= 2 goals)
- **Josh Morrissey: 2+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT07COLWPG-COL2|no: MOSTLY_INDEPENDENT (phi -0.024); failure: WPG offense succeeds (4+ goals)
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT07COLWPG-COL2|no; why: higher confidence-adjusted growth (5.08 vs 3.43 bp); despite a smaller raw edge (+0.039 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.017 vs 0.904); relationships: KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT07COLWPG-COL2|no: REINFORCING (phi 0.153); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 1.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no; why: higher confidence-adjusted growth (3.43 vs 1.80 bp); relationships: KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.116); KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no: REINFORCING (phi 0.153); failure: COL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis COL:SUPPRESSED (p 0.3522): highest fidelity KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3482): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT07COLWPG-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.4464): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT07COLWPG-COL2|no (same contract)
- KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4303, phi -0.172)
- KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3482, phi -0.073)
- KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4302, phi -0.223)
- KXNHLSPREAD-26OCT07COLWPG-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3325, phi -1.0)

portfolios: A EV +8.91 (adj +4.44) on $50.00, P(profit) 0.5171, adj growth 34.8 bp · B EV +6.19 (adj +3.72) on $49.62, P(profit) 0.5478, adj growth 32.2 bp · C EV +2.44 (adj +1.18) on $45.90, P(profit) 0.4942, adj growth 10.7 bp · R EV +0.44 (adj +0.20) on $6.00, P(profit) 0.6953, adj growth 7.2 bp

## EDM @ ANA  ·  10000 joint draws  ·  410 bet sides mapped, 8 +EV candidates, 4 on card


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
| Alex Formenton: 2+ goals YES | 1 | 0.027 | 0.023 | +0.017 | +0.012 | $2.28 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.05) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 8 | 0.121 | 0.104 | +0.035 | +0.019 | $4.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 8 | 0.116 | 0.101 | +0.031 | +0.016 | $4.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 72 | 0.828 | 0.755 | +0.094 | +0.021 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Alex Formenton: 2+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (27.94 vs 3.34 bp); despite a smaller raw edge (+0.017 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT07EDMANA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.062); failure: EDM offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT07EDMANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (10.03 vs 2.02 bp); despite a smaller raw edge (+0.036 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-2|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT07EDMANA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.012); failure: ANA offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (6.76 vs 3.34 bp); despite a smaller raw edge (+0.031 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-2|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.13); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (4.76 vs 3.72 bp); despite a smaller raw edge (+0.094 vs +0.106/contract); relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-2|yes: INTENTIONAL_DIVERSIFIER (phi -0.062); KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT07EDMANA-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.13); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:SUPPRESSED (p 0.3393): highest fidelity KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.4544): highest fidelity KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4408): highest fidelity KXNHLAST-26OCT07EDMANA-ANAAKILLORN17-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT07EDMANA-ANAAKILLORN17-1|yes (same contract)
- KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 95% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3393, phi -0.103)
- KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3436, phi -0.168)
- KXNHLGOAL-26OCT07EDMANA-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3393, phi -0.148)
- KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.3 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4544, phi -0.307)

portfolios: A EV +11.80 (adj +2.43) on $50.00, P(profit) 0.7132, adj growth 18.1 bp · B EV +9.47 (adj +4.94) on $30.82, P(profit) 0.2451, adj growth 41.4 bp · C EV +5.25 (adj +1.16) on $30.38, P(profit) 0.4929, adj growth 10.3 bp · R EV +1.56 (adj +1.16) on $1.00, P(profit) 0.0274, adj growth 31.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
