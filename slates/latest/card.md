# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-26T22:08:36Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +23.76 | +6.08 | +24.14 | 0.669 | -44.25 | -64.35 | 45.88 |
| B thesis-diversified (joint) ← optimiser card | 118.36 | +19.13 | +8.50 | +13.90 | 0.619 | -36.60 | -47.83 | 74.39 |
| C best expression per thesis | 87.14 | +13.77 | +6.38 | +7.28 | 0.593 | -39.07 | -47.61 | 55.41 |
| R FUNDED research stakes | 13.00 | +0.84 | +0.52 | +0.64 | 0.708 | -6.76 | -6.76 | 0.00 |

## LAK @ NYR  ·  10000 joint draws  ·  440 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.549 / away 0.451

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_LAK_win | p_overtime | goals | shots NYR/LAK | NYR/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.57 | 0.43 | 0.00 | 5.99 | 27.1/27.2 | 24.0/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.47 | 5.94 | 27.3/27.7 | 24.2/24.0 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.084 | 0.55 | 0.45 | 0.00 | 6.0 | 21.7/32.6 | 29.0/18.1 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.50 | 0.50 | 0.46 | 5.87 | 21.4/32.4 | 29.0/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.56 | 0.44 | 0.00 | 9.19 | 28.8/28.8 | 23.4/22.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.55 | 0.45 | 0.00 | 3.45 | 25.6/26.0 | 24.2/23.6 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 4 | 0.065 | 0.058 | +0.022 | +0.015 | $3.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 66 | 0.711 | 0.697 | +0.035 | +0.021 | $18.10 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ goals YES | 30 | 0.342 | 0.330 | +0.027 | +0.015 | $5.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
| Vladislav Gavrikov: 1+ assists YES | 23 | 0.333 | 0.256 | +0.090 | +0.014 | $4.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (11.31 vs 6.77 bp); despite a smaller raw edge (+0.022 vs +0.039/contract); relationships: KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT26LANYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: LAK offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26LANYR-NYRSDURZI5-1|no; why: higher confidence-adjusted growth (4.58 vs 0.27 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0049 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT26LANYR-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT26LANYR-NYRVGAVRIKOV44-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: NYR offense succeeds (4+ goals)
- **Artemi Panarin: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes; why: Player prop expression KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes selected over player prop KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.51 vs 0.48 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT26LANYR-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT26LANYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: LAK offense suppressed (<= 2 goals)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT26LANYR-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (2.25 vs 0.02 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT26LANYR-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.088); KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:OFFENSE_4PLUS (p 0.3331): highest fidelity KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes — Player prop expression KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes selected over player prop KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.51 vs 0.48 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis NYR:SUPPRESSED (p 0.384): highest fidelity KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.3964): highest fidelity KXNHLAST-26OCT26LANYR-NYRVGAVRIKOV44-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT26LANYR-NYRVGAVRIKOV44-1|yes (same contract)
- KXNHLGOAL-26OCT26LANYR-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4461, phi -0.122)
- KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3964, phi -0.242)
- KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4461, phi -0.284)
- KXNHLAST-26OCT26LANYR-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.8 pts; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.384, phi -0.266)
- override: Player prop expression KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes selected over player prop KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.51 vs 0.48 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +8.90 (adj +2.74) on $50.00, P(profit) 0.5015, adj growth 20.2 bp · B EV +4.79 (adj +2.24) on $31.29, P(profit) 0.46, adj growth 19.3 bp · C EV +3.74 (adj +1.57) on $30.74, P(profit) 0.4022, adj growth 13.7 bp · R EV +0.26 (adj +0.16) on $5.00, P(profit) 0.7111, adj growth 5.4 bp

## TOR @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.449 / away 0.551

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_TOR_win | p_overtime | goals | shots CGY/TOR | CGY/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.49 | 0.51 | 0.00 | 6.01 | 30.0/29.7 | 26.2/26.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.47 | 0.53 | 0.46 | 5.9 | 30.1/29.9 | 26.5/26.8 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.092 | 0.57 | 0.43 | 0.00 | 5.98 | 35.6/23.7 | 20.5/31.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.52 | 0.48 | 0.00 | 9.31 | 31.7/31.4 | 25.3/25.5 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.54 | 0.46 | 0.47 | 5.91 | 35.9/23.9 | 20.6/32.4 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.066 | 0.50 | 0.50 | 0.00 | 9.31 | 37.6/25.7 | 19.7/30.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.160 | 0.145 | +0.043 | +0.028 | $7.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 79 | 0.849 | 0.833 | +0.047 | +0.031 | $18.45 | FUNDED_RESEARCH | $5 | TOR:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 12 | 0.166 | 0.152 | +0.039 | +0.025 | $6.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ assists NO | 54 | 0.627 | 0.581 | +0.070 | +0.024 | $11.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT26TORCGY-TORJMCCABE22-1|yes; why: higher confidence-adjusted growth (16.22 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT26TORCGY-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.026); failure: TOR offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (13.55 vs 5.03 bp); despite a smaller raw edge (+0.047 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.108); failure: TOR offense succeeds (4+ goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR3|no; why: higher confidence-adjusted growth (11.76 vs 1.62 bp); despite a smaller raw edge (+0.039 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT26TORCGY-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: CGY offense suppressed (<= 2 goals)
- **Auston Matthews: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26TORCGY-TORKMARCHENKO86-1|no; why: higher confidence-adjusted growth (5.03 vs 2.53 bp); despite a smaller raw edge (+0.070 vs +0.088/contract); relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT26TORCGY-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.108); KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CGY shot control · normal event (5-7) · decided (2+) 0.09.
- thesis TOR:OFFENSE_4PLUS (p 0.3987): highest fidelity KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.4013): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3845): highest fidelity KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3845, phi -0.192)
- KXNHLGOAL-26OCT26TORCGY-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3987, phi -0.186)
- KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.3761, phi -0.193)
- KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3987, phi -0.263)

portfolios: A EV +5.72 (adj +1.47) on $50.00, P(profit) 0.536, adj growth 11.1 bp · B EV +7.16 (adj +4.20) on $43.69, P(profit) 0.6877, adj growth 36.8 bp · C EV +6.94 (adj +3.75) on $39.62, P(profit) 0.3009, adj growth 32.4 bp · R EV +0.29 (adj +0.19) on $5.00, P(profit) 0.8487, adj growth 7.4 bp

## DET @ EDM  ·  10000 joint draws  ·  510 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.611 / away 0.389

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_DET_win | p_overtime | goals | shots EDM/DET | EDM/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.136 | 0.71 | 0.29 | 0.00 | 6.05 | 27.9/27.8 | 25.3/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.69 | 0.31 | 0.00 | 9.46 | 29.3/29.4 | 24.3/21.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.47 | 5.98 | 28.0/27.8 | 24.3/24.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.080 | 0.76 | 0.24 | 0.00 | 6.03 | 32.7/22.0 | 19.6/27.7 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.065 | 0.78 | 0.22 | 0.00 | 9.39 | 34.7/23.3 | 19.3/26.0 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.60 | 0.40 | 0.46 | 5.97 | 33.2/22.3 | 19.2/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Leon Draisaitl: 1+ assists NO | 40 | 0.493 | 0.444 | +0.076 | +0.027 | $11.72 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
| Connor McDavid: 2+ assists NO | 63 | 0.753 | 0.670 | +0.106 | +0.023 | $18.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 26 | 0.300 | 0.288 | +0.026 | +0.015 | $8.33 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ assists YES | 30 | 0.391 | 0.325 | +0.076 | +0.011 | $5.05 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (6.72 vs 5.26 bp); despite a smaller raw edge (+0.076 vs +0.106/contract); relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.094); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.211); KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); failure: EDM offense succeeds (4+ goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no; why: second expression of the same thesis: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no has the higher standalone adjusted growth (6.72 vs 5.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.094); they share one thesis budget; relationships: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.094); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.2); KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.089); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes; why: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes has the higher standalone adjusted growth (2.64 vs 2.49 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.079); relationships: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.211); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.2); KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes; why: Player prop expression KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.50 vs 0.41 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.089); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:SUPPRESSED (p 0.2642): highest fidelity KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.5294): highest fidelity KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes — Player prop expression KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.50 vs 0.41 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis DET:SUPPRESSED (p 0.4602): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 27% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5294, phi -0.279)
- KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.8 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5294, phi -0.335)
- KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2642, phi -0.217)
- KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.1 pts; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2642, phi -0.232)
- override: Player prop expression KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.50 vs 0.41 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.14 (adj +1.87) on $50.00, P(profit) 0.5791, adj growth 14.6 bp · B EV +7.18 (adj +2.06) on $43.38, P(profit) 0.72, adj growth 18.3 bp · C EV +3.09 (adj +1.06) on $16.78, P(profit) 0.6593, adj growth 9.3 bp · R EV +0.29 (adj +0.17) on $3.00, P(profit) 0.2997, adj growth 4.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
