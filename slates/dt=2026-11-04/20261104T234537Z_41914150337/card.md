# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-04T23:45:37Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +29.32 | +12.07 | +19.39 | 0.631 | -47.38 | -63.51 | 100.47 |
| B thesis-diversified (joint) ← optimiser card | 146.86 | +26.05 | +15.04 | +19.69 | 0.619 | -49.96 | -63.43 | 131.40 |
| C best expression per thesis | 117.75 | +14.90 | +6.35 | +12.31 | 0.648 | -26.97 | -39.01 | 57.74 |
| R FUNDED research stakes | 17.00 | +2.55 | +1.55 | +3.80 | 0.502 | -10.07 | -11.37 | 0.00 |

## OTT @ BUF  ·  10000 joint draws  ·  502 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.535 / away 0.465

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
| Owen Power: 1+ goals NO | 88 | 0.915 | 0.905 | +0.028 | +0.018 | $20.00 | FUNDED_RESEARCH | $5 | BUF:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Ridly Greig: 1+ goals YES | 16 | 0.203 | 0.190 | +0.034 | +0.020 | $5.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 26 | 0.305 | 0.292 | +0.031 | +0.019 | $6.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 15 | 0.184 | 0.174 | +0.025 | +0.015 | $4.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04OTTBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (6.96 vs 2.09 bp); despite a smaller raw edge (+0.028 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: BUF offense succeeds (4+ goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (6.36 vs 3.77 bp); relationships: KXNHLGOAL-26NOV04OTTBUF-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: OTT offense suppressed (<= 2 goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV04OTTBUF-BUFJDOAN91-1|yes; why: higher confidence-adjusted growth (3.94 vs 0.00 bp); despite a smaller raw edge (+0.031 vs +0.037/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV04OTTBUF-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: BUF offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes has the higher standalone adjusted growth (6.36 vs 3.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV04OTTBUF-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.3873): highest fidelity KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.4511): highest fidelity KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.3397): highest fidelity KXNHLAST-26NOV04OTTBUF-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04OTTBUF-BUFTTHOMPSON72-1|no (same contract)
- KXNHLGOAL-26NOV04OTTBUF-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4511, phi -0.134)
- KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3917, phi -0.206)
- KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3397, phi -0.25)
- KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3917, phi -0.206)

portfolios: A EV +3.67 (adj +1.80) on $38.04, P(profit) 0.4284, adj growth 15.9 bp · B EV +3.15 (adj +1.93) on $36.26, P(profit) 0.51, adj growth 17.1 bp · C EV +3.28 (adj +1.56) on $25.88, P(profit) 0.4461, adj growth 13.5 bp · R EV +0.16 (adj +0.10) on $5.00, P(profit) 0.9151, adj growth 3.8 bp

## CHI @ FLA  ·  10000 joint draws  ·  438 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.685 / away 0.315

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
| Brady Tkachuk: 1+ goals NO | 59 | 0.675 | 0.652 | +0.068 | +0.045 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Niko Mikkola: 1+ goals YES | 5 | 0.080 | 0.071 | +0.027 | +0.018 | $4.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.270 | 0.254 | +0.048 | +0.032 | $9.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.127 | 0.115 | +0.031 | +0.019 | $4.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04CHIFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (18.88 vs 3.67 bp); despite a smaller raw edge (+0.068 vs +0.100/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04CHIFLA-FLANMIKKOLA77-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense succeeds (4+ goals)
- **Niko Mikkola: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV04CHIFLA-9|yes; why: higher confidence-adjusted growth (13.76 vs 0.54 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.843 vs 0.374); alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: FLA offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2|yes; why: higher confidence-adjusted growth (12.88 vs 5.46 bp); despite a smaller raw edge (+0.048 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV04CHIFLA-FLANMIKKOLA77-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV04CHIFLA-9|yes; why: higher confidence-adjusted growth (9.14 vs 0.54 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.805 vs 0.374); alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV04CHIFLA-FLANMIKKOLA77-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.14, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis FLA:SUPPRESSED (p 0.3122): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.3176): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.3884): highest fidelity KXNHLGAME-26NOV04CHIFLA-FLA|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4856, phi -0.231)
- KXNHLGOAL-26NOV04CHIFLA-FLANMIKKOLA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3122, phi -0.12)
- KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4697, phi -0.251)
- KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3122, phi -0.157)

portfolios: A EV +6.90 (adj +1.25) on $38.04, P(profit) 0.5718, adj growth 9.7 bp · B EV +7.96 (adj +5.25) on $38.65, P(profit) 0.4127, adj growth 46.0 bp · C EV +6.08 (adj +3.10) on $50.00, P(profit) 0.4703, adj growth 28.6 bp · R EV +0.56 (adj +0.37) on $5.00, P(profit) 0.6746, adj growth 13.7 bp
equivalent contracts collapsed: KXNHLGAME-26NOV04CHIFLA-CHI|yes == KXNHLGAME-26NOV04CHIFLA-FLA|no

## SJS @ LAK  ·  10000 joint draws  ·  488 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.598 / away 0.402

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
| Macklin Celebrini: 2+ assists NO | 82 | 0.912 | 0.864 | +0.082 | +0.033 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Macklin Celebrini: 1+ assists NO | 47 | 0.610 | 0.509 | +0.123 | +0.022 | $8.03 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.76) | EVIDENCE_MIXED | D |
| Yaroslav Askarov: 28+ saves NO | 56 | 0.646 | 0.598 | +0.069 | +0.021 | $12.52 | FUNDED_RESEARCH | $4 | SJS:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Michael Misa: 1+ goals YES | 15 | 0.180 | 0.171 | +0.021 | +0.012 | $3.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Macklin Celebrini: 2+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (17.46 vs 4.18 bp); despite a smaller raw edge (+0.082 vs +0.123/contract); relationships: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: DUPLICATIVE (phi 0.388); KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV04SJLA-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: SJS offense succeeds (4+ goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no; why: second expression of the same thesis: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no has the higher standalone adjusted growth (17.46 vs 4.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.388); they share one thesis budget; relationships: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no: DUPLICATIVE (phi 0.388); KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no: MOSTLY_INDEPENDENT (phi 0.032); KXNHLGOAL-26NOV04SJLA-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.032); failure: SJS offense succeeds (4+ goals)
- **Yaroslav Askarov: 28+ saves NO** — thesis: SJS net faces light volume (<= 25 shots; LAK suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.032); KXNHLGOAL-26NOV04SJLA-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: SJS net faces heavy volume (33+ shots; LAK pressure)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04SJLA-SJKSHERWOOD44-1|yes; why: higher confidence-adjusted growth (2.47 vs 2.17 bp); despite a smaller raw edge (+0.021 vs +0.023/contract); relationships: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi -0.032); KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no: MOSTLY_INDEPENDENT (phi -0.014); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SJS:SUPPRESSED (p 0.4784): highest fidelity KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no (same contract)
- thesis SJS:NET_LOW_VOLUME (p 0.3028): highest fidelity KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3045): highest fidelity KXNHLGOAL-26NOV04SJLA-SJKSHERWOOD44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04SJLA-SJMMISA77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3045, phi -0.244)
- KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 24% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.5 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3045, phi -0.273)
- KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis SJS:NET_HIGH_VOLUME (p 0.2718, phi -0.705)
- KXNHLGOAL-26NOV04SJLA-SJMMISA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4784, phi -0.204)

portfolios: A EV +7.30 (adj +1.41) on $38.04, P(profit) 0.6542, adj growth 12.5 bp · B EV +5.98 (adj +1.90) on $44.26, P(profit) 0.6624, adj growth 17.3 bp · C EV +5.55 (adj +1.69) on $41.87, P(profit) 0.6624, adj growth 15.6 bp · R EV +0.48 (adj +0.14) on $4.00, P(profit) 0.6463, adj growth 4.9 bp

## CGY @ SEA  ·  10000 joint draws  ·  446 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.543 / away 0.457

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
| Ben Meyers: 1+ goals YES | 11 | 0.170 | 0.153 | +0.053 | +0.037 | $9.15 | FUNDED_RESEARCH | $3 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jani Nyman: 1+ goals YES | 11 | 0.162 | 0.146 | +0.045 | +0.029 | $7.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 18 | 0.229 | 0.215 | +0.038 | +0.025 | $7.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ goals YES | 17 | 0.205 | 0.194 | +0.025 | +0.014 | $4.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
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

portfolios: A EV +11.45 (adj +7.61) on $35.88, P(profit) 0.4624, adj growth 62.3 bp · B EV +8.95 (adj +5.96) on $27.69, P(profit) 0.4624, adj growth 51.1 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +1.35 (adj +0.94) on $3.00, P(profit) 0.1696, adj growth 30.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
