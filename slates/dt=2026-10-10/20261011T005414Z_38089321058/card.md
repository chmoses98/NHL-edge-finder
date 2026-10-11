# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-11T00:54:14Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +23.56 | +6.95 | +11.37 | 0.651 | -43.51 | -49.08 | 55.40 |
| B thesis-diversified (joint) ← optimiser card | 91.54 | +19.82 | +9.80 | +13.66 | 0.534 | -39.88 | -53.49 | 85.12 |
| C best expression per thesis | 66.61 | +14.75 | +5.01 | +13.07 | 0.629 | -27.01 | -42.52 | 44.16 |
| R FUNDED research stakes | 8.00 | +1.58 | +1.06 | -0.91 | 0.195 | -8.00 | -8.00 | 0.00 |

## ANA @ CGY  ·  10000 joint draws  ·  462 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.477 / away 0.523

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_ANA_win | p_overtime | goals | shots CGY/ANA | CGY/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.50 | 0.50 | 0.00 | 6.02 | 28.5/29.0 | 25.5/25.0 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.107 | 0.43 | 0.57 | 0.00 | 6.01 | 23.0/35.0 | 31.0/19.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.50 | 0.50 | 0.46 | 5.97 | 28.6/29.2 | 25.9/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.52 | 0.48 | 0.00 | 9.45 | 30.0/30.6 | 24.4/23.4 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.47 | 0.53 | 0.49 | 5.92 | 22.7/34.6 | 31.2/19.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.079 | 0.43 | 0.57 | 0.00 | 9.42 | 24.4/36.2 | 29.0/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aydar Suniev: 1+ goals YES | 13 | 0.195 | 0.176 | +0.057 | +0.039 | $10.03 | FUNDED_RESEARCH | $3 | CGY:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| A.J. Greer: 1+ goals YES | 16 | 0.224 | 0.206 | +0.055 | +0.036 | $10.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 10 | 0.131 | 0.121 | +0.025 | +0.015 | $3.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Leo Carlsson: 2+ assists NO | 85 | 0.914 | 0.874 | +0.055 | +0.015 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | ANA:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10ANACGY-CGYYSHARANGOVICH17-1|yes; why: higher confidence-adjusted growth (26.62 vs 3.06 bp); despite a smaller raw edge (+0.057 vs +0.087/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-2|no: MOSTLY_INDEPENDENT (phi -0.007); failure: CGY offense suppressed (<= 2 goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10ANACGY-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (19.94 vs 3.26 bp); despite a smaller raw edge (+0.055 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-2|no: INTENTIONAL_DIVERSIFIER (phi -0.09); failure: ANA offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes has the higher standalone adjusted growth (19.94 vs 4.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-2|no: MOSTLY_INDEPENDENT (phi -0.006); failure: ANA offense suppressed (<= 2 goals)
- **Leo Carlsson: 2+ assists NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-1|no; why: higher confidence-adjusted growth (4.34 vs 1.12 bp); despite a smaller raw edge (+0.055 vs +0.083/contract); relationships: KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: ANA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4242): highest fidelity KXNHLAST-26OCT10ANACGY-ANAAKILLORN17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.4082): highest fidelity KXNHLAST-26OCT10ANACGY-CGYYSHARANGOVICH17-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT10ANACGY-CGYYSHARANGOVICH17-1|yes (same contract)
- thesis ANA:SUPPRESSED (p 0.3599): highest fidelity KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-1|no (same contract)
- KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.3745, phi -0.184)
- KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3599, phi -0.21)
- KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3599, phi -0.164)
- KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.4242, phi -0.221)

portfolios: A EV +14.46 (adj +5.05) on $50.00, P(profit) 0.6197, adj growth 38.5 bp · B EV +9.62 (adj +5.86) on $43.96, P(profit) 0.4505, adj growth 50.6 bp · C EV +6.24 (adj +2.67) on $22.97, P(profit) 0.3872, adj growth 23.0 bp · R EV +1.25 (adj +0.84) on $3.00, P(profit) 0.1953, adj growth 27.8 bp

## LAK @ VGK  ·  10000 joint draws  ·  502 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.602 / away 0.398

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_LAK_win | p_overtime | goals | shots VGK/LAK | VGK/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.64 | 0.36 | 0.00 | 6.0 | 27.3/27.1 | 24.2/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.46 | 5.92 | 27.6/27.5 | 24.1/24.3 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.093 | 0.72 | 0.28 | 0.00 | 5.94 | 32.2/21.4 | 19.0/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.63 | 0.37 | 0.00 | 9.14 | 29.2/28.7 | 23.4/22.6 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.55 | 0.45 | 0.46 | 5.84 | 32.5/21.7 | 18.6/29.0 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.51 | 0.49 | 0.47 | 2.78 | 26.0/25.9 | 24.5/24.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.081 | 0.072 | +0.027 | +0.018 | $4.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 48 | 0.647 | 0.535 | +0.150 | +0.038 | $19.75 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Mitch Marner: 1+ goals NO | 69 | 0.752 | 0.736 | +0.047 | +0.030 | $20.00 | FUNDED_RESEARCH | $5 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Trevor Moore: 1+ assists YES | 24 | 0.308 | 0.264 | +0.055 | +0.011 | $3.73 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10LAVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (14.09 vs 0.82 bp); despite a smaller raw edge (+0.027 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10LAVGK-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (12.53 vs 12.51 bp); relationships: KXNHLGOAL-26OCT10LAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.04); failure: LAK offense succeeds (4+ goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10LAVGK-VGKMMARNER93-2|no; why: KXNHLAST-26OCT10LAVGK-VGKMMARNER93-2|no has the higher standalone adjusted growth (12.07 vs 9.86 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.002); relationships: KXNHLGOAL-26OCT10LAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VGK offense succeeds (4+ goals)
- **Trevor Moore: 1+ assists YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10LAVGK-LAEHAULA56-1|yes; why: higher confidence-adjusted growth (1.41 vs 1.26 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10LAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.04); KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4941): highest fidelity KXNHLAST-26OCT10LAVGK-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3638): highest fidelity KXNHLAST-26OCT10LAVGK-VGKMMARNER93-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.2884): highest fidelity KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes (same contract)
- KXNHLGOAL-26OCT10LAVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3638, phi -0.133)
- KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.2 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2884, phi -0.26)
- KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.411, phi -0.207)
- KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4941, phi -0.286)

portfolios: A EV +9.10 (adj +1.90) on $50.00, P(profit) 0.7332, adj growth 16.9 bp · B EV +10.20 (adj +3.94) on $47.58, P(profit) 0.567, adj growth 34.5 bp · C EV +8.51 (adj +2.34) on $43.64, P(profit) 0.6019, adj growth 21.1 bp · R EV +0.34 (adj +0.22) on $5.00, P(profit) 0.7523, adj growth 7.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
