# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-04T22:40:13Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 139.71 | +35.53 | +10.91 | +25.69 | 0.663 | -70.08 | -96.51 | 79.41 |
| B thesis-diversified (joint) ← optimiser card | 124.97 | +21.33 | +13.17 | +17.20 | 0.597 | -50.57 | -57.80 | 116.39 |
| C best expression per thesis | 79.73 | +15.96 | +8.01 | +12.88 | 0.576 | -35.61 | -56.48 | 70.55 |
| R FUNDED research stakes | 17.00 | +1.74 | +0.81 | +2.00 | 0.735 | -5.11 | -9.81 | 0.00 |

## FLA @ ANA  ·  10000 joint draws  ·  360 bet sides mapped, 29 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.447 / away 0.553

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_FLA_win | p_overtime | goals | shots ANA/FLA | ANA/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.62 | 0.38 | 0.00 | 6.03 | 27.9/27.5 | 24.5/23.8 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.110 | 0.67 | 0.33 | 0.00 | 6.05 | 33.9/22.3 | 19.7/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.62 | 0.38 | 0.00 | 9.34 | 29.8/29.3 | 23.9/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.46 | 6.03 | 28.4/28.1 | 24.8/25.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.56 | 0.44 | 0.51 | 5.94 | 33.6/22.3 | 19.1/30.1 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.084 | 0.67 | 0.33 | 0.00 | 9.49 | 35.2/23.5 | 18.6/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 20 | 0.270 | 0.251 | +0.059 | +0.040 | $10.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Matthew Tkachuk: 1+ goals NO | 65 | 0.732 | 0.710 | +0.066 | +0.044 | $15.00 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 64 | 0.719 | 0.698 | +0.062 | +0.042 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Eetu Luostarinen: 1+ goals YES | 15 | 0.179 | 0.170 | +0.020 | +0.011 | $2.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04FLAANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (20.73 vs 12.04 bp); relationships: KXNHLGOAL-26OCT04FLAANA-FLAMTKACHUK19-1|no: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT04FLAANA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: ANA offense suppressed (<= 2 goals)
- **Matthew Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (19.48 vs 17.54 bp); relationships: KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT04FLAANA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: FLA offense succeeds (4+ goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT04FLAANA-FLAMTKACHUK19-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT04FLAANA-FLAMTKACHUK19-1|no has the higher standalone adjusted growth (19.48 vs 16.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT04FLAANA-FLAMTKACHUK19-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: FLA offense succeeds (4+ goals)
- **Eetu Luostarinen: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT04FLAANA-FLACVERHAEGHE23-1|yes; why: Player prop expression KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes selected over player prop KXNHLAST-26OCT04FLAANA-FLACVERHAEGHE23-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.28 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT04FLAANA-FLAMTKACHUK19-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT04FLAANA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4892): highest fidelity KXNHLTEAMTOTAL-26OCT04FLAANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3646): highest fidelity KXNHLGAME-26OCT04FLAANA-ANA|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.416): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04FLAANA-FLAMTKACHUK19-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3044, phi -0.237)
- KXNHLGOAL-26OCT04FLAANA-FLAMTKACHUK19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3642, phi -0.242)
- KXNHLGOAL-26OCT04FLAANA-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3642, phi -0.218)
- KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.416, phi -0.2)
- override: Player prop expression KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes selected over player prop KXNHLAST-26OCT04FLAANA-FLACVERHAEGHE23-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.28 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +14.43 (adj +3.01) on $50.00, P(profit) 0.5187, adj growth 20.0 bp · B EV +6.21 (adj +4.15) on $43.49, P(profit) 0.6517, adj growth 37.8 bp · C EV +7.29 (adj +4.04) on $50.00, P(profit) 0.7268, adj growth 36.2 bp · R EV +0.40 (adj +0.27) on $4.00, P(profit) 0.732, adj growth 10.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04FLAANA-FLA|no == KXNHLGAME-26OCT04FLAANA-ANA|yes

## CGY @ SEA  ·  10000 joint draws  ·  336 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.583 / away 0.417

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
| Ryan Winterton: 1+ goals YES | 11 | 0.163 | 0.147 | +0.046 | +0.030 | $7.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brandon Montour: 1+ goals NO | 84 | 0.888 | 0.875 | +0.038 | +0.025 | $20.00 | FUNDED_RESEARCH | $5 | SEA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Shane Wright: 1+ goals YES | 17 | 0.202 | 0.193 | +0.022 | +0.013 | $3.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes; why: higher confidence-adjusted growth (19.17 vs 2.33 bp); relationships: KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: SEA offense suppressed (<= 2 goals)
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT04CGYSEA-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (11.04 vs 0.37 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0062 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense succeeds (4+ goals)
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (2.33 vs 0.96 bp); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4273): highest fidelity KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes (same contract)
- thesis SEA:SUPPRESSED (p 0.3535): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3535, phi -0.192)
- KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.4273, phi -0.116)
- KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3535, phi -0.207)

portfolios: A EV +6.88 (adj +4.47) on $39.71, P(profit) 0.313, adj growth 35.2 bp · B EV +4.42 (adj +2.87) on $31.48, P(profit) 0.313, adj growth 25.2 bp · C EV +0.45 (adj +0.26) on $3.69, P(profit) 0.2016, adj growth 2.2 bp · R EV +0.23 (adj +0.15) on $5.00, P(profit) 0.8878, adj growth 5.7 bp

## VGK @ VAN  ·  10000 joint draws  ·  338 bet sides mapped, 29 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.290 / away 0.710

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
| Drew O'Connor: 1+ goals YES | 14 | 0.205 | 0.188 | +0.057 | +0.039 | $9.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 20 | 0.271 | 0.252 | +0.060 | +0.041 | $11.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Vegas wins by over 1.5 goals NO | 50 | 0.658 | 0.552 | +0.141 | +0.035 | $9.49 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mitch Marner: 1+ goals NO | 68 | 0.737 | 0.722 | +0.042 | +0.026 | $19.46 | FUNDED_RESEARCH | $5 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (25.86 vs 21.74 bp); despite a smaller raw edge (+0.057 vs +0.060/contract); relationships: KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: MOSTLY_INDEPENDENT (phi 0.127); KXNHLGOAL-26OCT04VGKVAN-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: higher confidence-adjusted growth (21.74 vs 15.05 bp); despite a smaller raw edge (+0.060 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.927 vs 0.553); relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: REINFORCING (phi 0.15); KXNHLGOAL-26OCT04VGKVAN-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: VAN offense suppressed (<= 2 goals)
- **Vegas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT04VGKVAN-VGK3|no; why: higher confidence-adjusted growth (10.51 vs 7.93 bp); relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.127); KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: REINFORCING (phi 0.15); KXNHLGOAL-26OCT04VGKVAN-VGKMMARNER93-1|no: REINFORCING (phi 0.167); failure: VGK wins by 2+
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes has the higher standalone adjusted growth (15.05 vs 7.29 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.150); relationships: KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: REINFORCING (phi 0.167); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3419): highest fidelity KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2214): highest fidelity KXNHLGAME-26OCT04VGKVAN-VGK|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT04VGKVAN-VGK|no (same contract)
- thesis VAN:WINS (p 0.4356): highest fidelity KXNHLGAME-26OCT04VGKVAN-VGK|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT04VGKVAN-VGK|no (same contract)
- KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4363, phi -0.206)
- KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4363, phi -0.247)
- KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.3 pts; opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3418, phi -1.0)
- KXNHLGOAL-26OCT04VGKVAN-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4399, phi -0.242)

portfolios: A EV +14.21 (adj +3.43) on $50.00, P(profit) 0.5525, adj growth 24.2 bp · B EV +10.71 (adj +6.15) on $50.00, P(profit) 0.4246, adj growth 53.4 bp · C EV +8.23 (adj +3.71) on $26.04, P(profit) 0.407, adj growth 32.1 bp · R EV +1.12 (adj +0.39) on $8.00, P(profit) 0.5202, adj growth 14.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04VGKVAN-VGK|no == KXNHLGAME-26OCT04VGKVAN-VAN|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
