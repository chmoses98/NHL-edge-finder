# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-08T00:02:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +28.64 | +7.83 | +27.93 | 0.716 | -34.16 | -50.48 | 66.50 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +25.42 | +14.11 | +21.05 | 0.673 | -34.78 | -49.98 | 128.54 |
| C best expression per thesis | 150.00 | +23.10 | +9.36 | +22.06 | 0.704 | -28.95 | -42.73 | 85.29 |
| R FUNDED research stakes | 18.00 | +2.90 | +1.56 | +2.70 | 0.564 | -7.79 | -13.59 | 0.00 |

## CHI @ CAR  ·  10000 joint draws  ·  462 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.787 / away 0.213

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CHI_win | p_overtime | goals | shots CAR/CHI | CAR/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.205 | 0.79 | 0.21 | 0.00 | 6.04 | 34.4/20.2 | 18.0/29.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.160 | 0.81 | 0.19 | 0.00 | 9.39 | 36.3/21.7 | 17.7/27.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.152 | 0.57 | 0.43 | 0.49 | 5.97 | 34.5/20.7 | 17.5/30.9 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.081 | 0.74 | 0.26 | 0.00 | 3.48 | 32.9/19.1 | 18.0/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.070 | 0.74 | 0.26 | 0.00 | 6.03 | 28.0/26.6 | 24.0/23.2 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.57 | 0.43 | 0.52 | 2.9 | 33.0/19.1 | 17.6/31.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dillon Boucher: 1+ goals YES | 5 | 0.089 | 0.077 | +0.036 | +0.024 | $3.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 62 | 0.703 | 0.680 | +0.067 | +0.044 | $13.67 | FUNDED_RESEARCH | $4 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 19 | 0.243 | 0.227 | +0.042 | +0.026 | $5.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 12 | 0.153 | 0.143 | +0.026 | +0.015 | $2.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Dillon Boucher: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (23.40 vs 9.45 bp); despite a smaller raw edge (+0.036 vs +0.042/contract); relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CHI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGAME-26NOV07CHICAR-CHI|yes; why: higher confidence-adjusted growth (18.05 vs 8.19 bp); despite a smaller raw edge (+0.067 vs +0.102/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: CAR offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGAME-26NOV07CHICAR-CHI|yes; why: higher confidence-adjusted growth (9.45 vs 8.19 bp); despite a smaller raw edge (+0.042 vs +0.102/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CHI offense suppressed (<= 2 goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (9.45 vs 4.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.20, CAR shot control · high event (8+) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15.
- thesis CAR:SUPPRESSED (p 0.2461): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.2753): highest fidelity KXNHLTEAMTOTAL-26NOV07CHICAR-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.313): highest fidelity KXNHLGAME-26NOV07CHICAR-CHI|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26NOV07CHICAR-CHI|yes (same contract)
- KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.159)
- KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5519, phi -0.228)
- KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.253)
- KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.178)

portfolios: A EV +5.52 (adj +1.11) on $25.00, P(profit) 0.6449, adj growth 9.1 bp · B EV +5.55 (adj +3.56) on $25.44, P(profit) 0.3833, adj growth 32.4 bp · C EV +4.30 (adj +2.13) on $23.73, P(profit) 0.4113, adj growth 19.6 bp · R EV +0.42 (adj +0.27) on $4.00, P(profit) 0.7034, adj growth 10.3 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07CHICAR-CAR|no == KXNHLGAME-26NOV07CHICAR-CHI|yes

## SJS @ DAL  ·  10000 joint draws  ·  456 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.723 / away 0.277

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_SJS_win | p_overtime | goals | shots DAL/SJS | DAL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.69 | 0.31 | 0.00 | 6.0 | 26.3/26.0 | 23.2/21.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.114 | 0.74 | 0.26 | 0.00 | 5.98 | 31.4/20.7 | 18.4/26.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.52 | 0.48 | 0.48 | 5.94 | 26.7/26.4 | 23.2/23.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.59 | 0.41 | 0.47 | 5.87 | 31.7/20.7 | 17.7/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.68 | 0.32 | 0.00 | 9.37 | 28.1/27.7 | 22.6/21.0 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.075 | 0.77 | 0.23 | 0.00 | 9.29 | 33.3/22.0 | 17.8/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dallas wins by over 1.5 goals NO | 50 | 0.594 | 0.545 | +0.077 | +0.027 | $8.12 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| San Jose over 3.5 goals scored YES | 22 | 0.292 | 0.254 | +0.060 | +0.022 | $4.09 | FUNDED_RESEARCH | $2 | SJS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ assists NO | 72 | 0.796 | 0.756 | +0.062 | +0.022 | $11.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Macklin Celebrini: 1+ assists NO | 53 | 0.611 | 0.566 | +0.064 | +0.018 | $8.81 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.77) | EVIDENCE_MIXED | D |
- **Dallas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26NOV07SJDAL-SJ2|yes; why: higher confidence-adjusted growth (6.46 vs 4.31 bp); relationships: KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes: REINFORCING (phi 0.408); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.144); KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.211); failure: DAL wins by 2+
- **San Jose over 3.5 goals scored YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07SJDAL-DAL2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07SJDAL-DAL2|no has the higher standalone adjusted growth (6.46 vs 5.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.408); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07SJDAL-DAL2|no: REINFORCING (phi 0.408); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.219); KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.296); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (5.28 vs 2.93 bp); despite a smaller raw edge (+0.062 vs +0.064/contract); relationships: KXNHLSPREAD-26NOV07SJDAL-DAL2|no: INTENTIONAL_DIVERSIFIER (phi -0.144); KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes: INTENTIONAL_DIVERSIFIER (phi -0.219); KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.068); failure: SJS offense succeeds (4+ goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no; why: second expression of the same thesis: KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no has the higher standalone adjusted growth (5.28 vs 2.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.068); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07SJDAL-DAL2|no: INTENTIONAL_DIVERSIFIER (phi -0.211); KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes: INTENTIONAL_DIVERSIFIER (phi -0.296); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.068); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis DAL:SUPPRESSED (p 0.3168): highest fidelity KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07SJDAL-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4148): highest fidelity KXNHLSPREAD-26NOV07SJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07SJDAL-DAL2|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.284): highest fidelity KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07SJDAL-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV07SJDAL-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.4057, phi -1.0)
- KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis SJS:SUPPRESSED (p 0.5044, phi -0.648)
- KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.284, phi -0.219)
- KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 23% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.284, phi -0.297)

portfolios: A EV +4.54 (adj +1.05) on $25.00, P(profit) 0.4928, adj growth 7.8 bp · B EV +4.29 (adj +1.44) on $32.72, P(profit) 0.4593, adj growth 13.5 bp · C EV +3.01 (adj +1.13) on $37.61, P(profit) 0.4448, adj growth 10.6 bp · R EV +0.96 (adj +0.34) on $5.00, P(profit) 0.6217, adj growth 11.1 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07SJDAL-DAL|no == KXNHLGAME-26NOV07SJDAL-SJ|yes

## TBL @ MIN  ·  10000 joint draws  ·  436 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.449 / away 0.551

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_TBL_win | p_overtime | goals | shots MIN/TBL | MIN/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.124 | 0.50 | 0.50 | 0.50 | 6.0 | 27.8/27.9 | 24.6/24.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.48 | 0.52 | 0.00 | 6.0 | 27.6/27.9 | 24.3/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.47 | 0.53 | 0.00 | 9.45 | 29.5/29.6 | 23.1/23.4 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.073 | 0.40 | 0.60 | 0.00 | 5.99 | 22.0/32.8 | 28.7/19.1 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.48 | 0.52 | 0.47 | 5.96 | 22.5/33.0 | 29.8/19.2 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.059 | 0.48 | 0.52 | 0.00 | 6.04 | 32.2/22.0 | 18.4/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 9 | 0.136 | 0.123 | +0.040 | +0.027 | $4.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 15 | 0.190 | 0.179 | +0.031 | +0.020 | $3.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Charle-Edouard D'Astous: 1+ goals NO | 90 | 0.928 | 0.920 | +0.022 | +0.013 | $13.67 | FUNDED_RESEARCH | $4 | TBL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 57 | 0.624 | 0.609 | +0.036 | +0.022 | $8.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (18.47 vs 1.44 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07TBMIN-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26NOV07TBMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (6.26 vs 1.44 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07TBMIN-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07TBMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.022); failure: MIN offense suppressed (<= 2 goals)
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07TBMIN-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (4.68 vs 1.95 bp); despite a smaller raw edge (+0.022 vs +0.122/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26NOV07TBMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07TBMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: TBL offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no; why: Player prop expression KXNHLGOAL-26NOV07TBMIN-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.80 vs 0.69 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV07TBMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV07TBMIN-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.388): highest fidelity KXNHLGOAL-26NOV07TBMIN-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no — Player prop expression KXNHLGOAL-26NOV07TBMIN-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.80 vs 0.69 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis TBL:SUPPRESSED (p 0.3573): highest fidelity KXNHLAST-26NOV07TBMIN-TBNKUCHEROV86-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07TBMIN-TBNKUCHEROV86-1|no (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.384): highest fidelity KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes (same contract)
- KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.388, phi -0.148)
- KXNHLGOAL-26NOV07TBMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.388, phi -0.186)
- KXNHLGOAL-26NOV07TBMIN-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4243, phi -0.124)
- KXNHLGOAL-26NOV07TBMIN-MINKKAPRIZOV97-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.384, phi -0.276)
- override: Player prop expression KXNHLGOAL-26NOV07TBMIN-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.80 vs 0.69 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.54 (adj +2.07) on $25.00, P(profit) 0.6096, adj growth 18.7 bp · B EV +3.51 (adj +2.30) on $30.60, P(profit) 0.2956, adj growth 20.9 bp · C EV +2.88 (adj +0.74) on $14.34, P(profit) 0.5259, adj growth 6.7 bp · R EV +0.10 (adj +0.06) on $4.00, P(profit) 0.9279, adj growth 2.3 bp

## DET @ COL  ·  10000 joint draws  ·  454 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.664 / away 0.336

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_DET_win | p_overtime | goals | shots COL/DET | COL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.74 | 0.26 | 0.00 | 5.99 | 28.6/28.2 | 25.7/23.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.112 | 0.76 | 0.24 | 0.00 | 6.01 | 33.7/22.1 | 19.8/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.54 | 0.46 | 0.47 | 5.99 | 28.4/28.0 | 24.6/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.73 | 0.27 | 0.00 | 9.37 | 30.0/29.7 | 24.8/22.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.088 | 0.80 | 0.20 | 0.00 | 9.32 | 35.9/23.7 | 19.8/27.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.60 | 0.40 | 0.44 | 5.98 | 34.2/22.6 | 19.3/30.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carter Mazur: 1+ goals YES | 6 | 0.085 | 0.075 | +0.021 | +0.011 | $1.85 | FUNDED_RESEARCH | $1 | DET:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Lucas Raymond: 1+ assists NO | 60 | 0.682 | 0.636 | +0.065 | +0.019 | $9.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
| Sheldon Dries: 1+ goals YES | 8 | 0.106 | 0.096 | +0.021 | +0.011 | $1.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ assists YES | 28 | 0.344 | 0.309 | +0.050 | +0.015 | $3.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
- **Carter Mazur: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV07DETCOL-2|yes; why: higher confidence-adjusted growth (4.44 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26NOV07DETCOL-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: DET offense suppressed (<= 2 goals)
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV07DETCOL-DETLRAYMOND23-1|no; why: higher confidence-adjusted growth (3.40 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07DETCOL-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26NOV07DETCOL-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: DET offense succeeds (4+ goals)
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV07DETCOL-2|yes; why: higher confidence-adjusted growth (3.34 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07DETCOL-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: DET offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ assists YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes; why: KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes has the higher standalone adjusted growth (2.83 vs 2.44 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.046); relationships: KXNHLGOAL-26NOV07DETCOL-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV07DETCOL-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis DET:SUPPRESSED (p 0.4945): highest fidelity KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no (same contract)
- thesis COL:OFFENSE_4PLUS (p 0.5356): highest fidelity KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:OFFENSE_4PLUS (p 0.2909): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV07DETCOL-DETCMAZUR34-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4945, phi -0.143)
- KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.2909, phi -0.265)
- KXNHLGOAL-26NOV07DETCOL-DETSDRIES15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4945, phi -0.164)
- KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2617, phi -0.236)

portfolios: A EV +4.20 (adj +1.37) on $25.00, P(profit) 0.521, adj growth 11.6 bp · B EV +2.69 (adj +1.05) on $16.80, P(profit) 0.3749, adj growth 9.5 bp · C EV +1.79 (adj +0.52) on $13.44, P(profit) 0.7795, adj growth 4.8 bp · R EV +0.33 (adj +0.17) on $1.00, P(profit) 0.0851, adj growth 5.5 bp

## PIT @ LAK  ·  10000 joint draws  ·  436 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.526 / away 0.474

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_PIT_win | p_overtime | goals | shots LAK/PIT | LAK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.57 | 0.42 | 0.00 | 5.99 | 27.7/27.5 | 24.1/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.53 | 0.47 | 0.43 | 5.93 | 27.3/27.4 | 24.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.58 | 0.42 | 0.00 | 9.24 | 29.0/29.0 | 23.4/22.4 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.071 | 0.64 | 0.36 | 0.00 | 6.02 | 32.4/22.0 | 19.3/28.2 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.55 | 0.45 | 0.46 | 5.9 | 32.2/22.0 | 18.9/28.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.066 | 0.47 | 0.53 | 0.00 | 6.02 | 21.7/31.7 | 27.8/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.075 | 0.068 | +0.022 | +0.014 | $2.35 | FUNDED_RESEARCH | $1 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ assists NO | 70 | 0.777 | 0.736 | +0.062 | +0.021 | $13.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Blake Lizotte: 1+ goals YES | 10 | 0.126 | 0.118 | +0.019 | +0.012 | $2.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.157 | 0.149 | +0.019 | +0.011 | $2.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07PITLA-PIT2|no; why: higher confidence-adjusted growth (8.55 vs 0.07 bp); despite a smaller raw edge (+0.022 vs +0.024/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: LAK offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07PITLA-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (4.83 vs 1.21 bp); relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: PIT offense succeeds (4+ goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (3.17 vs 2.12 bp); relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes has the higher standalone adjusted growth (3.17 vs 2.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis PIT:SUPPRESSED (p 0.4178): highest fidelity KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no (same contract)
- thesis PIT:WINS_BY_2PLUS (p 0.2416): highest fidelity KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.3534): highest fidelity KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.357, phi -0.132)
- KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3534, phi -0.232)
- KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4178, phi -0.192)
- KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4178, phi -0.197)

portfolios: A EV +2.47 (adj +1.12) on $25.00, P(profit) 0.3967, adj growth 10.1 bp · B EV +2.86 (adj +1.46) on $20.52, P(profit) 0.2881, adj growth 13.3 bp · C EV +1.96 (adj +0.81) on $23.42, P(profit) 0.5781, adj growth 7.4 bp · R EV +0.41 (adj +0.27) on $1.00, P(profit) 0.0751, adj growth 8.8 bp

## VAN @ EDM  ·  10000 joint draws  ·  428 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.751 / away 0.249

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_VAN_win | p_overtime | goals | shots EDM/VAN | EDM/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.147 | 0.80 | 0.20 | 0.00 | 6.08 | 33.2/21.1 | 18.9/28.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.141 | 0.80 | 0.20 | 0.00 | 9.49 | 34.8/22.3 | 18.3/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.73 | 0.27 | 0.00 | 9.52 | 29.1/28.3 | 23.6/21.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.73 | 0.27 | 0.00 | 6.12 | 27.3/26.6 | 24.1/22.8 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.59 | 0.41 | 0.45 | 6.0 | 33.4/21.3 | 18.2/29.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.54 | 0.46 | 0.48 | 6.02 | 27.7/27.1 | 23.8/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vasily Podkolzin: 1+ goals YES | 27 | 0.348 | 0.326 | +0.065 | +0.042 | $9.82 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 16 | 0.221 | 0.204 | +0.051 | +0.035 | $6.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 10 | 0.144 | 0.130 | +0.037 | +0.024 | $4.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 11 | 0.146 | 0.136 | +0.029 | +0.019 | $3.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (19.17 vs 1.50 bp); despite a smaller raw edge (+0.065 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: EDM offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (18.39 vs 5.58 bp); relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (18.39 vs 12.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (19.17 vs 7.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.15, EDM shot control · high event (8+) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5979): highest fidelity KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.3223): highest fidelity KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2184): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2184, phi -0.226)
- KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4569, phi -0.239)
- KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4569, phi -0.19)
- KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2184, phi -0.131)

portfolios: A EV +6.37 (adj +1.11) on $25.00, P(profit) 0.5544, adj growth 9.2 bp · B EV +6.52 (adj +4.30) on $23.92, P(profit) 0.6315, adj growth 38.9 bp · C EV +9.16 (adj +4.03) on $37.46, P(profit) 0.4929, adj growth 36.3 bp · R EV +0.68 (adj +0.45) on $3.00, P(profit) 0.3483, adj growth 15.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
