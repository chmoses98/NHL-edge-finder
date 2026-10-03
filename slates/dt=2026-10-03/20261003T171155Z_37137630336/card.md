# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T17:11:55Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +31.68 | +9.92 | +30.44 | 0.857 | -6.13 | -15.08 | 94.71 |
| B thesis-diversified (joint) ← optimiser card | 144.88 | +29.55 | +13.00 | +27.56 | 0.839 | -7.76 | -17.45 | 125.50 |
| C best expression per thesis | 149.98 | +31.47 | +13.24 | +29.04 | 0.770 | -19.63 | -32.08 | 124.15 |
| R FUNDED research stakes | 20.00 | +2.48 | +1.44 | +2.04 | 0.644 | -5.37 | -7.44 | 0.00 |

## CHI @ BUF  ·  10000 joint draws  ·  300 bet sides mapped, 5 +EV candidates, 4 on card

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
| Ryan Greene: 1+ goals YES | 12 | 0.173 | 0.158 | +0.045 | +0.031 | $2.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 59 | 0.649 | 0.633 | +0.042 | +0.026 | $4.65 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 62 | 0.749 | 0.655 | +0.112 | +0.019 | $4.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ assists NO | 57 | 0.646 | 0.605 | +0.059 | +0.018 | $3.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CHIBUF-BUF|no; why: higher confidence-adjusted growth (18.32 vs 0.94 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: CHI offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (6.32 vs 3.01 bp); despite a smaller raw edge (+0.042 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: BUF offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03CHIBUF-CHIPKANE88-1|no; why: higher confidence-adjusted growth (3.36 vs 0.14 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0040 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CHI offense succeeds (4+ goals)
- **Tage Thompson: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no has the higher standalone adjusted growth (6.32 vs 3.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: BUF offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.2926): highest fidelity KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.3103): highest fidelity KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no (same contract)
- thesis CHI:SUPPRESSED (p 0.4879): highest fidelity KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4879, phi -0.218)
- KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4825, phi -0.265)
- KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.4 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2926, phi -0.228)
- KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4825, phi -0.259)

portfolios: A EV +1.92 (adj +0.87) on $12.16, P(profit) 0.4312, adj growth 8.4 bp · B EV +2.22 (adj +0.98) on $14.45, P(profit) 0.5738, adj growth 9.4 bp · C EV +3.52 (adj +1.61) on $20.83, P(profit) 0.5738, adj growth 15.0 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.6492, adj growth 3.3 bp

## OTT @ TOR  ·  10000 joint draws  ·  360 bet sides mapped, 7 +EV candidates, 4 on card

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
| Stephen Halliday: 1+ goals YES | 9 | 0.134 | 0.122 | +0.038 | +0.026 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ assists YES | 26 | 0.329 | 0.289 | +0.055 | +0.016 | $1.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Auston Matthews: 1+ goals NO | 65 | 0.691 | 0.680 | +0.025 | +0.014 | $3.12 | FUNDED_RESEARCH | $1 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Tim Stutzle: 1+ assists NO | 53 | 0.608 | 0.562 | +0.061 | +0.014 | $2.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (16.73 vs 3.75 bp); despite a smaller raw edge (+0.038 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.036); failure: OTT offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT03OTTTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (2.80 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: INTENTIONAL_DIVERSIFIER (phi -0.059); KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: TOR offense suppressed (<= 2 goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03OTTTOR-TORKMARCHENKO86-1|no; why: Player prop expression KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT03OTTTOR-TORKMARCHENKO86-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.84 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.059); KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: TOR offense succeeds (4+ goals)
- **Tim Stutzle: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no; why: higher confidence-adjusted growth (1.77 vs 0.97 bp); alternative not eligible: confidence-adjusted EV +0.0098 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: OTT offense succeeds (4+ goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.3964): highest fidelity KXNHLGAME-26OCT03OTTTOR-OTT|yes [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS (p 0.548): highest fidelity KXNHLGAME-26OCT03OTTTOR-OTT|yes [STRUCTURAL], best adjusted EV KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.4475): highest fidelity KXNHLAST-26OCT03OTTTOR-TORKMARCHENKO86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-TORKMARCHENKO86-1|no (same contract)
- KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3882, phi -0.158)
- KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4475, phi -0.3)
- KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3332, phi -0.268)
- KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3964, phi -0.284)
- override: Player prop expression KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT03OTTTOR-TORKMARCHENKO86-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.84 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.04 (adj +0.54) on $12.16, P(profit) 0.5122, adj growth 5.1 bp · B EV +1.46 (adj +0.73) on $9.09, P(profit) 0.6388, adj growth 7.0 bp · C EV +2.83 (adj +0.70) on $18.06, P(profit) 0.7179, adj growth 6.6 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6911, adj growth 0.8 bp

## WSH @ TBL  ·  10000 joint draws  ·  356 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.629 / away 0.371

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
| John Carlson: 1+ assists NO | 48 | 0.746 | 0.567 | +0.249 | +0.069 | $5.78 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| John Carlson: 1+ points NO | 40 | 0.657 | 0.457 | +0.240 | +0.040 | $1.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.83) | CALIBRATION_WARNING | D |
| Anthony Beauvillier: 1+ goals YES | 10 | 0.135 | 0.125 | +0.029 | +0.019 | $1.41 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.211 | 0.200 | +0.031 | +0.020 | $1.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (41.91 vs 14.35 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no: DUPLICATIVE (phi 0.808); KXNHLGOAL-26OCT03WSHTB-WSHABEAUVILLIER72-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: TBL offense succeeds (4+ goals)
- **John Carlson: 1+ points NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no; why: second expression of the same thesis: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no has the higher standalone adjusted growth (41.91 vs 14.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.808); they share one thesis budget; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: DUPLICATIVE (phi 0.808); KXNHLGOAL-26OCT03WSHTB-WSHABEAUVILLIER72-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: TBL offense succeeds (4+ goals)
- **Anthony Beauvillier: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes; why: higher confidence-adjusted growth (7.84 vs 5.74 bp); despite a smaller raw edge (+0.029 vs +0.031/contract); relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: WSH offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03WSHTB-TB|no; why: higher confidence-adjusted growth (5.74 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT03WSHTB-WSHABEAUVILLIER72-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.3217): highest fidelity KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no (same contract)
- thesis WSH:OFFENSE_4PLUS (p 0.3068): highest fidelity KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes (same contract)
- thesis TBL:OFFENSE_4PLUS (p 0.4659): highest fidelity KXNHLGOAL-26OCT03WSHTB-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03WSHTB-TBACIRELLI71-1|yes (same contract)
- KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 27.6 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4659, phi -0.21)
- KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 26.7 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4659, phi -0.242)
- KXNHLGOAL-26OCT03WSHTB-WSHABEAUVILLIER72-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4782, phi -0.174)
- KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4782, phi -0.238)

portfolios: A EV +4.58 (adj +1.15) on $12.16, P(profit) 0.7197, adj growth 11.2 bp · B EV +4.32 (adj +1.36) on $10.12, P(profit) 0.7824, adj growth 13.2 bp · C EV +5.86 (adj +1.87) on $15.44, P(profit) 0.7965, adj growth 18.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ PHI  ·  10000 joint draws  ·  370 bet sides mapped, 17 +EV candidates, 3 on card

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
| Noel Acciari: 1+ goals YES | 9 | 0.135 | 0.121 | +0.040 | +0.026 | $1.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Mark Jankowski: 1+ goals NO | 84 | 0.884 | 0.872 | +0.035 | +0.022 | $5.78 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 79 | 0.856 | 0.821 | +0.054 | +0.019 | $5.78 | FUNDED_RESEARCH | $2 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03CARPHI-CAR2|no; why: higher confidence-adjusted growth (16.38 vs 5.03 bp); despite a smaller raw edge (+0.040 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT03CARPHI-CAR3|no: MOSTLY_INDEPENDENT (phi 0.084); failure: PHI offense suppressed (<= 2 goals)
- **Mark Jankowski: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03CARPHI-CAR2|no; why: higher confidence-adjusted growth (8.61 vs 5.03 bp); despite a smaller raw edge (+0.034 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT03CARPHI-CAR3|no: MOSTLY_INDEPENDENT (phi 0.111); failure: CAR offense succeeds (4+ goals)
- **Carolina wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03CARPHI-CAR2|no; why: KXNHLSPREAD-26OCT03CARPHI-CAR2|no has the higher standalone adjusted growth (5.03 vs 4.95 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.729); relationships: KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.084); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.111); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3711): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT03CARPHI-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.4667): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03CARPHI-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.548): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03CARPHI-CAR2|no (same contract)
- KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4082, phi -0.159)
- KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3207, phi -0.175)
- KXNHLSPREAD-26OCT03CARPHI-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2405, phi -0.729)

portfolios: A EV +1.33 (adj +0.34) on $12.16, P(profit) 0.6875, adj growth 3.2 bp · B EV +1.35 (adj +0.76) on $13.31, P(profit) 0.7913, adj growth 7.3 bp · C EV +0.94 (adj +0.32) on $10.15, P(profit) 0.7595, adj growth 3.0 bp · R EV +0.22 (adj +0.10) on $4.00, P(profit) 0.7691, adj growth 3.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03CARPHI-CAR|no == KXNHLGAME-26OCT03CARPHI-PHI|yes

## MTL @ PIT  ·  10000 joint draws  ·  330 bet sides mapped, 11 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.483 / away 0.517

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
| Connor Dewar: 1+ goals YES | 12 | 0.201 | 0.180 | +0.074 | +0.052 | $3.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Filip Hallander: 1+ goals YES | 13 | 0.202 | 0.182 | +0.064 | +0.044 | $3.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 29 | 0.374 | 0.349 | +0.070 | +0.045 | $4.21 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes; why: higher confidence-adjusted growth (51.79 vs 4.26 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.827 vs 0.498); relationships: KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03MTLPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: PIT offense suppressed (<= 2 goals)
- **Filip Hallander: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (51.79 vs 34.13 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03MTLPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (51.79 vs 20.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts PIT shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10, PIT shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.3425): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.4691): highest fidelity KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.5586): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3238, phi -0.228)
- KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3238, phi -0.186)
- KXNHLGOAL-26OCT03MTLPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3238, phi -0.263)

portfolios: A EV +4.48 (adj +2.86) on $12.16, P(profit) 0.4433, adj growth 27.2 bp · B EV +4.58 (adj +3.14) on $11.08, P(profit) 0.5972, adj growth 30.1 bp · C EV +3.92 (adj +2.77) on $6.75, P(profit) 0.2013, adj growth 25.5 bp · R EV +0.46 (adj +0.29) on $2.00, P(profit) 0.3739, adj growth 11.0 bp

## UTA @ CBJ  ·  10000 joint draws  ·  342 bet sides mapped, 7 +EV candidates, 4 on card

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
| Vincent Trocheck: 1+ assists NO | 68 | 0.862 | 0.734 | +0.167 | +0.039 | $5.78 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Charlie Coyle: 1+ goals YES | 21 | 0.271 | 0.253 | +0.049 | +0.031 | $2.74 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Danton Heinen: 1+ goals YES | 10 | 0.132 | 0.121 | +0.025 | +0.015 | $1.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 18 | 0.220 | 0.209 | +0.030 | +0.019 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03UTACBJ-CBJ|yes; why: higher confidence-adjusted growth (15.58 vs 1.36 bp); relationships: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: UTA offense succeeds (4+ goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03UTACBJ-CBJ|yes; why: higher confidence-adjusted growth (12.31 vs 1.36 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CBJ offense suppressed (<= 2 goals)
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (12.31 vs 5.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CBJ offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-UTAALEE72-1|yes; why: higher confidence-adjusted growth (4.85 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.4162): highest fidelity KXNHLGAME-26OCT03UTACBJ-CBJ|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.3582): highest fidelity KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.419): highest fidelity KXNHLGAME-26OCT03UTACBJ-CBJ|yes [DIRECT], best adjusted EV KXNHLGAME-26OCT03UTACBJ-CBJ|yes (same contract)
- KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.7 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3582, phi -0.189)
- KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.235)
- KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.15)
- KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.419, phi -0.222)

portfolios: A EV +1.72 (adj +0.70) on $12.16, P(profit) 0.5312, adj growth 6.7 bp · B EV +2.51 (adj +1.02) on $11.24, P(profit) 0.4756, adj growth 9.9 bp · C EV +1.71 (adj +1.01) on $10.24, P(profit) 0.431, adj growth 9.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ EDM  ·  10000 joint draws  ·  356 bet sides mapped, 11 +EV candidates, 4 on card

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
| Alex Formenton: 1+ goals YES | 17 | 0.235 | 0.215 | +0.055 | +0.035 | $3.13 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 10 | 0.141 | 0.130 | +0.035 | +0.023 | $1.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 68 | 0.826 | 0.728 | +0.131 | +0.033 | $5.78 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Connor McDavid: 1+ assists NO | 33 | 0.481 | 0.376 | +0.135 | +0.031 | $2.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (17.67 vs 5.42 bp); despite a smaller raw edge (+0.055 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.122); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.118); failure: EDM offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03SEAEDM-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (12.12 vs 2.14 bp); relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: SEA offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (11.04 vs 9.11 bp); despite a smaller raw edge (+0.131 vs +0.135/contract); relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.122); KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: DUPLICATIVE (phi 0.442); failure: EDM offense succeeds (4+ goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no; why: second expression of the same thesis: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (11.04 vs 9.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.442); they share one thesis budget; relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.118); KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: DUPLICATIVE (phi 0.442); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5105): highest fidelity KXNHLAST-26OCT03SEAEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2853): highest fidelity KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.3297): highest fidelity KXNHLGOAL-26OCT03SEAEDM-SEAKKAKKO84-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03SEAEDM-SEAKKAKKO84-1|yes (same contract)
- KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2853, phi -0.212)
- KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4474, phi -0.177)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.1 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5105, phi -0.28)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 27% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.1 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5105, phi -0.305)

portfolios: A EV +3.44 (adj +0.60) on $12.16, P(profit) 0.6926, adj growth 5.7 bp · B EV +3.58 (adj +1.47) on $13.13, P(profit) 0.6773, adj growth 14.1 bp · C EV +3.78 (adj +1.65) on $17.52, P(profit) 0.3666, adj growth 15.5 bp · R EV +0.30 (adj +0.19) on $1.00, P(profit) 0.2346, adj growth 7.3 bp

## NJD @ NYI  ·  10000 joint draws  ·  340 bet sides mapped, 13 +EV candidates, 3 on card

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
| Luke Evangelista: 1+ assists NO | 66 | 0.839 | 0.713 | +0.164 | +0.037 | $4.93 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 64 | 0.695 | 0.679 | +0.039 | +0.023 | $3.74 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Kyle Palmieri: 1+ assists NO | 70 | 0.824 | 0.730 | +0.109 | +0.016 | $4.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03NJNYI-NJ|no; why: higher confidence-adjusted growth (14.01 vs 8.88 bp); relationships: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.05); KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: NJD offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03NJNYI-NJ|no; why: Player prop expression KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no selected over broad KXNHLGAME-26OCT03NJNYI-NJ|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.79 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.05); KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: NJD offense succeeds (4+ goals)
- **Kyle Palmieri: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT03NJNYI-6|no; why: higher confidence-adjusted growth (2.67 vs 0.28 bp); wins across more scripts (relative breadth 0.993 vs 0.749); alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.07.
- thesis NJD:SUPPRESSED (p 0.4646): highest fidelity KXNHLSPREAD-26OCT03NJNYI-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.5332): highest fidelity KXNHLGAME-26OCT03NJNYI-NJ|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no (same contract)
- thesis NYI:WINS_BY_2PLUS (p 0.3025): highest fidelity KXNHLGAME-26OCT03NJNYI-NJ|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no (same contract)
- KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.4 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3115, phi -0.167)
- KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3115, phi -0.264)
- KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.4 pts; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.3608, phi -0.179)
- override: Player prop expression KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no selected over broad KXNHLGAME-26OCT03NJNYI-NJ|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.79 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.34 (adj +0.43) on $12.16, P(profit) 0.6071, adj growth 4.2 bp · B EV +2.16 (adj +0.51) on $13.51, P(profit) 0.6916, adj growth 5.0 bp · C EV +1.24 (adj +0.52) on $7.46, P(profit) 0.5332, adj growth 4.8 bp · R EV +0.06 (adj +0.03) on $1.00, P(profit) 0.695, adj growth 1.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03NJNYI-NYI|yes == KXNHLGAME-26OCT03NJNYI-NJ|no

## DAL @ NSH  ·  10000 joint draws  ·  326 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.443 / away 0.557

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_DAL_win | p_overtime | goals | shots NSH/DAL | NSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.55 | 0.45 | 0.00 | 6.04 | 27.0/27.2 | 23.8/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.46 | 5.87 | 27.2/27.4 | 24.1/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.55 | 0.45 | 0.00 | 9.22 | 28.4/28.7 | 23.0/21.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.078 | 0.45 | 0.55 | 0.00 | 5.91 | 21.2/31.7 | 27.9/18.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.50 | 0.50 | 0.46 | 5.86 | 21.6/32.0 | 28.7/18.5 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.065 | 0.62 | 0.38 | 0.00 | 6.04 | 31.8/21.7 | 18.7/27.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dallas wins NO | 44 | 0.530 | 0.487 | +0.073 | +0.030 | $3.18 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | B |
| Dallas wins by over 2.5 goals NO | 79 | 0.846 | 0.816 | +0.045 | +0.014 | $1.26 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mikko Rantanen: 1+ goals NO | 71 | 0.754 | 0.739 | +0.029 | +0.015 | $2.93 | FUNDED_RESEARCH | $1 | DAL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 2+ assists NO | 86 | 0.918 | 0.879 | +0.049 | +0.011 | $5.73 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Dallas wins NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03DALNSH-NSH|yes; why: best adjusted growth among the thesis's expressions; relationships: KXNHLSPREAD-26OCT03DALNSH-DAL3|no: DUPLICATIVE (phi 0.453); KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: REINFORCING (phi 0.162); KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-2|no: REINFORCING (phi 0.171); failure: DAL wins (incl. OT/SO)
- **Dallas wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03DALNSH-DAL|no; why: second expression of the same thesis: KXNHLGAME-26OCT03DALNSH-DAL|no has the higher standalone adjusted growth (8.07 vs 2.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.453); they share one thesis budget; relationships: KXNHLGAME-26OCT03DALNSH-DAL|no: DUPLICATIVE (phi 0.453); KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.128); KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-2|no: REINFORCING (phi 0.165); failure: DAL wins by 2+
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03DALNSH-DAL|no; why: second expression of the same thesis: KXNHLGAME-26OCT03DALNSH-DAL|no has the higher standalone adjusted growth (8.07 vs 2.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.162); they share one thesis budget; relationships: KXNHLGAME-26OCT03DALNSH-DAL|no: REINFORCING (phi 0.162); KXNHLSPREAD-26OCT03DALNSH-DAL3|no: MOSTLY_INDEPENDENT (phi 0.128); KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-2|no: MOSTLY_INDEPENDENT (phi -0.011); failure: DAL offense succeeds (4+ goals)
- **Mikko Rantanen: 2+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03DALNSH-DAL|no; why: second expression of the same thesis: KXNHLGAME-26OCT03DALNSH-DAL|no has the higher standalone adjusted growth (8.07 vs 2.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.171); they share one thesis budget; relationships: KXNHLGAME-26OCT03DALNSH-DAL|no: REINFORCING (phi 0.171); KXNHLSPREAD-26OCT03DALNSH-DAL3|no: REINFORCING (phi 0.165); KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NSH:WINS (p 0.5305): highest fidelity KXNHLGAME-26OCT03DALNSH-NSH|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.4398): highest fidelity KXNHLSPREAD-26OCT03DALNSH-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGAME-26OCT03DALNSH-DAL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.4695, phi -1.0)
- KXNHLSPREAD-26OCT03DALNSH-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.2565, phi -0.726)
- KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3484, phi -0.225)
- KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3484, phi -0.249)

portfolios: A EV +1.25 (adj +0.36) on $12.16, P(profit) 0.668, adj growth 3.4 bp · B EV +1.02 (adj +0.36) on $13.10, P(profit) 0.5103, adj growth 3.5 bp · C EV +1.14 (adj +0.47) on $7.11, P(profit) 0.5305, adj growth 4.4 bp · R EV +0.26 (adj +0.10) on $3.00, P(profit) 0.5305, adj growth 4.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03DALNSH-NSH|yes == KXNHLGAME-26OCT03DALNSH-DAL|no

## BOS @ MIN  ·  10000 joint draws  ·  332 bet sides mapped, 2 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.645 / away 0.355

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_BOS_win | p_overtime | goals | shots MIN/BOS | MIN/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.70 | 0.30 | 0.00 | 6.05 | 28.8/28.4 | 25.8/24.3 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.102 | 0.73 | 0.27 | 0.00 | 6.02 | 34.0/22.6 | 20.3/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.52 | 0.48 | 0.46 | 5.91 | 28.9/28.6 | 25.3/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.69 | 0.31 | 0.00 | 9.35 | 30.4/30.1 | 25.2/23.1 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.54 | 0.46 | 0.44 | 5.98 | 34.4/23.1 | 19.8/31.0 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.076 | 0.73 | 0.27 | 0.00 | 9.35 | 36.1/24.1 | 19.5/27.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.5004): highest fidelity - [-], best adjusted EV - — no eligible expression

portfolios: A EV +1.49 (adj +0.64) on $4.09, P(profit) 0.2192, adj growth 5.8 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ COL  ·  10000 joint draws  ·  338 bet sides mapped, 17 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.705 / away 0.295

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
| Nathan MacKinnon: 1+ goals NO | 52 | 0.606 | 0.584 | +0.069 | +0.046 | $5.78 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Colorado wins NO | 29 | 0.369 | 0.331 | +0.064 | +0.027 | $1.47 | FUNDED_RESEARCH | $1 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | B |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (18.66 vs 7.77 bp); despite a smaller raw edge (+0.069 vs +0.122/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGAME-26OCT03STLCOL-COL|no: REINFORCING (phi 0.196); failure: COL offense succeeds (4+ goals)
- **Colorado wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no; why: KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no has the higher standalone adjusted growth (7.77 vs 7.31 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.230); relationships: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: REINFORCING (phi 0.196); failure: COL wins (incl. OT/SO)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.16, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.2955): highest fidelity KXNHLSPREAD-26OCT03STLCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no — Broad expression KXNHLSPREAD-26OCT03STLCOL-COL3|no selected over player prop KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis STL:WINS (p 0.3688): highest fidelity KXNHLGAME-26OCT03STLCOL-STL|yes [STRUCTURAL], best adjusted EV KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS_BY_2PLUS (p 0.1833): highest fidelity KXNHLGAME-26OCT03STLCOL-STL|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-STL|yes (same contract)
- KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5047, phi -0.271)
- KXNHLGAME-26OCT03STLCOL-COL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.6312, phi -1.0)
- override: Broad expression KXNHLSPREAD-26OCT03STLCOL-COL3|no selected over player prop KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.00 (adj +0.28) on $12.16, P(profit) 0.6764, adj growth 2.5 bp · B EV +1.05 (adj +0.62) on $7.25, P(profit) 0.6063, adj growth 6.0 bp · C EV +3.46 (adj +1.48) on $18.27, P(profit) 0.6743, adj growth 13.9 bp · R EV +0.47 (adj +0.26) on $3.00, P(profit) 0.7052, adj growth 9.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03STLCOL-STL|yes == KXNHLGAME-26OCT03STLCOL-COL|no

## CGY @ VAN  ·  10000 joint draws  ·  310 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.502 / away 0.498

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CGY_win | p_overtime | goals | shots VAN/CGY | VAN/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.59 | 0.41 | 0.00 | 5.96 | 28.3/28.3 | 25.2/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.52 | 0.48 | 0.46 | 5.94 | 28.4/28.4 | 25.1/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.62 | 0.38 | 0.00 | 9.33 | 29.6/29.7 | 24.1/22.8 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.069 | 0.68 | 0.32 | 0.00 | 6.05 | 33.1/22.7 | 20.0/28.3 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.069 | 0.55 | 0.45 | 0.00 | 6.01 | 22.7/33.3 | 29.9/19.1 | even strength |
| VAN shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.54 | 0.46 | 0.46 | 5.86 | 33.2/22.4 | 19.3/30.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zayne Parekh: 1+ goals NO | 85 | 0.903 | 0.886 | +0.044 | +0.027 | $4.48 | FUNDED_RESEARCH | $2 | CGY:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Drew O'Connor: 1+ goals YES | 17 | 0.220 | 0.197 | +0.040 | +0.018 | $1.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Zeev Buium: 1+ goals NO | 89 | 0.923 | 0.909 | +0.026 | +0.013 | $4.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Paul Cotter: 1+ goals NO | 84 | 0.874 | 0.864 | +0.024 | +0.015 | $4.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
- **Zayne Parekh: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03CGYVAN-VAN2|yes; why: higher confidence-adjusted growth (13.49 vs 0.10 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.0 vs 0.519); alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CGY offense succeeds (4+ goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN5|yes; why: higher confidence-adjusted growth (4.53 vs 0.22 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.903 vs 0.521); alternative not eligible: confidence-adjusted EV +0.0042 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)
- **Zeev Buium: 1+ goals NO** — thesis: VAN offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03CGYVAN-VANBBOESER6-2|no; why: higher confidence-adjusted growth (3.80 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: VAN offense succeeds (4+ goals)
- **Paul Cotter: 1+ goals NO** — thesis: VAN offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03CGYVAN-VANBBOESER6-2|no; why: higher confidence-adjusted growth (3.65 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: VAN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.4402): highest fidelity KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes (same contract)
- thesis CGY:SUPPRESSED (p 0.4302): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis VAN:SUPPRESSED (p 0.3458): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.35, phi -0.122)
- KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3458, phi -0.217)
- KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:OFFENSE_4PLUS (p 0.4402, phi -0.114)
- KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:OFFENSE_4PLUS (p 0.4402, phi -0.152)

portfolios: A EV +0.82 (adj +0.41) on $12.16, P(profit) 0.2195, adj growth 4.0 bp · B EV +0.70 (adj +0.37) on $14.15, P(profit) 0.7815, adj growth 3.7 bp · C EV +0.56 (adj +0.24) on $2.51, P(profit) 0.2199, adj growth 2.3 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.903, adj growth 2.5 bp

## LAK @ SJS  ·  10000 joint draws  ·  312 bet sides mapped, 9 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.510 / away 0.490

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_LAK_win | p_overtime | goals | shots SJS/LAK | SJS/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.52 | 0.48 | 0.00 | 6.02 | 27.3/27.5 | 24.2/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.49 | 5.92 | 27.3/27.7 | 24.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.54 | 0.46 | 0.00 | 9.3 | 29.0/29.3 | 23.6/22.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.077 | 0.44 | 0.56 | 0.00 | 6.01 | 21.8/32.4 | 28.7/18.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.49 | 0.51 | 0.48 | 5.9 | 21.8/32.7 | 29.4/18.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.52 | 0.48 | 0.00 | 3.44 | 26.1/26.3 | 24.5/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kiefer Sherwood: 1+ goals YES | 13 | 0.199 | 0.179 | +0.061 | +0.041 | $3.07 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 58 | 0.826 | 0.653 | +0.229 | +0.056 | $5.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Mason Marchment: 1+ assists NO | 67 | 0.812 | 0.713 | +0.127 | +0.028 | $5.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03LASJ-SJCGRAF51-1|yes; why: higher confidence-adjusted growth (30.64 vs 0.03 bp); alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.025); failure: SJS offense suppressed (<= 2 goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (28.62 vs 5.55 bp); relationships: KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: LAK offense succeeds (4+ goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no; why: higher confidence-adjusted growth (7.86 vs 3.94 bp); relationships: KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.4231): highest fidelity KXNHLAST-26OCT03LASJ-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.3966): highest fidelity KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3833): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3966, phi -0.198)
- KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 26.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3574, phi -0.21)
- KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.2 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3833, phi -0.202)

portfolios: A EV +3.26 (adj +0.74) on $12.16, P(profit) 0.8502, adj growth 7.3 bp · B EV +4.59 (adj +1.68) on $14.45, P(profit) 0.7393, adj growth 16.3 bp · C EV +2.51 (adj +0.60) on $15.64, P(profit) 0.474, adj growth 5.6 bp · R EV +0.44 (adj +0.30) on $1.00, P(profit) 0.1991, adj growth 11.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
