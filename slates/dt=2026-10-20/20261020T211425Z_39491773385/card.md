# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-20T21:14:25Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +32.37 | +10.71 | +31.38 | 0.804 | -16.00 | -26.88 | 100.05 |
| B thesis-diversified (joint) ← optimiser card | 149.29 | +28.59 | +14.90 | +26.64 | 0.778 | -16.49 | -27.81 | 142.50 |
| C best expression per thesis | 149.99 | +27.34 | +12.96 | +25.66 | 0.765 | -17.96 | -28.95 | 123.16 |
| R FUNDED research stakes | 25.00 | +3.43 | +1.87 | +2.21 | 0.625 | -5.81 | -8.01 | 0.00 |

## SJS @ MTL  ·  10000 joint draws  ·  488 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.663 / away 0.337

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_SJS_win | p_overtime | goals | shots MTL/SJS | MTL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.64 | 0.36 | 0.00 | 5.97 | 27.2/27.2 | 24.3/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.48 | 5.93 | 27.5/27.4 | 24.1/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.67 | 0.33 | 0.00 | 9.21 | 28.9/28.7 | 23.8/22.1 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.079 | 0.70 | 0.30 | 0.00 | 5.99 | 31.8/21.4 | 18.9/27.1 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.065 | 0.59 | 0.41 | 0.00 | 6.01 | 21.8/31.9 | 28.3/18.1 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.58 | 0.42 | 0.47 | 5.92 | 32.0/21.6 | 18.2/28.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mason Marchment: 1+ goals YES | 18 | 0.226 | 0.213 | +0.036 | +0.023 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ goals NO | 55 | 0.606 | 0.591 | +0.039 | +0.024 | $3.54 | FUNDED_RESEARCH | $1 | MTL:SUPPRESSED | DIRECT (0.78) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 72 | 0.797 | 0.754 | +0.063 | +0.020 | $6.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Montreal over 4.5 goals scored NO | 65 | 0.732 | 0.686 | +0.066 | +0.020 | $3.88 | FUNDED_RESEARCH | $1 | MTL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20SJMTL-MTL3|no; why: higher confidence-adjusted growth (7.42 vs 2.79 bp); despite a smaller raw edge (+0.036 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT20SJMTL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no: MOSTLY_INDEPENDENT (phi -0.003); failure: SJS offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no; why: higher confidence-adjusted growth (5.02 vs 3.88 bp); despite a smaller raw edge (+0.039 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.004 vs 0.878); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT20SJMTL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no: REINFORCING (phi 0.218); failure: MTL offense succeeds (4+ goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20SJMTL-4|no; why: higher confidence-adjusted growth (4.32 vs 2.30 bp); wins across more scripts (relative breadth 0.991 vs 0.363); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no: MOSTLY_INDEPENDENT (phi 0.02); failure: SJS offense succeeds (4+ goals)
- **Montreal over 4.5 goals scored NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no has the higher standalone adjusted growth (5.02 vs 3.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.218); they share one thesis budget; relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: REINFORCING (phi 0.218); KXNHLAST-26OCT20SJMTL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:OFFENSE_4PLUS (p 0.3119): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3298): highest fidelity KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.4667): highest fidelity KXNHLAST-26OCT20SJMTL-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20SJMTL-SJMMARCHMENT27-1|no (same contract)
- KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4667, phi -0.25)
- KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4585, phi -0.238)
- KXNHLAST-26OCT20SJMTL-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3119, phi -0.198)
- KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4585, phi -0.658)

portfolios: A EV +1.78 (adj +0.52) on $13.64, P(profit) 0.488, adj growth 4.7 bp · B EV +1.57 (adj +0.69) on $15.81, P(profit) 0.5267, adj growth 6.6 bp · C EV +1.84 (adj +0.81) on $18.58, P(profit) 0.5267, adj growth 7.7 bp · R EV +0.17 (adj +0.07) on $2.00, P(profit) 0.4907, adj growth 2.7 bp

## COL @ NJD  ·  10000 joint draws  ·  466 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.517 / away 0.483

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_COL_win | p_overtime | goals | shots NJD/COL | NJD/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.48 | 0.52 | 0.00 | 6.03 | 28.6/28.8 | 25.0/25.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.48 | 0.52 | 0.48 | 5.89 | 28.9/29.0 | 25.8/25.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.50 | 0.50 | 0.00 | 9.12 | 30.0/30.2 | 24.2/24.2 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.080 | 0.42 | 0.57 | 0.00 | 5.98 | 22.8/33.6 | 29.3/19.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.45 | 0.55 | 0.49 | 5.94 | 23.0/34.1 | 30.7/19.8 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.062 | 0.54 | 0.46 | 0.00 | 5.95 | 33.9/23.3 | 20.1/30.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cody Glass: 1+ goals YES | 11 | 0.150 | 0.139 | +0.033 | +0.022 | $1.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ assists NO | 45 | 0.601 | 0.500 | +0.134 | +0.032 | $4.44 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 64 | 0.704 | 0.687 | +0.048 | +0.030 | $5.78 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ assists NO | 47 | 0.611 | 0.513 | +0.124 | +0.025 | $3.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20COLNJ-NJDMERCER91-1|yes; why: higher confidence-adjusted growth (9.97 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.022); failure: NJD offense suppressed (<= 2 goals)
- **Cale Makar: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-2|no; why: higher confidence-adjusted growth (9.16 vs 2.73 bp); relationships: KXNHLGOAL-26OCT20COLNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: COL offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (9.09 vs 5.65 bp); despite a smaller raw edge (+0.048 vs +0.124/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20COLNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: NJD offense succeeds (4+ goals)
- **Jack Hughes: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no has the higher standalone adjusted growth (9.09 vs 5.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT20COLNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis COL:SUPPRESSED (p 0.3958): highest fidelity KXNHLAST-26OCT20COLNJ-COLCMAKAR8-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4184): highest fidelity KXNHLAST-26OCT20COLNJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:OFFENSE_4PLUS (p 0.361): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT20COLNJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4184, phi -0.17)
- KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.6 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3807, phi -0.28)
- KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.361, phi -0.245)
- KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.1 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.361, phi -0.273)

portfolios: A EV +3.56 (adj +0.68) on $13.64, P(profit) 0.5644, adj growth 6.4 bp · B EV +3.10 (adj +1.08) on $15.57, P(profit) 0.7421, adj growth 10.4 bp · C EV +2.19 (adj +0.74) on $13.18, P(profit) 0.4209, adj growth 7.1 bp · R EV +0.15 (adj +0.09) on $2.00, P(profit) 0.7039, adj growth 3.6 bp

## ANA @ NYI  ·  10000 joint draws  ·  456 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.583 / away 0.417

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_ANA_win | p_overtime | goals | shots NYI/ANA | NYI/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.61 | 0.39 | 0.00 | 6.03 | 27.7/27.7 | 24.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.52 | 0.48 | 0.49 | 5.95 | 27.5/27.7 | 24.5/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.63 | 0.37 | 0.00 | 9.27 | 29.5/29.7 | 24.3/22.5 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.072 | 0.54 | 0.46 | 0.00 | 6.04 | 22.3/33.1 | 29.4/18.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.47 | 0.53 | 0.49 | 5.93 | 22.6/33.3 | 29.9/19.3 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.067 | 0.70 | 0.30 | 0.00 | 6.01 | 32.3/22.1 | 19.5/27.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 13 | 0.212 | 0.190 | +0.074 | +0.052 | $4.29 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 15 | 0.196 | 0.182 | +0.037 | +0.023 | $1.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 10 | 0.129 | 0.120 | +0.023 | +0.014 | $1.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Ilya Sorokin: 23+ saves YES | 50 | 0.624 | 0.540 | +0.106 | +0.022 | $4.16 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYI:NET_HIGH_VOLUME | DIRECT (0.95) | EVIDENCE_MIXED | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT20ANANYI-7|yes; why: higher confidence-adjusted growth (48.73 vs 0.40 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.885 vs 0.681); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLSAVE-26OCT20ANANYI-NYIISOROKIN30-23|yes: MOSTLY_INDEPENDENT (phi -0.031); failure: ANA offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT20ANANYI-7|yes; why: higher confidence-adjusted growth (8.82 vs 0.40 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.882 vs 0.681); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLSAVE-26OCT20ANANYI-NYIISOROKIN30-23|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: NYI offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes has the higher standalone adjusted growth (48.73 vs 4.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLSAVE-26OCT20ANANYI-NYIISOROKIN30-23|yes: MOSTLY_INDEPENDENT (phi -0.047); failure: ANA offense suppressed (<= 2 goals)
- **Ilya Sorokin: 23+ saves YES** — thesis: NYI net faces heavy volume (33+ shots; ANA pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.047); failure: NYI net faces light volume (<= 25 shots; ANA suppressed)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3377): highest fidelity KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.452): highest fidelity KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes (same contract)
- thesis NYI:NET_HIGH_VOLUME (p 0.223): highest fidelity KXNHLSAVE-26OCT20ANANYI-NYIISOROKIN30-23|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT20ANANYI-NYIISOROKIN30-23|yes (same contract)
- KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4388, phi -0.221)
- KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3304, phi -0.192)
- KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4388, phi -0.152)
- KXNHLSAVE-26OCT20ANANYI-NYIISOROKIN30-23|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 5% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.9 pts; fragile player expression; opposing: failure thesis NYI:NET_LOW_VOLUME (p 0.364, phi -0.772)

portfolios: A EV +4.10 (adj +2.01) on $13.64, P(profit) 0.6249, adj growth 19.2 bp · B EV +3.90 (adj +2.27) on $11.72, P(profit) 0.4517, adj growth 21.7 bp · C EV +4.71 (adj +2.50) on $14.57, P(profit) 0.3524, adj growth 23.6 bp · R EV +1.08 (adj +0.76) on $2.00, P(profit) 0.2121, adj growth 27.6 bp

## LAK @ WSH  ·  10000 joint draws  ·  478 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_LAK_win | p_overtime | goals | shots WSH/LAK | WSH/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.64 | 0.36 | 0.00 | 5.95 | 27.3/27.4 | 24.5/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.46 | 5.87 | 27.6/27.7 | 24.6/24.1 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.080 | 0.57 | 0.43 | 0.00 | 6.0 | 21.7/32.6 | 29.1/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.65 | 0.35 | 0.00 | 9.11 | 28.9/29.1 | 24.1/22.3 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.49 | 0.51 | 0.45 | 5.86 | 22.1/32.8 | 29.5/18.8 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.067 | 0.50 | 0.50 | 0.49 | 2.78 | 25.9/26.0 | 24.5/24.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.240 | 0.222 | +0.060 | +0.042 | $3.68 | FUNDED_RESEARCH | $1 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 54 | 0.664 | 0.577 | +0.107 | +0.020 | $3.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Darcy Kuemper: 27+ saves NO | 59 | 0.718 | 0.618 | +0.111 | +0.011 | $2.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:NET_LOW_VOLUME | STRUCTURAL (1.00) | CALIBRATION_WARNING | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (25.13 vs 0.28 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSAVE-26OCT20LAWSH-LADKUEMPER35-27|no: MOSTLY_INDEPENDENT (phi 0.035); failure: WSH offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT20LAWSH-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (3.40 vs 0.39 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSAVE-26OCT20LAWSH-LADKUEMPER35-27|no: MOSTLY_INDEPENDENT (phi 0.025); failure: LAK offense succeeds (4+ goals)
- **Darcy Kuemper: 27+ saves NO** — thesis: LAK net faces light volume (<= 25 shots; WSH suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.035); KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.025); failure: LAK net faces heavy volume (33+ shots; WSH pressure)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis WSH:OFFENSE_4PLUS (p 0.4034): highest fidelity KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes (same contract)
- thesis LAK:SUPPRESSED (p 0.5004): highest fidelity KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no (same contract)
- thesis LAK:NET_LOW_VOLUME (p 0.4466): highest fidelity KXNHLSAVE-26OCT20LAWSH-LADKUEMPER35-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT20LAWSH-LADKUEMPER35-27|no (same contract)
- KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.374, phi -0.233)
- KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2876, phi -0.27)
- KXNHLSAVE-26OCT20LAWSH-LADKUEMPER35-27|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.3 pts; fragile player expression; opposing: failure thesis LAK:NET_HIGH_VOLUME (p 0.1613, phi -0.625)

portfolios: A EV +3.19 (adj +1.24) on $13.64, P(profit) 0.6027, adj growth 11.8 bp · B EV +2.32 (adj +1.02) on $9.44, P(profit) 0.6027, adj growth 9.7 bp · C EV +2.73 (adj +1.20) on $11.09, P(profit) 0.6027, adj growth 11.4 bp · R EV +0.34 (adj +0.23) on $1.00, P(profit) 0.2403, adj growth 8.8 bp

## TOR @ CBJ  ·  10000 joint draws  ·  440 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.583 / away 0.417

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_TOR_win | p_overtime | goals | shots CBJ/TOR | CBJ/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CBJ shot control · normal event (5-7) · decided (2+) | 0.125 | 0.73 | 0.27 | 0.00 | 5.97 | 34.3/22.2 | 19.9/29.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.65 | 0.35 | 0.00 | 5.99 | 28.6/27.8 | 25.1/24.5 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.57 | 0.43 | 0.49 | 5.86 | 34.7/22.6 | 19.5/31.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.54 | 0.46 | 0.48 | 5.88 | 28.9/28.2 | 25.1/25.6 | even strength |
| CBJ shot control · high event (8+) · decided (2+) | 0.075 | 0.72 | 0.28 | 0.00 | 9.1 | 36.7/23.8 | 19.5/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.067 | 0.72 | 0.28 | 0.00 | 9.17 | 30.6/29.7 | 24.8/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 22 | 0.293 | 0.273 | +0.061 | +0.041 | $4.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 18 | 0.233 | 0.217 | +0.042 | +0.027 | $2.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Full Game: Over 6.5 goals scored NO | 50 | 0.580 | 0.537 | +0.063 | +0.020 | $5.03 | FUNDED_RESEARCH | $2 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Matthew Knies: 1+ goals NO | 68 | 0.721 | 0.709 | +0.025 | +0.014 | $2.45 | FUNDED_RESEARCH | $1 | CBJ:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (20.60 vs 9.99 bp); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLTOTAL-26OCT20TORCBJ-7|no: INTENTIONAL_DIVERSIFIER (phi -0.148); KXNHLGOAL-26OCT20TORCBJ-CBJMKNIES23-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (20.60 vs 9.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLTOTAL-26OCT20TORCBJ-7|no: INTENTIONAL_DIVERSIFIER (phi -0.143); KXNHLGOAL-26OCT20TORCBJ-CBJMKNIES23-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense suppressed (<= 2 goals)
- **Full Game: Over 6.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT20TORCBJ-5|no; why: KXNHLTOTAL-26OCT20TORCBJ-5|no has the higher standalone adjusted growth (5.75 vs 3.52 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.486); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.148); KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.143); KXNHLGOAL-26OCT20TORCBJ-CBJMKNIES23-1|no: REINFORCING (phi 0.167); failure: high-event game (8+ goals)
- **Matthew Knies: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20TORCBJ-5|no; why: Player prop expression KXNHLGOAL-26OCT20TORCBJ-CBJMKNIES23-1|no selected over player prop KXNHLAST-26OCT20TORCBJ-CBJAFANTILLI19-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.88 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLTOTAL-26OCT20TORCBJ-7|no: REINFORCING (phi 0.167); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CBJ:OFFENSE_4PLUS (p 0.4406): highest fidelity KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.5139): highest fidelity KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no (same contract)
- thesis GAME:LOW_EVENT (p 0.2698): highest fidelity KXNHLTOTAL-26OCT20TORCBJ-7|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3382, phi -0.24)
- KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3382, phi -0.225)
- KXNHLTOTAL-26OCT20TORCBJ-7|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2288, phi -0.64)
- KXNHLGOAL-26OCT20TORCBJ-CBJMKNIES23-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4406, phi -0.254)
- override: Player prop expression KXNHLGOAL-26OCT20TORCBJ-CBJMKNIES23-1|no selected over player prop KXNHLAST-26OCT20TORCBJ-CBJAFANTILLI19-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.88 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.74 (adj +0.49) on $13.64, P(profit) 0.5726, adj growth 4.6 bp · B EV +2.46 (adj +1.41) on $14.61, P(profit) 0.4278, adj growth 13.5 bp · C EV +2.49 (adj +1.31) on $14.91, P(profit) 0.4893, adj growth 12.5 bp · R EV +0.28 (adj +0.10) on $3.00, P(profit) 0.5801, adj growth 3.5 bp

## WPG @ STL  ·  10000 joint draws  ·  506 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.559 / away 0.441

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_WPG_win | p_overtime | goals | shots STL/WPG | STL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.66 | 0.34 | 0.00 | 6.02 | 26.6/26.5 | 23.7/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.55 | 0.45 | 0.48 | 5.96 | 26.7/26.6 | 23.4/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.68 | 0.32 | 0.00 | 9.19 | 28.3/28.3 | 23.5/21.3 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.076 | 0.73 | 0.27 | 0.00 | 6.02 | 31.4/21.0 | 18.6/26.6 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.062 | 0.58 | 0.42 | 0.00 | 5.96 | 21.2/31.2 | 27.9/17.6 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.57 | 0.43 | 0.48 | 5.88 | 31.2/21.1 | 18.0/27.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 22 | 0.298 | 0.276 | +0.066 | +0.044 | $3.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jake Neighbours: 1+ assists YES | 24 | 0.322 | 0.279 | +0.069 | +0.026 | $2.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Philip Broberg: 1+ assists YES | 33 | 0.411 | 0.368 | +0.066 | +0.023 | $1.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
| Dalibor Dvorsky: 1+ goals NO | 82 | 0.849 | 0.841 | +0.019 | +0.010 | $6.32 | FUNDED_RESEARCH | $2 | STL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20WPGSTL-STLJNEIGHBOURS63-1|yes; why: higher confidence-adjusted growth (23.47 vs 7.67 bp); despite a smaller raw edge (+0.066 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT20WPGSTL-STLJNEIGHBOURS63-1|yes: MOSTLY_INDEPENDENT (phi 0.12); KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.141); KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: STL offense suppressed (<= 2 goals)
- **Jake Neighbours: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (23.47 vs 7.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.120); they share one thesis budget; relationships: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.12); KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.066); KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: INTENTIONAL_DIVERSIFIER (phi -0.148); failure: STL offense suppressed (<= 2 goals)
- **Philip Broberg: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (23.47 vs 5.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.141); they share one thesis budget; relationships: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.141); KXNHLAST-26OCT20WPGSTL-STLJNEIGHBOURS63-1|yes: MOSTLY_INDEPENDENT (phi 0.066); KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: INTENTIONAL_DIVERSIFIER (phi -0.053); failure: STL offense suppressed (<= 2 goals)
- **Dalibor Dvorsky: 1+ goals NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20WPGSTL-STLPBUCHNEVICH89-1|no; why: higher confidence-adjusted growth (1.69 vs 0.17 bp); despite a smaller raw edge (+0.019 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0040 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT20WPGSTL-STLJNEIGHBOURS63-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.148); KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.053); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.458): highest fidelity KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:SUPPRESSED (p 0.3361): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3361, phi -0.242)
- KXNHLAST-26OCT20WPGSTL-STLJNEIGHBOURS63-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3361, phi -0.264)
- KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3361, phi -0.279)
- KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.458, phi -0.163)

portfolios: A EV +3.12 (adj +1.49) on $13.64, P(profit) 0.569, adj growth 14.0 bp · B EV +2.17 (adj +1.14) on $14.13, P(profit) 0.4467, adj growth 11.0 bp · C EV +1.43 (adj +0.95) on $5.01, P(profit) 0.2981, adj growth 9.0 bp · R EV +0.05 (adj +0.03) on $2.00, P(profit) 0.8493, adj growth 0.9 bp

## BOS @ DAL  ·  10000 joint draws  ·  422 bet sides mapped, 11 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.597 / away 0.403

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_BOS_win | p_overtime | goals | shots DAL/BOS | DAL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.51 | 0.49 | 0.00 | 6.06 | 26.6/26.4 | 22.7/23.0 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.109 | 0.59 | 0.41 | 0.00 | 6.02 | 31.5/20.6 | 17.5/27.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.47 | 0.53 | 0.46 | 5.9 | 26.6/26.4 | 23.1/23.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.54 | 0.46 | 0.46 | 5.92 | 31.7/20.7 | 17.5/28.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.48 | 0.52 | 0.00 | 9.22 | 27.9/27.7 | 21.8/22.0 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.065 | 0.60 | 0.40 | 0.00 | 9.31 | 33.6/22.1 | 17.1/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mikko Rantanen: 1+ goals NO | 68 | 0.735 | 0.720 | +0.040 | +0.025 | $6.32 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Boston over 2.5 goals scored YES | 51 | 0.598 | 0.552 | +0.071 | +0.024 | $4.23 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Charlie McAvoy: 1+ assists NO | 59 | 0.654 | 0.617 | +0.048 | +0.010 | $4.03 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20BOSDAL-DALRHINTZ24-1|no; why: higher confidence-adjusted growth (6.52 vs 2.07 bp); despite a smaller raw edge (+0.040 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26OCT20BOSDAL-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: DAL offense succeeds (4+ goals)
- **Boston over 2.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes; why: higher confidence-adjusted growth (5.12 vs 4.62 bp); wins across more scripts (relative breadth 0.872 vs 0.54); relationships: KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26OCT20BOSDAL-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.278); failure: BOS offense suppressed (<= 2 goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20BOSDAL-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (0.97 vs 0.07 bp); alternative not eligible: confidence-adjusted EV +0.0024 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: INTENTIONAL_DIVERSIFIER (phi -0.278); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis DAL:SUPPRESSED (p 0.3957): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.3632): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes (same contract)
- thesis BOS:WINS (p 0.4864): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3916, phi -0.225)
- KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.4135, phi -0.976)
- KXNHLAST-26OCT20BOSDAL-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3632, phi -0.264)
- override: Broad expression KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes selected over broad KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.42 (adj +0.76) on $13.64, P(profit) 0.3739, adj growth 6.6 bp · B EV +1.25 (adj +0.49) on $14.58, P(profit) 0.765, adj growth 4.7 bp · C EV +1.75 (adj +0.64) on $18.58, P(profit) 0.5757, adj growth 6.2 bp · R EV +0.38 (adj +0.16) on $4.00, P(profit) 0.4451, adj growth 6.1 bp

## MIN @ EDM  ·  10000 joint draws  ·  480 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.551 / away 0.449

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_MIN_win | p_overtime | goals | shots EDM/MIN | EDM/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.64 | 0.36 | 0.00 | 6.06 | 28.3/28.3 | 25.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.116 | 0.65 | 0.35 | 0.00 | 9.45 | 30.2/30.0 | 24.5/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.55 | 0.45 | 0.47 | 5.95 | 28.8/28.5 | 25.2/25.4 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.083 | 0.67 | 0.33 | 0.00 | 5.99 | 33.5/22.5 | 19.8/29.0 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.54 | 0.46 | 0.48 | 5.97 | 34.2/22.9 | 19.7/30.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.066 | 0.70 | 0.30 | 0.00 | 9.6 | 35.8/24.4 | 19.6/27.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 13 | 0.190 | 0.172 | +0.052 | +0.034 | $2.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 32 | 0.410 | 0.362 | +0.074 | +0.027 | $4.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Zach Hyman: 1+ goals YES | 32 | 0.375 | 0.359 | +0.040 | +0.023 | $3.30 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ assists YES | 30 | 0.380 | 0.338 | +0.066 | +0.023 | $2.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (21.29 vs 11.66 bp); despite a smaller raw edge (+0.052 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.055); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20MINEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.052); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (7.18 vs 0.95 bp); despite a smaller raw edge (+0.074 vs +0.084/contract); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.055); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.207); KXNHLAST-26OCT20MINEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.085); failure: EDM offense succeeds (4+ goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes; why: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes has the higher standalone adjusted growth (11.66 vs 5.37 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.125); relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.207); KXNHLAST-26OCT20MINEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.095); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes; why: Player prop expression KXNHLAST-26OCT20MINEDM-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.50 vs 0.42 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.052); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.085); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi 0.095); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4983): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes — Player prop expression KXNHLAST-26OCT20MINEDM-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.50 vs 0.42 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis EDM:SUPPRESSED (p 0.2913): highest fidelity KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no (same contract)
- thesis MIN:SUPPRESSED (p 0.4276): highest fidelity KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no (same contract)
- KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2913, phi -0.178)
- KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 33% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4983, phi -0.328)
- KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2913, phi -0.265)
- KXNHLAST-26OCT20MINEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2913, phi -0.24)
- override: Player prop expression KXNHLAST-26OCT20MINEDM-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.50 vs 0.42 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.19 (adj +1.14) on $13.64, P(profit) 0.5369, adj growth 10.8 bp · B EV +2.86 (adj +1.45) on $12.56, P(profit) 0.4413, adj growth 13.9 bp · C EV +2.27 (adj +0.92) on $11.83, P(profit) 0.4975, adj growth 8.7 bp · R EV +0.12 (adj +0.07) on $1.00, P(profit) 0.3749, adj growth 2.6 bp

## DET @ SEA  ·  10000 joint draws  ·  450 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.487 / away 0.513

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_DET_win | p_overtime | goals | shots SEA/DET | SEA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.02 | 27.8/28.1 | 25.1/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.48 | 5.92 | 27.9/28.3 | 25.0/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.64 | 0.36 | 0.00 | 9.26 | 29.6/29.9 | 24.5/22.6 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 6.04 | 22.4/33.7 | 30.3/18.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.50 | 0.50 | 0.47 | 5.87 | 22.2/33.6 | 30.3/19.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.56 | 0.44 | 0.00 | 3.45 | 26.8/27.1 | 25.3/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Freddy Gaudreau: 1+ goals YES | 8 | 0.142 | 0.118 | +0.057 | +0.033 | $2.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 11 | 0.153 | 0.141 | +0.036 | +0.024 | $1.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Dylan Larkin: 1+ goals NO | 68 | 0.741 | 0.725 | +0.046 | +0.030 | $6.32 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $1.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes; why: higher confidence-adjusted growth (28.94 vs 9.05 bp); despite a smaller raw edge (+0.057 vs +0.113/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes; why: higher confidence-adjusted growth (12.40 vs 9.05 bp); despite a smaller raw edge (+0.037 vs +0.113/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: SEA offense suppressed (<= 2 goals)
- **Dylan Larkin: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20DETSEA-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (9.09 vs 6.02 bp); despite a smaller raw edge (+0.046 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: DET offense succeeds (4+ goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes; why: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes has the higher standalone adjusted growth (9.05 vs 7.37 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.085); relationships: KXNHLGOAL-26OCT20DETSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis DET:SUPPRESSED (p 0.4539): highest fidelity KXNHLTEAMTOTAL-26OCT20DETSEA-DET4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.4437): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [DIRECT], best adjusted EV KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.58): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20DETSEA-DET4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20DETSEA-SEAFGAUDREAU89-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.178)
- KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.164)
- KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3287, phi -0.226)
- KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.182)

portfolios: A EV +3.48 (adj +0.88) on $13.64, P(profit) 0.5286, adj growth 8.2 bp · B EV +2.91 (adj +1.78) on $12.20, P(profit) 0.3959, adj growth 17.0 bp · C EV +2.20 (adj +0.77) on $17.03, P(profit) 0.7482, adj growth 7.4 bp · R EV +0.13 (adj +0.09) on $2.00, P(profit) 0.7414, adj growth 3.3 bp

## CAR @ VAN  ·  10000 joint draws  ·  452 bet sides mapped, 34 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.284 / away 0.716

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CAR_win | p_overtime | goals | shots VAN/CAR | VAN/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.171 | 0.37 | 0.63 | 0.00 | 6.02 | 20.8/34.0 | 29.5/18.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.144 | 0.48 | 0.52 | 0.48 | 5.95 | 21.1/34.6 | 31.1/17.8 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.128 | 0.37 | 0.63 | 0.00 | 9.39 | 22.5/36.1 | 28.6/17.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.082 | 0.42 | 0.58 | 0.00 | 6.04 | 27.0/28.3 | 24.3/23.8 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.073 | 0.41 | 0.59 | 0.00 | 3.47 | 19.8/32.7 | 30.3/18.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.48 | 0.52 | 0.49 | 5.98 | 26.7/28.0 | 24.7/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Filip Chytil: 1+ goals YES | 16 | 0.249 | 0.225 | +0.080 | +0.056 | $4.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 49 | 0.657 | 0.545 | +0.149 | +0.038 | $1.92 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 62 | 0.769 | 0.669 | +0.133 | +0.033 | $3.37 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 62 | 0.685 | 0.668 | +0.049 | +0.031 | $5.66 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20CARVAN-VAN3|yes; why: higher confidence-adjusted growth (47.34 vs 25.58 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.929 vs 0.5); relationships: KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.164); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: MOSTLY_INDEPENDENT (phi 0.134); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VAN offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (47.34 vs 12.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.164); they share one thesis budget; relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: REINFORCING (phi 0.164); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: DUPLICATIVE (phi 0.757); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: REINFORCING (phi 0.187); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (47.34 vs 10.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.134); they share one thesis budget; relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.134); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: DUPLICATIVE (phi 0.757); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: REINFORCING (phi 0.162); failure: CAR wins by 2+
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20CARVAN-VAN3|yes; why: KXNHLSPREAD-26OCT20CARVAN-VAN3|yes has the higher standalone adjusted growth (25.58 vs 9.26 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.135); relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.187); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: REINFORCING (phi 0.162); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3652): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.4391): highest fidelity KXNHLGAME-26OCT20CARVAN-CAR|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2329): highest fidelity KXNHLGAME-26OCT20CARVAN-CAR|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT20CARVAN-CAR|no (same contract)
- KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4186, phi -0.236)
- KXNHLSPREAD-26OCT20CARVAN-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 17.2 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3434, phi -1.0)
- KXNHLSPREAD-26OCT20CARVAN-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.4 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3434, phi -0.757)
- KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.458, phi -0.245)

portfolios: A EV +4.39 (adj +1.09) on $13.64, P(profit) 0.5489, adj growth 10.1 bp · B EV +3.82 (adj +2.09) on $15.47, P(profit) 0.5943, adj growth 20.0 bp · C EV +4.31 (adj +2.46) on $8.96, P(profit) 0.3316, adj growth 23.3 bp · R EV +0.66 (adj +0.22) on $4.00, P(profit) 0.5589, adj growth 8.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT20CARVAN-VAN|yes == KXNHLGAME-26OCT20CARVAN-CAR|no

## TBL @ VGK  ·  10000 joint draws  ·  486 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TBL_win | p_overtime | goals | shots VGK/TBL | VGK/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.63 | 0.37 | 0.00 | 6.03 | 26.8/26.8 | 23.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.49 | 5.94 | 26.8/27.1 | 23.8/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.65 | 0.35 | 0.00 | 9.21 | 28.5/28.5 | 23.4/21.5 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.072 | 0.58 | 0.42 | 0.00 | 5.95 | 21.4/31.7 | 28.4/17.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.067 | 0.70 | 0.30 | 0.00 | 5.99 | 31.4/21.2 | 18.5/26.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.54 | 0.46 | 0.53 | 2.82 | 25.4/25.4 | 23.9/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 4 | 0.080 | 0.069 | +0.037 | +0.026 | $1.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Brett Howden: 1+ goals YES | 19 | 0.233 | 0.221 | +0.032 | +0.020 | $1.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 72 | 0.767 | 0.754 | +0.033 | +0.020 | $6.05 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 65 | 0.696 | 0.682 | +0.030 | +0.016 | $3.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (34.44 vs 5.57 bp); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VGK offense suppressed (<= 2 goals)
- **Brett Howden: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: higher confidence-adjusted growth (5.57 vs 5.30 bp); despite a smaller raw edge (+0.032 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT20TBVGK-VGKJEICHEL9-2|no; why: higher confidence-adjusted growth (4.42 vs 0.09 bp); despite a smaller raw edge (+0.033 vs +0.074/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: VGK offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no; why: Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis VGK:OFFENSE_4PLUS (p 0.4283): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:WINS (p 0.5848): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis TBL:SUPPRESSED (p 0.4793): highest fidelity KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no — Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3602, phi -0.131)
- KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3602, phi -0.236)
- KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4283, phi -0.197)
- KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3048, phi -0.253)
- override: Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.41 (adj +0.41) on $13.64, P(profit) 0.5901, adj growth 3.7 bp · B EV +2.23 (adj +1.48) on $13.20, P(profit) 0.6546, adj growth 14.1 bp · C EV +1.44 (adj +0.66) on $16.25, P(profit) 0.6472, adj growth 6.3 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.7669, adj growth 2.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
