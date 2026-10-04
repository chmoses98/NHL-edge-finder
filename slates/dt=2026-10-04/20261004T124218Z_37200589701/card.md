# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-04T12:42:18Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +25.70 | +7.96 | +21.18 | 0.686 | -37.49 | -51.45 | 67.07 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +22.36 | +10.17 | +20.37 | 0.646 | -32.29 | -47.03 | 90.69 |
| C best expression per thesis | 54.75 | +13.29 | +6.69 | +5.31 | 0.569 | -27.86 | -37.70 | 58.26 |
| R FUNDED research stakes | 23.00 | +2.69 | +1.34 | +1.87 | 0.619 | -9.73 | -12.83 | 0.00 |

## WPG @ DET  ·  10000 joint draws  ·  250 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_WPG_win | p_overtime | goals | shots DET/WPG | DET/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.55 | 0.45 | 0.00 | 6.0 | 27.3/27.2 | 23.8/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.47 | 5.9 | 27.4/27.1 | 23.9/24.1 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.085 | 0.64 | 0.36 | 0.00 | 6.01 | 32.7/21.8 | 19.1/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.53 | 0.47 | 0.00 | 9.19 | 28.8/28.6 | 22.7/22.9 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.53 | 0.47 | 0.45 | 5.8 | 32.1/21.5 | 18.4/28.8 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.54 | 0.46 | 0.49 | 2.81 | 25.8/25.6 | 24.1/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Neal Pionk: 1+ goals NO | 90 | 0.940 | 0.928 | +0.033 | +0.022 | $13.50 | FUNDED_RESEARCH | $4 | WPG:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Cole Perfetti: 1+ goals NO | 73 | 0.790 | 0.774 | +0.046 | +0.030 | $13.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| J.T. Compher: 1+ goals YES | 14 | 0.175 | 0.164 | +0.027 | +0.015 | $3.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no; why: higher confidence-adjusted growth (12.97 vs 10.45 bp); despite a smaller raw edge (+0.033 vs +0.046/contract); relationships: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: WPG offense succeeds (4+ goals)
- **Cole Perfetti: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04WPGDET-WPG2|no; why: higher confidence-adjusted growth (10.45 vs 0.13 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04WPGDET-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: WPG offense succeeds (4+ goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT04WPGDET-WPG2|no; why: higher confidence-adjusted growth (4.10 vs 0.13 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04WPGDET-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WPG:SUPPRESSED (p 0.4595): highest fidelity KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.38): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT04WPGDET-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3274, phi -0.115)
- KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3274, phi -0.223)
- KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3989, phi -0.191)

portfolios: A EV +1.44 (adj +0.94) on $32.51, P(profit) 0.6673, adj growth 9.1 bp · B EV +2.03 (adj +1.28) on $30.86, P(profit) 0.7857, adj growth 12.0 bp · C EV +1.25 (adj +0.81) on $20.00, P(profit) 0.7901, adj growth 7.5 bp · R EV +0.15 (adj +0.10) on $4.00, P(profit) 0.9396, adj growth 3.8 bp

## UTA @ NYR  ·  10000 joint draws  ·  340 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_UTA_win | p_overtime | goals | shots NYR/UTA | NYR/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.57 | 0.43 | 0.00 | 5.98 | 26.3/26.6 | 23.3/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.54 | 0.46 | 0.49 | 5.88 | 26.3/26.6 | 23.4/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.59 | 0.41 | 0.00 | 9.25 | 27.9/28.2 | 22.6/21.6 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.088 | 0.53 | 0.47 | 0.00 | 5.99 | 21.0/31.8 | 28.2/17.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.47 | 0.53 | 0.47 | 5.91 | 21.2/31.9 | 28.4/18.0 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.054 | 0.66 | 0.34 | 0.00 | 6.0 | 30.8/21.2 | 18.6/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tye Kartye: 1+ goals YES | 10 | 0.142 | 0.129 | +0.036 | +0.023 | $5.23 | FUNDED_RESEARCH | $2 | NYR:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 70 | 0.849 | 0.743 | +0.135 | +0.028 | $18.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ assists NO | 71 | 0.786 | 0.738 | +0.061 | +0.013 | $12.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Tye Kartye: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT04UTANYR-9|yes; why: higher confidence-adjusted growth (11.53 vs 0.27 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.9 vs 0.373); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT04UTANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.032); failure: NYR offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT04UTANYR-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (8.33 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT04UTANYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT04UTANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: UTA offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT04UTANYR-NYRPDOROFEYEV16-2|no; why: higher confidence-adjusted growth (1.97 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT04UTANYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NYR:OFFENSE_4PLUS (p 0.4223): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis UTA:SUPPRESSED (p 0.4374): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis NYR:SUPPRESSED (p 0.3568): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT04UTANYR-NYRTKARTYE24-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3568, phi -0.179)
- KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.4 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3522, phi -0.167)
- KXNHLAST-26OCT04UTANYR-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.4223, phi -0.182)

portfolios: A EV +5.71 (adj +2.12) on $32.49, P(profit) 0.7211, adj growth 18.6 bp · B EV +6.22 (adj +2.05) on $36.07, P(profit) 0.7211, adj growth 18.4 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.67 (adj +0.43) on $2.00, P(profit) 0.1419, adj growth 13.7 bp

## FLA @ ANA  ·  10000 joint draws  ·  356 bet sides mapped, 16 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_FLA_win | p_overtime | goals | shots ANA/FLA | ANA/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.59 | 0.41 | 0.00 | 6.03 | 28.2/27.8 | 24.6/24.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.112 | 0.63 | 0.37 | 0.00 | 6.05 | 33.9/22.4 | 19.6/29.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.53 | 0.47 | 0.50 | 5.98 | 28.3/28.0 | 24.8/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.61 | 0.39 | 0.00 | 9.49 | 29.7/29.2 | 23.7/22.4 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.56 | 0.44 | 0.45 | 5.95 | 33.8/22.3 | 19.1/30.3 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.081 | 0.66 | 0.34 | 0.00 | 9.39 | 35.4/23.9 | 19.1/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 19 | 0.267 | 0.246 | +0.066 | +0.045 | $11.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 65 | 0.713 | 0.694 | +0.048 | +0.028 | $18.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ assists YES | 24 | 0.374 | 0.277 | +0.121 | +0.024 | $5.32 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
| Sandis Vilmanis: 1+ goals YES | 12 | 0.153 | 0.141 | +0.025 | +0.013 | $3.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes; why: higher confidence-adjusted growth (27.50 vs 10.91 bp); despite a smaller raw edge (+0.066 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.855 vs 0.464); relationships: KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT04FLAANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.061); KXNHLGOAL-26OCT04FLAANA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: ANA offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes; why: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes has the higher standalone adjusted growth (10.91 vs 7.68 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT04FLAANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT04FLAANA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: FLA offense succeeds (4+ goals)
- **Alex Killorn: 1+ assists YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (27.50 vs 6.76 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.061); they share one thesis budget; relationships: KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.061); KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT04FLAANA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: ANA offense suppressed (<= 2 goals)
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT04FLAANA-FLACVERHAEGHE23-1|yes; why: higher confidence-adjusted growth (3.49 vs 1.31 bp); despite a smaller raw edge (+0.025 vs +0.085/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT04FLAANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4779): highest fidelity KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4|yes less than the minimum stake; KXNHLAST-26OCT04FLAANA-ANAAKILLORN17-1|yes kept
- thesis ANA:WINS_BY_2PLUS (p 0.3513): highest fidelity KXNHLSPREAD-26OCT04FLAANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5717): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3154, phi -0.24)
- KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3713, phi -0.258)
- KXNHLAST-26OCT04FLAANA-ANAAKILLORN17-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3154, phi -0.249)
- KXNHLGOAL-26OCT04FLAANA-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4127, phi -0.171)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4|yes less than the minimum stake; KXNHLAST-26OCT04FLAANA-ANAAKILLORN17-1|yes kept

portfolios: A EV +9.50 (adj +2.29) on $32.51, P(profit) 0.6338, adj growth 19.4 bp · B EV +8.25 (adj +4.21) on $38.11, P(profit) 0.5154, adj growth 37.0 bp · C EV +7.56 (adj +3.76) on $22.31, P(profit) 0.4031, adj growth 32.4 bp · R EV +0.36 (adj +0.21) on $5.00, P(profit) 0.7134, adj growth 7.4 bp

## CGY @ SEA  ·  10000 joint draws  ·  334 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.64 | 0.36 | 0.00 | 5.98 | 28.0/28.0 | 24.9/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.46 | 5.86 | 28.3/28.2 | 24.9/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.62 | 0.38 | 0.00 | 9.17 | 29.8/29.8 | 24.4/22.8 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.075 | 0.66 | 0.34 | 0.00 | 6.01 | 33.1/22.4 | 19.7/28.7 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.58 | 0.42 | 0.46 | 5.92 | 33.4/22.5 | 19.3/30.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.59 | 0.41 | 0.00 | 3.45 | 27.0/27.0 | 25.4/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Winterton: 1+ goals YES | 12 | 0.165 | 0.150 | +0.037 | +0.022 | $5.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brandon Montour: 1+ goals NO | 86 | 0.892 | 0.881 | +0.024 | +0.012 | $18.00 | FUNDED_RESEARCH | $5 | SEA:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes; why: higher confidence-adjusted growth (9.75 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0019 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (2.88 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0011 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4174): highest fidelity KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes (same contract)
- thesis SEA:SUPPRESSED (p 0.3674): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3674, phi -0.196)
- KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.4174, phi -0.14)

portfolios: A EV +2.41 (adj +1.41) on $19.97, P(profit) 0.1648, adj growth 12.0 bp · B EV +2.05 (adj +1.18) on $23.27, P(profit) 0.1648, adj growth 10.5 bp · C EV +1.72 (adj +1.03) on $5.86, P(profit) 0.1648, adj growth 8.9 bp · R EV +0.14 (adj +0.07) on $5.00, P(profit) 0.8925, adj growth 2.6 bp

## VGK @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_VGK_win | p_overtime | goals | shots VAN/VGK | VAN/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.41 | 0.59 | 0.00 | 6.02 | 27.1/27.6 | 23.7/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.48 | 0.52 | 0.47 | 5.93 | 26.9/27.4 | 24.0/23.6 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.111 | 0.34 | 0.66 | 0.00 | 5.96 | 21.3/32.7 | 28.2/18.6 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.47 | 0.53 | 0.48 | 5.89 | 21.6/32.5 | 29.3/18.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.37 | 0.63 | 0.00 | 9.27 | 28.4/29.0 | 22.2/23.3 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.071 | 0.36 | 0.64 | 0.00 | 9.3 | 23.0/34.3 | 27.1/18.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 15 | 0.226 | 0.185 | +0.067 | +0.026 | $4.67 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 2.5 goals NO | 68 | 0.770 | 0.723 | +0.075 | +0.028 | $17.01 | FUNDED_RESEARCH | $5 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT04VGKVAN-VGK3|no; why: higher confidence-adjusted growth (11.25 vs 7.84 bp); despite a smaller raw edge (+0.067 vs +0.075/contract); relationships: KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: REINFORCING (phi 0.295); failure: VGK wins (incl. OT/SO)
- **Vegas wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes has the higher standalone adjusted growth (11.25 vs 7.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.295); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: REINFORCING (phi 0.295); failure: VGK wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.2257): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VGK3|no (same contract)
- thesis VAN:WINS (p 0.433): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VGK3|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3439): highest fidelity KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VGK3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS (p 0.567, phi -0.618)
- KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3472, phi -0.749)

portfolios: A EV +6.63 (adj +1.20) on $32.51, P(profit) 0.6528, adj growth 8.0 bp · B EV +3.80 (adj +1.45) on $21.68, P(profit) 0.7704, adj growth 12.8 bp · C EV +2.76 (adj +1.09) on $6.58, P(profit) 0.2257, adj growth 9.5 bp · R EV +1.38 (adj +0.53) on $7.00, P(profit) 0.7704, adj growth 17.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
