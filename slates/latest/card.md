# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-22T21:34:27Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +24.83 | +6.52 | +24.41 | 0.804 | -11.92 | -22.23 | 61.27 |
| B thesis-diversified (joint) ← optimiser card | 149.27 | +26.94 | +15.11 | +24.77 | 0.752 | -20.90 | -33.09 | 143.82 |
| C best expression per thesis | 149.23 | +24.54 | +10.85 | +22.94 | 0.742 | -21.36 | -32.47 | 102.11 |
| R FUNDED research stakes | 16.00 | +1.71 | +1.07 | +0.30 | 0.512 | -4.51 | -5.77 | 0.00 |

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
| Ryan O'Reilly: 1+ goals YES | 25 | 0.315 | 0.297 | +0.051 | +0.034 | $3.78 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Casey Mittelstadt: 1+ goals YES | 14 | 0.192 | 0.175 | +0.043 | +0.027 | $2.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Adam Wilsby: 1+ goals YES | 5 | 0.077 | 0.070 | +0.024 | +0.017 | $1.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 11 | 0.151 | 0.138 | +0.034 | +0.021 | $1.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (12.97 vs 9.46 bp); relationships: KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT22NSHBOS-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.049); failure: NSH offense suppressed (<= 2 goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-9|yes; why: higher confidence-adjusted growth (12.17 vs 1.53 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.878 vs 0.363); relationships: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT22NSHBOS-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: BOS offense suppressed (<= 2 goals)
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes has the higher standalone adjusted growth (12.97 vs 11.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NSH offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes has the higher standalone adjusted growth (12.97 vs 9.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.049); they share one thesis budget; relationships: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT22NSHBOS-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis NSH:OFFENSE_4PLUS (p 0.3593): highest fidelity KXNHLAST-26OCT22NSHBOS-NSHFFORSBERG9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.315): highest fidelity KXNHLAST-26OCT22NSHBOS-BOSPZACHA18-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22NSHBOS-BOSCMCAVOY73-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4811): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-9|yes [FRAGILE], best adjusted EV KXNHLTOTAL-26OCT22NSHBOS-9|yes (same contract)
- KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4176, phi -0.274)
- KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.315, phi -0.181)
- KXNHLGOAL-26OCT22NSHBOS-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4176, phi -0.115)
- KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4176, phi -0.197)

portfolios: A EV +2.25 (adj +0.77) on $12.98, P(profit) 0.5841, adj growth 7.4 bp · B EV +2.73 (adj +1.78) on $9.82, P(profit) 0.5596, adj growth 16.9 bp · C EV +2.43 (adj +0.98) on $12.24, P(profit) 0.3703, adj growth 9.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Teddy Blueger: 1+ goals YES | 10 | 0.138 | 0.125 | +0.032 | +0.018 | $1.69 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Taylor Raddysh: 1+ goals YES | 8 | 0.109 | 0.101 | +0.024 | +0.016 | $1.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Colton Sissons: 1+ goals YES | 11 | 0.136 | 0.128 | +0.019 | +0.011 | $1.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ assists YES | 26 | 0.322 | 0.286 | +0.048 | +0.012 | $1.49 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
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

portfolios: A EV +2.08 (adj +0.98) on $12.86, P(profit) 0.4803, adj growth 9.0 bp · B EV +1.35 (adj +0.73) on $5.71, P(profit) 0.3357, adj growth 6.9 bp · C EV +0.49 (adj +0.15) on $6.34, P(profit) 0.3215, adj growth 1.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Ridly Greig: 1+ goals YES | 16 | 0.201 | 0.190 | +0.032 | +0.020 | $2.26 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 56 | 0.707 | 0.602 | +0.129 | +0.024 | $6.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Michael Amadio: 1+ goals YES | 15 | 0.182 | 0.173 | +0.023 | +0.014 | $1.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 69 | 0.769 | 0.722 | +0.064 | +0.017 | $5.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22SJOTT-OTTTKLEVEN43-1|yes; why: higher confidence-adjusted growth (6.30 vs 0.00 bp); despite a smaller raw edge (+0.032 vs +0.099/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: OTT offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT22SJOTT-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (5.29 vs 2.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: OTT offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22SJOTT-OTTTKLEVEN43-1|yes; why: higher confidence-adjusted growth (3.07 vs 0.00 bp); despite a smaller raw edge (+0.023 vs +0.099/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.042); KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: OTT offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no; why: Player prop expression KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no selected over player prop KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.74 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis OTT:SUPPRESSED (p 0.3446): highest fidelity KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no (same contract)
- thesis SJS:SUPPRESSED (p 0.4233): highest fidelity KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no — Player prop expression KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no selected over player prop KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.74 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)
- thesis OTT:OFFENSE_4PLUS (p 0.441): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3446, phi -0.198)
- KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.1 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.441, phi -0.229)
- KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3446, phi -0.186)
- KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3576, phi -0.215)
- override: Player prop expression KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no selected over player prop KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.74 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +3.15 (adj +0.50) on $12.98, P(profit) 0.5982, adj growth 4.8 bp · B EV +2.63 (adj +0.82) on $16.19, P(profit) 0.6891, adj growth 7.8 bp · C EV +3.55 (adj +0.59) on $12.35, P(profit) 0.7065, adj growth 5.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## ANA @ NJD  ·  10000 joint draws  ·  444 bet sides mapped, 29 +EV candidates, 3 on card

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
| Alex Killorn: 1+ goals YES | 17 | 0.222 | 0.207 | +0.042 | +0.028 | $2.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 63 | 0.803 | 0.674 | +0.157 | +0.028 | $6.20 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 61 | 0.670 | 0.652 | +0.043 | +0.026 | $4.76 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22ANANJ-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (11.18 vs 4.21 bp); despite a smaller raw edge (+0.042 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: ANA offense suppressed (<= 2 goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no; why: KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no has the higher standalone adjusted growth (8.27 vs 7.49 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.188); relationships: KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.043); failure: NJD offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no; why: KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no has the higher standalone adjusted growth (8.27 vs 6.27 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.251); relationships: KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.043); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3732): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes — Broad expression KXNHLSPREAD-26OCT22ANANJ-ANA2|yes selected over player prop KXNHLAST-26OCT22ANANJ-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.55 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NJD:SUPPRESSED (p 0.3472): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.2482): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4121, phi -0.215)
- KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.8 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4395, phi -0.19)
- KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4395, phi -0.251)
- override: Broad expression KXNHLSPREAD-26OCT22ANANJ-ANA2|yes selected over player prop KXNHLAST-26OCT22ANANJ-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.55 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.88 (adj +0.46) on $12.98, P(profit) 0.5662, adj growth 4.4 bp · B EV +2.48 (adj +0.89) on $13.74, P(profit) 0.6462, adj growth 8.6 bp · C EV +3.41 (adj +1.28) on $21.79, P(profit) 0.4788, adj growth 12.0 bp · R EV +0.14 (adj +0.08) on $2.00, P(profit) 0.67, adj growth 3.1 bp
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
| Connor Dewar: 1+ goals YES | 13 | 0.194 | 0.174 | +0.056 | +0.036 | $3.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 63 | 0.718 | 0.694 | +0.072 | +0.047 | $7.31 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 10 | 0.149 | 0.133 | +0.042 | +0.026 | $2.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 10 | 0.139 | 0.127 | +0.033 | +0.020 | $1.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (23.19 vs 15.73 bp); relationships: KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: PIT offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no; why: higher confidence-adjusted growth (21.46 vs 19.31 bp); relationships: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: FLA offense succeeds (4+ goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (23.19 vs 15.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.038); failure: PIT offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22FLAPIT-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (9.30 vs 0.00 bp); despite a smaller raw edge (+0.033 vs +0.046/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.038); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4852): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS_BY_2PLUS (p 0.3716): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.428): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3078, phi -0.208)
- KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3515, phi -0.242)
- KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3078, phi -0.178)
- KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.428, phi -0.187)

portfolios: A EV +1.46 (adj +0.64) on $12.98, P(profit) 0.7043, adj growth 6.3 bp · B EV +3.71 (adj +2.37) on $15.00, P(profit) 0.4117, adj growth 22.6 bp · C EV +3.90 (adj +2.34) on $24.27, P(profit) 0.7451, adj growth 22.2 bp · R EV +0.22 (adj +0.15) on $2.00, P(profit) 0.718, adj growth 5.7 bp

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
| Brayden Schenn: 1+ goals YES | 21 | 0.247 | 0.237 | +0.026 | +0.015 | $1.72 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 55 | 0.619 | 0.582 | +0.051 | +0.015 | $3.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22LANYI-NYIJPAGEAU44-1|yes; why: higher confidence-adjusted growth (2.88 vs 0.34 bp); alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: NYI offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22LANYI-LA2|no; why: higher confidence-adjusted growth (1.90 vs 0.08 bp); alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3774): highest fidelity KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes (same contract)
- thesis LAK:SUPPRESSED (p 0.4549): highest fidelity KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no (same contract)
- KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4018, phi -0.231)
- KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3238, phi -0.284)

portfolios: A EV +0.72 (adj +0.28) on $7.33, P(profit) 0.7136, adj growth 2.6 bp · B EV +0.49 (adj +0.20) on $4.88, P(profit) 0.7136, adj growth 1.9 bp · C EV +0.65 (adj +0.26) on $6.49, P(profit) 0.7136, adj growth 2.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ STL  ·  10000 joint draws  ·  518 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.460 / away 0.540

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
| Trevor Connelly: 1+ goals NO | 78 | 0.819 | 0.808 | +0.027 | +0.016 | $6.32 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 23 | 0.270 | 0.257 | +0.027 | +0.015 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 73 | 0.769 | 0.758 | +0.025 | +0.014 | $4.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 28 | 0.316 | 0.306 | +0.022 | +0.012 | $1.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Trevor Connelly: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (3.29 vs 2.38 bp); relationships: KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: VGK offense succeeds (4+ goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (2.65 vs 1.46 bp); relationships: KXNHLGOAL-26OCT22VGKSTL-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: STL offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22VGKSTL-VGKWKARLSSON71-1|no; why: higher confidence-adjusted growth (2.38 vs 1.46 bp); despite a smaller raw edge (+0.025 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22VGKSTL-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense succeeds (4+ goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (2.65 vs 1.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT22VGKSTL-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.3858): highest fidelity KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3959): highest fidelity KXNHLAST-26OCT22VGKSTL-VGKWKARLSSON71-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22VGKSTL-VGKTCONNELLY24-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.385, phi -0.16)
- KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4001, phi -0.255)
- KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.385, phi -0.211)
- KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4001, phi -0.27)

portfolios: A EV +1.25 (adj +0.39) on $12.98, P(profit) 0.4027, adj growth 3.6 bp · B EV +0.67 (adj +0.38) on $14.13, P(profit) 0.6906, adj growth 3.6 bp · C EV +0.49 (adj +0.27) on $9.17, P(profit) 0.8288, adj growth 2.6 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.8186, adj growth 1.5 bp

## WPG @ DAL  ·  10000 joint draws  ·  510 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.636 / away 0.364

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
| Dylan Samberg: 1+ goals YES | 3 | 0.054 | 0.048 | +0.022 | +0.016 | $1.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Miro Heiskanen: 1+ goals NO | 86 | 0.898 | 0.886 | +0.029 | +0.017 | $7.18 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Gabriel Vilardi: 1+ goals YES | 22 | 0.266 | 0.253 | +0.034 | +0.021 | $2.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 67 | 0.711 | 0.698 | +0.026 | +0.013 | $3.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Dylan Samberg: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (17.65 vs 5.30 bp); despite a smaller raw edge (+0.022 vs +0.034/contract); relationships: KXNHLGOAL-26OCT22WPGDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: WPG offense suppressed (<= 2 goals)
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: higher confidence-adjusted growth (5.79 vs 1.88 bp); despite a smaller raw edge (+0.029 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22WPGDAL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: DAL offense succeeds (4+ goals)
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: higher confidence-adjusted growth (5.30 vs 1.88 bp); despite a smaller raw edge (+0.034 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22WPGDAL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT22WPGDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: WPG offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no has the higher standalone adjusted growth (1.88 vs 1.68 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.163); relationships: KXNHLGOAL-26OCT22WPGDAL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT22WPGDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.2888): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.3693): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- thesis GAME:TIGHT (p 0.4421): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- KXNHLGOAL-26OCT22WPGDAL-WPGDSAMBERG54-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4924, phi -0.106)
- KXNHLGOAL-26OCT22WPGDAL-DALMHEISKANEN4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4169, phi -0.139)
- KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4924, phi -0.28)
- KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4169, phi -0.242)

portfolios: A EV +0.90 (adj +0.38) on $12.98, P(profit) 0.6608, adj growth 3.6 bp · B EV +1.64 (adj +1.09) on $14.67, P(profit) 0.2988, adj growth 10.3 bp · C EV +0.74 (adj +0.35) on $7.88, P(profit) 0.2655, adj growth 3.3 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.8976, adj growth 1.6 bp

## MIN @ CGY  ·  10000 joint draws  ·  430 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.352 / away 0.647

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_MIN_win | p_overtime | goals | shots CGY/MIN | CGY/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.44 | 0.56 | 0.00 | 5.99 | 29.2/29.4 | 25.6/25.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.48 | 0.52 | 0.46 | 5.93 | 29.5/29.7 | 26.2/26.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.45 | 0.55 | 0.00 | 9.25 | 30.8/31.2 | 24.4/25.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.077 | 0.38 | 0.62 | 0.00 | 6.0 | 23.5/35.2 | 30.7/20.6 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.42 | 0.58 | 0.48 | 5.89 | 23.6/34.7 | 31.4/20.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.43 | 0.57 | 0.00 | 3.45 | 28.2/28.2 | 26.1/26.5 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Jones: 1+ goals NO | 86 | 0.914 | 0.899 | +0.046 | +0.031 | $7.31 | FUNDED_RESEARCH | $2 | CGY:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 17 | 0.224 | 0.208 | +0.044 | +0.028 | $2.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 51 | 0.620 | 0.545 | +0.092 | +0.018 | $3.54 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Morgan Frost: 1+ goals YES | 24 | 0.276 | 0.266 | +0.023 | +0.013 | $1.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Ben Jones: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22MINCGY-CGYJFARABEE86-1|no; why: higher confidence-adjusted growth (18.82 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT22MINCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: CGY offense succeeds (4+ goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT22MINCGY-CGY2|yes; why: KXNHL1PSPREAD-26OCT22MINCGY-CGY2|yes has the higher standalone adjusted growth (42.48 vs 11.50 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.074); relationships: KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT22MINCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: CGY offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no; why: Player prop expression KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no selected over broad KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.82 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT22MINCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi 0.03); failure: MIN offense succeeds (4+ goals)
- **Morgan Frost: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT22MINCGY-CGY2|yes; why: KXNHL1PSPREAD-26OCT22MINCGY-CGY2|yes has the higher standalone adjusted growth (42.48 vs 1.90 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.104); relationships: KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.03); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CGY:SCORES_FIRST (p 0.4801): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.3317): highest fidelity KXNHLTEAMTOTAL-26OCT22MINCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHL1PSPREAD-26OCT22MINCGY-CGY2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.2425): highest fidelity KXNHLSPREAD-26OCT22MINCGY-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.3317, phi -0.166)
- KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4486, phi -0.202)
- KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.5 pts; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3956, phi -0.313)
- KXNHLGOAL-26OCT22MINCGY-CGYMFROST16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4486, phi -0.257)
- override: Player prop expression KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no selected over broad KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.82 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.45 (adj +0.42) on $12.98, P(profit) 0.6162, adj growth 3.8 bp · B EV +1.87 (adj +0.92) on $15.38, P(profit) 0.3508, adj growth 8.9 bp · C EV +0.66 (adj +0.23) on $3.08, P(profit) 0.3695, adj growth 2.2 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.9142, adj growth 2.8 bp
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
| Mattias Ekholm: 1+ goals YES | 7 | 0.111 | 0.098 | +0.036 | +0.024 | $1.92 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 13 | 0.185 | 0.168 | +0.048 | +0.030 | $2.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 24 | 0.290 | 0.276 | +0.037 | +0.023 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 79 | 0.856 | 0.821 | +0.055 | +0.019 | $6.68 | FUNDED_RESEARCH | $2 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (17.21 vs 6.30 bp); despite a smaller raw edge (+0.036 vs +0.037/contract); relationships: KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.076); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (16.09 vs 6.30 bp); relationships: KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.078); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (6.30 vs 6.01 bp); despite a smaller raw edge (+0.037 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.119); failure: EDM offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: Broad expression KXNHLSPREAD-26OCT22CAREDM-CAR3|no selected over player prop KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.076); KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.078); KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.119); failure: CAR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CAR:SUPPRESSED (p 0.3931): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no — Broad expression KXNHLSPREAD-26OCT22CAREDM-CAR3|no selected over player prop KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis EDM:OFFENSE_4PLUS (p 0.4849): highest fidelity KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes [STRUCTURAL], best adjusted EV KXNHLAST-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS (p 0.5638): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-CAR2|no (same contract)
- KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3106, phi -0.138)
- KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3106, phi -0.166)
- KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3106, phi -0.224)
- KXNHLSPREAD-26OCT22CAREDM-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2309, phi -0.748)
- override: Broad expression KXNHLSPREAD-26OCT22CAREDM-CAR3|no selected over player prop KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.53 (adj +0.77) on $12.98, P(profit) 0.4947, adj growth 7.3 bp · B EV +2.70 (adj +1.59) on $13.83, P(profit) 0.4638, adj growth 15.1 bp · C EV +2.63 (adj +1.14) on $23.14, P(profit) 0.7319, adj growth 10.7 bp · R EV +0.62 (adj +0.37) on $3.00, P(profit) 0.111, adj growth 13.1 bp

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
| Shane Wright: 1+ goals YES | 14 | 0.205 | 0.188 | +0.057 | +0.039 | $3.78 | FUNDED_RESEARCH | $1 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 10 | 0.136 | 0.126 | +0.030 | +0.020 | $1.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Mackie Samoskevich: 1+ goals YES | 17 | 0.218 | 0.202 | +0.038 | +0.022 | $2.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 12 | 0.151 | 0.142 | +0.023 | +0.015 | $1.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
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

portfolios: A EV +2.66 (adj +0.45) on $12.98, P(profit) 0.6117, adj growth 4.1 bp · B EV +2.70 (adj +1.78) on $9.31, P(profit) 0.5433, adj growth 16.9 bp · C EV +2.71 (adj +1.59) on $14.58, P(profit) 0.2053, adj growth 14.8 bp · R EV +0.38 (adj +0.26) on $1.00, P(profit) 0.2053, adj growth 10.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22UTASEA-UTA|no == KXNHLGAME-26OCT22UTASEA-SEA|yes

## DET @ VAN  ·  10000 joint draws  ·  442 bet sides mapped, 21 +EV candidates, 4 on card

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
| Filip Chytil: 1+ goals YES | 19 | 0.270 | 0.246 | +0.069 | +0.046 | $4.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 19 | 0.259 | 0.241 | +0.059 | +0.040 | $3.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 12 | 0.177 | 0.158 | +0.049 | +0.030 | $2.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Dylan Larkin: 1+ goals NO | 67 | 0.720 | 0.705 | +0.034 | +0.019 | $5.65 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
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

portfolios: A EV +2.51 (adj +0.48) on $12.98, P(profit) 0.6508, adj growth 4.5 bp · B EV +3.97 (adj +2.56) on $16.61, P(profit) 0.5577, adj growth 24.4 bp · C EV +2.88 (adj +1.67) on $7.90, P(profit) 0.3838, adj growth 15.6 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7198, adj growth 2.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
