# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-01T21:24:49Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +24.50 | +4.79 | +25.73 | 0.610 | -54.14 | -71.40 | 30.70 |
| B thesis-diversified (joint) ← optimiser card | 84.95 | +22.61 | +11.69 | +22.38 | 0.590 | -46.07 | -46.07 | 102.02 |
| C best expression per thesis | 84.65 | +21.13 | +9.89 | +11.86 | 0.521 | -32.09 | -40.01 | 85.70 |
| R FUNDED research stakes | 13.00 | +3.35 | +2.10 | -3.98 | 0.374 | -8.01 | -13.00 | 0.00 |

## EDM @ NYR  ·  10000 joint draws  ·  424 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.540 / away 0.460

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_EDM_win | p_overtime | goals | shots NYR/EDM | NYR/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.49 | 0.51 | 0.00 | 6.06 | 27.0/27.4 | 23.8/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.109 | 0.54 | 0.46 | 0.00 | 9.45 | 28.4/28.8 | 22.8/21.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.50 | 0.50 | 0.49 | 6.06 | 27.4/27.7 | 24.4/23.9 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.097 | 0.46 | 0.54 | 0.00 | 6.07 | 21.8/32.8 | 28.9/18.5 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.46 | 0.54 | 0.46 | 5.93 | 21.8/33.2 | 29.7/18.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.074 | 0.47 | 0.53 | 0.00 | 9.37 | 23.0/34.5 | 27.8/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 11 | 0.167 | 0.152 | +0.051 | +0.035 | $8.74 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Filip Hallander: 1+ goals YES | 9 | 0.136 | 0.123 | +0.041 | +0.028 | $7.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ assists YES | 26 | 0.355 | 0.305 | +0.081 | +0.032 | $9.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
| Dylan Garand: 24+ saves YES | 42 | 0.569 | 0.466 | +0.132 | +0.029 | $14.38 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYR:NET_HIGH_VOLUME | DIRECT (0.93) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (25.13 vs 10.82 bp); despite a smaller raw edge (+0.051 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLSAVE-26NOV01EDMNYR-NYRDGARAND33-24|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: EDM offense suppressed (<= 2 goals)
- **Filip Hallander: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (25.13 vs 18.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSAVE-26NOV01EDMNYR-NYRDGARAND33-24|yes: MOSTLY_INDEPENDENT (phi -0.047); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (25.13 vs 10.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.032); they share one thesis budget; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSAVE-26NOV01EDMNYR-NYRDGARAND33-24|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: EDM offense suppressed (<= 2 goals)
- **Dylan Garand: 24+ saves YES** — thesis: NYR net faces heavy volume (33+ shots; EDM pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.047); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: NYR net faces light volume (<= 25 shots; EDM suppressed)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4261): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:NET_HIGH_VOLUME (p 0.2529): highest fidelity KXNHLSAVE-26NOV01EDMNYR-NYRDGARAND33-24|yes [DIRECT], best adjusted EV KXNHLSAVE-26NOV01EDMNYR-NYRDGARAND33-24|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.3517): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2|no (same contract)
- KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3517, phi -0.187)
- KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3517, phi -0.151)
- KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3517, phi -0.269)
- KXNHLSAVE-26NOV01EDMNYR-NYRDGARAND33-24|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.9 pts; fragile player expression; opposing: failure thesis NYR:NET_LOW_VOLUME (p 0.3242, phi -0.742)

portfolios: A EV +13.20 (adj +2.74) on $50.00, P(profit) 0.6305, adj growth 21.6 bp · B EV +14.03 (adj +6.73) on $39.92, P(profit) 0.4185, adj growth 57.9 bp · C EV +12.38 (adj +4.50) on $47.10, P(profit) 0.706, adj growth 39.0 bp · R EV +1.30 (adj +0.90) on $3.00, P(profit) 0.1674, adj growth 28.8 bp

## OTT @ ANA  ·  10000 joint draws  ·  426 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.481 / away 0.519

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_OTT_win | p_overtime | goals | shots ANA/OTT | ANA/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.66 | 0.34 | 0.00 | 6.05 | 27.4/27.6 | 24.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.49 | 0.51 | 0.47 | 6.0 | 27.4/27.4 | 24.0/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.67 | 0.33 | 0.00 | 9.37 | 29.1/28.9 | 24.0/21.4 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.083 | 0.72 | 0.28 | 0.00 | 6.02 | 32.1/21.5 | 19.0/27.5 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.53 | 0.47 | 0.47 | 5.9 | 32.7/22.0 | 18.8/29.3 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.061 | 0.58 | 0.42 | 0.00 | 6.05 | 22.1/32.2 | 29.1/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 16 | 0.247 | 0.223 | +0.077 | +0.053 | $11.60 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Ottawa wins by over 2.5 goals NO | 79 | 0.880 | 0.833 | +0.079 | +0.031 | $15.00 | FUNDED_RESEARCH | $4 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa over 4.5 goals scored NO | 73 | 0.815 | 0.770 | +0.071 | +0.026 | $15.00 | FUNDED_RESEARCH | $3 | ANA:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Fabian Zetterlund: 1+ goals YES | 17 | 0.200 | 0.191 | +0.020 | +0.011 | $3.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: higher confidence-adjusted growth (42.62 vs 13.53 bp); despite a smaller raw edge (+0.077 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: MOSTLY_INDEPENDENT (phi 0.109); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV01OTTANA-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: ANA offense suppressed (<= 2 goals)
- **Ottawa wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no; why: higher confidence-adjusted growth (13.53 vs 12.47 bp); wins across more scripts (relative breadth 1.028 vs 0.578); relationships: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.109); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: REINFORCING (phi 0.48); KXNHLGOAL-26NOV01OTTANA-OTTFZETTERLUND20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.122); failure: OTT wins by 2+
- **Ottawa over 4.5 goals scored NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over broad KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.48 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.48); KXNHLGOAL-26NOV01OTTANA-OTTFZETTERLUND20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.187); failure: OTT offense succeeds (4+ goals)
- **Fabian Zetterlund: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01OTTANA-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (1.81 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26NOV01OTTANA-OTT3|no: INTENTIONAL_DIVERSIFIER (phi -0.122); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: INTENTIONAL_DIVERSIFIER (phi -0.187); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4926): highest fidelity KXNHLTEAMTOTAL-26NOV01OTTANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5889): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4358): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3002, phi -0.202)
- KXNHLSPREAD-26NOV01OTTANA-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2025, phi -0.731)
- KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3498, phi -0.649)
- KXNHLGOAL-26NOV01OTTANA-OTTFZETTERLUND20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4358, phi -0.203)
- override: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over broad KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.48 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +11.30 (adj +2.05) on $50.00, P(profit) 0.5183, adj growth 9.1 bp · B EV +8.58 (adj +4.96) on $45.03, P(profit) 0.3385, adj growth 44.2 bp · C EV +8.75 (adj +5.39) on $37.55, P(profit) 0.3607, adj growth 46.7 bp · R EV +2.05 (adj +1.20) on $10.00, P(profit) 0.2467, adj growth 42.6 bp
equivalent contracts collapsed: KXNHLGAME-26NOV01OTTANA-OTT|no == KXNHLGAME-26NOV01OTTANA-ANA|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
