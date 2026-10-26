# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-26T22:36:37Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.53 | +6.33 | +27.25 | 0.671 | -47.27 | -64.05 | 46.66 |
| B thesis-diversified (joint) ← optimiser card | 119.17 | +19.21 | +8.70 | +16.21 | 0.623 | -39.63 | -51.87 | 75.95 |
| C best expression per thesis | 93.46 | +14.60 | +6.48 | +10.41 | 0.614 | -36.57 | -47.08 | 56.30 |
| R FUNDED research stakes | 10.00 | +0.69 | +0.41 | +0.97 | 0.502 | -3.84 | -10.00 | 0.00 |

## LAK @ NYR  ·  10000 joint draws  ·  440 bet sides mapped, 10 +EV candidates, 4 on card

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
| Alex Laferriere: 1+ goals YES | 25 | 0.313 | 0.296 | +0.050 | +0.033 | $12.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 4 | 0.065 | 0.058 | +0.022 | +0.015 | $3.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ goals YES | 30 | 0.342 | 0.330 | +0.027 | +0.015 | $5.32 | FUNDED_RESEARCH | $2 | LAK:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 54 | 0.601 | 0.568 | +0.043 | +0.011 | $12.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.77) | EVIDENCE_MIXED | D |
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT26LANYR-LASLAUGHTON21-1|yes; why: higher confidence-adjusted growth (11.97 vs 4.42 bp); relationships: KXNHLGOAL-26OCT26LANYR-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT26LANYR-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.215); failure: LAK offense suppressed (<= 2 goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes has the higher standalone adjusted growth (11.97 vs 11.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT26LANYR-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.089); failure: LAK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes; why: Player prop expression KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes selected over player prop KXNHLGOAL-26OCT26LANYR-LAEHAULA56-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.51 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT26LANYR-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT26LANYR-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: LAK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT26LANYR-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (0.98 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.215); KXNHLGOAL-26OCT26LANYR-LAJEDMUNDSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.089); KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:OFFENSE_4PLUS (p 0.3331): highest fidelity KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes — Player prop expression KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes selected over player prop KXNHLGOAL-26OCT26LANYR-LAEHAULA56-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.51 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis NYR:OFFENSE_4PLUS (p 0.3964): highest fidelity KXNHLAST-26OCT26LANYR-NYRVGAVRIKOV44-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT26LANYR-NYRVGAVRIKOV44-1|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.384): highest fidelity KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4461, phi -0.274)
- KXNHLGOAL-26OCT26LANYR-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4461, phi -0.122)
- KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4461, phi -0.284)
- KXNHLAST-26OCT26LANYR-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 23% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3331, phi -0.302)
- override: Player prop expression KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes selected over player prop KXNHLGOAL-26OCT26LANYR-LAEHAULA56-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.51 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +10.54 (adj +3.51) on $50.00, P(profit) 0.4973, adj growth 26.6 bp · B EV +5.50 (adj +3.19) on $33.18, P(profit) 0.5085, adj growth 27.5 bp · C EV +5.02 (adj +2.15) on $38.94, P(profit) 0.413, adj growth 18.7 bp · R EV +0.17 (adj +0.10) on $2.00, P(profit) 0.3417, adj growth 3.2 bp

## TOR @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 13 +EV candidates, 4 on card

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
| Teddy Blueger: 1+ goals YES | 11 | 0.160 | 0.141 | +0.043 | +0.024 | $6.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 12 | 0.166 | 0.152 | +0.039 | +0.025 | $6.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 80 | 0.849 | 0.834 | +0.037 | +0.023 | $18.47 | FUNDED_RESEARCH | $5 | TOR:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ assists NO | 54 | 0.627 | 0.581 | +0.070 | +0.024 | $11.53 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT26TORCGY-TORJMCCABE22-1|yes; why: higher confidence-adjusted growth (12.20 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT26TORCGY-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.026); failure: TOR offense suppressed (<= 2 goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR3|no; why: higher confidence-adjusted growth (11.76 vs 1.62 bp); despite a smaller raw edge (+0.039 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT26TORCGY-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: CGY offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (7.53 vs 5.03 bp); despite a smaller raw edge (+0.037 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.108); failure: TOR offense succeeds (4+ goals)
- **Auston Matthews: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26TORCGY-TORWNYLANDER88-2|no; why: higher confidence-adjusted growth (5.03 vs 2.57 bp); relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT26TORCGY-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.108); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CGY shot control · normal event (5-7) · decided (2+) 0.09.
- thesis TOR:OFFENSE_4PLUS (p 0.3987): highest fidelity KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.4013): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3845): highest fidelity KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3845, phi -0.192)
- KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.3761, phi -0.193)
- KXNHLGOAL-26OCT26TORCGY-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3987, phi -0.186)
- KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3987, phi -0.263)

portfolios: A EV +5.72 (adj +1.47) on $50.00, P(profit) 0.536, adj growth 11.1 bp · B EV +6.52 (adj +3.53) on $42.58, P(profit) 0.6877, adj growth 30.9 bp · C EV +6.49 (adj +3.27) on $37.74, P(profit) 0.6913, adj growth 28.3 bp · R EV +0.23 (adj +0.14) on $5.00, P(profit) 0.8487, adj growth 5.2 bp

## DET @ EDM  ·  10000 joint draws  ·  512 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.612 / away 0.388

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
| Leon Draisaitl: 1+ assists NO | 40 | 0.493 | 0.444 | +0.076 | +0.027 | $12.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
| Connor McDavid: 2+ assists NO | 63 | 0.753 | 0.666 | +0.106 | +0.020 | $17.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 26 | 0.300 | 0.288 | +0.026 | +0.015 | $8.35 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ assists YES | 30 | 0.391 | 0.325 | +0.076 | +0.011 | $5.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (6.72 vs 4.37 bp); relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.094); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.211); KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); failure: EDM offense succeeds (4+ goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no; why: second expression of the same thesis: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no has the higher standalone adjusted growth (6.72 vs 3.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.094); they share one thesis budget; relationships: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.094); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.2); KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.089); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes; why: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes has the higher standalone adjusted growth (2.64 vs 2.49 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.079); relationships: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.211); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.2); KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes; why: Player prop expression KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.50 vs 0.41 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.089); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:SUPPRESSED (p 0.2642): highest fidelity KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.5294): highest fidelity KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes — Player prop expression KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.50 vs 0.41 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 27% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5294, phi -0.279)
- KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.3 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5294, phi -0.335)
- KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2642, phi -0.217)
- KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.1 pts; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2642, phi -0.232)
- override: Player prop expression KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.50 vs 0.41 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +10.27 (adj +1.35) on $50.00, P(profit) 0.5732, adj growth 9.0 bp · B EV +7.19 (adj +1.98) on $43.41, P(profit) 0.72, adj growth 17.6 bp · C EV +3.09 (adj +1.06) on $16.78, P(profit) 0.6593, adj growth 9.3 bp · R EV +0.29 (adj +0.17) on $3.00, P(profit) 0.2997, adj growth 4.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
