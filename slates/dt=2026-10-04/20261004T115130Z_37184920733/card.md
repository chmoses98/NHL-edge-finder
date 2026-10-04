# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-04T11:51:30Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +20.35 | +7.22 | +19.15 | 0.627 | -48.53 | -64.53 | 58.38 |
| B thesis-diversified (joint) ← optimiser card | 113.69 | +16.09 | +6.50 | +10.51 | 0.667 | -27.64 | -44.19 | 58.20 |
| C best expression per thesis | 35.88 | +6.66 | +2.91 | -8.99 | 0.439 | -35.88 | -35.88 | 25.71 |
| R FUNDED research stakes | 23.00 | +3.74 | +1.64 | +3.48 | 0.540 | -11.39 | -12.27 | 0.00 |

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
| Neal Pionk: 1+ goals NO | 90 | 0.940 | 0.928 | +0.033 | +0.022 | $15.00 | FUNDED_RESEARCH | $4 | WPG:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Cole Perfetti: 1+ goals NO | 73 | 0.790 | 0.774 | +0.046 | +0.030 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| J.T. Compher: 1+ goals YES | 14 | 0.175 | 0.164 | +0.027 | +0.015 | $4.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no; why: higher confidence-adjusted growth (12.97 vs 10.45 bp); despite a smaller raw edge (+0.033 vs +0.046/contract); relationships: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: WPG offense succeeds (4+ goals)
- **Cole Perfetti: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04WPGDET-WPG2|no; why: higher confidence-adjusted growth (10.45 vs 0.13 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04WPGDET-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: WPG offense succeeds (4+ goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT04WPGDET-WPG2|no; why: higher confidence-adjusted growth (4.10 vs 0.13 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04WPGDET-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WPG:SUPPRESSED (p 0.4595): highest fidelity KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.38): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT04WPGDET-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3274, phi -0.115)
- KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3274, phi -0.223)
- KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3989, phi -0.191)

portfolios: A EV +1.85 (adj +1.18) on $41.68, P(profit) 0.6673, adj growth 11.4 bp · B EV +2.26 (adj +1.42) on $34.30, P(profit) 0.7857, adj growth 13.2 bp · C EV +1.25 (adj +0.81) on $20.00, P(profit) 0.7901, adj growth 7.5 bp · R EV +0.15 (adj +0.10) on $4.00, P(profit) 0.9396, adj growth 3.8 bp

## UTA @ NYR  ·  10000 joint draws  ·  340 bet sides mapped, 2 +EV candidates, 2 on card


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
| Tye Kartye: 1+ goals YES | 10 | 0.142 | 0.129 | +0.036 | +0.023 | $5.74 | FUNDED_RESEARCH | $2 | NYR:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 70 | 0.849 | 0.743 | +0.135 | +0.028 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
- **Tye Kartye: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT04UTANYR-9|yes; why: higher confidence-adjusted growth (11.53 vs 0.27 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.9 vs 0.373); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: NYR offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT04UTANYR-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (8.33 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT04UTANYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NYR:OFFENSE_4PLUS (p 0.4223): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis UTA:SUPPRESSED (p 0.4374): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT04UTANYR-NYRTKARTYE24-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3568, phi -0.179)
- KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.4 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3522, phi -0.167)

portfolios: A EV +5.92 (adj +2.41) on $24.97, P(profit) 0.1419, adj growth 20.2 bp · B EV +5.69 (adj +2.00) on $25.74, P(profit) 0.8713, adj growth 17.7 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.67 (adj +0.43) on $2.00, P(profit) 0.1419, adj growth 13.7 bp

## FLA @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 4 on card


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
| Anaheim wins by over 1.5 goals YES | 26 | 0.351 | 0.303 | +0.078 | +0.030 | $4.26 | FUNDED_RESEARCH | $2 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 78 | 0.862 | 0.819 | +0.070 | +0.027 | $16.91 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 68 | 0.769 | 0.722 | +0.074 | +0.027 | $6.93 | FUNDED_RESEARCH | $2 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 2.5 goals YES | 17 | 0.237 | 0.201 | +0.057 | +0.021 | $1.45 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | DIRECT (0.68) | EVIDENCE_MIXED | D |
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT04FLAANA-FLA3|no; why: higher confidence-adjusted growth (9.62 vs 9.57 bp); relationships: KXNHLSPREAD-26OCT04FLAANA-FLA3|no: REINFORCING (phi 0.294); KXNHLSPREAD-26OCT04FLAANA-FLA2|no: DUPLICATIVE (phi 0.403); KXNHLSPREAD-26OCT04FLAANA-ANA3|yes: DUPLICATIVE (phi 0.758); failure: FLA wins (incl. OT/SO)
- **Florida wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04FLAANA-ANA2|yes has the higher standalone adjusted growth (9.62 vs 9.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.294); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04FLAANA-ANA2|yes: REINFORCING (phi 0.294); KXNHLSPREAD-26OCT04FLAANA-FLA2|no: DUPLICATIVE (phi 0.729); KXNHLSPREAD-26OCT04FLAANA-ANA3|yes: REINFORCING (phi 0.223); failure: FLA wins by 2+
- **Florida wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04FLAANA-ANA2|yes has the higher standalone adjusted growth (9.62 vs 7.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.403); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04FLAANA-ANA2|yes: DUPLICATIVE (phi 0.403); KXNHLSPREAD-26OCT04FLAANA-FLA3|no: DUPLICATIVE (phi 0.729); KXNHLSPREAD-26OCT04FLAANA-ANA3|yes: DUPLICATIVE (phi 0.305); failure: FLA wins by 2+
- **Anaheim wins by over 2.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT04FLAANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04FLAANA-ANA2|yes has the higher standalone adjusted growth (9.62 vs 6.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.758); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04FLAANA-ANA2|yes: DUPLICATIVE (phi 0.758); KXNHLSPREAD-26OCT04FLAANA-FLA3|no: REINFORCING (phi 0.223); KXNHLSPREAD-26OCT04FLAANA-FLA2|no: DUPLICATIVE (phi 0.305); failure: FLA wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:WINS_BY_2PLUS (p 0.3513): highest fidelity KXNHLSPREAD-26OCT04FLAANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-ANA2|yes (same contract)
- thesis ANA:WINS (p 0.5717): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.4127): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT04FLAANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS (p 0.4283, phi -0.637)
- KXNHLSPREAD-26OCT04FLAANA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2307, phi -0.729)
- KXNHLSPREAD-26OCT04FLAANA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2307, phi -1.0)
- KXNHLSPREAD-26OCT04FLAANA-ANA3|yes: FUNDED_RESEARCH; family MIXED; loses 32% of the draws where the thesis happens; opposing: failure thesis FLA:WINS (p 0.4283, phi -0.483)

portfolios: A EV +6.48 (adj +2.24) on $41.68, P(profit) 0.5131, adj growth 17.1 bp · B EV +3.92 (adj +1.47) on $29.55, P(profit) 0.7693, adj growth 13.2 bp · C EV +2.65 (adj +1.01) on $9.30, P(profit) 0.3513, adj growth 8.8 bp · R EV +1.55 (adj +0.58) on $10.00, P(profit) 0.3513, adj growth 19.1 bp

## CGY @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.64 | 0.36 | 0.00 | 5.98 | 28.0/28.0 | 24.9/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.46 | 5.86 | 28.3/28.2 | 24.9/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.62 | 0.38 | 0.00 | 9.17 | 29.8/29.8 | 24.4/22.8 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.075 | 0.66 | 0.34 | 0.00 | 6.01 | 33.1/22.4 | 19.7/28.7 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.58 | 0.42 | 0.46 | 5.92 | 33.4/22.5 | 19.3/30.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.59 | 0.41 | 0.00 | 3.45 | 27.0/27.0 | 25.4/24.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 10 +EV candidates, 2 on card


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
| Vancouver wins by over 1.5 goals YES | 15 | 0.226 | 0.185 | +0.067 | +0.026 | $5.19 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 2.5 goals NO | 68 | 0.770 | 0.723 | +0.075 | +0.028 | $18.91 | FUNDED_RESEARCH | $5 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT04VGKVAN-VGK3|no; why: higher confidence-adjusted growth (11.25 vs 7.84 bp); despite a smaller raw edge (+0.067 vs +0.075/contract); relationships: KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: REINFORCING (phi 0.295); failure: VGK wins (incl. OT/SO)
- **Vegas wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes has the higher standalone adjusted growth (11.25 vs 7.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.295); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: REINFORCING (phi 0.295); failure: VGK wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.2257): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VGK3|no (same contract)
- thesis VAN:WINS (p 0.433): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VGK3|no (same contract)
- thesis VGK:SUPPRESSED (p 0.3377): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VGK3|no (same contract)
- KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS (p 0.567, phi -0.618)
- KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3472, phi -0.749)

portfolios: A EV +6.10 (adj +1.39) on $41.68, P(profit) 0.6928, adj growth 9.8 bp · B EV +4.23 (adj +1.61) on $24.10, P(profit) 0.7704, adj growth 14.1 bp · C EV +2.76 (adj +1.09) on $6.58, P(profit) 0.2257, adj growth 9.5 bp · R EV +1.38 (adj +0.53) on $7.00, P(profit) 0.7704, adj growth 17.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
