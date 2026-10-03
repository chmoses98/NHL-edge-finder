# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T19:41:31Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +33.72 | +11.41 | +32.83 | 0.868 | -4.13 | -13.44 | 109.42 |
| B thesis-diversified (joint) ← optimiser card | 145.86 | +30.73 | +15.46 | +28.51 | 0.835 | -8.14 | -17.51 | 149.60 |
| C best expression per thesis | 149.47 | +29.44 | +14.38 | +27.23 | 0.789 | -14.47 | -24.70 | 137.47 |
| R FUNDED research stakes | 18.00 | +2.38 | +1.44 | +2.09 | 0.638 | -4.70 | -6.42 | 0.00 |

## CHI @ BUF  ·  10000 joint draws  ·  300 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.669 / away 0.331

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_CHI_win | p_overtime | goals | shots BUF/CHI | BUF/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.136 | 0.72 | 0.28 | 0.00 | 6.0 | 33.3/21.3 | 18.9/28.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.71 | 0.29 | 0.00 | 6.06 | 28.0/27.2 | 24.3/23.4 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.45 | 5.93 | 33.6/21.5 | 18.4/30.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.53 | 0.47 | 0.50 | 5.97 | 27.9/27.3 | 24.0/24.6 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.089 | 0.75 | 0.25 | 0.00 | 9.32 | 35.2/22.7 | 18.3/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.67 | 0.33 | 0.00 | 9.33 | 29.7/28.9 | 23.6/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 12 | 0.173 | 0.158 | +0.045 | +0.031 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 59 | 0.649 | 0.633 | +0.042 | +0.026 | $3.99 | FUNDED_RESEARCH | $1 | BUF:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 62 | 0.749 | 0.659 | +0.112 | +0.022 | $4.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ assists NO | 57 | 0.646 | 0.605 | +0.059 | +0.018 | $2.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CHIBUF-BUF|no; why: higher confidence-adjusted growth (18.32 vs 0.94 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: CHI offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (6.32 vs 3.01 bp); despite a smaller raw edge (+0.042 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: BUF offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CHIBUF-CHIRKANTSEROV80-1|no; why: higher confidence-adjusted growth (4.63 vs 0.49 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CHI offense succeeds (4+ goals)
- **Tage Thompson: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no has the higher standalone adjusted growth (6.32 vs 3.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: BUF offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.2926): highest fidelity KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.3103): highest fidelity KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4879): highest fidelity KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4879, phi -0.218)
- KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4825, phi -0.265)
- KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.9 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2926, phi -0.228)
- KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4825, phi -0.259)

portfolios: A EV +1.82 (adj +0.84) on $11.54, P(profit) 0.4312, adj growth 8.1 bp · B EV +2.01 (adj +0.88) on $12.98, P(profit) 0.5738, adj growth 8.5 bp · C EV +2.58 (adj +1.18) on $15.27, P(profit) 0.5738, adj growth 11.2 bp · R EV +0.07 (adj +0.04) on $1.00, P(profit) 0.6492, adj growth 1.7 bp

## OTT @ TOR  ·  10000 joint draws  ·  360 bet sides mapped, 15 +EV candidates, 4 on card

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
| Stephen Halliday: 1+ goals YES | 9 | 0.134 | 0.122 | +0.038 | +0.026 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ goals NO | 64 | 0.691 | 0.677 | +0.035 | +0.021 | $4.13 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| William Eklund: 1+ assists NO | 66 | 0.736 | 0.695 | +0.060 | +0.019 | $4.83 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
| Easton Cowan: 1+ assists YES | 26 | 0.329 | 0.289 | +0.055 | +0.016 | $1.38 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (16.73 vs 3.75 bp); despite a smaller raw edge (+0.038 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: OTT offense suppressed (<= 2 goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03OTTTOR-TORKMARCHENKO86-1|no; why: higher confidence-adjusted growth (4.27 vs 3.08 bp); despite a smaller raw edge (+0.035 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.059); failure: TOR offense succeeds (4+ goals)
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTJSANDERSON85-1|no; why: KXNHLAST-26OCT03OTTTOR-OTTJSANDERSON85-1|no has the higher standalone adjusted growth (4.41 vs 3.83 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.071); relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense succeeds (4+ goals)
- **Easton Cowan: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT03OTTTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (2.80 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: INTENTIONAL_DIVERSIFIER (phi -0.059); KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:SUPPRESSED (p 0.3882): highest fidelity KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-OTTJSANDERSON85-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.4475): highest fidelity KXNHLAST-26OCT03OTTTOR-TORKMARCHENKO86-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS (p 0.548): highest fidelity KXNHLGAME-26OCT03OTTTOR-OTT|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3882, phi -0.158)
- KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3332, phi -0.268)
- KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3964, phi -0.222)
- KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4475, phi -0.3)

portfolios: A EV +1.93 (adj +0.33) on $11.54, P(profit) 0.6145, adj growth 3.2 bp · B EV +1.62 (adj +0.83) on $12.07, P(profit) 0.6561, adj growth 8.0 bp · C EV +1.82 (adj +0.64) on $15.57, P(profit) 0.7178, adj growth 6.1 bp · R EV +0.11 (adj +0.06) on $2.00, P(profit) 0.6911, adj growth 2.4 bp

## WSH @ TBL  ·  10000 joint draws  ·  356 bet sides mapped, 12 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.639 / away 0.361

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
| John Carlson: 1+ assists NO | 48 | 0.746 | 0.567 | +0.249 | +0.069 | $5.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.211 | 0.200 | +0.031 | +0.020 | $1.44 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (41.91 vs 11.79 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: TBL offense succeeds (4+ goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03WSHTB-TB|no; why: higher confidence-adjusted growth (5.74 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.3217): highest fidelity KXNHLAST-26OCT03WSHTB-TBNKUCHEROV86-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.3068): highest fidelity KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes (same contract)
- thesis TBL:OFFENSE_4PLUS (p 0.4659): highest fidelity KXNHLAST-26OCT03WSHTB-TBCDASTOUS51-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT03WSHTB-TBCDASTOUS51-1|yes (same contract)
- KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 27.6 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4659, phi -0.21)
- KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4782, phi -0.238)

portfolios: A EV +4.67 (adj +1.00) on $11.54, P(profit) 0.7462, adj growth 9.7 bp · B EV +2.85 (adj +0.88) on $6.63, P(profit) 0.7965, adj growth 8.6 bp · C EV +4.13 (adj +1.26) on $10.47, P(profit) 0.7965, adj growth 12.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ PHI  ·  10000 joint draws  ·  370 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.456 / away 0.544

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.134 | 0.51 | 0.49 | 0.00 | 5.99 | 20.5/32.0 | 28.4/17.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.49 | 0.51 | 0.47 | 5.85 | 20.6/32.1 | 28.8/17.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.55 | 0.45 | 0.00 | 5.96 | 25.8/26.5 | 23.1/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.55 | 0.45 | 0.46 | 5.9 | 25.8/26.8 | 23.6/22.4 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.073 | 0.54 | 0.46 | 0.47 | 2.74 | 19.2/30.9 | 29.3/17.7 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.070 | 0.51 | 0.49 | 0.00 | 3.44 | 19.3/30.6 | 28.8/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Couturier: 1+ goals YES | 10 | 0.176 | 0.155 | +0.070 | +0.048 | $2.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Noel Acciari: 1+ goals YES | 8 | 0.135 | 0.120 | +0.050 | +0.035 | $2.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Mark Jankowski: 1+ goals NO | 84 | 0.884 | 0.872 | +0.035 | +0.022 | $5.19 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 18 | 0.219 | 0.206 | +0.028 | +0.016 | $1.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03CARPHI-CAR2|no; why: higher confidence-adjusted growth (51.28 vs 5.03 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PHI offense suppressed (<= 2 goals)
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (51.28 vs 33.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: PHI offense suppressed (<= 2 goals)
- **Mark Jankowski: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03CARPHI-CAR2|no; why: higher confidence-adjusted growth (8.61 vs 5.03 bp); despite a smaller raw edge (+0.034 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: CAR offense succeeds (4+ goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (51.28 vs 3.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3711): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.4667): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03CARPHI-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.548): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03CARPHI-CAR2|no (same contract)
- KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4082, phi -0.21)
- KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4082, phi -0.159)
- KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3207, phi -0.175)
- KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4082, phi -0.227)

portfolios: A EV +2.75 (adj +1.51) on $11.54, P(profit) 0.5938, adj growth 14.3 bp · B EV +3.59 (adj +2.46) on $11.44, P(profit) 0.4241, adj growth 23.6 bp · C EV +3.03 (adj +1.95) on $8.59, P(profit) 0.1761, adj growth 18.4 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.8839, adj growth 2.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03CARPHI-CAR|no == KXNHLGAME-26OCT03CARPHI-PHI|yes

## MTL @ PIT  ·  10000 joint draws  ·  330 bet sides mapped, 11 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.484 / away 0.516

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
| Connor Dewar: 1+ goals YES | 12 | 0.201 | 0.180 | +0.074 | +0.052 | $3.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Filip Hallander: 1+ goals YES | 13 | 0.202 | 0.183 | +0.064 | +0.045 | $2.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 29 | 0.374 | 0.352 | +0.070 | +0.047 | $3.99 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
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

portfolios: A EV +4.25 (adj +2.76) on $11.54, P(profit) 0.4433, adj growth 26.4 bp · B EV +4.19 (adj +2.93) on $10.22, P(profit) 0.5972, adj growth 28.2 bp · C EV +2.66 (adj +1.89) on $4.59, P(profit) 0.2013, adj growth 17.8 bp · R EV +0.23 (adj +0.16) on $1.00, P(profit) 0.3739, adj growth 6.0 bp

## UTA @ CBJ  ·  10000 joint draws  ·  342 bet sides mapped, 10 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.491 / away 0.509

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
| Charlie Coyle: 1+ goals YES | 20 | 0.271 | 0.252 | +0.059 | +0.041 | $3.12 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 67 | 0.862 | 0.727 | +0.176 | +0.042 | $5.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Lawson Crouse: 1+ goals YES | 18 | 0.220 | 0.209 | +0.030 | +0.019 | $1.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-CBJSMONAHAN23-1|yes; why: higher confidence-adjusted growth (21.19 vs 2.97 bp); relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CBJ offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03UTACBJ-CBJ|yes; why: higher confidence-adjusted growth (18.00 vs 1.36 bp); relationships: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: UTA offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-UTAALEE72-1|yes; why: higher confidence-adjusted growth (4.85 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.029); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.4162): highest fidelity KXNHLGAME-26OCT03UTACBJ-CBJ|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.3582): highest fidelity KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.419): highest fidelity KXNHLGAME-26OCT03UTACBJ-CBJ|yes [DIRECT], best adjusted EV KXNHLGAME-26OCT03UTACBJ-CBJ|yes (same contract)
- KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.235)
- KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.7 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3582, phi -0.189)
- KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.419, phi -0.222)

portfolios: A EV +1.92 (adj +0.82) on $11.54, P(profit) 0.5908, adj growth 8.0 bp · B EV +2.44 (adj +1.06) on $9.75, P(profit) 0.406, adj growth 10.3 bp · C EV +1.96 (adj +1.14) on $14.70, P(profit) 0.4284, adj growth 10.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ EDM  ·  10000 joint draws  ·  356 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.639 / away 0.361

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
| Alex Formenton: 1+ goals YES | 16 | 0.235 | 0.213 | +0.065 | +0.044 | $3.40 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 10 | 0.141 | 0.130 | +0.035 | +0.023 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 68 | 0.826 | 0.728 | +0.131 | +0.033 | $5.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Connor McDavid: 1+ assists NO | 33 | 0.481 | 0.376 | +0.135 | +0.031 | $2.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (29.44 vs 6.67 bp); despite a smaller raw edge (+0.065 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.122); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.118); failure: EDM offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03SEAEDM-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (12.12 vs 2.14 bp); relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: SEA offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (11.04 vs 9.11 bp); despite a smaller raw edge (+0.131 vs +0.135/contract); relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.122); KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: DUPLICATIVE (phi 0.442); failure: EDM offense succeeds (4+ goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no; why: second expression of the same thesis: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (11.04 vs 9.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.442); they share one thesis budget; relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.118); KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: DUPLICATIVE (phi 0.442); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5105): highest fidelity KXNHLAST-26OCT03SEAEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2853): highest fidelity KXNHLPTS-26OCT03SEAEDM-EDMCMCDAVID97-3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.3297): highest fidelity KXNHLGOAL-26OCT03SEAEDM-SEAKKAKKO84-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03SEAEDM-SEAKKAKKO84-1|yes (same contract)
- KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2853, phi -0.212)
- KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4474, phi -0.177)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.1 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5105, phi -0.28)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 27% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.1 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5105, phi -0.305)

portfolios: A EV +2.95 (adj +0.55) on $11.54, P(profit) 0.654, adj growth 5.2 bp · B EV +3.70 (adj +1.66) on $12.46, P(profit) 0.6773, adj growth 16.1 bp · C EV +3.53 (adj +1.67) on $16.89, P(profit) 0.3666, adj growth 16.0 bp · R EV +0.38 (adj +0.26) on $1.00, P(profit) 0.2346, adj growth 9.9 bp

## NJD @ NYI  ·  10000 joint draws  ·  340 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.447 / away 0.553

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
| Jack Hughes: 1+ goals NO | 63 | 0.695 | 0.677 | +0.049 | +0.031 | $3.36 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| New Jersey wins NO | 44 | 0.533 | 0.489 | +0.076 | +0.032 | $2.09 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | B |
| Timo Meier: 1+ goals NO | 73 | 0.783 | 0.769 | +0.040 | +0.025 | $3.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Kyle Palmieri: 1+ assists NO | 69 | 0.824 | 0.727 | +0.119 | +0.022 | $3.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03NJNYI-NJ|no; why: higher confidence-adjusted growth (9.35 vs 8.88 bp); despite a smaller raw edge (+0.049 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGAME-26OCT03NJNYI-NJ|no: REINFORCING (phi 0.217); KXNHLGOAL-26OCT03NJNYI-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no has the higher standalone adjusted growth (9.35 vs 8.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.217); they share one thesis budget; relationships: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no: REINFORCING (phi 0.217); KXNHLGOAL-26OCT03NJNYI-NJTMEIER28-1|no: REINFORCING (phi 0.16); KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: INTENTIONAL_DIVERSIFIER (phi -0.133); failure: NJD wins (incl. OT/SO)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT03NJNYI-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT03NJNYI-NJAMANTHA39-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGAME-26OCT03NJNYI-NJ|no: REINFORCING (phi 0.16); KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: NJD offense succeeds (4+ goals)
- **Kyle Palmieri: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03NJNYI-NYIBHORVAT14-1|no; why: higher confidence-adjusted growth (5.22 vs 0.03 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0016 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGAME-26OCT03NJNYI-NJ|no: INTENTIONAL_DIVERSIFIER (phi -0.133); KXNHLGOAL-26OCT03NJNYI-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.07.
- thesis NJD:SUPPRESSED (p 0.4646): highest fidelity KXNHLSPREAD-26OCT03NJNYI-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no — Player prop expression KXNHLGOAL-26OCT03NJNYI-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT03NJNYI-NJAMANTHA39-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NYI:WINS (p 0.5332): highest fidelity KXNHLGAME-26OCT03NJNYI-NJ|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3608): highest fidelity KXNHLSPREAD-26OCT03NJNYI-NJ3|no [DIRECT], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3115, phi -0.264)
- KXNHLGAME-26OCT03NJNYI-NJ|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.4668, phi -1.0)
- KXNHLGOAL-26OCT03NJNYI-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3115, phi -0.231)
- KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.3608, phi -0.179)
- override: Player prop expression KXNHLGOAL-26OCT03NJNYI-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT03NJNYI-NJAMANTHA39-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.05 (adj +0.53) on $11.54, P(profit) 0.7604, adj growth 5.2 bp · B EV +1.44 (adj +0.55) on $12.98, P(profit) 0.6494, adj growth 5.4 bp · C EV +1.49 (adj +0.69) on $17.74, P(profit) 0.4205, adj growth 6.6 bp · R EV +0.24 (adj +0.12) on $2.00, P(profit) 0.5332, adj growth 4.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03NJNYI-NYI|yes == KXNHLGAME-26OCT03NJNYI-NJ|no

## DAL @ NSH  ·  10000 joint draws  ·  326 bet sides mapped, 12 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.446 / away 0.554

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
| Miro Heiskanen: 1+ goals NO | 86 | 0.903 | 0.891 | +0.035 | +0.023 | $4.80 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Dallas wins NO | 44 | 0.527 | 0.485 | +0.070 | +0.028 | $2.54 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | B |
| Lian Bichsel: 1+ goals NO | 93 | 0.957 | 0.948 | +0.022 | +0.013 | $4.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03DALNSH-DAL|no; why: higher confidence-adjusted growth (10.26 vs 7.05 bp); despite a smaller raw edge (+0.035 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGAME-26OCT03DALNSH-DAL|no: MOSTLY_INDEPENDENT (phi 0.1); KXNHLGOAL-26OCT03DALNSH-DALLBICHSEL6-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: DAL offense succeeds (4+ goals)
- **Dallas wins NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03DALNSH-NSH|yes; why: best adjusted growth among the thesis's expressions; relationships: KXNHLGOAL-26OCT03DALNSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.1); KXNHLGOAL-26OCT03DALNSH-DALLBICHSEL6-1|no: MOSTLY_INDEPENDENT (phi 0.059); failure: DAL wins (incl. OT/SO)
- **Lian Bichsel: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT03DALNSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGAME-26OCT03DALNSH-DAL|no: MOSTLY_INDEPENDENT (phi 0.059); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis DAL:SUPPRESSED (p 0.4393): highest fidelity KXNHLSPREAD-26OCT03DALNSH-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-DAL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS (p 0.5269): highest fidelity KXNHLGAME-26OCT03DALNSH-DAL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-DAL|no (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.3762): highest fidelity KXNHLSPREAD-26OCT03DALNSH-DAL3|no [DIRECT], best adjusted EV KXNHLGAME-26OCT03DALNSH-DAL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03DALNSH-DALMHEISKANEN4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3461, phi -0.157)
- KXNHLGAME-26OCT03DALNSH-DAL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.4731, phi -1.0)
- KXNHLGOAL-26OCT03DALNSH-DALLBICHSEL6-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3461, phi -0.1)

portfolios: A EV +1.54 (adj +0.40) on $11.54, P(profit) 0.594, adj growth 3.8 bp · B EV +0.69 (adj +0.35) on $12.14, P(profit) 0.4752, adj growth 3.4 bp · C EV +0.85 (adj +0.38) on $11.59, P(profit) 0.5101, adj growth 3.6 bp · R EV +0.23 (adj +0.11) on $3.00, P(profit) 0.4908, adj growth 4.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03DALNSH-NSH|yes == KXNHLGAME-26OCT03DALNSH-DAL|no

## BOS @ MIN  ·  10000 joint draws  ·  334 bet sides mapped, 6 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.644 / away 0.356

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
| Yakov Trenin: 1+ goals YES | 11 | 0.154 | 0.142 | +0.037 | +0.025 | $1.68 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 23 | 0.279 | 0.265 | +0.036 | +0.023 | $1.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 72 | 0.830 | 0.752 | +0.096 | +0.018 | $5.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (13.17 vs 6.15 bp); relationships: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT03BOSMIN-7|yes; why: higher confidence-adjusted growth (6.15 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.87 vs 0.661); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: MIN offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03BOSMIN-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (3.62 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.5004): highest fidelity KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.3156): highest fidelity KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.4677): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2968, phi -0.153)
- KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2968, phi -0.207)
- KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3156, phi -0.202)

portfolios: A EV +1.90 (adj +0.78) on $11.54, P(profit) 0.3811, adj growth 7.5 bp · B EV +1.49 (adj +0.66) on $8.72, P(profit) 0.3506, adj growth 6.4 bp · C EV +0.53 (adj +0.32) on $3.87, P(profit) 0.4353, adj growth 3.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ COL  ·  10000 joint draws  ·  338 bet sides mapped, 18 +EV candidates, 4 on card

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
| Nathan MacKinnon: 1+ goals NO | 52 | 0.606 | 0.584 | +0.069 | +0.046 | $5.19 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Colorado wins NO | 28 | 0.369 | 0.327 | +0.075 | +0.033 | $1.41 | FUNDED_RESEARCH | $1 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | B |
| Nathan MacKinnon: 1+ assists NO | 36 | 0.498 | 0.405 | +0.122 | +0.029 | $2.35 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.74) | EVIDENCE_MIXED | D |
| Jimmy Snuggerud: 1+ goals YES | 24 | 0.288 | 0.275 | +0.035 | +0.022 | $1.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: higher confidence-adjusted growth (18.66 vs 11.03 bp); despite a smaller raw edge (+0.069 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGAME-26OCT03STLCOL-COL|no: REINFORCING (phi 0.196); KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03STLCOL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: COL offense succeeds (4+ goals)
- **Colorado wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (11.03 vs 7.77 bp); despite a smaller raw edge (+0.075 vs +0.122/contract); relationships: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: REINFORCING (phi 0.196); KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no: REINFORCING (phi 0.23); KXNHLGOAL-26OCT03STLCOL-STLJSNUGGERUD21-1|yes: REINFORCING (phi 0.198); failure: COL wins (incl. OT/SO)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no has the higher standalone adjusted growth (18.66 vs 7.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGAME-26OCT03STLCOL-COL|no: REINFORCING (phi 0.23); KXNHLGOAL-26OCT03STLCOL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: COL offense succeeds (4+ goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: second expression of the same thesis: KXNHLGAME-26OCT03STLCOL-COL|no has the higher standalone adjusted growth (11.03 vs 5.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.198); they share one thesis budget; relationships: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGAME-26OCT03STLCOL-COL|no: REINFORCING (phi 0.198); KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.024); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.16, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.2955): highest fidelity KXNHLSPREAD-26OCT03STLCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT03STLCOL-COL3|no less than the minimum stake; KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no kept
- thesis STL:WINS (p 0.3688): highest fidelity KXNHLGAME-26OCT03STLCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3093): highest fidelity KXNHLTEAMTOTAL-26OCT03STLCOL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5047, phi -0.271)
- KXNHLGAME-26OCT03STLCOL-COL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.6312, phi -1.0)
- KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 26% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5047, phi -0.307)
- KXNHLGOAL-26OCT03STLCOL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4716, phi -0.278)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT03STLCOL-COL3|no less than the minimum stake; KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no kept

portfolios: A EV +4.01 (adj +0.54) on $11.54, P(profit) 0.6914, adj growth 4.9 bp · B EV +2.00 (adj +0.92) on $10.51, P(profit) 0.5578, adj growth 8.9 bp · C EV +1.63 (adj +0.92) on $9.95, P(profit) 0.6063, adj growth 8.8 bp · R EV +0.51 (adj +0.28) on $3.00, P(profit) 0.7052, adj growth 10.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03STLCOL-STL|yes == KXNHLGAME-26OCT03STLCOL-COL|no

## CGY @ VAN  ·  10000 joint draws  ·  310 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

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
| Drew O'Connor: 1+ goals YES | 17 | 0.223 | 0.208 | +0.043 | +0.028 | $1.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Zayne Parekh: 1+ goals NO | 85 | 0.900 | 0.884 | +0.041 | +0.025 | $4.73 | FUNDED_RESEARCH | $2 | CGY:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Paul Cotter: 1+ goals NO | 82 | 0.872 | 0.857 | +0.042 | +0.026 | $4.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 26 | 0.309 | 0.295 | +0.036 | +0.021 | $1.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (11.73 vs 4.90 bp); relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: VAN offense suppressed (<= 2 goals)
- **Zayne Parekh: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CGYVAN-CGYYSHARANGOVICH17-1|no; why: higher confidence-adjusted growth (11.19 vs 0.71 bp); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CGY offense succeeds (4+ goals)
- **Paul Cotter: 1+ goals NO** — thesis: VAN offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03CGYVAN-VANBBOESER6-2|no; why: higher confidence-adjusted growth (10.98 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: VAN offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (4.90 vs 4.43 bp); relationships: KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.4345): highest fidelity KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes (same contract)
- thesis VAN:SUPPRESSED (p 0.3529): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis CGY:SUPPRESSED (p 0.4316): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3529, phi -0.195)
- KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.347, phi -0.129)
- KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:OFFENSE_4PLUS (p 0.4345, phi -0.147)
- KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3529, phi -0.246)

portfolios: A EV +0.94 (adj +0.61) on $11.54, P(profit) 0.2223, adj growth 5.9 bp · B EV +1.13 (adj +0.71) on $12.98, P(profit) 0.414, adj growth 6.9 bp · C EV +0.33 (adj +0.19) on $2.50, P(profit) 0.3095, adj growth 1.8 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.8998, adj growth 2.3 bp

## LAK @ SJS  ·  10000 joint draws  ·  308 bet sides mapped, 13 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.513 / away 0.487

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
| Mats Zuccarello: 1+ assists NO | 58 | 0.819 | 0.660 | +0.222 | +0.064 | $5.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Mats Zuccarello: 2+ assists NO | 89 | 0.984 | 0.934 | +0.087 | +0.038 | $5.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DIFFUSE | NONE | EVIDENCE_MIXED | D |
| Kiefer Sherwood: 1+ goals YES | 13 | 0.197 | 0.179 | +0.059 | +0.041 | $2.74 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (36.89 vs 7.23 bp); relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-2|no: REINFORCING (phi 0.271); KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: LAK offense succeeds (4+ goals)
- **Mats Zuccarello: 2+ assists NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: REINFORCING (phi 0.271); KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: LAK offense succeeds (4+ goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03LASJ-SJCGRAF51-1|yes; why: higher confidence-adjusted growth (29.95 vs 0.94 bp); alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-2|no: MOSTLY_INDEPENDENT (phi -0.018); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.4192): highest fidelity KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3857): highest fidelity KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.3649): highest fidelity KXNHLAST-26OCT03LASJ-LAALAFERRIERE14-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-LAALAFERRIERE14-1|yes (same contract)
- KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 24.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3649, phi -0.195)
- KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; no single thesis (diffuse); fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3649, phi -0.116)
- KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4059, phi -0.211)

portfolios: A EV +3.00 (adj +0.74) on $11.54, P(profit) 0.8461, adj growth 7.2 bp · B EV +3.57 (adj +1.57) on $12.98, P(profit) 0.8543, adj growth 15.3 bp · C EV +4.89 (adj +2.15) on $17.74, P(profit) 0.8543, adj growth 20.8 bp · R EV +0.43 (adj +0.30) on $1.00, P(profit) 0.1968, adj growth 11.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
