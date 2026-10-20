# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-20T18:38:22Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +29.06 | +10.23 | +27.30 | 0.757 | -21.64 | -34.16 | 94.19 |
| B thesis-diversified (joint) ← optimiser card | 148.06 | +24.01 | +13.60 | +22.22 | 0.745 | -19.03 | -29.77 | 130.05 |
| C best expression per thesis | 149.41 | +30.06 | +14.41 | +27.56 | 0.740 | -24.07 | -37.03 | 134.77 |
| R FUNDED research stakes | 26.00 | +3.52 | +2.00 | +2.19 | 0.611 | -6.47 | -8.63 | 0.00 |

## SJS @ MTL  ·  10000 joint draws  ·  488 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.663 / away 0.337

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
| Mason Marchment: 1+ goals YES | 18 | 0.229 | 0.215 | +0.038 | +0.025 | $2.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ goals NO | 54 | 0.606 | 0.588 | +0.048 | +0.030 | $4.99 | FUNDED_RESEARCH | $2 | MTL:SUPPRESSED | DIRECT (0.79) | EVIDENCE_STRONGER | D |
| Montreal over 3.5 goals scored NO | 45 | 0.532 | 0.488 | +0.065 | +0.021 | $2.11 | FUNDED_RESEARCH | $1 | MTL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ assists NO | 74 | 0.793 | 0.764 | +0.040 | +0.011 | $4.18 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20SJMTL-MTL3|no; why: higher confidence-adjusted growth (8.62 vs 2.58 bp); despite a smaller raw edge (+0.038 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT20SJMTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.038); failure: SJS offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3|no; why: higher confidence-adjusted growth (8.26 vs 4.15 bp); despite a smaller raw edge (+0.048 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.009 vs 0.775); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4|no: REINFORCING (phi 0.271); KXNHLAST-26OCT20SJMTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: MTL offense succeeds (4+ goals)
- **Montreal over 3.5 goals scored NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4|no selected over player prop KXNHLAST-26OCT20SJMTL-MTLCKREIDER22-1|no because adjusted EV is 0.6 pts higher while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: REINFORCING (phi 0.271); KXNHLAST-26OCT20SJMTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: MTL offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20SJMTL-4|no; why: KXNHLTOTAL-26OCT20SJMTL-4|no has the higher standalone adjusted growth (3.84 vs 1.37 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.131); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4|no: MOSTLY_INDEPENDENT (phi -0.008); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:OFFENSE_4PLUS (p 0.3131): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3345): highest fidelity KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no — Broad expression KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4|no selected over player prop KXNHLAST-26OCT20SJMTL-MTLCKREIDER22-1|no because adjusted EV is 0.6 pts higher while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:LOW_EVENT (p 0.2366): highest fidelity KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4723, phi -0.228)
- KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4556, phi -0.273)
- KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4556, phi -0.976)
- KXNHLAST-26OCT20SJMTL-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3131, phi -0.228)
- override: Broad expression KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4|no selected over player prop KXNHLAST-26OCT20SJMTL-MTLCKREIDER22-1|no because adjusted EV is 0.6 pts higher while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.88 (adj +0.58) on $13.98, P(profit) 0.4901, adj growth 5.1 bp · B EV +1.43 (adj +0.74) on $13.71, P(profit) 0.5916, adj growth 7.1 bp · C EV +1.98 (adj +1.08) on $13.56, P(profit) 0.5522, adj growth 10.2 bp · R EV +0.31 (adj +0.15) on $3.00, P(profit) 0.6055, adj growth 5.8 bp

## COL @ NJD  ·  10000 joint draws  ·  460 bet sides mapped, 14 +EV candidates, 3 on card

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
| Cale Makar: 1+ assists NO | 45 | 0.601 | 0.500 | +0.134 | +0.032 | $5.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 64 | 0.704 | 0.687 | +0.048 | +0.030 | $6.08 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Nico Hischier: 1+ goals NO | 71 | 0.749 | 0.738 | +0.024 | +0.013 | $3.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Cale Makar: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-2|no; why: higher confidence-adjusted growth (9.16 vs 1.70 bp); relationships: KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT20COLNJ-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: COL offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20COLNJ-NJERODRIGUES17-1|no; why: higher confidence-adjusted growth (9.09 vs 7.38 bp); despite a smaller raw edge (+0.048 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT20COLNJ-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NJD offense succeeds (4+ goals)
- **Nico Hischier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT20COLNJ-NJNHISCHIER13-1|no selected over player prop KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.87 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis COL:SUPPRESSED (p 0.3958): highest fidelity KXNHLAST-26OCT20COLNJ-COLCMAKAR8-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4184): highest fidelity KXNHLAST-26OCT20COLNJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT20COLNJ-NJNHISCHIER13-1|no selected over player prop KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.87 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NJD:OFFENSE_4PLUS (p 0.361): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.6 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3807, phi -0.28)
- KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.361, phi -0.245)
- KXNHLGOAL-26OCT20COLNJ-NJNHISCHIER13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.361, phi -0.219)
- override: Player prop expression KXNHLGOAL-26OCT20COLNJ-NJNHISCHIER13-1|no selected over player prop KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.87 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.25 (adj +0.65) on $13.98, P(profit) 0.7709, adj growth 6.2 bp · B EV +2.03 (adj +0.71) on $14.95, P(profit) 0.5552, adj growth 6.8 bp · C EV +2.86 (adj +0.97) on $17.26, P(profit) 0.4209, adj growth 9.2 bp · R EV +0.15 (adj +0.09) on $2.00, P(profit) 0.7039, adj growth 3.6 bp

## ANA @ NYI  ·  10000 joint draws  ·  444 bet sides mapped, 4 +EV candidates, 3 on card

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
| A.J. Greer: 1+ goals YES | 13 | 0.212 | 0.190 | +0.074 | +0.052 | $4.41 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 15 | 0.196 | 0.182 | +0.037 | +0.023 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 10 | 0.129 | 0.120 | +0.023 | +0.014 | $1.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT20ANANYI-7|yes; why: higher confidence-adjusted growth (48.73 vs 0.40 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.885 vs 0.681); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: ANA offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT20ANANYI-7|yes; why: higher confidence-adjusted growth (8.82 vs 0.40 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.882 vs 0.681); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: NYI offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes has the higher standalone adjusted growth (48.73 vs 4.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3377): highest fidelity KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.452): highest fidelity KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes (same contract)
- KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4388, phi -0.221)
- KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3304, phi -0.192)
- KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4388, phi -0.152)

portfolios: A EV +4.38 (adj +2.98) on $12.04, P(profit) 0.5249, adj growth 27.8 bp · B EV +3.14 (adj +2.15) on $7.77, P(profit) 0.4517, adj growth 20.5 bp · C EV +4.24 (adj +2.94) on $9.62, P(profit) 0.3664, adj growth 27.2 bp · R EV +1.08 (adj +0.76) on $2.00, P(profit) 0.2121, adj growth 27.6 bp

## LAK @ WSH  ·  10000 joint draws  ·  440 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.583 / away 0.417

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
| Aliaksei Protas: 1+ goals YES | 17 | 0.240 | 0.222 | +0.060 | +0.042 | $3.85 | FUNDED_RESEARCH | $1 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 54 | 0.664 | 0.577 | +0.107 | +0.020 | $3.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Ryan Leonard: 1+ assists YES | 31 | 0.376 | 0.338 | +0.051 | +0.013 | $1.35 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Jordan Kyrou: 1+ assists NO | 67 | 0.727 | 0.696 | +0.042 | +0.011 | $3.53 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (25.13 vs 1.71 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26OCT20LAWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.043); failure: WSH offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT20LAWSH-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (3.40 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT20LAWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: LAK offense succeeds (4+ goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (25.13 vs 1.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.045); they share one thesis budget; relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT20LAWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.044); failure: WSH offense suppressed (<= 2 goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT20LAWSH-WSHJKYROU25-1|no; why: higher confidence-adjusted growth (1.14 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.043); KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis WSH:OFFENSE_4PLUS (p 0.4034): highest fidelity KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.5004): highest fidelity KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no (same contract)
- thesis WSH:SUPPRESSED (p 0.374): highest fidelity KXNHLAST-26OCT20LAWSH-WSHJKYROU25-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20LAWSH-WSHJKYROU25-1|no (same contract)
- KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.374, phi -0.233)
- KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2876, phi -0.27)
- KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.374, phi -0.278)
- KXNHLAST-26OCT20LAWSH-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4034, phi -0.229)

portfolios: A EV +2.57 (adj +1.09) on $13.98, P(profit) 0.4898, adj growth 10.4 bp · B EV +2.46 (adj +1.13) on $12.60, P(profit) 0.371, adj growth 10.8 bp · C EV +3.34 (adj +1.61) on $16.53, P(profit) 0.6129, adj growth 15.0 bp · R EV +0.34 (adj +0.23) on $1.00, P(profit) 0.2403, adj growth 8.8 bp

## TOR @ CBJ  ·  10000 joint draws  ·  426 bet sides mapped, 16 +EV candidates, 4 on card

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
| Charlie Coyle: 1+ goals YES | 23 | 0.293 | 0.276 | +0.050 | +0.033 | $3.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 18 | 0.233 | 0.217 | +0.042 | +0.027 | $2.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 80 | 0.845 | 0.832 | +0.034 | +0.021 | $6.15 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Full Game: Over 6.5 goals scored NO | 50 | 0.580 | 0.537 | +0.063 | +0.020 | $4.29 | FUNDED_RESEARCH | $2 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (13.13 vs 9.99 bp); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLTOTAL-26OCT20TORCBJ-7|no: INTENTIONAL_DIVERSIFIER (phi -0.148); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (13.13 vs 9.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLTOTAL-26OCT20TORCBJ-7|no: INTENTIONAL_DIVERSIFIER (phi -0.143); failure: CBJ offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no; why: Player prop expression KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no selected over player prop KXNHLAST-26OCT20TORCBJ-TORKMARCHENKO86-1|no because adjusted EV is 0.3 pts higher while thesis capture is 0.92 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLTOTAL-26OCT20TORCBJ-7|no: MOSTLY_INDEPENDENT (phi 0.138); failure: TOR offense succeeds (4+ goals)
- **Full Game: Over 6.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no; why: KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no has the higher standalone adjusted growth (5.36 vs 3.52 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.427); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.148); KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.143); KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.138); failure: high-event game (8+ goals)

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:SCORES_FIRST (p 0.4389): highest fidelity KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.4406): highest fidelity KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.5139): highest fidelity KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no (same contract)
- KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3382, phi -0.24)
- KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3382, phi -0.225)
- KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2668, phi -0.207)
- KXNHLTOTAL-26OCT20TORCBJ-7|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2288, phi -0.64)
- override: Player prop expression KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no selected over player prop KXNHLAST-26OCT20TORCBJ-TORKMARCHENKO86-1|no because adjusted EV is 0.3 pts higher while thesis capture is 0.92 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.78 (adj +0.49) on $13.98, P(profit) 0.5726, adj growth 4.6 bp · B EV +2.05 (adj +1.16) on $16.41, P(profit) 0.4181, adj growth 11.1 bp · C EV +5.71 (adj +2.29) on $20.71, P(profit) 0.7255, adj growth 21.4 bp · R EV +0.32 (adj +0.13) on $4.00, P(profit) 0.5148, adj growth 4.8 bp

## WPG @ STL  ·  10000 joint draws  ·  438 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.565 / away 0.435

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
| Robert Thomas: 1+ goals YES | 24 | 0.298 | 0.281 | +0.045 | +0.028 | $2.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Gabriel Vilardi: 1+ goals YES | 23 | 0.268 | 0.257 | +0.025 | +0.015 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Dalibor Dvorsky: 1+ goals NO | 82 | 0.849 | 0.841 | +0.019 | +0.010 | $5.21 | FUNDED_RESEARCH | $2 | STL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20WPGSTL-WPG2|no; why: higher confidence-adjusted growth (9.20 vs 1.14 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20WPGSTL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: STL offense suppressed (<= 2 goals)
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT20WPGSTL-9|yes; why: higher confidence-adjusted growth (2.54 vs 0.06 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.907 vs 0.37); alternative not eligible: confidence-adjusted EV +0.0019 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi -0.029); failure: WPG offense suppressed (<= 2 goals)
- **Dalibor Dvorsky: 1+ goals NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20WPGSTL-STLPBUCHNEVICH89-1|no; why: higher confidence-adjusted growth (1.69 vs 0.17 bp); despite a smaller raw edge (+0.019 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0040 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT20WPGSTL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.458): highest fidelity KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3045): highest fidelity KXNHLGOAL-26OCT20WPGSTL-WPGGVILARDI13-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20WPGSTL-WPGGVILARDI13-1|yes (same contract)
- thesis STL:SUPPRESSED (p 0.3361): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3361, phi -0.242)
- KXNHLGOAL-26OCT20WPGSTL-WPGGVILARDI13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4789, phi -0.26)
- KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.458, phi -0.163)

portfolios: A EV +1.13 (adj +0.69) on $12.17, P(profit) 0.4557, adj growth 6.4 bp · B EV +0.82 (adj +0.49) on $9.78, P(profit) 0.4557, adj growth 4.7 bp · C EV +1.04 (adj +0.64) on $6.76, P(profit) 0.4882, adj growth 6.0 bp · R EV +0.05 (adj +0.03) on $2.00, P(profit) 0.8493, adj growth 0.9 bp

## BOS @ DAL  ·  10000 joint draws  ·  422 bet sides mapped, 8 +EV candidates, 3 on card

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
| Boston over 4.5 goals scored YES | 13 | 0.200 | 0.162 | +0.062 | +0.024 | $1.50 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| Mikko Rantanen: 1+ goals NO | 68 | 0.735 | 0.720 | +0.040 | +0.025 | $6.56 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Boston over 2.5 goals scored YES | 51 | 0.598 | 0.552 | +0.071 | +0.024 | $1.92 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Boston over 4.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes; why: higher confidence-adjusted growth (10.79 vs 5.24 bp); wins across more scripts (relative breadth 0.54 vs 0.311); relationships: KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: INTENTIONAL_DIVERSIFIER (phi 0.005); KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: DUPLICATIVE (phi 0.409); failure: DAL wins (incl. OT/SO)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20BOSDAL-DAL2|no; why: higher confidence-adjusted growth (6.52 vs 1.80 bp); despite a smaller raw edge (+0.040 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes: INTENTIONAL_DIVERSIFIER (phi 0.005); KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: DAL offense succeeds (4+ goals)
- **Boston over 2.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes has the higher standalone adjusted growth (10.79 vs 5.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.409); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes: DUPLICATIVE (phi 0.409); KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.024); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BOS:OFFENSE_4PLUS (p 0.3632): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes kept
- thesis GAME:HIGH_EVENT (p 0.25): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:WINS (p 0.4864): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes: FUNDED_RESEARCH; family MIXED; loses 45% of the draws where the thesis happens; opposing: failure thesis DAL:WINS (p 0.5136, phi -0.429)
- KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3916, phi -0.225)
- KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.4135, phi -0.976)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes kept

portfolios: A EV +2.86 (adj +1.00) on $13.98, P(profit) 0.3739, adj growth 8.6 bp · B EV +1.31 (adj +0.59) on $9.98, P(profit) 0.4971, adj growth 5.7 bp · C EV +1.82 (adj +0.85) on $12.55, P(profit) 0.7874, adj growth 8.0 bp · R EV +0.70 (adj +0.30) on $4.00, P(profit) 0.4971, adj growth 10.8 bp

## MIN @ EDM  ·  10000 joint draws  ·  476 bet sides mapped, 14 +EV candidates, 4 on card

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
| Alex Formenton: 1+ goals YES | 13 | 0.192 | 0.174 | +0.054 | +0.036 | $3.13 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ assists NO | 39 | 0.483 | 0.434 | +0.076 | +0.027 | $3.83 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.69) | EVIDENCE_MIXED | D |
| Connor McDavid: 3+ assists NO | 89 | 0.942 | 0.911 | +0.045 | +0.014 | $6.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Zach Hyman: 1+ goals YES | 32 | 0.370 | 0.355 | +0.035 | +0.019 | $2.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20MINEDM-EDM6|yes; why: higher confidence-adjusted growth (22.88 vs 4.07 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.846 vs 0.309); relationships: KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-3|no: MOSTLY_INDEPENDENT (phi -0.039); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: EDM offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no; why: higher confidence-adjusted growth (6.79 vs 2.20 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-3|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: MIN offense succeeds (4+ goals)
- **Connor McDavid: 3+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (4.91 vs 1.15 bp); despite a smaller raw edge (+0.045 vs +0.078/contract); relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.039); KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.127); failure: EDM offense succeeds (4+ goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (22.88 vs 3.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-3|no: INTENTIONAL_DIVERSIFIER (phi -0.127); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5018): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4289): highest fidelity KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3227): highest fidelity KXNHLTOTAL-26OCT20MINEDM-8|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2953, phi -0.184)
- KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 31% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3548, phi -0.318)
- KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-3|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5018, phi -0.223)
- KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2953, phi -0.252)

portfolios: A EV +3.10 (adj +0.56) on $13.98, P(profit) 0.6102, adj growth 5.1 bp · B EV +2.53 (adj +1.32) on $16.05, P(profit) 0.5795, adj growth 12.6 bp · C EV +3.92 (adj +1.79) on $14.32, P(profit) 0.4116, adj growth 16.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ SEA  ·  10000 joint draws  ·  398 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.489 / away 0.511

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

portfolios: A EV +1.46 (adj +0.45) on $13.98, P(profit) 0.6073, adj growth 4.1 bp · B EV +2.23 (adj +1.30) on $16.41, P(profit) 0.2978, adj growth 12.5 bp · C EV +0.96 (adj +0.35) on $9.73, P(profit) 0.7853, adj growth 3.3 bp · R EV +0.30 (adj +0.13) on $4.00, P(profit) 0.7159, adj growth 5.1 bp

## CAR @ VAN  ·  10000 joint draws  ·  410 bet sides mapped, 27 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.282 / away 0.718

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CAR_win | p_overtime | goals | shots VAN/CAR | VAN/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.169 | 0.36 | 0.64 | 0.00 | 6.06 | 20.9/33.9 | 29.5/18.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.155 | 0.47 | 0.53 | 0.47 | 5.94 | 21.1/34.5 | 31.0/17.9 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.125 | 0.35 | 0.65 | 0.00 | 9.34 | 22.5/36.1 | 28.4/17.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.081 | 0.45 | 0.55 | 0.00 | 6.04 | 26.8/28.1 | 24.2/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.53 | 0.47 | 0.47 | 5.96 | 26.7/27.8 | 24.5/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.068 | 0.47 | 0.53 | 0.00 | 9.33 | 28.5/29.8 | 23.4/22.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 12 | 0.178 | 0.162 | +0.051 | +0.035 | $2.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ goals YES | 18 | 0.250 | 0.230 | +0.059 | +0.039 | $3.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 10 | 0.145 | 0.132 | +0.038 | +0.026 | $2.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 62 | 0.679 | 0.662 | +0.042 | +0.025 | $5.41 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: higher confidence-adjusted growth (23.37 vs 22.91 bp); despite a smaller raw edge (+0.051 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.921 vs 0.594); relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT20CARVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: VAN offense suppressed (<= 2 goals)
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes has the higher standalone adjusted growth (22.91 vs 21.68 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.198); relationships: KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT20CARVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes has the higher standalone adjusted growth (22.91 vs 15.07 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.180); relationships: KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VAN offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20CARVAN-VAN2|yes; why: Player prop expression KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-CAR3|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT20CARVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3648): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2282): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- thesis VAN:WINS (p 0.4384): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4181, phi -0.206)
- KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4181, phi -0.248)
- KXNHLGOAL-26OCT20CARVAN-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4181, phi -0.18)
- KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4526, phi -0.242)
- override: Player prop expression KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-CAR3|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.56 (adj +1.03) on $13.98, P(profit) 0.5474, adj growth 9.5 bp · B EV +3.40 (adj +2.27) on $14.03, P(profit) 0.4714, adj growth 21.6 bp · C EV +2.50 (adj +1.03) on $4.04, P(profit) 0.2942, adj growth 9.6 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.6788, adj growth 3.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT20CARVAN-VAN|yes == KXNHLGAME-26OCT20CARVAN-CAR|no

## TBL @ VGK  ·  10000 joint draws  ·  464 bet sides mapped, 12 +EV candidates, 4 on card

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
| Brayden McNabb: 1+ goals YES | 4 | 0.080 | 0.069 | +0.037 | +0.026 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 63 | 0.696 | 0.678 | +0.050 | +0.032 | $6.56 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Brett Howden: 1+ goals YES | 19 | 0.233 | 0.220 | +0.032 | +0.019 | $1.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 72 | 0.767 | 0.754 | +0.033 | +0.020 | $6.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: higher confidence-adjusted growth (34.44 vs 5.30 bp); despite a smaller raw edge (+0.038 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: VGK offense suppressed (<= 2 goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no; why: higher confidence-adjusted growth (9.71 vs 5.47 bp); despite a smaller raw edge (+0.050 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.995 vs 0.608); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: TBL offense succeeds (4+ goals)
- **Brett Howden: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: KXNHLSPREAD-26OCT20TBVGK-TB2|no has the higher standalone adjusted growth (5.30 vs 4.91 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.153); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT20TBVGK-VGKTCONNELLY24-2|no; why: higher confidence-adjusted growth (4.42 vs 0.03 bp); despite a smaller raw edge (+0.033 vs +0.045/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0011 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis TBL:SUPPRESSED (p 0.4793): highest fidelity KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:WINS (p 0.5848): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:OFFENSE_4PLUS (p 0.4283): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3602, phi -0.131)
- KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3048, phi -0.253)
- KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3602, phi -0.236)
- KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4283, phi -0.197)

portfolios: A EV +2.08 (adj +0.71) on $13.98, P(profit) 0.4664, adj growth 6.2 bp · B EV +2.62 (adj +1.74) on $16.37, P(profit) 0.6546, adj growth 16.6 bp · C EV +1.68 (adj +0.86) on $24.33, P(profit) 0.4327, adj growth 8.2 bp · R EV +0.15 (adj +0.10) on $2.00, P(profit) 0.6958, adj growth 3.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
