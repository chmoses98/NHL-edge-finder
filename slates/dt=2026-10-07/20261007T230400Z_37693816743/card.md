# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-07T23:04:00Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +40.54 | +7.22 | +41.95 | 0.784 | -27.15 | -45.59 | 59.10 |
| B thesis-diversified (joint) ← optimiser card | 135.50 | +42.96 | +26.86 | +33.06 | 0.662 | -64.40 | -90.93 | 230.36 |
| C best expression per thesis | 138.16 | +34.90 | +17.44 | +28.34 | 0.633 | -45.67 | -51.40 | 151.85 |
| R FUNDED research stakes | 13.00 | +3.94 | +2.76 | -6.28 | 0.486 | -13.00 | -13.00 | 0.00 |

## PIT @ WSH  ·  10000 joint draws  ·  426 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.591 / away 0.409

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PIT_win | p_overtime | goals | shots WSH/PIT | WSH/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.58 | 0.42 | 0.00 | 6.06 | 27.3/27.6 | 24.4/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.59 | 0.41 | 0.00 | 9.39 | 28.6/28.8 | 23.0/21.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.54 | 0.46 | 0.47 | 5.95 | 27.3/27.7 | 24.4/24.0 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.45 | 0.55 | 0.50 | 5.99 | 22.0/32.8 | 29.3/18.7 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.076 | 0.51 | 0.49 | 0.00 | 6.04 | 21.8/32.6 | 28.8/18.4 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.069 | 0.48 | 0.52 | 0.00 | 9.42 | 23.2/34.4 | 27.7/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Rickard Rakell: 1+ goals YES | 27 | 0.350 | 0.329 | +0.067 | +0.045 | $15.06 | FUNDED_RESEARCH | $4 | PIT:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 20 | 0.265 | 0.248 | +0.054 | +0.036 | $10.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 12 | 0.170 | 0.156 | +0.043 | +0.029 | $7.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 18 | 0.237 | 0.221 | +0.047 | +0.031 | $9.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-2|yes; why: higher confidence-adjusted growth (21.80 vs 18.01 bp); wins across more scripts (relative breadth 0.9 vs 0.769); relationships: KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT07PITWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: PIT offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (17.12 vs 13.53 bp); relationships: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT07PITWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: WSH offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes has the higher standalone adjusted growth (21.80 vs 16.02 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT07PITWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: PIT offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (17.12 vs 13.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.396): highest fidelity KXNHLAST-26OCT07PITWSH-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.4622): highest fidelity KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes (same contract)
- thesis PIT:NET_LOW_VOLUME (p 0.4447): highest fidelity KXNHLSAVE-26OCT07PITWSH-PITASILOVS37-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT07PITWSH-PITASILOVS37-27|no (same contract)
- KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3843, phi -0.27)
- KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3232, phi -0.231)
- KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3843, phi -0.206)
- KXNHLGOAL-26OCT07PITWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3232, phi -0.196)

portfolios: A EV +13.13 (adj +2.63) on $50.00, P(profit) 0.6669, adj growth 22.4 bp · B EV +11.03 (adj +7.45) on $42.48, P(profit) 0.702, adj growth 64.3 bp · C EV +8.88 (adj +4.37) on $50.00, P(profit) 0.5233, adj growth 39.0 bp · R EV +0.94 (adj +0.64) on $4.00, P(profit) 0.3504, adj growth 21.9 bp

## COL @ WPG  ·  10000 joint draws  ·  418 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.369 / away 0.631

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_COL_win | p_overtime | goals | shots WPG/COL | WPG/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.41 | 0.58 | 0.00 | 6.04 | 28.2/28.7 | 24.7/24.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.114 | 0.36 | 0.64 | 0.00 | 5.98 | 22.0/33.9 | 29.4/19.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.49 | 0.51 | 0.46 | 5.95 | 27.9/28.6 | 25.3/24.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.45 | 0.55 | 0.47 | 5.9 | 22.4/34.4 | 30.8/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.44 | 0.56 | 0.00 | 9.3 | 29.3/30.1 | 23.6/23.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.080 | 0.33 | 0.67 | 0.00 | 9.28 | 23.6/36.1 | 28.3/18.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Iafallo: 1+ goals YES | 12 | 0.173 | 0.159 | +0.046 | +0.031 | $8.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Morgan Barron: 1+ goals YES | 10 | 0.138 | 0.127 | +0.032 | +0.021 | $5.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Nazem Kadri: 1+ goals NO | 73 | 0.784 | 0.770 | +0.041 | +0.026 | $17.19 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 58 | 0.637 | 0.622 | +0.040 | +0.025 | $12.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT07COLWPG-COL3|no; why: higher confidence-adjusted growth (18.94 vs 3.12 bp); despite a smaller raw edge (+0.046 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT07COLWPG-COLNKADRI91-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: WPG offense suppressed (<= 2 goals)
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT07COLWPG-COL3|no; why: higher confidence-adjusted growth (9.76 vs 3.12 bp); despite a smaller raw edge (+0.032 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07COLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT07COLWPG-COLNKADRI91-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: WPG offense suppressed (<= 2 goals)
- **Nazem Kadri: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT07COLWPG-COLCMAKAR8-2|no; why: higher confidence-adjusted growth (7.72 vs 6.64 bp); despite a smaller raw edge (+0.041 vs +0.103/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07COLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.018); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT07COLWPG-COLCMAKAR8-2|no; why: KXNHLAST-26OCT07COLWPG-COLCMAKAR8-2|no has the higher standalone adjusted growth (6.64 vs 5.55 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.145); relationships: KXNHLGOAL-26OCT07COLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT07COLWPG-COLNKADRI91-1|no: MOSTLY_INDEPENDENT (phi -0.018); failure: COL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:SUPPRESSED (p 0.3468): highest fidelity KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.4356): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL2|no [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3515): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT07COLWPG-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT07COLWPG-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4297, phi -0.193)
- KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4297, phi -0.181)
- KXNHLGOAL-26OCT07COLWPG-COLNKADRI91-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4465, phi -0.187)
- KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4465, phi -0.267)

portfolios: A EV +14.38 (adj +1.91) on $50.00, P(profit) 0.6434, adj growth 14.1 bp · B EV +6.32 (adj +4.18) on $43.46, P(profit) 0.64, adj growth 36.4 bp · C EV +6.28 (adj +1.20) on $40.20, P(profit) 0.6588, adj growth 10.9 bp · R EV +0.27 (adj +0.17) on $5.00, P(profit) 0.7845, adj growth 6.3 bp

## EDM @ ANA  ·  10000 joint draws  ·  408 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.452 / away 0.548

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_EDM_win | p_overtime | goals | shots ANA/EDM | ANA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.49 | 0.51 | 0.00 | 6.09 | 29.0/28.8 | 25.1/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.116 | 0.51 | 0.49 | 0.00 | 9.53 | 31.0/30.8 | 24.6/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.47 | 0.53 | 0.48 | 6.02 | 28.8/28.7 | 25.2/25.5 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.079 | 0.55 | 0.45 | 0.00 | 6.07 | 34.1/22.9 | 19.8/29.9 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.068 | 0.54 | 0.46 | 0.00 | 9.41 | 35.5/24.7 | 18.9/28.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.50 | 0.50 | 0.45 | 5.95 | 34.1/23.2 | 19.9/30.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 12 | 0.214 | 0.190 | +0.087 | +0.062 | $15.80 | FUNDED_RESEARCH | $4 | EDM:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 7 | 0.119 | 0.106 | +0.045 | +0.031 | $7.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| A.J. Greer: 1+ goals YES | 17 | 0.246 | 0.224 | +0.066 | +0.044 | $12.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 33 | 0.491 | 0.383 | +0.146 | +0.038 | $14.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT07EDMANA-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (72.37 vs 0.65 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.086); failure: EDM offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (29.48 vs 28.78 bp); despite a smaller raw edge (+0.045 vs +0.066/contract); relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: ANA offense suppressed (<= 2 goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT07EDMANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (28.78 vs 6.61 bp); despite a smaller raw edge (+0.066 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: ANA offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-2|no; why: KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (17.57 vs 13.66 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.426); relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.086); KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4508): highest fidelity KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4403): highest fidelity KXNHLAST-26OCT07EDMANA-ANAAKILLORN17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3356): highest fidelity KXNHLAST-26OCT07EDMANA-EDMLDRAISAITL29-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3356, phi -0.199)
- KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3474, phi -0.138)
- KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3474, phi -0.228)
- KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.6 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4508, phi -0.304)

portfolios: A EV +13.02 (adj +2.68) on $50.00, P(profit) 0.6839, adj growth 22.6 bp · B EV +25.61 (adj +15.23) on $49.56, P(profit) 0.4801, adj growth 129.6 bp · C EV +19.74 (adj +11.87) on $47.96, P(profit) 0.4092, adj growth 102.0 bp · R EV +2.73 (adj +1.95) on $4.00, P(profit) 0.2143, adj growth 65.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
