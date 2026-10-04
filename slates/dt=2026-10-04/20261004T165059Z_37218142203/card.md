# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-04T16:50:59Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +28.46 | +8.72 | +26.69 | 0.692 | -39.93 | -55.11 | 72.55 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +24.85 | +14.01 | +20.45 | 0.657 | -35.54 | -48.31 | 126.91 |
| C best expression per thesis | 96.70 | +18.63 | +10.35 | +11.71 | 0.580 | -43.10 | -57.52 | 89.81 |
| R FUNDED research stakes | 21.00 | +3.40 | +2.03 | -0.50 | 0.418 | -6.69 | -11.29 | 0.00 |

## WPG @ DET  ·  10000 joint draws  ·  252 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

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
| Vladislav Namestnikov: 1+ goals NO | 86 | 0.898 | 0.887 | +0.030 | +0.019 | $12.75 | FUNDED_RESEARCH | $4 | WPG:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| J.T. Compher: 1+ goals YES | 14 | 0.175 | 0.165 | +0.027 | +0.017 | $3.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Morgan Barron: 1+ goals YES | 11 | 0.138 | 0.130 | +0.021 | +0.013 | $2.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Cole Perfetti: 1+ goals NO | 75 | 0.790 | 0.779 | +0.027 | +0.016 | $10.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Vladislav Namestnikov: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no; why: higher confidence-adjusted growth (6.99 vs 3.00 bp); relationships: KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT04WPGDET-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: WPG offense succeeds (4+ goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04WPGDET-DETMRASMUSSEN27-1|yes; why: higher confidence-adjusted growth (4.79 vs 0.99 bp); alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04WPGDET-WPGVNAMESTNIKOV7-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT04WPGDET-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: DET offense suppressed (<= 2 goals)
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT04WPGDET-3|yes; why: higher confidence-adjusted growth (3.65 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.905 vs 0.797); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT04WPGDET-WPGVNAMESTNIKOV7-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: WPG offense suppressed (<= 2 goals)
- **Cole Perfetti: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04WPGDET-WPG2|no; why: higher confidence-adjusted growth (3.00 vs 0.73 bp); despite a smaller raw edge (+0.027 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04WPGDET-WPGVNAMESTNIKOV7-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT04WPGDET-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WPG:SUPPRESSED (p 0.4595): highest fidelity KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.38): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis WPG:OFFENSE_4PLUS (p 0.3274): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT04WPGDET-WPGVNAMESTNIKOV7-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3274, phi -0.165)
- KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3989, phi -0.191)
- KXNHLGOAL-26OCT04WPGDET-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4595, phi -0.179)
- KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3274, phi -0.223)

portfolios: A EV +2.24 (adj +1.38) on $30.77, P(profit) 0.2841, adj growth 12.4 bp · B EV +1.96 (adj +1.21) on $29.32, P(profit) 0.2841, adj growth 11.1 bp · C EV +0.61 (adj +0.35) on $17.14, P(profit) 0.7901, adj growth 3.1 bp · R EV +0.14 (adj +0.09) on $4.00, P(profit) 0.8982, adj growth 3.3 bp

## UTA @ NYR  ·  10000 joint draws  ·  344 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.533 / away 0.467

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
| Vincent Trocheck: 1+ assists NO | 71 | 0.849 | 0.749 | +0.125 | +0.025 | $15.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Jack McBain: 1+ goals YES | 10 | 0.132 | 0.123 | +0.025 | +0.016 | $3.23 | FUNDED_RESEARCH | $1 | UTA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Anders Lee: 1+ goals YES | 19 | 0.228 | 0.217 | +0.028 | +0.017 | $3.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 16 | 0.196 | 0.184 | +0.026 | +0.015 | $3.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT04UTANYR-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (6.65 vs 0.18 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0044 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: UTA offense succeeds (4+ goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes; why: higher confidence-adjusted growth (6.02 vs 3.81 bp); despite a smaller raw edge (+0.025 vs +0.028/contract); relationships: KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: UTA offense suppressed (<= 2 goals)
- **Anders Lee: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (3.81 vs 3.44 bp); relationships: KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: UTA offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes has the higher standalone adjusted growth (3.81 vs 3.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis UTA:OFFENSE_4PLUS (p 0.3522): highest fidelity KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.4374): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.4 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3522, phi -0.167)
- KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4374, phi -0.181)
- KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4374, phi -0.229)
- KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4374, phi -0.215)

portfolios: A EV +4.67 (adj +1.97) on $26.91, P(profit) 0.4261, adj growth 17.3 bp · B EV +4.47 (adj +1.64) on $25.83, P(profit) 0.4063, adj growth 15.0 bp · C EV +0.69 (adj +0.42) on $5.05, P(profit) 0.2284, adj growth 3.7 bp · R EV +0.24 (adj +0.15) on $1.00, P(profit) 0.1318, adj growth 5.3 bp

## FLA @ ANA  ·  10000 joint draws  ·  356 bet sides mapped, 23 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.449 / away 0.551

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
| Sam Reinhart: 1+ goals NO | 63 | 0.714 | 0.692 | +0.068 | +0.045 | $14.91 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 78 | 0.865 | 0.820 | +0.073 | +0.028 | $14.91 | FUNDED_RESEARCH | $4 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Eetu Luostarinen: 1+ goals YES | 15 | 0.187 | 0.176 | +0.028 | +0.018 | $3.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Carter Verhaeghe: 1+ assists YES | 29 | 0.365 | 0.320 | +0.060 | +0.015 | $4.60 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | FLA:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_MIXED | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes; why: higher confidence-adjusted growth (19.83 vs 14.49 bp); despite a smaller raw edge (+0.068 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.004 vs 0.438); relationships: KXNHLSPREAD-26OCT04FLAANA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT04FLAANA-FLACVERHAEGHE23-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.067); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes; why: Broad expression KXNHLSPREAD-26OCT04FLAANA-FLA3|no selected over broad KXNHLSPREAD-26OCT04FLAANA-ANA3|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.67 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.151); KXNHLAST-26OCT04FLAANA-FLACVERHAEGHE23-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.168); failure: FLA wins by 2+
- **Eetu Luostarinen: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT04FLAANA-FLAAEKBLAD5-1|yes; why: higher confidence-adjusted growth (5.00 vs 2.56 bp); despite a smaller raw edge (+0.028 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT04FLAANA-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.151); KXNHLAST-26OCT04FLAANA-FLACVERHAEGHE23-1|yes: MOSTLY_INDEPENDENT (phi 0.067); failure: FLA offense suppressed (<= 2 goals)
- **Carter Verhaeghe: 1+ assists YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes; why: Player prop expression KXNHLAST-26OCT04FLAANA-FLACVERHAEGHE23-1|yes selected over player prop KXNHLAST-26OCT04FLAANA-FLAAEKBLAD5-1|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.54 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: INTENTIONAL_DIVERSIFIER (phi -0.067); KXNHLSPREAD-26OCT04FLAANA-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.168); KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes: MOSTLY_INDEPENDENT (phi 0.067); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis FLA:SUPPRESSED (p 0.4205): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3637): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-ANA3|yes — Broad expression KXNHLSPREAD-26OCT04FLAANA-FLA3|no selected over broad KXNHLSPREAD-26OCT04FLAANA-ANA3|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.67 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis ANA:WINS (p 0.5799): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-ANA3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3612, phi -0.243)
- KXNHLSPREAD-26OCT04FLAANA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2245, phi -0.734)
- KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4205, phi -0.211)
- KXNHLAST-26OCT04FLAANA-FLACVERHAEGHE23-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 46% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4205, phi -0.279)
- override: Broad expression KXNHLSPREAD-26OCT04FLAANA-FLA3|no selected over broad KXNHLSPREAD-26OCT04FLAANA-ANA3|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.67 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLAST-26OCT04FLAANA-FLACVERHAEGHE23-1|yes selected over player prop KXNHLAST-26OCT04FLAANA-FLAAEKBLAD5-1|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.54 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +8.36 (adj +1.47) on $30.77, P(profit) 0.5217, adj growth 10.3 bp · B EV +4.53 (adj +2.24) on $38.28, P(profit) 0.7084, adj growth 21.0 bp · C EV +7.10 (adj +3.58) on $42.37, P(profit) 0.6176, adj growth 31.8 bp · R EV +0.79 (adj +0.42) on $8.00, P(profit) 0.6379, adj growth 15.9 bp

## CGY @ SEA  ·  10000 joint draws  ·  334 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.579 / away 0.421

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
| Ryan Winterton: 1+ goals YES | 12 | 0.163 | 0.150 | +0.036 | +0.022 | $4.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brandon Montour: 1+ goals NO | 85 | 0.888 | 0.877 | +0.029 | +0.018 | $15.15 | FUNDED_RESEARCH | $4 | SEA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Shane Wright: 1+ goals YES | 17 | 0.202 | 0.193 | +0.022 | +0.013 | $2.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Jared McCann: 1+ goals NO | 71 | 0.746 | 0.736 | +0.021 | +0.011 | $7.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes; why: higher confidence-adjusted growth (9.73 vs 2.33 bp); relationships: KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: SEA offense suppressed (<= 2 goals)
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (6.04 vs 1.38 bp); relationships: KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: SEA offense succeeds (4+ goals)
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT04CGYSEA-SEAMBENIERS10-1|yes; why: higher confidence-adjusted growth (2.33 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.025/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: SEA offense suppressed (<= 2 goals)
- **Jared McCann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT04CGYSEA-SEAJMCCANN19-2|no; why: higher confidence-adjusted growth (1.38 vs 0.00 bp); despite a smaller raw edge (+0.021 vs +0.027/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: SEA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4273): highest fidelity KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes (same contract)
- thesis SEA:SUPPRESSED (p 0.3535): highest fidelity KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no (same contract)
- KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3535, phi -0.192)
- KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.4273, phi -0.116)
- KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3535, phi -0.207)
- KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.4273, phi -0.214)

portfolios: A EV +2.69 (adj +1.63) on $30.77, P(profit) 0.328, adj growth 14.4 bp · B EV +2.35 (adj +1.44) on $30.35, P(profit) 0.313, adj growth 13.0 bp · C EV +0.76 (adj +0.42) on $14.15, P(profit) 0.7979, adj growth 3.7 bp · R EV +0.13 (adj +0.08) on $4.00, P(profit) 0.8878, adj growth 3.2 bp

## VGK @ VAN  ·  10000 joint draws  ·  334 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.295 / away 0.705

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
| Drew O'Connor: 1+ goals YES | 13 | 0.209 | 0.187 | +0.071 | +0.049 | $8.41 | FUNDED_RESEARCH | $3 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 19 | 0.274 | 0.252 | +0.074 | +0.051 | $10.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Vancouver wins by over 1.5 goals YES | 14 | 0.229 | 0.182 | +0.081 | +0.034 | $3.25 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Brendan Gallagher: 1+ goals YES | 10 | 0.147 | 0.134 | +0.041 | +0.028 | $4.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (42.79 vs 35.06 bp); despite a smaller raw edge (+0.071 vs +0.074/contract); relationships: KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT04VGKVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (42.79 vs 35.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: MOSTLY_INDEPENDENT (phi 0.12); KXNHLGOAL-26OCT04VGKVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VAN offense suppressed (<= 2 goals)
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLGOAL-26OCT04VGKVAN-VANARATY54-1|yes; why: higher confidence-adjusted growth (19.14 vs 9.37 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.12); KXNHLGOAL-26OCT04VGKVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.145); failure: VGK wins (incl. OT/SO)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (42.79 vs 17.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: MOSTLY_INDEPENDENT (phi 0.145); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.3384): highest fidelity KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2291): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes (same contract)
- thesis VAN:WINS (p 0.4365): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4358, phi -0.234)
- KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4358, phi -0.246)
- KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS (p 0.5635, phi -0.619)
- KXNHLGOAL-26OCT04VGKVAN-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4358, phi -0.194)

portfolios: A EV +10.50 (adj +2.27) on $30.77, P(profit) 0.5688, adj growth 18.2 bp · B EV +11.54 (adj +7.48) on $26.21, P(profit) 0.511, adj growth 66.9 bp · C EV +9.47 (adj +5.58) on $17.99, P(profit) 0.3649, adj growth 47.6 bp · R EV +2.10 (adj +1.29) on $4.00, P(profit) 0.3649, adj growth 44.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04VGKVAN-VGK|no == KXNHLGAME-26OCT04VGKVAN-VAN|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
