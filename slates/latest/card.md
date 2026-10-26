# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-26T16:18:27Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 140.00 | +18.67 | +4.69 | +21.33 | 0.685 | -37.45 | -49.48 | 38.16 |
| B thesis-diversified (joint) ← optimiser card | 105.05 | +14.84 | +5.47 | +15.00 | 0.632 | -29.32 | -45.48 | 47.67 |
| C best expression per thesis | 99.27 | +13.46 | +4.63 | +5.60 | 0.721 | -26.10 | -42.22 | 40.54 |
| R FUNDED research stakes | 11.00 | +0.63 | +0.37 | +2.39 | 0.620 | -4.90 | -11.00 | 0.00 |

## LAK @ NYR  ·  10000 joint draws  ·  430 bet sides mapped, 2 +EV candidates, 2 on card

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
| Pavel Dorofeyev: 1+ goals NO | 67 | 0.722 | 0.708 | +0.037 | +0.023 | $17.90 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 66 | 0.800 | 0.696 | +0.125 | +0.020 | $19.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26LANYR-NYRSDURZI5-1|no; why: higher confidence-adjusted growth (5.19 vs 0.34 bp); despite a smaller raw edge (+0.037 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0055 below the 0.010/contract floor; relationships: KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.025); failure: NYR offense succeeds (4+ goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT26LANYR-LAMZUCCARELLO36-1|no; why: higher confidence-adjusted growth (4.17 vs 0.30 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.025); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYR:SUPPRESSED (p 0.385): highest fidelity KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no (same contract)
- thesis LAK:SUPPRESSED (p 0.4529): highest fidelity KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no (same contract)
- KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3892, phi -0.212)
- KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.0 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3375, phi -0.212)

portfolios: A EV +4.77 (adj +1.26) on $40.00, P(profit) 0.5826, adj growth 11.0 bp · B EV +4.56 (adj +1.18) on $37.40, P(profit) 0.5826, adj growth 10.4 bp · C EV +4.56 (adj +1.18) on $37.40, P(profit) 0.5826, adj growth 10.4 bp · R EV +0.27 (adj +0.16) on $5.00, P(profit) 0.7224, adj growth 5.7 bp

## TOR @ CGY  ·  10000 joint draws  ·  444 bet sides mapped, 14 +EV candidates, 4 on card

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
| Teddy Blueger: 1+ goals YES | 12 | 0.166 | 0.152 | +0.038 | +0.025 | $6.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 12 | 0.158 | 0.144 | +0.030 | +0.017 | $4.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 10 | 0.128 | 0.120 | +0.022 | +0.013 | $3.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| William Nylander: 1+ goals NO | 64 | 0.685 | 0.673 | +0.029 | +0.017 | $12.41 | FUNDED_RESEARCH | $4 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26TORCGY-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (11.55 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT26TORCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no: MOSTLY_INDEPENDENT (phi -0.023); failure: TOR offense suppressed (<= 2 goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR3|no; why: higher confidence-adjusted growth (5.65 vs 3.78 bp); despite a smaller raw edge (+0.030 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT26TORCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: CGY offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR3|no; why: higher confidence-adjusted growth (4.16 vs 3.78 bp); despite a smaller raw edge (+0.022 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CGY offense suppressed (<= 2 goals)
- **William Nylander: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4|no; why: Player prop expression KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no selected over broad KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT26TORCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis TOR:OFFENSE_4PLUS (p 0.3994): highest fidelity KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.3863): highest fidelity KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4|no (same contract)
- thesis CGY:WINS (p 0.5012): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3863, phi -0.191)
- KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.383, phi -0.187)
- KXNHLGOAL-26OCT26TORCGY-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.383, phi -0.162)
- KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3994, phi -0.271)
- override: Player prop expression KXNHLGOAL-26OCT26TORCGY-TORWNYLANDER88-1|no selected over broad KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.13 (adj +1.64) on $50.00, P(profit) 0.58, adj growth 13.2 bp · B EV +4.29 (adj +2.60) on $26.88, P(profit) 0.388, adj growth 22.5 bp · C EV +5.14 (adj +2.43) on $35.23, P(profit) 0.6827, adj growth 21.1 bp · R EV +0.18 (adj +0.10) on $4.00, P(profit) 0.6852, adj growth 3.4 bp

## DET @ EDM  ·  10000 joint draws  ·  414 bet sides mapped, 5 +EV candidates, 4 on card

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
| Connor McDavid: 2+ assists NO | 63 | 0.748 | 0.668 | +0.102 | +0.022 | $19.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Leon Draisaitl: 1+ assists NO | 41 | 0.492 | 0.446 | +0.065 | +0.019 | $9.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.75) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 26 | 0.299 | 0.288 | +0.025 | +0.015 | $7.73 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Kasperi Kapanen: 1+ assists YES | 25 | 0.313 | 0.276 | +0.050 | +0.013 | $4.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_MIXED | D |
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no; why: higher confidence-adjusted growth (4.51 vs 3.18 bp); relationships: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.134); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.212); KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); failure: EDM offense succeeds (4+ goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no; why: second expression of the same thesis: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (4.51 vs 3.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.134); they share one thesis budget; relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.134); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.24); KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (2.32 vs 2.00 bp); despite a smaller raw edge (+0.025 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.212); KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.24); KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi 0.092); failure: EDM offense suppressed (<= 2 goals)
- **Kasperi Kapanen: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (2.32 vs 2.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.092); they share one thesis budget; relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.092); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:SUPPRESSED (p 0.2609): highest fidelity KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.5412): highest fidelity KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.3 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5412, phi -0.337)
- KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 25% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5412, phi -0.305)
- KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2609, phi -0.225)
- KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2609, phi -0.206)

portfolios: A EV +7.78 (adj +1.79) on $50.00, P(profit) 0.612, adj growth 14.0 bp · B EV +5.99 (adj +1.69) on $40.77, P(profit) 0.649, adj growth 14.8 bp · C EV +3.76 (adj +1.02) on $26.64, P(profit) 0.7478, adj growth 9.0 bp · R EV +0.19 (adj +0.11) on $2.00, P(profit) 0.299, adj growth 3.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
