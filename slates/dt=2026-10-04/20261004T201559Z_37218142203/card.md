# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-04T20:15:59Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +31.65 | +9.64 | +30.46 | 0.689 | -44.91 | -64.76 | 78.97 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +21.67 | +11.12 | +19.32 | 0.689 | -34.51 | -42.44 | 101.24 |
| C best expression per thesis | 94.84 | +16.36 | +7.78 | +13.02 | 0.587 | -34.39 | -50.05 | 68.40 |
| R FUNDED research stakes | 19.00 | +1.91 | +0.91 | +1.61 | 0.723 | -4.83 | -8.69 | 0.00 |

## UTA @ NYR  ·  10000 joint draws  ·  344 bet sides mapped, 5 +EV candidates, 4 on card

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
| Vincent Trocheck: 1+ assists NO | 71 | 0.849 | 0.752 | +0.125 | +0.028 | $15.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Jack McBain: 1+ goals YES | 10 | 0.132 | 0.123 | +0.025 | +0.016 | $3.26 | FUNDED_RESEARCH | $1 | UTA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 16 | 0.196 | 0.186 | +0.026 | +0.016 | $3.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ assists NO | 69 | 0.792 | 0.722 | +0.087 | +0.017 | $13.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT04UTANYR-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (8.54 vs 0.18 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0044 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26OCT04UTANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: UTA offense succeeds (4+ goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (6.02 vs 4.04 bp); despite a smaller raw edge (+0.025 vs +0.026/contract); relationships: KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT04UTANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: UTA offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04UTANYR-UTAALEE72-1|yes; why: higher confidence-adjusted growth (4.04 vs 1.02 bp); alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT04UTANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: UTA offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT04UTANYR-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (3.21 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis UTA:OFFENSE_4PLUS (p 0.3522): highest fidelity KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.4374): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis NYR:OFFENSE_4PLUS (p 0.4223): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3522, phi -0.167)
- KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4374, phi -0.181)
- KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4374, phi -0.215)
- KXNHLAST-26OCT04UTANYR-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.7 pts; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.4223, phi -0.187)

portfolios: A EV +6.03 (adj +2.12) on $37.50, P(profit) 0.77, adj growth 18.7 bp · B EV +5.61 (adj +1.76) on $35.36, P(profit) 0.7658, adj growth 16.1 bp · C EV +0.73 (adj +0.44) on $4.65, P(profit) 0.1958, adj growth 3.9 bp · R EV +0.24 (adj +0.15) on $1.00, P(profit) 0.1318, adj growth 5.3 bp

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
| Sam Reinhart: 1+ goals NO | 64 | 0.714 | 0.694 | +0.058 | +0.038 | $14.39 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 78 | 0.865 | 0.820 | +0.073 | +0.028 | $14.39 | FUNDED_RESEARCH | $4 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| A.J. Greer: 1+ goals YES | 21 | 0.264 | 0.249 | +0.042 | +0.028 | $5.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Eetu Luostarinen: 1+ goals YES | 15 | 0.187 | 0.176 | +0.028 | +0.018 | $3.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04FLAANA-FLA3|no; why: higher confidence-adjusted growth (14.12 vs 10.57 bp); despite a smaller raw edge (+0.058 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT04FLAANA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: FLA offense succeeds (4+ goals)
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

portfolios: A EV +10.75 (adj +2.31) on $37.50, P(profit) 0.5186, adj growth 16.4 bp · B EV +4.34 (adj +2.46) on $38.21, P(profit) 0.7624, adj growth 22.8 bp · C EV +6.65 (adj +3.21) on $50.00, P(profit) 0.7481, adj growth 28.8 bp · R EV +0.72 (adj +0.37) on $8.00, P(profit) 0.6379, adj growth 14.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04FLAANA-FLA|no == KXNHLGAME-26OCT04FLAANA-ANA|yes

## CGY @ SEA  ·  10000 joint draws  ·  336 bet sides mapped, 5 +EV candidates, 4 on card

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
| Ryan Winterton: 1+ goals YES | 11 | 0.163 | 0.147 | +0.046 | +0.030 | $5.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brandon Montour: 1+ goals NO | 84 | 0.888 | 0.875 | +0.038 | +0.025 | $14.91 | FUNDED_RESEARCH | $4 | SEA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Zayne Parekh: 1+ goals NO | 87 | 0.898 | 0.889 | +0.020 | +0.011 | $14.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Shane Wright: 1+ goals YES | 17 | 0.202 | 0.193 | +0.022 | +0.013 | $2.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes; why: higher confidence-adjusted growth (19.17 vs 2.33 bp); relationships: KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT04CGYSEA-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: SEA offense suppressed (<= 2 goals)
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (11.04 vs 1.38 bp); relationships: KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT04CGYSEA-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense succeeds (4+ goals)
- **Zayne Parekh: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT04CGYSEA-CGYSNEMEC71-1|no; why: higher confidence-adjusted growth (2.37 vs 1.01 bp); despite a smaller raw edge (+0.020 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: CGY offense succeeds (4+ goals)
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (2.33 vs 0.96 bp); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT04CGYSEA-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4273): highest fidelity KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes (same contract)
- thesis SEA:SUPPRESSED (p 0.3535): highest fidelity KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT04CGYSEA-SEAJMCCANN19-1|no (same contract)
- thesis CGY:SUPPRESSED (p 0.4794): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3535, phi -0.192)
- KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.4273, phi -0.116)
- KXNHLGOAL-26OCT04CGYSEA-CGYZPAREKH19-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.3079, phi -0.129)
- KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3535, phi -0.207)

portfolios: A EV +4.73 (adj +3.03) on $37.50, P(profit) 0.328, adj growth 26.1 bp · B EV +3.60 (adj +2.30) on $38.21, P(profit) 0.2994, adj growth 20.9 bp · C EV +0.76 (adj +0.42) on $14.15, P(profit) 0.7979, adj growth 3.7 bp · R EV +0.18 (adj +0.12) on $4.00, P(profit) 0.8878, adj growth 4.6 bp

## VGK @ VAN  ·  10000 joint draws  ·  338 bet sides mapped, 30 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.286 / away 0.714

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_VGK_win | p_overtime | goals | shots VAN/VGK | VAN/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.39 | 0.61 | 0.00 | 6.05 | 27.0/27.6 | 23.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.45 | 5.96 | 27.0/27.4 | 24.1/23.8 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.102 | 0.34 | 0.66 | 0.00 | 5.98 | 21.5/32.7 | 28.1/18.8 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.49 | 0.51 | 0.46 | 5.91 | 21.6/32.6 | 29.3/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.41 | 0.59 | 0.00 | 9.31 | 28.2/28.7 | 22.1/22.6 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.071 | 0.32 | 0.68 | 0.00 | 9.23 | 22.6/34.1 | 26.4/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 14 | 0.205 | 0.188 | +0.057 | +0.039 | $7.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 20 | 0.271 | 0.252 | +0.060 | +0.041 | $8.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Vegas wins by over 1.5 goals NO | 50 | 0.658 | 0.552 | +0.141 | +0.035 | $7.79 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tomas Hertl: 1+ goals NO | 70 | 0.754 | 0.739 | +0.039 | +0.025 | $14.67 | FUNDED_RESEARCH | $4 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (25.86 vs 21.74 bp); despite a smaller raw edge (+0.057 vs +0.060/contract); relationships: KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: MOSTLY_INDEPENDENT (phi 0.127); KXNHLGOAL-26OCT04VGKVAN-VGKTHERTL48-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: higher confidence-adjusted growth (21.74 vs 15.05 bp); despite a smaller raw edge (+0.060 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.927 vs 0.553); relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: REINFORCING (phi 0.15); KXNHLGOAL-26OCT04VGKVAN-VGKTHERTL48-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: VAN offense suppressed (<= 2 goals)
- **Vegas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT04VGKVAN-VGK3|no; why: higher confidence-adjusted growth (10.51 vs 7.93 bp); relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.127); KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: REINFORCING (phi 0.15); KXNHLGOAL-26OCT04VGKVAN-VGKTHERTL48-1|no: MOSTLY_INDEPENDENT (phi 0.116); failure: VGK wins by 2+
- **Tomas Hertl: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes has the higher standalone adjusted growth (15.05 vs 6.55 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.104); relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: MOSTLY_INDEPENDENT (phi 0.116); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3419): highest fidelity KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2214): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VGK2|no (same contract)
- thesis VAN:WINS (p 0.4356): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VGK2|no (same contract)
- KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4363, phi -0.206)
- KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4363, phi -0.247)
- KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.3 pts; opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3418, phi -1.0)
- KXNHLGOAL-26OCT04VGKVAN-VGKTHERTL48-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4399, phi -0.206)

portfolios: A EV +10.14 (adj +2.18) on $37.50, P(profit) 0.6025, adj growth 17.7 bp · B EV +8.12 (adj +4.60) on $38.21, P(profit) 0.4246, adj growth 41.4 bp · C EV +8.23 (adj +3.71) on $26.04, P(profit) 0.407, adj growth 32.1 bp · R EV +0.76 (adj +0.27) on $6.00, P(profit) 0.52, adj growth 10.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04VGKVAN-VGK|no == KXNHLGAME-26OCT04VGKVAN-VAN|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
