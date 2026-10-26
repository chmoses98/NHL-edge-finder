# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-26T17:13:11Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 145.34 | +20.28 | +5.41 | +20.06 | 0.675 | -36.30 | -50.06 | 44.56 |
| B thesis-diversified (joint) ← optimiser card | 129.25 | +17.72 | +7.05 | +11.78 | 0.705 | -29.39 | -49.03 | 61.52 |
| C best expression per thesis | 105.71 | +15.13 | +5.62 | +17.08 | 0.589 | -29.71 | -47.85 | 49.11 |
| R FUNDED research stakes | 15.00 | +1.08 | +0.52 | +0.11 | 0.503 | -7.71 | -8.45 | 0.00 |

## LAK @ NYR  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.543 / away 0.457

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_LAK_win | p_overtime | goals | shots NYR/LAK | NYR/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 5.98 | 27.3/27.5 | 24.2/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.48 | 5.89 | 27.1/27.3 | 24.0/23.8 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.086 | 0.52 | 0.48 | 0.00 | 6.01 | 21.6/32.1 | 28.6/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.56 | 0.44 | 0.00 | 9.31 | 28.6/28.8 | 23.0/22.1 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.50 | 0.50 | 0.45 | 5.88 | 21.7/32.6 | 29.4/18.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.53 | 0.47 | 0.50 | 2.83 | 25.7/26.1 | 24.7/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mats Zuccarello: 1+ assists NO | 66 | 0.800 | 0.699 | +0.125 | +0.024 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ goals NO | 67 | 0.722 | 0.708 | +0.037 | +0.023 | $18.01 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Tye Kartye: 1+ goals YES | 15 | 0.177 | 0.169 | +0.018 | +0.010 | $2.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26LANYR-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (5.61 vs 0.66 bp); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT26LANYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: LAK offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26LANYR-NYRSDURZI5-1|no; why: higher confidence-adjusted growth (5.19 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0008 below the 0.010/contract floor; relationships: KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT26LANYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: NYR offense succeeds (4+ goals)
- **Tye Kartye: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT26LANYR-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (1.63 vs 0.40 bp); alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4529): highest fidelity KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no (same contract)
- thesis NYR:SUPPRESSED (p 0.385): highest fidelity KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.3892): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.5 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3375, phi -0.212)
- KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3892, phi -0.212)
- KXNHLGOAL-26OCT26LANYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.385, phi -0.171)

portfolios: A EV +5.37 (adj +1.69) on $45.34, P(profit) 0.6477, adj growth 14.6 bp · B EV +4.99 (adj +1.48) on $40.97, P(profit) 0.6477, adj growth 13.1 bp · C EV +4.65 (adj +1.29) on $37.89, P(profit) 0.5826, adj growth 11.5 bp · R EV +0.27 (adj +0.16) on $5.00, P(profit) 0.7224, adj growth 5.7 bp

## TOR @ CGY  ·  10000 joint draws  ·  460 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.423 / away 0.577

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_TOR_win | p_overtime | goals | shots CGY/TOR | CGY/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.49 | 0.51 | 0.00 | 6.02 | 30.0/29.7 | 26.0/26.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.45 | 5.93 | 30.0/29.8 | 26.5/26.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.50 | 0.50 | 0.00 | 9.37 | 31.7/31.2 | 24.9/25.5 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.092 | 0.53 | 0.47 | 0.00 | 5.98 | 35.8/23.7 | 20.4/31.6 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.55 | 0.45 | 0.46 | 5.92 | 35.9/23.8 | 20.6/32.4 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.064 | 0.54 | 0.46 | 0.00 | 9.31 | 37.6/25.6 | 19.8/30.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.166 | 0.147 | +0.049 | +0.030 | $8.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 12 | 0.158 | 0.144 | +0.030 | +0.017 | $4.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| William Nylander: 1+ goals NO | 63 | 0.685 | 0.670 | +0.039 | +0.024 | $14.89 | FUNDED_RESEARCH | $4 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Toronto wins by over 2.5 goals NO | 75 | 0.817 | 0.781 | +0.053 | +0.018 | $20.00 | FUNDED_RESEARCH | $5 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT26TORCGY-TORJMCCABE22-1|yes; why: higher confidence-adjusted growth (18.59 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLSPREAD-26OCT26TORCGY-TOR3|no: INTENTIONAL_DIVERSIFIER (phi -0.149); failure: TOR offense suppressed (<= 2 goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR3|no; why: higher confidence-adjusted growth (5.65 vs 3.78 bp); despite a smaller raw edge (+0.030 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT26TORCGY-TOR3|no: MOSTLY_INDEPENDENT (phi 0.106); failure: CGY offense suppressed (<= 2 goals)
- **William Nylander: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26TORCGY-TORGMCKENNA92-1|no; why: higher confidence-adjusted growth (5.46 vs 4.00 bp); despite a smaller raw edge (+0.039 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT26TORCGY-TOR3|no: REINFORCING (phi 0.186); failure: TOR offense succeeds (4+ goals)
- **Toronto wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no has the higher standalone adjusted growth (5.46 vs 3.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.186); they share one thesis budget; relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.149); KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.106); KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no: REINFORCING (phi 0.186); failure: TOR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis TOR:OFFENSE_4PLUS (p 0.3994): highest fidelity KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.3863): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.5012): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3863, phi -0.191)
- KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.383, phi -0.187)
- KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3994, phi -0.271)
- KXNHLSPREAD-26OCT26TORCGY-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2828, phi -0.755)

portfolios: A EV +5.45 (adj +1.46) on $50.00, P(profit) 0.6729, adj growth 12.5 bp · B EV +6.63 (adj +3.62) on $47.02, P(profit) 0.7143, adj growth 31.4 bp · C EV +6.60 (adj +3.40) on $44.21, P(profit) 0.6969, adj growth 29.5 bp · R EV +0.59 (adj +0.26) on $9.00, P(profit) 0.5929, adj growth 9.1 bp

## DET @ EDM  ·  10000 joint draws  ·  436 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.616 / away 0.384

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_DET_win | p_overtime | goals | shots EDM/DET | EDM/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.72 | 0.28 | 0.00 | 6.05 | 27.9/27.7 | 25.1/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.72 | 0.28 | 0.00 | 9.39 | 29.4/29.4 | 24.5/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.56 | 0.44 | 0.46 | 6.04 | 27.8/27.9 | 24.6/24.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.087 | 0.75 | 0.25 | 0.00 | 6.03 | 32.9/22.1 | 19.8/27.8 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.067 | 0.78 | 0.22 | 0.00 | 9.43 | 34.4/23.6 | 19.3/25.9 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.60 | 0.40 | 0.47 | 5.96 | 32.8/22.2 | 19.1/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor McDavid: 2+ assists NO | 63 | 0.748 | 0.668 | +0.102 | +0.022 | $19.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Leon Draisaitl: 1+ assists NO | 41 | 0.492 | 0.448 | +0.065 | +0.021 | $10.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.75) | EVIDENCE_MIXED | D |
| Filip Hallander: 1+ goals YES | 11 | 0.142 | 0.129 | +0.025 | +0.012 | $3.26 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 26 | 0.299 | 0.288 | +0.025 | +0.015 | $8.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no; why: higher confidence-adjusted growth (4.51 vs 4.08 bp); relationships: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.134); KXNHLGOAL-26OCT26DETEDM-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.212); failure: EDM offense succeeds (4+ goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no; why: second expression of the same thesis: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (4.51 vs 4.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.134); they share one thesis budget; relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.134); KXNHLGOAL-26OCT26DETEDM-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.24); failure: EDM offense succeeds (4+ goals)
- **Filip Hallander: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (3.13 vs 2.81 bp); despite a smaller raw edge (+0.025 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes; why: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes has the higher standalone adjusted growth (2.81 vs 2.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.092); relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.212); KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.24); KXNHLGOAL-26OCT26DETEDM-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:SUPPRESSED (p 0.2609): highest fidelity KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.5412): highest fidelity KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.3 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5412, phi -0.337)
- KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 25% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5412, phi -0.305)
- KXNHLGOAL-26OCT26DETEDM-EDMFHALLANDER11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2609, phi -0.154)
- KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2609, phi -0.225)

portfolios: A EV +9.45 (adj +2.26) on $50.00, P(profit) 0.6958, adj growth 17.5 bp · B EV +6.09 (adj +1.95) on $41.26, P(profit) 0.6117, adj growth 17.1 bp · C EV +3.88 (adj +0.93) on $23.61, P(profit) 0.7478, adj growth 8.2 bp · R EV +0.22 (adj +0.10) on $1.00, P(profit) 0.1421, adj growth 3.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
