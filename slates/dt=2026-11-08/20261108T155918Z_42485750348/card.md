# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-08T15:59:18Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +18.80 | +5.84 | +15.97 | 0.634 | -41.72 | -55.70 | 47.35 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +16.66 | +8.27 | +14.89 | 0.646 | -35.09 | -49.01 | 73.93 |
| C best expression per thesis | 123.30 | +15.98 | +6.51 | +14.88 | 0.644 | -34.67 | -47.49 | 56.77 |
| R FUNDED research stakes | 21.00 | +1.98 | +1.00 | +2.24 | 0.608 | -8.52 | -11.05 | 0.00 |

## FLA @ BOS  ·  10000 joint draws  ·  432 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_FLA_win | p_overtime | goals | shots BOS/FLA | BOS/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.69 | 0.31 | 0.00 | 6.05 | 27.1/27.3 | 24.7/22.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.72 | 0.28 | 0.00 | 9.47 | 28.6/28.8 | 24.0/20.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.47 | 5.97 | 27.0/27.3 | 24.0/23.7 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.081 | 0.61 | 0.39 | 0.00 | 6.05 | 21.7/32.2 | 28.8/17.9 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.53 | 0.47 | 0.46 | 5.93 | 21.5/32.1 | 28.6/18.2 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.064 | 0.60 | 0.40 | 0.00 | 9.37 | 22.9/33.7 | 28.2/16.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Casey Mittelstadt: 1+ goals YES | 17 | 0.211 | 0.200 | +0.031 | +0.020 | $5.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Pavel Zacha: 1+ goals YES | 29 | 0.337 | 0.324 | +0.032 | +0.019 | $5.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Sam Bennett: 1+ goals YES | 25 | 0.295 | 0.281 | +0.032 | +0.018 | $5.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 67 | 0.712 | 0.700 | +0.026 | +0.015 | $10.21 | FUNDED_RESEARCH | $3 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08FLABOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (5.78 vs 3.86 bp); despite a smaller raw edge (+0.031 vs +0.032/contract); relationships: KXNHLGOAL-26NOV08FLABOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV08FLABOS-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV08FLABOS-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: BOS offense suppressed (<= 2 goals)
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes; why: higher confidence-adjusted growth (3.86 vs 1.72 bp); despite a smaller raw edge (+0.032 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV08FLABOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV08FLABOS-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV08FLABOS-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: BOS offense suppressed (<= 2 goals)
- **Sam Bennett: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV08FLABOS-7|yes; why: higher confidence-adjusted growth (3.66 vs 1.04 bp); despite a smaller raw edge (+0.032 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.924 vs 0.683); relationships: KXNHLGOAL-26NOV08FLABOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV08FLABOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV08FLABOS-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: FLA offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV08FLABOS-FLASREINHART13-1|no; why: Player prop expression KXNHLGOAL-26NOV08FLABOS-FLASREINHART13-1|no selected over player prop KXNHLAST-26NOV08FLABOS-FLASREINHART13-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV08FLABOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV08FLABOS-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV08FLABOS-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BOS:OFFENSE_4PLUS (p 0.5148): highest fidelity KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08FLABOS-BOSPZACHA18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:OFFENSE_4PLUS (p 0.3332): highest fidelity KXNHLTOTAL-26NOV08FLABOS-7|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV08FLABOS-FLASBENNETT9-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.4481): highest fidelity KXNHLGOAL-26NOV08FLABOS-FLASREINHART13-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV08FLABOS-FLASREINHART13-1|no — Player prop expression KXNHLGOAL-26NOV08FLABOS-FLASREINHART13-1|no selected over player prop KXNHLAST-26NOV08FLABOS-FLASREINHART13-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26NOV08FLABOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.28, phi -0.186)
- KXNHLGOAL-26NOV08FLABOS-BOSPZACHA18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.28, phi -0.229)
- KXNHLGOAL-26NOV08FLABOS-FLASBENNETT9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4481, phi -0.259)
- KXNHLGOAL-26NOV08FLABOS-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3332, phi -0.279)
- override: Player prop expression KXNHLGOAL-26NOV08FLABOS-FLASREINHART13-1|no selected over player prop KXNHLAST-26NOV08FLABOS-FLASREINHART13-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.83 (adj +0.97) on $33.34, P(profit) 0.4368, adj growth 7.0 bp · B EV +2.52 (adj +1.50) on $26.30, P(profit) 0.5327, adj growth 13.3 bp · C EV +3.43 (adj +1.38) on $33.90, P(profit) 0.6526, adj growth 12.1 bp · R EV +0.12 (adj +0.06) on $3.00, P(profit) 0.7118, adj growth 2.2 bp

## VGK @ BUF  ·  10000 joint draws  ·  452 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_VGK_win | p_overtime | goals | shots BUF/VGK | BUF/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.53 | 0.47 | 0.00 | 6.01 | 27.4/27.6 | 24.1/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.49 | 0.51 | 0.47 | 5.99 | 27.7/27.7 | 24.3/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.47 | 0.53 | 0.00 | 9.33 | 29.2/29.1 | 22.8/23.2 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.073 | 0.57 | 0.43 | 0.00 | 5.99 | 32.6/21.9 | 18.8/28.5 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.064 | 0.44 | 0.56 | 0.00 | 6.03 | 22.0/32.3 | 28.3/18.8 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.53 | 0.47 | 0.45 | 5.9 | 32.8/22.3 | 19.1/29.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.072 | 0.067 | +0.019 | +0.013 | $2.79 | FUNDED_RESEARCH | $1 | VGK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08VGKBUF-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (7.32 vs 1.29 bp); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VGK:OFFENSE_4PLUS (p 0.3967): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV08VGKBUF-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3847, phi -0.118)

portfolios: A EV +1.15 (adj +0.81) on $3.29, P(profit) 0.072, adj growth 6.9 bp · B EV +0.98 (adj +0.69) on $2.79, P(profit) 0.072, adj growth 6.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.35 (adj +0.25) on $1.00, P(profit) 0.072, adj growth 8.1 bp

## TBL @ WPG  ·  10000 joint draws  ·  386 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_TBL_win | p_overtime | goals | shots WPG/TBL | WPG/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.52 | 0.48 | 0.00 | 6.0 | 26.8/27.2 | 23.8/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.47 | 5.96 | 27.1/27.5 | 24.3/23.6 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.095 | 0.39 | 0.61 | 0.00 | 5.98 | 21.6/32.6 | 28.5/18.8 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.46 | 0.54 | 0.48 | 5.88 | 21.5/32.6 | 29.3/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.48 | 0.52 | 0.00 | 9.27 | 28.5/29.0 | 22.8/22.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.51 | 0.49 | 0.00 | 3.49 | 25.9/26.0 | 24.1/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charle-Edouard D'Astous: 1+ goals NO | 89 | 0.930 | 0.919 | +0.033 | +0.022 | $17.60 | FUNDED_RESEARCH | $5 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Cole Perfetti: 1+ assists YES | 32 | 0.396 | 0.355 | +0.061 | +0.020 | $6.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.58) | EVIDENCE_MIXED | D |
| Alex Iafallo: 1+ goals YES | 13 | 0.159 | 0.150 | +0.021 | +0.012 | $2.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| John Carlson: 1+ assists NO | 64 | 0.708 | 0.669 | +0.052 | +0.013 | $8.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV08TBWPG-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (11.84 vs 1.64 bp); despite a smaller raw edge (+0.033 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26NOV08TBWPG-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.074); failure: TBL offense succeeds (4+ goals)
- **Cole Perfetti: 1+ assists YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08TBWPG-TB2|no; why: higher confidence-adjusted growth (4.02 vs 0.98 bp); alternative not eligible: confidence-adjusted EV +0.0100 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV08TBWPG-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLAST-26NOV08TBWPG-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: WPG offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes has the higher standalone adjusted growth (4.02 vs 2.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.032); they share one thesis budget; relationships: KXNHLGOAL-26NOV08TBWPG-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLAST-26NOV08TBWPG-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: WPG offense suppressed (<= 2 goals)
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV08TBWPG-TB2|no; why: higher confidence-adjusted growth (1.64 vs 0.98 bp); alternative not eligible: confidence-adjusted EV +0.0100 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV08TBWPG-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.3592): highest fidelity KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.4017): highest fidelity KXNHLAST-26NOV08TBWPG-TBJCARLSON74-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV08TBWPG-TBJCARLSON74-1|no (same contract)
- KXNHLGOAL-26NOV08TBWPG-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3836, phi -0.11)
- KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 42% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4151, phi -0.314)
- KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4151, phi -0.188)
- KXNHLAST-26NOV08TBWPG-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3836, phi -0.247)

portfolios: A EV +2.69 (adj +0.99) on $33.34, P(profit) 0.3949, adj growth 8.9 bp · B EV +2.90 (adj +1.24) on $35.17, P(profit) 0.4556, adj growth 11.3 bp · C EV +2.13 (adj +0.64) on $17.43, P(profit) 0.396, adj growth 5.6 bp · R EV +0.19 (adj +0.12) on $5.00, P(profit) 0.9303, adj growth 4.8 bp

## NJD @ TOR  ·  10000 joint draws  ·  442 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NJD_win | p_overtime | goals | shots TOR/NJD | TOR/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.127 | 0.46 | 0.54 | 0.00 | 5.96 | 22.8/35.6 | 31.6/19.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.48 | 0.52 | 0.45 | 5.96 | 23.4/35.7 | 32.2/20.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.53 | 0.47 | 0.00 | 6.0 | 28.8/29.5 | 26.0/25.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.51 | 0.49 | 0.47 | 5.95 | 28.9/29.7 | 26.3/25.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.55 | 0.45 | 0.00 | 9.3 | 30.4/31.3 | 25.3/24.2 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.078 | 0.45 | 0.55 | 0.00 | 9.37 | 24.6/37.5 | 30.4/18.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.156 | 0.141 | +0.039 | +0.024 | $5.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 61 | 0.671 | 0.653 | +0.044 | +0.027 | $12.05 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 74 | 0.788 | 0.773 | +0.035 | +0.020 | $14.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals YES | 18 | 0.220 | 0.208 | +0.030 | +0.018 | $4.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (11.64 vs 4.30 bp); relationships: KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: TOR offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no; why: higher confidence-adjusted growth (6.71 vs 4.76 bp); relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: NJD offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no has the higher standalone adjusted growth (6.71 vs 4.76 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NJD offense succeeds (4+ goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (11.64 vs 4.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3944): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3965): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS (p 0.5081): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3844, phi -0.201)
- KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3925, phi -0.247)
- KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3925, phi -0.232)
- KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3844, phi -0.21)

portfolios: A EV +4.14 (adj +1.06) on $33.34, P(profit) 0.5327, adj growth 8.5 bp · B EV +3.94 (adj +2.35) on $36.00, P(profit) 0.6719, adj growth 21.0 bp · C EV +4.49 (adj +2.25) on $36.08, P(profit) 0.6283, adj growth 19.6 bp · R EV +0.28 (adj +0.17) on $4.00, P(profit) 0.6712, adj growth 6.1 bp

## PHI @ CGY  ·  10000 joint draws  ·  434 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_PHI_win | p_overtime | goals | shots CGY/PHI | CGY/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.51 | 0.49 | 0.00 | 5.98 | 27.2/27.1 | 23.6/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.50 | 0.50 | 0.49 | 5.82 | 27.4/27.2 | 23.9/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.52 | 0.48 | 0.00 | 9.16 | 28.7/28.5 | 22.7/22.7 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.072 | 0.57 | 0.43 | 0.00 | 5.95 | 32.6/22.1 | 19.0/28.5 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.55 | 0.45 | 0.48 | 5.88 | 32.2/21.6 | 18.4/28.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.49 | 0.51 | 0.00 | 3.39 | 25.8/25.9 | 24.0/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Konecny: 1+ assists NO | 65 | 0.739 | 0.690 | +0.073 | +0.024 | $17.04 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV08PHICGY-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (5.54 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis PHI:SUPPRESSED (p 0.4302): highest fidelity KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no (same contract)
- KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3508, phi -0.234)

portfolios: A EV +1.47 (adj +0.47) on $13.34, P(profit) 0.7392, adj growth 4.4 bp · B EV +1.88 (adj +0.61) on $17.04, P(profit) 0.7392, adj growth 5.4 bp · C EV +2.13 (adj +0.69) on $19.36, P(profit) 0.7392, adj growth 6.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ ANA  ·  10000 joint draws  ·  444 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_PIT_win | p_overtime | goals | shots ANA/PIT | ANA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.137 | 0.66 | 0.34 | 0.00 | 9.77 | 29.4/29.3 | 23.8/22.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.68 | 0.32 | 0.00 | 6.08 | 27.6/27.4 | 24.7/23.1 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.100 | 0.74 | 0.26 | 0.00 | 9.7 | 34.7/23.5 | 18.7/26.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.53 | 0.47 | 0.47 | 6.03 | 27.7/27.3 | 23.9/24.2 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.084 | 0.71 | 0.29 | 0.00 | 6.1 | 32.4/21.8 | 19.3/27.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.56 | 0.44 | 0.49 | 6.05 | 32.6/21.8 | 18.6/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim wins by over 1.5 goals YES | 32 | 0.412 | 0.364 | +0.077 | +0.028 | $6.54 | FUNDED_RESEARCH | $2 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pittsburgh wins by over 1.5 goals NO | 71 | 0.797 | 0.751 | +0.072 | +0.026 | $17.60 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Connor Dewar: 1+ goals YES | 13 | 0.163 | 0.152 | +0.025 | +0.015 | $4.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 36 | 0.406 | 0.394 | +0.030 | +0.017 | $3.73 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26NOV08PITANA-PIT2|no; why: higher confidence-adjusted growth (7.86 vs 7.77 bp); relationships: KXNHLSPREAD-26NOV08PITANA-PIT2|no: DUPLICATIVE (phi 0.423); KXNHLGOAL-26NOV08PITANA-PITCDEWAR19-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.154); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: REINFORCING (phi 0.164); failure: tight game (one-goal final or OT)
- **Pittsburgh wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV08PITANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV08PITANA-ANA2|yes has the higher standalone adjusted growth (7.86 vs 7.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.423); they share one thesis budget; relationships: KXNHLSPREAD-26NOV08PITANA-ANA2|yes: DUPLICATIVE (phi 0.423); KXNHLGOAL-26NOV08PITANA-PITCDEWAR19-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.209); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.147); failure: PIT wins by 2+
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV08PITANA-9|yes; why: higher confidence-adjusted growth (3.86 vs 0.15 bp); despite a smaller raw edge (+0.025 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.848 vs 0.393); alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: KXNHLSPREAD-26NOV08PITANA-ANA2|yes: INTENTIONAL_DIVERSIFIER (phi -0.154); KXNHLSPREAD-26NOV08PITANA-PIT2|no: INTENTIONAL_DIVERSIFIER (phi -0.209); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: PIT offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08PITANA-ANA2|yes; why: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.51 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV08PITANA-ANA2|yes: REINFORCING (phi 0.164); KXNHLSPREAD-26NOV08PITANA-PIT2|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26NOV08PITANA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis ANA:WINS_BY_2PLUS (p 0.4122): highest fidelity KXNHLSPREAD-26NOV08PITANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA2|yes (same contract)
- thesis ANA:WINS (p 0.6167): highest fidelity KXNHLSPREAD-26NOV08PITANA-PIT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:OFFENSE_4PLUS (p 0.5806): highest fidelity KXNHLTEAMTOTAL-26NOV08PITANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA2|yes — Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.51 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- KXNHLSPREAD-26NOV08PITANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:TIGHT (p 0.3847, phi -0.662)
- KXNHLSPREAD-26NOV08PITANA-PIT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:WINS_BY_2PLUS (p 0.2031, phi -1.0)
- KXNHLGOAL-26NOV08PITANA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3801, phi -0.203)
- KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2315, phi -0.236)
- override: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.51 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +5.51 (adj +1.54) on $33.34, P(profit) 0.5151, adj growth 11.7 bp · B EV +4.45 (adj +1.88) on $32.70, P(profit) 0.6575, adj growth 16.8 bp · C EV +3.80 (adj +1.55) on $16.53, P(profit) 0.5362, adj growth 13.5 bp · R EV +1.04 (adj +0.40) on $8.00, P(profit) 0.5578, adj growth 13.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
