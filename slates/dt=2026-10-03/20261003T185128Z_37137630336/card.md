# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T18:51:28Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +33.23 | +11.03 | +32.41 | 0.861 | -5.14 | -14.62 | 105.60 |
| B thesis-diversified (joint) ← optimiser card | 146.18 | +30.11 | +15.02 | +28.53 | 0.835 | -7.63 | -17.41 | 145.26 |
| C best expression per thesis | 150.00 | +24.10 | +11.36 | +22.68 | 0.776 | -14.53 | -23.41 | 108.98 |
| R FUNDED research stakes | 23.00 | +2.58 | +1.59 | +2.43 | 0.656 | -5.21 | -6.94 | 0.00 |

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
| Ryan Greene: 1+ goals YES | 12 | 0.173 | 0.158 | +0.045 | +0.031 | $2.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 59 | 0.649 | 0.633 | +0.042 | +0.026 | $4.21 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 62 | 0.749 | 0.655 | +0.112 | +0.019 | $4.04 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ assists NO | 57 | 0.646 | 0.605 | +0.059 | +0.018 | $2.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CHIBUF-BUF|no; why: higher confidence-adjusted growth (18.32 vs 0.94 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: CHI offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (6.32 vs 3.01 bp); despite a smaller raw edge (+0.042 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: BUF offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CHIBUF-CHIRKANTSEROV80-1|no; why: higher confidence-adjusted growth (3.36 vs 0.49 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CHI offense succeeds (4+ goals)
- **Tage Thompson: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no has the higher standalone adjusted growth (6.32 vs 3.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: BUF offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.2926): highest fidelity KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.3103): highest fidelity KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4879): highest fidelity KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4879, phi -0.218)
- KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4825, phi -0.265)
- KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.4 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2926, phi -0.228)
- KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4825, phi -0.259)

portfolios: A EV +1.83 (adj +0.83) on $11.56, P(profit) 0.4312, adj growth 8.0 bp · B EV +2.01 (adj +0.88) on $13.09, P(profit) 0.5738, adj growth 8.5 bp · C EV +2.35 (adj +1.08) on $13.91, P(profit) 0.5738, adj growth 10.3 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.6492, adj growth 3.3 bp

## OTT @ TOR  ·  10000 joint draws  ·  360 bet sides mapped, 12 +EV candidates, 3 on card

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
| Stephen Halliday: 1+ goals YES | 9 | 0.134 | 0.122 | +0.038 | +0.026 | $1.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Carter Yakemchuk: 1+ goals NO | 90 | 0.934 | 0.923 | +0.028 | +0.017 | $5.24 | FUNDED_RESEARCH | $2 | OTT:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ goals NO | 65 | 0.691 | 0.680 | +0.025 | +0.014 | $2.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03OTTTOR-OTT|yes; why: higher confidence-adjusted growth (16.73 vs 1.29 bp); despite a smaller raw edge (+0.038 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: OTT offense suppressed (<= 2 goals)
- **Carter Yakemchuk: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (7.26 vs 1.77 bp); despite a smaller raw edge (+0.028 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: OTT offense succeeds (4+ goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no; why: Player prop expression KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.84 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT03OTTTOR-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: TOR offense succeeds (4+ goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:SUPPRESSED (p 0.4475): highest fidelity KXNHLAST-26OCT03OTTTOR-TORKMARCHENKO86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no — Player prop expression KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.84 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis TOR:OFFENSE_4PLUS (p 0.3332): highest fidelity KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes (same contract)
- thesis TOR:NET_HIGH_VOLUME (p 0.3759): highest fidelity KXNHLSAVE-26OCT03OTTTOR-TORSBOBROVSKY72-26|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT03OTTTOR-TORSBOBROVSKY72-26|yes (same contract)
- KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3882, phi -0.158)
- KXNHLGOAL-26OCT03OTTTOR-OTTCYAKEMCHUK26-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3964, phi -0.104)
- KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3332, phi -0.268)
- override: Player prop expression KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.84 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.98 (adj +0.34) on $11.56, P(profit) 0.5984, adj growth 3.2 bp · B EV +0.93 (adj +0.61) on $9.59, P(profit) 0.689, adj growth 5.9 bp · C EV +2.02 (adj +0.48) on $13.13, P(profit) 0.6598, adj growth 4.6 bp · R EV +0.06 (adj +0.04) on $2.00, P(profit) 0.9339, adj growth 1.4 bp

## WSH @ TBL  ·  10000 joint draws  ·  356 bet sides mapped, 10 +EV candidates, 3 on card

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
| John Carlson: 1+ assists NO | 48 | 0.746 | 0.567 | +0.249 | +0.069 | $5.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.211 | 0.200 | +0.031 | +0.020 | $1.43 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ assists NO | 38 | 0.457 | 0.416 | +0.060 | +0.019 | $1.63 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (41.91 vs 11.79 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT03WSHTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.074); failure: TBL offense succeeds (4+ goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03WSHTB-TB|no; why: higher confidence-adjusted growth (5.74 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT03WSHTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.021); failure: WSH offense suppressed (<= 2 goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no; why: second expression of the same thesis: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no has the higher standalone adjusted growth (41.91 vs 3.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.074); they share one thesis budget; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.021); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.3217): highest fidelity KXNHLAST-26OCT03WSHTB-TBNKUCHEROV86-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.3068): highest fidelity KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes (same contract)
- KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 27.6 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4659, phi -0.21)
- KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4782, phi -0.238)
- KXNHLAST-26OCT03WSHTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4659, phi -0.308)

portfolios: A EV +4.06 (adj +0.83) on $11.56, P(profit) 0.6872, adj growth 8.1 bp · B EV +3.11 (adj +0.97) on $8.30, P(profit) 0.7677, adj growth 9.5 bp · C EV +3.76 (adj +1.16) on $8.78, P(profit) 0.7965, adj growth 11.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ PHI  ·  10000 joint draws  ·  370 bet sides mapped, 14 +EV candidates, 4 on card

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
| Noel Acciari: 1+ goals YES | 8 | 0.135 | 0.120 | +0.050 | +0.035 | $2.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 11 | 0.176 | 0.156 | +0.059 | +0.039 | $2.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Mark Jankowski: 1+ goals NO | 84 | 0.884 | 0.872 | +0.035 | +0.022 | $5.24 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 18 | 0.219 | 0.206 | +0.028 | +0.016 | $1.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (33.24 vs 31.14 bp); despite a smaller raw edge (+0.050 vs +0.059/contract); relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: PHI offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03CARPHI-CAR2|no; why: higher confidence-adjusted growth (31.14 vs 5.03 bp); despite a smaller raw edge (+0.059 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PHI offense suppressed (<= 2 goals)
- **Mark Jankowski: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03CARPHI-CAR2|no; why: higher confidence-adjusted growth (8.61 vs 5.03 bp); despite a smaller raw edge (+0.034 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: CAR offense succeeds (4+ goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (31.14 vs 3.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3711): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.4667): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03CARPHI-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.548): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03CARPHI-CAR2|no (same contract)
- KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4082, phi -0.159)
- KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4082, phi -0.21)
- KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3207, phi -0.175)
- KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4082, phi -0.227)

portfolios: A EV +2.28 (adj +1.10) on $11.56, P(profit) 0.5938, adj growth 10.4 bp · B EV +2.93 (adj +1.96) on $11.07, P(profit) 0.4241, adj growth 18.9 bp · C EV +2.06 (adj +1.21) on $8.10, P(profit) 0.1761, adj growth 11.5 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.8839, adj growth 2.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03CARPHI-CAR|no == KXNHLGAME-26OCT03CARPHI-PHI|yes

## MTL @ PIT  ·  10000 joint draws  ·  330 bet sides mapped, 8 +EV candidates, 3 on card

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
| Connor Dewar: 1+ goals YES | 12 | 0.201 | 0.180 | +0.074 | +0.052 | $3.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Filip Hallander: 1+ goals YES | 13 | 0.202 | 0.183 | +0.064 | +0.045 | $2.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 29 | 0.374 | 0.352 | +0.070 | +0.047 | $4.02 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes; why: higher confidence-adjusted growth (51.79 vs 4.26 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.827 vs 0.498); relationships: KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03MTLPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: PIT offense suppressed (<= 2 goals)
- **Filip Hallander: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (51.79 vs 36.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03MTLPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (51.79 vs 22.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts PIT shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10, PIT shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.3425): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.4691): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-MTL2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.5586): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3238, phi -0.228)
- KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3238, phi -0.186)
- KXNHLGOAL-26OCT03MTLPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3238, phi -0.263)

portfolios: A EV +4.26 (adj +2.76) on $11.56, P(profit) 0.4433, adj growth 26.4 bp · B EV +4.23 (adj +2.96) on $10.31, P(profit) 0.5972, adj growth 28.4 bp · C EV +2.62 (adj +1.85) on $4.51, P(profit) 0.2013, adj growth 17.5 bp · R EV +0.46 (adj +0.31) on $2.00, P(profit) 0.3739, adj growth 11.6 bp

## UTA @ CBJ  ·  10000 joint draws  ·  342 bet sides mapped, 10 +EV candidates, 4 on card

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
| Charlie Coyle: 1+ goals YES | 20 | 0.271 | 0.252 | +0.059 | +0.041 | $3.15 | FUNDED_RESEARCH | $1 | CBJ:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 67 | 0.862 | 0.727 | +0.176 | +0.042 | $5.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Danton Heinen: 1+ goals YES | 10 | 0.132 | 0.121 | +0.025 | +0.015 | $1.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 18 | 0.220 | 0.209 | +0.030 | +0.019 | $1.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-CBJSMONAHAN23-1|yes; why: higher confidence-adjusted growth (21.19 vs 2.97 bp); relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CBJ offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03UTACBJ-CBJ|yes; why: higher confidence-adjusted growth (18.00 vs 1.36 bp); relationships: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: UTA offense succeeds (4+ goals)
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (21.19 vs 5.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CBJ offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-UTAALEE72-1|yes; why: higher confidence-adjusted growth (4.85 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.4162): highest fidelity KXNHLGAME-26OCT03UTACBJ-CBJ|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.3582): highest fidelity KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.419): highest fidelity KXNHLGAME-26OCT03UTACBJ-CBJ|yes [DIRECT], best adjusted EV KXNHLGAME-26OCT03UTACBJ-CBJ|yes (same contract)
- KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.235)
- KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.7 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3582, phi -0.189)
- KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.15)
- KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.419, phi -0.222)

portfolios: A EV +2.35 (adj +0.81) on $11.56, P(profit) 0.7664, adj growth 7.9 bp · B EV +2.70 (adj +1.21) on $10.84, P(profit) 0.4756, adj growth 11.7 bp · C EV +1.89 (adj +1.10) on $14.21, P(profit) 0.4284, adj growth 10.5 bp · R EV +0.28 (adj +0.19) on $1.00, P(profit) 0.2706, adj growth 7.3 bp

## SEA @ EDM  ·  10000 joint draws  ·  356 bet sides mapped, 14 +EV candidates, 4 on card

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
| Alex Formenton: 1+ goals YES | 17 | 0.235 | 0.215 | +0.055 | +0.035 | $2.84 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 10 | 0.141 | 0.130 | +0.035 | +0.023 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 68 | 0.826 | 0.728 | +0.131 | +0.033 | $5.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Connor McDavid: 1+ assists NO | 33 | 0.481 | 0.376 | +0.135 | +0.031 | $2.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (17.67 vs 5.42 bp); despite a smaller raw edge (+0.055 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.122); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.118); failure: EDM offense suppressed (<= 2 goals)
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

portfolios: A EV +2.95 (adj +0.55) on $11.56, P(profit) 0.654, adj growth 5.2 bp · B EV +3.25 (adj +1.33) on $11.90, P(profit) 0.6773, adj growth 12.9 bp · C EV +2.55 (adj +1.07) on $17.14, P(profit) 0.3642, adj growth 10.4 bp · R EV +0.30 (adj +0.19) on $1.00, P(profit) 0.2346, adj growth 7.3 bp

## NJD @ NYI  ·  10000 joint draws  ·  340 bet sides mapped, 18 +EV candidates, 3 on card

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
| Jack Hughes: 1+ goals NO | 63 | 0.695 | 0.677 | +0.049 | +0.031 | $4.61 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| New Jersey wins NO | 44 | 0.533 | 0.489 | +0.076 | +0.032 | $3.36 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | B |
| Kyle Palmieri: 1+ assists NO | 68 | 0.824 | 0.724 | +0.129 | +0.029 | $5.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03NJNYI-NJ|no; why: higher confidence-adjusted growth (9.35 vs 8.88 bp); despite a smaller raw edge (+0.049 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGAME-26OCT03NJNYI-NJ|no: REINFORCING (phi 0.217); KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no has the higher standalone adjusted growth (9.35 vs 8.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.217); they share one thesis budget; relationships: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no: REINFORCING (phi 0.217); KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: INTENTIONAL_DIVERSIFIER (phi -0.133); failure: NJD wins (incl. OT/SO)
- **Kyle Palmieri: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03NJNYI-NYIBHORVAT14-1|no; why: higher confidence-adjusted growth (8.56 vs 0.03 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0016 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGAME-26OCT03NJNYI-NJ|no: INTENTIONAL_DIVERSIFIER (phi -0.133); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.07.
- thesis NJD:SUPPRESSED (p 0.4646): highest fidelity KXNHLSPREAD-26OCT03NJNYI-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.5332): highest fidelity KXNHLGAME-26OCT03NJNYI-NJ|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no (same contract)
- thesis NYI:WINS_BY_2PLUS (p 0.3025): highest fidelity KXNHLGAME-26OCT03NJNYI-NJ|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no (same contract)
- KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3115, phi -0.264)
- KXNHLGAME-26OCT03NJNYI-NJ|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.4668, phi -1.0)
- KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.4 pts; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.3608, phi -0.179)

portfolios: A EV +2.16 (adj +0.47) on $11.56, P(profit) 0.5869, adj growth 4.7 bp · B EV +1.85 (adj +0.67) on $13.09, P(profit) 0.749, adj growth 6.5 bp · C EV +1.44 (adj +0.66) on $17.14, P(profit) 0.4205, adj growth 6.4 bp · R EV +0.32 (adj +0.17) on $3.00, P(profit) 0.695, adj growth 6.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03NJNYI-NYI|yes == KXNHLGAME-26OCT03NJNYI-NJ|no

## DAL @ NSH  ·  10000 joint draws  ·  326 bet sides mapped, 11 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.443 / away 0.557

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
| Miro Heiskanen: 1+ goals NO | 86 | 0.903 | 0.891 | +0.035 | +0.023 | $4.84 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Dallas wins NO | 44 | 0.527 | 0.485 | +0.070 | +0.028 | $2.56 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | B |
| Lian Bichsel: 1+ goals NO | 93 | 0.957 | 0.948 | +0.022 | +0.013 | $4.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
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

portfolios: A EV +1.46 (adj +0.36) on $11.56, P(profit) 0.6536, adj growth 3.4 bp · B EV +0.70 (adj +0.35) on $12.25, P(profit) 0.4752, adj growth 3.5 bp · C EV +0.83 (adj +0.36) on $11.21, P(profit) 0.5101, adj growth 3.5 bp · R EV +0.23 (adj +0.11) on $3.00, P(profit) 0.4908, adj growth 4.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03DALNSH-NSH|yes == KXNHLGAME-26OCT03DALNSH-DAL|no

## BOS @ MIN  ·  10000 joint draws  ·  334 bet sides mapped, 4 +EV candidates, 3 on card

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
| Yakov Trenin: 1+ goals YES | 11 | 0.154 | 0.142 | +0.037 | +0.025 | $1.69 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 23 | 0.279 | 0.265 | +0.036 | +0.023 | $1.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 72 | 0.830 | 0.752 | +0.096 | +0.018 | $5.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (13.17 vs 6.15 bp); relationships: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT03BOSMIN-7|yes; why: higher confidence-adjusted growth (6.15 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.87 vs 0.661); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: MIN offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03BOSMIN-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (3.62 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.5004): highest fidelity KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.4677): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2968, phi -0.153)
- KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2968, phi -0.207)
- KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3156, phi -0.202)

portfolios: A EV +2.44 (adj +1.22) on $11.28, P(profit) 0.4372, adj growth 11.5 bp · B EV +1.51 (adj +0.67) on $8.79, P(profit) 0.3506, adj growth 6.4 bp · C EV +0.37 (adj +0.23) on $2.49, P(profit) 0.2786, adj growth 2.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ COL  ·  10000 joint draws  ·  338 bet sides mapped, 16 +EV candidates, 4 on card

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
| Nathan MacKinnon: 1+ goals NO | 52 | 0.606 | 0.584 | +0.069 | +0.046 | $5.24 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Colorado wins NO | 28 | 0.369 | 0.336 | +0.075 | +0.042 | $2.34 | FUNDED_RESEARCH | $1 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | A |
| Pius Suter: 1+ goals YES | 11 | 0.148 | 0.136 | +0.031 | +0.019 | $1.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ assists NO | 36 | 0.498 | 0.405 | +0.122 | +0.029 | $2.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.74) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: higher confidence-adjusted growth (18.66 vs 18.28 bp); despite a smaller raw edge (+0.069 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGAME-26OCT03STLCOL-COL|no: REINFORCING (phi 0.196); KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: COL offense succeeds (4+ goals)
- **Colorado wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (18.28 vs 7.77 bp); despite a smaller raw edge (+0.075 vs +0.122/contract); relationships: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: REINFORCING (phi 0.196); KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: REINFORCING (phi 0.169); KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no: REINFORCING (phi 0.23); failure: COL wins (incl. OT/SO)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: second expression of the same thesis: KXNHLGAME-26OCT03STLCOL-COL|no has the higher standalone adjusted growth (18.28 vs 7.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.169); they share one thesis budget; relationships: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGAME-26OCT03STLCOL-COL|no: REINFORCING (phi 0.169); KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: STL offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no has the higher standalone adjusted growth (18.66 vs 7.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGAME-26OCT03STLCOL-COL|no: REINFORCING (phi 0.23); KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.16, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.2955): highest fidelity KXNHLSPREAD-26OCT03STLCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT03STLCOL-COL3|no less than the minimum stake; KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no kept
- thesis STL:WINS (p 0.3688): highest fidelity KXNHLGAME-26OCT03STLCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3093): highest fidelity KXNHLTEAMTOTAL-26OCT03STLCOL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5047, phi -0.271)
- KXNHLGAME-26OCT03STLCOL-COL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.6312, phi -1.0)
- KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4716, phi -0.205)
- KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 26% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5047, phi -0.307)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT03STLCOL-COL3|no less than the minimum stake; KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no kept

portfolios: A EV +3.52 (adj +0.49) on $11.56, P(profit) 0.6279, adj growth 4.4 bp · B EV +2.24 (adj +1.12) on $10.77, P(profit) 0.5113, adj growth 10.8 bp · C EV +1.90 (adj +1.16) on $10.86, P(profit) 0.7052, adj growth 11.1 bp · R EV +0.51 (adj +0.31) on $3.00, P(profit) 0.7052, adj growth 12.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03STLCOL-STL|yes == KXNHLGAME-26OCT03STLCOL-COL|no

## CGY @ VAN  ·  10000 joint draws  ·  310 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.502 / away 0.498

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CGY_win | p_overtime | goals | shots VAN/CGY | VAN/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.59 | 0.41 | 0.00 | 6.01 | 28.3/28.4 | 25.2/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.47 | 5.9 | 28.2/28.3 | 24.9/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.61 | 0.39 | 0.00 | 9.36 | 30.2/30.2 | 24.6/23.4 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.067 | 0.64 | 0.36 | 0.00 | 5.94 | 32.9/22.1 | 19.2/28.5 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.52 | 0.48 | 0.44 | 5.91 | 22.4/33.2 | 29.8/19.3 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.061 | 0.50 | 0.50 | 0.00 | 5.98 | 22.6/33.3 | 29.5/19.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zeev Buium: 1+ goals NO | 87 | 0.918 | 0.905 | +0.040 | +0.027 | $5.00 | FUNDED_RESEARCH | $2 | VAN:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Zayne Parekh: 1+ goals NO | 85 | 0.902 | 0.886 | +0.044 | +0.027 | $5.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Drew O'Connor: 1+ goals YES | 17 | 0.222 | 0.208 | +0.043 | +0.028 | $2.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 22 | 0.257 | 0.247 | +0.025 | +0.015 | $1.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Zeev Buium: 1+ goals NO** — thesis: VAN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANBBOESER6-1|no; why: higher confidence-adjusted growth (15.12 vs 2.27 bp); relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: VAN offense succeeds (4+ goals)
- **Zayne Parekh: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CGYVAN-CGYMCORONATO27-1|no; why: higher confidence-adjusted growth (13.12 vs 2.33 bp); relationships: KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CGY offense succeeds (4+ goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (11.60 vs 2.64 bp); relationships: KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (11.60 vs 2.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.4394): highest fidelity KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:SUPPRESSED (p 0.4255): highest fidelity KXNHLGOAL-26OCT03CGYVAN-CGYYSHARANGOVICH17-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CGYVAN-CGYMCORONATO27-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:SUPPRESSED (p 0.35): highest fidelity KXNHLGOAL-26OCT03CGYVAN-VANBBOESER6-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CGYVAN-VANBBOESER6-1|no (same contract)
- KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:OFFENSE_4PLUS (p 0.4394, phi -0.118)
- KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.3499, phi -0.136)
- KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.35, phi -0.197)
- KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.35, phi -0.218)

portfolios: A EV +0.95 (adj +0.62) on $11.56, P(profit) 0.2222, adj growth 6.0 bp · B EV +1.07 (adj +0.69) on $13.09, P(profit) 0.3869, adj growth 6.8 bp · C EV +0.97 (adj +0.61) on $11.38, P(profit) 0.6428, adj growth 5.8 bp · R EV +0.09 (adj +0.06) on $2.00, P(profit) 0.9181, adj growth 2.4 bp

## LAK @ SJS  ·  10000 joint draws  ·  312 bet sides mapped, 10 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.511 / away 0.489

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_LAK_win | p_overtime | goals | shots SJS/LAK | SJS/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.53 | 0.47 | 0.00 | 6.01 | 27.4/27.5 | 24.1/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.48 | 5.94 | 27.5/27.8 | 24.4/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.56 | 0.44 | 0.00 | 9.22 | 28.8/29.0 | 23.3/22.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.079 | 0.47 | 0.53 | 0.00 | 5.96 | 21.8/32.8 | 29.1/18.5 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.48 | 0.52 | 0.48 | 5.85 | 21.9/32.6 | 29.1/18.9 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.058 | 0.59 | 0.41 | 0.00 | 6.04 | 31.9/21.7 | 18.7/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kiefer Sherwood: 1+ goals YES | 13 | 0.202 | 0.182 | +0.064 | +0.045 | $2.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 58 | 0.827 | 0.653 | +0.230 | +0.056 | $5.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Luca Cagnoni: 1+ goals NO | 88 | 0.932 | 0.918 | +0.045 | +0.030 | $5.09 | FUNDED_RESEARCH | $2 | SJS:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03LASJ-SJWSMITH2-1|yes; why: higher confidence-adjusted growth (35.49 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03LASJ-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: SJS offense suppressed (<= 2 goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (29.05 vs 6.20 bp); relationships: KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03LASJ-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: LAK offense succeeds (4+ goals)
- **Luca Cagnoni: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no; why: higher confidence-adjusted growth (20.87 vs 2.19 bp); despite a smaller raw edge (+0.045 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.423): highest fidelity KXNHLAST-26OCT03LASJ-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.3998): highest fidelity KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.363): highest fidelity KXNHLAST-26OCT03LASJ-LAALAFERRIERE14-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-LAALAFERRIERE14-1|yes (same contract)
- KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3998, phi -0.191)
- KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 26.7 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.363, phi -0.193)
- KXNHLGOAL-26OCT03LASJ-SJLCAGNONI42-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3817, phi -0.126)

portfolios: A EV +2.99 (adj +0.65) on $11.56, P(profit) 0.8559, adj growth 6.4 bp · B EV +3.56 (adj +1.60) on $13.09, P(profit) 0.8145, adj growth 15.5 bp · C EV +1.35 (adj +0.39) on $17.14, P(profit) 0.7584, adj growth 3.8 bp · R EV +0.10 (adj +0.07) on $2.00, P(profit) 0.9321, adj growth 2.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
