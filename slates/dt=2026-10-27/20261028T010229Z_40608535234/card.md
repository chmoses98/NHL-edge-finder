# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-28T01:02:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +34.43 | +7.16 | +28.21 | 0.660 | -43.68 | -61.72 | 50.03 |
| B thesis-diversified (joint) ← optimiser card | 109.12 | +22.67 | +9.07 | +17.24 | 0.670 | -38.55 | -53.02 | 78.56 |
| C best expression per thesis | 109.93 | +18.82 | +6.44 | +18.40 | 0.655 | -34.81 | -45.81 | 56.32 |
| R FUNDED research stakes | 7.00 | +1.58 | +1.03 | +0.98 | 0.714 | -7.00 | -7.00 | 0.00 |

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
| Mitch Marner: 1+ assists NO | 46 | 0.608 | 0.509 | +0.131 | +0.031 | $16.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.085 | 0.078 | +0.021 | +0.014 | $3.41 | FUNDED_RESEARCH | $1 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Jonas Johansson: 28+ saves NO | 61 | 0.773 | 0.647 | +0.146 | +0.020 | $18.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:NET_LOW_VOLUME | STRUCTURAL (1.00) | CALIBRATION_WARNING | D |
| Michael Amadio: 1+ goals YES | 13 | 0.161 | 0.152 | +0.023 | +0.014 | $3.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT27OTTVGK-5|no; why: higher confidence-adjusted growth (8.53 vs 0.88 bp); wins across more scripts (relative breadth 1.009 vs 0.388); alternative not eligible: confidence-adjusted EV +0.0077 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no: MOSTLY_INDEPENDENT (phi -0.046); KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: VGK offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27OTTVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (6.70 vs 1.61 bp); relationships: KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.048); KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: VGK offense suppressed (<= 2 goals)
- **Jonas Johansson: 28+ saves NO** — thesis: OTT net faces light volume (<= 25 shots; VGK suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.046); KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: OTT net faces heavy volume (33+ shots; VGK pressure)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHL2PSPREAD-26OCT27OTTVGK-OTT2|yes; why: higher confidence-adjusted growth (3.50 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no: MOSTLY_INDEPENDENT (phi -0.022); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.3344): highest fidelity KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no (same contract)
- thesis OTT:NET_LOW_VOLUME (p 0.4375): highest fidelity KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3355): highest fidelity KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes (same contract)
- KXNHLAST-26OCT27OTTVGK-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.3 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4477, phi -0.276)
- KXNHLGOAL-26OCT27OTTVGK-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3344, phi -0.121)
- KXNHLSAVE-26OCT27OTTVGK-OTTJJOHANSSON31-28|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.8 pts; fragile player expression; opposing: failure thesis OTT:NET_HIGH_VOLUME (p 0.1648, phi -0.694)
- KXNHLGOAL-26OCT27OTTVGK-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4484, phi -0.214)

portfolios: A EV +9.29 (adj +1.91) on $50.00, P(profit) 0.7356, adj growth 17.2 bp · B EV +10.47 (adj +2.77) on $41.69, P(profit) 0.5792, adj growth 24.2 bp · C EV +9.62 (adj +2.22) on $41.83, P(profit) 0.6354, adj growth 19.4 bp · R EV +0.33 (adj +0.21) on $1.00, P(profit) 0.0852, adj growth 7.1 bp

## VAN @ ANA  ·  10000 joint draws  ·  458 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_VAN_win | p_overtime | goals | shots ANA/VAN | ANA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.152 | 0.68 | 0.32 | 0.00 | 6.07 | 34.4/21.6 | 18.9/29.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.137 | 0.71 | 0.29 | 0.00 | 9.36 | 36.0/22.6 | 18.1/27.7 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.55 | 0.45 | 0.45 | 5.97 | 34.1/21.5 | 18.3/30.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.096 | 0.64 | 0.36 | 0.00 | 6.08 | 28.0/27.3 | 24.2/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.59 | 0.41 | 0.00 | 9.49 | 29.6/28.6 | 22.8/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.50 | 0.50 | 0.44 | 6.01 | 28.0/27.1 | 23.7/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 2+ goals YES | 2 | 0.040 | 0.034 | +0.018 | +0.012 | $2.11 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.07) | EVIDENCE_STRONGER | D |
| A.J. Greer: 1+ goals YES | 17 | 0.269 | 0.202 | +0.089 | +0.022 | $3.27 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ goals YES | 19 | 0.234 | 0.222 | +0.034 | +0.021 | $6.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 17 | 0.212 | 0.200 | +0.032 | +0.020 | $5.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 2+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (14.34 vs 6.86 bp); despite a smaller raw edge (+0.018 vs +0.089/contract); relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes: DUPLICATIVE (phi 0.334); KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: VAN wins (incl. OT/SO)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT27VANANA-ANATWASHE42-1|yes; why: higher confidence-adjusted growth (6.86 vs 2.65 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-2|yes: DUPLICATIVE (phi 0.334); KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: ANA offense suppressed (<= 2 goals)
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (6.11 vs 5.91 bp); relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (6.11 vs 5.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT27VANANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.15, ANA shot control · high event (8+) · decided (2+) 0.14, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.12.
- thesis ANA:OFFENSE_4PLUS (p 0.5242): highest fidelity KXNHLAST-26OCT27VANANA-ANABSENNECKE45-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.3715): highest fidelity KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes (same contract)
- thesis ANA:SUPPRESSED (p 0.2756): highest fidelity KXNHLGOAL-26OCT27VANANA-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT27VANANA-ANACGAUTHIER61-1|no (same contract)
- KXNHLGOAL-26OCT27VANANA-ANAAGREER18-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 93% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:WINS (p 0.3959, phi -0.122)
- KXNHLGOAL-26OCT27VANANA-ANAAGREER18-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 64% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.4 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2756, phi -0.214)
- KXNHLGOAL-26OCT27VANANA-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.416, phi -0.232)
- KXNHLGOAL-26OCT27VANANA-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.416, phi -0.208)

portfolios: A EV +15.11 (adj +3.82) on $50.00, P(profit) 0.4911, adj growth 22.0 bp · B EV +5.52 (adj +2.91) on $17.55, P(profit) 0.5601, adj growth 24.8 bp · C EV +3.91 (adj +1.43) on $18.52, P(profit) 0.4404, adj growth 12.4 bp · R EV +0.85 (adj +0.57) on $1.00, P(profit) 0.0396, adj growth 16.6 bp

## BUF @ SJS  ·  10000 joint draws  ·  534 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.428 / away 0.572

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
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no; why: higher confidence-adjusted growth (10.73 vs 8.50 bp); despite a smaller raw edge (+0.037 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: SJS offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no; why: higher confidence-adjusted growth (9.20 vs 8.50 bp); despite a smaller raw edge (+0.049 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: BUF offense succeeds (4+ goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes has the higher standalone adjusted growth (10.73 vs 6.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.085); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT27BUFSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (2.76 vs 1.58 bp); despite a smaller raw edge (+0.088 vs +0.135/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.085); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4384): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF3|no (same contract)
- thesis SJS:WINS_BY_2PLUS (p 0.3061): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3869): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT27BUFSJ-SJAGAUDETTE81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3465, phi -0.197)
- KXNHLGOAL-26OCT27BUFSJ-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.398, phi -0.24)
- KXNHLGOAL-26OCT27BUFSJ-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3465, phi -0.221)
- KXNHLAST-26OCT27BUFSJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.9 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4384, phi -0.229)

portfolios: A EV +10.03 (adj +1.43) on $50.00, P(profit) 0.6477, adj growth 10.9 bp · B EV +6.69 (adj +3.39) on $49.88, P(profit) 0.6759, adj growth 29.6 bp · C EV +5.29 (adj +2.79) on $49.58, P(profit) 0.6475, adj growth 24.5 bp · R EV +0.39 (adj +0.25) on $5.00, P(profit) 0.6756, adj growth 8.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
