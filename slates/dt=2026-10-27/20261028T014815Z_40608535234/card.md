# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-28T01:48:15Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +36.46 | +9.72 | +25.35 | 0.691 | -43.60 | -58.68 | 76.11 |
| B thesis-diversified (joint) ← optimiser card | 124.81 | +26.84 | +13.47 | +25.35 | 0.604 | -38.73 | -66.13 | 116.48 |
| C best expression per thesis | 123.21 | +28.31 | +11.70 | +24.36 | 0.652 | -41.04 | -51.08 | 101.52 |
| R FUNDED research stakes | 10.00 | +2.54 | +1.74 | -2.02 | 0.324 | -10.00 | -10.00 | 0.00 |

## OTT @ VGK  ·  10000 joint draws  ·  468 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.591 / away 0.409

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_OTT_win | p_overtime | goals | shots VGK/OTT | VGK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.01 | 26.8/26.7 | 23.8/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.47 | 5.91 | 26.8/26.6 | 23.3/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.61 | 0.39 | 0.00 | 9.29 | 28.1/28.1 | 22.4/21.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.080 | 0.68 | 0.32 | 0.00 | 5.99 | 31.3/21.2 | 18.6/26.7 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.55 | 0.45 | 0.47 | 5.89 | 31.6/21.3 | 18.2/28.3 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.060 | 0.56 | 0.44 | 0.00 | 6.06 | 21.2/31.2 | 27.7/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ assists NO | 46 | 0.611 | 0.509 | +0.133 | +0.032 | $16.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.085 | 0.077 | +0.021 | +0.013 | $3.35 | FUNDED_RESEARCH | $1 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 58 | 0.712 | 0.623 | +0.114 | +0.026 | $18.32 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Michael Amadio: 1+ goals YES | 13 | 0.161 | 0.152 | +0.023 | +0.014 | $4.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27OTTVGK-VGKMSTONE61-1|no; why: higher confidence-adjusted growth (9.01 vs 2.02 bp); relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: VGK offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (6.42 vs 1.61 bp); relationships: KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.048); KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: VGK offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27OTTVGK-OTTTSTUTZLE18-2|no; why: higher confidence-adjusted growth (6.03 vs 3.30 bp); relationships: KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.076); failure: OTT offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27OTTVGK-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (3.50 vs 0.62 bp); alternative not eligible: confidence-adjusted EV +0.0062 below the 0.010/contract floor; relationships: KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.076); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.3344): highest fidelity KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4484): highest fidelity KXNHLAST-26OCT27OTTVGK-OTTTSTUTZLE18-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:NET_LOW_VOLUME (p 0.4375): highest fidelity KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no (same contract)
- KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.6 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4477, phi -0.273)
- KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3344, phi -0.121)
- KXNHLAST-26OCT27OTTVGK-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3355, phi -0.245)
- KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4484, phi -0.214)

portfolios: A EV +9.85 (adj +2.16) on $50.00, P(profit) 0.7366, adj growth 19.7 bp · B EV +9.78 (adj +2.99) on $41.92, P(profit) 0.5578, adj growth 26.1 bp · C EV +11.40 (adj +2.55) on $50.00, P(profit) 0.8258, adj growth 22.7 bp · R EV +0.33 (adj +0.21) on $1.00, P(profit) 0.0848, adj growth 6.9 bp

## VAN @ ANA  ·  10000 joint draws  ·  458 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_VAN_win | p_overtime | goals | shots ANA/VAN | ANA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.151 | 0.69 | 0.31 | 0.00 | 6.09 | 34.1/21.3 | 18.6/29.4 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.131 | 0.70 | 0.30 | 0.00 | 9.54 | 35.8/22.6 | 17.9/27.3 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.55 | 0.45 | 0.47 | 5.99 | 34.3/21.6 | 18.4/30.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.095 | 0.63 | 0.37 | 0.00 | 6.02 | 27.7/26.7 | 23.5/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.60 | 0.40 | 0.00 | 9.54 | 29.8/28.7 | 23.1/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.53 | 0.47 | 0.45 | 6.03 | 27.9/27.1 | 23.8/24.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 17 | 0.262 | 0.238 | +0.082 | +0.058 | $15.87 | FUNDED_RESEARCH | $4 | ANA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ goals YES | 19 | 0.237 | 0.224 | +0.036 | +0.023 | $6.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 17 | 0.212 | 0.200 | +0.032 | +0.020 | $5.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 13 | 0.165 | 0.155 | +0.027 | +0.017 | $4.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27VANANA-ANATWASHE42-1|yes; why: higher confidence-adjusted growth (48.01 vs 5.54 bp); despite a smaller raw edge (+0.082 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT27VANANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: ANA offense suppressed (<= 2 goals)
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANMSASSON63-1|yes; why: higher confidence-adjusted growth (7.14 vs 2.50 bp); relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27VANANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (7.14 vs 5.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27VANANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (48.01 vs 5.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.15, ANA shot control · high event (8+) · decided (2+) 0.13, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.12.
- thesis ANA:OFFENSE_4PLUS (p 0.5226): highest fidelity KXNHLPTS-26OCT27VANANA-ANATWASHE42-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.3681): highest fidelity KXNHLSPREAD-26OCT27VANANA-ANA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4045): highest fidelity KXNHLSPREAD-26OCT27VANANA-ANA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27VANANA-ANA2|no (same contract)
- KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2763, phi -0.218)
- KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4158, phi -0.247)
- KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4158, phi -0.215)
- KXNHLGOAL-26OCT27VANANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2763, phi -0.155)

portfolios: A EV +16.22 (adj +5.95) on $50.00, P(profit) 0.4942, adj growth 43.8 bp · B EV +10.37 (adj +7.09) on $33.01, P(profit) 0.5311, adj growth 60.8 bp · C EV +9.64 (adj +6.31) on $34.64, P(profit) 0.4018, adj growth 54.1 bp · R EV +1.82 (adj +1.28) on $4.00, P(profit) 0.2618, adj growth 43.8 bp

## BUF @ SJS  ·  10000 joint draws  ·  534 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.426 / away 0.574

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_BUF_win | p_overtime | goals | shots SJS/BUF | SJS/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.55 | 0.45 | 0.00 | 6.05 | 27.8/28.1 | 24.6/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.45 | 5.94 | 27.7/28.1 | 24.8/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.55 | 0.45 | 0.00 | 9.35 | 29.4/29.8 | 24.1/23.0 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.076 | 0.48 | 0.52 | 0.00 | 6.0 | 22.0/32.8 | 28.8/18.8 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.47 | 0.53 | 0.46 | 5.98 | 22.2/33.0 | 29.5/18.9 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.060 | 0.44 | 0.56 | 0.00 | 9.38 | 23.6/34.6 | 28.0/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Gaudette: 1+ goals YES | 13 | 0.175 | 0.162 | +0.037 | +0.024 | $6.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 61 | 0.676 | 0.658 | +0.049 | +0.031 | $20.00 | FUNDED_RESEARCH | $5 | BUF:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 22 | 0.270 | 0.256 | +0.037 | +0.024 | $8.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 63 | 0.734 | 0.663 | +0.088 | +0.017 | $15.18 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (10.73 vs 6.93 bp); despite a smaller raw edge (+0.037 vs +0.037/contract); relationships: KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: SJS offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF3|no; why: higher confidence-adjusted growth (9.20 vs 6.11 bp); despite a smaller raw edge (+0.049 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.008 vs 0.776); relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: BUF offense succeeds (4+ goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes has the higher standalone adjusted growth (10.73 vs 6.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.085); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT27BUFSJ-SJISTENBERG41-1|no; why: Player prop expression KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no selected over player prop KXNHLPTS-26OCT27BUFSJ-SJISTENBERG41-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.86 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.085); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4384): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS_BY_2PLUS (p 0.3061): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3869): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3465, phi -0.197)
- KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.398, phi -0.24)
- KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3465, phi -0.221)
- KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.9 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4384, phi -0.229)
- override: Player prop expression KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no selected over player prop KXNHLPTS-26OCT27BUFSJ-SJISTENBERG41-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.86 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +10.39 (adj +1.61) on $50.00, P(profit) 0.6477, adj growth 12.7 bp · B EV +6.69 (adj +3.39) on $49.88, P(profit) 0.6759, adj growth 29.6 bp · C EV +7.28 (adj +2.84) on $38.57, P(profit) 0.6091, adj growth 24.7 bp · R EV +0.39 (adj +0.25) on $5.00, P(profit) 0.6756, adj growth 8.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
