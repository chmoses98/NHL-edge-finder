# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-08T23:23:23Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 144.99 | +22.96 | +7.59 | +4.42 | 0.540 | -57.59 | -73.22 | 48.91 |
| B thesis-diversified (joint) ← optimiser card | 94.90 | +17.31 | +10.69 | +7.21 | 0.603 | -47.97 | -53.23 | 92.21 |
| C best expression per thesis | 53.08 | +12.37 | +6.59 | +0.57 | 0.656 | -29.46 | -53.08 | 56.51 |
| R FUNDED research stakes | 11.00 | +0.80 | +0.49 | +0.70 | 0.689 | -5.89 | -5.89 | 0.00 |

## NJD @ TOR  ·  10000 joint draws  ·  434 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.409 / away 0.591

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NJD_win | p_overtime | goals | shots TOR/NJD | TOR/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.132 | 0.45 | 0.55 | 0.00 | 6.04 | 22.9/35.6 | 31.7/19.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.50 | 0.50 | 0.48 | 5.91 | 23.3/35.9 | 32.6/20.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.54 | 0.46 | 0.00 | 5.99 | 29.0/29.7 | 26.4/25.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.52 | 0.48 | 0.47 | 5.95 | 29.2/30.1 | 26.8/25.8 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.084 | 0.44 | 0.56 | 0.00 | 9.27 | 24.7/37.8 | 31.0/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.53 | 0.47 | 0.00 | 9.27 | 30.5/31.3 | 25.3/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 9 | 0.149 | 0.132 | +0.053 | +0.036 | $8.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals YES | 17 | 0.215 | 0.202 | +0.035 | +0.022 | $6.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 59 | 0.647 | 0.631 | +0.040 | +0.025 | $14.93 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 12 | 0.151 | 0.142 | +0.024 | +0.015 | $4.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (31.67 vs 7.45 bp); relationships: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV08NJTOR-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: TOR offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (31.67 vs 7.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV08NJTOR-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: TOR offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV08NJTOR-TOR2|yes; why: Player prop expression KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no selected over player prop KXNHLAST-26NOV08NJTOR-NJERODRIGUES17-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.80 vs 0.93 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV08NJTOR-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-NJLEVANGELISTA77-1|yes; why: higher confidence-adjusted growth (4.11 vs 0.30 bp); alternative not eligible: confidence-adjusted EV +0.0048 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3902): highest fidelity KXNHLTEAMTOTAL-26NOV08NJTOR-TOR3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3972): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no selected over player prop KXNHLAST-26NOV08NJTOR-NJERODRIGUES17-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.80 vs 0.93 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis TOR:WINS (p 0.5072): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3946, phi -0.201)
- KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3946, phi -0.225)
- KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3788, phi -0.258)
- KXNHLGOAL-26NOV08NJTOR-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3972, phi -0.169)
- override: Player prop expression KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no selected over player prop KXNHLAST-26NOV08NJTOR-NJERODRIGUES17-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.80 vs 0.93 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.15 (adj +1.44) on $50.00, P(profit) 0.6842, adj growth 12.3 bp · B EV +7.78 (adj +5.11) on $34.06, P(profit) 0.4009, adj growth 43.8 bp · C EV +5.99 (adj +3.86) on $24.37, P(profit) 0.3171, adj growth 32.9 bp · R EV +0.26 (adj +0.16) on $4.00, P(profit) 0.6469, adj growth 5.7 bp

## PHI @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.483 / away 0.517

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_PHI_win | p_overtime | goals | shots CGY/PHI | CGY/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.48 | 0.52 | 0.00 | 6.0 | 27.3/27.2 | 23.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.50 | 0.50 | 0.45 | 5.88 | 27.2/27.0 | 23.8/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.48 | 0.52 | 0.00 | 9.25 | 29.0/28.9 | 22.7/23.0 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.074 | 0.57 | 0.43 | 0.00 | 5.99 | 31.8/21.7 | 18.6/27.8 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.50 | 0.50 | 0.50 | 5.91 | 32.3/21.7 | 18.4/29.1 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.063 | 0.42 | 0.58 | 0.00 | 5.97 | 21.7/31.9 | 27.8/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Konecny: 1+ assists NO | 65 | 0.736 | 0.691 | +0.070 | +0.025 | $14.88 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Porter Martone: 1+ goals NO | 77 | 0.813 | 0.800 | +0.031 | +0.018 | $15.12 | FUNDED_RESEARCH | $4 | PHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 9 | 0.114 | 0.107 | +0.018 | +0.011 | $2.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no; why: higher confidence-adjusted growth (6.01 vs 3.96 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: PHI offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no; why: second expression of the same thesis: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no has the higher standalone adjusted growth (6.01 vs 3.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.056); they share one thesis budget; relationships: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: PHI offense succeeds (4+ goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PHICGY-CGYMBACKLUND11-1|yes; why: higher confidence-adjusted growth (2.95 vs 0.08 bp); alternative not eligible: confidence-adjusted EV +0.0024 below the 0.010/contract floor; relationships: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis PHI:SUPPRESSED (p 0.4269): highest fidelity KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.3493): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3556, phi -0.238)
- KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3556, phi -0.187)
- KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4282, phi -0.143)

portfolios: A EV +3.84 (adj +1.76) on $44.99, P(profit) 0.6494, adj growth 14.7 bp · B EV +2.68 (adj +1.20) on $32.72, P(profit) 0.6436, adj growth 10.7 bp · C EV +2.11 (adj +0.74) on $20.00, P(profit) 0.7362, adj growth 6.5 bp · R EV +0.16 (adj +0.09) on $4.00, P(profit) 0.8132, adj growth 3.3 bp

## PIT @ ANA  ·  10000 joint draws  ·  448 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_PIT_win | p_overtime | goals | shots ANA/PIT | ANA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.135 | 0.69 | 0.31 | 0.00 | 9.73 | 29.4/29.2 | 23.9/21.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.70 | 0.30 | 0.00 | 6.09 | 27.4/27.2 | 24.4/22.9 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.096 | 0.77 | 0.23 | 0.00 | 9.58 | 34.3/23.0 | 18.7/25.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.56 | 0.44 | 0.47 | 6.08 | 27.6/27.4 | 24.0/24.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.087 | 0.73 | 0.27 | 0.00 | 6.05 | 32.4/21.5 | 19.0/27.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.58 | 0.42 | 0.47 | 6.01 | 32.6/22.1 | 18.8/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jeff Malott: 1+ goals YES | 11 | 0.156 | 0.143 | +0.039 | +0.027 | $6.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 19 | 0.244 | 0.228 | +0.043 | +0.027 | $8.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Kaedan Korczak: 1+ goals YES | 3 | 0.052 | 0.044 | +0.020 | +0.012 | $2.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 34 | 0.401 | 0.384 | +0.045 | +0.029 | $10.95 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes; why: higher confidence-adjusted growth (14.68 vs 11.70 bp); despite a smaller raw edge (+0.039 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.816 vs 0.322); relationships: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV08PITANA-PITKKORCZAK6-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes; why: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes has the higher standalone adjusted growth (11.70 vs 10.10 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.173); relationships: KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV08PITANA-PITKKORCZAK6-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: ANA offense suppressed (<= 2 goals)
- **Kaedan Korczak: 1+ goals YES** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: PIT offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes; why: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes has the higher standalone adjusted growth (11.70 vs 7.72 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.193); relationships: KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV08PITANA-PITKKORCZAK6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.5882): highest fidelity KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.4031): highest fidelity KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.6384): highest fidelity KXNHLSPREAD-26NOV08PITANA-PIT3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2252, phi -0.134)
- KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2252, phi -0.175)
- KXNHLGOAL-26NOV08PITANA-PITKKORCZAK6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3996, phi -0.096)
- KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2252, phi -0.247)

portfolios: A EV +13.97 (adj +4.39) on $50.00, P(profit) 0.4562, adj growth 22.0 bp · B EV +6.86 (adj +4.38) on $28.12, P(profit) 0.6396, adj growth 37.7 bp · C EV +4.27 (adj +1.99) on $8.71, P(profit) 0.2539, adj growth 17.0 bp · R EV +0.38 (adj +0.24) on $3.00, P(profit) 0.4006, adj growth 8.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
