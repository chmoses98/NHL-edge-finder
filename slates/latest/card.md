# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-08T18:43:05Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +23.04 | +7.59 | +20.22 | 0.636 | -51.96 | -71.35 | 58.27 |
| B thesis-diversified (joint) ← optimiser card | 116.68 | +16.25 | +8.60 | +13.35 | 0.610 | -42.94 | -50.81 | 75.37 |
| C best expression per thesis | 81.29 | +13.01 | +5.57 | +11.17 | 0.607 | -36.76 | -47.07 | 48.40 |
| R FUNDED research stakes | 13.00 | +1.43 | +0.76 | +0.29 | 0.622 | -6.62 | -7.68 | 0.00 |

## VGK @ BUF  ·  10000 joint draws  ·  458 bet sides mapped, 6 +EV candidates, 4 on card

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
| Victor Olofsson: 1+ assists NO | 75 | 0.836 | 0.791 | +0.073 | +0.028 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 5 | 0.072 | 0.065 | +0.019 | +0.012 | $2.83 | FUNDED_RESEARCH | $1 | VGK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Marc Gatcomb: 1+ goals YES | 7 | 0.098 | 0.088 | +0.023 | +0.014 | $3.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Olen Zellweger: 1+ goals YES | 8 | 0.107 | 0.099 | +0.022 | +0.014 | $3.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Victor Olofsson: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV08VGKBUF-VGKMSTONE61-1|no; why: higher confidence-adjusted growth (9.29 vs 1.60 bp); relationships: KXNHLGOAL-26NOV08VGKBUF-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV08VGKBUF-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26NOV08VGKBUF-BUFOZELLWEGER8-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: VGK offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08VGKBUF-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (6.01 vs 1.29 bp); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLAST-26NOV08VGKBUF-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV08VGKBUF-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV08VGKBUF-BUFOZELLWEGER8-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: VGK offense suppressed (<= 2 goals)
- **Marc Gatcomb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08VGKBUF-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (5.79 vs 1.29 bp); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLAST-26NOV08VGKBUF-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26NOV08VGKBUF-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV08VGKBUF-BUFOZELLWEGER8-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense suppressed (<= 2 goals)
- **Olen Zellweger: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08VGKBUF-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (5.41 vs 2.01 bp); despite a smaller raw edge (+0.022 vs +0.024/contract); relationships: KXNHLAST-26NOV08VGKBUF-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV08VGKBUF-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV08VGKBUF-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.401): highest fidelity KXNHLGOAL-26NOV08VGKBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV08VGKBUF-BUFZBENSON6-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.3847): highest fidelity KXNHLAST-26NOV08VGKBUF-VGKMSTONE61-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV08VGKBUF-VGKMSTONE61-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.3967): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV08VGKBUF-VGKVOLOFSSON95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3967, phi -0.18)
- KXNHLGOAL-26NOV08VGKBUF-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3847, phi -0.118)
- KXNHLGOAL-26NOV08VGKBUF-VGKMGATCOMB17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3847, phi -0.152)
- KXNHLGOAL-26NOV08VGKBUF-BUFOZELLWEGER8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3804, phi -0.139)

portfolios: A EV +4.94 (adj +2.15) on $42.61, P(profit) 0.6784, adj growth 17.9 bp · B EV +4.86 (adj +2.55) on $29.72, P(profit) 0.2516, adj growth 22.5 bp · C EV +1.08 (adj +0.41) on $12.37, P(profit) 0.7287, adj growth 3.6 bp · R EV +0.35 (adj +0.22) on $1.00, P(profit) 0.072, adj growth 7.1 bp

## TBL @ WPG  ·  10000 joint draws  ·  410 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.426 / away 0.574

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
| Cole Perfetti: 1+ assists YES | 32 | 0.396 | 0.353 | +0.061 | +0.018 | $6.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.58) | EVIDENCE_MIXED | D |
| Alex Iafallo: 1+ goals YES | 13 | 0.159 | 0.150 | +0.021 | +0.012 | $3.30 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Cole Perfetti: 1+ assists YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08TBWPG-TB2|no; why: higher confidence-adjusted growth (3.09 vs 0.98 bp); alternative not eligible: confidence-adjusted EV +0.0100 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.032); failure: WPG offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes has the higher standalone adjusted growth (3.09 vs 2.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.032); they share one thesis budget; relationships: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi 0.032); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.3592): highest fidelity KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes (same contract)
- KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 42% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4151, phi -0.314)
- KXNHLGOAL-26NOV08TBWPG-WPGAIAFALLO9-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4151, phi -0.188)

portfolios: A EV +3.86 (adj +1.36) on $22.18, P(profit) 0.4862, adj growth 9.6 bp · B EV +1.61 (adj +0.62) on $9.45, P(profit) 0.4862, adj growth 5.4 bp · C EV +1.15 (adj +0.34) on $6.33, P(profit) 0.396, adj growth 2.9 bp · R EV +0.15 (adj +0.09) on $1.00, P(profit) 0.1587, adj growth 3.0 bp

## NJD @ TOR  ·  10000 joint draws  ·  444 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.417 / away 0.583

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
| Easton Cowan: 1+ goals YES | 17 | 0.222 | 0.208 | +0.042 | +0.028 | $7.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Colton Sissons: 1+ goals YES | 9 | 0.128 | 0.116 | +0.032 | +0.020 | $4.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 61 | 0.668 | 0.652 | +0.042 | +0.026 | $15.96 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Nico Hischier: 1+ goals NO | 69 | 0.735 | 0.722 | +0.030 | +0.017 | $14.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08NJTOR-TOR2|yes; why: higher confidence-adjusted growth (11.42 vs 5.92 bp); despite a smaller raw edge (+0.042 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.917 vs 0.56); relationships: KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV08NJTOR-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: TOR offense suppressed (<= 2 goals)
- **Colton Sissons: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes has the higher standalone adjusted growth (11.42 vs 9.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV08NJTOR-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: TOR offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV08NJTOR-TOR2|yes; why: higher confidence-adjusted growth (6.29 vs 5.92 bp); despite a smaller raw edge (+0.042 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.009 vs 0.56); relationships: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV08NJTOR-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense succeeds (4+ goals)
- **Nico Hischier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no has the higher standalone adjusted growth (6.29 vs 3.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense succeeds (4+ goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3944): highest fidelity KXNHLTEAMTOTAL-26NOV08NJTOR-TOR3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3965): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS (p 0.5081): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3844, phi -0.227)
- KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3844, phi -0.168)
- KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3925, phi -0.256)
- KXNHLGOAL-26NOV08NJTOR-NJNHISCHIER13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3925, phi -0.238)

portfolios: A EV +7.61 (adj +1.87) on $42.61, P(profit) 0.482, adj growth 14.6 bp · B EV +5.16 (adj +3.27) on $42.87, P(profit) 0.6531, adj growth 28.4 bp · C EV +5.93 (adj +2.52) on $41.40, P(profit) 0.701, adj growth 21.9 bp · R EV +0.27 (adj +0.17) on $4.00, P(profit) 0.6684, adj growth 5.9 bp

## PHI @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 0 +EV candidates, 0 on card

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

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, CGY shot control · normal event (5-7) · decided (2+) 0.07.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ ANA  ·  10000 joint draws  ·  454 bet sides mapped, 10 +EV candidates, 4 on card

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
| Pittsburgh wins by over 1.5 goals NO | 71 | 0.797 | 0.751 | +0.072 | +0.026 | $20.00 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Connor Dewar: 1+ goals YES | 12 | 0.160 | 0.144 | +0.033 | +0.016 | $5.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 12 | 0.155 | 0.144 | +0.028 | +0.016 | $3.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 36 | 0.406 | 0.394 | +0.030 | +0.017 | $5.55 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Pittsburgh wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV08PITANA-ANA2|yes; why: KXNHLSPREAD-26NOV08PITANA-ANA2|yes has the higher standalone adjusted growth (7.86 vs 7.77 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.423); relationships: KXNHLGOAL-26NOV08PITANA-PITCDEWAR19-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.198); KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.095); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.147); failure: PIT wins by 2+
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV08PITANA-9|yes; why: higher confidence-adjusted growth (5.25 vs 0.42 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.831 vs 0.396); alternative not eligible: confidence-adjusted EV +0.0063 below the 0.010/contract floor; relationships: KXNHLSPREAD-26NOV08PITANA-PIT2|no: INTENTIONAL_DIVERSIFIER (phi -0.198); KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: PIT offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes; why: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (8.97 vs 5.15 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.002); relationships: KXNHLSPREAD-26NOV08PITANA-PIT2|no: MOSTLY_INDEPENDENT (phi 0.095); KXNHLGOAL-26NOV08PITANA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes; why: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.51 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV08PITANA-PIT2|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26NOV08PITANA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.5806): highest fidelity KXNHLTEAMTOTAL-26NOV08PITANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA2|yes — Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.51 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis ANA:WINS_BY_2PLUS (p 0.4122): highest fidelity KXNHLSPREAD-26NOV08PITANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA2|yes (same contract)
- thesis ANA:WINS (p 0.6167): highest fidelity KXNHLSPREAD-26NOV08PITANA-PIT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV08PITANA-PIT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:WINS_BY_2PLUS (p 0.2031, phi -1.0)
- KXNHLGOAL-26NOV08PITANA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3801, phi -0.201)
- KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2315, phi -0.143)
- KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2315, phi -0.236)
- override: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.51 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +6.62 (adj +2.21) on $42.61, P(profit) 0.5151, adj growth 16.2 bp · B EV +4.62 (adj +2.16) on $34.64, P(profit) 0.5384, adj growth 19.1 bp · C EV +4.84 (adj +2.30) on $21.19, P(profit) 0.6151, adj growth 20.0 bp · R EV +0.66 (adj +0.28) on $7.00, P(profit) 0.3528, adj growth 9.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
