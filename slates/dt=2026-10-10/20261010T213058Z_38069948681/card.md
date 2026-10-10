# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-10T21:30:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +31.69 | +9.87 | +30.20 | 0.830 | -9.95 | -19.97 | 93.31 |
| B thesis-diversified (joint) ← optimiser card | 149.05 | +33.57 | +19.60 | +30.65 | 0.780 | -18.92 | -31.28 | 186.76 |
| C best expression per thesis | 149.12 | +26.92 | +12.60 | +25.23 | 0.770 | -17.06 | -28.78 | 119.73 |
| R FUNDED research stakes | 16.00 | +2.80 | +1.90 | -1.11 | 0.441 | -4.62 | -6.54 | 0.00 |

## MIN @ FLA  ·  10000 joint draws  ·  428 bet sides mapped, 29 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.551 / away 0.449

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_MIN_win | p_overtime | goals | shots FLA/MIN | FLA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.45 | 0.55 | 0.00 | 6.02 | 28.0/28.0 | 24.0/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.48 | 0.52 | 0.46 | 5.93 | 28.1/28.0 | 24.6/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.46 | 0.54 | 0.00 | 9.35 | 29.8/29.7 | 23.3/23.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.077 | 0.50 | 0.50 | 0.00 | 6.0 | 33.5/22.7 | 19.2/29.6 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.54 | 0.46 | 0.50 | 5.96 | 33.3/22.5 | 19.4/29.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.057 | 0.37 | 0.63 | 0.00 | 6.02 | 22.3/32.8 | 28.6/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 7 | 0.137 | 0.119 | +0.062 | +0.044 | $3.23 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Nico Sturm: 1+ goals YES | 6 | 0.104 | 0.092 | +0.040 | +0.028 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Michael McCarron: 1+ goals YES | 8 | 0.127 | 0.114 | +0.042 | +0.029 | $2.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Sandis Vilmanis: 1+ goals YES | 10 | 0.150 | 0.136 | +0.044 | +0.030 | $2.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (58.89 vs 16.81 bp); relationships: KXNHLGOAL-26OCT10MINFLA-MINNSTURM78-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT10MINFLA-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: MIN offense suppressed (<= 2 goals)
- **Nico Sturm: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (27.26 vs 16.81 bp); despite a smaller raw edge (+0.040 vs +0.051/contract); relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT10MINFLA-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: MIN offense suppressed (<= 2 goals)
- **Michael McCarron: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (22.79 vs 16.81 bp); despite a smaller raw edge (+0.042 vs +0.051/contract); relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT10MINFLA-MINNSTURM78-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense suppressed (<= 2 goals)
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT10MINFLA-9|yes; why: higher confidence-adjusted growth (19.97 vs 2.53 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.916 vs 0.362); relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10MINFLA-MINNSTURM78-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT10MINFLA-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4253): highest fidelity KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.4036): highest fidelity KXNHLSPREAD-26OCT10MINFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10MINFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2855): highest fidelity KXNHLTOTAL-26OCT10MINFLA-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3525, phi -0.156)
- KXNHLGOAL-26OCT10MINFLA-MINNSTURM78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3525, phi -0.141)
- KXNHLGOAL-26OCT10MINFLA-MINMMCCARRON47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3525, phi -0.169)
- KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4036, phi -0.182)

portfolios: A EV +3.98 (adj +0.72) on $13.64, P(profit) 0.5971, adj growth 6.4 bp · B EV +6.13 (adj +4.29) on $10.01, P(profit) 0.4287, adj growth 40.5 bp · C EV +2.62 (adj +1.49) on $14.03, P(profit) 0.3497, adj growth 14.2 bp · R EV +0.84 (adj +0.60) on $1.00, P(profit) 0.137, adj growth 22.2 bp

## UTA @ BUF  ·  10000 joint draws  ·  422 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.496 / away 0.504

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_UTA_win | p_overtime | goals | shots BUF/UTA | BUF/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.52 | 0.48 | 0.00 | 6.04 | 27.3/27.2 | 23.8/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.48 | 0.52 | 0.45 | 5.97 | 27.6/27.4 | 24.1/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.52 | 0.48 | 0.00 | 9.35 | 29.0/28.7 | 22.6/23.1 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.076 | 0.57 | 0.43 | 0.00 | 6.01 | 32.4/21.4 | 18.4/28.2 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.54 | 0.46 | 0.45 | 5.94 | 32.7/22.0 | 18.8/29.2 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.058 | 0.59 | 0.41 | 0.00 | 9.38 | 34.2/23.1 | 17.8/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 17 | 0.223 | 0.208 | +0.043 | +0.029 | $2.81 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 68 | 0.816 | 0.725 | +0.121 | +0.029 | $6.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Justin Danforth: 1+ goals YES | 10 | 0.131 | 0.122 | +0.024 | +0.015 | $1.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 12 | 0.152 | 0.143 | +0.024 | +0.015 | $1.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10UTABUF-UTAALEE72-1|yes; why: higher confidence-adjusted growth (11.97 vs 0.24 bp); alternative not eligible: confidence-adjusted EV +0.0044 below the 0.010/contract floor; relationships: KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.046); KXNHLGOAL-26OCT10UTABUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT10UTABUF-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: UTA offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10UTABUF-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (8.90 vs 0.61 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10UTABUF-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.046); KXNHLGOAL-26OCT10UTABUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT10UTABUF-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: UTA offense succeeds (4+ goals)
- **Justin Danforth: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10UTABUF-BUFPKREBS19-1|yes; why: higher confidence-adjusted growth (5.33 vs 2.39 bp); relationships: KXNHLGOAL-26OCT10UTABUF-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT10UTABUF-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: BUF offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10UTABUF-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10UTABUF-UTALCROUSE67-1|yes has the higher standalone adjusted growth (11.97 vs 4.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT10UTABUF-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT10UTABUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.3915): highest fidelity KXNHLGOAL-26OCT10UTABUF-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10UTABUF-UTALCROUSE67-1|yes (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.4173): highest fidelity KXNHLAST-26OCT10UTABUF-BUFOPOWER25-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT10UTABUF-BUFJDOAN91-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3807): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT10UTABUF-UTALCROUSE67-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3807, phi -0.204)
- KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.1 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3915, phi -0.206)
- KXNHLGOAL-26OCT10UTABUF-BUFJDANFORTH15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3655, phi -0.149)
- KXNHLGOAL-26OCT10UTABUF-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3807, phi -0.176)

portfolios: A EV +2.68 (adj +0.89) on $13.64, P(profit) 0.629, adj growth 8.3 bp · B EV +2.40 (adj +1.09) on $12.17, P(profit) 0.4063, adj growth 10.4 bp · C EV +1.01 (adj +0.65) on $4.75, P(profit) 0.3575, adj growth 6.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ MTL  ·  10000 joint draws  ·  486 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.639 / away 0.361

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_DET_win | p_overtime | goals | shots MTL/DET | MTL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.67 | 0.33 | 0.00 | 6.06 | 27.3/27.7 | 25.0/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.55 | 0.45 | 0.46 | 5.89 | 27.2/27.7 | 24.5/23.9 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.096 | 0.61 | 0.39 | 0.00 | 5.97 | 22.0/32.7 | 29.5/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.68 | 0.32 | 0.00 | 9.34 | 28.8/29.1 | 24.1/21.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.52 | 0.48 | 0.45 | 5.88 | 21.8/32.5 | 29.1/18.5 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.063 | 0.63 | 0.37 | 0.00 | 9.28 | 23.3/34.6 | 28.8/16.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nate Danielson: 1+ goals YES | 7 | 0.107 | 0.096 | +0.032 | +0.022 | $1.73 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Emmitt Finnie: 1+ goals YES | 16 | 0.201 | 0.188 | +0.031 | +0.019 | $1.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Andrew Copp: 1+ goals YES | 15 | 0.185 | 0.175 | +0.026 | +0.016 | $1.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 69 | 0.764 | 0.725 | +0.059 | +0.020 | $6.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Nate Danielson: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes; why: higher confidence-adjusted growth (14.50 vs 5.38 bp); relationships: KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT10DETMTL-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT10DETMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: DET offense suppressed (<= 2 goals)
- **Emmitt Finnie: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT10DETMTL-DET5|yes; why: higher confidence-adjusted growth (5.38 vs 0.09 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.908 vs 0.524); alternative not eligible: confidence-adjusted EV +0.0023 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10DETMTL-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT10DETMTL-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT10DETMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: DET offense suppressed (<= 2 goals)
- **Andrew Copp: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes has the higher standalone adjusted growth (5.38 vs 4.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT10DETMTL-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT10DETMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: DET offense suppressed (<= 2 goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10DETMTL-MTLNSUZUKI14-2|no; why: higher confidence-adjusted growth (4.07 vs 1.85 bp); relationships: KXNHLGOAL-26OCT10DETMTL-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT10DETMTL-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DET:OFFENSE_4PLUS (p 0.3182): highest fidelity KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.312): highest fidelity KXNHLAST-26OCT10DETMTL-MTLNSUZUKI14-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT10DETMTL-MTLCKREIDER22-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:NET_HIGH_VOLUME (p 0.2498): highest fidelity KXNHLSAVE-26OCT10DETMTL-MTLJFOWLER32-23|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT10DETMTL-MTLJFOWLER32-23|yes (same contract)
- KXNHLGOAL-26OCT10DETMTL-DETNDANIELSON29-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4676, phi -0.147)
- KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4676, phi -0.231)
- KXNHLGOAL-26OCT10DETMTL-DETACOPP18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4676, phi -0.208)
- KXNHLAST-26OCT10DETMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4837, phi -0.204)

portfolios: A EV +2.30 (adj +0.77) on $13.64, P(profit) 0.4854, adj growth 7.4 bp · B EV +1.82 (adj +1.01) on $11.04, P(profit) 0.3545, adj growth 9.7 bp · C EV +1.95 (adj +0.54) on $13.17, P(profit) 0.5903, adj growth 5.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ OTT  ·  10000 joint draws  ·  424 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.591 / away 0.409

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NSH_win | p_overtime | goals | shots OTT/NSH | OTT/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.133 | 0.69 | 0.31 | 0.00 | 6.01 | 33.6/21.9 | 19.4/29.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.63 | 0.37 | 0.00 | 6.04 | 28.4/27.6 | 24.6/24.3 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.55 | 0.45 | 0.50 | 5.94 | 33.8/22.0 | 18.8/30.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.48 | 0.52 | 0.46 | 5.93 | 28.2/27.6 | 24.3/25.0 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.088 | 0.71 | 0.29 | 0.00 | 9.35 | 35.7/23.4 | 18.8/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.61 | 0.39 | 0.00 | 9.38 | 29.7/28.9 | 23.2/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Warren Foegele: 1+ goals YES | 11 | 0.186 | 0.166 | +0.070 | +0.049 | $4.02 | FUNDED_RESEARCH | $2 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 15 | 0.212 | 0.194 | +0.053 | +0.035 | $3.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 22 | 0.279 | 0.263 | +0.047 | +0.031 | $3.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Stephen Halliday: 1+ goals YES | 11 | 0.150 | 0.139 | +0.033 | +0.022 | $1.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Warren Foegele: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (49.36 vs 19.72 bp); relationships: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT10NSHOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10NSHOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (19.72 vs 5.79 bp); despite a smaller raw edge (+0.053 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10NSHOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT10NSHOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: OTT offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT10NSHOTT-7|yes; why: higher confidence-adjusted growth (11.83 vs 0.24 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.929 vs 0.703); alternative not eligible: confidence-adjusted EV +0.0052 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10NSHOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT10NSHOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: NSH offense suppressed (<= 2 goals)
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (19.72 vs 9.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT10NSHOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.4604): highest fidelity KXNHLAST-26OCT10NSHOTT-OTTJSPENCE10-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.3268): highest fidelity KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3217): highest fidelity KXNHLAST-26OCT10NSHOTT-OTTABURAKOVSKY95-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10NSHOTT-OTTABURAKOVSKY95-1|no (same contract)
- KXNHLGOAL-26OCT10NSHOTT-OTTWFOEGELE37-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3217, phi -0.165)
- KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3217, phi -0.213)
- KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4537, phi -0.253)
- KXNHLGOAL-26OCT10NSHOTT-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3217, phi -0.152)

portfolios: A EV +3.57 (adj +1.85) on $13.64, P(profit) 0.4384, adj growth 17.6 bp · B EV +4.64 (adj +3.18) on $12.29, P(profit) 0.6117, adj growth 30.2 bp · C EV +3.04 (adj +1.56) on $13.91, P(profit) 0.4369, adj growth 14.7 bp · R EV +1.19 (adj +0.84) on $2.00, P(profit) 0.1865, adj growth 30.2 bp

## DAL @ PIT  ·  10000 joint draws  ·  414 bet sides mapped, 25 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.384 / away 0.616

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_DAL_win | p_overtime | goals | shots PIT/DAL | PIT/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.50 | 0.50 | 0.00 | 6.0 | 26.5/26.3 | 22.8/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.47 | 6.0 | 26.6/26.5 | 23.2/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.51 | 0.49 | 0.00 | 9.3 | 27.9/27.8 | 22.0/21.7 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.085 | 0.57 | 0.43 | 0.00 | 5.97 | 31.5/20.9 | 17.9/27.5 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.53 | 0.47 | 0.47 | 6.03 | 31.5/20.9 | 17.6/28.1 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.060 | 0.60 | 0.40 | 0.00 | 9.25 | 33.0/22.3 | 17.2/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 10 | 0.154 | 0.139 | +0.048 | +0.033 | $2.60 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Bryan Rust: 1+ goals YES | 26 | 0.326 | 0.308 | +0.053 | +0.035 | $3.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Roope Hintz: 1+ assists NO | 56 | 0.708 | 0.608 | +0.130 | +0.031 | $6.13 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 75 | 0.826 | 0.785 | +0.063 | +0.022 | $4.26 | FUNDED_RESEARCH | $2 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes; why: Player prop expression KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes selected over broad KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3|yes because adjusted EV is 0.8 pts higher while thesis capture is 0.25 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT10DALPIT-DAL3|no: MOSTLY_INDEPENDENT (phi 0.11); failure: PIT offense suppressed (<= 2 goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (24.12 vs 13.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT10DALPIT-DAL3|no: MOSTLY_INDEPENDENT (phi 0.134); failure: PIT offense suppressed (<= 2 goals)
- **Roope Hintz: 1+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes; why: higher confidence-adjusted growth (8.71 vs 7.75 bp); wins across more scripts (relative breadth 0.994 vs 0.504); relationships: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT10DALPIT-DAL3|no: REINFORCING (phi 0.15); failure: DAL offense succeeds (4+ goals)
- **Dallas wins by over 2.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes; why: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes has the higher standalone adjusted growth (7.75 vs 6.13 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.292); relationships: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.11); KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.134); KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: REINFORCING (phi 0.15); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4184): highest fidelity KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes — Player prop expression KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes selected over broad KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3|yes because adjusted EV is 0.8 pts higher while thesis capture is 0.25 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PIT:WINS_BY_2PLUS (p 0.2879): highest fidelity KXNHLSPREAD-26OCT10DALPIT-PIT2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.3804): highest fidelity KXNHLSPREAD-26OCT10DALPIT-DAL3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3717, phi -0.195)
- KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3717, phi -0.264)
- KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.3 pts; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4031, phi -0.254)
- KXNHLSPREAD-26OCT10DALPIT-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.2763, phi -0.743)
- override: Player prop expression KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes selected over broad KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3|yes because adjusted EV is 0.8 pts higher while thesis capture is 0.25 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.76 (adj +0.67) on $13.64, P(profit) 0.5683, adj growth 6.3 bp · B EV +3.59 (adj +1.72) on $16.56, P(profit) 0.4149, adj growth 16.4 bp · C EV +3.53 (adj +1.51) on $14.02, P(profit) 0.5136, adj growth 14.2 bp · R EV +0.17 (adj +0.06) on $2.00, P(profit) 0.8261, adj growth 2.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10DALPIT-DAL|no == KXNHLGAME-26OCT10DALPIT-PIT|yes

## CAR @ CHI  ·  10000 joint draws  ·  416 bet sides mapped, 26 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.315 / away 0.685

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_CAR_win | p_overtime | goals | shots CHI/CAR | CHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.171 | 0.34 | 0.66 | 0.00 | 6.01 | 20.4/33.5 | 28.9/17.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.139 | 0.45 | 0.55 | 0.46 | 5.9 | 20.5/33.4 | 30.1/17.4 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.120 | 0.34 | 0.66 | 0.00 | 9.36 | 22.2/35.2 | 27.5/17.4 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.079 | 0.38 | 0.62 | 0.00 | 3.46 | 19.0/32.1 | 29.8/17.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.079 | 0.39 | 0.61 | 0.00 | 6.04 | 26.1/27.1 | 23.1/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.47 | 0.53 | 0.47 | 5.91 | 26.3/27.4 | 24.0/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 14 | 0.199 | 0.183 | +0.050 | +0.034 | $3.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 26 | 0.326 | 0.308 | +0.052 | +0.035 | $3.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 65 | 0.721 | 0.702 | +0.055 | +0.036 | $6.62 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Ryan Donato: 1+ goals YES | 13 | 0.177 | 0.164 | +0.039 | +0.026 | $2.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (19.97 vs 13.20 bp); despite a smaller raw edge (+0.050 vs +0.052/contract); relationships: KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT10CARCHI-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes has the higher standalone adjusted growth (19.97 vs 13.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10CARCHI-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: CHI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10CARCHI-CARSAHO20-1|no; why: higher confidence-adjusted growth (12.93 vs 6.91 bp); despite a smaller raw edge (+0.055 vs +0.122/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10CARCHI-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: CAR offense succeeds (4+ goals)
- **Ryan Donato: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes has the higher standalone adjusted growth (19.97 vs 12.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.026); they share one thesis budget; relationships: KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis CHI:OFFENSE_4PLUS (p 0.3328): highest fidelity KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.3257): highest fidelity KXNHLSPREAD-26OCT10CARCHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2834): highest fidelity KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10CARCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4482, phi -0.234)
- KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4482, phi -0.268)
- KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4595, phi -0.215)
- KXNHLGOAL-26OCT10CARCHI-CHIRDONATO8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4482, phi -0.207)

portfolios: A EV +2.59 (adj +0.54) on $13.64, P(profit) 0.554, adj growth 5.1 bp · B EV +2.94 (adj +1.97) on $15.68, P(profit) 0.4937, adj growth 18.8 bp · C EV +4.00 (adj +1.83) on $20.43, P(profit) 0.6745, adj growth 17.4 bp · R EV +0.17 (adj +0.11) on $2.00, P(profit) 0.7211, adj growth 4.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10CARCHI-CHI|yes == KXNHLGAME-26OCT10CARCHI-CAR|no

## CBJ @ STL  ·  10000 joint draws  ·  428 bet sides mapped, 8 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.516 / away 0.484

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_CBJ_win | p_overtime | goals | shots STL/CBJ | STL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.57 | 0.43 | 0.00 | 5.99 | 26.8/27.1 | 23.7/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.51 | 0.49 | 0.49 | 5.9 | 27.0/27.2 | 23.9/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.57 | 0.43 | 0.00 | 9.21 | 28.5/28.7 | 23.0/22.0 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.48 | 0.52 | 0.47 | 5.89 | 21.7/32.3 | 28.8/18.5 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.079 | 0.50 | 0.50 | 0.00 | 5.97 | 21.4/32.0 | 28.3/18.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.58 | 0.42 | 0.00 | 3.48 | 25.6/25.8 | 24.2/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Conor Garland: 1+ goals NO | 83 | 0.887 | 0.872 | +0.048 | +0.032 | $6.62 | FUNDED_RESEARCH | $2 | CBJ:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Ross Johnston: 1+ goals YES | 6 | 0.083 | 0.077 | +0.019 | +0.013 | $1.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 20 | 0.243 | 0.231 | +0.032 | +0.020 | $1.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (16.99 vs 5.39 bp); despite a smaller raw edge (+0.048 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10CBJSTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT10CBJSTL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CBJ offense succeeds (4+ goals)
- **Ross Johnston: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10CBJSTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (6.46 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10CBJSTL-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT10CBJSTL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: STL offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10CBJSTL-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (4.99 vs 3.60 bp); relationships: KXNHLGOAL-26OCT10CBJSTL-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT10CBJSTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:SUPPRESSED (p 0.447): highest fidelity KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.3309): highest fidelity KXNHLGOAL-26OCT10CBJSTL-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10CBJSTL-CBJCCOYLE3-1|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3835): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT10CBJSTL-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3309, phi -0.167)
- KXNHLGOAL-26OCT10CBJSTL-STLRJOHNSTON49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3862, phi -0.131)
- KXNHLGOAL-26OCT10CBJSTL-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.447, phi -0.234)

portfolios: A EV +1.40 (adj +0.54) on $13.64, P(profit) 0.6392, adj growth 5.3 bp · B EV +1.01 (adj +0.67) on $9.73, P(profit) 0.2839, adj growth 6.5 bp · C EV +1.23 (adj +0.53) on $10.85, P(profit) 0.8149, adj growth 5.1 bp · R EV +0.11 (adj +0.08) on $2.00, P(profit) 0.8875, adj growth 3.0 bp

## TOR @ COL  ·  10000 joint draws  ·  448 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.656 / away 0.344

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_TOR_win | p_overtime | goals | shots COL/TOR | COL/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.193 | 0.77 | 0.23 | 0.00 | 6.06 | 36.8/22.3 | 20.0/31.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.154 | 0.78 | 0.23 | 0.00 | 9.4 | 38.8/23.7 | 19.5/29.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.135 | 0.58 | 0.42 | 0.46 | 5.95 | 36.9/22.7 | 19.5/33.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.080 | 0.73 | 0.27 | 0.00 | 6.01 | 30.0/28.6 | 26.0/25.5 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.074 | 0.73 | 0.27 | 0.00 | 3.5 | 35.5/21.2 | 19.9/32.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.55 | 0.45 | 0.48 | 5.99 | 30.1/28.7 | 25.4/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cale Makar: 1+ goals NO | 76 | 0.808 | 0.795 | +0.036 | +0.022 | $6.01 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Zachary L'Heureux: 1+ goals YES | 12 | 0.155 | 0.144 | +0.028 | +0.017 | $1.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Nick Paul: 1+ goals NO | 83 | 0.865 | 0.855 | +0.025 | +0.015 | $6.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Martin Necas: 1+ goals NO | 63 | 0.675 | 0.662 | +0.029 | +0.016 | $3.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no; why: higher confidence-adjusted growth (6.28 vs 2.47 bp); relationships: KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10TORCOL-TORNPAUL20-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: COL offense succeeds (4+ goals)
- **Zachary L'Heureux: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10TORCOL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (5.39 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10TORCOL-TORNPAUL20-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: COL offense suppressed (<= 2 goals)
- **Nick Paul: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no; why: higher confidence-adjusted growth (3.61 vs 1.54 bp); despite a smaller raw edge (+0.025 vs +0.086/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: TOR offense succeeds (4+ goals)
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10TORCOL-COLNMACKINNON29-1|no; why: Player prop expression KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no selected over player prop KXNHLAST-26OCT10TORCOL-COLNMACKINNON29-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.85 vs 0.74 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT10TORCOL-TORNPAUL20-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.19, COL shot control · high event (8+) · decided (2+) 0.15, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.14.
- thesis COL:SUPPRESSED (p 0.2512): highest fidelity KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no (same contract)
- thesis TOR:SUPPRESSED (p 0.4971): highest fidelity KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no (same contract)
- thesis COL:OFFENSE_4PLUS (p 0.556): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.556, phi -0.186)
- KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2512, phi -0.156)
- KXNHLGOAL-26OCT10TORCOL-TORNPAUL20-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.288, phi -0.187)
- KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.556, phi -0.235)
- override: Player prop expression KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no selected over player prop KXNHLAST-26OCT10TORCOL-COLNMACKINNON29-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.85 vs 0.74 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.48 (adj +0.38) on $13.64, P(profit) 0.6101, adj growth 3.6 bp · B EV +0.88 (adj +0.53) on $16.56, P(profit) 0.5475, adj growth 5.1 bp · C EV +0.74 (adj +0.20) on $8.55, P(profit) 0.4826, adj growth 1.9 bp · R EV +0.09 (adj +0.06) on $2.00, P(profit) 0.8085, adj growth 2.2 bp

## TBL @ NYI  ·  10000 joint draws  ·  392 bet sides mapped, 27 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.386 / away 0.614

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_TBL_win | p_overtime | goals | shots NYI/TBL | NYI/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.54 | 0.46 | 0.00 | 6.0 | 26.7/27.0 | 23.6/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.49 | 5.87 | 27.0/27.3 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.55 | 0.45 | 0.00 | 9.22 | 28.4/28.4 | 22.6/22.1 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.074 | 0.43 | 0.57 | 0.00 | 5.93 | 21.2/31.8 | 27.7/18.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.44 | 0.56 | 0.46 | 5.83 | 21.5/32.1 | 28.7/18.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.067 | 0.54 | 0.46 | 0.48 | 2.78 | 25.3/25.6 | 24.2/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 18 | 0.268 | 0.244 | +0.077 | +0.054 | $5.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| John Carlson: 1+ assists NO | 53 | 0.727 | 0.596 | +0.180 | +0.048 | $6.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Jake Guentzel: 1+ goals NO | 67 | 0.716 | 0.704 | +0.031 | +0.018 | $3.50 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT10TBNYI-TB3|no; why: higher confidence-adjusted growth (40.55 vs 11.47 bp); despite a smaller raw edge (+0.077 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT10TBNYI-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NYI offense suppressed (<= 2 goals)
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10TBNYI-TB3|no; why: higher confidence-adjusted growth (20.62 vs 11.47 bp); relationships: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT10TBNYI-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi 0.13); failure: TBL offense succeeds (4+ goals)
- **Jake Guentzel: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no; why: Player prop expression KXNHLGOAL-26OCT10TBNYI-TBJGUENTZEL59-1|no selected over broad KXNHLTEAMTOTAL-26OCT10TBNYI-TB4|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.13); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3546): highest fidelity KXNHLTEAMTOTAL-26OCT10TBNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.4424): highest fidelity KXNHLSPREAD-26OCT10TBNYI-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no — Player prop expression KXNHLGOAL-26OCT10TBNYI-TBJGUENTZEL59-1|no selected over broad KXNHLTEAMTOTAL-26OCT10TBNYI-TB4|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NYI:WINS (p 0.5144): highest fidelity KXNHLSPREAD-26OCT10TBNYI-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10TBNYI-TB3|no (same contract)
- KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4237, phi -0.259)
- KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.2 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3353, phi -0.231)
- KXNHLGOAL-26OCT10TBNYI-TBJGUENTZEL59-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3353, phi -0.241)
- override: Player prop expression KXNHLGOAL-26OCT10TBNYI-TBJGUENTZEL59-1|no selected over broad KXNHLTEAMTOTAL-26OCT10TBNYI-TB4|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.92 (adj +0.72) on $13.64, P(profit) 0.7216, adj growth 6.8 bp · B EV +4.32 (adj +2.10) on $15.00, P(profit) 0.6681, adj growth 20.1 bp · C EV +5.22 (adj +2.41) on $20.43, P(profit) 0.7455, adj growth 23.1 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.7164, adj growth 1.0 bp

## ANA @ CGY  ·  10000 joint draws  ·  462 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.479 / away 0.521

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_ANA_win | p_overtime | goals | shots CGY/ANA | CGY/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.50 | 0.50 | 0.00 | 6.02 | 28.5/29.0 | 25.5/25.0 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.107 | 0.43 | 0.57 | 0.00 | 6.01 | 23.0/35.0 | 31.0/19.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.50 | 0.50 | 0.46 | 5.97 | 28.6/29.2 | 25.9/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.52 | 0.48 | 0.00 | 9.45 | 30.0/30.6 | 24.4/23.4 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.47 | 0.53 | 0.49 | 5.92 | 22.7/34.6 | 31.2/19.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.079 | 0.43 | 0.57 | 0.00 | 9.42 | 24.4/36.2 | 29.0/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 16 | 0.224 | 0.206 | +0.055 | +0.036 | $3.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 14 | 0.195 | 0.178 | +0.047 | +0.029 | $2.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 9 | 0.131 | 0.120 | +0.035 | +0.024 | $1.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Zayne Parekh: 1+ goals NO | 85 | 0.881 | 0.872 | +0.022 | +0.013 | $6.62 | FUNDED_RESEARCH | $2 | CGY:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10ANACGY-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (19.94 vs 0.91 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT10ANACGY-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10ANACGY-CGYMFROST16-1|yes; why: higher confidence-adjusted growth (14.58 vs 2.82 bp); relationships: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10ANACGY-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: CGY offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes has the higher standalone adjusted growth (19.94 vs 14.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10ANACGY-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: ANA offense suppressed (<= 2 goals)
- **Zayne Parekh: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT10ANACGY-CGYMCORONATO27-1|no; why: higher confidence-adjusted growth (3.22 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: CGY offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4242): highest fidelity KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.4082): highest fidelity KXNHLGOAL-26OCT10ANACGY-CGYMFROST16-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10ANACGY-CGYMFROST16-1|yes (same contract)
- thesis ANA:SUPPRESSED (p 0.3599): highest fidelity KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no (same contract)
- KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3599, phi -0.21)
- KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.3745, phi -0.184)
- KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3599, phi -0.164)
- KXNHLGOAL-26OCT10ANACGY-CGYZPAREKH19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.4082, phi -0.149)

portfolios: A EV +3.74 (adj +2.07) on $13.64, P(profit) 0.4573, adj growth 19.6 bp · B EV +2.77 (adj +1.80) on $14.44, P(profit) 0.4573, adj growth 17.2 bp · C EV +1.72 (adj +1.10) on $10.32, P(profit) 0.374, adj growth 10.4 bp · R EV +0.05 (adj +0.03) on $2.00, P(profit) 0.8813, adj growth 1.2 bp

## LAK @ VGK  ·  10000 joint draws  ·  502 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.598 / away 0.402

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_LAK_win | p_overtime | goals | shots VGK/LAK | VGK/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.64 | 0.36 | 0.00 | 6.0 | 27.3/27.1 | 24.2/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.46 | 5.92 | 27.6/27.5 | 24.1/24.3 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.093 | 0.72 | 0.28 | 0.00 | 5.94 | 32.2/21.4 | 19.0/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.63 | 0.37 | 0.00 | 9.14 | 29.2/28.7 | 23.4/22.6 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.55 | 0.45 | 0.46 | 5.84 | 32.5/21.7 | 18.6/29.0 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.51 | 0.49 | 0.47 | 2.78 | 26.0/25.9 | 24.5/24.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.081 | 0.072 | +0.027 | +0.018 | $1.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 69 | 0.752 | 0.736 | +0.047 | +0.030 | $6.62 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 50 | 0.647 | 0.548 | +0.130 | +0.031 | $5.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Trevor Moore: 1+ assists YES | 23 | 0.308 | 0.261 | +0.065 | +0.019 | $1.94 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10LAVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (14.09 vs 0.82 bp); despite a smaller raw edge (+0.027 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10LAVGK-VGKTHERTL48-1|no; why: higher confidence-adjusted growth (9.86 vs 1.03 bp); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10LAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VGK offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10LAVGK-LAAPANARIN10-2|no; why: KXNHLAST-26OCT10LAVGK-LAAPANARIN10-2|no has the higher standalone adjusted growth (12.51 vs 8.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.372); relationships: KXNHLGOAL-26OCT10LAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.04); failure: LAK offense succeeds (4+ goals)
- **Trevor Moore: 1+ assists YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10LAVGK-LAEHAULA56-1|yes; why: higher confidence-adjusted growth (4.23 vs 1.66 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0098 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10LAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.04); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4941): highest fidelity KXNHLAST-26OCT10LAVGK-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3638): highest fidelity KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.2884): highest fidelity KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes (same contract)
- KXNHLGOAL-26OCT10LAVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3638, phi -0.133)
- KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.411, phi -0.207)
- KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.2 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2884, phi -0.26)
- KXNHLAST-26OCT10LAVGK-LATMOORE12-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4941, phi -0.286)

portfolios: A EV +2.28 (adj +0.72) on $13.64, P(profit) 0.649, adj growth 6.9 bp · B EV +3.08 (adj +1.24) on $15.57, P(profit) 0.6507, adj growth 11.9 bp · C EV +1.85 (adj +0.78) on $18.66, P(profit) 0.7883, adj growth 7.6 bp · R EV +0.13 (adj +0.09) on $2.00, P(profit) 0.7523, adj growth 3.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
