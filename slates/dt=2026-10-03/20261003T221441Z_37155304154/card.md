# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T22:14:41Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +35.13 | +12.12 | +33.68 | 0.881 | -3.26 | -12.58 | 116.80 |
| B thesis-diversified (joint) ← optimiser card | 147.59 | +35.77 | +18.76 | +33.37 | 0.834 | -9.39 | -20.47 | 180.82 |
| C best expression per thesis | 149.14 | +29.76 | +14.23 | +27.22 | 0.809 | -11.77 | -21.75 | 136.59 |
| R FUNDED research stakes | 19.00 | +2.98 | +1.93 | +2.31 | 0.634 | -5.50 | -7.55 | 0.00 |

## CHI @ BUF  ·  10000 joint draws  ·  300 bet sides mapped, 9 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.672 / away 0.328

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_CHI_win | p_overtime | goals | shots BUF/CHI | BUF/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.137 | 0.73 | 0.27 | 0.00 | 6.02 | 33.2/21.3 | 18.8/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.67 | 0.33 | 0.00 | 6.04 | 27.6/27.1 | 24.2/23.3 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.57 | 0.43 | 0.46 | 5.9 | 33.9/21.8 | 18.8/30.4 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.096 | 0.71 | 0.29 | 0.00 | 9.25 | 35.0/22.7 | 18.3/27.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.51 | 0.49 | 0.47 | 5.92 | 28.0/27.3 | 24.1/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.68 | 0.32 | 0.00 | 9.33 | 29.2/28.5 | 23.5/21.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 12 | 0.172 | 0.158 | +0.045 | +0.030 | $2.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 57 | 0.651 | 0.630 | +0.064 | +0.043 | $5.46 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 62 | 0.751 | 0.659 | +0.114 | +0.023 | $5.35 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CHIBUF-BUF|no; why: higher confidence-adjusted growth (17.89 vs 2.26 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.023); failure: CHI offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (16.36 vs 3.45 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: BUF offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CHIBUF-CHIRKANTSEROV80-1|no; why: higher confidence-adjusted growth (4.89 vs 0.24 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: CHI offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.2973): highest fidelity KXNHLSPREAD-26OCT03CHIBUF-BUF2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3117): highest fidelity KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4868): highest fidelity KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4868, phi -0.224)
- KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4836, phi -0.243)
- KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.1 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2973, phi -0.232)

portfolios: A EV +1.96 (adj +0.93) on $11.54, P(profit) 0.4336, adj growth 9.1 bp · B EV +2.30 (adj +1.09) on $12.92, P(profit) 0.5781, adj growth 10.6 bp · C EV +2.60 (adj +1.23) on $14.61, P(profit) 0.5781, adj growth 11.9 bp · R EV +0.22 (adj +0.14) on $2.00, P(profit) 0.6512, adj growth 5.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03CHIBUF-CHI|yes == KXNHLGAME-26OCT03CHIBUF-BUF|no

## OTT @ TOR  ·  10000 joint draws  ·  360 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.505 / away 0.495

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_OTT_win | p_overtime | goals | shots TOR/OTT | TOR/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.132 | 0.38 | 0.62 | 0.00 | 6.01 | 21.8/34.0 | 29.4/18.9 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.45 | 0.55 | 0.47 | 5.92 | 22.1/34.2 | 30.9/19.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.47 | 0.53 | 0.00 | 5.98 | 27.6/28.5 | 24.8/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.51 | 0.49 | 0.46 | 5.97 | 27.7/28.6 | 25.3/24.4 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.083 | 0.37 | 0.63 | 0.00 | 9.11 | 23.1/35.8 | 28.8/18.2 | even strength |
| OTT shot control · low event (<=4) · decided (2+) | 0.073 | 0.44 | 0.56 | 0.00 | 3.41 | 20.6/32.9 | 30.9/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Stephen Halliday: 1+ goals YES | 9 | 0.134 | 0.122 | +0.038 | +0.026 | $1.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 9 | 0.128 | 0.117 | +0.033 | +0.022 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ goals NO | 64 | 0.691 | 0.677 | +0.035 | +0.021 | $4.27 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| William Eklund: 1+ assists NO | 66 | 0.736 | 0.695 | +0.060 | +0.019 | $4.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (16.73 vs 3.75 bp); despite a smaller raw edge (+0.038 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); failure: OTT offense suppressed (<= 2 goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (11.75 vs 0.71 bp); despite a smaller raw edge (+0.033 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: TOR offense suppressed (<= 2 goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no; why: Player prop expression KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.84 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT03OTTTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: TOR offense succeeds (4+ goals)
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTJSANDERSON85-1|no; why: KXNHLAST-26OCT03OTTTOR-OTTJSANDERSON85-1|no has the higher standalone adjusted growth (4.41 vs 3.83 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.071); relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLGOAL-26OCT03OTTTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: OTT offense succeeds (4+ goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:SUPPRESSED (p 0.4475): highest fidelity KXNHLAST-26OCT03OTTTOR-TORKMARCHENKO86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no — Player prop expression KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.84 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis OTT:SUPPRESSED (p 0.3882): highest fidelity KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-OTTJSANDERSON85-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS (p 0.548): highest fidelity KXNHLGAME-26OCT03OTTTOR-TOR|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3882, phi -0.158)
- KXNHLGOAL-26OCT03OTTTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4475, phi -0.19)
- KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3332, phi -0.268)
- KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3964, phi -0.222)
- override: Player prop expression KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.84 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.98 (adj +0.38) on $11.54, P(profit) 0.6145, adj growth 3.6 bp · B EV +1.90 (adj +1.11) on $12.55, P(profit) 0.6369, adj growth 10.7 bp · C EV +2.38 (adj +0.67) on $15.48, P(profit) 0.6889, adj growth 6.4 bp · R EV +0.11 (adj +0.06) on $2.00, P(profit) 0.6911, adj growth 2.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03OTTTOR-TOR|no == KXNHLGAME-26OCT03OTTTOR-OTT|yes

## WSH @ TBL  ·  10000 joint draws  ·  356 bet sides mapped, 17 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.638 / away 0.362

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WSH_win | p_overtime | goals | shots TBL/WSH | TBL/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.67 | 0.33 | 0.00 | 6.01 | 27.1/26.6 | 23.7/22.9 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.112 | 0.71 | 0.29 | 0.00 | 6.0 | 32.4/20.9 | 18.5/27.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.52 | 0.48 | 0.46 | 6.01 | 27.2/26.9 | 23.6/23.9 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.55 | 0.45 | 0.48 | 5.9 | 32.5/21.4 | 18.3/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.64 | 0.36 | 0.00 | 9.38 | 28.7/28.3 | 22.9/21.7 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.075 | 0.74 | 0.26 | 0.00 | 9.18 | 34.2/22.5 | 18.3/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| John Carlson: 1+ assists NO | 48 | 0.746 | 0.567 | +0.249 | +0.069 | $5.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| John Carlson: 1+ points NO | 40 | 0.657 | 0.461 | +0.240 | +0.044 | $1.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.83) | CALIBRATION_WARNING | D |
| Aliaksei Protas: 1+ goals YES | 16 | 0.211 | 0.197 | +0.042 | +0.028 | $2.08 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (41.91 vs 17.17 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no: DUPLICATIVE (phi 0.808); KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: TBL offense succeeds (4+ goals)
- **John Carlson: 1+ points NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no; why: second expression of the same thesis: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no has the higher standalone adjusted growth (41.91 vs 17.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.808); they share one thesis budget; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: DUPLICATIVE (phi 0.808); KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: TBL offense succeeds (4+ goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03WSHTB-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (11.78 vs 1.53 bp); relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.3217): highest fidelity KXNHLAST-26OCT03WSHTB-TBNKUCHEROV86-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.3068): highest fidelity KXNHLGOAL-26OCT03WSHTB-WSHTWILSON43-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:OFFENSE_4PLUS (p 0.4659): highest fidelity KXNHLGOAL-26OCT03WSHTB-TBIMIKHEYEV95-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03WSHTB-TBIMIKHEYEV95-1|yes (same contract)
- KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 27.6 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4659, phi -0.21)
- KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 26.2 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4659, phi -0.242)
- KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4782, phi -0.238)

portfolios: A EV +4.82 (adj +0.99) on $11.54, P(profit) 0.7412, adj growth 9.6 bp · B EV +4.20 (adj +1.27) on $9.20, P(profit) 0.7965, adj growth 12.4 bp · C EV +3.94 (adj +1.41) on $10.43, P(profit) 0.7965, adj growth 13.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ PHI  ·  10000 joint draws  ·  366 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.458 / away 0.542

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.125 | 0.49 | 0.51 | 0.47 | 5.85 | 20.3/31.8 | 28.5/17.2 | even strength |
| CAR shot control · normal event (5-7) · decided (2+) | 0.122 | 0.52 | 0.48 | 0.00 | 5.95 | 20.7/32.6 | 29.0/17.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.59 | 0.41 | 0.00 | 5.95 | 25.9/26.6 | 23.5/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.50 | 0.50 | 0.45 | 5.88 | 25.9/26.6 | 23.3/22.8 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.074 | 0.49 | 0.51 | 0.45 | 2.77 | 19.0/30.4 | 28.9/17.5 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.069 | 0.50 | 0.50 | 0.00 | 3.38 | 19.3/30.6 | 28.7/17.6 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Couturier: 1+ goals YES | 9 | 0.174 | 0.152 | +0.079 | +0.056 | $3.50 | FUNDED_RESEARCH | $1 | PHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Noel Acciari: 1+ goals YES | 8 | 0.135 | 0.120 | +0.050 | +0.035 | $2.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 17 | 0.215 | 0.202 | +0.035 | +0.022 | $1.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| William Carrier: 1+ goals YES | 9 | 0.122 | 0.113 | +0.026 | +0.017 | $1.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CARPHI-CAR|no; why: higher confidence-adjusted growth (75.37 vs 7.89 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT03CARPHI-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: PHI offense suppressed (<= 2 goals)
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (75.37 vs 32.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT03CARPHI-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (75.37 vs 7.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT03CARPHI-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)
- **William Carrier: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03CARPHI-CARLSTANKOVEN22-1|yes; why: higher confidence-adjusted growth (7.06 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: CAR offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3793): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.3089): highest fidelity KXNHLGAME-26OCT03CARPHI-PHI|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.5401): highest fidelity KXNHLGAME-26OCT03CARPHI-PHI|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03CARPHI-PHI|yes (same contract)
- KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4036, phi -0.224)
- KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4036, phi -0.168)
- KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4036, phi -0.195)
- KXNHLGOAL-26OCT03CARPHI-CARWCARRIER28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:SUPPRESSED (p 0.4652, phi -0.174)

portfolios: A EV +3.41 (adj +2.09) on $11.54, P(profit) 0.4965, adj growth 20.0 bp · B EV +4.78 (adj +3.36) on $8.53, P(profit) 0.5072, adj growth 32.0 bp · C EV +3.56 (adj +2.44) on $6.30, P(profit) 0.1743, adj growth 23.1 bp · R EV +0.82 (adj +0.59) on $1.00, P(profit) 0.1743, adj growth 22.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03CARPHI-PHI|yes == KXNHLGAME-26OCT03CARPHI-CAR|no

## MTL @ PIT  ·  10000 joint draws  ·  330 bet sides mapped, 9 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.487 / away 0.513

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_MTL_win | p_overtime | goals | shots PIT/MTL | PIT/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| PIT shot control · normal event (5-7) · decided (2+) | 0.125 | 0.63 | 0.37 | 0.00 | 6.07 | 32.9/21.2 | 18.2/28.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.56 | 0.44 | 0.00 | 6.05 | 27.5/26.8 | 23.4/23.5 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.55 | 0.45 | 0.49 | 5.93 | 33.0/21.6 | 18.4/29.7 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.099 | 0.65 | 0.35 | 0.00 | 9.33 | 34.4/22.4 | 17.5/27.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.56 | 0.44 | 0.00 | 9.41 | 29.0/28.4 | 22.5/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.49 | 0.51 | 0.48 | 5.96 | 27.5/26.9 | 23.7/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 12 | 0.201 | 0.180 | +0.074 | +0.052 | $3.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Filip Hallander: 1+ goals YES | 13 | 0.202 | 0.183 | +0.064 | +0.045 | $3.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 29 | 0.374 | 0.352 | +0.070 | +0.047 | $4.20 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes; why: higher confidence-adjusted growth (51.79 vs 4.26 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.827 vs 0.498); relationships: KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03MTLPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: PIT offense suppressed (<= 2 goals)
- **Filip Hallander: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (51.79 vs 36.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03MTLPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (51.79 vs 22.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts PIT shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10, PIT shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.3425): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.4691): highest fidelity KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.5586): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3238, phi -0.228)
- KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3238, phi -0.186)
- KXNHLGOAL-26OCT03MTLPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3238, phi -0.263)

portfolios: A EV +4.25 (adj +2.76) on $11.54, P(profit) 0.4433, adj growth 26.4 bp · B EV +4.42 (adj +3.09) on $10.78, P(profit) 0.5972, adj growth 29.6 bp · C EV +2.36 (adj +1.67) on $4.07, P(profit) 0.2013, adj growth 15.9 bp · R EV +0.46 (adj +0.31) on $2.00, P(profit) 0.3739, adj growth 11.6 bp

## UTA @ CBJ  ·  10000 joint draws  ·  342 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.485 / away 0.515

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_UTA_win | p_overtime | goals | shots CBJ/UTA | CBJ/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.57 | 0.43 | 0.00 | 6.03 | 27.4/27.4 | 24.1/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.47 | 5.94 | 27.7/27.4 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 9.31 | 29.2/29.0 | 23.3/22.8 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.079 | 0.64 | 0.36 | 0.00 | 6.0 | 32.3/21.7 | 18.9/27.9 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.57 | 0.43 | 0.46 | 5.91 | 32.4/21.9 | 18.8/28.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.058 | 0.50 | 0.50 | 0.00 | 5.97 | 21.9/32.1 | 28.3/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vincent Trocheck: 1+ assists NO | 66 | 0.862 | 0.727 | +0.186 | +0.052 | $5.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Charlie Coyle: 1+ goals YES | 20 | 0.271 | 0.252 | +0.059 | +0.041 | $3.29 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Danton Heinen: 1+ goals YES | 9 | 0.132 | 0.120 | +0.036 | +0.024 | $1.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 18 | 0.220 | 0.209 | +0.030 | +0.019 | $1.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03UTACBJ-CBJ|yes; why: higher confidence-adjusted growth (26.96 vs 1.36 bp); relationships: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: UTA offense succeeds (4+ goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-CBJSMONAHAN23-1|yes; why: higher confidence-adjusted growth (21.19 vs 2.97 bp); relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CBJ offense suppressed (<= 2 goals)
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (21.19 vs 14.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CBJ offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-UTAALEE72-1|yes; why: higher confidence-adjusted growth (4.85 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.4162): highest fidelity KXNHLGAME-26OCT03UTACBJ-UTA|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.3582): highest fidelity KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.3649): highest fidelity KXNHLAST-26OCT03UTACBJ-CBJMKNIES23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03UTACBJ-CBJMKNIES23-1|no (same contract)
- KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.7 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3582, phi -0.189)
- KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.235)
- KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.15)
- KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.419, phi -0.222)

portfolios: A EV +2.76 (adj +0.90) on $11.54, P(profit) 0.6568, adj growth 8.7 bp · B EV +3.29 (adj +1.62) on $11.93, P(profit) 0.4851, adj growth 15.7 bp · C EV +2.42 (adj +1.14) on $13.63, P(profit) 0.3981, adj growth 10.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03UTACBJ-UTA|no == KXNHLGAME-26OCT03UTACBJ-CBJ|yes

## SEA @ EDM  ·  10000 joint draws  ·  356 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.638 / away 0.362

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_SEA_win | p_overtime | goals | shots EDM/SEA | EDM/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.125 | 0.73 | 0.27 | 0.00 | 6.04 | 33.9/21.9 | 19.4/28.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.65 | 0.35 | 0.00 | 6.05 | 28.4/27.8 | 24.8/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.55 | 0.45 | 0.48 | 6.0 | 28.5/27.8 | 24.6/25.1 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.58 | 0.42 | 0.47 | 6.01 | 34.2/22.2 | 19.0/30.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.099 | 0.71 | 0.29 | 0.00 | 9.44 | 35.8/23.5 | 19.0/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.67 | 0.33 | 0.00 | 9.38 | 29.9/29.3 | 24.1/22.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 17 | 0.235 | 0.217 | +0.055 | +0.037 | $3.14 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 32 | 0.481 | 0.373 | +0.145 | +0.038 | $3.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
| Ryan Winterton: 1+ goals YES | 10 | 0.141 | 0.130 | +0.035 | +0.023 | $1.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 9 | 0.123 | 0.114 | +0.028 | +0.018 | $1.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (20.27 vs 3.73 bp); despite a smaller raw edge (+0.055 vs +0.096/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.118); KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT03SEAEDM-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (13.91 vs 11.04 bp); relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.118); KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT03SEAEDM-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: EDM offense succeeds (4+ goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03SEAEDM-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (12.12 vs 2.14 bp); relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT03SEAEDM-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: SEA offense suppressed (<= 2 goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03SEAEDM-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (8.09 vs 2.14 bp); relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5105): highest fidelity KXNHLAST-26OCT03SEAEDM-EDMMEKHOLM14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2853): highest fidelity KXNHLPTS-26OCT03SEAEDM-EDMCMCDAVID97-3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.3297): highest fidelity KXNHLGOAL-26OCT03SEAEDM-SEAKKAKKO84-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03SEAEDM-SEAKKAKKO84-1|yes (same contract)
- KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2853, phi -0.212)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 27% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.6 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5105, phi -0.305)
- KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4474, phi -0.177)
- KXNHLGOAL-26OCT03SEAEDM-SEAFGAUDREAU89-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4474, phi -0.173)

portfolios: A EV +3.21 (adj +0.64) on $11.54, P(profit) 0.654, adj growth 6.2 bp · B EV +3.55 (adj +1.67) on $9.93, P(profit) 0.7193, adj growth 16.1 bp · C EV +3.41 (adj +1.40) on $15.44, P(profit) 0.6233, adj growth 13.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ NYI  ·  10000 joint draws  ·  340 bet sides mapped, 21 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.449 / away 0.551

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_NJD_win | p_overtime | goals | shots NYI/NJD | NYI/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.56 | 0.44 | 0.00 | 5.98 | 28.0/28.0 | 24.8/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.50 | 0.50 | 0.48 | 5.88 | 27.7/27.8 | 24.5/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.59 | 0.41 | 0.00 | 9.05 | 29.5/29.5 | 24.2/23.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.53 | 0.47 | 0.00 | 3.48 | 26.5/26.6 | 24.8/24.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.067 | 0.52 | 0.48 | 0.48 | 2.74 | 26.4/26.7 | 25.3/24.9 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.065 | 0.62 | 0.38 | 0.00 | 5.99 | 33.1/22.5 | 19.6/28.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Hughes: 1+ goals NO | 63 | 0.695 | 0.677 | +0.049 | +0.031 | $4.82 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| New Jersey wins NO | 44 | 0.533 | 0.489 | +0.076 | +0.032 | $3.51 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | B |
| Kyle Palmieri: 1+ assists NO | 69 | 0.824 | 0.730 | +0.119 | +0.025 | $5.35 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03NJNYI-NJ|no; why: higher confidence-adjusted growth (9.35 vs 8.88 bp); despite a smaller raw edge (+0.049 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGAME-26OCT03NJNYI-NJ|no: REINFORCING (phi 0.217); KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no has the higher standalone adjusted growth (9.35 vs 8.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.217); they share one thesis budget; relationships: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no: REINFORCING (phi 0.217); KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: INTENTIONAL_DIVERSIFIER (phi -0.133); failure: NJD wins (incl. OT/SO)
- **Kyle Palmieri: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03NJNYI-NYIBHORVAT14-1|no; why: higher confidence-adjusted growth (6.86 vs 0.03 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0016 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGAME-26OCT03NJNYI-NJ|no: INTENTIONAL_DIVERSIFIER (phi -0.133); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.07.
- thesis NJD:SUPPRESSED (p 0.4646): highest fidelity KXNHLSPREAD-26OCT03NJNYI-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.5332): highest fidelity KXNHLGAME-26OCT03NJNYI-NJ|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3608): highest fidelity KXNHLSPREAD-26OCT03NJNYI-NJ3|no [DIRECT], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3115, phi -0.264)
- KXNHLGAME-26OCT03NJNYI-NJ|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.4668, phi -1.0)
- KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.4 pts; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.3608, phi -0.179)

portfolios: A EV +2.52 (adj +0.41) on $11.54, P(profit) 0.7002, adj growth 4.0 bp · B EV +1.85 (adj +0.67) on $13.69, P(profit) 0.749, adj growth 6.5 bp · C EV +1.30 (adj +0.60) on $15.48, P(profit) 0.4205, adj growth 5.8 bp · R EV +0.32 (adj +0.17) on $3.00, P(profit) 0.695, adj growth 6.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03NJNYI-NYI|yes == KXNHLGAME-26OCT03NJNYI-NJ|no

## DAL @ NSH  ·  10000 joint draws  ·  326 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.439 / away 0.561

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_DAL_win | p_overtime | goals | shots NSH/DAL | NSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.55 | 0.45 | 0.00 | 5.98 | 27.1/27.4 | 24.0/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.51 | 0.49 | 0.46 | 5.89 | 27.1/27.4 | 24.0/23.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.082 | 0.48 | 0.52 | 0.00 | 6.01 | 21.6/31.9 | 27.9/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.53 | 0.47 | 0.00 | 9.21 | 28.7/28.8 | 23.1/22.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.46 | 0.54 | 0.49 | 5.9 | 21.6/32.1 | 28.7/18.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.063 | 0.53 | 0.47 | 0.49 | 2.86 | 25.4/25.6 | 24.1/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Miro Heiskanen: 1+ goals NO | 86 | 0.903 | 0.891 | +0.035 | +0.023 | $5.12 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Dallas wins by over 1.5 goals NO | 67 | 0.745 | 0.705 | +0.059 | +0.019 | $3.31 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mavrik Bourque: 1+ goals YES | 18 | 0.216 | 0.206 | +0.026 | +0.015 | $1.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 71 | 0.752 | 0.740 | +0.028 | +0.016 | $3.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL2|no; why: higher confidence-adjusted growth (10.26 vs 3.88 bp); despite a smaller raw edge (+0.035 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT03DALNSH-DAL2|no: MOSTLY_INDEPENDENT (phi 0.103); KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: DAL offense succeeds (4+ goals)
- **Dallas wins by over 1.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL3|no; why: higher confidence-adjusted growth (3.88 vs 3.70 bp); relationships: KXNHLGOAL-26OCT03DALNSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.103); KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: REINFORCING (phi 0.157); failure: DAL wins by 2+
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT03DALNSH-DAL2|no has the higher standalone adjusted growth (3.88 vs 3.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.146); they share one thesis budget; relationships: KXNHLGOAL-26OCT03DALNSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLSPREAD-26OCT03DALNSH-DAL2|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: NSH offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL2|no; why: Player prop expression KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no selected over player prop KXNHLAST-26OCT03DALNSH-DALRHINTZ24-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.87 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT03DALNSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT03DALNSH-DAL2|no: REINFORCING (phi 0.157); KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis DAL:SUPPRESSED (p 0.4393): highest fidelity KXNHLTEAMTOTAL-26OCT03DALNSH-DAL4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03DALNSH-DAL2|no — Player prop expression KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no selected over player prop KXNHLAST-26OCT03DALNSH-DALRHINTZ24-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.87 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NSH:WINS (p 0.5269): highest fidelity KXNHLSPREAD-26OCT03DALNSH-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03DALNSH-DAL2|no (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.3762): highest fidelity KXNHLSPREAD-26OCT03DALNSH-DAL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT03DALNSH-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03DALNSH-DALMHEISKANEN4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3461, phi -0.157)
- KXNHLSPREAD-26OCT03DALNSH-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.255, phi -1.0)
- KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3986, phi -0.214)
- KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3461, phi -0.225)
- override: Player prop expression KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no selected over player prop KXNHLAST-26OCT03DALNSH-DALRHINTZ24-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.87 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.38 (adj +0.29) on $11.54, P(profit) 0.6345, adj growth 2.8 bp · B EV +0.76 (adj +0.39) on $12.61, P(profit) 0.6086, adj growth 3.8 bp · C EV +0.59 (adj +0.23) on $11.27, P(profit) 0.7175, adj growth 2.2 bp · R EV +0.17 (adj +0.08) on $3.00, P(profit) 0.6863, adj growth 3.2 bp

## BOS @ MIN  ·  10000 joint draws  ·  334 bet sides mapped, 7 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.646 / away 0.353

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_BOS_win | p_overtime | goals | shots MIN/BOS | MIN/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.70 | 0.30 | 0.00 | 6.05 | 28.8/28.4 | 25.8/24.3 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.102 | 0.73 | 0.27 | 0.00 | 6.02 | 34.0/22.6 | 20.3/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.52 | 0.48 | 0.46 | 5.91 | 28.9/28.6 | 25.3/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.69 | 0.31 | 0.00 | 9.35 | 30.4/30.1 | 25.2/23.1 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.54 | 0.46 | 0.44 | 5.98 | 34.4/23.1 | 19.8/31.0 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.076 | 0.73 | 0.27 | 0.00 | 9.35 | 36.1/24.1 | 19.5/27.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 11 | 0.154 | 0.142 | +0.037 | +0.025 | $1.79 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 71 | 0.830 | 0.746 | +0.106 | +0.021 | $5.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Elias Lindholm: 1+ goals YES | 19 | 0.223 | 0.214 | +0.022 | +0.013 | $1.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (13.17 vs 2.57 bp); relationships: KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: MIN offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03BOSMIN-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (4.92 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.135); failure: BOS offense succeeds (4+ goals)
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-BOSCMITTELSTADT11-1|yes; why: higher confidence-adjusted growth (2.25 vs 0.33 bp); alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.135); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.5004): highest fidelity KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.3156): highest fidelity KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.4677): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2968, phi -0.153)
- KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.0 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3156, phi -0.202)
- KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4677, phi -0.232)

portfolios: A EV +1.89 (adj +0.72) on $11.54, P(profit) 0.3811, adj growth 6.9 bp · B EV +1.52 (adj +0.63) on $8.57, P(profit) 0.2941, adj growth 6.1 bp · C EV +0.28 (adj +0.16) on $2.65, P(profit) 0.4353, adj growth 1.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ COL  ·  10000 joint draws  ·  334 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.710 / away 0.290

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_STL_win | p_overtime | goals | shots COL/STL | COL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.158 | 0.71 | 0.29 | 0.00 | 6.04 | 33.7/21.4 | 18.8/29.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.57 | 0.43 | 0.47 | 5.91 | 34.1/21.8 | 18.6/30.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.108 | 0.75 | 0.25 | 0.00 | 9.44 | 35.5/22.8 | 18.4/27.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.68 | 0.32 | 0.00 | 6.04 | 28.3/27.3 | 24.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.55 | 0.45 | 0.50 | 6.01 | 28.4/27.5 | 24.2/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.67 | 0.33 | 0.00 | 9.43 | 29.6/28.7 | 23.3/22.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 1+ goals NO | 52 | 0.606 | 0.584 | +0.069 | +0.046 | $5.48 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 10 | 0.148 | 0.135 | +0.042 | +0.029 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 24 | 0.288 | 0.275 | +0.035 | +0.022 | $1.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 63 | 0.715 | 0.670 | +0.069 | +0.024 | $1.91 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: higher confidence-adjusted growth (18.66 vs 11.03 bp); despite a smaller raw edge (+0.069 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT03STLCOL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT03STLCOL-COL3|no: REINFORCING (phi 0.178); failure: COL offense succeeds (4+ goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: higher confidence-adjusted growth (18.42 vs 11.03 bp); despite a smaller raw edge (+0.042 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT03STLCOL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT03STLCOL-COL3|no: MOSTLY_INDEPENDENT (phi 0.135); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: KXNHLGAME-26OCT03STLCOL-COL|no has the higher standalone adjusted growth (11.03 vs 5.67 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.198); relationships: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT03STLCOL-COL3|no: REINFORCING (phi 0.161); failure: STL offense suppressed (<= 2 goals)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT03STLCOL-COL2|no; why: Broad expression KXNHLSPREAD-26OCT03STLCOL-COL3|no selected over player prop KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: REINFORCING (phi 0.178); KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT03STLCOL-STLJSNUGGERUD21-1|yes: REINFORCING (phi 0.161); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.16, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.2955): highest fidelity KXNHLSPREAD-26OCT03STLCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no — Broad expression KXNHLSPREAD-26OCT03STLCOL-COL3|no selected over player prop KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis STL:OFFENSE_4PLUS (p 0.3093): highest fidelity KXNHLTEAMTOTAL-26OCT03STLCOL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.3688): highest fidelity KXNHLGAME-26OCT03STLCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no (same contract)
- KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5047, phi -0.271)
- KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4716, phi -0.205)
- KXNHLGOAL-26OCT03STLCOL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4716, phi -0.278)
- KXNHLSPREAD-26OCT03STLCOL-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4099, phi -0.757)
- override: Broad expression KXNHLSPREAD-26OCT03STLCOL-COL3|no selected over player prop KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.58 (adj +0.36) on $11.54, P(profit) 0.5591, adj growth 3.4 bp · B EV +1.90 (adj +1.21) on $11.08, P(profit) 0.5551, adj growth 11.6 bp · C EV +1.92 (adj +0.93) on $15.48, P(profit) 0.641, adj growth 9.0 bp · R EV +0.36 (adj +0.21) on $3.00, P(profit) 0.6063, adj growth 8.0 bp

## CGY @ VAN  ·  10000 joint draws  ·  310 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.503 / away 0.497

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CGY_win | p_overtime | goals | shots VAN/CGY | VAN/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.58 | 0.42 | 0.00 | 6.02 | 28.1/28.2 | 24.9/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.94 | 28.4/28.4 | 25.1/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.59 | 0.41 | 0.00 | 9.37 | 29.8/29.9 | 24.3/23.1 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.070 | 0.66 | 0.34 | 0.00 | 6.01 | 32.8/22.3 | 19.6/28.2 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.067 | 0.53 | 0.47 | 0.00 | 6.01 | 22.6/33.3 | 29.5/19.0 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.49 | 0.51 | 0.46 | 5.94 | 22.8/33.6 | 30.2/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Paul Cotter: 1+ goals NO | 82 | 0.872 | 0.858 | +0.042 | +0.028 | $5.48 | FUNDED_RESEARCH | $2 | VAN:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Drew O'Connor: 1+ goals YES | 17 | 0.223 | 0.208 | +0.043 | +0.028 | $2.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 25 | 0.309 | 0.293 | +0.046 | +0.030 | $2.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 22 | 0.263 | 0.251 | +0.031 | +0.019 | $1.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Paul Cotter: 1+ goals NO** — thesis: VAN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANBBOESER6-1|no; why: higher confidence-adjusted growth (12.05 vs 0.00 bp); alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense succeeds (4+ goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (11.73 vs 10.23 bp); despite a smaller raw edge (+0.043 vs +0.046/contract); relationships: KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (10.23 vs 4.43 bp); relationships: KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes has the higher standalone adjusted growth (10.23 vs 4.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.4345): highest fidelity KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes (same contract)
- thesis CGY:SUPPRESSED (p 0.4316): highest fidelity KXNHLGOAL-26OCT03CGYVAN-CGYYSHARANGOVICH17-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CGYVAN-CGYYSHARANGOVICH17-1|no (same contract)
- thesis VAN:SUPPRESSED (p 0.3529): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:OFFENSE_4PLUS (p 0.4345, phi -0.147)
- KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3529, phi -0.195)
- KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3529, phi -0.246)
- KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3529, phi -0.236)

portfolios: A EV +1.31 (adj +0.86) on $11.54, P(profit) 0.464, adj growth 8.4 bp · B EV +1.51 (adj +0.99) on $12.11, P(profit) 0.5678, adj growth 9.5 bp · C EV +0.74 (adj +0.47) on $8.82, P(profit) 0.3095, adj growth 4.5 bp · R EV +0.10 (adj +0.07) on $2.00, P(profit) 0.8723, adj growth 2.6 bp

## LAK @ SJS  ·  10000 joint draws  ·  308 bet sides mapped, 15 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.511 / away 0.489

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_LAK_win | p_overtime | goals | shots SJS/LAK | SJS/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.52 | 0.48 | 0.00 | 6.02 | 27.1/27.3 | 23.9/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.47 | 5.92 | 27.4/27.8 | 24.5/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.53 | 0.47 | 0.00 | 9.28 | 29.0/29.4 | 23.6/22.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.080 | 0.50 | 0.50 | 0.00 | 5.99 | 22.0/32.6 | 28.8/18.7 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.47 | 0.53 | 0.52 | 5.9 | 22.0/33.0 | 29.6/18.9 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.065 | 0.59 | 0.41 | 0.00 | 5.93 | 32.2/21.8 | 18.9/28.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mats Zuccarello: 1+ assists NO | 58 | 0.819 | 0.660 | +0.222 | +0.064 | $5.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Mats Zuccarello: 2+ assists NO | 89 | 0.984 | 0.934 | +0.087 | +0.038 | $5.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DIFFUSE | NONE | EVIDENCE_MIXED | D |
| Kiefer Sherwood: 1+ goals YES | 13 | 0.197 | 0.179 | +0.059 | +0.041 | $2.89 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (36.89 vs 7.23 bp); relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-2|no: REINFORCING (phi 0.271); KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: LAK offense succeeds (4+ goals)
- **Mats Zuccarello: 2+ assists NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: REINFORCING (phi 0.271); KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: LAK offense succeeds (4+ goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03LASJ-SJCGRAF51-1|yes; why: higher confidence-adjusted growth (29.95 vs 0.94 bp); alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-2|no: MOSTLY_INDEPENDENT (phi -0.018); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.4192): highest fidelity KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3857): highest fidelity KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.4059): highest fidelity KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no (same contract)
- KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 24.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3649, phi -0.195)
- KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; no single thesis (diffuse); fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3649, phi -0.116)
- KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4059, phi -0.211)

portfolios: A EV +3.06 (adj +0.79) on $11.54, P(profit) 0.8461, adj growth 7.8 bp · B EV +3.77 (adj +1.66) on $13.69, P(profit) 0.8543, adj growth 16.2 bp · C EV +4.26 (adj +1.88) on $15.48, P(profit) 0.8543, adj growth 18.2 bp · R EV +0.43 (adj +0.30) on $1.00, P(profit) 0.1968, adj growth 11.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
