# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-04T13:32:17Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +27.47 | +7.77 | +26.02 | 0.660 | -45.72 | -63.51 | 61.68 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +25.07 | +12.77 | +21.02 | 0.638 | -40.47 | -52.58 | 112.93 |
| C best expression per thesis | 61.63 | +15.66 | +8.45 | +6.96 | 0.602 | -34.74 | -45.15 | 73.17 |
| R FUNDED research stakes | 22.00 | +3.58 | +1.99 | +0.17 | 0.602 | -10.46 | -11.65 | 0.00 |

## WPG @ DET  ·  10000 joint draws  ·  250 bet sides mapped, 4 +EV candidates, 4 on card


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
| Cole Perfetti: 1+ goals NO | 73 | 0.790 | 0.774 | +0.046 | +0.030 | $9.64 | FUNDED_RESEARCH | $3 | WPG:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Vladislav Namestnikov: 1+ goals NO | 86 | 0.898 | 0.887 | +0.030 | +0.019 | $9.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Isak Rosen: 1+ goals NO | 86 | 0.897 | 0.887 | +0.029 | +0.018 | $9.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| J.T. Compher: 1+ goals YES | 14 | 0.175 | 0.164 | +0.027 | +0.015 | $2.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Cole Perfetti: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04WPGDET-WPG2|no; why: higher confidence-adjusted growth (10.45 vs 0.13 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04WPGDET-WPGVNAMESTNIKOV7-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT04WPGDET-WPGIROSEN27-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: WPG offense succeeds (4+ goals)
- **Vladislav Namestnikov: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no has the higher standalone adjusted growth (10.45 vs 6.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT04WPGDET-WPGIROSEN27-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: WPG offense succeeds (4+ goals)
- **Isak Rosen: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no has the higher standalone adjusted growth (10.45 vs 6.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT04WPGDET-WPGVNAMESTNIKOV7-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: WPG offense succeeds (4+ goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT04WPGDET-WPG2|no; why: higher confidence-adjusted growth (4.10 vs 0.13 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT04WPGDET-WPGVNAMESTNIKOV7-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT04WPGDET-WPGIROSEN27-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WPG:SUPPRESSED (p 0.4595): highest fidelity KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.38): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3274, phi -0.223)
- KXNHLGOAL-26OCT04WPGDET-WPGVNAMESTNIKOV7-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3274, phi -0.165)
- KXNHLGOAL-26OCT04WPGDET-WPGIROSEN27-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3274, phi -0.148)
- KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3989, phi -0.191)

portfolios: A EV +2.11 (adj +1.31) on $35.68, P(profit) 0.7018, adj growth 12.2 bp · B EV +1.78 (adj +1.11) on $31.86, P(profit) 0.6943, adj growth 10.5 bp · C EV +1.25 (adj +0.81) on $20.00, P(profit) 0.7901, adj growth 7.5 bp · R EV +0.19 (adj +0.12) on $3.00, P(profit) 0.7901, adj growth 4.6 bp

## UTA @ NYR  ·  10000 joint draws  ·  340 bet sides mapped, 5 +EV candidates, 4 on card


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
| Tye Kartye: 1+ goals YES | 10 | 0.142 | 0.129 | +0.036 | +0.023 | $5.60 | FUNDED_RESEARCH | $2 | NYR:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 10 | 0.132 | 0.121 | +0.025 | +0.015 | $3.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 71 | 0.849 | 0.746 | +0.125 | +0.021 | $19.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Lawson Crouse: 1+ goals YES | 16 | 0.196 | 0.184 | +0.026 | +0.015 | $4.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Tye Kartye: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT04UTANYR-9|yes; why: higher confidence-adjusted growth (11.53 vs 0.27 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.9 vs 0.373); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: NYR offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (5.14 vs 3.44 bp); despite a smaller raw edge (+0.025 vs +0.026/contract); relationships: KXNHLGOAL-26OCT04UTANYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: UTA offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT04UTANYR-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (5.00 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT04UTANYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: UTA offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes; why: higher confidence-adjusted growth (3.44 vs 0.76 bp); alternative not eligible: confidence-adjusted EV +0.0076 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04UTANYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.026); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis UTA:OFFENSE_4PLUS (p 0.3522): highest fidelity KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.4223): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis UTA:SUPPRESSED (p 0.4374): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT04UTANYR-NYRTKARTYE24-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3568, phi -0.179)
- KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4374, phi -0.181)
- KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.9 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3522, phi -0.167)
- KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4374, phi -0.215)

portfolios: A EV +5.98 (adj +2.33) on $35.68, P(profit) 0.3048, adj growth 20.3 bp · B EV +6.79 (adj +2.68) on $33.02, P(profit) 0.3781, adj growth 23.6 bp · C EV +0.67 (adj +0.38) on $4.27, P(profit) 0.1958, adj growth 3.3 bp · R EV +0.67 (adj +0.43) on $2.00, P(profit) 0.1419, adj growth 13.7 bp

## FLA @ ANA  ·  10000 joint draws  ·  356 bet sides mapped, 17 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_FLA_win | p_overtime | goals | shots ANA/FLA | ANA/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.60 | 0.40 | 0.00 | 6.06 | 28.2/27.7 | 24.7/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.61 | 0.39 | 0.00 | 9.44 | 29.9/29.3 | 23.6/22.9 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.102 | 0.68 | 0.32 | 0.00 | 6.06 | 33.9/22.2 | 19.5/29.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.50 | 0.50 | 0.48 | 5.94 | 28.2/27.8 | 24.5/24.8 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.088 | 0.69 | 0.31 | 0.00 | 9.37 | 34.9/23.4 | 18.7/26.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.56 | 0.44 | 0.51 | 5.97 | 33.9/22.7 | 19.4/30.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 19 | 0.264 | 0.243 | +0.063 | +0.042 | $9.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 78 | 0.865 | 0.820 | +0.073 | +0.028 | $17.36 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sam Reinhart: 1+ goals NO | 65 | 0.714 | 0.694 | +0.048 | +0.028 | $17.21 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Aaron Ekblad: 1+ assists YES | 26 | 0.328 | 0.284 | +0.054 | +0.010 | $3.89 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes; why: higher confidence-adjusted growth (23.79 vs 14.49 bp); despite a smaller raw edge (+0.063 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.844 vs 0.438); relationships: KXNHLSPREAD-26OCT04FLAANA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.104); KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT04FLAANA-FLAAEKBLAD5-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: ANA offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes; why: Broad expression KXNHLSPREAD-26OCT04FLAANA-FLA3|no selected over broad KXNHLSPREAD-26OCT04FLAANA-ANA3|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.67 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.104); KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLAST-26OCT04FLAANA-FLAAEKBLAD5-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.145); failure: FLA wins by 2+
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes; why: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes has the higher standalone adjusted growth (14.49 vs 7.89 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.135); relationships: KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLSPREAD-26OCT04FLAANA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLAST-26OCT04FLAANA-FLAAEKBLAD5-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.11); failure: FLA offense succeeds (4+ goals)
- **Aaron Ekblad: 1+ assists YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT04FLAANA-FLASBENNETT9-1|yes; why: higher confidence-adjusted growth (1.16 vs 0.10 bp); alternative not eligible: confidence-adjusted EV +0.0032 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT04FLAANA-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.145); KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: INTENTIONAL_DIVERSIFIER (phi -0.11); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4755): highest fidelity KXNHLTEAMTOTAL-26OCT04FLAANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3637): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-ANA3|yes — Broad expression KXNHLSPREAD-26OCT04FLAANA-FLA3|no selected over broad KXNHLSPREAD-26OCT04FLAANA-ANA3|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.67 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis ANA:WINS (p 0.5799): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-ANA3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3125, phi -0.226)
- KXNHLSPREAD-26OCT04FLAANA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2245, phi -0.734)
- KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3612, phi -0.243)
- KXNHLAST-26OCT04FLAANA-FLAAEKBLAD5-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4205, phi -0.267)
- override: Broad expression KXNHLSPREAD-26OCT04FLAANA-FLA3|no selected over broad KXNHLSPREAD-26OCT04FLAANA-ANA3|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.67 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +10.10 (adj +1.82) on $35.68, P(profit) 0.511, adj growth 12.6 bp · B EV +6.67 (adj +3.53) on $48.20, P(profit) 0.3846, adj growth 31.7 bp · C EV +7.30 (adj +3.67) on $22.07, P(profit) 0.4114, adj growth 31.6 bp · R EV +0.82 (adj +0.39) on $10.00, P(profit) 0.6379, adj growth 14.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04FLAANA-FLA|no == KXNHLGAME-26OCT04FLAANA-ANA|yes

## CGY @ SEA  ·  10000 joint draws  ·  334 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.65 | 0.35 | 0.00 | 6.0 | 28.0/28.1 | 25.2/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.48 | 5.93 | 28.3/28.3 | 25.1/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.67 | 0.33 | 0.00 | 9.31 | 29.9/29.8 | 24.7/22.9 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.077 | 0.68 | 0.32 | 0.00 | 6.01 | 32.9/22.1 | 19.5/28.4 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.56 | 0.44 | 0.48 | 5.9 | 33.6/22.7 | 19.6/30.0 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.060 | 0.49 | 0.51 | 0.47 | 2.78 | 26.8/26.8 | 25.3/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Winterton: 1+ goals YES | 12 | 0.163 | 0.149 | +0.036 | +0.021 | $5.34 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT04CGYSEA-SEABMONTOUR62-1|yes; why: higher confidence-adjusted growth (8.68 vs 0.54 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4273): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3535, phi -0.192)

portfolios: A EV +2.05 (adj +1.21) on $7.30, P(profit) 0.1631, adj growth 9.9 bp · B EV +1.50 (adj +0.89) on $5.34, P(profit) 0.1631, adj growth 7.7 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ VAN  ·  10000 joint draws  ·  334 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_VGK_win | p_overtime | goals | shots VAN/VGK | VAN/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.41 | 0.59 | 0.00 | 5.98 | 26.8/27.3 | 23.4/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.48 | 6.0 | 26.8/27.4 | 24.0/23.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.107 | 0.33 | 0.67 | 0.00 | 6.01 | 21.2/32.4 | 27.9/18.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.42 | 0.58 | 0.00 | 9.2 | 28.5/29.1 | 22.6/23.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.42 | 0.58 | 0.50 | 5.92 | 21.4/32.6 | 29.2/18.3 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.075 | 0.31 | 0.69 | 0.00 | 9.35 | 22.6/34.4 | 26.5/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 14 | 0.209 | 0.188 | +0.061 | +0.040 | $9.62 | FUNDED_RESEARCH | $3 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Vancouver wins by over 1.5 goals YES | 15 | 0.229 | 0.187 | +0.070 | +0.028 | $3.91 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Marco Rossi: 1+ goals YES | 21 | 0.274 | 0.251 | +0.053 | +0.029 | $7.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Vegas over 4.5 goals scored NO | 68 | 0.749 | 0.712 | +0.053 | +0.017 | $10.14 | FUNDED_RESEARCH | $3 | VAN:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: higher confidence-adjusted growth (26.72 vs 12.73 bp); despite a smaller raw edge (+0.061 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.896 vs 0.556); relationships: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5|no: MOSTLY_INDEPENDENT (phi -0.006); failure: VAN offense suppressed (<= 2 goals)
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN3|yes; why: higher confidence-adjusted growth (12.73 vs 5.17 bp); relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.12); KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5|no: REINFORCING (phi 0.293); failure: VGK wins (incl. OT/SO)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (26.72 vs 10.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: MOSTLY_INDEPENDENT (phi 0.12); KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5|no: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)
- **Vegas over 4.5 goals scored NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes has the higher standalone adjusted growth (12.73 vs 2.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.293); they share one thesis budget; relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: REINFORCING (phi 0.293); KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.3384): highest fidelity KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2291): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes (same contract)
- thesis VAN:WINS (p 0.4365): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT04VGKVAN-VGK2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5|no kept
- KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4358, phi -0.234)
- KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS (p 0.5635, phi -0.619)
- KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4358, phi -0.246)
- KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4435, phi -0.649)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT04VGKVAN-VGK2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5|no kept

portfolios: A EV +7.24 (adj +1.10) on $35.68, P(profit) 0.5418, adj growth 6.7 bp · B EV +8.34 (adj +4.56) on $31.59, P(profit) 0.5236, adj growth 39.4 bp · C EV +6.45 (adj +3.59) on $15.29, P(profit) 0.3649, adj growth 30.8 bp · R EV +1.90 (adj +1.05) on $7.00, P(profit) 0.3626, adj growth 35.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04VGKVAN-VAN|yes == KXNHLGAME-26OCT04VGKVAN-VGK|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
