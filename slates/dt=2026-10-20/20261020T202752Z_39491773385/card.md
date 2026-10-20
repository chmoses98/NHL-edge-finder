# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-20T20:27:52Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +31.74 | +10.54 | +31.09 | 0.790 | -17.51 | -29.67 | 98.38 |
| B thesis-diversified (joint) ← optimiser card | 148.35 | +25.63 | +13.10 | +24.26 | 0.771 | -15.88 | -26.76 | 125.48 |
| C best expression per thesis | 147.36 | +27.67 | +12.43 | +25.61 | 0.767 | -17.95 | -29.99 | 117.61 |
| R FUNDED research stakes | 23.00 | +3.01 | +1.70 | +1.32 | 0.611 | -5.44 | -7.20 | 0.00 |

## SJS @ MTL  ·  10000 joint draws  ·  488 bet sides mapped, 17 +EV candidates, 4 on card

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
| Mason Marchment: 1+ goals YES | 18 | 0.229 | 0.215 | +0.038 | +0.025 | $2.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cole Caufield: 2+ goals NO | 87 | 0.910 | 0.897 | +0.032 | +0.019 | $6.30 | FUNDED_RESEARCH | $2 | MTL:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ goals NO | 55 | 0.606 | 0.590 | +0.038 | +0.023 | $3.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:SUPPRESSED | DIRECT (0.79) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 74 | 0.793 | 0.764 | +0.040 | +0.011 | $3.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20SJMTL-MTL3|no; why: higher confidence-adjusted growth (8.62 vs 2.58 bp); despite a smaller raw edge (+0.038 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-2|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT20SJMTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.038); failure: SJS offense suppressed (<= 2 goals)
- **Cole Caufield: 2+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no; why: higher confidence-adjusted growth (7.78 vs 4.74 bp); despite a smaller raw edge (+0.032 vs +0.038/contract); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: DUPLICATIVE (phi 0.39); KXNHLAST-26OCT20SJMTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: MTL offense succeeds (4+ goals)
- **Cole Caufield: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3|no; why: higher confidence-adjusted growth (4.74 vs 4.15 bp); despite a smaller raw edge (+0.038 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.009 vs 0.775); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-2|no: DUPLICATIVE (phi 0.39); KXNHLAST-26OCT20SJMTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: MTL offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20SJMTL-4|no; why: KXNHLTOTAL-26OCT20SJMTL-4|no has the higher standalone adjusted growth (3.84 vs 1.37 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.131); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-2|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:OFFENSE_4PLUS (p 0.3131): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3345): highest fidelity KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:LOW_EVENT (p 0.2366): highest fidelity KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4723, phi -0.228)
- KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4556, phi -0.232)
- KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4556, phi -0.273)
- KXNHLAST-26OCT20SJMTL-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3131, phi -0.228)

portfolios: A EV +1.84 (adj +0.55) on $13.64, P(profit) 0.5118, adj growth 4.9 bp · B EV +1.13 (adj +0.63) on $15.86, P(profit) 0.6002, adj growth 6.1 bp · C EV +0.89 (adj +0.57) on $7.24, P(profit) 0.697, adj growth 5.4 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.9097, adj growth 1.7 bp

## COL @ NJD  ·  10000 joint draws  ·  466 bet sides mapped, 10 +EV candidates, 4 on card

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
| Cale Makar: 1+ assists NO | 45 | 0.601 | 0.500 | +0.134 | +0.032 | $4.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 64 | 0.704 | 0.687 | +0.048 | +0.030 | $5.59 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 11 | 0.150 | 0.138 | +0.033 | +0.021 | $1.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ assists NO | 47 | 0.611 | 0.516 | +0.124 | +0.029 | $3.94 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Cale Makar: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-2|no; why: higher confidence-adjusted growth (9.16 vs 4.21 bp); relationships: KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT20COLNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: COL offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT20COLNJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.85 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT20COLNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20COLNJ-NJDMERCER91-1|yes; why: higher confidence-adjusted growth (8.88 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.022); failure: NJD offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no has the higher standalone adjusted growth (9.09 vs 7.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.017); they share one thesis budget; relationships: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT20COLNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis COL:SUPPRESSED (p 0.3958): highest fidelity KXNHLAST-26OCT20COLNJ-COLCMAKAR8-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4184): highest fidelity KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.361): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.6 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3807, phi -0.28)
- KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.361, phi -0.245)
- KXNHLGOAL-26OCT20COLNJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4184, phi -0.17)
- KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.6 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.361, phi -0.273)
- override: Player prop expression KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT20COLNJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.85 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.88 (adj +0.66) on $13.64, P(profit) 0.7223, adj growth 6.5 bp · B EV +3.09 (adj +1.06) on $15.41, P(profit) 0.7421, adj growth 10.3 bp · C EV +2.32 (adj +0.79) on $14.01, P(profit) 0.4209, adj growth 7.5 bp · R EV +0.15 (adj +0.09) on $2.00, P(profit) 0.7039, adj growth 3.6 bp

## ANA @ NYI  ·  10000 joint draws  ·  456 bet sides mapped, 7 +EV candidates, 3 on card

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
| A.J. Greer: 1+ goals YES | 13 | 0.212 | 0.190 | +0.074 | +0.052 | $4.26 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 15 | 0.196 | 0.183 | +0.037 | +0.025 | $2.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 10 | 0.129 | 0.120 | +0.023 | +0.014 | $1.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20ANANYI-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (48.73 vs 2.13 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: ANA offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT20ANANYI-7|yes; why: higher confidence-adjusted growth (9.78 vs 0.40 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.882 vs 0.681); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: NYI offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes has the higher standalone adjusted growth (48.73 vs 4.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3377): highest fidelity KXNHLAST-26OCT20ANANYI-ANAAKILLORN17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:OFFENSE_4PLUS (p 0.452): highest fidelity KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes (same contract)
- thesis NYI:NET_HIGH_VOLUME (p 0.223): highest fidelity KXNHLSAVE-26OCT20ANANYI-NYIISOROKIN30-23|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT20ANANYI-NYIISOROKIN30-23|yes (same contract)
- KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4388, phi -0.221)
- KXNHLGOAL-26OCT20ANANYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3304, phi -0.192)
- KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4388, phi -0.152)

portfolios: A EV +4.12 (adj +2.12) on $13.64, P(profit) 0.5538, adj growth 20.0 bp · B EV +3.06 (adj +2.12) on $7.64, P(profit) 0.4517, adj growth 20.2 bp · C EV +4.02 (adj +2.50) on $10.91, P(profit) 0.3664, adj growth 23.5 bp · R EV +1.08 (adj +0.76) on $2.00, P(profit) 0.2121, adj growth 27.6 bp

## LAK @ WSH  ·  10000 joint draws  ·  478 bet sides mapped, 5 +EV candidates, 4 on card

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
| Aliaksei Protas: 1+ goals YES | 17 | 0.240 | 0.222 | +0.060 | +0.042 | $3.72 | FUNDED_RESEARCH | $1 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 54 | 0.664 | 0.577 | +0.107 | +0.020 | $3.75 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Ryan Leonard: 1+ assists YES | 31 | 0.376 | 0.338 | +0.051 | +0.013 | $1.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Jordan Kyrou: 1+ assists NO | 67 | 0.727 | 0.696 | +0.042 | +0.011 | $3.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (25.13 vs 1.71 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26OCT20LAWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.043); failure: WSH offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20LAWSH-LAEGUSTAFSSON64-1|no; why: higher confidence-adjusted growth (3.40 vs 0.23 bp); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT20LAWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: LAK offense succeeds (4+ goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (25.13 vs 1.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.045); they share one thesis budget; relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT20LAWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.044); failure: WSH offense suppressed (<= 2 goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT20LAWSH-WSHJKYROU25-1|no; why: higher confidence-adjusted growth (1.14 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.043); KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis WSH:OFFENSE_4PLUS (p 0.4034): highest fidelity KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.5004): highest fidelity KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no (same contract)
- thesis LAK:NET_LOW_VOLUME (p 0.4466): highest fidelity KXNHLSAVE-26OCT20LAWSH-LADKUEMPER35-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT20LAWSH-LADKUEMPER35-27|no (same contract)
- KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.374, phi -0.233)
- KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2876, phi -0.27)
- KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.374, phi -0.278)
- KXNHLAST-26OCT20LAWSH-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4034, phi -0.229)

portfolios: A EV +2.94 (adj +1.07) on $13.64, P(profit) 0.4882, adj growth 10.2 bp · B EV +2.38 (adj +1.10) on $12.19, P(profit) 0.371, adj growth 10.5 bp · C EV +3.18 (adj +1.35) on $16.06, P(profit) 0.507, adj growth 12.7 bp · R EV +0.34 (adj +0.23) on $1.00, P(profit) 0.2403, adj growth 8.8 bp

## TOR @ CBJ  ·  10000 joint draws  ·  440 bet sides mapped, 25 +EV candidates, 4 on card

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
| Charlie Coyle: 1+ goals YES | 23 | 0.293 | 0.276 | +0.050 | +0.033 | $2.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 18 | 0.233 | 0.217 | +0.042 | +0.027 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 80 | 0.845 | 0.832 | +0.034 | +0.021 | $5.26 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Jack Roslovic: 1+ goals NO | 77 | 0.809 | 0.798 | +0.026 | +0.015 | $4.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (13.13 vs 9.99 bp); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT20TORCBJ-TORJROSLOVIC96-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (13.13 vs 9.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT20TORCBJ-TORJROSLOVIC96-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: CBJ offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20TORCBJ-5|no; why: Player prop expression KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no selected over broad KXNHLTOTAL-26OCT20TORCBJ-8|no because adjusted EV is 0.7 pts higher while thesis capture is 0.92 vs 0.94 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT20TORCBJ-TORJROSLOVIC96-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: TOR offense succeeds (4+ goals)
- **Jack Roslovic: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no; why: Player prop expression KXNHLGOAL-26OCT20TORCBJ-TORJROSLOVIC96-1|no selected over player prop KXNHLAST-26OCT20TORCBJ-TORKMARCHENKO86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: TOR offense succeeds (4+ goals)

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:SCORES_FIRST (p 0.4389): highest fidelity KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.4406): highest fidelity KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.5139): highest fidelity KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no (same contract)
- KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3382, phi -0.24)
- KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3382, phi -0.225)
- KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2668, phi -0.207)
- KXNHLGOAL-26OCT20TORCBJ-TORJROSLOVIC96-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2668, phi -0.203)
- override: Player prop expression KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no selected over broad KXNHLTOTAL-26OCT20TORCBJ-8|no because adjusted EV is 0.7 pts higher while thesis capture is 0.92 vs 0.94 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT20TORCBJ-TORJROSLOVIC96-1|no selected over player prop KXNHLAST-26OCT20TORCBJ-TORKMARCHENKO86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.74 (adj +0.49) on $13.64, P(profit) 0.5726, adj growth 4.6 bp · B EV +1.47 (adj +0.94) on $14.71, P(profit) 0.4472, adj growth 9.1 bp · C EV +2.31 (adj +1.11) on $13.94, P(profit) 0.4892, adj growth 10.4 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.8448, adj growth 2.0 bp

## WPG @ STL  ·  10000 joint draws  ·  506 bet sides mapped, 5 +EV candidates, 4 on card

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
| Robert Thomas: 1+ goals YES | 23 | 0.298 | 0.277 | +0.056 | +0.035 | $2.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jake Neighbours: 1+ assists YES | 24 | 0.322 | 0.279 | +0.069 | +0.026 | $2.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Philip Broberg: 1+ assists YES | 33 | 0.411 | 0.368 | +0.066 | +0.023 | $2.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
| Dalibor Dvorsky: 1+ goals NO | 82 | 0.849 | 0.841 | +0.019 | +0.010 | $6.35 | FUNDED_RESEARCH | $2 | STL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20WPGSTL-STLJNEIGHBOURS63-1|yes; why: higher confidence-adjusted growth (14.37 vs 7.67 bp); despite a smaller raw edge (+0.056 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT20WPGSTL-STLJNEIGHBOURS63-1|yes: MOSTLY_INDEPENDENT (phi 0.12); KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.141); KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: STL offense suppressed (<= 2 goals)
- **Jake Neighbours: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (14.37 vs 7.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.120); they share one thesis budget; relationships: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.12); KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.066); KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: INTENTIONAL_DIVERSIFIER (phi -0.148); failure: STL offense suppressed (<= 2 goals)
- **Philip Broberg: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (14.37 vs 5.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.141); they share one thesis budget; relationships: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.141); KXNHLAST-26OCT20WPGSTL-STLJNEIGHBOURS63-1|yes: MOSTLY_INDEPENDENT (phi 0.066); KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: INTENTIONAL_DIVERSIFIER (phi -0.053); failure: STL offense suppressed (<= 2 goals)
- **Dalibor Dvorsky: 1+ goals NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20WPGSTL-STLPBUCHNEVICH89-1|no; why: higher confidence-adjusted growth (1.69 vs 0.17 bp); despite a smaller raw edge (+0.019 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0040 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT20WPGSTL-STLJNEIGHBOURS63-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.148); KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.053); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.458): highest fidelity KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:SUPPRESSED (p 0.3361): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3361, phi -0.242)
- KXNHLAST-26OCT20WPGSTL-STLJNEIGHBOURS63-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3361, phi -0.264)
- KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3361, phi -0.279)
- KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.458, phi -0.163)

portfolios: A EV +2.89 (adj +1.29) on $13.64, P(profit) 0.569, adj growth 12.0 bp · B EV +1.83 (adj +0.87) on $13.60, P(profit) 0.4605, adj growth 8.3 bp · C EV +0.99 (adj +0.62) on $4.31, P(profit) 0.2981, adj growth 5.9 bp · R EV +0.05 (adj +0.03) on $2.00, P(profit) 0.8493, adj growth 0.9 bp

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
| Mikko Rantanen: 1+ goals NO | 68 | 0.735 | 0.720 | +0.040 | +0.025 | $6.35 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Boston over 2.5 goals scored YES | 51 | 0.598 | 0.552 | +0.071 | +0.024 | $4.24 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Charlie McAvoy: 1+ assists NO | 59 | 0.654 | 0.617 | +0.048 | +0.010 | $4.05 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20BOSDAL-DAL2|no; why: higher confidence-adjusted growth (6.52 vs 1.80 bp); despite a smaller raw edge (+0.040 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26OCT20BOSDAL-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: DAL offense succeeds (4+ goals)
- **Boston over 2.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes; why: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes has the higher standalone adjusted growth (10.79 vs 5.12 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.409); relationships: KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26OCT20BOSDAL-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.278); failure: BOS offense suppressed (<= 2 goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT20BOSDAL-BOSCMCAVOY73-2|no; why: higher confidence-adjusted growth (0.97 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0000 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: INTENTIONAL_DIVERSIFIER (phi -0.278); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BOS:OFFENSE_4PLUS (p 0.3632): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes — Broad expression KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes selected over broad KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:HIGH_EVENT (p 0.25): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:WINS (p 0.4864): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3916, phi -0.225)
- KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.4135, phi -0.976)
- KXNHLAST-26OCT20BOSDAL-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3632, phi -0.264)
- override: Broad expression KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes selected over broad KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.07 (adj +1.04) on $13.64, P(profit) 0.4574, adj growth 9.1 bp · B EV +1.25 (adj +0.49) on $14.64, P(profit) 0.765, adj growth 4.7 bp · C EV +2.29 (adj +0.90) on $17.30, P(profit) 0.6724, adj growth 8.5 bp · R EV +0.38 (adj +0.16) on $4.00, P(profit) 0.4451, adj growth 6.1 bp

## MIN @ EDM  ·  10000 joint draws  ·  480 bet sides mapped, 11 +EV candidates, 4 on card

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
| Alex Formenton: 1+ goals YES | 13 | 0.190 | 0.172 | +0.052 | +0.034 | $2.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 32 | 0.410 | 0.362 | +0.074 | +0.027 | $4.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Zach Hyman: 1+ goals YES | 32 | 0.375 | 0.359 | +0.040 | +0.023 | $3.07 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| Edmonton over 2.5 goals scored YES | 65 | 0.718 | 0.682 | +0.052 | +0.016 | $3.71 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (21.29 vs 6.31 bp); despite a smaller raw edge (+0.052 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.055); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes: REINFORCING (phi 0.175); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (7.18 vs 0.95 bp); despite a smaller raw edge (+0.074 vs +0.084/contract); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.055); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.207); KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes: INTENTIONAL_DIVERSIFIER (phi -0.335); failure: EDM offense succeeds (4+ goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes; why: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes has the higher standalone adjusted growth (6.31 vs 5.37 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.125); relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.207); KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes: REINFORCING (phi 0.26); failure: EDM offense suppressed (<= 2 goals)
- **Edmonton over 2.5 goals scored YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes selected over player prop KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.42 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: REINFORCING (phi 0.175); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.335); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: REINFORCING (phi 0.26); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:SUPPRESSED (p 0.2913): highest fidelity KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.4983): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes — Broad expression KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes selected over player prop KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.42 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:HIGH_EVENT (p 0.3219): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes (same contract)
- KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2913, phi -0.178)
- KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 33% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4983, phi -0.328)
- KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2913, phi -0.265)
- KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis EDM:SUPPRESSED (p 0.2913, phi -0.977)
- override: Broad expression KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes selected over player prop KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.42 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.55 (adj +0.81) on $13.64, P(profit) 0.6361, adj growth 7.7 bp · B EV +2.68 (adj +1.35) on $14.00, P(profit) 0.5756, adj growth 12.9 bp · C EV +2.47 (adj +0.93) on $13.25, P(profit) 0.5988, adj growth 8.9 bp · R EV +0.20 (adj +0.09) on $2.00, P(profit) 0.3749, adj growth 3.5 bp

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
| Adam Larsson: 1+ assists YES | 18 | 0.313 | 0.223 | +0.123 | +0.033 | $2.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
| Ben Meyers: 1+ goals YES | 11 | 0.153 | 0.141 | +0.036 | +0.024 | $1.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Dylan Larkin: 1+ goals NO | 68 | 0.741 | 0.725 | +0.046 | +0.030 | $6.35 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $1.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Adam Larsson: 1+ assists YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20DETSEA-DET3|no; why: higher confidence-adjusted growth (15.32 vs 5.35 bp); relationships: KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.074); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.085); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes has the higher standalone adjusted growth (15.32 vs 12.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.074); they share one thesis budget; relationships: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.074); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: SEA offense suppressed (<= 2 goals)
- **Dylan Larkin: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20DETSEA-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (9.09 vs 6.02 bp); despite a smaller raw edge (+0.046 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: DET offense succeeds (4+ goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes has the higher standalone adjusted growth (15.32 vs 7.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.085); they share one thesis budget; relationships: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.085); KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4437): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [DIRECT], best adjusted EV KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4539): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.58): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT20DETSEA-SEAKKAKKO84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.8 pts; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.235)
- KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.164)
- KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3287, phi -0.226)
- KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.182)

portfolios: A EV +3.77 (adj +1.03) on $13.64, P(profit) 0.5286, adj growth 9.7 bp · B EV +2.75 (adj +1.26) on $11.94, P(profit) 0.4211, adj growth 12.1 bp · C EV +2.91 (adj +1.02) on $18.68, P(profit) 0.7482, adj growth 9.7 bp · R EV +0.13 (adj +0.09) on $2.00, P(profit) 0.7414, adj growth 3.3 bp

## CAR @ VAN  ·  10000 joint draws  ·  452 bet sides mapped, 30 +EV candidates, 4 on card

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
| Filip Chytil: 1+ goals YES | 18 | 0.250 | 0.231 | +0.059 | +0.041 | $3.44 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 17 | 0.232 | 0.215 | +0.052 | +0.035 | $2.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 62 | 0.778 | 0.672 | +0.141 | +0.036 | $6.35 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sean Walker: 1+ assists YES | 28 | 0.351 | 0.310 | +0.057 | +0.016 | $2.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CAR:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: higher confidence-adjusted growth (23.06 vs 22.91 bp); despite a smaller raw edge (+0.059 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.905 vs 0.594); relationships: KXNHLGOAL-26OCT20CARVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLAST-26OCT20CARVAN-CARSWALKER26-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (23.06 vs 17.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: MOSTLY_INDEPENDENT (phi 0.122); KXNHLAST-26OCT20CARVAN-CARSWALKER26-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: VAN offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes has the higher standalone adjusted growth (22.91 vs 12.02 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.244); relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT20CARVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.122); KXNHLAST-26OCT20CARVAN-CARSWALKER26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.155); failure: CAR wins by 2+
- **Sean Walker: 1+ assists YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT20CARVAN-CAREROBINSON50-1|yes; why: higher confidence-adjusted growth (2.80 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT20CARVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: INTENTIONAL_DIVERSIFIER (phi -0.155); failure: CAR offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3648): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.4384): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.2282): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4181, phi -0.248)
- KXNHLGOAL-26OCT20CARVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4181, phi -0.225)
- KXNHLSPREAD-26OCT20CARVAN-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.3 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3389, phi -0.746)
- KXNHLAST-26OCT20CARVAN-CARSWALKER26-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:SUPPRESSED (p 0.3275, phi -0.247)

portfolios: A EV +4.45 (adj +1.01) on $13.64, P(profit) 0.5474, adj growth 9.3 bp · B EV +3.73 (adj +1.78) on $14.81, P(profit) 0.5468, adj growth 17.0 bp · C EV +4.75 (adj +1.93) on $14.39, P(profit) 0.4594, adj growth 18.3 bp · R EV +0.44 (adj +0.11) on $2.00, P(profit) 0.778, adj growth 4.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT20CARVAN-VAN|yes == KXNHLGAME-26OCT20CARVAN-CAR|no

## TBL @ VGK  ·  10000 joint draws  ·  472 bet sides mapped, 12 +EV candidates, 4 on card

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
| Mitch Marner: 1+ goals NO | 72 | 0.767 | 0.754 | +0.033 | +0.020 | $6.08 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 65 | 0.696 | 0.683 | +0.030 | +0.017 | $3.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (34.44 vs 5.57 bp); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VGK offense suppressed (<= 2 goals)
- **Brett Howden: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: higher confidence-adjusted growth (5.57 vs 5.30 bp); despite a smaller raw edge (+0.032 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT20TBVGK-VGKJEICHEL9-2|no; why: higher confidence-adjusted growth (4.42 vs 0.09 bp); despite a smaller raw edge (+0.033 vs +0.074/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: VGK offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no; why: Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis VGK:OFFENSE_4PLUS (p 0.4283): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:WINS (p 0.5848): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis TBL:SUPPRESSED (p 0.4793): highest fidelity KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no — Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3602, phi -0.131)
- KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3602, phi -0.236)
- KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4283, phi -0.197)
- KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3048, phi -0.253)
- override: Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.50 (adj +0.47) on $13.64, P(profit) 0.5915, adj growth 4.4 bp · B EV +2.25 (adj +1.50) on $13.55, P(profit) 0.6546, adj growth 14.3 bp · C EV +1.53 (adj +0.71) on $17.27, P(profit) 0.6472, adj growth 6.7 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.7669, adj growth 2.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
