# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-04T22:50:49Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.59 | +11.85 | +18.50 | 0.620 | -44.39 | -57.29 | 99.84 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +23.97 | +13.52 | +17.80 | 0.623 | -44.34 | -59.10 | 119.00 |
| C best expression per thesis | 103.83 | +14.18 | +5.89 | +13.85 | 0.638 | -31.89 | -43.75 | 52.51 |
| R FUNDED research stakes | 18.00 | +2.38 | +1.61 | +2.10 | 0.606 | -6.14 | -11.84 | 0.00 |

## OTT @ BUF  ·  10000 joint draws  ·  482 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.533 / away 0.467

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_OTT_win | p_overtime | goals | shots BUF/OTT | BUF/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.09 | 27.5/27.4 | 24.0/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.54 | 0.46 | 0.47 | 5.96 | 27.5/27.6 | 24.3/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.57 | 0.43 | 0.00 | 9.4 | 28.9/28.8 | 23.0/22.3 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.071 | 0.61 | 0.39 | 0.00 | 6.02 | 32.1/21.9 | 19.0/28.1 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.53 | 0.47 | 0.47 | 5.94 | 32.2/21.5 | 18.3/29.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.064 | 0.49 | 0.51 | 0.00 | 6.02 | 22.0/32.6 | 29.1/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Owen Power: 1+ goals NO | 87 | 0.915 | 0.903 | +0.037 | +0.025 | $18.21 | FUNDED_RESEARCH | $5 | BUF:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 26 | 0.305 | 0.292 | +0.031 | +0.019 | $7.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 15 | 0.184 | 0.174 | +0.025 | +0.015 | $4.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ assists NO | 56 | 0.635 | 0.593 | +0.058 | +0.015 | $10.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04OTTBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (12.68 vs 2.09 bp); despite a smaller raw edge (+0.037 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26NOV04OTTBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.066); failure: BUF offense succeeds (4+ goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV04OTTBUF-BUFJDOAN91-1|yes; why: higher confidence-adjusted growth (3.94 vs 0.00 bp); despite a smaller raw edge (+0.031 vs +0.037/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV04OTTBUF-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV04OTTBUF-BUFTTHOMPSON72-1|no: INTENTIONAL_DIVERSIFIER (phi -0.196); failure: BUF offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (3.77 vs 1.82 bp); relationships: KXNHLGOAL-26NOV04OTTBUF-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV04OTTBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: OTT offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26NOV04OTTBUF-4|no; why: higher confidence-adjusted growth (2.09 vs 0.51 bp); wins across more scripts (relative breadth 1.017 vs 0.364); alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04OTTBUF-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.066); KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.196); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis BUF:OFFENSE_4PLUS (p 0.4511): highest fidelity KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3873): highest fidelity KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3397): highest fidelity KXNHLAST-26NOV04OTTBUF-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04OTTBUF-BUFTTHOMPSON72-1|no (same contract)
- KXNHLGOAL-26NOV04OTTBUF-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4511, phi -0.134)
- KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3397, phi -0.25)
- KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3917, phi -0.206)
- KXNHLAST-26NOV04OTTBUF-BUFTTHOMPSON72-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4511, phi -0.261)

portfolios: A EV +3.43 (adj +1.67) on $38.04, P(profit) 0.4142, adj growth 14.8 bp · B EV +3.24 (adj +1.66) on $39.53, P(profit) 0.4142, adj growth 15.0 bp · C EV +2.73 (adj +1.24) on $23.72, P(profit) 0.4316, adj growth 10.8 bp · R EV +0.21 (adj +0.14) on $5.00, P(profit) 0.9151, adj growth 5.4 bp

## CHI @ FLA  ·  10000 joint draws  ·  438 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.687 / away 0.313

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_CHI_win | p_overtime | goals | shots FLA/CHI | FLA/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.138 | 0.70 | 0.30 | 0.00 | 6.02 | 32.6/20.9 | 18.3/27.8 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.56 | 0.44 | 0.44 | 5.91 | 32.8/20.9 | 17.7/29.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.66 | 0.34 | 0.00 | 6.06 | 27.1/26.2 | 23.2/22.8 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.099 | 0.72 | 0.28 | 0.00 | 9.33 | 34.4/22.4 | 17.9/25.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.48 | 0.52 | 0.46 | 5.94 | 27.3/26.5 | 23.3/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.67 | 0.33 | 0.00 | 9.39 | 28.7/28.0 | 22.6/21.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 59 | 0.675 | 0.652 | +0.068 | +0.045 | $18.99 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Niko Mikkola: 1+ goals YES | 5 | 0.080 | 0.071 | +0.027 | +0.018 | $3.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.270 | 0.254 | +0.048 | +0.032 | $9.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.127 | 0.115 | +0.031 | +0.019 | $4.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04CHIFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (18.88 vs 3.67 bp); despite a smaller raw edge (+0.068 vs +0.100/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04CHIFLA-FLANMIKKOLA77-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense succeeds (4+ goals)
- **Niko Mikkola: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV04CHIFLA-9|yes; why: higher confidence-adjusted growth (13.76 vs 0.54 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.843 vs 0.374); alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: FLA offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes; why: higher confidence-adjusted growth (12.88 vs 5.81 bp); despite a smaller raw edge (+0.048 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.909 vs 0.792); relationships: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV04CHIFLA-FLANMIKKOLA77-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV04CHIFLA-9|yes; why: higher confidence-adjusted growth (9.14 vs 0.54 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.805 vs 0.374); alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV04CHIFLA-FLANMIKKOLA77-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.14, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis FLA:SUPPRESSED (p 0.3122): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.3176): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.3884): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4856, phi -0.231)
- KXNHLGOAL-26NOV04CHIFLA-FLANMIKKOLA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3122, phi -0.12)
- KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4697, phi -0.251)
- KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3122, phi -0.157)

portfolios: A EV +5.73 (adj +1.43) on $38.04, P(profit) 0.6501, adj growth 12.8 bp · B EV +7.56 (adj +4.99) on $36.70, P(profit) 0.4127, adj growth 43.9 bp · C EV +7.42 (adj +3.82) on $50.00, P(profit) 0.6785, adj growth 34.4 bp · R EV +0.56 (adj +0.37) on $5.00, P(profit) 0.6746, adj growth 13.7 bp

## SJS @ LAK  ·  10000 joint draws  ·  488 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.599 / away 0.401

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
| Ivar Stenberg: 1+ goals NO | 80 | 0.852 | 0.838 | +0.041 | +0.027 | $18.07 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Macklin Celebrini: 1+ assists NO | 47 | 0.610 | 0.506 | +0.123 | +0.019 | $7.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.76) | EVIDENCE_MIXED | D |
| Brandt Clarke: 2+ assists NO | 88 | 0.922 | 0.899 | +0.035 | +0.011 | $18.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 41 | 0.554 | 0.439 | +0.127 | +0.012 | $4.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.75) | CALIBRATION_WARNING | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (10.32 vs 4.06 bp); despite a smaller raw edge (+0.041 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.136); KXNHLAST-26NOV04SJLA-LABCLARKE92-2|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: SJS offense succeeds (4+ goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMMARCHMENT27-1|no; why: KXNHLAST-26NOV04SJLA-SJMMARCHMENT27-1|no has the higher standalone adjusted growth (4.06 vs 3.03 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.067); relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.136); KXNHLAST-26NOV04SJLA-LABCLARKE92-2|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: SJS offense succeeds (4+ goals)
- **Brandt Clarke: 2+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (2.80 vs 1.20 bp); despite a smaller raw edge (+0.035 vs +0.127/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.062); failure: LAK offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-LABCLARKE92-1|no; why: higher confidence-adjusted growth (1.20 vs 0.69 bp); evidence CALIBRATION_WARNING vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26NOV04SJLA-LABCLARKE92-2|no: MOSTLY_INDEPENDENT (phi 0.062); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SJS:SUPPRESSED (p 0.4784): highest fidelity KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-SJMMARCHMENT27-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:NET_LOW_VOLUME (p 0.3028): highest fidelity KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no (same contract)
- thesis LAK:SUPPRESSED (p 0.359): highest fidelity KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no (same contract)
- KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3045, phi -0.17)
- KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 24% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.0 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3045, phi -0.273)
- KXNHLAST-26NOV04SJLA-LABCLARKE92-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4321, phi -0.223)
- KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4321, phi -0.285)

portfolios: A EV +6.97 (adj +1.14) on $38.04, P(profit) 0.616, adj growth 9.9 bp · B EV +4.67 (adj +1.21) on $47.48, P(profit) 0.663, adj growth 11.2 bp · C EV +4.03 (adj +0.83) on $30.11, P(profit) 0.6241, adj growth 7.3 bp · R EV +0.25 (adj +0.16) on $5.00, P(profit) 0.8522, adj growth 6.2 bp

## CGY @ SEA  ·  10000 joint draws  ·  446 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.548 / away 0.452

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
| Ben Meyers: 1+ goals YES | 11 | 0.170 | 0.153 | +0.053 | +0.037 | $8.69 | FUNDED_RESEARCH | $3 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jani Nyman: 1+ goals YES | 11 | 0.162 | 0.146 | +0.045 | +0.029 | $6.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 18 | 0.229 | 0.215 | +0.038 | +0.025 | $6.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ goals YES | 17 | 0.205 | 0.194 | +0.025 | +0.014 | $3.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (27.52 vs 0.72 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: SEA offense suppressed (<= 2 goals)
- **Jani Nyman: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (17.71 vs 0.72 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (8.78 vs 0.72 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: SEA offense suppressed (<= 2 goals)
- **Kaapo Kakko: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (2.90 vs 0.72 bp); despite a smaller raw edge (+0.025 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4772): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.171)
- KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.171)
- KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.188)
- KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.177)

portfolios: A EV +11.45 (adj +7.61) on $35.88, P(profit) 0.4624, adj growth 62.3 bp · B EV +8.50 (adj +5.66) on $26.30, P(profit) 0.4624, adj growth 48.9 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +1.35 (adj +0.94) on $3.00, P(profit) 0.1696, adj growth 30.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
