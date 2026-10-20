# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-20T17:43:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.96 | +29.76 | +10.67 | +28.28 | 0.754 | -22.28 | -34.30 | 98.06 |
| B thesis-diversified (joint) ← optimiser card | 149.04 | +26.42 | +14.21 | +23.62 | 0.763 | -17.73 | -27.19 | 135.51 |
| C best expression per thesis | 148.51 | +30.60 | +15.39 | +26.98 | 0.727 | -24.87 | -37.30 | 143.81 |
| R FUNDED research stakes | 26.00 | +3.66 | +2.08 | +2.05 | 0.625 | -5.52 | -7.57 | 0.00 |

## SJS @ MTL  ·  10000 joint draws  ·  488 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.664 / away 0.336

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_SJS_win | p_overtime | goals | shots MTL/SJS | MTL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.65 | 0.35 | 0.00 | 5.99 | 27.3/27.2 | 24.5/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.54 | 0.46 | 0.48 | 5.89 | 27.4/27.4 | 24.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.68 | 0.32 | 0.00 | 9.25 | 28.7/28.7 | 23.4/21.4 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.077 | 0.69 | 0.31 | 0.00 | 6.01 | 31.9/21.5 | 18.9/27.2 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.59 | 0.41 | 0.46 | 5.84 | 32.1/21.7 | 18.5/28.6 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.065 | 0.58 | 0.42 | 0.00 | 6.07 | 21.9/32.2 | 28.7/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mason Marchment: 1+ goals YES | 18 | 0.229 | 0.215 | +0.038 | +0.025 | $2.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ goals NO | 54 | 0.606 | 0.588 | +0.048 | +0.030 | $4.72 | FUNDED_RESEARCH | $2 | MTL:SUPPRESSED | DIRECT (0.79) | EVIDENCE_STRONGER | D |
| Montreal over 4.5 goals scored NO | 64 | 0.727 | 0.681 | +0.071 | +0.025 | $4.98 | FUNDED_RESEARCH | $2 | MTL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ assists NO | 74 | 0.793 | 0.764 | +0.040 | +0.011 | $4.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20SJMTL-MTL3|no; why: higher confidence-adjusted growth (8.62 vs 2.58 bp); despite a smaller raw edge (+0.038 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26OCT20SJMTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.038); failure: SJS offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no; why: higher confidence-adjusted growth (8.26 vs 6.00 bp); despite a smaller raw edge (+0.048 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.009 vs 0.884); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no: REINFORCING (phi 0.243); KXNHLAST-26OCT20SJMTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: MTL offense succeeds (4+ goals)
- **Montreal over 4.5 goals scored NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no has the higher standalone adjusted growth (8.26 vs 6.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.243); they share one thesis budget; relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: REINFORCING (phi 0.243); KXNHLAST-26OCT20SJMTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: MTL offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20SJMTL-4|no; why: KXNHLTOTAL-26OCT20SJMTL-4|no has the higher standalone adjusted growth (3.84 vs 1.37 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.131); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no: MOSTLY_INDEPENDENT (phi 0.008); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:OFFENSE_4PLUS (p 0.3131): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3345): highest fidelity KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:LOW_EVENT (p 0.2366): highest fidelity KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no (same contract)
- KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4723, phi -0.228)
- KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4556, phi -0.273)
- KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4556, phi -0.67)
- KXNHLAST-26OCT20SJMTL-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3131, phi -0.228)

portfolios: A EV +1.92 (adj +0.61) on $13.90, P(profit) 0.4901, adj growth 5.5 bp · B EV +1.66 (adj +0.83) on $16.25, P(profit) 0.5274, adj growth 7.9 bp · C EV +2.34 (adj +1.20) on $17.41, P(profit) 0.6344, adj growth 11.2 bp · R EV +0.39 (adj +0.19) on $4.00, P(profit) 0.4931, adj growth 6.9 bp

## COL @ NJD  ·  10000 joint draws  ·  462 bet sides mapped, 12 +EV candidates, 4 on card

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
| Fedor Svechkov: 1+ goals YES | 8 | 0.116 | 0.105 | +0.030 | +0.020 | $1.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ assists NO | 46 | 0.601 | 0.503 | +0.124 | +0.025 | $4.35 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 65 | 0.704 | 0.689 | +0.038 | +0.023 | $5.97 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ assists NO | 49 | 0.611 | 0.523 | +0.103 | +0.015 | $2.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Fedor Svechkov: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20COLNJ-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (11.28 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0010 below the 0.010/contract floor; relationships: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: COL offense suppressed (<= 2 goals)
- **Cale Makar: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-2|no; why: higher confidence-adjusted growth (5.70 vs 4.21 bp); relationships: KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: COL offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20COLNJ-NJJHUGHES86-2|no; why: Player prop expression KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT20COLNJ-NJLEVANGELISTA77-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.85 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: NJD offense succeeds (4+ goals)
- **Jack Hughes: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no has the higher standalone adjusted growth (5.34 vs 2.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis COL:SUPPRESSED (p 0.3958): highest fidelity KXNHLAST-26OCT20COLNJ-COLCMAKAR8-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4184): highest fidelity KXNHLAST-26OCT20COLNJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT20COLNJ-NJLEVANGELISTA77-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.85 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis COL:OFFENSE_4PLUS (p 0.3807): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3958, phi -0.146)
- KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.1 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3807, phi -0.28)
- KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.361, phi -0.245)
- KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.6 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.361, phi -0.273)
- override: Player prop expression KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT20COLNJ-NJLEVANGELISTA77-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.85 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.81 (adj +0.47) on $13.90, P(profit) 0.6932, adj growth 4.6 bp · B EV +2.62 (adj +0.93) on $14.71, P(profit) 0.495, adj growth 8.9 bp · C EV +2.04 (adj +0.62) on $14.57, P(profit) 0.4209, adj growth 5.8 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.7039, adj growth 2.6 bp

## ANA @ NYI  ·  10000 joint draws  ·  422 bet sides mapped, 5 +EV candidates, 3 on card

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
| A.J. Greer: 1+ goals YES | 12 | 0.212 | 0.188 | +0.085 | +0.060 | $4.90 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 15 | 0.196 | 0.182 | +0.037 | +0.023 | $2.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 10 | 0.129 | 0.120 | +0.023 | +0.014 | $1.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT20ANANYI-7|yes; why: higher confidence-adjusted growth (68.65 vs 0.40 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.885 vs 0.681); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: ANA offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT20ANANYI-7|yes; why: higher confidence-adjusted growth (8.82 vs 0.40 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.882 vs 0.681); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: NYI offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes has the higher standalone adjusted growth (68.65 vs 4.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3377): highest fidelity KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.452): highest fidelity KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes (same contract)
- KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4388, phi -0.221)
- KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3304, phi -0.192)
- KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4388, phi -0.152)

portfolios: A EV +5.03 (adj +3.44) on $12.06, P(profit) 0.4517, adj growth 32.3 bp · B EV +4.02 (adj +2.80) on $8.25, P(profit) 0.4517, adj growth 26.5 bp · C EV +5.45 (adj +3.82) on $10.14, P(profit) 0.3664, adj growth 35.3 bp · R EV +1.33 (adj +0.95) on $2.00, P(profit) 0.2121, adj growth 34.7 bp

## LAK @ WSH  ·  10000 joint draws  ·  464 bet sides mapped, 5 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.586 / away 0.414

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
| Mats Zuccarello: 1+ assists NO | 65 | 0.861 | 0.708 | +0.195 | +0.042 | $6.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Aliaksei Protas: 1+ goals YES | 18 | 0.240 | 0.223 | +0.050 | +0.032 | $3.06 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 2+ assists NO | 93 | 0.990 | 0.952 | +0.055 | +0.018 | $6.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DIFFUSE | NONE | EVIDENCE_MIXED | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (17.18 vs 3.40 bp); relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT20LAWSH-LAMZUCCARELLO36-2|no: REINFORCING (phi 0.254); failure: LAK offense succeeds (4+ goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (14.67 vs 1.71 bp); despite a smaller raw edge (+0.050 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT20LAWSH-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT20LAWSH-LAMZUCCARELLO36-2|no: MOSTLY_INDEPENDENT (phi -0.001); failure: WSH offense suppressed (<= 2 goals)
- **Mats Zuccarello: 2+ assists NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLAST-26OCT20LAWSH-LAMZUCCARELLO36-1|no: REINFORCING (phi 0.254); KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis WSH:OFFENSE_4PLUS (p 0.4034): highest fidelity KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.5004): highest fidelity KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no (same contract)
- KXNHLAST-26OCT20LAWSH-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 23.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2876, phi -0.181)
- KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.374, phi -0.233)
- KXNHLAST-26OCT20LAWSH-LAMZUCCARELLO36-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; no single thesis (diffuse); fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2876, phi -0.112)

portfolios: A EV +2.52 (adj +0.54) on $13.90, P(profit) 0.5826, adj growth 5.3 bp · B EV +3.11 (adj +1.06) on $16.19, P(profit) 0.8898, adj growth 10.2 bp · C EV +2.81 (adj +1.14) on $19.63, P(profit) 0.7408, adj growth 10.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ CBJ  ·  10000 joint draws  ·  424 bet sides mapped, 16 +EV candidates, 4 on card

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
| Charlie Coyle: 1+ goals YES | 23 | 0.293 | 0.276 | +0.050 | +0.033 | $3.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 80 | 0.845 | 0.831 | +0.034 | +0.020 | $6.56 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 19 | 0.233 | 0.218 | +0.032 | +0.018 | $2.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Full Game: Over 5.5 goals scored NO | 40 | 0.478 | 0.436 | +0.061 | +0.020 | $3.65 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (13.13 vs 4.14 bp); relationships: KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLTOTAL-26OCT20TORCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.152); failure: CBJ offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20TORCBJ-TORAMATTHEWS34-2|no; why: KXNHLAST-26OCT20TORCBJ-TORAMATTHEWS34-2|no has the higher standalone adjusted growth (6.85 vs 5.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.055); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLTOTAL-26OCT20TORCBJ-6|no: MOSTLY_INDEPENDENT (phi 0.136); failure: TOR offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (13.13 vs 4.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLTOTAL-26OCT20TORCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.156); failure: CBJ offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no; why: KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no has the higher standalone adjusted growth (5.36 vs 3.43 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.453); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.152); KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.136); KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.156); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:SCORES_FIRST (p 0.4389): highest fidelity KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.4406): highest fidelity KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.5139): highest fidelity KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no (same contract)
- KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3382, phi -0.24)
- KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2668, phi -0.207)
- KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3382, phi -0.225)
- KXNHLTOTAL-26OCT20TORCBJ-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4406, phi -0.558)

portfolios: A EV +1.92 (adj +0.56) on $13.90, P(profit) 0.539, adj growth 5.1 bp · B EV +1.91 (adj +1.03) on $16.01, P(profit) 0.6868, adj growth 9.9 bp · C EV +5.55 (adj +2.23) on $19.23, P(profit) 0.6846, adj growth 20.9 bp · R EV +0.23 (adj +0.10) on $3.00, P(profit) 0.4281, adj growth 3.6 bp

## WPG @ STL  ·  10000 joint draws  ·  438 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.564 / away 0.436

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_WPG_win | p_overtime | goals | shots STL/WPG | STL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.65 | 0.35 | 0.00 | 6.0 | 26.6/26.5 | 23.6/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.54 | 0.46 | 0.48 | 5.93 | 26.3/26.6 | 23.4/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.67 | 0.33 | 0.00 | 9.32 | 28.0/28.1 | 22.9/21.1 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.081 | 0.71 | 0.29 | 0.00 | 6.01 | 31.3/21.0 | 18.6/26.5 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.55 | 0.45 | 0.46 | 5.88 | 30.9/21.0 | 17.9/27.6 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.063 | 0.58 | 0.42 | 0.00 | 5.98 | 21.3/31.3 | 28.0/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Morgan Barron: 1+ goals YES | 9 | 0.121 | 0.112 | +0.026 | +0.017 | $1.40 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Haydn Fleury: 1+ goals NO | 94 | 0.962 | 0.956 | +0.018 | +0.012 | $6.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 25 | 0.296 | 0.282 | +0.033 | +0.019 | $2.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 15 | 0.180 | 0.170 | +0.021 | +0.011 | $1.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (6.87 vs 1.63 bp); relationships: KXNHLGOAL-26OCT20WPGSTL-WPGHFLEURY24-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT20WPGSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: WPG offense suppressed (<= 2 goals)
- **Haydn Fleury: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT20WPGSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: WPG offense succeeds (4+ goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes; why: higher confidence-adjusted growth (4.12 vs 2.62 bp); despite a smaller raw edge (+0.033 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT20WPGSTL-WPGHFLEURY24-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT20WPGSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (4.12 vs 2.10 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT20WPGSTL-WPGHFLEURY24-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.4575): highest fidelity KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3138): highest fidelity KXNHLGOAL-26OCT20WPGSTL-WPGGVILARDI13-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20WPGSTL-WPGGVILARDI13-1|yes (same contract)
- KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4711, phi -0.163)
- KXNHLGOAL-26OCT20WPGSTL-WPGHFLEURY24-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3138, phi -0.09)
- KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3346, phi -0.242)
- KXNHLGOAL-26OCT20WPGSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3346, phi -0.191)

portfolios: A EV +2.05 (adj +0.94) on $12.80, P(profit) 0.5189, adj growth 8.6 bp · B EV +0.91 (adj +0.55) on $11.07, P(profit) 0.4812, adj growth 5.3 bp · C EV +0.74 (adj +0.42) on $14.36, P(profit) 0.4682, adj growth 4.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ DAL  ·  10000 joint draws  ·  418 bet sides mapped, 9 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.602 / away 0.398

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
| Boston over 2.5 goals scored YES | 51 | 0.598 | 0.552 | +0.071 | +0.024 | $1.40 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Miro Heiskanen: 1+ goals NO | 87 | 0.898 | 0.888 | +0.020 | +0.010 | $6.52 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
- **Boston over 2.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes; why: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes has the higher standalone adjusted growth (5.24 vs 5.12 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.248); relationships: KXNHLGOAL-26OCT20BOSDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: BOS offense suppressed (<= 2 goals)
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20BOSDAL-DAL2|no; why: higher confidence-adjusted growth (2.21 vs 1.80 bp); despite a smaller raw edge (+0.020 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:HIGH_EVENT (p 0.25): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.3632): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes (same contract)
- thesis BOS:WINS (p 0.4864): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.4135, phi -0.976)
- KXNHLGOAL-26OCT20BOSDAL-DALMHEISKANEN4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3916, phi -0.145)

portfolios: A EV +2.94 (adj +0.93) on $13.90, P(profit) 0.3739, adj growth 7.4 bp · B EV +0.33 (adj +0.14) on $7.92, P(profit) 0.5382, adj growth 1.4 bp · C EV +0.28 (adj +0.08) on $3.83, P(profit) 0.7045, adj growth 0.8 bp · R EV +0.18 (adj +0.07) on $3.00, P(profit) 0.5382, adj growth 2.7 bp

## MIN @ EDM  ·  10000 joint draws  ·  476 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.550 / away 0.450

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_MIN_win | p_overtime | goals | shots EDM/MIN | EDM/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.62 | 0.38 | 0.00 | 6.05 | 28.6/28.4 | 25.3/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.113 | 0.64 | 0.36 | 0.00 | 9.45 | 30.3/30.2 | 24.6/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.55 | 0.45 | 0.47 | 5.98 | 28.4/28.4 | 25.0/25.2 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.082 | 0.70 | 0.30 | 0.00 | 6.07 | 33.7/22.7 | 20.0/29.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.069 | 0.72 | 0.28 | 0.00 | 9.46 | 35.1/24.2 | 19.6/26.7 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.58 | 0.42 | 0.50 | 5.94 | 33.9/22.9 | 19.7/30.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 13 | 0.192 | 0.175 | +0.054 | +0.037 | $3.21 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ assists NO | 39 | 0.483 | 0.434 | +0.076 | +0.027 | $3.83 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.69) | EVIDENCE_MIXED | D |
| Zach Hyman: 1+ goals YES | 32 | 0.370 | 0.355 | +0.035 | +0.019 | $2.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ assists YES | 34 | 0.408 | 0.369 | +0.052 | +0.013 | $1.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20MINEDM-EDM6|yes; why: higher confidence-adjusted growth (24.49 vs 4.07 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.846 vs 0.309); relationships: KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT20MINEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: EDM offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no; why: higher confidence-adjusted growth (6.79 vs 2.20 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT20MINEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense succeeds (4+ goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (24.49 vs 3.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT20MINEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.085); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (24.49 vs 1.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi 0.085); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5018): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes less than the minimum stake; KXNHLAST-26OCT20MINEDM-EDMVPODKOLZIN92-1|yes kept
- thesis MIN:SUPPRESSED (p 0.4289): highest fidelity KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3227): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20MINEDM-EDM6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2953, phi -0.184)
- KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 31% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3548, phi -0.318)
- KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2953, phi -0.252)
- KXNHLAST-26OCT20MINEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 46% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2953, phi -0.259)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes less than the minimum stake; KXNHLAST-26OCT20MINEDM-EDMVPODKOLZIN92-1|yes kept

portfolios: A EV +3.04 (adj +1.36) on $13.90, P(profit) 0.4621, adj growth 12.7 bp · B EV +2.39 (adj +1.30) on $10.57, P(profit) 0.4296, adj growth 12.4 bp · C EV +3.19 (adj +1.72) on $11.23, P(profit) 0.5871, adj growth 16.1 bp · R EV +0.39 (adj +0.27) on $1.00, P(profit) 0.1915, adj growth 10.1 bp

## DET @ SEA  ·  10000 joint draws  ·  398 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.490 / away 0.510

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
| Ryan Winterton: 1+ goals YES | 12 | 0.169 | 0.156 | +0.042 | +0.028 | $2.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 11 | 0.153 | 0.141 | +0.036 | +0.024 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Moritz Seider: 1+ goals NO | 85 | 0.901 | 0.884 | +0.042 | +0.025 | $6.48 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Detroit wins by over 1.5 goals NO | 70 | 0.785 | 0.740 | +0.071 | +0.025 | $5.73 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20DETSEA-DET2|no; why: higher confidence-adjusted growth (15.29 vs 6.99 bp); despite a smaller raw edge (+0.042 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT20DETSEA-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26OCT20DETSEA-DET2|no: MOSTLY_INDEPENDENT (phi 0.112); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20DETSEA-DET2|no; why: higher confidence-adjusted growth (12.40 vs 6.99 bp); despite a smaller raw edge (+0.037 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT20DETSEA-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26OCT20DETSEA-DET2|no: MOSTLY_INDEPENDENT (phi 0.097); failure: SEA offense suppressed (<= 2 goals)
- **Moritz Seider: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20DETSEA-DET2|no; why: higher confidence-adjusted growth (11.89 vs 6.99 bp); despite a smaller raw edge (+0.042 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26OCT20DETSEA-DET2|no: MOSTLY_INDEPENDENT (phi 0.069); failure: DET offense succeeds (4+ goals)
- **Detroit wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20DETSEA-DET3|no; why: higher confidence-adjusted growth (6.99 vs 5.35 bp); relationships: KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.112); KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.097); KXNHLGOAL-26OCT20DETSEA-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.069); failure: DET wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4437): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4539): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.58): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no (same contract)
- KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.182)
- KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.164)
- KXNHLGOAL-26OCT20DETSEA-DETMSEIDER53-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3287, phi -0.146)
- KXNHLSPREAD-26OCT20DETSEA-DET2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2147, phi -1.0)

portfolios: A EV +1.46 (adj +0.46) on $13.90, P(profit) 0.6073, adj growth 4.2 bp · B EV +2.23 (adj +1.30) on $16.41, P(profit) 0.2978, adj growth 12.5 bp · C EV +0.94 (adj +0.34) on $9.56, P(profit) 0.7853, adj growth 3.3 bp · R EV +0.30 (adj +0.13) on $4.00, P(profit) 0.7159, adj growth 5.1 bp

## CAR @ VAN  ·  10000 joint draws  ·  404 bet sides mapped, 29 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.282 / away 0.718

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CAR_win | p_overtime | goals | shots VAN/CAR | VAN/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.177 | 0.37 | 0.63 | 0.00 | 6.03 | 20.8/34.3 | 29.8/17.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.145 | 0.47 | 0.53 | 0.46 | 5.93 | 20.9/34.3 | 30.8/17.8 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.128 | 0.38 | 0.62 | 0.00 | 9.33 | 22.5/36.1 | 28.6/17.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.082 | 0.46 | 0.54 | 0.00 | 6.06 | 27.0/28.3 | 24.6/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.52 | 0.48 | 0.46 | 5.93 | 26.9/27.9 | 24.7/23.7 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.071 | 0.39 | 0.61 | 0.00 | 3.45 | 19.9/32.7 | 30.2/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 11 | 0.181 | 0.162 | +0.064 | +0.045 | $3.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 10 | 0.149 | 0.136 | +0.043 | +0.029 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 49 | 0.659 | 0.546 | +0.152 | +0.038 | $3.71 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 62 | 0.686 | 0.667 | +0.049 | +0.030 | $5.83 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: higher confidence-adjusted growth (41.99 vs 28.56 bp); despite a smaller raw edge (+0.064 vs +0.086/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.942 vs 0.593); relationships: KXNHLGOAL-26OCT20CARVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (41.99 vs 19.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: MOSTLY_INDEPENDENT (phi 0.128); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: VAN offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes has the higher standalone adjusted growth (28.56 vs 12.94 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.327); relationships: KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT20CARVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.128); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: REINFORCING (phi 0.175); failure: CAR wins by 2+
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-CAR2|no; why: KXNHLTEAMTOTAL-26OCT20CARVAN-CAR2|no has the higher standalone adjusted growth (13.52 vs 8.66 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.202); relationships: KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT20CARVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.175); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.18, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3658): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.4415): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.2367): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4261, phi -0.207)
- KXNHLGOAL-26OCT20CARVAN-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4261, phi -0.194)
- KXNHLSPREAD-26OCT20CARVAN-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 17.4 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3409, phi -1.0)
- KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.452, phi -0.233)

portfolios: A EV +4.42 (adj +0.97) on $13.90, P(profit) 0.5479, adj growth 8.9 bp · B EV +4.38 (adj +2.53) on $15.25, P(profit) 0.6171, adj growth 24.0 bp · C EV +5.90 (adj +3.22) on $9.44, P(profit) 0.4144, adj growth 29.9 bp · R EV +0.45 (adj +0.17) on $3.00, P(profit) 0.6856, adj growth 6.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT20CARVAN-VAN|yes == KXNHLGAME-26OCT20CARVAN-CAR|no

## TBL @ VGK  ·  10000 joint draws  ·  460 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.503 / away 0.497

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TBL_win | p_overtime | goals | shots VGK/TBL | VGK/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.63 | 0.37 | 0.00 | 6.04 | 26.8/26.8 | 23.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.54 | 0.46 | 0.49 | 5.9 | 26.8/27.1 | 23.9/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.64 | 0.36 | 0.00 | 9.21 | 28.2/28.2 | 23.2/21.3 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.069 | 0.59 | 0.41 | 0.00 | 6.02 | 21.4/31.9 | 28.6/17.6 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.066 | 0.70 | 0.30 | 0.00 | 6.0 | 31.0/21.2 | 18.5/26.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.59 | 0.41 | 0.00 | 3.44 | 25.5/25.6 | 24.1/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 4 | 0.082 | 0.070 | +0.040 | +0.028 | $1.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 1.5 goals NO | 71 | 0.792 | 0.748 | +0.067 | +0.024 | $6.44 | FUNDED_RESEARCH | $2 | VGK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Brett Howden: 1+ goals YES | 19 | 0.236 | 0.222 | +0.035 | +0.021 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 71 | 0.760 | 0.746 | +0.035 | +0.021 | $6.44 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: higher confidence-adjusted growth (38.36 vs 6.32 bp); despite a smaller raw edge (+0.040 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT20TBVGK-TB2|no: MOSTLY_INDEPENDENT (phi 0.084); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: VGK offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: VGK wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no; why: higher confidence-adjusted growth (6.32 vs 3.31 bp); wins across more scripts (relative breadth 0.98 vs 0.61); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.084); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.142); failure: TBL wins by 2+
- **Brett Howden: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT20TBVGK-TB2|no has the higher standalone adjusted growth (6.32 vs 6.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.147); they share one thesis budget; relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26OCT20TBVGK-TB2|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20TBVGK-VGKTCONNELLY24-1|no; why: higher confidence-adjusted growth (5.11 vs 0.20 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0042 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT20TBVGK-TB2|no: INTENTIONAL_DIVERSIFIER (phi -0.142); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis VGK:OFFENSE_4PLUS (p 0.4248): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis VGK:WINS (p 0.5876): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis TBL:SUPPRESSED (p 0.4817): highest fidelity KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3512, phi -0.136)
- KXNHLSPREAD-26OCT20TBVGK-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2083, phi -1.0)
- KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3512, phi -0.217)
- KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4248, phi -0.219)

portfolios: A EV +1.65 (adj +0.39) on $13.90, P(profit) 0.5921, adj growth 3.6 bp · B EV +2.87 (adj +1.74) on $16.41, P(profit) 0.6718, adj growth 16.6 bp · C EV +1.35 (adj +0.60) on $19.11, P(profit) 0.5767, adj growth 5.7 bp · R EV +0.28 (adj +0.13) on $4.00, P(profit) 0.5767, adj growth 4.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
