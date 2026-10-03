# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T16:23:59Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.97 | +32.73 | +10.91 | +30.47 | 0.842 | -7.89 | -17.68 | 103.71 |
| B thesis-diversified (joint) ← optimiser card | 147.31 | +30.02 | +14.19 | +28.47 | 0.830 | -8.86 | -18.78 | 136.90 |
| C best expression per thesis | 150.00 | +31.79 | +14.38 | +28.62 | 0.762 | -21.72 | -33.97 | 134.50 |
| R FUNDED research stakes | 22.00 | +2.25 | +1.27 | +2.03 | 0.644 | -4.60 | -6.26 | 0.00 |

## CHI @ BUF  ·  10000 joint draws  ·  316 bet sides mapped, 5 +EV candidates, 4 on card

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
| Ryan Greene: 1+ goals YES | 12 | 0.168 | 0.154 | +0.040 | +0.027 | $1.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 59 | 0.649 | 0.631 | +0.042 | +0.024 | $4.28 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 64 | 0.752 | 0.676 | +0.096 | +0.020 | $4.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ assists NO | 57 | 0.646 | 0.605 | +0.059 | +0.018 | $3.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CHIBUF-BUF|no; why: higher confidence-adjusted growth (14.03 vs 0.94 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.021); failure: CHI offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (5.17 vs 3.01 bp); despite a smaller raw edge (+0.042 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: BUF offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CHIBUF-CHIRKANTSEROV80-1|no; why: higher confidence-adjusted growth (3.78 vs 0.21 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: CHI offense succeeds (4+ goals)
- **Tage Thompson: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no has the higher standalone adjusted growth (5.17 vs 3.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: BUF offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.2926): highest fidelity KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.3103): highest fidelity KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no (same contract)
- thesis CHI:SUPPRESSED (p 0.4879): highest fidelity KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4879, phi -0.219)
- KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4825, phi -0.265)
- KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.7 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2926, phi -0.237)
- KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4825, phi -0.259)

portfolios: A EV +1.65 (adj +0.74) on $11.91, P(profit) 0.4277, adj growth 7.1 bp · B EV +1.93 (adj +0.83) on $14.12, P(profit) 0.5729, adj growth 8.0 bp · C EV +2.87 (adj +1.30) on $19.50, P(profit) 0.5729, adj growth 12.1 bp · R EV +0.14 (adj +0.08) on $2.00, P(profit) 0.6492, adj growth 2.9 bp

## OTT @ TOR  ·  10000 joint draws  ·  356 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.511 / away 0.489

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
| Stephen Halliday: 1+ goals YES | 9 | 0.134 | 0.122 | +0.038 | +0.026 | $1.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals NO | 80 | 0.838 | 0.826 | +0.027 | +0.015 | $5.65 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| William Eklund: 1+ assists NO | 66 | 0.736 | 0.693 | +0.060 | +0.017 | $4.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
| Easton Cowan: 1+ assists YES | 26 | 0.329 | 0.289 | +0.055 | +0.016 | $1.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (16.73 vs 3.75 bp); despite a smaller raw edge (+0.038 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-TORECOWAN53-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: OTT offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03OTTTOR-TORKMARCHENKO86-1|no; why: higher confidence-adjusted growth (3.28 vs 2.07 bp); despite a smaller raw edge (+0.027 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: TOR offense succeeds (4+ goals)
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-2|no; why: higher confidence-adjusted growth (2.91 vs 1.15 bp); alternative not eligible: confidence-adjusted EV +0.0077 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLGOAL-26OCT03OTTTOR-TORECOWAN53-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense succeeds (4+ goals)
- **Easton Cowan: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03OTTTOR-TORJTAVARES91-2|yes; why: higher confidence-adjusted growth (2.80 vs 0.00 bp); alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT03OTTTOR-TORECOWAN53-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.3964): highest fidelity KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3882): highest fidelity KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no (same contract)
- thesis TOR:OFFENSE_4PLUS (p 0.3332): highest fidelity KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes (same contract)
- KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3882, phi -0.158)
- KXNHLGOAL-26OCT03OTTTOR-TORECOWAN53-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3332, phi -0.165)
- KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3964, phi -0.222)
- KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4475, phi -0.3)

portfolios: A EV +1.84 (adj +0.40) on $11.91, P(profit) 0.5971, adj growth 3.8 bp · B EV +1.65 (adj +0.82) on $13.63, P(profit) 0.6793, adj growth 7.9 bp · C EV +2.68 (adj +0.68) on $18.87, P(profit) 0.7315, adj growth 6.3 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.8384, adj growth 1.4 bp

## WSH @ TBL  ·  10000 joint draws  ·  352 bet sides mapped, 8 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.615 / away 0.386

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
| John Carlson: 1+ assists NO | 48 | 0.746 | 0.563 | +0.249 | +0.066 | $5.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.211 | 0.200 | +0.031 | +0.020 | $1.58 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 11 | 0.144 | 0.133 | +0.027 | +0.016 | $1.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (38.06 vs 8.53 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT03WSHTB-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: TBL offense succeeds (4+ goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03WSHTB-TB|no; why: higher confidence-adjusted growth (5.74 vs 0.08 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT03WSHTB-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (5.74 vs 5.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.3217): highest fidelity KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no (same contract)
- thesis WSH:OFFENSE_4PLUS (p 0.3068): highest fidelity KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes (same contract)
- thesis TBL:OFFENSE_4PLUS (p 0.4659): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 28.1 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4659, phi -0.21)
- KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4782, phi -0.238)
- KXNHLGOAL-26OCT03WSHTB-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4782, phi -0.185)

portfolios: A EV +4.24 (adj +1.00) on $11.91, P(profit) 0.7197, adj growth 9.7 bp · B EV +3.38 (adj +1.09) on $8.42, P(profit) 0.8257, adj growth 10.6 bp · C EV +5.47 (adj +1.63) on $12.76, P(profit) 0.7965, adj growth 15.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ PHI  ·  10000 joint draws  ·  368 bet sides mapped, 17 +EV candidates, 4 on card

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
| Sean Couturier: 1+ goals YES | 10 | 0.176 | 0.155 | +0.070 | +0.048 | $3.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Noel Acciari: 1+ goals YES | 9 | 0.135 | 0.121 | +0.040 | +0.026 | $1.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Mark Jankowski: 1+ goals NO | 84 | 0.884 | 0.872 | +0.035 | +0.022 | $5.65 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 18 | 0.219 | 0.206 | +0.028 | +0.016 | $1.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03CARPHI-CAR2|no; why: higher confidence-adjusted growth (51.28 vs 5.03 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PHI offense suppressed (<= 2 goals)
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (51.28 vs 16.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: PHI offense suppressed (<= 2 goals)
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

portfolios: A EV +3.03 (adj +1.59) on $11.91, P(profit) 0.5044, adj growth 15.1 bp · B EV +3.28 (adj +2.20) on $11.93, P(profit) 0.4241, adj growth 21.1 bp · C EV +4.26 (adj +2.74) on $12.07, P(profit) 0.1761, adj growth 25.2 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.8839, adj growth 2.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03CARPHI-CAR|no == KXNHLGAME-26OCT03CARPHI-PHI|yes

## MTL @ PIT  ·  10000 joint draws  ·  326 bet sides mapped, 10 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.468 / away 0.532

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
| Filip Hallander: 1+ goals YES | 13 | 0.202 | 0.182 | +0.064 | +0.044 | $3.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.201 | 0.181 | +0.063 | +0.043 | $3.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 31 | 0.374 | 0.353 | +0.049 | +0.028 | $2.67 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Filip Hallander: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (34.13 vs 33.10 bp); relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03MTLPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes; why: higher confidence-adjusted growth (33.10 vs 7.20 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.827 vs 0.442); relationships: KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03MTLPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (33.10 vs 7.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts PIT shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10, PIT shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4691): highest fidelity KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS_BY_2PLUS (p 0.3425): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.5586): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3238, phi -0.186)
- KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3238, phi -0.228)
- KXNHLGOAL-26OCT03MTLPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3238, phi -0.263)

portfolios: A EV +4.50 (adj +2.52) on $11.91, P(profit) 0.463, adj growth 23.4 bp · B EV +3.28 (adj +2.18) on $8.88, P(profit) 0.3624, adj growth 20.9 bp · C EV +2.55 (adj +1.73) on $5.56, P(profit) 0.2013, adj growth 16.1 bp · R EV +0.15 (adj +0.09) on $1.00, P(profit) 0.3739, adj growth 3.3 bp

## UTA @ CBJ  ·  10000 joint draws  ·  342 bet sides mapped, 6 +EV candidates, 4 on card

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
| Vincent Trocheck: 1+ assists NO | 67 | 0.862 | 0.727 | +0.176 | +0.042 | $5.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Charlie Coyle: 1+ goals YES | 21 | 0.271 | 0.253 | +0.049 | +0.031 | $2.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Conor Garland: 1+ goals NO | 82 | 0.863 | 0.851 | +0.033 | +0.021 | $5.33 | FUNDED_RESEARCH | $2 | CBJ:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Danton Heinen: 1+ goals YES | 10 | 0.132 | 0.121 | +0.025 | +0.015 | $1.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03UTACBJ-CBJ|yes; why: higher confidence-adjusted growth (18.00 vs 1.36 bp); relationships: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: UTA offense succeeds (4+ goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-CBJSMONAHAN23-1|yes; why: higher confidence-adjusted growth (12.31 vs 2.07 bp); relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: CBJ offense suppressed (<= 2 goals)
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03UTACBJ-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (6.91 vs 0.20 bp); despite a smaller raw edge (+0.033 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CBJ offense succeeds (4+ goals)
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (12.31 vs 5.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.4162): highest fidelity KXNHLGAME-26OCT03UTACBJ-CBJ|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.419): highest fidelity KXNHLGAME-26OCT03UTACBJ-CBJ|yes [DIRECT], best adjusted EV KXNHLGAME-26OCT03UTACBJ-CBJ|yes (same contract)
- thesis CBJ:WINS (p 0.5385): highest fidelity KXNHLGAME-26OCT03UTACBJ-CBJ|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03UTACBJ-CBJ|yes (same contract)
- KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.7 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3582, phi -0.189)
- KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.235)
- KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4162, phi -0.154)
- KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.15)

portfolios: A EV +1.74 (adj +0.70) on $11.91, P(profit) 0.5312, adj growth 6.8 bp · B EV +2.37 (adj +0.95) on $14.14, P(profit) 0.8269, adj growth 9.3 bp · C EV +1.15 (adj +0.69) on $6.15, P(profit) 0.2706, adj growth 6.4 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.8634, adj growth 2.0 bp

## SEA @ EDM  ·  10000 joint draws  ·  356 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.643 / away 0.357

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_SEA_win | p_overtime | goals | shots EDM/SEA | EDM/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.126 | 0.73 | 0.27 | 0.00 | 6.05 | 33.9/21.9 | 19.4/28.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.65 | 0.35 | 0.00 | 6.04 | 28.4/27.9 | 24.9/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.54 | 0.46 | 0.49 | 6.0 | 28.4/27.8 | 24.6/25.1 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.58 | 0.42 | 0.46 | 6.01 | 34.2/22.2 | 19.0/30.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.099 | 0.71 | 0.29 | 0.00 | 9.44 | 35.8/23.5 | 19.1/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.68 | 0.32 | 0.00 | 9.37 | 29.8/29.3 | 24.1/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 17 | 0.244 | 0.222 | +0.065 | +0.042 | $3.61 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 68 | 0.817 | 0.725 | +0.121 | +0.029 | $5.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ goals YES | 10 | 0.133 | 0.123 | +0.027 | +0.017 | $1.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 33 | 0.462 | 0.370 | +0.116 | +0.024 | $2.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (25.82 vs 6.34 bp); despite a smaller raw edge (+0.065 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLGOAL-26OCT03SEAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.097); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (8.96 vs 5.59 bp); relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLGOAL-26OCT03SEAEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.103); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: DUPLICATIVE (phi 0.439); failure: EDM offense succeeds (4+ goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (25.82 vs 6.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.103); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.125); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no; why: second expression of the same thesis: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (8.96 vs 5.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.439); they share one thesis budget; relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.097); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: DUPLICATIVE (phi 0.439); KXNHLGOAL-26OCT03SEAEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.125); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5105): highest fidelity KXNHLPTS-26OCT03SEAEDM-EDMMEKHOLM14-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2853): highest fidelity KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.3297): highest fidelity KXNHLGOAL-26OCT03SEAEDM-SEAKKAKKO84-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03SEAEDM-SEAKKAKKO84-1|yes (same contract)
- KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2853, phi -0.224)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.2 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5105, phi -0.305)
- KXNHLGOAL-26OCT03SEAEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2853, phi -0.137)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.2 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5105, phi -0.308)

portfolios: A EV +3.46 (adj +0.54) on $11.91, P(profit) 0.6826, adj growth 5.1 bp · B EV +3.41 (adj +1.49) on $13.01, P(profit) 0.6843, adj growth 14.3 bp · C EV +4.10 (adj +1.95) on $17.64, P(profit) 0.3732, adj growth 18.3 bp · R EV +0.36 (adj +0.23) on $1.00, P(profit) 0.2444, adj growth 8.9 bp

## NJD @ NYI  ·  10000 joint draws  ·  338 bet sides mapped, 12 +EV candidates, 4 on card

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
| Luke Evangelista: 1+ assists NO | 67 | 0.839 | 0.716 | +0.154 | +0.031 | $5.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| New Jersey wins NO | 44 | 0.533 | 0.489 | +0.076 | +0.032 | $3.52 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | B |
| Dougie Hamilton: 2+ assists YES | 5 | 0.072 | 0.066 | +0.019 | +0.013 | $1.05 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_MIXED | D |
| New Jersey over 3.5 goals scored NO | 59 | 0.678 | 0.629 | +0.071 | +0.022 | $2.11 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03NJNYI-NJ|no; why: higher confidence-adjusted growth (9.70 vs 8.88 bp); relationships: KXNHLGAME-26OCT03NJNYI-NJ|no: MOSTLY_INDEPENDENT (phi 0.108); KXNHLAST-26OCT03NJNYI-NJDHAMILTON7-2|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no: REINFORCING (phi 0.169); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03NJNYI-NYI|yes; why: best adjusted growth among the thesis's expressions; relationships: KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.108); KXNHLAST-26OCT03NJNYI-NJDHAMILTON7-2|yes: INTENTIONAL_DIVERSIFIER (phi -0.139); KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no: REINFORCING (phi 0.512); failure: NJD wins (incl. OT/SO)
- **Dougie Hamilton: 2+ assists YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03NJNYI-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (6.84 vs 0.72 bp); despite a smaller raw edge (+0.019 vs +0.042/contract); alternative not eligible: confidence-adjusted EV +0.0085 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGAME-26OCT03NJNYI-NJ|no: INTENTIONAL_DIVERSIFIER (phi -0.139); KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no: INTENTIONAL_DIVERSIFIER (phi -0.213); failure: NJD offense suppressed (<= 2 goals)
- **New Jersey over 3.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03NJNYI-NJ|no; why: second expression of the same thesis: KXNHLGAME-26OCT03NJNYI-NJ|no has the higher standalone adjusted growth (8.88 vs 4.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.512); they share one thesis budget; relationships: KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.169); KXNHLGAME-26OCT03NJNYI-NJ|no: REINFORCING (phi 0.512); KXNHLAST-26OCT03NJNYI-NJDHAMILTON7-2|yes: INTENTIONAL_DIVERSIFIER (phi -0.213); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.07.
- thesis NJD:SUPPRESSED (p 0.4646): highest fidelity KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.5332): highest fidelity KXNHLGAME-26OCT03NJNYI-NJ|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no (same contract)
- thesis NYI:WINS_BY_2PLUS (p 0.3025): highest fidelity KXNHLGAME-26OCT03NJNYI-NJ|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no (same contract)
- KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.9 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3115, phi -0.167)
- KXNHLGAME-26OCT03NJNYI-NJ|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.4668, phi -1.0)
- KXNHLAST-26OCT03NJNYI-NJDHAMILTON7-2|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4646, phi -0.204)
- KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3115, phi -0.977)

portfolios: A EV +2.07 (adj +0.48) on $11.91, P(profit) 0.7604, adj growth 4.7 bp · B EV +2.47 (adj +0.83) on $12.33, P(profit) 0.5218, adj growth 8.0 bp · C EV +1.96 (adj +0.98) on $9.85, P(profit) 0.5848, adj growth 9.2 bp · R EV +0.28 (adj +0.11) on $2.00, P(profit) 0.5332, adj growth 4.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03NJNYI-NYI|yes == KXNHLGAME-26OCT03NJNYI-NJ|no

## DAL @ NSH  ·  10000 joint draws  ·  324 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.449 / away 0.551

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_DAL_win | p_overtime | goals | shots NSH/DAL | NSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.55 | 0.45 | 0.00 | 6.03 | 26.8/27.1 | 23.8/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.51 | 0.49 | 0.46 | 5.89 | 27.0/27.3 | 24.0/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.58 | 0.42 | 0.00 | 9.19 | 28.3/28.6 | 23.0/21.7 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.074 | 0.47 | 0.53 | 0.00 | 5.91 | 21.5/32.1 | 28.4/18.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.50 | 0.50 | 0.42 | 5.87 | 21.6/31.8 | 28.4/18.4 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.060 | 0.60 | 0.40 | 0.00 | 6.01 | 31.8/21.6 | 18.7/27.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mavrik Bourque: 1+ goals YES | 17 | 0.211 | 0.200 | +0.032 | +0.020 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Dallas wins by over 1.5 goals NO | 68 | 0.753 | 0.714 | +0.058 | +0.019 | $1.92 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mikko Rantanen: 1+ goals NO | 70 | 0.749 | 0.733 | +0.034 | +0.018 | $4.20 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 79 | 0.848 | 0.817 | +0.047 | +0.015 | $2.58 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL2|no; why: higher confidence-adjusted growth (5.87 vs 3.59 bp); despite a smaller raw edge (+0.032 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT03DALNSH-DAL2|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLSPREAD-26OCT03DALNSH-DAL3|no: MOSTLY_INDEPENDENT (phi 0.123); failure: NSH offense suppressed (<= 2 goals)
- **Dallas wins by over 1.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL3|no; why: higher confidence-adjusted growth (3.59 vs 3.15 bp); relationships: KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.138); KXNHLSPREAD-26OCT03DALNSH-DAL3|no: DUPLICATIVE (phi 0.737); failure: DAL wins by 2+
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT03DALNSH-DAL2|no has the higher standalone adjusted growth (3.59 vs 3.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.138); they share one thesis budget; relationships: KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLSPREAD-26OCT03DALNSH-DAL2|no: MOSTLY_INDEPENDENT (phi 0.138); KXNHLSPREAD-26OCT03DALNSH-DAL3|no: MOSTLY_INDEPENDENT (phi 0.126); failure: DAL offense succeeds (4+ goals)
- **Dallas wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL2|no; why: Broad expression KXNHLSPREAD-26OCT03DALNSH-DAL3|no selected over player prop KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-1|no because adjusted EV is 0.5 pts higher while thesis capture is 1.00 vs 0.80 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.123); KXNHLSPREAD-26OCT03DALNSH-DAL2|no: DUPLICATIVE (phi 0.737); KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.126); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:OFFENSE_4PLUS (p 0.3886): highest fidelity KXNHLSPREAD-26OCT03DALNSH-DAL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS (p 0.5364): highest fidelity KXNHLSPREAD-26OCT03DALNSH-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03DALNSH-DAL2|no (same contract)
- thesis DAL:SUPPRESSED (p 0.4367): highest fidelity KXNHLSPREAD-26OCT03DALNSH-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03DALNSH-DAL2|no — Broad expression KXNHLSPREAD-26OCT03DALNSH-DAL3|no selected over player prop KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-1|no because adjusted EV is 0.5 pts higher while thesis capture is 1.00 vs 0.80 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3982, phi -0.213)
- KXNHLSPREAD-26OCT03DALNSH-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.2473, phi -1.0)
- KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3374, phi -0.235)
- KXNHLSPREAD-26OCT03DALNSH-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.2473, phi -0.737)
- override: Broad expression KXNHLSPREAD-26OCT03DALNSH-DAL3|no selected over player prop KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-1|no because adjusted EV is 0.5 pts higher while thesis capture is 1.00 vs 0.80 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.59 (adj +0.30) on $11.91, P(profit) 0.5904, adj growth 2.7 bp · B EV +0.78 (adj +0.37) on $10.21, P(profit) 0.6547, adj growth 3.6 bp · C EV +1.03 (adj +0.47) on $9.54, P(profit) 0.7788, adj growth 4.4 bp · R EV +0.24 (adj +0.10) on $4.00, P(profit) 0.6549, adj growth 3.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03DALNSH-DAL|no == KXNHLGAME-26OCT03DALNSH-NSH|yes

## BOS @ MIN  ·  10000 joint draws  ·  332 bet sides mapped, 4 +EV candidates, 3 on card

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

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Olli Maatta: 1+ goals YES | 5 | 0.077 | 0.070 | +0.024 | +0.017 | $1.12 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 12 | 0.154 | 0.142 | +0.027 | +0.015 | $1.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 24 | 0.279 | 0.265 | +0.026 | +0.012 | $1.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (11.78 vs 1.78 bp); despite a smaller raw edge (+0.023 vs +0.026/contract); relationships: KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: MIN offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (4.18 vs 1.78 bp); relationships: KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT03BOSMIN-9|yes; why: higher confidence-adjusted growth (1.78 vs 0.38 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.87 vs 0.361); alternative not eligible: confidence-adjusted EV +0.0052 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.5004): highest fidelity KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.3156): highest fidelity KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes (same contract)
- KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2968, phi -0.102)
- KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2968, phi -0.153)
- KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2968, phi -0.207)

portfolios: A EV +1.44 (adj +0.86) on $7.05, P(profit) 0.5615, adj growth 8.1 bp · B EV +0.84 (adj +0.53) on $3.33, P(profit) 0.4372, adj growth 5.1 bp · C EV +0.37 (adj +0.17) on $3.47, P(profit) 0.4353, adj growth 1.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ COL  ·  10000 joint draws  ·  336 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.705 / away 0.295

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_STL_win | p_overtime | goals | shots COL/STL | COL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.149 | 0.71 | 0.29 | 0.00 | 6.02 | 34.0/21.4 | 18.9/29.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.57 | 0.43 | 0.45 | 5.95 | 34.2/21.8 | 18.7/30.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.112 | 0.75 | 0.25 | 0.00 | 9.28 | 35.4/22.7 | 18.5/26.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.69 | 0.31 | 0.00 | 6.05 | 28.0/27.1 | 24.4/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.53 | 0.47 | 0.47 | 5.94 | 28.3/27.4 | 24.2/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.64 | 0.36 | 0.00 | 9.32 | 30.0/28.7 | 23.5/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 1+ goals NO | 53 | 0.606 | 0.584 | +0.058 | +0.037 | $5.41 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 11 | 0.145 | 0.134 | +0.028 | +0.017 | $1.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 64 | 0.717 | 0.676 | +0.061 | +0.020 | $1.98 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dylan Holloway: 1+ goals YES | 25 | 0.293 | 0.280 | +0.030 | +0.017 | $1.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: higher confidence-adjusted growth (11.91 vs 7.28 bp); despite a smaller raw edge (+0.058 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLSPREAD-26OCT03STLCOL-COL3|no: REINFORCING (phi 0.198); KXNHLGOAL-26OCT03STLCOL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: COL offense succeeds (4+ goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: KXNHLGAME-26OCT03STLCOL-COL|no has the higher standalone adjusted growth (7.28 vs 6.12 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.135); relationships: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLSPREAD-26OCT03STLCOL-COL3|no: MOSTLY_INDEPENDENT (phi 0.102); KXNHLGOAL-26OCT03STLCOL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT03STLCOL-COL2|no; why: Broad expression KXNHLSPREAD-26OCT03STLCOL-COL3|no selected over player prop KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: REINFORCING (phi 0.198); KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.102); KXNHLGOAL-26OCT03STLCOL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.149); failure: COL wins by 2+
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: KXNHLGAME-26OCT03STLCOL-COL|no has the higher standalone adjusted growth (7.28 vs 3.05 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.184); relationships: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT03STLCOL-COL3|no: MOSTLY_INDEPENDENT (phi 0.149); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.2896): highest fidelity KXNHLSPREAD-26OCT03STLCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no — Broad expression KXNHLSPREAD-26OCT03STLCOL-COL3|no selected over player prop KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis STL:WINS (p 0.3687): highest fidelity KXNHLSPREAD-26OCT03STLCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3081): highest fidelity KXNHLTEAMTOTAL-26OCT03STLCOL-STL4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03STLCOL-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4997, phi -0.279)
- KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4763, phi -0.194)
- KXNHLSPREAD-26OCT03STLCOL-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4065, phi -0.759)
- KXNHLGOAL-26OCT03STLCOL-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4763, phi -0.259)
- override: Broad expression KXNHLSPREAD-26OCT03STLCOL-COL3|no selected over player prop KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.94 (adj +0.43) on $11.91, P(profit) 0.6805, adj growth 4.1 bp · B EV +1.20 (adj +0.68) on $9.93, P(profit) 0.5653, adj growth 6.6 bp · C EV +1.80 (adj +0.92) on $13.62, P(profit) 0.6055, adj growth 8.6 bp · R EV +0.31 (adj +0.16) on $3.00, P(profit) 0.6055, adj growth 6.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03STLCOL-STL|yes == KXNHLGAME-26OCT03STLCOL-COL|no

## CGY @ VAN  ·  10000 joint draws  ·  310 bet sides mapped, 5 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.506 / away 0.494

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
| Zayne Parekh: 1+ goals NO | 85 | 0.903 | 0.886 | +0.044 | +0.027 | $5.65 | FUNDED_RESEARCH | $2 | CGY:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Zeev Buium: 1+ goals NO | 88 | 0.923 | 0.908 | +0.035 | +0.021 | $5.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Drew O'Connor: 1+ goals YES | 17 | 0.220 | 0.204 | +0.040 | +0.024 | $1.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Zayne Parekh: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03CGYVAN-VAN2|yes; why: higher confidence-adjusted growth (13.49 vs 0.10 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.0 vs 0.519); alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CGY offense succeeds (4+ goals)
- **Zeev Buium: 1+ goals NO** — thesis: VAN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANBBOESER6-1|no; why: higher confidence-adjusted growth (9.67 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: VAN offense succeeds (4+ goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03CGYVAN-VANFHRONEK17-1|yes; why: higher confidence-adjusted growth (8.30 vs 0.11 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0035 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.4402): highest fidelity KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes (same contract)
- thesis CGY:SUPPRESSED (p 0.4302): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis VAN:SUPPRESSED (p 0.3458): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.35, phi -0.122)
- KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:OFFENSE_4PLUS (p 0.4402, phi -0.114)
- KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3458, phi -0.217)

portfolios: A EV +1.03 (adj +0.62) on $11.91, P(profit) 0.2199, adj growth 6.0 bp · B EV +0.94 (adj +0.57) on $13.24, P(profit) 0.2174, adj growth 5.5 bp · C EV +0.75 (adj +0.45) on $3.38, P(profit) 0.2199, adj growth 4.2 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.903, adj growth 2.5 bp

## LAK @ SJS  ·  10000 joint draws  ·  312 bet sides mapped, 10 +EV candidates, 3 on card

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
| Kiefer Sherwood: 1+ goals YES | 13 | 0.199 | 0.179 | +0.061 | +0.041 | $3.00 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 58 | 0.826 | 0.653 | +0.229 | +0.056 | $5.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Mason Marchment: 1+ assists NO | 67 | 0.812 | 0.713 | +0.127 | +0.028 | $5.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03LASJ-SJCGRAF51-1|yes; why: higher confidence-adjusted growth (30.64 vs 0.10 bp); alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.025); failure: SJS offense suppressed (<= 2 goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (28.62 vs 5.55 bp); relationships: KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: LAK offense succeeds (4+ goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no; why: higher confidence-adjusted growth (7.86 vs 3.94 bp); relationships: KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.4231): highest fidelity KXNHLAST-26OCT03LASJ-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.3966): highest fidelity KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.3574): highest fidelity KXNHLAST-26OCT03LASJ-LAALAFERRIERE14-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-LAALAFERRIERE14-1|yes (same contract)
- KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3966, phi -0.198)
- KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 26.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3574, phi -0.21)
- KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.2 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3833, phi -0.202)

portfolios: A EV +3.20 (adj +0.73) on $11.91, P(profit) 0.8502, adj growth 7.1 bp · B EV +4.49 (adj +1.65) on $14.14, P(profit) 0.7393, adj growth 16.0 bp · C EV +2.79 (adj +0.67) on $17.59, P(profit) 0.6308, adj growth 6.3 bp · R EV +0.44 (adj +0.30) on $1.00, P(profit) 0.1991, adj growth 11.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
