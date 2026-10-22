# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-22T17:42:20Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +22.61 | +6.47 | +22.35 | 0.780 | -14.21 | -24.03 | 60.28 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +27.74 | +13.99 | +26.16 | 0.770 | -17.70 | -28.55 | 133.35 |
| C best expression per thesis | 150.01 | +23.19 | +10.71 | +21.55 | 0.742 | -18.88 | -29.10 | 101.18 |
| R FUNDED research stakes | 22.00 | +2.73 | +1.56 | +1.99 | 0.602 | -5.40 | -7.17 | 0.00 |

## NSH @ BOS  ·  10000 joint draws  ·  426 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.567 / away 0.433

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
| Ryan O'Reilly: 1+ goals YES | 26 | 0.315 | 0.298 | +0.041 | +0.025 | $2.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Matthew Wood: 1+ goals YES | 16 | 0.202 | 0.190 | +0.033 | +0.021 | $2.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 12 | 0.151 | 0.141 | +0.024 | +0.013 | $1.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 61 | 0.659 | 0.644 | +0.033 | +0.018 | $4.33 | FUNDED_RESEARCH | $2 | BOS:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (6.83 vs 3.44 bp); relationships: KXNHLGOAL-26OCT22NSHBOS-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: NSH offense suppressed (<= 2 goals)
- **Matthew Wood: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes has the higher standalone adjusted growth (6.83 vs 6.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: NSH offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes has the higher standalone adjusted growth (6.83 vs 3.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.049); they share one thesis budget; relationships: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26OCT22NSHBOS-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: NSH offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22NSHBOS-BOSPZACHA18-1|no; why: Player prop expression KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT22NSHBOS-BOSPZACHA18-2|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.84 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT22NSHBOS-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis NSH:OFFENSE_4PLUS (p 0.3593): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-9|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.315): highest fidelity KXNHLAST-26OCT22NSHBOS-BOSPZACHA18-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no — Player prop expression KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT22NSHBOS-BOSPZACHA18-2|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.84 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis GAME:HIGH_EVENT (p 0.3084): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-9|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT22NSHBOS-9|yes (same contract)
- KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4176, phi -0.274)
- KXNHLGOAL-26OCT22NSHBOS-NSHMWOOD71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4176, phi -0.206)
- KXNHLGOAL-26OCT22NSHBOS-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4176, phi -0.197)
- KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4811, phi -0.256)
- override: Player prop expression KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT22NSHBOS-BOSPZACHA18-2|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.84 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.37 (adj +0.36) on $14.19, P(profit) 0.7436, adj growth 3.5 bp · B EV +1.31 (adj +0.78) on $10.64, P(profit) 0.5044, adj growth 7.5 bp · C EV +1.29 (adj +0.60) on $13.53, P(profit) 0.5851, adj growth 5.7 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.6592, adj growth 2.1 bp

## NYR @ TOR  ·  10000 joint draws  ·  444 bet sides mapped, 2 +EV candidates, 2 on card

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
| Teddy Blueger: 1+ goals YES | 10 | 0.138 | 0.125 | +0.032 | +0.018 | $1.68 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Colton Sissons: 1+ goals YES | 11 | 0.136 | 0.128 | +0.019 | +0.011 | $1.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22NYRTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (7.70 vs 0.10 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22NYRTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: TOR offense suppressed (<= 2 goals)
- **Colton Sissons: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22NYRTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (2.59 vs 0.10 bp); despite a smaller raw edge (+0.019 vs +0.026/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22NYRTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis TOR:OFFENSE_4PLUS (p 0.404): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT22NYRTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3754, phi -0.178)
- KXNHLGOAL-26OCT22NYRTOR-TORCSISSONS15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3754, phi -0.176)

portfolios: A EV +0.99 (adj +0.58) on $4.02, P(profit) 0.2523, adj growth 5.4 bp · B EV +0.67 (adj +0.39) on $2.73, P(profit) 0.2523, adj growth 3.7 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ OTT  ·  10000 joint draws  ·  524 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.552 / away 0.448

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
| Jake Sanderson: 1+ assists NO | 55 | 0.714 | 0.601 | +0.147 | +0.034 | $7.32 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Ridly Greig: 1+ goals YES | 16 | 0.197 | 0.186 | +0.028 | +0.017 | $1.98 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 67 | 0.777 | 0.704 | +0.091 | +0.019 | $5.78 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Macklin Celebrini: 1+ assists NO | 43 | 0.576 | 0.463 | +0.128 | +0.015 | $2.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.74) | CALIBRATION_WARNING | D |
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT22SJOTT-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (10.05 vs 1.81 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: OTT offense succeeds (4+ goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22SJOTT-OTTTKLEVEN43-1|yes; why: higher confidence-adjusted growth (4.50 vs 0.00 bp); despite a smaller raw edge (+0.028 vs +0.098/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: OTT offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (3.53 vs 2.12 bp); despite a smaller raw edge (+0.091 vs +0.128/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.074); failure: SJS offense succeeds (4+ goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no; why: second expression of the same thesis: KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no has the higher standalone adjusted growth (3.53 vs 2.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.074); they share one thesis budget; relationships: KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.074); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:SUPPRESSED (p 0.3423): highest fidelity KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4418): highest fidelity KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.4335): highest fidelity KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no (same contract)
- KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.4 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4418, phi -0.219)
- KXNHLGOAL-26OCT22SJOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3423, phi -0.197)
- KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.2 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3455, phi -0.242)
- KXNHLAST-26OCT22SJOTT-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 26% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.0 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3455, phi -0.278)

portfolios: A EV +3.30 (adj +0.53) on $14.19, P(profit) 0.5968, adj growth 5.0 bp · B EV +3.64 (adj +0.87) on $17.35, P(profit) 0.7028, adj growth 8.3 bp · C EV +3.62 (adj +0.96) on $18.44, P(profit) 0.6374, adj growth 9.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## ANA @ NJD  ·  10000 joint draws  ·  454 bet sides mapped, 23 +EV candidates, 4 on card

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
| A.J. Greer: 1+ goals YES | 13 | 0.209 | 0.187 | +0.071 | +0.049 | $4.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 62 | 0.803 | 0.674 | +0.166 | +0.038 | $6.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Sam Colangelo: 1+ goals YES | 12 | 0.154 | 0.144 | +0.027 | +0.017 | $1.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 62 | 0.670 | 0.656 | +0.034 | +0.020 | $4.30 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: higher confidence-adjusted growth (42.41 vs 7.61 bp); despite a smaller raw edge (+0.071 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22ANANJ-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: ANA offense suppressed (<= 2 goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: higher confidence-adjusted growth (13.54 vs 7.61 bp); relationships: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22ANANJ-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.043); failure: NJD offense succeeds (4+ goals)
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes has the higher standalone adjusted growth (42.41 vs 5.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: Player prop expression KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no selected over broad KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.043); KXNHLGOAL-26OCT22ANANJ-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3732): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4538): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.2482): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4121, phi -0.223)
- KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.8 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4395, phi -0.19)
- KXNHLGOAL-26OCT22ANANJ-ANASCOLANGELO12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4121, phi -0.174)
- KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4395, phi -0.251)
- override: Player prop expression KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no selected over broad KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.86 (adj +0.54) on $14.19, P(profit) 0.5988, adj growth 4.9 bp · B EV +4.68 (adj +2.37) on $17.21, P(profit) 0.6883, adj growth 22.6 bp · C EV +3.60 (adj +2.19) on $14.00, P(profit) 0.209, adj growth 20.5 bp · R EV +0.11 (adj +0.06) on $2.00, P(profit) 0.67, adj growth 2.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22ANANJ-NJ|no == KXNHLGAME-26OCT22ANANJ-ANA|yes

## FLA @ PIT  ·  10000 joint draws  ·  556 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.513 / away 0.487

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_FLA_win | p_overtime | goals | shots PIT/FLA | PIT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.63 | 0.37 | 0.00 | 6.03 | 26.9/26.8 | 24.0/22.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.65 | 0.35 | 0.00 | 9.43 | 28.5/28.4 | 23.2/21.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.54 | 0.46 | 0.48 | 5.97 | 27.0/26.8 | 23.6/23.5 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.082 | 0.68 | 0.32 | 0.00 | 6.03 | 32.2/21.6 | 18.9/27.5 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.57 | 0.43 | 0.45 | 5.96 | 31.7/21.5 | 18.3/28.3 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.065 | 0.71 | 0.29 | 0.00 | 9.23 | 33.5/23.0 | 18.5/25.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 63 | 0.710 | 0.689 | +0.064 | +0.042 | $7.32 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 14 | 0.193 | 0.176 | +0.045 | +0.028 | $2.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 11 | 0.152 | 0.138 | +0.035 | +0.021 | $1.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 10 | 0.136 | 0.124 | +0.030 | +0.018 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no; why: higher confidence-adjusted growth (17.22 vs 9.89 bp); relationships: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: FLA offense succeeds (4+ goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (12.99 vs 8.96 bp); relationships: KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (12.99 vs 8.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: PIT offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22FLAPIT-FLAGHATHAWAY21-1|yes; why: higher confidence-adjusted growth (7.49 vs 0.00 bp); despite a smaller raw edge (+0.030 vs +0.032/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis FLA:SUPPRESSED (p 0.426): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.4891): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:OFFENSE_4PLUS (p 0.352): highest fidelity KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes (same contract)
- KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.352, phi -0.247)
- KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3042, phi -0.195)
- KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3042, phi -0.175)
- KXNHLGOAL-26OCT22FLAPIT-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.426, phi -0.191)

portfolios: A EV +1.44 (adj +0.50) on $14.19, P(profit) 0.6834, adj growth 4.8 bp · B EV +2.60 (adj +1.63) on $13.71, P(profit) 0.4117, adj growth 15.5 bp · C EV +2.83 (adj +1.67) on $19.91, P(profit) 0.7168, adj growth 15.8 bp · R EV +0.20 (adj +0.13) on $2.00, P(profit) 0.7098, adj growth 5.1 bp

## LAK @ NYI  ·  10000 joint draws  ·  404 bet sides mapped, 3 +EV candidates, 3 on card

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
| Mats Zuccarello: 1+ assists NO | 64 | 0.833 | 0.691 | +0.177 | +0.035 | $7.32 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.247 | 0.237 | +0.026 | +0.015 | $1.74 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Scott Laughton: 1+ goals YES | 13 | 0.160 | 0.150 | +0.022 | +0.012 | $1.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (11.99 vs 0.66 bp); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.042); failure: LAK offense succeeds (4+ goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22LANYI-NYIJPAGEAU44-1|yes; why: higher confidence-adjusted growth (2.88 vs 0.81 bp); alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: NYI offense suppressed (<= 2 goals)
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22LANYI-LATMOORE12-1|yes; why: higher confidence-adjusted growth (2.53 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.044/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.4549): highest fidelity KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3774): highest fidelity KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.3238): highest fidelity KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes (same contract)
- KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.8 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3238, phi -0.19)
- KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4018, phi -0.231)
- KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4549, phi -0.219)

portfolios: A EV +2.08 (adj +0.62) on $9.80, P(profit) 0.3696, adj growth 5.9 bp · B EV +2.37 (adj +0.62) on $10.34, P(profit) 0.8384, adj growth 6.0 bp · C EV +2.84 (adj +0.74) on $12.38, P(profit) 0.8384, adj growth 7.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ STL  ·  10000 joint draws  ·  444 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.464 / away 0.536

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_VGK_win | p_overtime | goals | shots STL/VGK | STL/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.50 | 0.50 | 0.00 | 5.96 | 26.7/27.0 | 23.5/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.49 | 0.51 | 0.44 | 5.94 | 26.3/26.6 | 23.3/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.53 | 0.47 | 0.00 | 9.34 | 27.9/28.4 | 22.6/21.5 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.085 | 0.45 | 0.55 | 0.00 | 6.05 | 21.0/31.6 | 27.6/17.8 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.46 | 0.54 | 0.45 | 5.94 | 21.2/31.9 | 28.5/18.0 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.059 | 0.40 | 0.60 | 0.00 | 9.27 | 22.6/33.5 | 26.5/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 73 | 0.776 | 0.763 | +0.033 | +0.020 | $7.26 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 28 | 0.322 | 0.310 | +0.028 | +0.016 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22VGKSTL-VGKMSTONE61-2|no; why: higher confidence-adjusted growth (4.51 vs 1.45 bp); despite a smaller raw edge (+0.033 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: VGK offense succeeds (4+ goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22VGKSTL-STLJNEIGHBOURS63-1|yes; why: higher confidence-adjusted growth (2.76 vs 0.15 bp); despite a smaller raw edge (+0.028 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.3955): highest fidelity KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3843): highest fidelity KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes (same contract)
- KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.385, phi -0.218)
- KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3935, phi -0.254)

portfolios: A EV +0.52 (adj +0.31) on $8.49, P(profit) 0.3221, adj growth 2.9 bp · B EV +0.51 (adj +0.30) on $9.29, P(profit) 0.7764, adj growth 2.9 bp · C EV +0.61 (adj +0.36) on $11.12, P(profit) 0.7764, adj growth 3.5 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.7764, adj growth 2.0 bp

## WPG @ DAL  ·  10000 joint draws  ·  510 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.639 / away 0.361

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_WPG_win | p_overtime | goals | shots DAL/WPG | DAL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.63 | 0.37 | 0.00 | 6.03 | 25.8/25.7 | 22.7/21.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.50 | 5.88 | 26.2/25.9 | 22.7/22.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.096 | 0.69 | 0.31 | 0.00 | 5.96 | 31.0/20.5 | 17.9/26.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.53 | 0.47 | 0.43 | 5.88 | 30.8/20.5 | 17.4/27.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.63 | 0.37 | 0.00 | 9.24 | 27.7/27.3 | 22.2/20.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.58 | 0.42 | 0.00 | 3.43 | 24.5/24.4 | 22.7/22.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mikko Rantanen: 1+ goals NO | 66 | 0.716 | 0.700 | +0.041 | +0.024 | $6.49 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Gabriel Vilardi: 1+ goals YES | 22 | 0.261 | 0.248 | +0.029 | +0.016 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 71 | 0.772 | 0.739 | +0.048 | +0.014 | $2.45 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mark Scheifele: 1+ goals YES | 27 | 0.307 | 0.296 | +0.023 | +0.013 | $1.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22WPGDAL-DALTSEGUIN91-1|no; why: higher confidence-adjusted growth (5.79 vs 2.63 bp); despite a smaller raw edge (+0.041 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: REINFORCING (phi 0.171); KXNHLGOAL-26OCT22WPGDAL-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: DAL offense succeeds (4+ goals)
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: higher confidence-adjusted growth (3.25 vs 2.17 bp); despite a smaller raw edge (+0.029 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT22WPGDAL-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: WPG offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL2|no; why: Broad expression KXNHLSPREAD-26OCT22WPGDAL-DAL3|no selected over player prop KXNHLAST-26OCT22WPGDAL-DALTSEGUIN91-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: REINFORCING (phi 0.171); KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT22WPGDAL-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.145); failure: DAL wins by 2+
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes has the higher standalone adjusted growth (3.25 vs 1.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.145); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DAL:SUPPRESSED (p 0.375): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no — Broad expression KXNHLSPREAD-26OCT22WPGDAL-DAL3|no selected over player prop KXNHLAST-26OCT22WPGDAL-DALTSEGUIN91-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis WPG:OFFENSE_4PLUS (p 0.2951): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4468): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4089, phi -0.245)
- KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.49, phi -0.257)
- KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3432, phi -0.752)
- KXNHLGOAL-26OCT22WPGDAL-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.49, phi -0.289)
- override: Broad expression KXNHLSPREAD-26OCT22WPGDAL-DAL3|no selected over player prop KXNHLAST-26OCT22WPGDAL-DALTSEGUIN91-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.21 (adj +0.39) on $14.19, P(profit) 0.6495, adj growth 3.7 bp · B EV +0.88 (adj +0.46) on $12.07, P(profit) 0.6456, adj growth 4.4 bp · C EV +0.96 (adj +0.49) on $13.38, P(profit) 0.659, adj growth 4.6 bp · R EV +0.19 (adj +0.09) on $3.00, P(profit) 0.5853, adj growth 3.4 bp

## MIN @ CGY  ·  10000 joint draws  ·  434 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.362 / away 0.638

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_MIN_win | p_overtime | goals | shots CGY/MIN | CGY/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.43 | 0.57 | 0.00 | 5.99 | 29.1/29.5 | 25.5/25.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.49 | 0.51 | 0.47 | 5.93 | 29.3/29.5 | 26.1/26.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.44 | 0.56 | 0.00 | 9.16 | 30.8/31.0 | 24.4/25.3 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.080 | 0.38 | 0.62 | 0.00 | 5.96 | 23.6/34.7 | 30.3/20.6 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.43 | 0.57 | 0.45 | 5.92 | 23.6/35.1 | 31.8/20.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.41 | 0.59 | 0.00 | 3.46 | 28.1/28.5 | 26.3/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kirill Kaprizov: 1+ goals NO | 52 | 0.613 | 0.588 | +0.075 | +0.051 | $7.32 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Minnesota wins by over 1.5 goals NO | 59 | 0.680 | 0.633 | +0.073 | +0.026 | $2.99 | FUNDED_RESEARCH | $1 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jonathan Castagna: 1+ goals YES | 10 | 0.135 | 0.122 | +0.029 | +0.016 | $1.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 17 | 0.206 | 0.195 | +0.026 | +0.015 | $1.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN2|no; why: higher confidence-adjusted growth (22.76 vs 6.11 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.991 vs 0.887); relationships: KXNHLSPREAD-26OCT22MINCGY-MIN2|no: REINFORCING (phi 0.254); KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: MIN offense succeeds (4+ goals)
- **Minnesota wins by over 1.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no has the higher standalone adjusted growth (22.76 vs 6.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.254); they share one thesis budget; relationships: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: REINFORCING (phi 0.254); KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.119); KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.124); failure: MIN wins by 2+
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22MINCGY-MIN2|no has the higher standalone adjusted growth (6.11 vs 5.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.119); they share one thesis budget; relationships: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT22MINCGY-MIN2|no: MOSTLY_INDEPENDENT (phi 0.119); KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CGY offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22MINCGY-MIN2|no has the higher standalone adjusted growth (6.11 vs 3.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.124); they share one thesis budget; relationships: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT22MINCGY-MIN2|no: MOSTLY_INDEPENDENT (phi 0.124); KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.3746): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.4524): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.335): highest fidelity KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3955, phi -0.308)
- KXNHLSPREAD-26OCT22MINCGY-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3196, phi -1.0)
- KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.446, phi -0.187)
- KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.446, phi -0.218)

portfolios: A EV +1.80 (adj +0.72) on $14.19, P(profit) 0.5992, adj growth 6.8 bp · B EV +1.96 (adj +1.14) on $13.10, P(profit) 0.6656, adj growth 11.0 bp · C EV +1.82 (adj +1.04) on $13.67, P(profit) 0.6127, adj growth 9.9 bp · R EV +0.40 (adj +0.23) on $3.00, P(profit) 0.6127, adj growth 8.9 bp

## CAR @ EDM  ·  10000 joint draws  ·  418 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.481 / away 0.519

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CAR_win | p_overtime | goals | shots EDM/CAR | EDM/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.61 | 0.39 | 0.00 | 6.07 | 27.3/27.9 | 24.9/23.2 | even strength |
| CAR shot control · normal event (5-7) · decided (2+) | 0.107 | 0.54 | 0.46 | 0.00 | 6.04 | 21.9/33.5 | 29.9/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.64 | 0.36 | 0.00 | 9.54 | 29.0/29.7 | 24.3/21.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.52 | 0.48 | 0.48 | 6.01 | 27.6/28.0 | 24.6/24.2 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.51 | 0.49 | 0.48 | 5.97 | 22.1/33.7 | 30.2/18.9 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.094 | 0.54 | 0.46 | 0.00 | 9.29 | 23.2/34.7 | 28.6/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mattias Ekholm: 1+ goals YES | 7 | 0.116 | 0.104 | +0.042 | +0.029 | $2.38 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 13 | 0.180 | 0.165 | +0.042 | +0.027 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Logan Stankoven: 1+ goals YES | 26 | 0.315 | 0.300 | +0.042 | +0.027 | $3.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 69 | 0.766 | 0.726 | +0.061 | +0.021 | $6.38 | FUNDED_RESEARCH | $2 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes; why: higher confidence-adjusted growth (25.58 vs 4.73 bp); despite a smaller raw edge (+0.042 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.892 vs 0.754); relationships: KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT22CAREDM-CARLSTANKOVEN22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT22CAREDM-CAR2|no: MOSTLY_INDEPENDENT (phi 0.115); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes; why: higher confidence-adjusted growth (13.46 vs 4.73 bp); despite a smaller raw edge (+0.042 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.883 vs 0.754); relationships: KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT22CAREDM-CARLSTANKOVEN22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26OCT22CAREDM-CAR2|no: MOSTLY_INDEPENDENT (phi 0.11); failure: EDM offense suppressed (<= 2 goals)
- **Logan Stankoven: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22CAREDM-CARKMILLER19-1|yes; why: higher confidence-adjusted growth (7.74 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26OCT22CAREDM-CAR2|no: INTENTIONAL_DIVERSIFIER (phi -0.211); failure: CAR offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes; why: KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes has the higher standalone adjusted growth (4.73 vs 4.43 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.427); relationships: KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.11); KXNHLGOAL-26OCT22CAREDM-CARLSTANKOVEN22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.211); failure: CAR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CAR:OFFENSE_4PLUS (p 0.3847): highest fidelity KXNHLGOAL-26OCT22CAREDM-CARLSTANKOVEN22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22CAREDM-CARLSTANKOVEN22-1|yes (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.4821): highest fidelity KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes (same contract)
- thesis EDM:WINS (p 0.5641): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3097, phi -0.153)
- KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3097, phi -0.167)
- KXNHLGOAL-26OCT22CAREDM-CARLSTANKOVEN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:SUPPRESSED (p 0.3871, phi -0.272)
- KXNHLSPREAD-26OCT22CAREDM-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2341, phi -1.0)

portfolios: A EV +1.76 (adj +0.46) on $14.19, P(profit) 0.5883, adj growth 4.2 bp · B EV +3.23 (adj +1.97) on $15.05, P(profit) 0.4106, adj growth 18.7 bp · C EV +1.87 (adj +0.84) on $15.98, P(profit) 0.6541, adj growth 8.0 bp · R EV +0.73 (adj +0.45) on $3.00, P(profit) 0.1164, adj growth 16.2 bp

## UTA @ SEA  ·  10000 joint draws  ·  444 bet sides mapped, 16 +EV candidates, 4 on card

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
| Shane Wright: 1+ goals YES | 14 | 0.201 | 0.184 | +0.052 | +0.036 | $3.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 64 | 0.702 | 0.684 | +0.046 | +0.028 | $7.32 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 12 | 0.154 | 0.145 | +0.027 | +0.017 | $1.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 16 | 0.198 | 0.186 | +0.029 | +0.017 | $1.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: higher confidence-adjusted growth (21.91 vs 8.66 bp); despite a smaller raw edge (+0.052 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT22UTASEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22UTASEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: SEA offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: KXNHLSPREAD-26OCT22UTASEA-UTA3|no has the higher standalone adjusted growth (8.66 vs 7.61 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.138); relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT22UTASEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT22UTASEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: UTA offense succeeds (4+ goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (21.91 vs 5.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT22UTASEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (21.91 vs 4.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT22UTASEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, UTA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:OFFENSE_4PLUS (p 0.4116): highest fidelity KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4936): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- thesis UTA:SUPPRESSED (p 0.3693): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3742, phi -0.206)
- KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4158, phi -0.23)
- KXNHLGOAL-26OCT22UTASEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3742, phi -0.178)
- KXNHLGOAL-26OCT22UTASEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3742, phi -0.214)

portfolios: A EV +2.59 (adj +0.75) on $14.19, P(profit) 0.4936, adj growth 6.6 bp · B EV +2.40 (adj +1.56) on $14.22, P(profit) 0.3907, adj growth 14.8 bp · C EV +2.30 (adj +1.31) on $12.83, P(profit) 0.2009, adj growth 12.3 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.7021, adj growth 3.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22UTASEA-UTA|no == KXNHLGAME-26OCT22UTASEA-SEA|yes

## DET @ VAN  ·  10000 joint draws  ·  394 bet sides mapped, 19 +EV candidates, 4 on card

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
| Liam Ohgren: 1+ goals YES | 11 | 0.177 | 0.157 | +0.060 | +0.040 | $3.48 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 12 | 0.165 | 0.151 | +0.037 | +0.024 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Detroit wins by over 2.5 goals NO | 74 | 0.850 | 0.775 | +0.096 | +0.022 | $6.60 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jake DeBrusk: 1+ goals YES | 28 | 0.325 | 0.312 | +0.031 | +0.018 | $2.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: higher confidence-adjusted growth (32.33 vs 9.48 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.927 vs 0.458); relationships: KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT22DETVAN-DET3|no: MOSTLY_INDEPENDENT (phi 0.095); KXNHLGOAL-26OCT22DETVAN-VANJDEBRUSK74-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: higher confidence-adjusted growth (10.86 vs 9.48 bp); despite a smaller raw edge (+0.037 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.933 vs 0.458); relationships: KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT22DETVAN-DET3|no: MOSTLY_INDEPENDENT (phi 0.097); KXNHLGOAL-26OCT22DETVAN-VANJDEBRUSK74-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense suppressed (<= 2 goals)
- **Detroit wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes has the higher standalone adjusted growth (9.48 vs 5.61 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.208); relationships: KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.095); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.097); KXNHLGOAL-26OCT22DETVAN-VANJDEBRUSK74-1|yes: MOSTLY_INDEPENDENT (phi 0.13); failure: DET wins by 2+
- **Jake DeBrusk: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes has the higher standalone adjusted growth (9.48 vs 3.46 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.162); relationships: KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26OCT22DETVAN-DET3|no: MOSTLY_INDEPENDENT (phi 0.13); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4129): highest fidelity KXNHLTEAMTOTAL-26OCT22DETVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-DET2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.3098): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-DET2|no (same contract)
- thesis DET:SUPPRESSED (p 0.4132): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-DET2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3706, phi -0.186)
- KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3706, phi -0.177)
- KXNHLSPREAD-26OCT22DETVAN-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.5 pts; opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2486, phi -0.731)
- KXNHLGOAL-26OCT22DETVAN-VANJDEBRUSK74-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3706, phi -0.246)

portfolios: A EV +2.70 (adj +0.71) on $14.19, P(profit) 0.6072, adj growth 6.5 bp · B EV +3.48 (adj +1.90) on $14.28, P(profit) 0.5157, adj growth 18.0 bp · C EV +1.44 (adj +0.51) on $4.77, P(profit) 0.4983, adj growth 4.8 bp · R EV +0.77 (adj +0.40) on $3.00, P(profit) 0.1771, adj growth 14.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
