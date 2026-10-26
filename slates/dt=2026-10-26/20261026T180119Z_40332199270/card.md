# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-26T18:01:19Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.65 | +22.41 | +6.51 | +22.12 | 0.650 | -48.56 | -67.22 | 50.08 |
| B thesis-diversified (joint) ← optimiser card | 111.35 | +14.80 | +6.54 | +12.41 | 0.635 | -35.76 | -51.25 | 56.99 |
| C best expression per thesis | 101.94 | +12.48 | +5.30 | +7.82 | 0.689 | -23.97 | -46.46 | 46.28 |
| R FUNDED research stakes | 9.00 | +0.79 | +0.46 | +1.75 | 0.520 | -5.65 | -9.00 | 0.00 |

## LAK @ NYR  ·  10000 joint draws  ·  428 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.548 / away 0.452

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
| Alex Laferriere: 1+ goals YES | 26 | 0.313 | 0.298 | +0.039 | +0.025 | $8.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 66 | 0.711 | 0.697 | +0.035 | +0.021 | $16.97 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Tye Kartye: 1+ goals YES | 15 | 0.180 | 0.171 | +0.021 | +0.012 | $3.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ goals YES | 30 | 0.342 | 0.330 | +0.027 | +0.015 | $5.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes; why: higher confidence-adjusted growth (6.77 vs 2.38 bp); relationships: KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT26LANYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: LAK offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26LANYR-NYRJMILLER8-1|no; why: higher confidence-adjusted growth (4.58 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT26LANYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NYR offense succeeds (4+ goals)
- **Tye Kartye: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26LANYR-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (2.47 vs 0.13 bp); despite a smaller raw edge (+0.021 vs +0.080/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: NYR offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes has the higher standalone adjusted growth (6.77 vs 2.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT26LANYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:OFFENSE_4PLUS (p 0.3331): highest fidelity KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.384): highest fidelity KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.3964): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT26LANYR-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4461, phi -0.274)
- KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3964, phi -0.242)
- KXNHLGOAL-26OCT26LANYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.384, phi -0.19)
- KXNHLGOAL-26OCT26LANYR-LAAPANARIN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4461, phi -0.284)

portfolios: A EV +4.67 (adj +2.83) on $49.65, P(profit) 0.5002, adj growth 22.6 bp · B EV +3.01 (adj +1.83) on $34.20, P(profit) 0.5002, adj growth 15.9 bp · C EV +2.10 (adj +1.30) on $25.45, P(profit) 0.3128, adj growth 11.4 bp · R EV +0.26 (adj +0.16) on $5.00, P(profit) 0.7111, adj growth 5.4 bp

## TOR @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.435 / away 0.565

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
| Gavin McKenna: 1+ assists NO | 67 | 0.757 | 0.709 | +0.072 | +0.023 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
| Jonathan Castagna: 1+ goals YES | 13 | 0.166 | 0.153 | +0.028 | +0.015 | $4.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ goals NO | 58 | 0.618 | 0.608 | +0.021 | +0.010 | $4.40 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT26TORCGY-TORJMCCABE22-1|yes; why: higher confidence-adjusted growth (12.20 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT26TORCGY-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT26TORCGY-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: TOR offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (5.45 vs 4.03 bp); relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT26TORCGY-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.118); failure: TOR offense succeeds (4+ goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR3|no; why: higher confidence-adjusted growth (4.32 vs 3.14 bp); despite a smaller raw edge (+0.028 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT26TORCGY-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT26TORCGY-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.026); failure: CGY offense suppressed (<= 2 goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26TORCGY-TORGMCKENNA92-1|no; why: Player prop expression KXNHLGOAL-26OCT26TORCGY-TORAMATTHEWS34-1|no selected over broad KXNHLSPREAD-26OCT26TORCGY-TOR3|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.73 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT26TORCGY-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.118); KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CGY shot control · normal event (5-7) · decided (2+) 0.09.
- thesis TOR:OFFENSE_4PLUS (p 0.3987): highest fidelity KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.3845): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT26TORCGY-TORGMCKENNA92-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.4013): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT26TORCGY-TOR3|no (same contract)
- KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3845, phi -0.192)
- KXNHLAST-26OCT26TORCGY-TORGMCKENNA92-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3987, phi -0.214)
- KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.3761, phi -0.193)
- KXNHLGOAL-26OCT26TORCGY-TORAMATTHEWS34-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3987, phi -0.277)
- override: Player prop expression KXNHLGOAL-26OCT26TORCGY-TORAMATTHEWS34-1|no selected over broad KXNHLSPREAD-26OCT26TORCGY-TOR3|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.73 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +8.50 (adj +1.66) on $50.00, P(profit) 0.5605, adj growth 12.2 bp · B EV +5.36 (adj +2.49) on $34.71, P(profit) 0.6294, adj growth 21.7 bp · C EV +6.43 (adj +2.84) on $48.81, P(profit) 0.7542, adj growth 24.7 bp · R EV +0.07 (adj +0.03) on $2.00, P(profit) 0.6183, adj growth 1.2 bp

## DET @ EDM  ·  10000 joint draws  ·  428 bet sides mapped, 7 +EV candidates, 4 on card

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
| J.T. Compher: 1+ goals YES | 11 | 0.144 | 0.133 | +0.027 | +0.016 | $4.25 | FUNDED_RESEARCH | $2 | DET:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 63 | 0.747 | 0.668 | +0.101 | +0.021 | $19.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 26 | 0.303 | 0.291 | +0.030 | +0.018 | $9.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Leon Draisaitl: 1+ assists NO | 41 | 0.490 | 0.445 | +0.063 | +0.018 | $8.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.74) | EVIDENCE_MIXED | D |
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT26DETEDM-DETEFINNIE58-1|yes; why: higher confidence-adjusted growth (5.30 vs 0.23 bp); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: DET offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no; why: higher confidence-adjusted growth (4.39 vs 2.92 bp); relationships: KXNHLGOAL-26OCT26DETEDM-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.208); KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.129); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (3.46 vs 1.98 bp); despite a smaller raw edge (+0.030 vs +0.086/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT26DETEDM-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.208); KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.235); failure: EDM offense suppressed (<= 2 goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no; why: second expression of the same thesis: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (4.39 vs 2.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.129); they share one thesis budget; relationships: KXNHLGOAL-26OCT26DETEDM-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.129); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.235); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:SUPPRESSED (p 0.2609): highest fidelity KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.5412): highest fidelity KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:OFFENSE_4PLUS (p 0.325): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT26DETEDM-DETJCOMPHER37-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4592, phi -0.182)
- KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.2 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5412, phi -0.35)
- KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2609, phi -0.227)
- KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 26% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5412, phi -0.296)

portfolios: A EV +9.24 (adj +2.02) on $50.00, P(profit) 0.6939, adj growth 15.3 bp · B EV +6.42 (adj +2.22) on $42.44, P(profit) 0.6059, adj growth 19.4 bp · C EV +3.95 (adj +1.16) on $27.68, P(profit) 0.8654, adj growth 10.2 bp · R EV +0.46 (adj +0.27) on $2.00, P(profit) 0.1437, adj growth 8.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
