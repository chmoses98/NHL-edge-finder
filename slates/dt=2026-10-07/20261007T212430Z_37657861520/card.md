# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-07T21:24:30Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +52.10 | +13.68 | +49.88 | 0.761 | -36.50 | -56.41 | 113.65 |
| B thesis-diversified (joint) ← optimiser card | 126.28 | +39.66 | +26.97 | +35.30 | 0.622 | -67.17 | -92.78 | 230.60 |
| C best expression per thesis | 122.94 | +38.64 | +20.33 | +26.37 | 0.682 | -52.82 | -70.22 | 174.44 |
| R FUNDED research stakes | 16.00 | +4.33 | +2.93 | -3.48 | 0.456 | -11.86 | -16.00 | 0.00 |

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
- thesis PIT:NET_LOW_VOLUME (p 0.4447): highest fidelity KXNHLSAVE-26OCT07PITWSH-PITASILOVS37-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT07PITWSH-PITASILOVS37-27|no (same contract)
- KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3843, phi -0.27)
- KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3232, phi -0.231)
- KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3843, phi -0.206)
- KXNHLGOAL-26OCT07PITWSH-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3843, phi -0.172)

portfolios: A EV +14.84 (adj +2.91) on $50.00, P(profit) 0.6669, adj growth 25.0 bp · B EV +10.90 (adj +7.37) on $39.17, P(profit) 0.6576, adj growth 63.6 bp · C EV +12.63 (adj +5.18) on $43.78, P(profit) 0.5251, adj growth 45.0 bp · R EV +0.94 (adj +0.64) on $4.00, P(profit) 0.3504, adj growth 21.9 bp

## COL @ WPG  ·  10000 joint draws  ·  418 bet sides mapped, 26 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.368 / away 0.632

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
| Alex Iafallo: 1+ goals YES | 12 | 0.174 | 0.160 | +0.047 | +0.032 | $8.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 58 | 0.652 | 0.632 | +0.055 | +0.035 | $20.00 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 71 | 0.784 | 0.744 | +0.059 | +0.020 | $9.66 | FUNDED_RESEARCH | $3 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Martin Necas: 1+ goals NO | 66 | 0.699 | 0.688 | +0.023 | +0.012 | $8.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT07COLWPG-COL3|no; why: higher confidence-adjusted growth (19.85 vs 4.36 bp); despite a smaller raw edge (+0.047 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26OCT07COLWPG-COL3|no: MOSTLY_INDEPENDENT (phi 0.093); KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: WPG offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT07COLWPG-COLCMAKAR8-2|no; why: higher confidence-adjusted growth (10.97 vs 6.32 bp); despite a smaller raw edge (+0.055 vs +0.101/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07COLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26OCT07COLWPG-COL3|no: REINFORCING (phi 0.188); KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no has the higher standalone adjusted growth (10.97 vs 4.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.188); they share one thesis budget; relationships: KXNHLGOAL-26OCT07COLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.093); KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no: REINFORCING (phi 0.188); KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no: REINFORCING (phi 0.15); failure: COL wins by 2+
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no; why: Player prop expression KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no selected over player prop KXNHLPTS-26OCT07COLWPG-COLCMAKAR8-2|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.85 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT07COLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT07COLWPG-COL3|no: REINFORCING (phi 0.15); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:SUPPRESSED (p 0.3497): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no — Player prop expression KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no selected over player prop KXNHLPTS-26OCT07COLWPG-COLCMAKAR8-2|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.85 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)
- thesis WPG:WINS (p 0.4436): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3439): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT07COLWPG-COL3|no (same contract)
- KXNHLGOAL-26OCT07COLWPG-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.426, phi -0.194)
- KXNHLGOAL-26OCT07COLWPG-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4356, phi -0.28)
- KXNHLSPREAD-26OCT07COLWPG-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3354, phi -0.74)
- KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4356, phi -0.245)
- override: Player prop expression KXNHLGOAL-26OCT07COLWPG-COLMNECAS88-1|no selected over player prop KXNHLPTS-26OCT07COLWPG-COLCMAKAR8-2|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.85 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +18.09 (adj +2.61) on $50.00, P(profit) 0.7321, adj growth 17.6 bp · B EV +5.95 (adj +3.65) on $46.16, P(profit) 0.6194, adj growth 31.6 bp · C EV +3.02 (adj +1.55) on $34.39, P(profit) 0.5481, adj growth 13.7 bp · R EV +0.71 (adj +0.37) on $8.00, P(profit) 0.6523, adj growth 13.2 bp

## EDM @ ANA  ·  10000 joint draws  ·  408 bet sides mapped, 15 +EV candidates, 4 on card

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
| Alex Formenton: 1+ goals YES | 12 | 0.213 | 0.189 | +0.086 | +0.061 | $14.75 | FUNDED_RESEARCH | $4 | EDM:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| A.J. Greer: 1+ goals YES | 16 | 0.246 | 0.223 | +0.076 | +0.054 | $14.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 7 | 0.119 | 0.104 | +0.045 | +0.030 | $6.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 7 | 0.110 | 0.099 | +0.035 | +0.024 | $5.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (70.16 vs 0.95 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT07EDMANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: EDM offense suppressed (<= 2 goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT07EDMANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (43.66 vs 6.61 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT07EDMANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (43.66 vs 27.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT07EDMANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (43.66 vs 17.60 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4508): highest fidelity KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4403): highest fidelity KXNHLAST-26OCT07EDMANA-ANAAKILLORN17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3356): highest fidelity KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT07EDMANA-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3356, phi -0.21)
- KXNHLGOAL-26OCT07EDMANA-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3474, phi -0.228)
- KXNHLGOAL-26OCT07EDMANA-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3474, phi -0.138)
- KXNHLGOAL-26OCT07EDMANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3474, phi -0.139)

portfolios: A EV +19.17 (adj +8.16) on $50.00, P(profit) 0.6165, adj growth 71.1 bp · B EV +22.81 (adj +15.95) on $40.95, P(profit) 0.5334, adj growth 135.3 bp · C EV +22.98 (adj +13.60) on $44.77, P(profit) 0.408, adj growth 115.8 bp · R EV +2.69 (adj +1.92) on $4.00, P(profit) 0.213, adj growth 64.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
