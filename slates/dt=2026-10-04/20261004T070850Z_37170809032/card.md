# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-04T07:08:50Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +28.32 | +7.32 | +30.57 | 0.617 | -70.47 | -90.01 | 44.69 |
| B thesis-diversified (joint) ← optimiser card | 94.75 | +12.24 | +5.04 | +6.95 | 0.654 | -27.81 | -36.05 | 45.19 |
| C best expression per thesis | 68.20 | +8.22 | +3.87 | +6.01 | 0.730 | -20.88 | -20.88 | 35.23 |
| R FUNDED research stakes | 19.00 | +3.71 | +1.44 | +0.10 | 0.629 | -7.54 | -11.36 | 0.00 |

## WPG @ DET  ·  10000 joint draws  ·  250 bet sides mapped, 3 +EV candidates, 3 on card


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
| Neal Pionk: 1+ goals NO | 90 | 0.941 | 0.929 | +0.034 | +0.023 | $16.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Cole Perfetti: 1+ goals NO | 73 | 0.794 | 0.777 | +0.050 | +0.033 | $15.23 | FUNDED_RESEARCH | $4 | WPG:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Isak Rosen: 1+ goals NO | 86 | 0.888 | 0.879 | +0.020 | +0.010 | $14.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
- **Neal Pionk: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT04WPGDET-WPGIROSEN27-1|no: MOSTLY_INDEPENDENT (phi -0.025); failure: WPG offense succeeds (4+ goals)
- **Cole Perfetti: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT04WPGDET-WPGMSCHEIFELE55-1|no; why: higher confidence-adjusted growth (12.54 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT04WPGDET-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT04WPGDET-WPGIROSEN27-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: WPG offense succeeds (4+ goals)
- **Isak Rosen: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no has the higher standalone adjusted growth (12.54 vs 2.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT04WPGDET-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WPG:SUPPRESSED (p 0.4551): highest fidelity KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no (same contract)
- KXNHLGOAL-26OCT04WPGDET-WPGNPIONK4-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3231, phi -0.092)
- KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3231, phi -0.216)
- KXNHLGOAL-26OCT04WPGDET-WPGIROSEN27-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3231, phi -0.153)

portfolios: A EV +2.14 (adj +1.36) on $50.00, P(profit) 0.6624, adj growth 12.9 bp · B EV +2.00 (adj +1.28) on $46.83, P(profit) 0.6624, adj growth 12.2 bp · C EV +2.11 (adj +1.39) on $40.00, P(profit) 0.7472, adj growth 13.2 bp · R EV +0.27 (adj +0.18) on $4.00, P(profit) 0.7939, adj growth 6.7 bp

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

## FLA @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 3 on card


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
| Florida wins by over 2.5 goals NO | 78 | 0.868 | 0.821 | +0.075 | +0.029 | $20.00 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 2.5 goals YES | 16 | 0.238 | 0.197 | +0.069 | +0.027 | $5.81 | FUNDED_RESEARCH | $2 | ANA:WINS_BY_2PLUS | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Florida over 4.5 goals scored NO | 74 | 0.808 | 0.769 | +0.054 | +0.015 | $1.99 | FUNDED_RESEARCH | $1 | ANA:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes; why: higher confidence-adjusted growth (11.50 vs 11.45 bp); wins across more scripts (relative breadth 1.036 vs 0.438); relationships: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes: REINFORCING (phi 0.219); KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no: REINFORCING (phi 0.49); failure: FLA wins by 2+
- **Anaheim wins by over 2.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT04FLAANA-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT04FLAANA-FLA3|no has the higher standalone adjusted growth (11.50 vs 11.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.219); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04FLAANA-FLA3|no: REINFORCING (phi 0.219); KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no: REINFORCING (phi 0.245); failure: FLA wins (incl. OT/SO)
- **Florida over 4.5 goals scored NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04FLAANA-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT04FLAANA-FLA3|no has the higher standalone adjusted growth (11.50 vs 2.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.490); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04FLAANA-FLA3|no: REINFORCING (phi 0.49); KXNHLSPREAD-26OCT04FLAANA-ANA3|yes: REINFORCING (phi 0.245); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:WINS (p 0.5767): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-FLA3|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3556): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-FLA3|no (same contract)
- thesis FLA:SUPPRESSED (p 0.4217): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-FLA3|no (same contract)
- KXNHLSPREAD-26OCT04FLAANA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2224, phi -0.731)
- KXNHLSPREAD-26OCT04FLAANA-ANA3|yes: FUNDED_RESEARCH; family MIXED; loses 33% of the draws where the thesis happens; opposing: failure thesis FLA:WINS (p 0.4233, phi -0.479)
- KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3653, phi -0.643)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT04FLAANA-FLA2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no kept

portfolios: A EV +10.88 (adj +1.77) on $50.00, P(profit) 0.5767, adj growth 6.0 bp · B EV +4.42 (adj +1.72) on $27.80, P(profit) 0.7708, adj growth 15.4 bp · C EV +1.91 (adj +0.74) on $20.00, P(profit) 0.8675, adj growth 7.0 bp · R EV +1.36 (adj +0.53) on $8.00, P(profit) 0.2385, adj growth 18.1 bp
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

## VGK @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 10 +EV candidates, 4 on card


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
| Vancouver wins by over 1.5 goals YES | 15 | 0.240 | 0.193 | +0.082 | +0.034 | $6.35 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 4.5 goals scored YES | 13 | 0.196 | 0.160 | +0.058 | +0.022 | $1.81 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_MIXED | D |
| Vegas wins by over 1.5 goals NO | 55 | 0.682 | 0.593 | +0.115 | +0.026 | $1.68 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 2.5 goals NO | 68 | 0.794 | 0.717 | +0.099 | +0.022 | $10.28 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN3|yes; why: higher confidence-adjusted growth (18.35 vs 10.40 bp); relationships: KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN5|yes: REINFORCING (phi 0.508); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: DUPLICATIVE (phi 0.384); KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: REINFORCING (phi 0.286); failure: VGK wins (incl. OT/SO)
- **Vancouver over 4.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes has the higher standalone adjusted growth (18.35 vs 9.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.508); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: REINFORCING (phi 0.508); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: REINFORCING (phi 0.299); KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: REINFORCING (phi 0.233); failure: VGK wins (incl. OT/SO)
- **Vegas wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: Broad expression KXNHLSPREAD-26OCT04VGKVAN-VGK2|no selected over broad KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK6|no because adjusted EV is 1.3 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: DUPLICATIVE (phi 0.384); KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN5|yes: REINFORCING (phi 0.299); KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: DUPLICATIVE (phi 0.745); failure: VGK wins by 2+
- **Vegas wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes has the higher standalone adjusted growth (18.35 vs 4.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.286); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: REINFORCING (phi 0.286); KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN5|yes: REINFORCING (phi 0.233); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: DUPLICATIVE (phi 0.745); failure: VGK wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.2405): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3643): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VGK3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.4579): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes — Broad expression KXNHLSPREAD-26OCT04VGKVAN-VGK2|no selected over broad KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK6|no because adjusted EV is 1.3 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS (p 0.5421, phi -0.612)
- KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN5|yes: FUNDED_RESEARCH; family MIXED; loses 46% of the draws where the thesis happens; opposing: failure thesis VGK:WINS (p 0.5421, phi -0.445)
- KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.7 pts; opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3181, phi -1.0)
- KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.9 pts; opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3181, phi -0.745)
- override: Broad expression KXNHLSPREAD-26OCT04VGKVAN-VGK2|no selected over broad KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK6|no because adjusted EV is 1.3 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +15.30 (adj +4.19) on $50.00, P(profit) 0.4579, adj growth 25.9 bp · B EV +5.82 (adj +2.04) on $20.12, P(profit) 0.3002, adj growth 17.7 bp · C EV +4.21 (adj +1.74) on $8.20, P(profit) 0.2405, adj growth 15.1 bp · R EV +2.08 (adj +0.73) on $7.00, P(profit) 0.3031, adj growth 23.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04VGKVAN-VGK|no == KXNHLGAME-26OCT04VGKVAN-VAN|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
