# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-20T15:48:10Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +37.02 | +13.66 | +28.33 | 0.750 | -22.71 | -35.00 | 122.50 |
| B thesis-diversified (joint) ← optimiser card | 148.28 | +26.97 | +14.34 | +23.63 | 0.740 | -21.24 | -32.28 | 135.60 |
| C best expression per thesis | 148.36 | +31.33 | +14.50 | +26.60 | 0.723 | -28.28 | -41.55 | 133.07 |
| R FUNDED research stakes | 28.00 | +3.89 | +2.02 | +2.62 | 0.648 | -6.08 | -8.42 | 0.00 |

## SJS @ MTL  ·  10000 joint draws  ·  394 bet sides mapped, 13 +EV candidates, 4 on card


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
| Mason Marchment: 1+ goals YES | 18 | 0.229 | 0.215 | +0.038 | +0.025 | $2.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ goals NO | 54 | 0.605 | 0.587 | +0.047 | +0.030 | $5.34 | FUNDED_RESEARCH | $2 | MTL:SUPPRESSED | DIRECT (0.79) | EVIDENCE_STRONGER | D |
| Zachary Bolduc: 1+ goals NO | 76 | 0.804 | 0.789 | +0.032 | +0.017 | $6.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Full Game: Over 5.5 goals scored NO | 37 | 0.434 | 0.400 | +0.048 | +0.013 | $1.54 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20SJMTL-MTL2|no; why: higher confidence-adjusted growth (8.62 vs 1.40 bp); despite a smaller raw edge (+0.038 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT20SJMTL-MTLZBOLDUC76-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTOTAL-26OCT20SJMTL-6|no: INTENTIONAL_DIVERSIFIER (phi -0.157); failure: SJS offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20SJMTL-4|no; why: higher confidence-adjusted growth (7.93 vs 3.84 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.009 vs 0.354); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT20SJMTL-MTLZBOLDUC76-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLTOTAL-26OCT20SJMTL-6|no: REINFORCING (phi 0.211); failure: MTL offense succeeds (4+ goals)
- **Zachary Bolduc: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no has the higher standalone adjusted growth (7.93 vs 3.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLTOTAL-26OCT20SJMTL-6|no: REINFORCING (phi 0.153); failure: MTL offense succeeds (4+ goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT20SJMTL-4|no; why: Broad expression KXNHLTOTAL-26OCT20SJMTL-6|no selected over broad KXNHLTOTAL-26OCT20SJMTL-4|no because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.61 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.157); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: REINFORCING (phi 0.211); KXNHLGOAL-26OCT20SJMTL-MTLZBOLDUC76-1|no: REINFORCING (phi 0.153); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:OFFENSE_4PLUS (p 0.3131): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3345): highest fidelity KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:LOW_EVENT (p 0.2366): highest fidelity KXNHLTOTAL-26OCT20SJMTL-7|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3|no — Broad expression KXNHLTOTAL-26OCT20SJMTL-6|no selected over broad KXNHLTOTAL-26OCT20SJMTL-4|no because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.61 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4723, phi -0.228)
- KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4556, phi -0.273)
- KXNHLGOAL-26OCT20SJMTL-MTLZBOLDUC76-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4556, phi -0.199)
- KXNHLTOTAL-26OCT20SJMTL-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4556, phi -0.535)
- override: Broad expression KXNHLTOTAL-26OCT20SJMTL-6|no selected over broad KXNHLTOTAL-26OCT20SJMTL-4|no because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.61 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.66 (adj +0.42) on $14.10, P(profit) 0.4481, adj growth 3.5 bp · B EV +1.47 (adj +0.85) on $15.81, P(profit) 0.5871, adj growth 8.1 bp · C EV +2.28 (adj +1.29) on $15.33, P(profit) 0.7207, adj growth 11.9 bp · R EV +0.29 (adj +0.14) on $3.00, P(profit) 0.6047, adj growth 5.2 bp

## COL @ NJD  ·  10000 joint draws  ·  462 bet sides mapped, 10 +EV candidates, 4 on card


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
| Fedor Svechkov: 1+ goals YES | 8 | 0.116 | 0.104 | +0.030 | +0.019 | $1.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ assists NO | 44 | 0.601 | 0.490 | +0.144 | +0.033 | $6.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Parker Kelly: 1+ goals YES | 9 | 0.125 | 0.115 | +0.029 | +0.019 | $1.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 65 | 0.704 | 0.689 | +0.038 | +0.023 | $6.77 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Fedor Svechkov: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20COLNJ-NJ3|no; why: higher confidence-adjusted growth (9.95 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0002 below the 0.010/contract floor; relationships: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT20COLNJ-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: COL offense suppressed (<= 2 goals)
- **Cale Makar: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT20COLNJ-COLCMAKAR8-2|no; why: higher confidence-adjusted growth (9.38 vs 1.52 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT20COLNJ-COLPKELLY17-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: COL offense succeeds (4+ goals)
- **Parker Kelly: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20COLNJ-NJ3|no; why: higher confidence-adjusted growth (9.33 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0002 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: COL offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT20COLNJ-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis COL:SUPPRESSED (p 0.3958): highest fidelity KXNHLPTS-26OCT20COLNJ-COLCMAKAR8-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4184): highest fidelity KXNHLAST-26OCT20COLNJ-NJERODRIGUES17-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis COL:OFFENSE_4PLUS (p 0.3807): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3958, phi -0.146)
- KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.1 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3807, phi -0.28)
- KXNHLGOAL-26OCT20COLNJ-COLPKELLY17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3958, phi -0.153)
- KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.361, phi -0.245)
- override: Player prop expression KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.22 (adj +0.63) on $14.10, P(profit) 0.6932, adj growth 6.1 bp · B EV +3.60 (adj +1.48) on $16.79, P(profit) 0.5626, adj growth 14.1 bp · C EV +5.00 (adj +1.14) on $17.53, P(profit) 0.6011, adj growth 10.6 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.7039, adj growth 2.6 bp

## ANA @ NYI  ·  10000 joint draws  ·  392 bet sides mapped, 3 +EV candidates, 3 on card


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
| A.J. Greer: 1+ goals YES | 12 | 0.212 | 0.188 | +0.085 | +0.060 | $5.67 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 10 | 0.129 | 0.119 | +0.023 | +0.013 | $1.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Jackson LaCombe: 1+ goals YES | 11 | 0.137 | 0.129 | +0.020 | +0.012 | $1.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20ANANYI-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (68.65 vs 0.07 bp); alternative not eligible: confidence-adjusted EV +0.0022 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20ANANYI-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes has the higher standalone adjusted growth (68.65 vs 3.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20ANANYI-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: ANA offense suppressed (<= 2 goals)
- **Jackson LaCombe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes has the higher standalone adjusted growth (68.65 vs 2.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3377): highest fidelity KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes (same contract)
- KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4388, phi -0.221)
- KXNHLGOAL-26OCT20ANANYI-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4388, phi -0.152)
- KXNHLGOAL-26OCT20ANANYI-ANAJLACOMBE2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4388, phi -0.164)

portfolios: A EV +4.40 (adj +3.05) on $9.00, P(profit) 0.4096, adj growth 28.6 bp · B EV +4.25 (adj +2.97) on $8.15, P(profit) 0.4096, adj growth 27.9 bp · C EV +5.90 (adj +4.21) on $8.87, P(profit) 0.2121, adj growth 38.1 bp · R EV +1.33 (adj +0.95) on $2.00, P(profit) 0.2121, adj growth 34.7 bp

## LAK @ WSH  ·  10000 joint draws  ·  426 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_LAK_win | p_overtime | goals | shots WSH/LAK | WSH/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.63 | 0.37 | 0.00 | 5.99 | 27.6/27.8 | 24.7/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.47 | 5.87 | 27.2/27.5 | 24.2/23.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.078 | 0.56 | 0.44 | 0.00 | 5.95 | 22.0/32.3 | 28.8/18.3 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.51 | 0.49 | 0.46 | 5.83 | 22.2/33.0 | 29.5/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.66 | 0.34 | 0.00 | 9.08 | 29.0/29.3 | 24.0/22.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.61 | 0.39 | 0.00 | 3.51 | 26.1/26.2 | 24.8/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.238 | 0.221 | +0.048 | +0.031 | $3.30 | FUNDED_RESEARCH | $1 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 4 | 0.062 | 0.055 | +0.019 | +0.013 | $1.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 53 | 0.643 | 0.560 | +0.095 | +0.012 | $3.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Ryan Leonard: 1+ assists YES | 31 | 0.372 | 0.336 | +0.047 | +0.011 | $1.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (13.10 vs 1.24 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20LAWSH-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.056); failure: WSH offense suppressed (<= 2 goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT20LAWSH-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (8.18 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.043/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.101); KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: LAK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT20LAWSH-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (1.33 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT20LAWSH-LAJEDMUNDSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.101); KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: LAK offense succeeds (4+ goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (13.10 vs 1.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.056); they share one thesis budget; relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26OCT20LAWSH-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis WSH:OFFENSE_4PLUS (p 0.4019): highest fidelity KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.4984): highest fidelity KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.2881): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3783, phi -0.254)
- KXNHLGOAL-26OCT20LAWSH-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4984, phi -0.13)
- KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.8 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2881, phi -0.285)
- KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3783, phi -0.274)

portfolios: A EV +2.95 (adj +1.21) on $14.10, P(profit) 0.4504, adj growth 11.2 bp · B EV +2.08 (adj +0.98) on $8.87, P(profit) 0.4504, adj growth 9.3 bp · C EV +2.00 (adj +0.93) on $9.20, P(profit) 0.2379, adj growth 8.5 bp · R EV +0.25 (adj +0.16) on $1.00, P(profit) 0.2379, adj growth 6.0 bp

## TOR @ CBJ  ·  10000 joint draws  ·  390 bet sides mapped, 14 +EV candidates, 4 on card


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
| Gavin McKenna: 1+ goals NO | 80 | 0.846 | 0.834 | +0.035 | +0.022 | $7.58 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 19 | 0.233 | 0.220 | +0.032 | +0.019 | $2.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Full Game: Over 5.5 goals scored NO | 40 | 0.478 | 0.436 | +0.061 | +0.020 | $2.97 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Toronto over 3.5 goals scored NO | 65 | 0.724 | 0.682 | +0.058 | +0.016 | $1.30 | FUNDED_RESEARCH | $1 | TOR:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20TORCBJ-6|no; why: higher confidence-adjusted growth (7.21 vs 3.43 bp); despite a smaller raw edge (+0.035 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.992 vs 0.75); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLTOTAL-26OCT20TORCBJ-6|no: MOSTLY_INDEPENDENT (phi 0.128); KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no: REINFORCING (phi 0.2); failure: TOR offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20TORCBJ-TOR3|no; why: higher confidence-adjusted growth (4.75 vs 0.96 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLTOTAL-26OCT20TORCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.156); KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no: MOSTLY_INDEPENDENT (phi 0.025); failure: CBJ offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT20TORCBJ-5|no; why: higher confidence-adjusted growth (3.43 vs 2.96 bp); wins across more scripts (relative breadth 0.75 vs 0.382); relationships: KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.128); KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.156); KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no: REINFORCING (phi 0.453); failure: CBJ offense succeeds (4+ goals)
- **Toronto over 3.5 goals scored NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no selected over player prop KXNHLAST-26OCT20TORCBJ-TORKMARCHENKO86-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.85 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: REINFORCING (phi 0.2); KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLTOTAL-26OCT20TORCBJ-6|no: REINFORCING (phi 0.453); failure: TOR offense succeeds (4+ goals)

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:SCORES_FIRST (p 0.4389): highest fidelity KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.5139): highest fidelity KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no — Broad expression KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no selected over player prop KXNHLAST-26OCT20TORCBJ-TORKMARCHENKO86-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.85 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CBJ:OFFENSE_4PLUS (p 0.4406): highest fidelity KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes (same contract)
- KXNHLGOAL-26OCT20TORCBJ-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2668, phi -0.201)
- KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3382, phi -0.225)
- KXNHLTOTAL-26OCT20TORCBJ-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4406, phi -0.558)
- KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2668, phi -0.977)
- override: Broad expression KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4|no selected over player prop KXNHLAST-26OCT20TORCBJ-TORKMARCHENKO86-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.85 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.32 (adj +2.58) on $14.10, P(profit) 0.5088, adj growth 19.9 bp · B EV +1.25 (adj +0.60) on $14.19, P(profit) 0.5613, adj growth 5.7 bp · C EV +2.04 (adj +0.99) on $21.93, P(profit) 0.5613, adj growth 9.1 bp · R EV +0.32 (adj +0.13) on $4.00, P(profit) 0.4274, adj growth 4.7 bp

## WPG @ STL  ·  10000 joint draws  ·  434 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_WPG_win | p_overtime | goals | shots STL/WPG | STL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.134 | 0.65 | 0.35 | 0.00 | 6.04 | 26.5/26.5 | 23.5/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.46 | 5.91 | 26.4/26.4 | 23.2/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.64 | 0.36 | 0.00 | 9.24 | 28.0/28.0 | 22.9/21.0 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.077 | 0.68 | 0.32 | 0.00 | 6.03 | 30.8/20.9 | 18.3/26.2 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.58 | 0.42 | 0.47 | 5.89 | 31.3/21.2 | 18.1/28.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.059 | 0.57 | 0.43 | 0.00 | 6.01 | 21.1/31.1 | 27.8/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Morgan Barron: 1+ goals YES | 6 | 0.124 | 0.107 | +0.060 | +0.043 | $3.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Dalibor Dvorsky: 1+ goals NO | 82 | 0.857 | 0.846 | +0.026 | +0.016 | $7.58 | FUNDED_RESEARCH | $2 | STL:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 25 | 0.293 | 0.280 | +0.030 | +0.017 | $2.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 15 | 0.183 | 0.172 | +0.024 | +0.013 | $1.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (62.89 vs 0.09 bp); alternative not eligible: confidence-adjusted EV +0.0027 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT20WPGSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: WPG offense suppressed (<= 2 goals)
- **Dalibor Dvorsky: 1+ goals NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20WPGSTL-STLPBUCHNEVICH89-1|no; why: higher confidence-adjusted growth (3.91 vs 0.23 bp); despite a smaller raw edge (+0.026 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT20WPGSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: STL offense succeeds (4+ goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-STLPSUTER22-1|yes; why: higher confidence-adjusted growth (3.25 vs 2.95 bp); relationships: KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT20WPGSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (3.25 vs 2.95 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.019); they share one thesis budget; relationships: KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis STL:OFFENSE_4PLUS (p 0.4452): highest fidelity KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3123): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis STL:SUPPRESSED (p 0.3423): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4685, phi -0.177)
- KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4452, phi -0.175)
- KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3423, phi -0.253)
- KXNHLGOAL-26OCT20WPGSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3423, phi -0.197)

portfolios: A EV +4.33 (adj +2.69) on $14.10, P(profit) 0.443, adj growth 25.1 bp · B EV +3.98 (adj +2.74) on $14.57, P(profit) 0.4475, adj growth 25.6 bp · C EV +0.38 (adj +0.21) on $3.31, P(profit) 0.2935, adj growth 2.0 bp · R EV +0.06 (adj +0.04) on $2.00, P(profit) 0.8565, adj growth 1.5 bp

## BOS @ DAL  ·  10000 joint draws  ·  420 bet sides mapped, 9 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_BOS_win | p_overtime | goals | shots DAL/BOS | DAL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.53 | 0.47 | 0.00 | 6.0 | 26.4/25.9 | 22.5/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.48 | 5.98 | 26.7/26.2 | 22.9/23.3 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.102 | 0.60 | 0.40 | 0.00 | 6.02 | 31.6/20.8 | 17.8/27.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.52 | 0.48 | 0.48 | 5.88 | 31.7/20.8 | 17.7/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.54 | 0.46 | 0.00 | 9.26 | 28.3/27.9 | 22.1/22.2 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.066 | 0.60 | 0.40 | 0.00 | 9.13 | 33.2/22.0 | 17.0/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Morgan Geekie: 1+ goals YES | 25 | 0.299 | 0.285 | +0.036 | +0.022 | $2.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 68 | 0.730 | 0.715 | +0.035 | +0.020 | $5.89 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 75 | 0.810 | 0.777 | +0.046 | +0.014 | $3.32 | FUNDED_RESEARCH | $1 | BOS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Morgan Geekie: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes; why: higher confidence-adjusted growth (5.61 vs 4.97 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.913 vs 0.358); relationships: KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.131); failure: BOS offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20BOSDAL-DAL3|no; why: higher confidence-adjusted growth (3.99 vs 2.44 bp); despite a smaller raw edge (+0.035 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.146); failure: DAL offense succeeds (4+ goals)
- **Dallas wins by over 2.5 goals NO** — thesis: BOS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes; why: Broad expression KXNHLSPREAD-26OCT20BOSDAL-DAL3|no selected over player prop KXNHLAST-26OCT20BOSDAL-DALTSEGUIN91-1|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.146); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.3577): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2541): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — Broad expression KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes selected over broad KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes because adjusted EV is 0.4 pts higher while thesis capture is 0.71 vs 0.29 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis BOS:WINS (p 0.4741): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4174, phi -0.26)
- KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3962, phi -0.24)
- KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3031, phi -0.735)
- override: Broad expression KXNHLSPREAD-26OCT20BOSDAL-DAL3|no selected over player prop KXNHLAST-26OCT20BOSDAL-DALTSEGUIN91-1|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes selected over broad KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes because adjusted EV is 0.4 pts higher while thesis capture is 0.71 vs 0.29 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.45 (adj +0.39) on $14.10, P(profit) 0.5337, adj growth 3.5 bp · B EV +0.83 (adj +0.44) on $11.69, P(profit) 0.7025, adj growth 4.2 bp · C EV +1.62 (adj +0.83) on $14.90, P(profit) 0.2654, adj growth 7.6 bp · R EV +0.16 (adj +0.08) on $3.00, P(profit) 0.6163, adj growth 2.8 bp

## MIN @ EDM  ·  10000 joint draws  ·  452 bet sides mapped, 7 +EV candidates, 4 on card


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
| Alex Formenton: 1+ goals YES | 14 | 0.192 | 0.176 | +0.043 | +0.028 | $2.96 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ assists NO | 39 | 0.483 | 0.434 | +0.076 | +0.027 | $4.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.69) | EVIDENCE_MIXED | D |
| Zach Hyman: 1+ goals YES | 32 | 0.370 | 0.355 | +0.035 | +0.019 | $3.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 68 | 0.781 | 0.712 | +0.086 | +0.017 | $7.58 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20MINEDM-EDM6|yes; why: higher confidence-adjusted growth (13.04 vs 4.07 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.846 vs 0.309); relationships: KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.045); failure: EDM offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no; why: higher confidence-adjusted growth (6.79 vs 2.57 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.023); failure: MIN offense succeeds (4+ goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (13.04 vs 3.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.178); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (2.96 vs 0.56 bp); alternative not eligible: confidence-adjusted EV +0.0076 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.178); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5018): highest fidelity KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4289): highest fidelity KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3227): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM6|yes [FRAGILE], best adjusted EV KXNHLTEAMTOTAL-26OCT20MINEDM-EDM6|yes (same contract)
- KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2953, phi -0.184)
- KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 31% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3548, phi -0.318)
- KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2953, phi -0.252)
- KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.6 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5018, phi -0.336)

portfolios: A EV +2.12 (adj +0.89) on $14.10, P(profit) 0.5079, adj growth 8.5 bp · B EV +2.95 (adj +1.22) on $18.18, P(profit) 0.6574, adj growth 11.6 bp · C EV +4.74 (adj +1.81) on $25.14, P(profit) 0.5611, adj growth 16.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ SEA  ·  10000 joint draws  ·  396 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_DET_win | p_overtime | goals | shots SEA/DET | SEA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.64 | 0.36 | 0.00 | 6.05 | 27.8/28.2 | 25.3/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.46 | 5.92 | 27.8/28.1 | 24.8/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.64 | 0.36 | 0.00 | 9.28 | 29.3/29.7 | 24.4/22.1 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.093 | 0.56 | 0.44 | 0.00 | 5.99 | 22.1/33.3 | 30.0/18.5 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.49 | 0.51 | 0.47 | 5.79 | 22.3/33.8 | 30.7/19.2 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.055 | 0.56 | 0.44 | 0.00 | 9.17 | 24.0/35.4 | 29.2/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Winterton: 1+ goals YES | 12 | 0.165 | 0.152 | +0.037 | +0.025 | $2.37 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 11 | 0.153 | 0.141 | +0.036 | +0.024 | $2.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Shane Wright: 1+ goals YES | 18 | 0.223 | 0.211 | +0.032 | +0.020 | $2.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Detroit wins by over 1.5 goals NO | 71 | 0.783 | 0.744 | +0.059 | +0.020 | $4.46 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20DETSEA-SEASWRIGHT51-1|yes; why: higher confidence-adjusted growth (12.02 vs 5.83 bp); relationships: KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT20DETSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLSPREAD-26OCT20DETSEA-DET2|no: MOSTLY_INDEPENDENT (phi 0.1); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20DETSEA-SEASWRIGHT51-1|yes; why: higher confidence-adjusted growth (11.81 vs 5.83 bp); relationships: KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT20DETSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT20DETSEA-DET2|no: MOSTLY_INDEPENDENT (phi 0.087); failure: SEA offense suppressed (<= 2 goals)
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20DETSEA-DET2|no; why: higher confidence-adjusted growth (5.83 vs 4.27 bp); despite a smaller raw edge (+0.032 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT20DETSEA-DET2|no: MOSTLY_INDEPENDENT (phi 0.137); failure: SEA offense suppressed (<= 2 goals)
- **Detroit wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20DETSEA-DET3|no; why: Broad expression KXNHLSPREAD-26OCT20DETSEA-DET2|no selected over broad KXNHLTEAMTOTAL-26OCT20DETSEA-DET5|no because adjusted EV is 0.9 pts higher while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.1); KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.087); KXNHLGOAL-26OCT20DETSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.137); failure: DET wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4353): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20DETSEA-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.3551): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20DETSEA-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.5826): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no (same contract)
- KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3412, phi -0.181)
- KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3412, phi -0.172)
- KXNHLGOAL-26OCT20DETSEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3412, phi -0.215)
- KXNHLSPREAD-26OCT20DETSEA-DET2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2168, phi -1.0)
- override: Broad expression KXNHLSPREAD-26OCT20DETSEA-DET2|no selected over broad KXNHLTEAMTOTAL-26OCT20DETSEA-DET5|no because adjusted EV is 0.9 pts higher while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.18 (adj +0.34) on $14.10, P(profit) 0.4541, adj growth 3.2 bp · B EV +2.09 (adj +1.26) on $11.12, P(profit) 0.4273, adj growth 12.0 bp · C EV +1.36 (adj +0.62) on $13.31, P(profit) 0.808, adj growth 5.7 bp · R EV +0.16 (adj +0.05) on $2.00, P(profit) 0.7832, adj growth 2.1 bp

## CAR @ VAN  ·  10000 joint draws  ·  404 bet sides mapped, 27 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CAR_win | p_overtime | goals | shots VAN/CAR | VAN/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.171 | 0.37 | 0.63 | 0.00 | 6.02 | 20.9/34.4 | 30.0/18.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.145 | 0.47 | 0.53 | 0.45 | 5.94 | 21.3/34.7 | 31.2/18.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.132 | 0.37 | 0.63 | 0.00 | 9.36 | 22.2/35.6 | 27.9/17.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.083 | 0.46 | 0.54 | 0.00 | 6.02 | 26.6/27.8 | 24.1/23.0 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.074 | 0.39 | 0.61 | 0.00 | 3.5 | 19.9/32.6 | 30.3/18.3 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.068 | 0.46 | 0.54 | 0.47 | 2.86 | 19.7/32.8 | 31.3/18.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 12 | 0.173 | 0.156 | +0.046 | +0.029 | $2.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 48 | 0.656 | 0.538 | +0.159 | +0.041 | $5.42 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 1.5 goals scored YES | 71 | 0.799 | 0.752 | +0.075 | +0.028 | $4.85 | FUNDED_RESEARCH | $2 | VAN:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 63 | 0.685 | 0.667 | +0.038 | +0.021 | $4.51 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes has the higher standalone adjusted growth (25.77 vs 15.91 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.190); relationships: KXNHLSPREAD-26OCT20CARVAN-CAR2|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes: REINFORCING (phi 0.168); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: VAN offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes has the higher standalone adjusted growth (25.77 vs 14.72 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.317); relationships: KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.132); KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes: REINFORCING (phi 0.431); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: REINFORCING (phi 0.166); failure: CAR wins by 2+
- **Vancouver over 1.5 goals scored YES** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes has the higher standalone adjusted growth (25.77 vs 8.40 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.250); relationships: KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes: REINFORCING (phi 0.168); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.431); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: VAN offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-CAR2|no; why: KXNHLTEAMTOTAL-26OCT20CARVAN-CAR2|no has the higher standalone adjusted growth (16.68 vs 4.25 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.203); relationships: KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.166); KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3646): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.4398): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.2337): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- KXNHLGOAL-26OCT20CARVAN-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4241, phi -0.194)
- KXNHLSPREAD-26OCT20CARVAN-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 18.1 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3436, phi -1.0)
- KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis VAN:SUPPRESSED (p 0.4241, phi -0.584)
- KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4561, phi -0.236)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT20CARVAN-CAR3|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes kept

portfolios: A EV +4.56 (adj +0.92) on $14.10, P(profit) 0.5461, adj growth 8.4 bp · B EV +3.36 (adj +1.32) on $17.17, P(profit) 0.6855, adj growth 12.5 bp · C EV +4.92 (adj +2.08) on $6.98, P(profit) 0.3185, adj growth 19.1 bp · R EV +0.96 (adj +0.31) on $6.00, P(profit) 0.6491, adj growth 11.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT20CARVAN-VAN|yes == KXNHLGAME-26OCT20CARVAN-CAR|no

## TBL @ VGK  ·  10000 joint draws  ·  414 bet sides mapped, 7 +EV candidates, 3 on card


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
| Tampa Bay wins by over 1.5 goals NO | 71 | 0.792 | 0.748 | +0.067 | +0.024 | $7.05 | FUNDED_RESEARCH | $2 | VGK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Brett Howden: 1+ goals YES | 19 | 0.236 | 0.221 | +0.035 | +0.020 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 64 | 0.684 | 0.671 | +0.028 | +0.015 | $2.77 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: VGK wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no; why: higher confidence-adjusted growth (6.32 vs 3.31 bp); wins across more scripts (relative breadth 0.98 vs 0.61); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: REINFORCING (phi 0.188); failure: TBL wins by 2+
- **Brett Howden: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT20TBVGK-TB2|no has the higher standalone adjusted growth (6.32 vs 5.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.147); they share one thesis budget; relationships: KXNHLSPREAD-26OCT20TBVGK-TB2|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.024); failure: VGK offense suppressed (<= 2 goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.82 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT20TBVGK-TB2|no: REINFORCING (phi 0.188); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis VGK:WINS (p 0.5876): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.4248): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis TBL:SUPPRESSED (p 0.4817): highest fidelity KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no — Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.82 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLSPREAD-26OCT20TBVGK-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2083, phi -1.0)
- KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3512, phi -0.217)
- KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3045, phi -0.258)
- override: Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.82 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.83 (adj +0.54) on $14.10, P(profit) 0.4687, adj growth 4.6 bp · B EV +1.11 (adj +0.48) on $11.74, P(profit) 0.6459, adj growth 4.6 bp · C EV +1.10 (adj +0.39) on $11.86, P(profit) 0.7917, adj growth 3.7 bp · R EV +0.23 (adj +0.09) on $3.00, P(profit) 0.5772, adj growth 3.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
