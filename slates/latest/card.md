# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-01T21:00:04Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +22.73 | +4.97 | +25.33 | 0.646 | -48.81 | -65.24 | 34.70 |
| B thesis-diversified (joint) ← optimiser card | 82.70 | +22.06 | +12.12 | +17.78 | 0.551 | -44.34 | -45.63 | 104.83 |
| C best expression per thesis | 78.52 | +17.26 | +9.17 | +6.05 | 0.525 | -36.32 | -39.05 | 79.20 |
| R FUNDED research stakes | 14.00 | +3.78 | +2.40 | -5.11 | 0.374 | -7.76 | -14.00 | 0.00 |

## EDM @ NYR  ·  10000 joint draws  ·  424 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.539 / away 0.461

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
| Alex Formenton: 1+ goals YES | 11 | 0.167 | 0.152 | +0.051 | +0.035 | $8.81 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Filip Hallander: 1+ goals YES | 9 | 0.136 | 0.122 | +0.041 | +0.027 | $6.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ assists YES | 26 | 0.355 | 0.305 | +0.081 | +0.032 | $10.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
| Connor McDavid: 1+ assists NO | 35 | 0.458 | 0.385 | +0.092 | +0.019 | $9.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.69) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (25.13 vs 10.82 bp); despite a smaller raw edge (+0.051 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.035); failure: EDM offense suppressed (<= 2 goals)
- **Filip Hallander: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (25.13 vs 17.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (25.13 vs 10.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.032); they share one thesis budget; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.122); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no; why: KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no has the higher standalone adjusted growth (3.26 vs 3.24 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.087); relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.122); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4261): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.4375): highest fidelity KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.3517): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3517, phi -0.187)
- KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3517, phi -0.151)
- KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3517, phi -0.269)
- KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 31% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.3 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4261, phi -0.323)

portfolios: A EV +12.95 (adj +3.24) on $50.00, P(profit) 0.712, adj growth 26.1 bp · B EV +11.91 (adj +6.08) on $34.65, P(profit) 0.5317, adj growth 52.2 bp · C EV +8.51 (adj +3.78) on $40.97, P(profit) 0.3909, adj growth 32.5 bp · R EV +1.30 (adj +0.90) on $3.00, P(profit) 0.1674, adj growth 28.8 bp

## OTT @ ANA  ·  10000 joint draws  ·  426 bet sides mapped, 17 +EV candidates, 4 on card

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
| A.J. Greer: 1+ goals YES | 16 | 0.247 | 0.223 | +0.077 | +0.053 | $13.41 | FUNDED_RESEARCH | $4 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Ottawa wins by over 2.5 goals NO | 79 | 0.880 | 0.833 | +0.079 | +0.031 | $18.13 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jeff Malott: 1+ goals YES | 10 | 0.136 | 0.125 | +0.029 | +0.019 | $4.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Ottawa over 4.5 goals scored NO | 74 | 0.815 | 0.773 | +0.062 | +0.019 | $11.87 | FUNDED_RESEARCH | $2 | ANA:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: higher confidence-adjusted growth (42.62 vs 13.53 bp); despite a smaller raw edge (+0.077 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: MOSTLY_INDEPENDENT (phi 0.109); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: MOSTLY_INDEPENDENT (phi 0.013); failure: ANA offense suppressed (<= 2 goals)
- **Ottawa wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no; why: higher confidence-adjusted growth (13.53 vs 12.47 bp); wins across more scripts (relative breadth 1.028 vs 0.578); relationships: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.109); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.077); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: REINFORCING (phi 0.48); failure: OTT wins by 2+
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (42.62 vs 8.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLSPREAD-26NOV01OTTANA-OTT3|no: MOSTLY_INDEPENDENT (phi 0.077); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: MOSTLY_INDEPENDENT (phi 0.002); failure: ANA offense suppressed (<= 2 goals)
- **Ottawa over 4.5 goals scored NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over broad KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.48 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.48); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4926): highest fidelity KXNHLTEAMTOTAL-26NOV01OTTANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5889): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4358): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3002, phi -0.202)
- KXNHLSPREAD-26NOV01OTTANA-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2025, phi -0.731)
- KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3002, phi -0.155)
- KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3498, phi -0.649)
- override: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over broad KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.48 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.79 (adj +1.73) on $50.00, P(profit) 0.5374, adj growth 8.6 bp · B EV +10.15 (adj +6.04) on $48.05, P(profit) 0.346, adj growth 52.6 bp · C EV +8.75 (adj +5.39) on $37.55, P(profit) 0.3607, adj growth 46.7 bp · R EV +2.48 (adj +1.50) on $11.00, P(profit) 0.2467, adj growth 50.9 bp
equivalent contracts collapsed: KXNHLGAME-26NOV01OTTANA-OTT|no == KXNHLGAME-26NOV01OTTANA-ANA|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
