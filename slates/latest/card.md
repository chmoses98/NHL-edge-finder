# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T00:42:17Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 91.42 | +20.28 | +8.21 | +4.30 | 0.571 | -47.01 | -62.14 | 63.73 |
| B thesis-diversified (joint) ← optimiser card | 64.83 | +12.19 | +6.11 | +8.35 | 0.502 | -26.69 | -43.13 | 53.14 |
| C best expression per thesis | 39.16 | +5.15 | +1.25 | +0.08 | 0.595 | -15.61 | -15.61 | 11.33 |
| R FUNDED research stakes | 7.00 | +1.02 | +0.66 | -0.84 | 0.162 | -7.00 | -7.00 | 0.00 |

## SJS @ LAK  ·  10000 joint draws  ·  488 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.597 / away 0.403

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_SJS_win | p_overtime | goals | shots LAK/SJS | LAK/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.63 | 0.37 | 0.00 | 5.98 | 27.9/27.4 | 24.4/23.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.108 | 0.67 | 0.33 | 0.00 | 6.0 | 33.4/22.2 | 19.5/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.47 | 5.9 | 28.1/27.8 | 24.6/24.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.59 | 0.41 | 0.51 | 5.83 | 33.2/22.2 | 19.2/29.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.63 | 0.37 | 0.00 | 9.23 | 29.3/28.8 | 23.8/22.4 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.064 | 0.71 | 0.29 | 0.00 | 9.13 | 34.7/22.9 | 18.4/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 1+ goals NO | 80 | 0.852 | 0.838 | +0.041 | +0.027 | $17.60 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.080 | 0.069 | +0.027 | +0.016 | $3.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 65 | 0.732 | 0.686 | +0.067 | +0.020 | $12.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 41 | 0.554 | 0.442 | +0.127 | +0.015 | $7.49 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.75) | CALIBRATION_WARNING | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no; why: higher confidence-adjusted growth (10.32 vs 8.12 bp); despite a smaller raw edge (+0.041 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04SJLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV04SJLA-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.107); KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: SJS offense succeeds (4+ goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV04SJLA-LAJEDMUNDSON6-1|yes; why: higher confidence-adjusted growth (10.28 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV04SJLA-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.074); failure: LAK offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no; why: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no has the higher standalone adjusted growth (8.12 vs 4.06 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.064); relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26NOV04SJLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: SJS offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-LAEGUSTAFSSON64-1|no; why: higher confidence-adjusted growth (2.10 vs 0.79 bp); evidence CALIBRATION_WARNING vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV04SJLA-LAJEDMUNDSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.074); KXNHLAST-26NOV04SJLA-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SJS:SUPPRESSED (p 0.4784): highest fidelity KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3045): highest fidelity KXNHLGOAL-26NOV04SJLA-SJKSHERWOOD44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04SJLA-SJKSHERWOOD44-1|yes (same contract)
- thesis LAK:SUPPRESSED (p 0.359): highest fidelity KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no (same contract)
- KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3045, phi -0.17)
- KXNHLGOAL-26NOV04SJLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.359, phi -0.133)
- KXNHLAST-26NOV04SJLA-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3045, phi -0.249)
- KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4321, phi -0.285)

portfolios: A EV +9.85 (adj +1.60) on $50.00, P(profit) 0.6097, adj growth 13.1 bp · B EV +6.15 (adj +2.27) on $41.04, P(profit) 0.4114, adj growth 20.1 bp · C EV +5.15 (adj +1.25) on $39.16, P(profit) 0.595, adj growth 11.3 bp · R EV +0.25 (adj +0.16) on $5.00, P(profit) 0.8522, adj growth 6.2 bp

## CGY @ SEA  ·  10000 joint draws  ·  446 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.541 / away 0.459

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.64 | 0.36 | 0.00 | 6.03 | 28.2/28.4 | 25.5/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.44 | 5.86 | 28.4/28.3 | 25.2/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.67 | 0.34 | 0.00 | 9.45 | 29.9/30.0 | 24.9/22.5 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.071 | 0.59 | 0.41 | 0.00 | 6.09 | 22.9/34.1 | 30.8/19.1 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.068 | 0.70 | 0.30 | 0.00 | 6.0 | 33.2/22.8 | 20.3/28.3 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.058 | 0.51 | 0.49 | 0.50 | 5.92 | 23.0/34.0 | 30.7/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jani Nyman: 1+ goals YES | 11 | 0.162 | 0.146 | +0.045 | +0.029 | $7.42 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 18 | 0.229 | 0.215 | +0.038 | +0.025 | $7.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 13 | 0.170 | 0.157 | +0.032 | +0.019 | $5.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ goals YES | 17 | 0.205 | 0.194 | +0.025 | +0.014 | $4.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Jani Nyman: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CGYSEA-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (17.71 vs 1.45 bp); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CGYSEA-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (8.78 vs 1.45 bp); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CGYSEA-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (6.75 vs 1.45 bp); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: SEA offense suppressed (<= 2 goals)
- **Kaapo Kakko: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CGYSEA-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (2.90 vs 1.45 bp); wins across more scripts (relative breadth 0.91 vs 0.782); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4772): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.171)
- KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.188)
- KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.171)
- KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.177)

portfolios: A EV +10.43 (adj +6.61) on $41.42, P(profit) 0.5725, adj growth 50.6 bp · B EV +6.04 (adj +3.84) on $23.79, P(profit) 0.4624, adj growth 33.1 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.76 (adj +0.50) on $2.00, P(profit) 0.1615, adj growth 17.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
