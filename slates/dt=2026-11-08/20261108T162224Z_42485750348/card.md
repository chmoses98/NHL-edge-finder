# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-08T16:22:24Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +18.88 | +5.97 | +17.05 | 0.645 | -38.81 | -52.94 | 49.50 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +17.07 | +8.11 | +15.17 | 0.652 | -34.52 | -48.48 | 72.05 |
| C best expression per thesis | 125.50 | +15.40 | +5.59 | +14.24 | 0.674 | -32.26 | -46.23 | 48.89 |
| R FUNDED research stakes | 25.00 | +2.18 | +1.10 | +2.38 | 0.608 | -7.93 | -11.75 | 0.00 |

## FLA @ BOS  ·  10000 joint draws  ·  434 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_FLA_win | p_overtime | goals | shots BOS/FLA | BOS/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.69 | 0.31 | 0.00 | 6.05 | 27.0/27.2 | 24.6/22.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.72 | 0.28 | 0.00 | 9.47 | 28.6/28.8 | 24.1/20.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.52 | 0.48 | 0.46 | 5.98 | 27.0/27.3 | 24.0/23.6 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 6.06 | 21.8/32.2 | 28.8/18.0 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.54 | 0.46 | 0.47 | 5.92 | 21.5/32.1 | 28.5/18.1 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.064 | 0.60 | 0.40 | 0.00 | 9.34 | 23.0/33.9 | 28.3/16.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pavel Zacha: 1+ goals YES | 29 | 0.337 | 0.324 | +0.032 | +0.019 | $5.85 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Sam Bennett: 1+ goals YES | 25 | 0.295 | 0.281 | +0.032 | +0.018 | $5.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ assists NO | 61 | 0.692 | 0.646 | +0.065 | +0.019 | $12.22 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | FLA:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
| Fraser Minten: 1+ goals YES | 20 | 0.233 | 0.223 | +0.022 | +0.012 | $3.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes; why: KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes has the higher standalone adjusted growth (4.10 vs 3.86 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.225); relationships: KXNHLGOAL-26NOV08FLABOS-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV08FLABOS-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV08FLABOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: BOS offense suppressed (<= 2 goals)
- **Sam Bennett: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV08FLABOS-10|yes; why: higher confidence-adjusted growth (3.66 vs 0.11 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.917 vs 0.321); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV08FLABOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV08FLABOS-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV08FLABOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: FLA offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV08FLABOS-BOS3|yes; why: higher confidence-adjusted growth (3.53 vs 1.11 bp); wins across more scripts (relative breadth 1.001 vs 0.461); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV08FLABOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV08FLABOS-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV08FLABOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: FLA offense succeeds (4+ goals)
- **Fraser Minten: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes; why: Player prop expression KXNHLGOAL-26NOV08FLABOS-BOSFMINTEN93-1|yes selected over broad KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.32 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV08FLABOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV08FLABOS-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26NOV08FLABOS-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BOS:OFFENSE_4PLUS (p 0.5148): highest fidelity KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes (same contract)
- thesis BOS:WINS (p 0.6201): highest fidelity KXNHLTEAMTOTAL-26NOV08FLABOS-BOS2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:OFFENSE_4PLUS (p 0.3332): highest fidelity KXNHLGOAL-26NOV08FLABOS-FLASBENNETT9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV08FLABOS-FLASBENNETT9-1|yes (same contract)
- KXNHLGOAL-26NOV08FLABOS-BOSPZACHA18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.28, phi -0.229)
- KXNHLGOAL-26NOV08FLABOS-FLASBENNETT9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4481, phi -0.259)
- KXNHLAST-26NOV08FLABOS-FLASREINHART13-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3332, phi -0.24)
- KXNHLGOAL-26NOV08FLABOS-BOSFMINTEN93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.28, phi -0.19)
- override: Player prop expression KXNHLGOAL-26NOV08FLABOS-BOSFMINTEN93-1|yes selected over broad KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.32 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.72 (adj +1.14) on $30.62, P(profit) 0.4646, adj growth 8.9 bp · B EV +2.84 (adj +1.28) on $26.34, P(profit) 0.5009, adj growth 11.4 bp · C EV +3.72 (adj +1.36) on $36.48, P(profit) 0.6285, adj growth 11.9 bp · R EV +0.21 (adj +0.13) on $2.00, P(profit) 0.3367, adj growth 4.3 bp

## VGK @ BUF  ·  10000 joint draws  ·  456 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_VGK_win | p_overtime | goals | shots BUF/VGK | BUF/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.53 | 0.47 | 0.00 | 6.0 | 27.4/27.5 | 24.2/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.49 | 0.51 | 0.48 | 5.99 | 27.7/27.6 | 24.2/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.46 | 0.54 | 0.00 | 9.33 | 29.0/29.0 | 22.7/23.1 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.072 | 0.56 | 0.44 | 0.00 | 6.0 | 32.5/21.9 | 18.7/28.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.066 | 0.44 | 0.56 | 0.00 | 6.03 | 22.1/32.3 | 28.1/18.9 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.53 | 0.47 | 0.42 | 5.91 | 32.9/22.3 | 19.0/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.072 | 0.067 | +0.019 | +0.013 | $2.76 | FUNDED_RESEARCH | $1 | VGK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08VGKBUF-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (7.32 vs 0.98 bp); alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VGK:OFFENSE_4PLUS (p 0.3967): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV08VGKBUF-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3847, phi -0.118)

portfolios: A EV +1.06 (adj +0.75) on $3.02, P(profit) 0.072, adj growth 6.4 bp · B EV +0.97 (adj +0.68) on $2.76, P(profit) 0.072, adj growth 5.9 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.35 (adj +0.25) on $1.00, P(profit) 0.072, adj growth 8.1 bp

## TBL @ WPG  ·  10000 joint draws  ·  394 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_TBL_win | p_overtime | goals | shots WPG/TBL | WPG/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.51 | 0.49 | 0.00 | 6.01 | 27.1/27.5 | 24.0/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.49 | 0.51 | 0.47 | 5.91 | 27.0/27.4 | 24.2/23.7 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.096 | 0.39 | 0.61 | 0.00 | 5.98 | 21.4/32.7 | 28.6/18.5 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.47 | 0.53 | 0.46 | 5.9 | 21.6/32.7 | 29.3/18.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.48 | 0.52 | 0.00 | 9.27 | 28.5/28.8 | 22.8/22.7 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.058 | 0.41 | 0.59 | 0.00 | 9.28 | 23.0/34.4 | 26.9/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charle-Edouard D'Astous: 1+ goals NO | 89 | 0.921 | 0.912 | +0.024 | +0.015 | $17.39 | FUNDED_RESEARCH | $5 | TBL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Cole Perfetti: 1+ assists YES | 32 | 0.396 | 0.355 | +0.061 | +0.020 | $5.72 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.58) | EVIDENCE_MIXED | D |
| Alex Iafallo: 1+ goals YES | 13 | 0.159 | 0.150 | +0.021 | +0.012 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 77 | 0.821 | 0.793 | +0.039 | +0.011 | $7.09 | FUNDED_RESEARCH | $2 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV08TBWPG-TB3|no; why: higher confidence-adjusted growth (5.29 vs 1.46 bp); despite a smaller raw edge (+0.024 vs +0.039/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26NOV08TBWPG-TB3|no: MOSTLY_INDEPENDENT (phi 0.058); failure: TBL offense succeeds (4+ goals)
- **Cole Perfetti: 1+ assists YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08TBWPG-TB3|no; why: higher confidence-adjusted growth (4.02 vs 1.46 bp); relationships: KXNHLGOAL-26NOV08TBWPG-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLSPREAD-26NOV08TBWPG-TB3|no: REINFORCING (phi 0.162); failure: WPG offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes has the higher standalone adjusted growth (4.02 vs 2.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.032); they share one thesis budget; relationships: KXNHLGOAL-26NOV08TBWPG-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLSPREAD-26NOV08TBWPG-TB3|no: MOSTLY_INDEPENDENT (phi 0.096); failure: WPG offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes has the higher standalone adjusted growth (4.02 vs 1.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.162); they share one thesis budget; relationships: KXNHLGOAL-26NOV08TBWPG-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.058); KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: REINFORCING (phi 0.162); KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.096); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.3592): highest fidelity KXNHLSPREAD-26NOV08TBWPG-TB3|no [DIRECT], best adjusted EV KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.4829): highest fidelity KXNHLSPREAD-26NOV08TBWPG-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.4017): highest fidelity KXNHLSPREAD-26NOV08TBWPG-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08TBWPG-TB3|no (same contract)
- KXNHLGOAL-26NOV08TBWPG-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3836, phi -0.11)
- KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 42% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4151, phi -0.314)
- KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4151, phi -0.188)
- KXNHLSPREAD-26NOV08TBWPG-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2932, phi -0.725)

portfolios: A EV +2.81 (adj +1.09) on $30.62, P(profit) 0.4715, adj growth 9.4 bp · B EV +2.26 (adj +0.98) on $32.96, P(profit) 0.4517, adj growth 8.9 bp · C EV +1.72 (adj +0.54) on $17.09, P(profit) 0.396, adj growth 4.8 bp · R EV +0.23 (adj +0.11) on $7.00, P(profit) 0.7619, adj growth 4.1 bp

## NJD @ TOR  ·  10000 joint draws  ·  442 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NJD_win | p_overtime | goals | shots TOR/NJD | TOR/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.128 | 0.45 | 0.55 | 0.00 | 5.96 | 23.0/35.9 | 31.8/19.9 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.48 | 0.52 | 0.43 | 5.93 | 23.1/36.0 | 32.6/19.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.53 | 0.47 | 0.00 | 6.02 | 28.9/29.7 | 26.1/25.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.49 | 5.95 | 29.3/30.1 | 26.9/26.0 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.085 | 0.48 | 0.52 | 0.00 | 9.33 | 24.7/37.9 | 30.8/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.53 | 0.47 | 0.00 | 9.33 | 30.3/31.3 | 25.2/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 10 | 0.146 | 0.132 | +0.040 | +0.026 | $5.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 61 | 0.668 | 0.652 | +0.042 | +0.026 | $15.23 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals YES | 18 | 0.222 | 0.209 | +0.032 | +0.019 | $4.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ assists YES | 29 | 0.362 | 0.324 | +0.058 | +0.019 | $5.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (15.18 vs 4.94 bp); relationships: KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.042); failure: TOR offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no; why: higher confidence-adjusted growth (6.29 vs 3.81 bp); relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: NJD offense succeeds (4+ goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26NOV08NJTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (4.94 vs 3.75 bp); despite a smaller raw edge (+0.032 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: TOR offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes has the higher standalone adjusted growth (4.94 vs 3.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.042); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis NJD:SUPPRESSED (p 0.3965): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS (p 0.5081): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:OFFENSE_4PLUS (p 0.3944): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ3|no [DIRECT], best adjusted EV KXNHLAST-26NOV08NJTOR-TORECOWAN53-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3844, phi -0.181)
- KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3925, phi -0.256)
- KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3844, phi -0.227)
- KXNHLAST-26NOV08NJTOR-TORECOWAN53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3844, phi -0.292)

portfolios: A EV +4.58 (adj +0.98) on $30.62, P(profit) 0.5391, adj growth 8.4 bp · B EV +4.85 (adj +2.77) on $30.53, P(profit) 0.4515, adj growth 24.4 bp · C EV +4.37 (adj +1.64) on $37.29, P(profit) 0.6599, adj growth 14.3 bp · R EV +0.27 (adj +0.17) on $4.00, P(profit) 0.6684, adj growth 5.9 bp

## PHI @ CGY  ·  10000 joint draws  ·  436 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_PHI_win | p_overtime | goals | shots CGY/PHI | CGY/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.48 | 0.52 | 0.00 | 6.01 | 27.0/27.0 | 23.5/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.49 | 0.51 | 0.48 | 5.88 | 27.1/27.2 | 23.8/23.7 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.075 | 0.57 | 0.43 | 0.00 | 5.98 | 31.9/21.5 | 18.4/27.8 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.53 | 0.47 | 0.47 | 5.89 | 32.2/22.0 | 18.9/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.50 | 0.50 | 0.00 | 9.22 | 28.7/28.6 | 22.7/22.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.44 | 0.56 | 0.00 | 3.44 | 25.9/26.0 | 24.1/24.2 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Konecny: 1+ assists NO | 65 | 0.739 | 0.689 | +0.073 | +0.023 | $16.18 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Porter Martone: 1+ goals NO | 78 | 0.813 | 0.802 | +0.021 | +0.010 | $9.83 | FUNDED_RESEARCH | $3 | PHI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV08PHICGY-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (5.39 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.056); failure: PHI offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no; why: second expression of the same thesis: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no has the higher standalone adjusted growth (5.39 vs 1.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.056); they share one thesis budget; relationships: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi 0.056); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, CGY shot control · normal event (5-7) · decided (2+) 0.07.
- thesis PHI:SUPPRESSED (p 0.4273): highest fidelity KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no (same contract)
- KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3453, phi -0.216)
- KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3453, phi -0.182)

portfolios: A EV +1.66 (adj +0.59) on $24.50, P(profit) 0.6101, adj growth 5.3 bp · B EV +2.03 (adj +0.70) on $26.01, P(profit) 0.6101, adj growth 6.2 bp · C EV +2.09 (adj +0.67) on $19.11, P(profit) 0.7386, adj growth 5.9 bp · R EV +0.08 (adj +0.04) on $3.00, P(profit) 0.813, adj growth 1.4 bp

## PIT @ ANA  ·  10000 joint draws  ·  444 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_PIT_win | p_overtime | goals | shots ANA/PIT | ANA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.145 | 0.65 | 0.35 | 0.00 | 9.71 | 29.4/29.2 | 23.6/22.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.65 | 0.35 | 0.00 | 6.08 | 27.7/27.3 | 24.2/23.3 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.098 | 0.73 | 0.27 | 0.00 | 9.7 | 34.5/23.2 | 18.5/26.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.54 | 0.46 | 0.47 | 6.07 | 27.6/27.3 | 24.0/24.0 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.087 | 0.73 | 0.27 | 0.00 | 6.1 | 32.3/21.7 | 19.3/27.2 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.57 | 0.43 | 0.51 | 6.0 | 32.7/22.0 | 18.8/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim wins by over 1.5 goals YES | 32 | 0.412 | 0.364 | +0.077 | +0.028 | $6.21 | FUNDED_RESEARCH | $2 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pittsburgh wins by over 1.5 goals NO | 71 | 0.797 | 0.751 | +0.072 | +0.026 | $17.39 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Beckett Sennecke: 1+ goals YES | 36 | 0.406 | 0.394 | +0.030 | +0.017 | $3.69 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.160 | 0.150 | +0.022 | +0.012 | $4.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26NOV08PITANA-PIT2|no; why: higher confidence-adjusted growth (7.86 vs 7.77 bp); relationships: KXNHLSPREAD-26NOV08PITANA-PIT2|no: DUPLICATIVE (phi 0.423); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: REINFORCING (phi 0.164); KXNHLGOAL-26NOV08PITANA-PITCDEWAR19-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.142); failure: tight game (one-goal final or OT)
- **Pittsburgh wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV08PITANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV08PITANA-ANA2|yes has the higher standalone adjusted growth (7.86 vs 7.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.423); they share one thesis budget; relationships: KXNHLSPREAD-26NOV08PITANA-ANA2|yes: DUPLICATIVE (phi 0.423); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26NOV08PITANA-PITCDEWAR19-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.198); failure: PIT wins by 2+
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08PITANA-ANA2|yes; why: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.51 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV08PITANA-ANA2|yes: REINFORCING (phi 0.164); KXNHLSPREAD-26NOV08PITANA-PIT2|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26NOV08PITANA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV08PITANA-9|yes; why: higher confidence-adjusted growth (2.70 vs 0.42 bp); despite a smaller raw edge (+0.022 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.831 vs 0.396); alternative not eligible: confidence-adjusted EV +0.0063 below the 0.010/contract floor; relationships: KXNHLSPREAD-26NOV08PITANA-ANA2|yes: INTENTIONAL_DIVERSIFIER (phi -0.142); KXNHLSPREAD-26NOV08PITANA-PIT2|no: INTENTIONAL_DIVERSIFIER (phi -0.198); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis ANA:WINS_BY_2PLUS (p 0.4122): highest fidelity KXNHLSPREAD-26NOV08PITANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA2|yes (same contract)
- thesis ANA:WINS (p 0.6167): highest fidelity KXNHLSPREAD-26NOV08PITANA-PIT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:OFFENSE_4PLUS (p 0.5806): highest fidelity KXNHLTEAMTOTAL-26NOV08PITANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA2|yes — Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.51 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- KXNHLSPREAD-26NOV08PITANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:TIGHT (p 0.3847, phi -0.662)
- KXNHLSPREAD-26NOV08PITANA-PIT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:WINS_BY_2PLUS (p 0.2031, phi -1.0)
- KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2315, phi -0.236)
- KXNHLGOAL-26NOV08PITANA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3801, phi -0.201)
- override: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.51 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +5.06 (adj +1.42) on $30.62, P(profit) 0.5151, adj growth 11.0 bp · B EV +4.12 (adj +1.70) on $31.41, P(profit) 0.6109, adj growth 15.2 bp · C EV +3.50 (adj +1.38) on $15.53, P(profit) 0.5319, adj growth 12.0 bp · R EV +1.04 (adj +0.40) on $8.00, P(profit) 0.5578, adj growth 13.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
