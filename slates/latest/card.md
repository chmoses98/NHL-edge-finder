# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-22T19:38:24Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +25.75 | +7.01 | +25.11 | 0.795 | -14.28 | -26.06 | 65.03 |
| B thesis-diversified (joint) ← optimiser card | 149.07 | +25.18 | +14.42 | +23.11 | 0.734 | -22.87 | -34.06 | 136.93 |
| C best expression per thesis | 149.03 | +26.10 | +12.18 | +23.32 | 0.702 | -29.44 | -42.30 | 111.89 |
| R FUNDED research stakes | 20.00 | +1.52 | +0.94 | +0.99 | 0.574 | -4.78 | -6.49 | 0.00 |

## NSH @ BOS  ·  10000 joint draws  ·  436 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.568 / away 0.432

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
| Casey Mittelstadt: 1+ goals YES | 14 | 0.192 | 0.175 | +0.043 | +0.027 | $2.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 11 | 0.151 | 0.138 | +0.034 | +0.021 | $2.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 26 | 0.315 | 0.297 | +0.041 | +0.024 | $2.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 61 | 0.659 | 0.646 | +0.033 | +0.019 | $4.47 | FUNDED_RESEARCH | $2 | BOS:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-9|yes; why: higher confidence-adjusted growth (12.17 vs 1.53 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.878 vs 0.363); relationships: KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: BOS offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (9.46 vs 6.16 bp); despite a smaller raw edge (+0.034 vs +0.041/contract); relationships: KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: NSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (9.46 vs 6.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.049); they share one thesis budget; relationships: KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: NSH offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22NSHBOS-BOSDPASTRNAK88-1|no; why: Player prop expression KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT22NSHBOS-BOSDPASTRNAK88-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.84 vs 0.72 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis NSH:OFFENSE_4PLUS (p 0.3593): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-9|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.315): highest fidelity KXNHLAST-26OCT22NSHBOS-BOSPZACHA18-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no — Player prop expression KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT22NSHBOS-BOSDPASTRNAK88-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.84 vs 0.72 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis BOS:OFFENSE_4PLUS (p 0.4811): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-9|yes [FRAGILE], best adjusted EV KXNHLTOTAL-26OCT22NSHBOS-9|yes (same contract)
- KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.315, phi -0.181)
- KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4176, phi -0.197)
- KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4176, phi -0.274)
- KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4811, phi -0.256)
- override: Player prop expression KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT22NSHBOS-BOSDPASTRNAK88-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.84 vs 0.72 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.29 (adj +0.93) on $13.01, P(profit) 0.6109, adj growth 8.9 bp · B EV +2.00 (adj +1.21) on $11.81, P(profit) 0.4524, adj growth 11.5 bp · C EV +1.74 (adj +0.96) on $13.71, P(profit) 0.7088, adj growth 8.8 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.6592, adj growth 2.2 bp

## NYR @ TOR  ·  10000 joint draws  ·  458 bet sides mapped, 4 +EV candidates, 4 on card

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
| Teddy Blueger: 1+ goals YES | 10 | 0.138 | 0.125 | +0.032 | +0.018 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Colton Sissons: 1+ goals YES | 11 | 0.136 | 0.128 | +0.019 | +0.011 | $1.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ assists YES | 26 | 0.322 | 0.286 | +0.048 | +0.012 | $1.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ goals NO | 67 | 0.708 | 0.696 | +0.022 | +0.010 | $3.32 | FUNDED_RESEARCH | $1 | NYR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22NYRTOR-TORCSISSONS15-1|yes; why: higher confidence-adjusted growth (7.70 vs 0.00 bp); despite a smaller raw edge (+0.032 vs +0.038/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22NYRTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT22NYRTOR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: TOR offense suppressed (<= 2 goals)
- **Colton Sissons: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22NYRTOR-TORCSISSONS15-1|yes; why: higher confidence-adjusted growth (2.59 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.038/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22NYRTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT22NYRTOR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: TOR offense suppressed (<= 2 goals)
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22NYRTOR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (1.66 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22NYRTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT22NYRTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT22NYRTOR-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.064); failure: NYR offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22NYRTOR-NYRMZIBANEJAD93-1|no; why: higher confidence-adjusted growth (1.05 vs 0.71 bp); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22NYRTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT22NYRTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.064); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NYR:OFFENSE_4PLUS (p 0.3865): highest fidelity KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.3922): highest fidelity KXNHLGOAL-26OCT22NYRTOR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22NYRTOR-NYRPDOROFEYEV16-1|no (same contract)
- thesis TOR:OFFENSE_4PLUS (p 0.404): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT22NYRTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3754, phi -0.178)
- KXNHLGOAL-26OCT22NYRTOR-TORCSISSONS15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3754, phi -0.176)
- KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3922, phi -0.26)
- KXNHLGOAL-26OCT22NYRTOR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3865, phi -0.239)

portfolios: A EV +1.81 (adj +0.79) on $12.54, P(profit) 0.4752, adj growth 7.3 bp · B EV +1.08 (adj +0.52) on $7.74, P(profit) 0.4161, adj growth 5.0 bp · C EV +0.63 (adj +0.20) on $8.11, P(profit) 0.3215, adj growth 1.8 bp · R EV +0.03 (adj +0.01) on $1.00, P(profit) 0.7075, adj growth 0.6 bp

## SJS @ OTT  ·  10000 joint draws  ·  524 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.548 / away 0.452

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_SJS_win | p_overtime | goals | shots OTT/SJS | OTT/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.59 | 0.41 | 0.00 | 6.06 | 27.1/26.8 | 23.5/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.48 | 5.94 | 27.1/26.6 | 23.2/23.8 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.107 | 0.67 | 0.33 | 0.00 | 6.02 | 32.3/21.1 | 18.5/27.8 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.55 | 0.45 | 0.45 | 5.92 | 32.2/21.0 | 17.9/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.59 | 0.41 | 0.00 | 9.29 | 28.4/28.0 | 22.4/21.8 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.076 | 0.65 | 0.35 | 0.00 | 9.24 | 33.9/22.5 | 17.9/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jake Sanderson: 1+ assists NO | 56 | 0.714 | 0.604 | +0.137 | +0.027 | $7.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Ridly Greig: 1+ goals YES | 16 | 0.197 | 0.186 | +0.028 | +0.017 | $2.02 | FUNDED_RESEARCH | $1 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 15 | 0.177 | 0.169 | +0.018 | +0.010 | $1.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 70 | 0.764 | 0.727 | +0.049 | +0.012 | $4.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT22SJOTT-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (6.48 vs 0.99 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT22SJOTT-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: OTT offense succeeds (4+ goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22SJOTT-OTTTKLEVEN43-1|yes; why: higher confidence-adjusted growth (4.50 vs 0.00 bp); despite a smaller raw edge (+0.028 vs +0.098/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT22SJOTT-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes has the higher standalone adjusted growth (4.50 vs 1.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT22SJOTT-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: OTT offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no; why: KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no has the higher standalone adjusted growth (1.82 vs 1.64 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.041); relationships: KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:SUPPRESSED (p 0.3423): highest fidelity KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4418): highest fidelity KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.4335): highest fidelity KXNHLAST-26OCT22SJOTT-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.9 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4418, phi -0.219)
- KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3423, phi -0.197)
- KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3423, phi -0.193)
- KXNHLAST-26OCT22SJOTT-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3455, phi -0.222)

portfolios: A EV +2.84 (adj +0.38) on $13.01, P(profit) 0.6053, adj growth 3.6 bp · B EV +2.50 (adj +0.70) on $15.01, P(profit) 0.6557, adj growth 6.6 bp · C EV +4.58 (adj +1.02) on $19.10, P(profit) 0.7844, adj growth 9.4 bp · R EV +0.16 (adj +0.10) on $1.00, P(profit) 0.197, adj growth 3.6 bp

## ANA @ NJD  ·  10000 joint draws  ·  444 bet sides mapped, 25 +EV candidates, 4 on card

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
| A.J. Greer: 1+ goals YES | 13 | 0.211 | 0.187 | +0.073 | +0.049 | $4.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 17 | 0.222 | 0.207 | +0.042 | +0.028 | $2.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Jackson LaCombe: 1+ goals YES | 10 | 0.141 | 0.127 | +0.035 | +0.021 | $1.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 61 | 0.670 | 0.654 | +0.043 | +0.027 | $6.88 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (42.71 vs 11.18 bp); relationships: KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT22ANANJ-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes has the higher standalone adjusted growth (42.71 vs 11.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.021); they share one thesis budget; relationships: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT22ANANJ-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: ANA offense suppressed (<= 2 goals)
- **Jackson LaCombe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes has the higher standalone adjusted growth (42.71 vs 9.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: ANA offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: Player prop expression KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.84 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22ANANJ-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3732): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4538): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.2482): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4121, phi -0.223)
- KXNHLGOAL-26OCT22ANANJ-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4121, phi -0.215)
- KXNHLGOAL-26OCT22ANANJ-ANAJLACOMBE2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4121, phi -0.171)
- KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4395, phi -0.251)
- override: Player prop expression KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.84 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.00 (adj +0.44) on $13.01, P(profit) 0.5883, adj growth 4.0 bp · B EV +4.14 (adj +2.70) on $16.10, P(profit) 0.4184, adj growth 25.6 bp · C EV +5.18 (adj +3.09) on $19.75, P(profit) 0.2109, adj growth 28.1 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.67, adj growth 3.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22ANANJ-NJ|no == KXNHLGAME-26OCT22ANANJ-ANA|yes

## FLA @ PIT  ·  10000 joint draws  ·  556 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.511 / away 0.489

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_FLA_win | p_overtime | goals | shots PIT/FLA | PIT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.62 | 0.38 | 0.00 | 6.04 | 27.2/27.0 | 24.0/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.109 | 0.63 | 0.37 | 0.00 | 9.35 | 28.6/28.4 | 23.1/21.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.53 | 0.47 | 0.47 | 6.0 | 27.1/27.1 | 23.8/23.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.083 | 0.67 | 0.33 | 0.00 | 6.03 | 32.1/21.4 | 18.7/27.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.066 | 0.73 | 0.27 | 0.00 | 9.38 | 33.7/22.7 | 18.4/25.2 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.57 | 0.43 | 0.46 | 5.99 | 31.8/21.7 | 18.5/28.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 13 | 0.190 | 0.171 | +0.052 | +0.033 | $3.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 10 | 0.149 | 0.133 | +0.043 | +0.027 | $2.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 63 | 0.708 | 0.688 | +0.062 | +0.041 | $7.42 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 10 | 0.141 | 0.128 | +0.035 | +0.022 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT22FLAPIT-FLA3|no; why: higher confidence-adjusted growth (19.70 vs 2.20 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.041); failure: FLA wins (incl. OT/SO)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (19.70 vs 16.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: PIT offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no; why: higher confidence-adjusted growth (16.38 vs 9.65 bp); relationships: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA wins by 2+; alternative: KXNHLPTS-26OCT22FLAPIT-PITSCROSBY87-2|no; why: higher confidence-adjusted growth (10.94 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.041); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.021); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:WINS_BY_2PLUS (p 0.3682): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.4848): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.5863): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:WINS (p 0.4137, phi -0.202)
- KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3072, phi -0.178)
- KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3572, phi -0.236)
- KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.422, phi -0.195)

portfolios: A EV +2.23 (adj +1.08) on $13.01, P(profit) 0.4881, adj growth 10.4 bp · B EV +3.65 (adj +2.33) on $15.32, P(profit) 0.4143, adj growth 22.2 bp · C EV +4.44 (adj +2.86) on $21.53, P(profit) 0.3096, adj growth 26.4 bp · R EV +0.19 (adj +0.13) on $2.00, P(profit) 0.7084, adj growth 4.9 bp

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
| Brayden Schenn: 1+ goals YES | 21 | 0.247 | 0.237 | +0.026 | +0.015 | $1.74 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 55 | 0.619 | 0.579 | +0.051 | +0.012 | $2.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22LANYI-NYIJPAGEAU44-1|yes; why: higher confidence-adjusted growth (2.88 vs 0.81 bp); alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: NYI offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22LANYI-LA3|no; why: higher confidence-adjusted growth (1.30 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0006 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3774): highest fidelity KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes (same contract)
- thesis LAK:SUPPRESSED (p 0.4549): highest fidelity KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no (same contract)
- KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4018, phi -0.231)
- KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3238, phi -0.284)

portfolios: A EV +0.72 (adj +0.26) on $7.35, P(profit) 0.7136, adj growth 2.4 bp · B EV +0.44 (adj +0.18) on $4.41, P(profit) 0.7136, adj growth 1.7 bp · C EV +0.74 (adj +0.29) on $7.39, P(profit) 0.7136, adj growth 2.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ STL  ·  10000 joint draws  ·  512 bet sides mapped, 8 +EV candidates, 4 on card

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
| Trevor Connelly: 1+ goals NO | 78 | 0.819 | 0.808 | +0.027 | +0.016 | $6.38 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 73 | 0.769 | 0.758 | +0.025 | +0.014 | $4.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Jake Neighbours: 1+ assists YES | 24 | 0.302 | 0.264 | +0.050 | +0.011 | $1.13 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
| Jimmy Snuggerud: 1+ goals YES | 28 | 0.316 | 0.305 | +0.022 | +0.011 | $1.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Trevor Connelly: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22VGKSTL-VGKMSTONE61-1|no; why: KXNHLAST-26OCT22VGKSTL-VGKMSTONE61-1|no has the higher standalone adjusted growth (3.98 vs 3.29 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.075); relationships: KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT22VGKSTL-STLJNEIGHBOURS63-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: VGK offense succeeds (4+ goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22VGKSTL-VGKMSTONE61-1|no; why: Player prop expression KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no selected over player prop KXNHLAST-26OCT22VGKSTL-VGKMSTONE61-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.89 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT22VGKSTL-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT22VGKSTL-STLJNEIGHBOURS63-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense succeeds (4+ goals)
- **Jake Neighbours: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (1.37 vs 1.17 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT22VGKSTL-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.091); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22VGKSTL-STLJNEIGHBOURS63-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT22VGKSTL-STLJNEIGHBOURS63-1|yes has the higher standalone adjusted growth (1.37 vs 1.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.091); they share one thesis budget; relationships: KXNHLGOAL-26OCT22VGKSTL-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT22VGKSTL-STLJNEIGHBOURS63-1|yes: MOSTLY_INDEPENDENT (phi 0.091); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.3959): highest fidelity KXNHLAST-26OCT22VGKSTL-VGKWKARLSSON71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22VGKSTL-VGKMSTONE61-1|no — Player prop expression KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no selected over player prop KXNHLAST-26OCT22VGKSTL-VGKMSTONE61-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.89 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis STL:OFFENSE_4PLUS (p 0.3858): highest fidelity KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT22VGKSTL-STLJNEIGHBOURS63-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22VGKSTL-VGKTCONNELLY24-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.385, phi -0.16)
- KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.385, phi -0.211)
- KXNHLAST-26OCT22VGKSTL-STLJNEIGHBOURS63-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4001, phi -0.239)
- KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4001, phi -0.27)
- override: Player prop expression KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no selected over player prop KXNHLAST-26OCT22VGKSTL-VGKMSTONE61-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.89 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.96 (adj +0.38) on $13.01, P(profit) 0.5641, adj growth 3.5 bp · B EV +0.69 (adj +0.31) on $13.47, P(profit) 0.6646, adj growth 3.0 bp · C EV +1.31 (adj +0.38) on $9.69, P(profit) 0.6123, adj growth 3.5 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.8186, adj growth 1.5 bp

## WPG @ DAL  ·  10000 joint draws  ·  510 bet sides mapped, 4 +EV candidates, 4 on card

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
| Gabriel Vilardi: 1+ goals YES | 21 | 0.266 | 0.247 | +0.044 | +0.025 | $2.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Miro Heiskanen: 1+ goals NO | 86 | 0.898 | 0.886 | +0.029 | +0.017 | $7.42 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 71 | 0.770 | 0.738 | +0.046 | +0.013 | $2.72 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mark Scheifele: 1+ goals YES | 27 | 0.304 | 0.294 | +0.020 | +0.011 | $1.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: higher confidence-adjusted growth (7.86 vs 1.88 bp); despite a smaller raw edge (+0.044 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22WPGDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.145); KXNHLGOAL-26OCT22WPGDAL-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: WPG offense suppressed (<= 2 goals)
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: higher confidence-adjusted growth (5.79 vs 1.88 bp); despite a smaller raw edge (+0.029 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.078); KXNHLGOAL-26OCT22WPGDAL-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: DAL offense succeeds (4+ goals)
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL2|no; why: higher confidence-adjusted growth (1.88 vs 0.12 bp); wins across more scripts (relative breadth 0.995 vs 0.868); alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.145); KXNHLGOAL-26OCT22WPGDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.078); KXNHLGOAL-26OCT22WPGDAL-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.139); failure: DAL wins by 2+
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes has the higher standalone adjusted growth (7.86 vs 1.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT22WPGDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.139); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.2888): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.3693): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- thesis GAME:TIGHT (p 0.4421): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4924, phi -0.28)
- KXNHLGOAL-26OCT22WPGDAL-DALMHEISKANEN4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4169, phi -0.139)
- KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3541, phi -0.738)
- KXNHLGOAL-26OCT22WPGDAL-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4924, phi -0.26)

portfolios: A EV +1.11 (adj +0.56) on $13.01, P(profit) 0.4345, adj growth 5.3 bp · B EV +1.03 (adj +0.54) on $13.97, P(profit) 0.4307, adj growth 5.2 bp · C EV +1.26 (adj +0.61) on $10.39, P(profit) 0.2655, adj growth 5.6 bp · R EV +0.13 (adj +0.06) on $3.00, P(profit) 0.7011, adj growth 2.2 bp

## MIN @ CGY  ·  10000 joint draws  ·  430 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.355 / away 0.645

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
| Ben Jones: 1+ goals NO | 86 | 0.914 | 0.899 | +0.046 | +0.031 | $7.42 | FUNDED_RESEARCH | $2 | CGY:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 17 | 0.224 | 0.208 | +0.044 | +0.028 | $3.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 51 | 0.620 | 0.545 | +0.092 | +0.018 | $3.60 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Morgan Frost: 1+ goals YES | 24 | 0.276 | 0.264 | +0.023 | +0.012 | $1.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Ben Jones: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22MINCGY-CGYJFARABEE86-1|no; why: higher confidence-adjusted growth (18.82 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT22MINCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: CGY offense succeeds (4+ goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT22MINCGY-CGY2|yes; why: KXNHL1PSPREAD-26OCT22MINCGY-CGY2|yes has the higher standalone adjusted growth (42.48 vs 11.50 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.074); relationships: KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT22MINCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: CGY offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN3|no; why: Player prop expression KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no selected over broad KXNHLSPREAD-26OCT22MINCGY-MIN3|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.75 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT22MINCGY-CGYMFROST16-1|yes: MOSTLY_INDEPENDENT (phi 0.03); failure: MIN offense succeeds (4+ goals)
- **Morgan Frost: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT22MINCGY-CGY2|yes; why: KXNHL1PSPREAD-26OCT22MINCGY-CGY2|yes has the higher standalone adjusted growth (42.48 vs 1.55 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.104); relationships: KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.03); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CGY:SCORES_FIRST (p 0.4801): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN3|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3317): highest fidelity KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.4542): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN3|no (same contract)
- KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.3317, phi -0.166)
- KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4486, phi -0.202)
- KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.5 pts; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3956, phi -0.313)
- KXNHLGOAL-26OCT22MINCGY-CGYMFROST16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4486, phi -0.257)
- override: Player prop expression KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no selected over broad KXNHLSPREAD-26OCT22MINCGY-MIN3|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.75 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.53 (adj +0.43) on $13.01, P(profit) 0.5996, adj growth 3.8 bp · B EV +1.89 (adj +0.92) on $15.47, P(profit) 0.3508, adj growth 8.9 bp · C EV +1.26 (adj +0.46) on $12.43, P(profit) 0.7978, adj growth 4.4 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.9142, adj growth 2.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22MINCGY-MIN|no == KXNHLGAME-26OCT22MINCGY-CGY|yes

## CAR @ EDM  ·  10000 joint draws  ·  454 bet sides mapped, 14 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.481 / away 0.519

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
| Alex Formenton: 1+ goals YES | 13 | 0.185 | 0.169 | +0.048 | +0.031 | $3.00 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 7 | 0.111 | 0.098 | +0.036 | +0.024 | $2.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 24 | 0.290 | 0.274 | +0.037 | +0.021 | $2.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (17.44 vs 5.03 bp); relationships: KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (17.21 vs 5.03 bp); despite a smaller raw edge (+0.036 vs +0.037/contract); relationships: KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (5.03 vs 3.80 bp); despite a smaller raw edge (+0.037 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4849): highest fidelity KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS_BY_2PLUS (p 0.3485): highest fidelity KXNHLSPREAD-26OCT22CAREDM-EDM2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-EDM2|yes (same contract)
- thesis EDM:WINS (p 0.5638): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-EDM2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3106, phi -0.166)
- KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3106, phi -0.138)
- KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3106, phi -0.224)

portfolios: A EV +1.87 (adj +0.56) on $13.01, P(profit) 0.5256, adj growth 5.1 bp · B EV +2.37 (adj +1.52) on $7.44, P(profit) 0.484, adj growth 14.3 bp · C EV +1.07 (adj +0.48) on $6.54, P(profit) 0.4952, adj growth 4.4 bp · R EV +0.34 (adj +0.23) on $1.00, P(profit) 0.1854, adj growth 8.4 bp

## UTA @ SEA  ·  10000 joint draws  ·  458 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.394 / away 0.606

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_UTA_win | p_overtime | goals | shots SEA/UTA | SEA/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.49 | 0.51 | 0.00 | 6.0 | 27.4/27.7 | 24.2/24.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.107 | 0.45 | 0.55 | 0.00 | 6.03 | 21.8/32.9 | 29.1/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.48 | 5.93 | 27.5/28.1 | 24.8/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.48 | 0.52 | 0.00 | 9.35 | 28.7/29.2 | 22.9/22.7 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.46 | 0.54 | 0.46 | 5.95 | 21.8/32.7 | 29.5/18.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.074 | 0.44 | 0.56 | 0.00 | 9.29 | 23.2/34.7 | 27.8/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Shane Wright: 1+ goals YES | 15 | 0.201 | 0.187 | +0.042 | +0.028 | $2.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 10 | 0.140 | 0.129 | +0.034 | +0.023 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 64 | 0.702 | 0.685 | +0.046 | +0.029 | $7.42 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 12 | 0.154 | 0.145 | +0.027 | +0.017 | $1.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: higher confidence-adjusted growth (12.62 vs 8.66 bp); despite a smaller raw edge (+0.042 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT22UTASEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (12.62 vs 11.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT22UTASEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: SEA offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: KXNHLSPREAD-26OCT22UTASEA-UTA3|no has the higher standalone adjusted growth (8.66 vs 8.31 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.138); relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT22UTASEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: UTA offense succeeds (4+ goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (12.62 vs 5.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, UTA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:OFFENSE_4PLUS (p 0.4116): highest fidelity KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4936): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- thesis UTA:SUPPRESSED (p 0.3693): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3742, phi -0.206)
- KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3742, phi -0.171)
- KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4158, phi -0.23)
- KXNHLGOAL-26OCT22UTASEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3742, phi -0.178)

portfolios: A EV +2.38 (adj +0.69) on $13.01, P(profit) 0.4936, adj growth 6.1 bp · B EV +2.30 (adj +1.51) on $14.05, P(profit) 0.3825, adj growth 14.3 bp · C EV +2.43 (adj +1.26) on $16.97, P(profit) 0.2009, adj growth 11.6 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.7021, adj growth 3.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22UTASEA-UTA|no == KXNHLGAME-26OCT22UTASEA-SEA|yes

## DET @ VAN  ·  10000 joint draws  ·  442 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.399 / away 0.601

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_DET_win | p_overtime | goals | shots VAN/DET | VAN/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.117 | 0.52 | 0.48 | 0.00 | 6.05 | 21.7/33.5 | 29.9/18.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.60 | 0.40 | 0.00 | 6.05 | 27.2/27.8 | 24.7/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.46 | 5.94 | 27.5/28.1 | 24.8/24.1 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.50 | 5.91 | 21.8/33.5 | 30.2/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.56 | 0.44 | 0.00 | 9.34 | 29.0/29.5 | 23.7/22.5 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.074 | 0.51 | 0.49 | 0.00 | 9.2 | 23.2/35.2 | 28.7/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Liam Ohgren: 1+ goals YES | 11 | 0.177 | 0.157 | +0.060 | +0.040 | $3.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 12 | 0.165 | 0.151 | +0.037 | +0.024 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Dylan Larkin: 1+ goals NO | 67 | 0.720 | 0.705 | +0.034 | +0.019 | $6.01 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Jake DeBrusk: 1+ goals YES | 28 | 0.325 | 0.312 | +0.031 | +0.018 | $2.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: higher confidence-adjusted growth (32.33 vs 9.48 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.927 vs 0.458); relationships: KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT22DETVAN-VANJDEBRUSK74-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: higher confidence-adjusted growth (10.86 vs 9.48 bp); despite a smaller raw edge (+0.037 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.933 vs 0.458); relationships: KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22DETVAN-VANJDEBRUSK74-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense suppressed (<= 2 goals)
- **Dylan Larkin: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes has the higher standalone adjusted growth (9.48 vs 3.82 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.125); relationships: KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22DETVAN-VANJDEBRUSK74-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: DET offense succeeds (4+ goals)
- **Jake DeBrusk: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes has the higher standalone adjusted growth (9.48 vs 3.46 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.162); relationships: KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4129): highest fidelity KXNHLTEAMTOTAL-26OCT22DETVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-DET2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.3098): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-DET2|no (same contract)
- thesis DET:SUPPRESSED (p 0.4132): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-DET2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3706, phi -0.186)
- KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3706, phi -0.177)
- KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.358, phi -0.234)
- KXNHLGOAL-26OCT22DETVAN-VANJDEBRUSK74-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3706, phi -0.246)

portfolios: A EV +3.01 (adj +0.51) on $13.01, P(profit) 0.6805, adj growth 4.6 bp · B EV +3.10 (adj +1.98) on $14.28, P(profit) 0.4788, adj growth 18.7 bp · C EV +1.45 (adj +0.57) on $3.42, P(profit) 0.1966, adj growth 5.2 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7198, adj growth 2.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
