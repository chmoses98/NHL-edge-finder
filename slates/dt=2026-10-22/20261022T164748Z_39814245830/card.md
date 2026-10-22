# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-22T16:47:48Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +23.93 | +7.08 | +23.60 | 0.779 | -15.60 | -26.57 | 66.12 |
| B thesis-diversified (joint) ← optimiser card | 149.37 | +25.64 | +12.72 | +24.23 | 0.768 | -17.93 | -28.00 | 121.36 |
| C best expression per thesis | 149.99 | +25.68 | +12.06 | +24.16 | 0.725 | -23.21 | -35.34 | 112.83 |
| R FUNDED research stakes | 24.00 | +2.26 | +1.22 | +2.36 | 0.637 | -5.18 | -7.17 | 0.00 |

## NSH @ BOS  ·  10000 joint draws  ·  426 bet sides mapped, 9 +EV candidates, 4 on card

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
| Ryan O'Reilly: 1+ goals YES | 26 | 0.315 | 0.298 | +0.041 | +0.025 | $2.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Matthew Wood: 1+ goals YES | 16 | 0.202 | 0.190 | +0.033 | +0.021 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 61 | 0.659 | 0.644 | +0.033 | +0.018 | $4.21 | FUNDED_RESEARCH | $2 | BOS:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Casey Mittelstadt: 1+ goals YES | 15 | 0.192 | 0.171 | +0.033 | +0.013 | $1.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-9|yes; why: higher confidence-adjusted growth (6.83 vs 1.53 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.915 vs 0.363); relationships: KXNHLGOAL-26OCT22NSHBOS-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: NSH offense suppressed (<= 2 goals)
- **Matthew Wood: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes has the higher standalone adjusted growth (6.83 vs 6.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: NSH offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22NSHBOS-BOSPZACHA18-1|no; why: higher confidence-adjusted growth (2.95 vs 2.44 bp); despite a smaller raw edge (+0.033 vs +0.088/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT22NSHBOS-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: BOS offense succeeds (4+ goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-9|yes; why: higher confidence-adjusted growth (2.54 vs 1.53 bp); despite a smaller raw edge (+0.033 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.878 vs 0.363); relationships: KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT22NSHBOS-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis NSH:OFFENSE_4PLUS (p 0.3593): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-9|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.315): highest fidelity KXNHLAST-26OCT22NSHBOS-BOSPZACHA18-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4811): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-9|yes [FRAGILE], best adjusted EV KXNHLTOTAL-26OCT22NSHBOS-9|yes (same contract)
- KXNHLGOAL-26OCT22NSHBOS-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4176, phi -0.274)
- KXNHLGOAL-26OCT22NSHBOS-NSHMWOOD71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4176, phi -0.206)
- KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4811, phi -0.256)
- KXNHLGOAL-26OCT22NSHBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.315, phi -0.181)

portfolios: A EV +1.83 (adj +0.36) on $13.81, P(profit) 0.5333, adj growth 3.4 bp · B EV +1.31 (adj +0.74) on $10.43, P(profit) 0.5237, adj growth 7.1 bp · C EV +1.44 (adj +0.68) on $15.19, P(profit) 0.5851, adj growth 6.3 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.6592, adj growth 2.1 bp

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
| Teddy Blueger: 1+ goals YES | 10 | 0.138 | 0.122 | +0.032 | +0.016 | $1.43 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ assists YES | 25 | 0.322 | 0.276 | +0.058 | +0.013 | $1.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22NYRTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (5.77 vs 0.10 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: TOR offense suppressed (<= 2 goals)
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22NYRTOR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (1.79 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22NYRTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NYR:OFFENSE_4PLUS (p 0.3865): highest fidelity KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes (same contract)
- thesis TOR:OFFENSE_4PLUS (p 0.404): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT22NYRTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3754, phi -0.178)
- KXNHLAST-26OCT22NYRTOR-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3922, phi -0.26)

portfolios: A EV +1.94 (adj +0.63) on $7.92, P(profit) 0.4176, adj growth 5.5 bp · B EV +0.74 (adj +0.28) on $2.86, P(profit) 0.4176, adj growth 2.7 bp · C EV +0.42 (adj +0.09) on $1.92, P(profit) 0.3215, adj growth 0.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ OTT  ·  10000 joint draws  ·  462 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.554 / away 0.446

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_SJS_win | p_overtime | goals | shots OTT/SJS | OTT/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.59 | 0.41 | 0.00 | 6.02 | 27.0/26.6 | 23.4/23.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.113 | 0.65 | 0.35 | 0.00 | 5.97 | 32.1/20.9 | 18.1/27.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.51 | 0.49 | 0.48 | 5.94 | 27.3/26.7 | 23.4/24.0 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.56 | 0.44 | 0.46 | 5.91 | 32.4/21.3 | 18.2/28.9 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.078 | 0.68 | 0.32 | 0.00 | 9.2 | 33.7/22.5 | 18.1/25.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.59 | 0.41 | 0.00 | 9.27 | 28.4/27.8 | 22.1/21.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jake Sanderson: 1+ assists NO | 54 | 0.710 | 0.596 | +0.153 | +0.039 | $7.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Michael Amadio: 1+ goals YES | 15 | 0.183 | 0.174 | +0.024 | +0.015 | $1.58 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 67 | 0.776 | 0.704 | +0.090 | +0.018 | $5.86 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Mason Marchment: 1+ assists NO | 71 | 0.770 | 0.735 | +0.046 | +0.011 | $3.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT22SJOTT-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (13.42 vs 0.85 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT22SJOTT-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: OTT offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22SJOTT-OTTNCOUSINS21-1|yes; why: higher confidence-adjusted growth (3.55 vs 0.00 bp); despite a smaller raw edge (+0.024 vs +0.043/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.042); KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT22SJOTT-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: OTT offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22SJOTT-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (3.40 vs 1.25 bp); relationships: KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT22SJOTT-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.044); failure: SJS offense succeeds (4+ goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no; why: second expression of the same thesis: KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no has the higher standalone adjusted growth (3.40 vs 1.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.044); they share one thesis budget; relationships: KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.044); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis OTT:SUPPRESSED (p 0.3406): highest fidelity KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no (same contract)
- thesis SJS:SUPPRESSED (p 0.4437): highest fidelity KXNHLAST-26OCT22SJOTT-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.4433): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.5 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4433, phi -0.24)
- KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3406, phi -0.191)
- KXNHLAST-26OCT22SJOTT-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.1 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3393, phi -0.21)
- KXNHLAST-26OCT22SJOTT-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3393, phi -0.245)

portfolios: A EV +2.15 (adj +0.59) on $13.81, P(profit) 0.5357, adj growth 5.8 bp · B EV +3.18 (adj +0.85) on $17.92, P(profit) 0.6266, adj growth 8.2 bp · C EV +3.79 (adj +0.91) on $18.16, P(profit) 0.5514, adj growth 8.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## ANA @ NJD  ·  10000 joint draws  ·  454 bet sides mapped, 22 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.652 / away 0.348

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_ANA_win | p_overtime | goals | shots NJD/ANA | NJD/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.57 | 0.43 | 0.00 | 6.03 | 28.8/28.5 | 25.3/25.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.45 | 5.98 | 28.9/28.5 | 25.2/25.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.54 | 0.46 | 0.00 | 9.28 | 30.2/30.1 | 24.1/23.8 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.085 | 0.60 | 0.40 | 0.00 | 6.01 | 33.9/22.8 | 19.8/29.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.54 | 0.46 | 0.48 | 5.94 | 34.1/22.8 | 19.6/30.7 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.058 | 0.66 | 0.34 | 0.00 | 9.35 | 35.6/24.3 | 19.2/27.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 13 | 0.210 | 0.187 | +0.072 | +0.050 | $4.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 63 | 0.800 | 0.676 | +0.153 | +0.030 | $6.18 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 62 | 0.675 | 0.660 | +0.039 | +0.024 | $4.57 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: higher confidence-adjusted growth (43.57 vs 3.63 bp); despite a smaller raw edge (+0.072 vs +0.090/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: ANA offense suppressed (<= 2 goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no; why: higher confidence-adjusted growth (8.68 vs 6.29 bp); wins across more scripts (relative breadth 1.011 vs 0.807); relationships: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.033); failure: NJD offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no; why: KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no has the higher standalone adjusted growth (6.29 vs 5.31 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.243); relationships: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.033); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3704): highest fidelity KXNHLTEAMTOTAL-26OCT22ANANJ-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3497): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4607): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4037, phi -0.228)
- KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.0 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4306, phi -0.201)
- KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4306, phi -0.247)

portfolios: A EV +3.21 (adj +0.59) on $13.81, P(profit) 0.6363, adj growth 5.4 bp · B EV +4.10 (adj +2.08) on $15.27, P(profit) 0.6388, adj growth 19.7 bp · C EV +4.01 (adj +2.50) on $9.44, P(profit) 0.4697, adj growth 23.1 bp · R EV +0.12 (adj +0.07) on $2.00, P(profit) 0.6752, adj growth 2.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22ANANJ-NJ|no == KXNHLGAME-26OCT22ANANJ-ANA|yes

## FLA @ PIT  ·  10000 joint draws  ·  528 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.511 / away 0.489

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
| Connor Dewar: 1+ goals YES | 14 | 0.193 | 0.174 | +0.045 | +0.025 | $2.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 11 | 0.152 | 0.136 | +0.035 | +0.019 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 63 | 0.690 | 0.672 | +0.043 | +0.026 | $5.19 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 67 | 0.727 | 0.710 | +0.042 | +0.025 | $5.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (10.77 vs 7.92 bp); relationships: KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (10.77 vs 7.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: PIT offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no; why: higher confidence-adjusted growth (6.44 vs 6.26 bp); relationships: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: FLA offense succeeds (4+ goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no has the higher standalone adjusted growth (6.44 vs 6.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4891): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.426): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.5934): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22FLAPIT-FLA2|no (same contract)
- KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3042, phi -0.195)
- KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3042, phi -0.175)
- KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.352, phi -0.264)
- KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.352, phi -0.233)

portfolios: A EV +1.79 (adj +0.73) on $13.81, P(profit) 0.5405, adj growth 7.0 bp · B EV +1.89 (adj +1.08) on $14.77, P(profit) 0.6432, adj growth 10.4 bp · C EV +1.80 (adj +0.95) on $15.88, P(profit) 0.6374, adj growth 8.9 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.6896, adj growth 3.0 bp

## LAK @ NYI  ·  10000 joint draws  ·  404 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.489 / away 0.511

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
| Mats Zuccarello: 1+ assists NO | 64 | 0.833 | 0.691 | +0.177 | +0.035 | $7.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.247 | 0.237 | +0.026 | +0.015 | $1.71 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Scott Laughton: 1+ goals YES | 13 | 0.160 | 0.150 | +0.022 | +0.012 | $1.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (11.99 vs 0.66 bp); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.042); failure: LAK offense succeeds (4+ goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT22LANYI-NYI3|yes; why: higher confidence-adjusted growth (2.88 vs 0.06 bp); despite a smaller raw edge (+0.026 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0025 below the 0.010/contract floor; relationships: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: NYI offense suppressed (<= 2 goals)
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22LANYI-LATMOORE12-1|yes; why: higher confidence-adjusted growth (2.53 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.044/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.4549): highest fidelity KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3774): highest fidelity KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.3238): highest fidelity KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes (same contract)
- KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.8 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3238, phi -0.19)
- KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4018, phi -0.231)
- KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4549, phi -0.219)

portfolios: A EV +2.02 (adj +0.60) on $9.54, P(profit) 0.3696, adj growth 5.7 bp · B EV +2.32 (adj +0.61) on $10.12, P(profit) 0.8384, adj growth 5.9 bp · C EV +3.19 (adj +0.83) on $13.90, P(profit) 0.8384, adj growth 8.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ STL  ·  10000 joint draws  ·  440 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.467 / away 0.533

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
| Mitch Marner: 1+ goals NO | 73 | 0.776 | 0.763 | +0.033 | +0.020 | $7.11 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 28 | 0.322 | 0.309 | +0.028 | +0.015 | $1.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22VGKSTL-VGKMSTONE61-2|no; why: higher confidence-adjusted growth (4.51 vs 1.45 bp); despite a smaller raw edge (+0.033 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: VGK offense succeeds (4+ goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22VGKSTL-STLJNEIGHBOURS63-1|yes; why: higher confidence-adjusted growth (2.35 vs 0.15 bp); despite a smaller raw edge (+0.028 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.3955): highest fidelity KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3843): highest fidelity KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes (same contract)
- KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.385, phi -0.218)
- KXNHLGOAL-26OCT22VGKSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3935, phi -0.254)

portfolios: A EV +0.50 (adj +0.29) on $8.26, P(profit) 0.3221, adj growth 2.7 bp · B EV +0.49 (adj +0.28) on $8.94, P(profit) 0.7764, adj growth 2.7 bp · C EV +0.67 (adj +0.39) on $12.27, P(profit) 0.7764, adj growth 3.6 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.7764, adj growth 2.0 bp

## WPG @ DAL  ·  10000 joint draws  ·  506 bet sides mapped, 5 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.638 / away 0.362

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_WPG_win | p_overtime | goals | shots DAL/WPG | DAL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.63 | 0.37 | 0.00 | 5.96 | 26.0/25.7 | 22.8/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.47 | 5.8 | 26.2/25.9 | 22.7/22.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.098 | 0.68 | 0.32 | 0.00 | 5.93 | 30.8/20.2 | 17.7/26.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.59 | 0.41 | 0.46 | 5.87 | 31.2/20.7 | 17.8/27.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.59 | 0.41 | 0.00 | 9.2 | 27.3/27.1 | 21.8/20.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.53 | 0.47 | 0.46 | 2.8 | 24.3/24.4 | 22.9/22.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Gabriel Vilardi: 1+ goals YES | 21 | 0.265 | 0.248 | +0.043 | +0.027 | $2.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 71 | 0.776 | 0.740 | +0.051 | +0.016 | $3.33 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mikko Rantanen: 1+ goals NO | 67 | 0.717 | 0.702 | +0.032 | +0.016 | $4.37 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: higher confidence-adjusted growth (8.99 vs 2.78 bp); despite a smaller raw edge (+0.043 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.141); KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: WPG offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL2|no; why: higher confidence-adjusted growth (2.78 vs 1.02 bp); wins across more scripts (relative breadth 0.983 vs 0.864); relationships: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.141); KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: REINFORCING (phi 0.159); failure: DAL wins by 2+
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no has the higher standalone adjusted growth (2.78 vs 2.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.159); they share one thesis budget; relationships: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: REINFORCING (phi 0.159); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.2894): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4478): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- thesis DAL:SUPPRESSED (p 0.3754): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4926, phi -0.265)
- KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3404, phi -0.749)
- KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4015, phi -0.227)

portfolios: A EV +1.66 (adj +0.60) on $13.81, P(profit) 0.4425, adj growth 5.5 bp · B EV +0.96 (adj +0.50) on $10.42, P(profit) 0.6814, adj growth 4.8 bp · C EV +1.16 (adj +0.59) on $9.81, P(profit) 0.2645, adj growth 5.5 bp · R EV +0.16 (adj +0.07) on $3.00, P(profit) 0.586, adj growth 2.6 bp

## MIN @ CGY  ·  10000 joint draws  ·  434 bet sides mapped, 9 +EV candidates, 4 on card

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
| Kirill Kaprizov: 1+ goals NO | 53 | 0.613 | 0.591 | +0.065 | +0.043 | $7.17 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Minnesota wins by over 1.5 goals NO | 59 | 0.680 | 0.633 | +0.073 | +0.026 | $3.06 | FUNDED_RESEARCH | $1 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jonathan Castagna: 1+ goals YES | 10 | 0.135 | 0.120 | +0.029 | +0.014 | $1.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 17 | 0.206 | 0.195 | +0.026 | +0.015 | $1.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN2|no; why: higher confidence-adjusted growth (16.62 vs 6.11 bp); despite a smaller raw edge (+0.065 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.991 vs 0.887); relationships: KXNHLSPREAD-26OCT22MINCGY-MIN2|no: REINFORCING (phi 0.254); KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: MIN offense succeeds (4+ goals)
- **Minnesota wins by over 1.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no has the higher standalone adjusted growth (16.62 vs 6.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.254); they share one thesis budget; relationships: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: REINFORCING (phi 0.254); KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.119); KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.124); failure: MIN wins by 2+
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22MINCGY-MIN2|no has the higher standalone adjusted growth (6.11 vs 4.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.119); they share one thesis budget; relationships: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT22MINCGY-MIN2|no: MOSTLY_INDEPENDENT (phi 0.119); KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CGY offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22MINCGY-MIN2|no has the higher standalone adjusted growth (6.11 vs 3.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.124); they share one thesis budget; relationships: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT22MINCGY-MIN2|no: MOSTLY_INDEPENDENT (phi 0.124); KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.3746): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.4524): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.335): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3955, phi -0.308)
- KXNHLSPREAD-26OCT22MINCGY-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3196, phi -1.0)
- KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.446, phi -0.187)
- KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.446, phi -0.218)

portfolios: A EV +1.47 (adj +0.59) on $13.81, P(profit) 0.6337, adj growth 5.6 bp · B EV +1.72 (adj +0.95) on $12.71, P(profit) 0.6514, adj growth 9.1 bp · C EV +1.85 (adj +1.02) on $15.40, P(profit) 0.6127, adj growth 9.6 bp · R EV +0.36 (adj +0.20) on $3.00, P(profit) 0.6127, adj growth 7.7 bp

## CAR @ EDM  ·  10000 joint draws  ·  416 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.481 / away 0.519

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CAR_win | p_overtime | goals | shots EDM/CAR | EDM/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.60 | 0.40 | 0.00 | 6.05 | 27.2/27.9 | 24.8/23.2 | even strength |
| CAR shot control · normal event (5-7) · decided (2+) | 0.110 | 0.55 | 0.45 | 0.00 | 6.03 | 21.8/33.5 | 30.1/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.63 | 0.37 | 0.00 | 9.49 | 28.9/29.4 | 24.0/21.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.54 | 0.46 | 0.47 | 6.0 | 27.4/28.1 | 24.8/24.2 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.46 | 5.97 | 22.0/33.7 | 30.4/18.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.088 | 0.54 | 0.46 | 0.00 | 9.34 | 23.3/35.0 | 28.8/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vasily Podkolzin: 1+ goals YES | 25 | 0.310 | 0.294 | +0.047 | +0.030 | $3.41 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 8 | 0.119 | 0.103 | +0.034 | +0.018 | $1.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 15 | 0.183 | 0.172 | +0.024 | +0.013 | $1.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 80 | 0.855 | 0.825 | +0.044 | +0.014 | $4.35 | FUNDED_RESEARCH | $2 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes; why: higher confidence-adjusted growth (10.39 vs 4.39 bp); despite a smaller raw edge (+0.047 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.895 vs 0.749); relationships: KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.129); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (10.39 vs 9.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.083); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (10.39 vs 2.95 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.086); failure: EDM offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes; why: Broad expression KXNHLSPREAD-26OCT22CAREDM-CAR3|no selected over player prop KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.129); KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.086); failure: CAR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CAR shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4827): highest fidelity KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS_BY_2PLUS (p 0.3474): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS (p 0.5634): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3036, phi -0.227)
- KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3036, phi -0.136)
- KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3036, phi -0.173)
- KXNHLSPREAD-26OCT22CAREDM-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2361, phi -0.74)
- override: Broad expression KXNHLSPREAD-26OCT22CAREDM-CAR3|no selected over player prop KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.72 (adj +0.45) on $13.81, P(profit) 0.5908, adj growth 4.2 bp · B EV +1.63 (adj +0.89) on $10.51, P(profit) 0.4922, adj growth 8.5 bp · C EV +1.79 (adj +0.86) on $15.44, P(profit) 0.432, adj growth 8.1 bp · R EV +0.29 (adj +0.15) on $3.00, P(profit) 0.3098, adj growth 5.7 bp

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
| Shane Wright: 1+ goals YES | 14 | 0.201 | 0.184 | +0.052 | +0.036 | $3.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 11 | 0.148 | 0.138 | +0.032 | +0.021 | $2.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 64 | 0.702 | 0.684 | +0.046 | +0.028 | $6.46 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Utah wins by over 1.5 goals NO | 61 | 0.705 | 0.655 | +0.078 | +0.028 | $6.05 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: higher confidence-adjusted growth (21.91 vs 8.66 bp); despite a smaller raw edge (+0.052 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22UTASEA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT22UTASEA-UTA2|no: MOSTLY_INDEPENDENT (phi 0.136); failure: SEA offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22UTASEA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (8.92 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT22UTASEA-UTA2|no: INTENTIONAL_DIVERSIFIER (phi -0.162); failure: UTA offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: KXNHLSPREAD-26OCT22UTASEA-UTA3|no has the higher standalone adjusted growth (8.66 vs 7.61 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.138); relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT22UTASEA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT22UTASEA-UTA2|no: REINFORCING (phi 0.158); failure: UTA offense succeeds (4+ goals)
- **Utah wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: KXNHLSPREAD-26OCT22UTASEA-UTA3|no has the higher standalone adjusted growth (8.66 vs 7.51 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.731); relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.136); KXNHLGOAL-26OCT22UTASEA-UTAJMCBAIN22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.162); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: REINFORCING (phi 0.158); failure: UTA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, UTA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:OFFENSE_4PLUS (p 0.4116): highest fidelity KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4936): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- thesis UTA:SUPPRESSED (p 0.3693): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3742, phi -0.206)
- KXNHLGOAL-26OCT22UTASEA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3693, phi -0.18)
- KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4158, phi -0.23)
- KXNHLSPREAD-26OCT22UTASEA-UTA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2951, phi -1.0)

portfolios: A EV +2.82 (adj +0.54) on $13.81, P(profit) 0.603, adj growth 4.8 bp · B EV +2.94 (adj +1.72) on $17.92, P(profit) 0.6832, adj growth 16.3 bp · C EV +2.58 (adj +1.47) on $14.40, P(profit) 0.2009, adj growth 13.7 bp · R EV +0.39 (adj +0.18) on $4.00, P(profit) 0.5278, adj growth 6.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22UTASEA-UTA|no == KXNHLGAME-26OCT22UTASEA-SEA|yes

## DET @ VAN  ·  10000 joint draws  ·  358 bet sides mapped, 16 +EV candidates, 4 on card

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
| Liam Ohgren: 1+ goals YES | 11 | 0.177 | 0.155 | +0.060 | +0.038 | $3.36 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ goals YES | 19 | 0.270 | 0.247 | +0.069 | +0.047 | $4.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 12 | 0.165 | 0.151 | +0.037 | +0.024 | $2.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Detroit over 5.5 goals scored NO | 87 | 0.920 | 0.892 | +0.042 | +0.014 | $7.17 | FUNDED_RESEARCH | $2 | VAN:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes; why: higher confidence-adjusted growth (30.36 vs 29.08 bp); despite a smaller raw edge (+0.060 vs +0.069/contract); relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no: MOSTLY_INDEPENDENT (phi -0.005); failure: VAN offense suppressed (<= 2 goals)
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: higher confidence-adjusted growth (29.08 vs 9.48 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.954 vs 0.458); relationships: KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no: MOSTLY_INDEPENDENT (phi 0.018); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (29.08 vs 10.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no: MOSTLY_INDEPENDENT (phi 0.012); failure: VAN offense suppressed (<= 2 goals)
- **Detroit over 5.5 goals scored NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no selected over broad KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.47 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: high-event game (8+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4129): highest fidelity KXNHLTEAMTOTAL-26OCT22DETVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5383): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.3098): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-DET2|no (same contract)
- KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3706, phi -0.186)
- KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3706, phi -0.246)
- KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3706, phi -0.177)
- KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2641, phi -0.425)
- override: Broad expression KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no selected over broad KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.47 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.81 (adj +1.11) on $13.81, P(profit) 0.6788, adj growth 10.6 bp · B EV +4.36 (adj +2.74) on $17.50, P(profit) 0.4932, adj growth 26.0 bp · C EV +2.97 (adj +1.77) on $8.18, P(profit) 0.3836, adj growth 16.5 bp · R EV +0.61 (adj +0.36) on $3.00, P(profit) 0.1771, adj growth 13.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
