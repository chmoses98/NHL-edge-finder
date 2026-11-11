# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-11T23:45:46Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +25.98 | +7.99 | +24.69 | 0.711 | -31.27 | -46.82 | 69.73 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +28.29 | +17.06 | +23.82 | 0.663 | -40.70 | -55.32 | 154.62 |
| C best expression per thesis | 132.82 | +23.63 | +11.39 | +18.83 | 0.639 | -45.33 | -59.70 | 98.75 |
| R FUNDED research stakes | 20.00 | +3.08 | +1.96 | -0.11 | 0.483 | -7.88 | -10.47 | 0.00 |

## TBL @ BUF  ·  10000 joint draws  ·  434 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.459 / away 0.541

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_TBL_win | p_overtime | goals | shots BUF/TBL | BUF/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.46 | 0.54 | 0.00 | 5.99 | 27.3/27.4 | 23.8/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.48 | 5.91 | 27.7/27.9 | 24.6/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.49 | 0.51 | 0.00 | 9.26 | 28.9/29.3 | 23.2/23.0 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.081 | 0.40 | 0.60 | 0.00 | 5.97 | 21.7/32.4 | 28.3/18.8 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.49 | 0.51 | 0.48 | 5.91 | 21.7/32.6 | 29.4/18.5 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.058 | 0.55 | 0.45 | 0.00 | 6.0 | 31.7/21.8 | 18.7/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yanni Gourde: 1+ goals NO | 84 | 0.887 | 0.874 | +0.038 | +0.025 | $13.61 | FUNDED_RESEARCH | $4 | TBL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Ryan McLeod: 1+ assists NO | 72 | 0.798 | 0.754 | +0.064 | +0.020 | $13.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ goals NO | 63 | 0.671 | 0.659 | +0.024 | +0.013 | $5.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Full Game: Over 5.5 goals scored NO | 37 | 0.429 | 0.397 | +0.042 | +0.011 | $1.03 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Yanni Gourde: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV11TBBUF-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (10.84 vs 1.27 bp); despite a smaller raw edge (+0.038 vs +0.142/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLAST-26NOV11TBBUF-BUFRMCLEOD71-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV11TBBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLTOTAL-26NOV11TBBUF-6|no: MOSTLY_INDEPENDENT (phi 0.089); failure: TBL offense succeeds (4+ goals)
- **Ryan McLeod: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV11TBBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (4.41 vs 1.61 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV11TBBUF-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV11TBBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.041); KXNHLTOTAL-26NOV11TBBUF-6|no: MOSTLY_INDEPENDENT (phi 0.136); failure: BUF offense succeeds (4+ goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26NOV11TBBUF-6|no; why: higher confidence-adjusted growth (1.61 vs 1.01 bp); despite a smaller raw edge (+0.024 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.999 vs 0.772); relationships: KXNHLGOAL-26NOV11TBBUF-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV11TBBUF-BUFRMCLEOD71-1|no: MOSTLY_INDEPENDENT (phi 0.041); KXNHLTOTAL-26NOV11TBBUF-6|no: REINFORCING (phi 0.18); failure: BUF offense succeeds (4+ goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLAST-26NOV11TBBUF-TBNKUCHEROV86-1|no; why: Broad expression KXNHLTOTAL-26NOV11TBBUF-6|no selected over player prop KXNHLAST-26NOV11TBBUF-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.72 vs 0.73 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26NOV11TBBUF-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi 0.089); KXNHLAST-26NOV11TBBUF-BUFRMCLEOD71-1|no: MOSTLY_INDEPENDENT (phi 0.136); KXNHLGOAL-26NOV11TBBUF-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.18); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:SUPPRESSED (p 0.4045): highest fidelity KXNHLGOAL-26NOV11TBBUF-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV11TBBUF-BUFTTHOMPSON72-1|no (same contract)
- thesis TBL:SUPPRESSED (p 0.3722): highest fidelity KXNHLAST-26NOV11TBBUF-TBNKUCHEROV86-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV11TBBUF-TBNKUCHEROV86-1|no (same contract)
- thesis GAME:LOW_EVENT (p 0.229): highest fidelity KXNHLTOTAL-26NOV11TBBUF-6|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV11TBBUF-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV11TBBUF-TBYGOURDE37-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4055, phi -0.155)
- KXNHLAST-26NOV11TBBUF-BUFRMCLEOD71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3818, phi -0.186)
- KXNHLGOAL-26NOV11TBBUF-BUFTTHOMPSON72-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3818, phi -0.26)
- KXNHLTOTAL-26NOV11TBBUF-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2793, phi -0.539)
- override: Broad expression KXNHLTOTAL-26NOV11TBBUF-6|no selected over player prop KXNHLAST-26NOV11TBBUF-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.72 vs 0.73 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +3.78 (adj +0.71) on $25.00, P(profit) 0.5888, adj growth 6.2 bp · B EV +2.11 (adj +0.91) on $33.76, P(profit) 0.7084, adj growth 8.5 bp · C EV +2.03 (adj +0.33) on $14.03, P(profit) 0.6707, adj growth 2.9 bp · R EV +0.29 (adj +0.14) on $5.00, P(profit) 0.3943, adj growth 5.5 bp

## NYR @ CGY  ·  10000 joint draws  ·  466 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.437 / away 0.563

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_NYR_win | p_overtime | goals | shots CGY/NYR | CGY/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.53 | 0.47 | 0.00 | 6.02 | 28.1/28.0 | 24.5/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.51 | 0.49 | 0.47 | 5.89 | 28.2/28.0 | 24.7/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.50 | 0.50 | 0.00 | 9.23 | 29.6/29.6 | 23.3/23.8 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.075 | 0.63 | 0.37 | 0.00 | 6.01 | 32.9/22.1 | 19.2/28.6 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.54 | 0.46 | 0.48 | 5.86 | 33.2/22.6 | 19.4/29.5 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.059 | 0.44 | 0.56 | 0.00 | 6.02 | 22.5/32.7 | 28.5/19.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aydar Suniev: 1+ goals YES | 16 | 0.212 | 0.198 | +0.043 | +0.029 | $5.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 8 | 0.109 | 0.100 | +0.024 | +0.015 | $2.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 68 | 0.728 | 0.713 | +0.032 | +0.018 | $10.20 | FUNDED_RESEARCH | $3 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Morgan Frost: 1+ goals YES | 23 | 0.268 | 0.257 | +0.026 | +0.015 | $3.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY3|yes; why: higher confidence-adjusted growth (12.42 vs 4.05 bp); despite a smaller raw edge (+0.043 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV11NYRCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV11NYRCGY-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV11NYRCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CGY offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY3|yes; why: higher confidence-adjusted growth (6.43 vs 4.05 bp); despite a smaller raw edge (+0.024 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV11NYRCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV11NYRCGY-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV11NYRCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CGY offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV11NYRCGY-NYR3|no; why: higher confidence-adjusted growth (3.35 vs 2.48 bp); despite a smaller raw edge (+0.032 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV11NYRCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV11NYRCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV11NYRCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: NYR offense succeeds (4+ goals)
- **Morgan Frost: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY3|yes; why: KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY3|yes has the higher standalone adjusted growth (4.05 vs 2.62 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.237); relationships: KXNHLGOAL-26NOV11NYRCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV11NYRCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV11NYRCGY-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CGY:OFFENSE_4PLUS (p 0.3849): highest fidelity KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY3|yes (same contract)
- thesis CGY:WINS (p 0.5129): highest fidelity KXNHLSPREAD-26NOV11NYRCGY-NYR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.2864): highest fidelity KXNHLSPREAD-26NOV11NYRCGY-NYR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV11NYRCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.3882, phi -0.185)
- KXNHLGOAL-26NOV11NYRCGY-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.3882, phi -0.141)
- KXNHLGOAL-26NOV11NYRCGY-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3642, phi -0.219)
- KXNHLGOAL-26NOV11NYRCGY-CGYMFROST16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.3882, phi -0.241)

portfolios: A EV +2.89 (adj +0.87) on $25.00, P(profit) 0.5254, adj growth 7.4 bp · B EV +2.92 (adj +1.85) on $21.51, P(profit) 0.4369, adj growth 16.8 bp · C EV +2.16 (adj +0.87) on $27.59, P(profit) 0.4524, adj growth 7.6 bp · R EV +0.14 (adj +0.08) on $3.00, P(profit) 0.7276, adj growth 2.8 bp

## PHI @ EDM  ·  10000 joint draws  ·  442 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.628 / away 0.372

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_PHI_win | p_overtime | goals | shots EDM/PHI | EDM/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.67 | 0.33 | 0.00 | 6.08 | 26.6/26.2 | 23.4/22.0 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.108 | 0.71 | 0.29 | 0.00 | 5.99 | 31.4/20.5 | 18.0/26.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.47 | 5.97 | 26.7/26.3 | 23.0/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.67 | 0.33 | 0.00 | 9.36 | 28.0/27.6 | 22.7/21.0 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.56 | 0.44 | 0.47 | 5.96 | 31.9/21.0 | 17.8/28.2 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.078 | 0.74 | 0.26 | 0.00 | 9.41 | 33.2/22.2 | 17.8/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Couturier: 1+ goals YES | 10 | 0.150 | 0.136 | +0.043 | +0.030 | $5.04 | FUNDED_RESEARCH | $2 | PHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 16 | 0.217 | 0.202 | +0.048 | +0.032 | $5.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 11 | 0.146 | 0.136 | +0.029 | +0.019 | $3.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 28 | 0.411 | 0.319 | +0.117 | +0.025 | $5.32 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.67) | EVIDENCE_MIXED | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (19.77 vs 15.73 bp); despite a smaller raw edge (+0.043 vs +0.048/contract); relationships: KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV11PHIEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11PHIEDM-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV11PHIEDM-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (19.77 vs 15.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV11PHIEDM-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV11PHIEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: PHI offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV11PHIEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (7.21 vs 5.79 bp); despite a smaller raw edge (+0.029 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV11PHIEDM-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.022); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (6.63 vs 1.03 bp); relationships: KXNHLGOAL-26NOV11PHIEDM-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV11PHIEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, EDM shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PHI:OFFENSE_4PLUS (p 0.3254): highest fidelity KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.2936): highest fidelity KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.502): highest fidelity KXNHLAST-26NOV11PHIEDM-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV11PHIEDM-EDMVPODKOLZIN92-1|yes (same contract)
- KXNHLGOAL-26NOV11PHIEDM-PHISCOUTURIER14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4548, phi -0.202)
- KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4548, phi -0.224)
- KXNHLGOAL-26NOV11PHIEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2936, phi -0.148)
- KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 33% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.1 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.502, phi -0.329)

portfolios: A EV +6.30 (adj +1.62) on $25.00, P(profit) 0.6537, adj growth 14.4 bp · B EV +6.66 (adj +3.52) on $19.65, P(profit) 0.429, adj growth 31.8 bp · C EV +8.32 (adj +3.49) on $24.20, P(profit) 0.6927, adj growth 30.0 bp · R EV +0.82 (adj +0.56) on $2.00, P(profit) 0.1497, adj growth 18.9 bp

## UTA @ VGK  ·  10000 joint draws  ·  466 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.534 / away 0.466

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_UTA_win | p_overtime | goals | shots VGK/UTA | VGK/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.58 | 0.42 | 0.00 | 6.07 | 27.1/27.2 | 23.9/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.45 | 5.95 | 27.2/27.2 | 24.0/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.64 | 0.36 | 0.00 | 9.34 | 28.8/28.7 | 23.3/21.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.080 | 0.65 | 0.35 | 0.00 | 6.04 | 32.2/21.7 | 18.9/28.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.54 | 0.46 | 0.45 | 5.86 | 32.1/21.8 | 18.6/28.7 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.061 | 0.55 | 0.45 | 0.00 | 5.95 | 22.0/32.2 | 28.7/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 4 | 0.084 | 0.071 | +0.041 | +0.029 | $3.97 | FUNDED_RESEARCH | $1 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ goals YES | 16 | 0.223 | 0.206 | +0.054 | +0.037 | $6.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 10 | 0.151 | 0.136 | +0.045 | +0.029 | $4.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 17 | 0.220 | 0.205 | +0.040 | +0.025 | $4.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (41.22 vs 20.65 bp); despite a smaller raw edge (+0.041 vs +0.054/contract); relationships: KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV11UTAVGK-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: VGK offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11UTAVGK-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (20.65 vs 6.45 bp); relationships: KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV11UTAVGK-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: VGK offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (19.51 vs 9.13 bp); relationships: KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: UTA offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV11UTAVGK-UTAMWEEGAR52-1|yes; why: higher confidence-adjusted growth (9.13 vs 1.27 bp); despite a smaller raw edge (+0.040 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV11UTAVGK-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:OFFENSE_4PLUS (p 0.4491): highest fidelity KXNHLAST-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.3475): highest fidelity KXNHLAST-26NOV11UTAVGK-UTAMWEEGAR52-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3419, phi -0.135)
- KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3419, phi -0.194)
- KXNHLGOAL-26NOV11UTAVGK-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4274, phi -0.182)
- KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4274, phi -0.246)

portfolios: A EV +5.16 (adj +2.18) on $25.00, P(profit) 0.4532, adj growth 19.1 bp · B EV +9.18 (adj +6.24) on $20.69, P(profit) 0.5294, adj growth 55.7 bp · C EV +4.86 (adj +3.23) on $17.44, P(profit) 0.395, adj growth 27.8 bp · R EV +0.96 (adj +0.67) on $1.00, P(profit) 0.0836, adj growth 23.7 bp

## NSH @ ANA  ·  10000 joint draws  ·  474 bet sides mapped, 26 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.562 / away 0.438

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_NSH_win | p_overtime | goals | shots ANA/NSH | ANA/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.119 | 0.75 | 0.25 | 0.00 | 9.45 | 30.1/29.5 | 24.7/22.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.113 | 0.77 | 0.23 | 0.00 | 6.09 | 33.9/22.1 | 19.7/28.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.72 | 0.28 | 0.00 | 6.1 | 28.2/27.7 | 25.0/23.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.111 | 0.80 | 0.20 | 0.00 | 9.4 | 35.7/23.7 | 19.6/26.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.53 | 0.47 | 0.44 | 6.02 | 28.4/28.1 | 24.7/24.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.56 | 0.44 | 0.50 | 5.99 | 34.0/22.2 | 19.0/30.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Beckett Sennecke: 1+ goals YES | 33 | 0.413 | 0.391 | +0.067 | +0.045 | $9.79 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 18 | 0.244 | 0.227 | +0.053 | +0.036 | $6.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Jackson LaCombe: 1+ goals YES | 12 | 0.171 | 0.157 | +0.043 | +0.029 | $4.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 62 | 0.683 | 0.666 | +0.046 | +0.029 | $12.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11NSHANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (19.84 vs 18.28 bp); relationships: KXNHLGOAL-26NOV11NSHANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV11NSHANA-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.03); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes has the higher standalone adjusted growth (19.84 vs 18.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV11NSHANA-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: ANA offense suppressed (<= 2 goals)
- **Jackson LaCombe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes has the higher standalone adjusted growth (19.84 vs 16.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV11NSHANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: ANA offense suppressed (<= 2 goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV11NSHANA-ANA2|yes; why: higher confidence-adjusted growth (8.10 vs 7.22 bp); despite a smaller raw edge (+0.046 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.998 vs 0.507); relationships: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.03); KXNHLGOAL-26NOV11NSHANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV11NSHANA-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.5711): highest fidelity KXNHLSPREAD-26NOV11NSHANA-NSH3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:SUPPRESSED (p 0.4555): highest fidelity KXNHLSPREAD-26NOV11NSHANA-NSH3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.453): highest fidelity KXNHLSPREAD-26NOV11NSHANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV11NSHANA-ANA2|yes (same contract)
- KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2432, phi -0.24)
- KXNHLGOAL-26NOV11NSHANA-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2432, phi -0.179)
- KXNHLGOAL-26NOV11NSHANA-ANAJLACOMBE2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2432, phi -0.155)
- KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3175, phi -0.254)

portfolios: A EV +5.02 (adj +1.91) on $25.00, P(profit) 0.5971, adj growth 16.8 bp · B EV +6.05 (adj +4.06) on $32.85, P(profit) 0.5176, adj growth 37.3 bp · C EV +5.31 (adj +3.21) on $38.30, P(profit) 0.5826, adj growth 28.1 bp · R EV +0.59 (adj +0.39) on $3.00, P(profit) 0.4129, adj growth 14.3 bp

## PIT @ SJS  ·  10000 joint draws  ·  464 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.433 / away 0.567

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_PIT_win | p_overtime | goals | shots SJS/PIT | SJS/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.47 | 0.53 | 0.00 | 6.04 | 27.3/27.5 | 23.7/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.46 | 5.96 | 27.6/27.8 | 24.4/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.51 | 0.49 | 0.00 | 9.37 | 29.3/29.6 | 23.5/23.0 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.078 | 0.41 | 0.59 | 0.00 | 6.02 | 22.1/32.7 | 28.5/19.1 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.45 | 0.55 | 0.47 | 5.89 | 22.3/33.2 | 29.7/19.1 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.057 | 0.56 | 0.44 | 0.00 | 6.06 | 32.3/22.1 | 18.8/28.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Erik Karlsson: 1+ goals NO | 82 | 0.855 | 0.845 | +0.025 | +0.015 | $13.61 | FUNDED_RESEARCH | $4 | PIT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Pittsburgh over 3.5 goals scored NO | 50 | 0.569 | 0.532 | +0.051 | +0.015 | $2.94 | FUNDED_RESEARCH | $1 | PIT:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pittsburgh wins by over 1.5 goals NO | 64 | 0.703 | 0.669 | +0.047 | +0.013 | $2.74 | FUNDED_RESEARCH | $1 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tyler Toffoli: 1+ assists YES | 24 | 0.304 | 0.264 | +0.051 | +0.012 | $2.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
- **Erik Karlsson: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no; why: higher confidence-adjusted growth (3.47 vs 1.84 bp); despite a smaller raw edge (+0.025 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: REINFORCING (phi 0.176); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense succeeds (4+ goals)
- **Pittsburgh over 3.5 goals scored NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no; why: Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: REINFORCING (phi 0.176); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: REINFORCING (phi 0.531); KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PIT offense succeeds (4+ goals)
- **Pittsburgh wins by over 1.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no; why: Broad expression KXNHLSPREAD-26NOV11PITSJ-PIT2|no selected over broad KXNHLTEAMTOTAL-26NOV11PITSJ-PIT5|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: REINFORCING (phi 0.531); KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.143); failure: PIT wins by 2+
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV11PITSJ-PIT2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV11PITSJ-PIT2|no has the higher standalone adjusted growth (1.60 vs 1.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.143); they share one thesis budget; relationships: KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: MOSTLY_INDEPENDENT (phi 0.143); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:SUPPRESSED (p 0.3636): highest fidelity KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no (same contract)
- thesis SJS:WINS (p 0.4876): highest fidelity KXNHLSPREAD-26NOV11PITSJ-PIT2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no — Broad expression KXNHLSPREAD-26NOV11PITSJ-PIT2|no selected over broad KXNHLTEAMTOTAL-26NOV11PITSJ-PIT5|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis SJS:OFFENSE_4PLUS (p 0.4037): highest fidelity KXNHLSPREAD-26NOV11PITSJ-PIT2|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV11PITSJ-PIT2|no (same contract)
- KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4203, phi -0.175)
- KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4203, phi -0.978)
- KXNHLSPREAD-26NOV11PITSJ-PIT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:WINS_BY_2PLUS (p 0.2971, phi -1.0)
- KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3833, phi -0.236)
- override: Broad expression KXNHLSPREAD-26NOV11PITSJ-PIT2|no selected over broad KXNHLTEAMTOTAL-26NOV11PITSJ-PIT5|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.83 (adj +0.70) on $25.00, P(profit) 0.5464, adj growth 5.8 bp · B EV +1.35 (adj +0.48) on $21.54, P(profit) 0.6194, adj growth 4.4 bp · C EV +0.95 (adj +0.26) on $11.26, P(profit) 0.5202, adj growth 2.3 bp · R EV +0.29 (adj +0.12) on $6.00, P(profit) 0.6624, adj growth 4.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
