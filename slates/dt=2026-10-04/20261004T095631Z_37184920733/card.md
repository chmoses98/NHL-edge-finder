# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-04T09:56:31Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.24 | +25.71 | +6.55 | +20.52 | 0.658 | -63.97 | -82.44 | 42.76 |
| B thesis-diversified (joint) ← optimiser card | 104.51 | +13.01 | +5.40 | +6.79 | 0.660 | -28.64 | -41.76 | 48.16 |
| C best expression per thesis | 54.61 | +8.39 | +3.85 | -5.65 | 0.420 | -32.54 | -32.54 | 34.40 |
| R FUNDED research stakes | 21.00 | +3.09 | +1.17 | +2.00 | 0.628 | -6.90 | -10.67 | 0.00 |

## WPG @ DET  ·  10000 joint draws  ·  250 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_WPG_win | p_overtime | goals | shots DET/WPG | DET/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.57 | 0.43 | 0.00 | 5.98 | 27.2/27.1 | 23.7/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.52 | 0.48 | 0.46 | 5.89 | 27.3/27.1 | 23.8/23.9 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.087 | 0.61 | 0.39 | 0.00 | 6.0 | 32.3/21.8 | 18.9/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.56 | 0.44 | 0.00 | 9.14 | 28.6/28.6 | 23.2/22.4 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.53 | 0.47 | 0.51 | 5.82 | 32.3/21.8 | 18.6/28.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.56 | 0.44 | 0.00 | 3.48 | 26.2/25.9 | 24.3/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cole Perfetti: 1+ goals NO | 73 | 0.794 | 0.777 | +0.050 | +0.033 | $20.00 | FUNDED_RESEARCH | $5 | WPG:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Neal Pionk: 1+ goals NO | 90 | 0.941 | 0.928 | +0.034 | +0.022 | $20.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| J.T. Compher: 1+ goals YES | 14 | 0.180 | 0.167 | +0.032 | +0.019 | $5.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Cole Perfetti: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04WPGDET-WPG2|no; why: higher confidence-adjusted growth (12.54 vs 0.02 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0012 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04WPGDET-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: WPG offense succeeds (4+ goals)
- **Neal Pionk: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: WPG offense succeeds (4+ goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04WPGDET-DETVARVIDSSON33-1|yes; why: higher confidence-adjusted growth (6.17 vs 0.06 bp); alternative not eligible: confidence-adjusted EV +0.0024 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT04WPGDET-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WPG:SUPPRESSED (p 0.4551): highest fidelity KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3801): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3231, phi -0.216)
- KXNHLGOAL-26OCT04WPGDET-WPGNPIONK4-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3231, phi -0.092)
- KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.399, phi -0.176)

portfolios: A EV +4.07 (adj +2.55) on $49.24, P(profit) 0.1799, adj growth 21.9 bp · B EV +3.22 (adj +2.03) on $45.24, P(profit) 0.7902, adj growth 18.7 bp · C EV +2.11 (adj +1.36) on $40.00, P(profit) 0.7472, adj growth 12.9 bp · R EV +0.34 (adj +0.22) on $5.00, P(profit) 0.7939, adj growth 8.2 bp

## UTA @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_UTA_win | p_overtime | goals | shots NYR/UTA | NYR/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.56 | 0.44 | 0.00 | 6.02 | 26.3/26.6 | 23.4/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.47 | 5.98 | 26.3/26.6 | 23.3/22.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.096 | 0.46 | 0.54 | 0.00 | 6.05 | 21.2/31.9 | 28.1/17.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.56 | 0.44 | 0.00 | 9.26 | 27.7/28.0 | 22.2/21.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.47 | 0.53 | 0.44 | 5.9 | 21.1/31.8 | 28.4/18.0 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.055 | 0.47 | 0.53 | 0.00 | 9.17 | 22.2/33.2 | 26.9/16.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## FLA @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_FLA_win | p_overtime | goals | shots ANA/FLA | ANA/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.59 | 0.41 | 0.00 | 6.04 | 28.1/27.6 | 24.4/23.9 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.108 | 0.65 | 0.35 | 0.00 | 6.03 | 33.8/22.1 | 19.3/29.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.50 | 0.50 | 0.45 | 5.93 | 28.1/27.7 | 24.5/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.60 | 0.40 | 0.00 | 9.38 | 29.7/29.4 | 23.7/22.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.55 | 0.45 | 0.47 | 5.94 | 34.0/22.5 | 19.3/30.4 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.082 | 0.71 | 0.29 | 0.00 | 9.37 | 35.1/23.6 | 19.0/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim wins by over 2.5 goals YES | 17 | 0.238 | 0.202 | +0.059 | +0.022 | $3.87 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 79 | 0.868 | 0.824 | +0.066 | +0.022 | $19.83 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim over 3.5 goals scored YES | 40 | 0.485 | 0.437 | +0.068 | +0.021 | $2.39 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida over 4.5 goals scored NO | 74 | 0.808 | 0.771 | +0.054 | +0.018 | $7.77 | FUNDED_RESEARCH | $2 | ANA:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Anaheim wins by over 2.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT04FLAANA-FLA3|no; why: higher confidence-adjusted growth (7.02 vs 6.81 bp); despite a smaller raw edge (+0.059 vs +0.066/contract); relationships: KXNHLSPREAD-26OCT04FLAANA-FLA3|no: REINFORCING (phi 0.219); KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4|yes: REINFORCING (phi 0.498); KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no: REINFORCING (phi 0.245); failure: FLA wins (incl. OT/SO)
- **Florida wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes has the higher standalone adjusted growth (7.02 vs 6.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.219); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes: REINFORCING (phi 0.219); KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4|yes: DUPLICATIVE (phi 0.328); KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no: REINFORCING (phi 0.49); failure: FLA wins by 2+
- **Anaheim over 3.5 goals scored YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4|yes selected over broad KXNHLTEAMTOTAL-26OCT04FLAANA-ANA5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.62 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes: REINFORCING (phi 0.498); KXNHLSPREAD-26OCT04FLAANA-FLA3|no: DUPLICATIVE (phi 0.328); KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no: MOSTLY_INDEPENDENT (phi 0.01); failure: ANA offense suppressed (<= 2 goals)
- **Florida over 4.5 goals scored NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes has the higher standalone adjusted growth (7.02 vs 3.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.245); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes: REINFORCING (phi 0.245); KXNHLSPREAD-26OCT04FLAANA-FLA3|no: REINFORCING (phi 0.49); KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:WINS_BY_2PLUS (p 0.3556): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-FLA3|no (same contract)
- thesis ANA:WINS (p 0.5767): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-FLA3|no (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4746): highest fidelity KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-FLA3|no — Broad expression KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4|yes selected over broad KXNHLTEAMTOTAL-26OCT04FLAANA-ANA5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.62 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLSPREAD-26OCT04FLAANA-ANA3|yes: FUNDED_RESEARCH; family MIXED; loses 33% of the draws where the thesis happens; opposing: failure thesis FLA:WINS (p 0.4233, phi -0.479)
- KXNHLSPREAD-26OCT04FLAANA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2224, phi -0.731)
- KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis ANA:SUPPRESSED (p 0.3169, phi -0.661)
- KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3653, phi -0.643)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT04FLAANA-FLA2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no kept
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT04FLAANA-ANA2|yes less than the minimum stake; KXNHLSPREAD-26OCT04FLAANA-ANA3|yes kept
- override: Broad expression KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4|yes selected over broad KXNHLTEAMTOTAL-26OCT04FLAANA-ANA5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.62 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +10.20 (adj +1.95) on $50.00, P(profit) 0.4686, adj growth 8.4 bp · B EV +3.84 (adj +1.32) on $33.87, P(profit) 0.7708, adj growth 11.7 bp · C EV +1.89 (adj +0.70) on $5.80, P(profit) 0.2385, adj growth 6.1 bp · R EV +1.04 (adj +0.36) on $9.00, P(profit) 0.4152, adj growth 12.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04FLAANA-FLA|no == KXNHLGAME-26OCT04FLAANA-ANA|yes

## CGY @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.62 | 0.38 | 0.00 | 6.01 | 28.3/28.3 | 25.2/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.47 | 5.9 | 28.1/28.0 | 24.8/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.64 | 0.36 | 0.00 | 9.26 | 29.8/29.7 | 24.4/22.9 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.080 | 0.67 | 0.33 | 0.00 | 5.97 | 33.4/22.6 | 19.9/28.8 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.57 | 0.43 | 0.45 | 5.84 | 32.9/22.4 | 19.3/29.4 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.063 | 0.55 | 0.46 | 0.00 | 5.95 | 22.7/33.0 | 29.7/19.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_VGK_win | p_overtime | goals | shots VAN/VGK | VAN/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.45 | 0.55 | 0.00 | 6.02 | 26.7/27.2 | 23.4/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.49 | 5.94 | 26.9/27.2 | 24.0/23.5 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.103 | 0.36 | 0.64 | 0.00 | 6.05 | 21.4/32.7 | 28.2/18.5 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.46 | 0.54 | 0.46 | 5.95 | 21.6/33.1 | 29.7/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.45 | 0.55 | 0.00 | 9.35 | 28.6/29.1 | 22.8/22.8 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.070 | 0.37 | 0.63 | 0.00 | 9.33 | 22.9/34.5 | 26.9/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 15 | 0.240 | 0.193 | +0.082 | +0.034 | $6.89 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 1.5 goals NO | 54 | 0.682 | 0.586 | +0.124 | +0.029 | $6.66 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 2.5 goals NO | 68 | 0.794 | 0.717 | +0.099 | +0.022 | $3.90 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas over 5.5 goals scored NO | 84 | 0.889 | 0.862 | +0.040 | +0.013 | $7.94 | FUNDED_RESEARCH | $2 | VAN:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN3|yes; why: higher confidence-adjusted growth (18.35 vs 10.40 bp); relationships: KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: DUPLICATIVE (phi 0.384); KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: REINFORCING (phi 0.286); KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK6|no: REINFORCING (phi 0.189); failure: VGK wins (incl. OT/SO)
- **Vegas wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes has the higher standalone adjusted growth (18.35 vs 7.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.384); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: DUPLICATIVE (phi 0.384); KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: DUPLICATIVE (phi 0.745); KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK6|no: DUPLICATIVE (phi 0.412); failure: VGK wins by 2+
- **Vegas wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes has the higher standalone adjusted growth (18.35 vs 4.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.286); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: REINFORCING (phi 0.286); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: DUPLICATIVE (phi 0.745); KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK6|no: REINFORCING (phi 0.46); failure: VGK wins by 2+
- **Vegas over 5.5 goals scored NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes has the higher standalone adjusted growth (18.35 vs 2.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.189); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: REINFORCING (phi 0.189); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: DUPLICATIVE (phi 0.412); KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: REINFORCING (phi 0.46); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.2405): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes (same contract)
- thesis VAN:WINS (p 0.4579): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.3643): highest fidelity KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS (p 0.5421, phi -0.612)
- KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.7 pts; opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3181, phi -1.0)
- KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.9 pts; opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3181, phi -0.745)
- KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2724, phi -0.488)

portfolios: A EV +11.44 (adj +2.05) on $50.00, P(profit) 0.5621, adj growth 12.5 bp · B EV +5.96 (adj +2.05) on $25.40, P(profit) 0.6679, adj growth 17.8 bp · C EV +4.40 (adj +1.79) on $8.81, P(profit) 0.3031, adj growth 15.4 bp · R EV +1.71 (adj +0.59) on $7.00, P(profit) 0.6679, adj growth 20.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04VGKVAN-VGK|no == KXNHLGAME-26OCT04VGKVAN-VAN|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
