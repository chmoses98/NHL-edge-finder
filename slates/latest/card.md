# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-10T23:12:09Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +38.48 | +12.76 | +34.22 | 0.692 | -47.85 | -72.00 | 104.67 |
| B thesis-diversified (joint) ← optimiser card | 127.62 | +28.41 | +13.26 | +19.40 | 0.658 | -41.87 | -57.31 | 116.05 |
| C best expression per thesis | 115.52 | +18.50 | +7.90 | +15.51 | 0.644 | -29.23 | -46.50 | 71.19 |
| R FUNDED research stakes | 15.00 | +1.08 | +0.54 | +1.60 | 0.573 | -5.49 | -7.91 | 0.00 |

## TBL @ NYI  ·  10000 joint draws  ·  404 bet sides mapped, 24 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.386 / away 0.614

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_TBL_win | p_overtime | goals | shots NYI/TBL | NYI/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.54 | 0.46 | 0.00 | 5.98 | 26.6/26.8 | 23.5/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.52 | 0.48 | 0.49 | 5.89 | 26.9/27.1 | 23.8/23.5 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.073 | 0.46 | 0.54 | 0.00 | 5.93 | 21.5/32.1 | 28.4/18.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.47 | 0.53 | 0.48 | 5.89 | 21.6/32.3 | 28.9/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.52 | 0.48 | 0.00 | 9.21 | 28.2/28.3 | 22.4/22.0 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.067 | 0.49 | 0.51 | 0.48 | 2.84 | 25.5/25.6 | 24.1/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| John Carlson: 1+ assists NO | 53 | 0.732 | 0.597 | +0.184 | +0.050 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 75 | 0.844 | 0.795 | +0.081 | +0.032 | $20.00 | FUNDED_RESEARCH | $5 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jake Guentzel: 1+ goals NO | 66 | 0.701 | 0.689 | +0.025 | +0.014 | $5.11 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10TBNYI-TB3|no; why: higher confidence-adjusted growth (22.11 vs 12.16 bp); relationships: KXNHLSPREAD-26OCT10TBNYI-TB3|no: REINFORCING (phi 0.16); KXNHLGOAL-26OCT10TBNYI-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi 0.119); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10TBNYI-NYI2|yes; why: higher confidence-adjusted growth (12.16 vs 9.78 bp); wins across more scripts (relative breadth 0.998 vs 0.524); relationships: KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: REINFORCING (phi 0.16); KXNHLGOAL-26OCT10TBNYI-TBJGUENTZEL59-1|no: REINFORCING (phi 0.156); failure: TBL wins by 2+
- **Jake Guentzel: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no; why: Player prop expression KXNHLGOAL-26OCT10TBNYI-TBJGUENTZEL59-1|no selected over player prop KXNHLPTS-26OCT10TBNYI-TBJCARLSON74-2|no because adjusted EV is 0.0 pts higher while thesis capture is 0.83 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.119); KXNHLSPREAD-26OCT10TBNYI-TB3|no: REINFORCING (phi 0.156); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.07.
- thesis TBL:SUPPRESSED (p 0.4433): highest fidelity KXNHLSPREAD-26OCT10TBNYI-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no — Player prop expression KXNHLGOAL-26OCT10TBNYI-TBJGUENTZEL59-1|no selected over player prop KXNHLPTS-26OCT10TBNYI-TBJCARLSON74-2|no because adjusted EV is 0.0 pts higher while thesis capture is 0.83 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)
- thesis NYI:OFFENSE_4PLUS (p 0.3538): highest fidelity KXNHLTEAMTOTAL-26OCT10TBNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10TBNYI-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.5099): highest fidelity KXNHLSPREAD-26OCT10TBNYI-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10TBNYI-TB3|no (same contract)
- KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.7 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3301, phi -0.23)
- KXNHLSPREAD-26OCT10TBNYI-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.264, phi -0.717)
- KXNHLGOAL-26OCT10TBNYI-TBJGUENTZEL59-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3301, phi -0.237)
- override: Player prop expression KXNHLGOAL-26OCT10TBNYI-TBJGUENTZEL59-1|no selected over player prop KXNHLPTS-26OCT10TBNYI-TBJCARLSON74-2|no because adjusted EV is 0.0 pts higher while thesis capture is 0.83 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +14.84 (adj +2.89) on $50.00, P(profit) 0.7273, adj growth 23.7 bp · B EV +9.06 (adj +2.76) on $45.11, P(profit) 0.6436, adj growth 25.3 bp · C EV +9.39 (adj +2.95) on $44.19, P(profit) 0.708, adj growth 27.1 bp · R EV +0.61 (adj +0.25) on $7.00, P(profit) 0.6176, adj growth 9.2 bp

## ANA @ CGY  ·  10000 joint draws  ·  462 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.479 / away 0.521

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
| Aydar Suniev: 1+ goals YES | 13 | 0.195 | 0.176 | +0.057 | +0.039 | $9.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| A.J. Greer: 1+ goals YES | 16 | 0.224 | 0.207 | +0.055 | +0.037 | $10.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 9 | 0.131 | 0.120 | +0.035 | +0.024 | $5.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Cutter Gauthier: 1+ goals NO | 59 | 0.634 | 0.622 | +0.027 | +0.015 | $9.37 | FUNDED_RESEARCH | $3 | ANA:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10ANACGY-CGYMFROST16-1|yes; why: higher confidence-adjusted growth (26.62 vs 2.82 bp); relationships: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: CGY offense suppressed (<= 2 goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10ANACGY-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (21.33 vs 7.21 bp); despite a smaller raw edge (+0.055 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: ANA offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes has the higher standalone adjusted growth (21.33 vs 14.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)
- **Cutter Gauthier: 1+ goals NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-1|no; why: Player prop expression KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no selected over player prop KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-2|no because adjusted EV is 0.2 pts higher while thesis capture is 0.82 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4242): highest fidelity KXNHLAST-26OCT10ANACGY-ANAAKILLORN17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.4082): highest fidelity KXNHLGOAL-26OCT10ANACGY-CGYMFROST16-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10ANACGY-CGYMFROST16-1|yes (same contract)
- thesis ANA:SUPPRESSED (p 0.3599): highest fidelity KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no (same contract)
- KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.3745, phi -0.184)
- KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3599, phi -0.21)
- KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3599, phi -0.164)
- KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.4242, phi -0.28)
- override: Player prop expression KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no selected over player prop KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-2|no because adjusted EV is 0.2 pts higher while thesis capture is 0.82 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +14.59 (adj +7.44) on $50.00, P(profit) 0.547, adj growth 60.5 bp · B EV +10.06 (adj +6.75) on $35.51, P(profit) 0.4573, adj growth 57.9 bp · C EV +4.35 (adj +2.86) on $25.65, P(profit) 0.374, adj growth 24.7 bp · R EV +0.13 (adj +0.07) on $3.00, P(profit) 0.6342, adj growth 2.5 bp

## LAK @ VGK  ·  10000 joint draws  ·  502 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.598 / away 0.402

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
| Brayden McNabb: 1+ goals YES | 5 | 0.081 | 0.072 | +0.027 | +0.018 | $4.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 69 | 0.752 | 0.736 | +0.047 | +0.030 | $20.00 | FUNDED_RESEARCH | $5 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 50 | 0.647 | 0.548 | +0.130 | +0.031 | $17.03 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Trevor Moore: 1+ assists YES | 23 | 0.308 | 0.261 | +0.065 | +0.019 | $5.86 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10LAVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (14.09 vs 0.82 bp); despite a smaller raw edge (+0.027 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10LAVGK-VGKMMARNER93-2|no; why: higher confidence-adjusted growth (9.86 vs 3.19 bp); despite a smaller raw edge (+0.047 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10LAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VGK offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10LAVGK-LAAPANARIN10-2|no; why: KXNHLAST-26OCT10LAVGK-LAAPANARIN10-2|no has the higher standalone adjusted growth (19.15 vs 8.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.372); relationships: KXNHLGOAL-26OCT10LAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.04); failure: LAK offense succeeds (4+ goals)
- **Trevor Moore: 1+ assists YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10LAVGK-LAEHAULA56-1|yes; why: higher confidence-adjusted growth (4.23 vs 1.26 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10LAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.04); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4941): highest fidelity KXNHLAST-26OCT10LAVGK-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT10LAVGK-LAAPANARIN10-2|no (same contract)
- thesis VGK:SUPPRESSED (p 0.3638): highest fidelity KXNHLAST-26OCT10LAVGK-VGKMMARNER93-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.2884): highest fidelity KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes (same contract)
- KXNHLGOAL-26OCT10LAVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3638, phi -0.133)
- KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.411, phi -0.207)
- KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.2 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2884, phi -0.26)
- KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4941, phi -0.286)

portfolios: A EV +9.06 (adj +2.43) on $50.00, P(profit) 0.6869, adj growth 20.5 bp · B EV +9.29 (adj +3.75) on $47.00, P(profit) 0.6507, adj growth 32.8 bp · C EV +4.77 (adj +2.09) on $45.68, P(profit) 0.7883, adj growth 19.4 bp · R EV +0.34 (adj +0.22) on $5.00, P(profit) 0.7523, adj growth 7.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
