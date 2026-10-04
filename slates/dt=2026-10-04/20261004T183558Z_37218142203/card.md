# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-04T18:35:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +34.10 | +8.82 | +31.99 | 0.710 | -43.08 | -56.48 | 70.67 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +26.25 | +13.25 | +22.11 | 0.672 | -35.69 | -48.50 | 119.87 |
| C best expression per thesis | 106.99 | +23.66 | +10.79 | +20.13 | 0.705 | -37.02 | -44.63 | 95.65 |
| R FUNDED research stakes | 17.00 | +2.36 | +1.48 | -0.03 | 0.302 | -6.13 | -11.18 | 0.00 |

## UTA @ NYR  ·  10000 joint draws  ·  344 bet sides mapped, 6 +EV candidates, 4 on card

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
| Vincent Trocheck: 1+ assists NO | 70 | 0.849 | 0.749 | +0.135 | +0.034 | $16.93 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Jack McBain: 1+ goals YES | 10 | 0.132 | 0.123 | +0.025 | +0.016 | $3.57 | FUNDED_RESEARCH | $1 | UTA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Noah Laba: 1+ goals YES | 11 | 0.139 | 0.131 | +0.022 | +0.014 | $3.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Anders Lee: 1+ goals YES | 19 | 0.228 | 0.217 | +0.028 | +0.017 | $4.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT04UTANYR-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (12.71 vs 0.42 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT04UTANYR-NYRNLABA42-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); failure: UTA offense succeeds (4+ goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes; why: higher confidence-adjusted growth (6.02 vs 3.81 bp); despite a smaller raw edge (+0.025 vs +0.028/contract); relationships: KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT04UTANYR-NYRNLABA42-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: UTA offense suppressed (<= 2 goals)
- **Noah Laba: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT04UTANYR-9|yes; why: higher confidence-adjusted growth (3.90 vs 0.27 bp); despite a smaller raw edge (+0.022 vs +0.023/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.88 vs 0.373); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: NYR offense suppressed (<= 2 goals)
- **Anders Lee: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (3.81 vs 3.44 bp); relationships: KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT04UTANYR-NYRNLABA42-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis UTA:OFFENSE_4PLUS (p 0.3522): highest fidelity KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.4374): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis NYR:OFFENSE_4PLUS (p 0.4223): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.4 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3522, phi -0.167)
- KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4374, phi -0.181)
- KXNHLGOAL-26OCT04UTANYR-NYRNLABA42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3568, phi -0.159)
- KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4374, phi -0.229)

portfolios: A EV +5.53 (adj +1.78) on $37.50, P(profit) 0.3655, adj growth 15.9 bp · B EV +5.26 (adj +2.10) on $28.15, P(profit) 0.377, adj growth 19.2 bp · C EV +0.69 (adj +0.42) on $5.05, P(profit) 0.2284, adj growth 3.7 bp · R EV +0.24 (adj +0.15) on $1.00, P(profit) 0.1318, adj growth 5.3 bp

## FLA @ ANA  ·  10000 joint draws  ·  360 bet sides mapped, 23 +EV candidates, 4 on card

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
| Sam Reinhart: 1+ goals NO | 64 | 0.714 | 0.693 | +0.058 | +0.037 | $15.94 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 78 | 0.865 | 0.820 | +0.073 | +0.028 | $15.94 | FUNDED_RESEARCH | $4 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| A.J. Greer: 1+ goals YES | 21 | 0.264 | 0.249 | +0.042 | +0.028 | $6.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Eetu Luostarinen: 1+ goals YES | 15 | 0.187 | 0.176 | +0.028 | +0.018 | $4.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04FLAANA-FLA3|no; why: higher confidence-adjusted growth (13.21 vs 10.57 bp); despite a smaller raw edge (+0.058 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT04FLAANA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes; why: higher confidence-adjusted growth (10.57 vs 9.39 bp); wins across more scripts (relative breadth 1.034 vs 0.438); relationships: KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.104); KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.151); failure: FLA wins by 2+
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT04FLAANA-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT04FLAANA-FLA3|no has the higher standalone adjusted growth (10.57 vs 9.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.104); they share one thesis budget; relationships: KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLSPREAD-26OCT04FLAANA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.104); KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: ANA offense suppressed (<= 2 goals)
- **Eetu Luostarinen: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT04FLAANA-FLACVERHAEGHE23-1|yes; why: higher confidence-adjusted growth (5.00 vs 4.32 bp); despite a smaller raw edge (+0.028 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT04FLAANA-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.151); KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis FLA:SUPPRESSED (p 0.4205): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5799): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-FLA3|no (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4755): highest fidelity KXNHLTEAMTOTAL-26OCT04FLAANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-FLA3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3612, phi -0.243)
- KXNHLSPREAD-26OCT04FLAANA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2245, phi -0.734)
- KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3125, phi -0.226)
- KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4205, phi -0.211)

portfolios: A EV +12.05 (adj +2.08) on $37.50, P(profit) 0.5725, adj growth 12.4 bp · B EV +4.81 (adj +2.70) on $42.33, P(profit) 0.7624, adj growth 24.7 bp · C EV +6.65 (adj +3.17) on $50.00, P(profit) 0.7481, adj growth 28.4 bp · R EV +0.72 (adj +0.37) on $8.00, P(profit) 0.6379, adj growth 13.7 bp

## CGY @ SEA  ·  10000 joint draws  ·  334 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

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
| Ryan Winterton: 1+ goals YES | 12 | 0.163 | 0.149 | +0.036 | +0.021 | $4.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brandon Montour: 1+ goals NO | 85 | 0.888 | 0.877 | +0.029 | +0.018 | $16.93 | FUNDED_RESEARCH | $5 | SEA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Zayne Parekh: 1+ goals NO | 87 | 0.898 | 0.889 | +0.020 | +0.011 | $16.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Shane Wright: 1+ goals YES | 17 | 0.202 | 0.193 | +0.022 | +0.013 | $3.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes; why: higher confidence-adjusted growth (8.68 vs 2.33 bp); relationships: KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT04CGYSEA-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: SEA offense suppressed (<= 2 goals)
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (6.04 vs 1.38 bp); relationships: KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT04CGYSEA-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense succeeds (4+ goals)
- **Zayne Parekh: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT04CGYSEA-CGYSNEMEC71-1|no; why: higher confidence-adjusted growth (2.37 vs 1.01 bp); despite a smaller raw edge (+0.020 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: CGY offense succeeds (4+ goals)
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT04CGYSEA-SEAMBENIERS10-1|yes; why: higher confidence-adjusted growth (2.33 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.025/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT04CGYSEA-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4273): highest fidelity KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes (same contract)
- thesis SEA:SUPPRESSED (p 0.3535): highest fidelity KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no (same contract)
- thesis CGY:SUPPRESSED (p 0.4794): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3535, phi -0.192)
- KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.4273, phi -0.116)
- KXNHLGOAL-26OCT04CGYSEA-CGYZPAREKH19-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.3079, phi -0.129)
- KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3535, phi -0.207)

portfolios: A EV +3.27 (adj +1.92) on $37.50, P(profit) 0.328, adj growth 16.4 bp · B EV +2.64 (adj +1.56) on $41.63, P(profit) 0.2978, adj growth 14.1 bp · C EV +0.76 (adj +0.42) on $14.15, P(profit) 0.7979, adj growth 3.7 bp · R EV +0.17 (adj +0.11) on $5.00, P(profit) 0.8878, adj growth 4.0 bp

## VGK @ VAN  ·  10000 joint draws  ·  338 bet sides mapped, 28 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.290 / away 0.710

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
| Drew O'Connor: 1+ goals YES | 14 | 0.209 | 0.191 | +0.061 | +0.042 | $9.83 | FUNDED_RESEARCH | $3 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Adin Hill: 19+ saves YES | 52 | 0.734 | 0.595 | +0.196 | +0.057 | $16.93 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VAN:SHOT_CONTROL | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Marco Rossi: 1+ goals YES | 20 | 0.274 | 0.255 | +0.063 | +0.043 | $11.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (30.13 vs 24.25 bp); despite a smaller raw edge (+0.061 vs +0.063/contract); relationships: KXNHLSAVE-26OCT04VGKVAN-VGKAHILL33-19|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: VAN offense suppressed (<= 2 goals)
- **Adin Hill: 19+ saves YES** — thesis: VAN controls shots (share >= 0.55); alternative: KXNHLSAVE-26OCT04VGKVAN-VANKLANKINEN32-30|no; why: higher confidence-adjusted growth (28.98 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: no executable ask; relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.03); failure: VGK net faces light volume (<= 25 shots; VAN suppressed)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (30.13 vs 24.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLSAVE-26OCT04VGKVAN-VGKAHILL33-19|yes: MOSTLY_INDEPENDENT (phi -0.03); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.3384): highest fidelity KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:SHOT_CONTROL (p 0.1567): highest fidelity KXNHLSAVE-26OCT04VGKVAN-VGKAHILL33-19|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT04VGKVAN-VGKAHILL33-19|yes (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.2291): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes (same contract)
- KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4358, phi -0.234)
- KXNHLSAVE-26OCT04VGKVAN-VGKAHILL33-19|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.4 pts; fragile player expression; opposing: failure thesis VGK:NET_LOW_VOLUME (p 0.5214, phi -0.474)
- KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4358, phi -0.246)

portfolios: A EV +13.24 (adj +3.04) on $37.50, P(profit) 0.6007, adj growth 26.0 bp · B EV +13.54 (adj +6.89) on $37.89, P(profit) 0.4286, adj growth 61.9 bp · C EV +15.57 (adj +6.78) on $37.79, P(profit) 0.3649, adj growth 59.9 bp · R EV +1.23 (adj +0.85) on $3.00, P(profit) 0.2093, adj growth 28.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04VGKVAN-VGK|no == KXNHLGAME-26OCT04VGKVAN-VAN|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
