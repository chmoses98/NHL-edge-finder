# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-08T17:42:56Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +22.07 | +6.72 | +21.94 | 0.681 | -37.33 | -53.01 | 56.88 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +23.94 | +13.66 | +16.36 | 0.623 | -41.87 | -56.33 | 119.08 |
| C best expression per thesis | 137.63 | +18.56 | +7.34 | +17.03 | 0.652 | -35.65 | -48.85 | 64.14 |
| R FUNDED research stakes | 20.00 | +1.83 | +1.00 | +2.18 | 0.606 | -10.04 | -10.54 | 0.00 |

## FLA @ BOS  ·  10000 joint draws  ·  430 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.578 / away 0.422

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_FLA_win | p_overtime | goals | shots BOS/FLA | BOS/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.69 | 0.31 | 0.00 | 6.04 | 27.1/27.3 | 24.5/22.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.112 | 0.71 | 0.29 | 0.00 | 9.42 | 28.7/28.7 | 23.7/21.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.54 | 0.46 | 0.46 | 5.97 | 27.0/27.4 | 24.3/23.7 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.084 | 0.65 | 0.35 | 0.00 | 5.99 | 21.7/32.4 | 29.2/17.5 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.55 | 0.45 | 0.48 | 5.97 | 21.3/32.2 | 29.0/18.0 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.061 | 0.62 | 0.38 | 0.00 | 9.4 | 23.3/34.3 | 28.4/16.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nikita Zadorov: 1+ goals YES | 4 | 0.065 | 0.067 | +0.023 | +0.024 | $4.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Niko Mikkola: 1+ goals YES | 4 | 0.065 | 0.061 | +0.022 | +0.018 | $3.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Hampus Lindholm: 1+ goals YES | 6 | 0.088 | 0.081 | +0.024 | +0.017 | $3.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 66 | 0.716 | 0.701 | +0.040 | +0.025 | $16.51 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Nikita Zadorov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08FLABOS-BOS6|yes; why: higher confidence-adjusted growth (28.53 vs 10.33 bp); despite a smaller raw edge (+0.023 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.902 vs 0.316); relationships: KXNHLGOAL-26NOV08FLABOS-FLANMIKKOLA77-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV08FLABOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV08FLABOS-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: BOS offense suppressed (<= 2 goals)
- **Niko Mikkola: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV08FLABOS-6|yes; why: higher confidence-adjusted growth (17.04 vs 3.68 bp); despite a smaller raw edge (+0.022 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.846 vs 0.706); relationships: KXNHLGOAL-26NOV08FLABOS-BOSNZADOROV91-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV08FLABOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV08FLABOS-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: FLA offense suppressed (<= 2 goals)
- **Hampus Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08FLABOS-BOS6|yes; why: KXNHLTEAMTOTAL-26NOV08FLABOS-BOS6|yes has the higher standalone adjusted growth (10.33 vs 10.15 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.097); relationships: KXNHLGOAL-26NOV08FLABOS-BOSNZADOROV91-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV08FLABOS-FLANMIKKOLA77-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV08FLABOS-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: BOS offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV08FLABOS-BOS3|yes; why: higher confidence-adjusted growth (6.29 vs 2.05 bp); despite a smaller raw edge (+0.040 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.007 vs 0.474); relationships: KXNHLGOAL-26NOV08FLABOS-BOSNZADOROV91-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV08FLABOS-FLANMIKKOLA77-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV08FLABOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.5219): highest fidelity KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.3144): highest fidelity KXNHLTOTAL-26NOV08FLABOS-6|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:WINS (p 0.6324): highest fidelity KXNHLTEAMTOTAL-26NOV08FLABOS-BOS2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV08FLABOS-BOSNZADOROV91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.2732, phi -0.099)
- KXNHLGOAL-26NOV08FLABOS-FLANMIKKOLA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4562, phi -0.121)
- KXNHLGOAL-26NOV08FLABOS-BOSHLINDHOLM27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.2732, phi -0.112)
- KXNHLGOAL-26NOV08FLABOS-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3283, phi -0.236)

portfolios: A EV +3.79 (adj +1.05) on $27.78, P(profit) 0.5872, adj growth 8.2 bp · B EV +6.76 (adj +5.84) on $28.56, P(profit) 0.2023, adj growth 49.2 bp · C EV +4.43 (adj +1.87) on $33.43, P(profit) 0.4605, adj growth 16.4 bp · R EV +0.30 (adj +0.19) on $5.00, P(profit) 0.716, adj growth 6.5 bp

## VGK @ BUF  ·  10000 joint draws  ·  458 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.496 / away 0.504

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
| Victor Olofsson: 1+ assists NO | 75 | 0.836 | 0.791 | +0.073 | +0.028 | $16.89 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 5 | 0.072 | 0.067 | +0.019 | +0.013 | $2.76 | FUNDED_RESEARCH | $1 | VGK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Olen Zellweger: 1+ goals YES | 8 | 0.107 | 0.099 | +0.022 | +0.014 | $3.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Mark Stone: 1+ assists NO | 56 | 0.626 | 0.591 | +0.049 | +0.013 | $7.20 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Victor Olofsson: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV08VGKBUF-VGKMSTONE61-1|no; why: higher confidence-adjusted growth (9.29 vs 1.60 bp); relationships: KXNHLGOAL-26NOV08VGKBUF-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV08VGKBUF-BUFOZELLWEGER8-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26NOV08VGKBUF-VGKMSTONE61-1|no: MOSTLY_INDEPENDENT (phi 0.05); failure: VGK offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08VGKBUF-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (7.32 vs 1.29 bp); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLAST-26NOV08VGKBUF-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV08VGKBUF-BUFOZELLWEGER8-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV08VGKBUF-VGKMSTONE61-1|no: MOSTLY_INDEPENDENT (phi -0.045); failure: VGK offense suppressed (<= 2 goals)
- **Olen Zellweger: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08VGKBUF-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (5.41 vs 2.01 bp); despite a smaller raw edge (+0.022 vs +0.024/contract); relationships: KXNHLAST-26NOV08VGKBUF-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV08VGKBUF-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV08VGKBUF-VGKMSTONE61-1|no: MOSTLY_INDEPENDENT (phi -0.027); failure: BUF offense suppressed (<= 2 goals)
- **Mark Stone: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV08VGKBUF-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (1.60 vs 0.77 bp); despite a smaller raw edge (+0.049 vs +0.105/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0094 below the 0.010/contract floor; relationships: KXNHLAST-26NOV08VGKBUF-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi 0.05); KXNHLGOAL-26NOV08VGKBUF-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26NOV08VGKBUF-BUFOZELLWEGER8-1|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.401): highest fidelity KXNHLGOAL-26NOV08VGKBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV08VGKBUF-BUFZBENSON6-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.3847): highest fidelity KXNHLAST-26NOV08VGKBUF-VGKMSTONE61-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV08VGKBUF-VGKMSTONE61-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.3967): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV08VGKBUF-VGKVOLOFSSON95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3967, phi -0.18)
- KXNHLGOAL-26NOV08VGKBUF-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3847, phi -0.118)
- KXNHLGOAL-26NOV08VGKBUF-BUFOZELLWEGER8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3804, phi -0.139)
- KXNHLAST-26NOV08VGKBUF-VGKMSTONE61-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3967, phi -0.271)

portfolios: A EV +3.05 (adj +1.33) on $27.78, P(profit) 0.6844, adj growth 12.0 bp · B EV +3.98 (adj +1.95) on $29.87, P(profit) 0.6221, adj growth 17.6 bp · C EV +1.08 (adj +0.41) on $12.37, P(profit) 0.7287, adj growth 3.6 bp · R EV +0.35 (adj +0.25) on $1.00, P(profit) 0.072, adj growth 8.1 bp

## TBL @ WPG  ·  10000 joint draws  ·  402 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.427 / away 0.573

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
| Cole Perfetti: 1+ assists YES | 32 | 0.396 | 0.355 | +0.061 | +0.020 | $5.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.58) | EVIDENCE_MIXED | D |
| Alex Iafallo: 1+ goals YES | 13 | 0.159 | 0.149 | +0.021 | +0.011 | $2.35 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 77 | 0.821 | 0.793 | +0.039 | +0.011 | $6.16 | FUNDED_RESEARCH | $2 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ assists NO | 40 | 0.537 | 0.427 | +0.120 | +0.010 | $3.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.73) | CALIBRATION_WARNING | D |
- **Cole Perfetti: 1+ assists YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08TBWPG-TB3|no; why: higher confidence-adjusted growth (4.02 vs 1.46 bp); relationships: KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLSPREAD-26NOV08TBWPG-TB3|no: REINFORCING (phi 0.162); KXNHLAST-26NOV08TBWPG-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.023); failure: WPG offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes has the higher standalone adjusted growth (4.02 vs 2.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.032); they share one thesis budget; relationships: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLSPREAD-26NOV08TBWPG-TB3|no: MOSTLY_INDEPENDENT (phi 0.096); KXNHLAST-26NOV08TBWPG-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: WPG offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes has the higher standalone adjusted growth (4.02 vs 1.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.162); they share one thesis budget; relationships: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: REINFORCING (phi 0.162); KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.096); KXNHLAST-26NOV08TBWPG-TBNKUCHEROV86-1|no: REINFORCING (phi 0.19); failure: TBL wins by 2+
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV08TBWPG-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV08TBWPG-TB3|no has the higher standalone adjusted growth (1.46 vs 0.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.190); they share one thesis budget; relationships: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSPREAD-26NOV08TBWPG-TB3|no: REINFORCING (phi 0.19); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.3592): highest fidelity KXNHLSPREAD-26NOV08TBWPG-TB3|no [DIRECT], best adjusted EV KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.4829): highest fidelity KXNHLSPREAD-26NOV08TBWPG-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.4017): highest fidelity KXNHLSPREAD-26NOV08TBWPG-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08TBWPG-TB3|no (same contract)
- KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 42% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4151, phi -0.314)
- KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4151, phi -0.188)
- KXNHLSPREAD-26NOV08TBWPG-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2932, phi -0.725)
- KXNHLAST-26NOV08TBWPG-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 27% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.7 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3836, phi -0.301)

portfolios: A EV +4.75 (adj +1.03) on $27.78, P(profit) 0.6869, adj growth 8.5 bp · B EV +2.61 (adj +0.69) on $17.37, P(profit) 0.4524, adj growth 6.2 bp · C EV +1.72 (adj +0.54) on $17.09, P(profit) 0.396, adj growth 4.8 bp · R EV +0.25 (adj +0.11) on $3.00, P(profit) 0.1587, adj growth 3.6 bp

## NJD @ TOR  ·  10000 joint draws  ·  442 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.419 / away 0.581

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
| Teddy Blueger: 1+ goals YES | 10 | 0.146 | 0.127 | +0.040 | +0.021 | $4.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals YES | 17 | 0.222 | 0.205 | +0.042 | +0.025 | $6.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 61 | 0.668 | 0.652 | +0.042 | +0.026 | $14.50 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Colton Sissons: 1+ goals YES | 9 | 0.128 | 0.109 | +0.032 | +0.014 | $2.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (9.95 vs 9.48 bp); despite a smaller raw edge (+0.040 vs +0.042/contract); relationships: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: TOR offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08NJTOR-TOR2|yes; why: higher confidence-adjusted growth (9.48 vs 5.92 bp); despite a smaller raw edge (+0.042 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.917 vs 0.56); relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: TOR offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV08NJTOR-TOR2|yes; why: higher confidence-adjusted growth (6.29 vs 5.92 bp); despite a smaller raw edge (+0.042 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.009 vs 0.56); relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NJD offense succeeds (4+ goals)
- **Colton Sissons: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes has the higher standalone adjusted growth (9.48 vs 4.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3944): highest fidelity KXNHLTEAMTOTAL-26NOV08NJTOR-TOR3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3965): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS (p 0.5081): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3844, phi -0.181)
- KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3844, phi -0.227)
- KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3925, phi -0.256)
- KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3844, phi -0.168)

portfolios: A EV +4.96 (adj +1.48) on $27.78, P(profit) 0.4829, adj growth 12.6 bp · B EV +4.90 (adj +2.69) on $27.53, P(profit) 0.4206, adj growth 23.9 bp · C EV +5.75 (adj +2.31) on $40.57, P(profit) 0.6857, adj growth 20.1 bp · R EV +0.27 (adj +0.17) on $4.00, P(profit) 0.6684, adj growth 5.9 bp

## PHI @ CGY  ·  10000 joint draws  ·  444 bet sides mapped, 1 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.483 / away 0.517

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
| Travis Konecny: 1+ assists NO | 65 | 0.739 | 0.689 | +0.073 | +0.023 | $16.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV08PHICGY-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (5.39 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, CGY shot control · normal event (5-7) · decided (2+) 0.07.
- thesis PHI:SUPPRESSED (p 0.4273): highest fidelity KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no (same contract)
- KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3453, phi -0.216)

portfolios: A EV +1.21 (adj +0.39) on $11.11, P(profit) 0.7386, adj growth 3.6 bp · B EV +1.76 (adj +0.57) on $16.14, P(profit) 0.7386, adj growth 5.1 bp · C EV +2.09 (adj +0.67) on $19.11, P(profit) 0.7386, adj growth 5.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ ANA  ·  10000 joint draws  ·  446 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

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
| Alex Killorn: 1+ goals YES | 19 | 0.242 | 0.225 | +0.041 | +0.025 | $5.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Pittsburgh wins by over 1.5 goals NO | 71 | 0.797 | 0.751 | +0.072 | +0.026 | $16.89 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tim Washe: 1+ goals YES | 13 | 0.168 | 0.154 | +0.030 | +0.017 | $3.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 36 | 0.406 | 0.394 | +0.030 | +0.017 | $4.74 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08PITANA-ANA2|yes; why: higher confidence-adjusted growth (8.13 vs 7.86 bp); despite a smaller raw edge (+0.041 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.8 vs 0.513); relationships: KXNHLSPREAD-26NOV08PITANA-PIT2|no: MOSTLY_INDEPENDENT (phi 0.125); KXNHLGOAL-26NOV08PITANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: ANA offense suppressed (<= 2 goals)
- **Pittsburgh wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV08PITANA-ANA2|yes; why: KXNHLSPREAD-26NOV08PITANA-ANA2|yes has the higher standalone adjusted growth (7.86 vs 7.77 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.423); relationships: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.125); KXNHLGOAL-26NOV08PITANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.089); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.147); failure: PIT wins by 2+
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (8.13 vs 4.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26NOV08PITANA-PIT2|no: MOSTLY_INDEPENDENT (phi 0.089); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: ANA offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (8.13 vs 2.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26NOV08PITANA-PIT2|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26NOV08PITANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.5806): highest fidelity KXNHLTEAMTOTAL-26NOV08PITANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.4122): highest fidelity KXNHLSPREAD-26NOV08PITANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA2|yes (same contract)
- thesis ANA:WINS (p 0.6167): highest fidelity KXNHLSPREAD-26NOV08PITANA-PIT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2315, phi -0.179)
- KXNHLSPREAD-26NOV08PITANA-PIT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:WINS_BY_2PLUS (p 0.2031, phi -1.0)
- KXNHLGOAL-26NOV08PITANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2315, phi -0.143)
- KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2315, phi -0.236)

portfolios: A EV +4.32 (adj +1.44) on $27.78, P(profit) 0.5151, adj growth 11.9 bp · B EV +3.94 (adj +1.92) on $30.54, P(profit) 0.5484, adj growth 17.1 bp · C EV +3.49 (adj +1.54) on $15.06, P(profit) 0.519, adj growth 13.4 bp · R EV +0.66 (adj +0.28) on $7.00, P(profit) 0.3528, adj growth 9.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
