# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-08T23:23:10Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +31.61 | +7.84 | +30.25 | 0.755 | -28.50 | -44.69 | 68.17 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +22.98 | +11.44 | +21.00 | 0.642 | -35.18 | -52.46 | 101.77 |
| C best expression per thesis | 149.99 | +26.51 | +9.41 | +24.96 | 0.701 | -32.87 | -49.74 | 82.41 |
| R FUNDED research stakes | 12.00 | +1.95 | +1.31 | +1.02 | 0.657 | -5.91 | -5.91 | 0.00 |

## CHI @ NYI  ·  10000 joint draws  ·  398 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.622 / away 0.378

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CHI_win | p_overtime | goals | shots NYI/CHI | NYI/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NYI shot control · normal event (5-7) · decided (2+) | 0.144 | 0.74 | 0.26 | 0.00 | 6.0 | 32.8/21.0 | 18.7/27.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.68 | 0.32 | 0.00 | 6.04 | 27.5/26.9 | 24.0/23.2 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.48 | 5.92 | 33.3/21.5 | 18.4/30.0 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.096 | 0.75 | 0.25 | 0.00 | 9.28 | 34.9/22.7 | 18.4/26.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.50 | 0.50 | 0.48 | 5.93 | 27.6/27.0 | 23.7/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.68 | 0.32 | 0.00 | 9.41 | 29.3/28.5 | 23.5/22.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 10 | 0.155 | 0.140 | +0.049 | +0.034 | $7.75 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Kyle Palmieri: 1+ assists NO | 67 | 0.764 | 0.715 | +0.079 | +0.029 | $18.47 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Patrick Kane: 1+ assists NO | 59 | 0.722 | 0.633 | +0.115 | +0.026 | $17.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Casey Cizikas: 1+ goals YES | 11 | 0.140 | 0.130 | +0.023 | +0.013 | $3.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08CHINYI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (25.32 vs 0.76 bp); alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08CHINYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT08CHINYI-NYICCIZIKAS53-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CHI offense suppressed (<= 2 goals)
- **Kyle Palmieri: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no; why: higher confidence-adjusted growth (8.66 vs 1.17 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT08CHINYI-NYICCIZIKAS53-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NYI offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08CHINYI-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (6.26 vs 1.25 bp); relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLAST-26OCT08CHINYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT08CHINYI-NYICCIZIKAS53-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: CHI offense succeeds (4+ goals)
- **Casey Cizikas: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08CHINYI-7|yes; why: higher confidence-adjusted growth (3.70 vs 0.55 bp); despite a smaller raw edge (+0.023 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.891 vs 0.685); alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT08CHINYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3): highest fidelity KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4862): highest fidelity KXNHLAST-26OCT08CHINYI-CHIBBYRAM24-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:SUPPRESSED (p 0.3059): highest fidelity KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no (same contract)
- KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4862, phi -0.222)
- KXNHLAST-26OCT08CHINYI-NYIKPALMIERI21-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.4869, phi -0.203)
- KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3, phi -0.246)
- KXNHLGOAL-26OCT08CHINYI-NYICCIZIKAS53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3059, phi -0.151)

portfolios: A EV +6.90 (adj +3.23) on $37.50, P(profit) 0.5185, adj growth 28.9 bp · B EV +9.70 (adj +4.38) on $47.28, P(profit) 0.672, adj growth 38.5 bp · C EV +7.65 (adj +3.58) on $34.21, P(profit) 0.5624, adj growth 30.8 bp · R EV +0.92 (adj +0.63) on $2.00, P(profit) 0.155, adj growth 21.8 bp

## SJS @ STL  ·  10000 joint draws  ·  402 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.583 / away 0.417

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_SJS_win | p_overtime | goals | shots STL/SJS | STL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 6.03 | 26.5/26.3 | 23.3/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.46 | 5.94 | 26.5/26.3 | 22.9/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.58 | 0.42 | 0.00 | 9.34 | 28.1/27.9 | 22.5/21.4 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.088 | 0.68 | 0.33 | 0.00 | 6.07 | 31.3/21.0 | 18.4/26.7 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.57 | 0.43 | 0.47 | 5.93 | 31.8/21.4 | 18.3/28.3 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.061 | 0.68 | 0.32 | 0.00 | 9.3 | 33.4/22.6 | 18.3/25.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Philip Broberg: 1+ goals YES | 7 | 0.101 | 0.092 | +0.026 | +0.017 | $3.96 | FUNDED_RESEARCH | $1 | STL:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 70 | 0.789 | 0.740 | +0.074 | +0.025 | $18.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Pius Suter: 1+ goals YES | 14 | 0.176 | 0.166 | +0.028 | +0.018 | $4.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Dmitry Orlov: 1+ assists YES | 26 | 0.339 | 0.294 | +0.065 | +0.021 | $6.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-7|yes; why: higher confidence-adjusted growth (9.01 vs 0.39 bp); despite a smaller raw edge (+0.026 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.893 vs 0.69); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT08SJSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT08SJSTL-SJDORLOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: STL offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT08SJSTL-SJLCAGNONI42-1|no; why: higher confidence-adjusted growth (6.64 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT08SJSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT08SJSTL-SJDORLOV9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); failure: SJS offense succeeds (4+ goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-7|yes; why: higher confidence-adjusted growth (5.22 vs 0.39 bp); despite a smaller raw edge (+0.028 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.883 vs 0.69); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT08SJSTL-SJDORLOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: STL offense suppressed (<= 2 goals)
- **Dmitry Orlov: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08SJSTL-SJCGRAF51-1|yes; why: higher confidence-adjusted growth (4.77 vs 0.67 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT08SJSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:SUPPRESSED (p 0.4352): highest fidelity KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3496): highest fidelity KXNHLAST-26OCT08SJSTL-SJDORLOV9-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT08SJSTL-SJDORLOV9-1|yes (same contract)
- thesis STL:SUPPRESSED (p 0.3389): highest fidelity KXNHLAST-26OCT08SJSTL-STLAJIRICEK36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08SJSTL-STLAJIRICEK36-1|no (same contract)
- KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3389, phi -0.119)
- KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3496, phi -0.192)
- KXNHLGOAL-26OCT08SJSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3389, phi -0.182)
- KXNHLAST-26OCT08SJSTL-SJDORLOV9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4352, phi -0.288)

portfolios: A EV +5.51 (adj +1.45) on $37.50, P(profit) 0.6051, adj growth 12.7 bp · B EV +5.78 (adj +2.61) on $34.08, P(profit) 0.4298, adj growth 23.0 bp · C EV +5.51 (adj +1.53) on $45.05, P(profit) 0.5601, adj growth 13.6 bp · R EV +0.35 (adj +0.23) on $1.00, P(profit) 0.1005, adj growth 7.9 bp

## COL @ CGY  ·  10000 joint draws  ·  418 bet sides mapped, 35 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.324 / away 0.676

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_COL_win | p_overtime | goals | shots CGY/COL | CGY/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.131 | 0.36 | 0.64 | 0.00 | 6.0 | 22.9/35.5 | 30.9/20.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.48 | 0.52 | 0.50 | 5.91 | 23.1/35.5 | 32.0/19.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.42 | 0.58 | 0.00 | 5.97 | 28.6/29.5 | 25.5/25.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.50 | 0.50 | 0.46 | 5.94 | 28.9/29.7 | 26.5/25.6 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.084 | 0.36 | 0.64 | 0.00 | 9.28 | 24.2/37.2 | 29.7/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.41 | 0.59 | 0.00 | 9.24 | 30.1/31.2 | 24.5/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 1+ goals NO | 56 | 0.644 | 0.622 | +0.067 | +0.044 | $14.18 | FUNDED_RESEARCH | $4 | COL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Martin Necas: 1+ goals NO | 63 | 0.701 | 0.682 | +0.054 | +0.035 | $14.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Scott Wedgewood: 22+ saves YES | 51 | 0.588 | 0.546 | +0.060 | +0.019 | $9.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:NET_HIGH_VOLUME | DIRECT (0.95) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (17.82 vs 12.58 bp); despite a smaller raw edge (+0.067 vs +0.234/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSAVE-26OCT08COLCGY-COLSWEDGEWOOD41-22|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: COL offense succeeds (4+ goals)
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no; why: Player prop expression KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no selected over player prop KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.94 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSAVE-26OCT08COLCGY-COLSWEDGEWOOD41-22|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: COL offense succeeds (4+ goals)
- **Scott Wedgewood: 22+ saves YES** — thesis: COL net faces heavy volume (33+ shots; CGY pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: COL net faces light volume (<= 25 shots; CGY suppressed)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.3484): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no — Player prop expression KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no selected over player prop KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.94 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)
- thesis CGY:WINS_BY_2PLUS (p 0.221): highest fidelity KXNHLSPREAD-26OCT08COLCGY-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.4375): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4289, phi -0.263)
- KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4289, phi -0.228)
- KXNHLSAVE-26OCT08COLCGY-COLSWEDGEWOOD41-22|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family MIXED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:NET_LOW_VOLUME (p 0.4694, phi -0.728)
- override: Player prop expression KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no selected over player prop KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.94 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +14.88 (adj +2.27) on $37.50, P(profit) 0.7613, adj growth 18.7 bp · B EV +3.96 (adj +2.22) on $38.22, P(profit) 0.715, adj growth 20.6 bp · C EV +10.56 (adj +3.41) on $44.52, P(profit) 0.7229, adj growth 30.0 bp · R EV +0.46 (adj +0.31) on $4.00, P(profit) 0.644, adj growth 11.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08COLCGY-COL|no == KXNHLGAME-26OCT08COLCGY-CGY|yes

## TOR @ VGK  ·  10000 joint draws  ·  448 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.601 / away 0.400

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TOR_win | p_overtime | goals | shots VGK/TOR | VGK/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.153 | 0.76 | 0.24 | 0.00 | 5.99 | 34.0/21.4 | 19.1/29.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.59 | 0.41 | 0.48 | 5.92 | 34.3/21.7 | 18.7/30.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.68 | 0.32 | 0.00 | 6.04 | 28.4/27.7 | 25.0/24.0 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.105 | 0.77 | 0.23 | 0.00 | 9.28 | 36.0/23.0 | 18.9/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.47 | 0.49 | 5.96 | 28.4/27.7 | 24.5/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.73 | 0.27 | 0.00 | 9.35 | 30.1/29.2 | 24.6/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 6 | 0.088 | 0.080 | +0.024 | +0.016 | $3.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 81 | 0.858 | 0.845 | +0.037 | +0.024 | $18.91 | FUNDED_RESEARCH | $5 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Braeden Bowman: 1+ goals YES | 17 | 0.207 | 0.197 | +0.027 | +0.017 | $4.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Marc Gatcomb: 1+ goals YES | 12 | 0.152 | 0.142 | +0.025 | +0.014 | $3.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (8.88 vs 3.56 bp); despite a smaller raw edge (+0.024 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT08TORVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT08TORVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: VGK offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no; why: higher confidence-adjusted growth (8.50 vs 4.81 bp); despite a smaller raw edge (+0.037 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT08TORVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT08TORVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: TOR offense succeeds (4+ goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (4.06 vs 3.56 bp); despite a smaller raw edge (+0.027 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT08TORVGK-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT08TORVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi 0.021); failure: VGK offense suppressed (<= 2 goals)
- **Marc Gatcomb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (3.91 vs 3.56 bp); despite a smaller raw edge (+0.025 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT08TORVGK-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT08TORVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.021); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.15, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:SUPPRESSED (p 0.5076): highest fidelity KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.5093): highest fidelity KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2885, phi -0.115)
- KXNHLGOAL-26OCT08TORVGK-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2861, phi -0.172)
- KXNHLGOAL-26OCT08TORVGK-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2885, phi -0.184)
- KXNHLGOAL-26OCT08TORVGK-VGKMGATCOMB17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2885, phi -0.167)

portfolios: A EV +4.32 (adj +0.89) on $37.50, P(profit) 0.7078, adj growth 7.9 bp · B EV +3.54 (adj +2.23) on $30.43, P(profit) 0.3469, adj growth 19.7 bp · C EV +2.79 (adj +0.89) on $26.21, P(profit) 0.3154, adj growth 8.0 bp · R EV +0.22 (adj +0.14) on $5.00, P(profit) 0.8577, adj growth 5.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
