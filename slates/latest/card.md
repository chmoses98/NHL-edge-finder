# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-22T22:02:05Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +25.18 | +6.35 | +25.22 | 0.804 | -12.77 | -23.04 | 58.90 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +27.64 | +15.79 | +25.55 | 0.756 | -20.37 | -32.02 | 150.68 |
| C best expression per thesis | 149.22 | +23.99 | +11.66 | +21.97 | 0.725 | -23.15 | -33.63 | 109.66 |
| R FUNDED research stakes | 17.00 | +1.79 | +1.08 | +1.21 | 0.614 | -4.30 | -5.92 | 0.00 |

## NSH @ BOS  ·  10000 joint draws  ·  448 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.580 / away 0.420

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_NSH_win | p_overtime | goals | shots BOS/NSH | BOS/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.62 | 0.38 | 0.00 | 6.04 | 28.2/28.1 | 25.0/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.46 | 5.97 | 28.0/28.0 | 24.6/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.63 | 0.37 | 0.00 | 9.5 | 29.8/29.6 | 24.1/22.7 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.077 | 0.66 | 0.34 | 0.00 | 6.03 | 33.0/21.9 | 19.2/28.4 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.58 | 0.42 | 0.47 | 5.96 | 33.0/22.4 | 19.2/29.6 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.064 | 0.68 | 0.32 | 0.00 | 9.27 | 34.7/23.6 | 18.8/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Casey Mittelstadt: 1+ goals YES | 14 | 0.192 | 0.175 | +0.043 | +0.027 | $2.53 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Adam Wilsby: 1+ goals YES | 5 | 0.077 | 0.070 | +0.024 | +0.017 | $1.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 11 | 0.151 | 0.138 | +0.034 | +0.021 | $1.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 26 | 0.315 | 0.300 | +0.041 | +0.026 | $2.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-9|yes; why: higher confidence-adjusted growth (12.17 vs 1.53 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.878 vs 0.363); relationships: KXNHLGOAL-26OCT22NSHBOS-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: BOS offense suppressed (<= 2 goals)
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (11.99 vs 9.46 bp); despite a smaller raw edge (+0.024 vs +0.034/contract); relationships: KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: NSH offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (9.46 vs 7.52 bp); despite a smaller raw edge (+0.034 vs +0.041/contract); relationships: KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT22NSHBOS-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.049); failure: NSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (9.46 vs 7.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.049); they share one thesis budget; relationships: KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT22NSHBOS-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.049); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis NSH:OFFENSE_4PLUS (p 0.3593): highest fidelity KXNHLAST-26OCT22NSHBOS-NSHFFORSBERG9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.315): highest fidelity KXNHLAST-26OCT22NSHBOS-BOSPZACHA18-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22NSHBOS-BOSCMCAVOY73-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4811): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-9|yes [FRAGILE], best adjusted EV KXNHLTOTAL-26OCT22NSHBOS-9|yes (same contract)
- KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.315, phi -0.181)
- KXNHLGOAL-26OCT22NSHBOS-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4176, phi -0.115)
- KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4176, phi -0.197)
- KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4176, phi -0.274)

portfolios: A EV +1.79 (adj +0.44) on $12.98, P(profit) 0.6164, adj growth 4.2 bp · B EV +2.32 (adj +1.51) on $8.58, P(profit) 0.5596, adj growth 14.3 bp · C EV +2.08 (adj +0.74) on $9.31, P(profit) 0.6679, adj growth 7.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYR @ TOR  ·  10000 joint draws  ·  458 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.498 / away 0.502

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYR_win | p_overtime | goals | shots TOR/NYR | TOR/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.53 | 0.47 | 0.00 | 6.02 | 27.4/27.4 | 23.9/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.50 | 0.50 | 0.46 | 5.95 | 27.5/27.6 | 24.3/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.49 | 0.51 | 0.00 | 9.23 | 29.0/29.1 | 23.0/23.0 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.078 | 0.46 | 0.54 | 0.00 | 6.06 | 21.8/32.4 | 28.5/18.4 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.063 | 0.60 | 0.40 | 0.00 | 6.03 | 32.0/21.9 | 18.9/28.0 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.48 | 0.52 | 0.45 | 5.94 | 21.9/32.7 | 29.2/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 10 | 0.138 | 0.125 | +0.032 | +0.018 | $1.61 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Taylor Raddysh: 1+ goals YES | 8 | 0.109 | 0.101 | +0.024 | +0.016 | $1.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Colton Sissons: 1+ goals YES | 11 | 0.136 | 0.128 | +0.019 | +0.011 | $1.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ assists YES | 26 | 0.322 | 0.286 | +0.048 | +0.012 | $1.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22NYRTOR-TORCSISSONS15-1|yes; why: higher confidence-adjusted growth (7.70 vs 0.00 bp); despite a smaller raw edge (+0.032 vs +0.048/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22NYRTOR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT22NYRTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: TOR offense suppressed (<= 2 goals)
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (6.74 vs 1.66 bp); despite a smaller raw edge (+0.024 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22NYRTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT22NYRTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NYR offense suppressed (<= 2 goals)
- **Colton Sissons: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22NYRTOR-TORCSISSONS15-1|yes; why: higher confidence-adjusted growth (2.59 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.048/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22NYRTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT22NYRTOR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: TOR offense suppressed (<= 2 goals)
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22NYRTOR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (1.66 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22NYRTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT22NYRTOR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT22NYRTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NYR:OFFENSE_4PLUS (p 0.3865): highest fidelity KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.3922): highest fidelity KXNHLGOAL-26OCT22NYRTOR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22NYRTOR-NYRPDOROFEYEV16-1|no (same contract)
- thesis TOR:OFFENSE_4PLUS (p 0.404): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT22NYRTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3754, phi -0.178)
- KXNHLGOAL-26OCT22NYRTOR-NYRTRADDYSH14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3922, phi -0.133)
- KXNHLGOAL-26OCT22NYRTOR-TORCSISSONS15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3754, phi -0.176)
- KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3922, phi -0.26)

portfolios: A EV +2.08 (adj +0.98) on $12.86, P(profit) 0.4803, adj growth 9.0 bp · B EV +1.29 (adj +0.69) on $5.44, P(profit) 0.3357, adj growth 6.6 bp · C EV +0.46 (adj +0.14) on $5.93, P(profit) 0.3215, adj growth 1.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ OTT  ·  10000 joint draws  ·  524 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.544 / away 0.456

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_SJS_win | p_overtime | goals | shots OTT/SJS | OTT/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.56 | 0.44 | 0.00 | 6.01 | 26.9/26.6 | 23.2/23.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.108 | 0.63 | 0.37 | 0.00 | 6.03 | 32.0/21.0 | 18.1/27.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.54 | 0.46 | 0.46 | 5.99 | 27.1/26.7 | 23.4/23.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.57 | 0.43 | 0.46 | 5.95 | 32.4/21.4 | 18.2/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.57 | 0.43 | 0.00 | 9.35 | 28.7/28.2 | 22.4/22.3 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.074 | 0.65 | 0.35 | 0.00 | 9.33 | 34.2/22.5 | 17.5/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ridly Greig: 1+ goals YES | 16 | 0.201 | 0.190 | +0.032 | +0.020 | $2.13 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 56 | 0.707 | 0.602 | +0.129 | +0.024 | $5.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Macklin Celebrini: 1+ assists NO | 39 | 0.567 | 0.430 | +0.160 | +0.024 | $3.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.74) | CALIBRATION_WARNING | D |
| Ivar Stenberg: 1+ assists NO | 69 | 0.769 | 0.724 | +0.064 | +0.019 | $5.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22SJOTT-OTTTKLEVEN43-1|yes; why: higher confidence-adjusted growth (6.30 vs 0.00 bp); despite a smaller raw edge (+0.032 vs +0.099/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: OTT offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT22SJOTT-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (5.29 vs 2.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: OTT offense succeeds (4+ goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (5.09 vs 3.97 bp); evidence CALIBRATION_WARNING vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.061); failure: SJS offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no; why: second expression of the same thesis: KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no has the higher standalone adjusted growth (5.09 vs 3.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.061); they share one thesis budget; relationships: KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.061); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis OTT:SUPPRESSED (p 0.3446): highest fidelity KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no (same contract)
- thesis SJS:SUPPRESSED (p 0.4233): highest fidelity KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.441): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3446, phi -0.198)
- KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.1 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.441, phi -0.229)
- KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 26% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.1 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3576, phi -0.28)
- KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3576, phi -0.215)

portfolios: A EV +3.15 (adj +0.52) on $12.98, P(profit) 0.5982, adj growth 4.9 bp · B EV +3.48 (adj +0.85) on $17.13, P(profit) 0.7035, adj growth 8.1 bp · C EV +3.32 (adj +0.56) on $11.55, P(profit) 0.7065, adj growth 5.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## ANA @ NJD  ·  10000 joint draws  ·  444 bet sides mapped, 29 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_ANA_win | p_overtime | goals | shots NJD/ANA | NJD/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.54 | 0.46 | 0.00 | 6.05 | 28.7/28.3 | 24.8/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.46 | 5.95 | 28.8/28.4 | 25.2/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.57 | 0.43 | 0.00 | 9.4 | 30.4/30.1 | 24.3/23.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.086 | 0.64 | 0.36 | 0.00 | 6.02 | 33.9/22.7 | 19.8/29.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.56 | 0.44 | 0.46 | 5.9 | 33.7/22.8 | 19.8/30.3 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.061 | 0.66 | 0.34 | 0.00 | 9.33 | 35.6/24.1 | 19.2/27.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 13 | 0.211 | 0.188 | +0.073 | +0.050 | $4.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 17 | 0.222 | 0.207 | +0.042 | +0.028 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 61 | 0.670 | 0.652 | +0.043 | +0.026 | $5.60 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 72 | 0.761 | 0.750 | +0.027 | +0.015 | $4.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (44.88 vs 11.18 bp); relationships: KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT22ANANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes has the higher standalone adjusted growth (44.88 vs 11.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.021); they share one thesis budget; relationships: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22ANANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: ANA offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT22ANANJ-NJ2|no; why: Player prop expression KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.84 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22ANANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: NJD offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT22ANANJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT22ANANJ-NJLHUGHES43-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3732): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.2482): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4538): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4121, phi -0.223)
- KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4121, phi -0.215)
- KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4395, phi -0.251)
- KXNHLGOAL-26OCT22ANANJ-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4395, phi -0.225)
- override: Player prop expression KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.84 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT22ANANJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT22ANANJ-NJLHUGHES43-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.15 (adj +0.50) on $12.98, P(profit) 0.5867, adj growth 4.6 bp · B EV +3.36 (adj +2.24) on $17.12, P(profit) 0.368, adj growth 21.3 bp · C EV +3.63 (adj +2.45) on $13.78, P(profit) 0.2109, adj growth 22.9 bp · R EV +0.14 (adj +0.08) on $2.00, P(profit) 0.67, adj growth 3.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22ANANJ-NJ|no == KXNHLGAME-26OCT22ANANJ-ANA|yes

## FLA @ PIT  ·  10000 joint draws  ·  544 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.495 / away 0.505

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_FLA_win | p_overtime | goals | shots PIT/FLA | PIT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.64 | 0.36 | 0.00 | 6.07 | 27.1/26.9 | 23.9/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.47 | 5.96 | 27.1/27.2 | 23.9/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.109 | 0.62 | 0.38 | 0.00 | 9.38 | 28.7/28.8 | 23.4/21.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.081 | 0.71 | 0.29 | 0.00 | 6.04 | 31.8/21.4 | 18.9/27.3 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.56 | 0.44 | 0.46 | 5.95 | 32.0/21.4 | 18.2/28.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.061 | 0.71 | 0.29 | 0.00 | 9.4 | 33.4/22.6 | 18.2/25.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 13 | 0.194 | 0.174 | +0.056 | +0.036 | $3.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 63 | 0.718 | 0.694 | +0.072 | +0.047 | $6.96 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 10 | 0.149 | 0.133 | +0.042 | +0.026 | $2.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 10 | 0.139 | 0.127 | +0.033 | +0.020 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (23.19 vs 15.73 bp); relationships: KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: PIT offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no; why: higher confidence-adjusted growth (21.46 vs 12.72 bp); relationships: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: FLA offense succeeds (4+ goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (23.19 vs 15.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.038); failure: PIT offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22FLAPIT-FLAGHATHAWAY21-1|yes; why: higher confidence-adjusted growth (9.30 vs 0.00 bp); despite a smaller raw edge (+0.033 vs +0.036/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.038); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4852): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS_BY_2PLUS (p 0.3716): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.428): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3078, phi -0.208)
- KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3515, phi -0.242)
- KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3078, phi -0.178)
- KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.428, phi -0.187)

portfolios: A EV +1.73 (adj +0.63) on $12.98, P(profit) 0.5769, adj growth 6.0 bp · B EV +3.53 (adj +2.26) on $14.29, P(profit) 0.4117, adj growth 21.6 bp · C EV +3.64 (adj +2.19) on $22.71, P(profit) 0.7451, adj growth 20.8 bp · R EV +0.22 (adj +0.15) on $2.00, P(profit) 0.718, adj growth 5.7 bp

## LAK @ NYI  ·  10000 joint draws  ·  406 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.497 / away 0.503

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_LAK_win | p_overtime | goals | shots NYI/LAK | NYI/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.54 | 0.46 | 0.00 | 5.97 | 27.2/27.1 | 23.7/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.50 | 0.50 | 0.47 | 5.89 | 27.3/27.2 | 24.0/24.1 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.083 | 0.62 | 0.38 | 0.00 | 5.94 | 32.2/21.6 | 18.8/27.9 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.56 | 0.44 | 0.47 | 5.82 | 32.3/21.9 | 18.6/28.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.57 | 0.43 | 0.00 | 9.19 | 28.9/28.7 | 23.2/22.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.50 | 0.50 | 0.46 | 2.77 | 25.8/25.9 | 24.4/24.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 21 | 0.247 | 0.237 | +0.026 | +0.015 | $1.64 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 55 | 0.619 | 0.582 | +0.051 | +0.015 | $3.01 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22LANYI-NYIJPAGEAU44-1|yes; why: higher confidence-adjusted growth (2.88 vs 0.34 bp); alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: NYI offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22LANYI-LA2|no; why: higher confidence-adjusted growth (1.90 vs 0.08 bp); alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3774): highest fidelity KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes (same contract)
- thesis LAK:SUPPRESSED (p 0.4549): highest fidelity KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no (same contract)
- KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4018, phi -0.231)
- KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3238, phi -0.284)

portfolios: A EV +0.72 (adj +0.28) on $7.33, P(profit) 0.7136, adj growth 2.6 bp · B EV +0.46 (adj +0.19) on $4.65, P(profit) 0.7136, adj growth 1.8 bp · C EV +0.60 (adj +0.25) on $6.07, P(profit) 0.7136, adj growth 2.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ STL  ·  10000 joint draws  ·  518 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.459 / away 0.541

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_VGK_win | p_overtime | goals | shots STL/VGK | STL/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.51 | 0.49 | 0.00 | 5.99 | 26.5/26.7 | 23.2/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.48 | 5.92 | 26.6/26.9 | 23.6/23.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.091 | 0.43 | 0.57 | 0.00 | 6.04 | 20.9/31.9 | 28.0/17.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.49 | 0.51 | 0.00 | 9.26 | 28.1/28.5 | 22.5/22.4 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.45 | 0.55 | 0.47 | 5.92 | 21.0/32.2 | 28.9/17.7 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.056 | 0.38 | 0.62 | 0.00 | 9.26 | 22.7/33.5 | 26.4/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Trevor Connelly: 1+ goals NO | 78 | 0.819 | 0.808 | +0.027 | +0.016 | $6.02 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 73 | 0.769 | 0.758 | +0.025 | +0.014 | $4.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 23 | 0.270 | 0.255 | +0.027 | +0.013 | $1.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 28 | 0.316 | 0.306 | +0.022 | +0.012 | $1.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Trevor Connelly: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (3.29 vs 2.38 bp); relationships: KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: VGK offense succeeds (4+ goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22VGKSTL-VGKWKARLSSON71-1|no; why: higher confidence-adjusted growth (2.38 vs 1.46 bp); despite a smaller raw edge (+0.025 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22VGKSTL-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense succeeds (4+ goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (1.84 vs 1.46 bp); relationships: KXNHLGOAL-26OCT22VGKSTL-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (1.84 vs 1.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT22VGKSTL-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.3959): highest fidelity KXNHLAST-26OCT22VGKSTL-VGKWKARLSSON71-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3858): highest fidelity KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22VGKSTL-VGKTCONNELLY24-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.385, phi -0.16)
- KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.385, phi -0.211)
- KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4001, phi -0.255)
- KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4001, phi -0.27)

portfolios: A EV +1.25 (adj +0.37) on $12.98, P(profit) 0.4027, adj growth 3.4 bp · B EV +0.61 (adj +0.33) on $13.17, P(profit) 0.6563, adj growth 3.2 bp · C EV +0.42 (adj +0.22) on $8.23, P(profit) 0.7692, adj growth 2.0 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.8186, adj growth 1.5 bp

## WPG @ DAL  ·  10000 joint draws  ·  510 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.643 / away 0.357

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_WPG_win | p_overtime | goals | shots DAL/WPG | DAL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.64 | 0.36 | 0.00 | 6.04 | 26.0/25.9 | 23.0/21.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.50 | 0.50 | 0.46 | 5.9 | 26.1/25.9 | 22.7/22.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.097 | 0.72 | 0.28 | 0.00 | 5.93 | 30.8/20.3 | 17.8/26.2 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.55 | 0.45 | 0.43 | 5.86 | 31.0/20.4 | 17.4/27.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.62 | 0.38 | 0.00 | 9.19 | 27.6/27.1 | 21.8/21.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.58 | 0.42 | 0.00 | 3.45 | 24.6/24.7 | 22.9/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Miro Heiskanen: 1+ goals NO | 86 | 0.898 | 0.886 | +0.029 | +0.017 | $5.78 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Gabriel Vilardi: 1+ goals YES | 22 | 0.266 | 0.253 | +0.034 | +0.021 | $2.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 66 | 0.711 | 0.697 | +0.035 | +0.021 | $4.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 27 | 0.304 | 0.294 | +0.020 | +0.011 | $1.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no; why: higher confidence-adjusted growth (5.79 vs 4.58 bp); despite a smaller raw edge (+0.029 vs +0.035/contract); relationships: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22WPGDAL-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: DAL offense succeeds (4+ goals)
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: higher confidence-adjusted growth (5.30 vs 1.88 bp); despite a smaller raw edge (+0.034 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22WPGDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22WPGDAL-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: WPG offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: higher confidence-adjusted growth (4.58 vs 1.88 bp); despite a smaller raw edge (+0.035 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22WPGDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22WPGDAL-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: DAL offense succeeds (4+ goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes has the higher standalone adjusted growth (5.30 vs 1.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT22WPGDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.025); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.2888): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.3693): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4421): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- KXNHLGOAL-26OCT22WPGDAL-DALMHEISKANEN4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4169, phi -0.139)
- KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4924, phi -0.28)
- KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4169, phi -0.242)
- KXNHLGOAL-26OCT22WPGDAL-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4924, phi -0.26)

portfolios: A EV +0.97 (adj +0.42) on $12.98, P(profit) 0.5997, adj growth 4.0 bp · B EV +0.86 (adj +0.51) on $13.98, P(profit) 0.4024, adj growth 5.0 bp · C EV +0.99 (adj +0.54) on $13.23, P(profit) 0.6584, adj growth 5.1 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.8976, adj growth 1.6 bp

## MIN @ CGY  ·  10000 joint draws  ·  438 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.353 / away 0.647

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_MIN_win | p_overtime | goals | shots CGY/MIN | CGY/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.43 | 0.57 | 0.00 | 6.03 | 29.2/29.5 | 25.6/25.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.49 | 0.51 | 0.49 | 5.91 | 29.5/29.7 | 26.4/26.0 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.085 | 0.38 | 0.62 | 0.00 | 5.98 | 23.6/34.8 | 30.3/20.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.45 | 0.55 | 0.00 | 9.18 | 31.0/31.2 | 24.7/25.2 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.49 | 0.51 | 0.47 | 5.88 | 23.6/34.9 | 31.5/20.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.43 | 0.57 | 0.00 | 3.45 | 28.1/28.3 | 26.2/26.4 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aydar Suniev: 1+ goals YES | 16 | 0.221 | 0.205 | +0.052 | +0.035 | $3.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 2+ goals NO | 87 | 0.914 | 0.899 | +0.036 | +0.021 | $6.32 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Minnesota over 3.5 goals scored NO | 50 | 0.590 | 0.542 | +0.072 | +0.025 | $3.73 | FUNDED_RESEARCH | $1 | MIN:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jesper Wallstedt: 23+ saves YES | 57 | 0.654 | 0.607 | +0.067 | +0.020 | $4.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:NET_HIGH_VOLUME | DIRECT (0.95) | EVIDENCE_MIXED | D |
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT22MINCGY-CGY2|yes; why: KXNHL1PSPREAD-26OCT22MINCGY-CGY2|yes has the higher standalone adjusted growth (41.82 vs 19.10 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.062); relationships: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSAVE-26OCT22MINCGY-MINJWALLSTEDT30-23|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: CGY offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 2+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no; why: higher confidence-adjusted growth (9.60 vs 8.39 bp); despite a smaller raw edge (+0.036 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.998 vs 0.793); relationships: KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4|no: REINFORCING (phi 0.247); KXNHLSAVE-26OCT22MINCGY-MINJWALLSTEDT30-23|yes: MOSTLY_INDEPENDENT (phi -0.042); failure: MIN offense succeeds (4+ goals)
- **Minnesota over 3.5 goals scored NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no; why: Broad expression KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4|no selected over broad KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no: REINFORCING (phi 0.247); KXNHLSAVE-26OCT22MINCGY-MINJWALLSTEDT30-23|yes: INTENTIONAL_DIVERSIFIER (phi -0.063); failure: MIN offense succeeds (4+ goals)
- **Jesper Wallstedt: 23+ saves YES** — thesis: MIN net faces heavy volume (33+ shots; CGY pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi -0.042); KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4|no: INTENTIONAL_DIVERSIFIER (phi -0.063); failure: MIN net faces light volume (<= 25 shots; CGY suppressed)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CGY:SCORES_FIRST (p 0.4706): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.3347): highest fidelity KXNHLTEAMTOTAL-26OCT22MINCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.2432): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4473, phi -0.228)
- KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3999, phi -0.246)
- KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3999, phi -0.978)
- KXNHLSAVE-26OCT22MINCGY-MINJWALLSTEDT30-23|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family MIXED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:NET_LOW_VOLUME (p 0.334, phi -0.767)
- override: Broad expression KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4|no selected over broad KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.64 (adj +0.47) on $12.98, P(profit) 0.607, adj growth 4.2 bp · B EV +2.21 (adj +1.11) on $17.40, P(profit) 0.5064, adj growth 10.7 bp · C EV +1.14 (adj +0.45) on $15.74, P(profit) 0.5926, adj growth 4.3 bp · R EV +0.22 (adj +0.10) on $3.00, P(profit) 0.5731, adj growth 3.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22MINCGY-MIN|no == KXNHLGAME-26OCT22MINCGY-CGY|yes

## CAR @ EDM  ·  10000 joint draws  ·  442 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.459 / away 0.541

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CAR_win | p_overtime | goals | shots EDM/CAR | EDM/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.65 | 0.35 | 0.00 | 6.04 | 27.6/28.2 | 25.1/23.3 | even strength |
| CAR shot control · normal event (5-7) · decided (2+) | 0.106 | 0.55 | 0.45 | 0.00 | 6.04 | 21.7/33.3 | 29.9/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.63 | 0.37 | 0.00 | 9.49 | 28.9/29.5 | 23.9/21.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.53 | 0.47 | 0.46 | 5.94 | 27.4/28.0 | 24.8/24.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.46 | 0.54 | 0.48 | 5.98 | 21.7/33.4 | 30.0/18.5 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.091 | 0.56 | 0.44 | 0.00 | 9.4 | 23.3/35.2 | 28.9/17.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 12 | 0.185 | 0.167 | +0.058 | +0.039 | $3.35 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 7 | 0.111 | 0.098 | +0.036 | +0.024 | $1.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 24 | 0.290 | 0.276 | +0.037 | +0.023 | $2.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 79 | 0.856 | 0.821 | +0.055 | +0.019 | $5.99 | FUNDED_RESEARCH | $2 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (29.28 vs 6.30 bp); relationships: KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.078); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (17.21 vs 6.30 bp); despite a smaller raw edge (+0.036 vs +0.037/contract); relationships: KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.076); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (6.30 vs 6.01 bp); despite a smaller raw edge (+0.037 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.119); failure: EDM offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: Broad expression KXNHLSPREAD-26OCT22CAREDM-CAR3|no selected over player prop KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.078); KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.076); KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.119); failure: CAR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CAR:SUPPRESSED (p 0.3931): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no — Broad expression KXNHLSPREAD-26OCT22CAREDM-CAR3|no selected over player prop KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis EDM:OFFENSE_4PLUS (p 0.4849): highest fidelity KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes [STRUCTURAL], best adjusted EV KXNHLAST-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS (p 0.5638): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-CAR2|no (same contract)
- KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3106, phi -0.166)
- KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3106, phi -0.138)
- KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3106, phi -0.224)
- KXNHLSPREAD-26OCT22CAREDM-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2309, phi -0.748)
- override: Broad expression KXNHLSPREAD-26OCT22CAREDM-CAR3|no selected over player prop KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.53 (adj +0.77) on $12.98, P(profit) 0.4947, adj growth 7.3 bp · B EV +3.17 (adj +1.97) on $13.55, P(profit) 0.4638, adj growth 18.7 bp · C EV +2.46 (adj +1.06) on $21.64, P(profit) 0.7319, adj growth 10.0 bp · R EV +0.59 (adj +0.35) on $3.00, P(profit) 0.1854, adj growth 13.4 bp

## UTA @ SEA  ·  10000 joint draws  ·  458 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.393 / away 0.607

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_UTA_win | p_overtime | goals | shots SEA/UTA | SEA/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.51 | 0.49 | 0.00 | 6.05 | 27.3/27.7 | 24.1/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.51 | 0.49 | 0.45 | 5.99 | 27.3/27.8 | 24.6/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.49 | 0.51 | 0.00 | 9.34 | 28.9/29.4 | 23.5/22.8 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.098 | 0.42 | 0.58 | 0.00 | 6.01 | 21.5/33.0 | 29.1/18.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.46 | 0.54 | 0.47 | 5.96 | 21.6/32.9 | 29.5/18.4 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.077 | 0.39 | 0.61 | 0.00 | 9.26 | 23.1/34.8 | 27.4/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Shane Wright: 1+ goals YES | 14 | 0.205 | 0.188 | +0.057 | +0.039 | $3.60 | FUNDED_RESEARCH | $1 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 10 | 0.136 | 0.126 | +0.030 | +0.020 | $1.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Mackie Samoskevich: 1+ goals YES | 17 | 0.218 | 0.202 | +0.038 | +0.022 | $2.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 12 | 0.151 | 0.142 | +0.023 | +0.015 | $1.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: higher confidence-adjusted growth (26.06 vs 6.06 bp); despite a smaller raw edge (+0.057 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT22UTASEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22UTASEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (26.06 vs 8.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT22UTASEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22UTASEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: SEA offense suppressed (<= 2 goals)
- **Mackie Samoskevich: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (26.06 vs 7.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22UTASEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: SEA offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (26.06 vs 4.07 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT22UTASEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4001): highest fidelity KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4891): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2807): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3757, phi -0.222)
- KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3757, phi -0.169)
- KXNHLGOAL-26OCT22UTASEA-SEAMSAMOSKEVICH11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3757, phi -0.196)
- KXNHLGOAL-26OCT22UTASEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3757, phi -0.164)

portfolios: A EV +2.66 (adj +0.49) on $12.98, P(profit) 0.5952, adj growth 4.3 bp · B EV +2.58 (adj +1.69) on $8.87, P(profit) 0.5433, adj growth 16.1 bp · C EV +2.53 (adj +1.49) on $13.64, P(profit) 0.2053, adj growth 13.9 bp · R EV +0.38 (adj +0.26) on $1.00, P(profit) 0.2053, adj growth 10.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22UTASEA-UTA|no == KXNHLGAME-26OCT22UTASEA-SEA|yes

## DET @ VAN  ·  10000 joint draws  ·  442 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.402 / away 0.598

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_DET_win | p_overtime | goals | shots VAN/DET | VAN/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.117 | 0.52 | 0.48 | 0.00 | 6.05 | 21.8/33.5 | 29.9/18.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.60 | 0.40 | 0.00 | 6.05 | 27.2/27.8 | 24.7/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.46 | 5.94 | 27.5/28.1 | 24.8/24.1 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.50 | 5.91 | 21.8/33.5 | 30.2/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.56 | 0.44 | 0.00 | 9.34 | 29.0/29.5 | 23.7/22.5 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.074 | 0.51 | 0.49 | 0.00 | 9.2 | 23.2/35.2 | 28.7/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Filip Chytil: 1+ goals YES | 19 | 0.270 | 0.246 | +0.069 | +0.046 | $4.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 19 | 0.259 | 0.241 | +0.059 | +0.040 | $3.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 12 | 0.177 | 0.158 | +0.049 | +0.030 | $2.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Dylan Larkin: 1+ goals NO | 67 | 0.720 | 0.705 | +0.034 | +0.019 | $5.38 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (27.74 vs 21.39 bp); relationships: KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (27.74 vs 21.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: VAN offense suppressed (<= 2 goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (27.74 vs 17.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.023); failure: VAN offense suppressed (<= 2 goals)
- **Dylan Larkin: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes has the higher standalone adjusted growth (9.48 vs 3.82 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.125); relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: DET offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4129): highest fidelity KXNHLTEAMTOTAL-26OCT22DETVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5383): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.3099): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-DET2|no (same contract)
- KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3705, phi -0.246)
- KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3705, phi -0.215)
- KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3705, phi -0.186)
- KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.358, phi -0.234)

portfolios: A EV +2.51 (adj +0.48) on $12.98, P(profit) 0.6508, adj growth 4.5 bp · B EV +3.78 (adj +2.44) on $15.82, P(profit) 0.5577, adj growth 23.3 bp · C EV +2.70 (adj +1.57) on $7.39, P(profit) 0.3838, adj growth 14.7 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7198, adj growth 2.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
