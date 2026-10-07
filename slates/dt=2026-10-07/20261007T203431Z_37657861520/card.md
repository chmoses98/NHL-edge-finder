# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-07T20:34:31Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +48.82 | +14.28 | +48.17 | 0.748 | -42.94 | -62.06 | 117.65 |
| B thesis-diversified (joint) ← optimiser card | 126.38 | +38.20 | +25.79 | +33.46 | 0.617 | -63.82 | -94.96 | 220.73 |
| C best expression per thesis | 123.20 | +31.79 | +19.04 | +21.31 | 0.638 | -48.48 | -68.55 | 163.39 |
| R FUNDED research stakes | 16.00 | +4.32 | +2.92 | -3.48 | 0.455 | -11.86 | -16.00 | 0.00 |

## PIT @ WSH  ·  10000 joint draws  ·  426 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.593 / away 0.407

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
| Rickard Rakell: 1+ goals YES | 27 | 0.350 | 0.329 | +0.067 | +0.045 | $14.91 | FUNDED_RESEARCH | $4 | PIT:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 20 | 0.265 | 0.248 | +0.054 | +0.036 | $11.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 12 | 0.170 | 0.156 | +0.043 | +0.029 | $7.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 9 | 0.130 | 0.119 | +0.035 | +0.023 | $5.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (21.80 vs 16.02 bp); relationships: KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT07PITWSH-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PIT offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (17.12 vs 7.23 bp); relationships: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT07PITWSH-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.024); failure: WSH offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes has the higher standalone adjusted growth (21.80 vs 16.02 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT07PITWSH-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes has the higher standalone adjusted growth (21.80 vs 13.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.396): highest fidelity KXNHLAST-26OCT07PITWSH-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.4622): highest fidelity KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes (same contract)
- thesis WSH:SUPPRESSED (p 0.3232): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3843, phi -0.27)
- KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3232, phi -0.231)
- KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3843, phi -0.206)
- KXNHLGOAL-26OCT07PITWSH-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3843, phi -0.172)

portfolios: A EV +13.35 (adj +4.27) on $50.00, P(profit) 0.5477, adj growth 36.3 bp · B EV +10.90 (adj +7.37) on $39.17, P(profit) 0.6576, adj growth 63.6 bp · C EV +7.22 (adj +4.53) on $46.19, P(profit) 0.5251, adj growth 39.5 bp · R EV +0.94 (adj +0.64) on $4.00, P(profit) 0.3504, adj growth 21.9 bp

## COL @ WPG  ·  10000 joint draws  ·  418 bet sides mapped, 25 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.364 / away 0.636

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_COL_win | p_overtime | goals | shots WPG/COL | WPG/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.117 | 0.35 | 0.65 | 0.00 | 5.99 | 22.1/34.0 | 29.6/19.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.43 | 0.57 | 0.00 | 6.03 | 27.8/28.4 | 24.5/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.50 | 0.50 | 0.47 | 5.98 | 28.1/28.7 | 25.2/24.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.46 | 0.54 | 0.47 | 5.93 | 22.4/34.6 | 31.1/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.42 | 0.58 | 0.00 | 9.28 | 29.3/30.0 | 23.6/23.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.079 | 0.35 | 0.65 | 0.00 | 9.17 | 23.4/35.9 | 28.0/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 1+ goals NO | 58 | 0.652 | 0.632 | +0.055 | +0.035 | $18.59 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 13 | 0.174 | 0.162 | +0.036 | +0.024 | $6.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 71 | 0.784 | 0.744 | +0.059 | +0.020 | $10.35 | FUNDED_RESEARCH | $3 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Martin Necas: 1+ goals NO | 65 | 0.699 | 0.684 | +0.033 | +0.018 | $11.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (10.97 vs 4.68 bp); despite a smaller raw edge (+0.055 vs +0.129/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT07COLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26OCT07COLWPG-COL3|no: REINFORCING (phi 0.188); KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: COL offense succeeds (4+ goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT07COLWPG-COL3|no; why: higher confidence-adjusted growth (10.53 vs 4.36 bp); despite a smaller raw edge (+0.036 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26OCT07COLWPG-COL3|no: MOSTLY_INDEPENDENT (phi 0.093); KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: WPG offense suppressed (<= 2 goals)
- **Colorado wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no has the higher standalone adjusted growth (10.97 vs 4.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.188); they share one thesis budget; relationships: KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no: REINFORCING (phi 0.188); KXNHLGOAL-26OCT07COLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.093); KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no: REINFORCING (phi 0.15); failure: COL wins by 2+
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no has the higher standalone adjusted growth (10.97 vs 3.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT07COLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT07COLWPG-COL3|no: REINFORCING (phi 0.15); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:SUPPRESSED (p 0.3497): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.4436): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3439): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT07COLWPG-COL3|no (same contract)
- KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4356, phi -0.28)
- KXNHLGOAL-26OCT07COLWPG-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.426, phi -0.194)
- KXNHLSPREAD-26OCT07COLWPG-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3354, phi -0.74)
- KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4356, phi -0.245)

portfolios: A EV +17.80 (adj +2.46) on $50.00, P(profit) 0.7321, adj growth 16.2 bp · B EV +4.80 (adj +2.78) on $46.65, P(profit) 0.5428, adj growth 24.4 bp · C EV +3.02 (adj +1.55) on $34.39, P(profit) 0.5481, adj growth 13.7 bp · R EV +0.71 (adj +0.37) on $8.00, P(profit) 0.6523, adj growth 13.2 bp

## EDM @ ANA  ·  10000 joint draws  ·  414 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.454 / away 0.546

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
| Alex Formenton: 1+ goals YES | 12 | 0.212 | 0.188 | +0.085 | +0.061 | $14.68 | FUNDED_RESEARCH | $4 | EDM:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| A.J. Greer: 1+ goals YES | 16 | 0.246 | 0.223 | +0.076 | +0.054 | $14.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 7 | 0.119 | 0.103 | +0.045 | +0.029 | $6.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 7 | 0.110 | 0.099 | +0.035 | +0.024 | $5.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (69.32 vs 3.06 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT07EDMANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: EDM offense suppressed (<= 2 goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT07EDMANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (43.66 vs 6.61 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT07EDMANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (43.66 vs 25.02 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT07EDMANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (43.66 vs 17.60 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4508): highest fidelity KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:OFFENSE_4PLUS (p 0.4403): highest fidelity KXNHLAST-26OCT07EDMANA-ANAAKILLORN17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3356): highest fidelity KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3356, phi -0.205)
- KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3474, phi -0.228)
- KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3474, phi -0.138)
- KXNHLGOAL-26OCT07EDMANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3474, phi -0.139)

portfolios: A EV +17.68 (adj +7.55) on $50.00, P(profit) 0.6175, adj growth 65.2 bp · B EV +22.50 (adj +15.64) on $40.56, P(profit) 0.5334, adj growth 132.7 bp · C EV +21.55 (adj +12.96) on $42.62, P(profit) 0.4064, adj growth 110.3 bp · R EV +2.67 (adj +1.91) on $4.00, P(profit) 0.2125, adj growth 63.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
