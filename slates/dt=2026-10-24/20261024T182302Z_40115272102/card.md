# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T18:23:02Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.37 | +10.12 | +24.85 | 0.746 | -22.15 | -33.87 | 93.87 |
| B thesis-diversified (joint) ← optimiser card | 148.04 | +22.97 | +11.17 | +21.96 | 0.738 | -20.36 | -31.36 | 105.55 |
| C best expression per thesis | 150.00 | +26.25 | +11.29 | +24.78 | 0.717 | -27.83 | -42.28 | 103.41 |
| R FUNDED research stakes | 23.00 | +2.53 | +1.52 | +1.94 | 0.581 | -6.44 | -8.72 | 0.00 |

## LAK @ NJD  ·  10000 joint draws  ·  410 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.631 / away 0.369

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_LAK_win | p_overtime | goals | shots NJD/LAK | NJD/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.58 | 0.42 | 0.00 | 6.0 | 28.4/27.9 | 24.7/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.48 | 0.52 | 0.49 | 5.86 | 28.5/28.1 | 24.9/25.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.112 | 0.62 | 0.38 | 0.00 | 6.01 | 33.8/22.2 | 19.3/29.4 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.54 | 0.46 | 0.50 | 5.91 | 34.0/22.5 | 19.3/30.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.064 | 0.54 | 0.46 | 0.00 | 9.09 | 30.4/29.6 | 24.0/24.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.54 | 0.46 | 0.00 | 3.42 | 27.4/26.8 | 25.2/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Luke Evangelista: 1+ assists NO | 61 | 0.790 | 0.663 | +0.164 | +0.037 | $6.37 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Timo Meier: 1+ goals NO | 73 | 0.789 | 0.773 | +0.046 | +0.030 | $6.37 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 2.5 goals NO | 73 | 0.796 | 0.761 | +0.052 | +0.017 | $4.35 | FUNDED_RESEARCH | $2 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Alex Laferriere: 1+ goals YES | 24 | 0.277 | 0.265 | +0.024 | +0.012 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no; why: higher confidence-adjusted growth (12.66 vs 10.13 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no: REINFORCING (phi 0.226); KXNHLSPREAD-26OCT24LANJ-NJ3|no: REINFORCING (phi 0.16); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: NJD offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no has the higher standalone adjusted growth (12.66 vs 10.13 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.226); they share one thesis budget; relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.226); KXNHLSPREAD-26OCT24LANJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins by over 2.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT24LANJ-NJ2|no; why: KXNHLTEAMTOTAL-26OCT24LANJ-NJ2|no has the higher standalone adjusted growth (3.94 vs 3.28 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.247); relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.16); KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.136); failure: NJD wins by 2+
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24LANJ-NJ3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24LANJ-NJ3|no has the higher standalone adjusted growth (3.28 vs 1.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.136); they share one thesis budget; relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT24LANJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.136); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.11.
- thesis NJD:SUPPRESSED (p 0.4092): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS (p 0.4551): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT24LANJ-NJLEVANGELISTA77-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.303): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT24LANJ-NJ3|no (same contract)
- KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.5 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3736, phi -0.219)
- KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3736, phi -0.196)
- KXNHLSPREAD-26OCT24LANJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.32, phi -0.737)
- KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.474, phi -0.251)

portfolios: A EV +2.60 (adj +0.52) on $14.80, P(profit) 0.7185, adj growth 4.9 bp · B EV +2.48 (adj +0.79) on $18.37, P(profit) 0.7179, adj growth 7.6 bp · C EV +4.38 (adj +1.09) on $22.11, P(profit) 0.6555, adj growth 10.2 bp · R EV +0.26 (adj +0.12) on $4.00, P(profit) 0.6527, adj growth 4.8 bp

## SJS @ BOS  ·  10000 joint draws  ·  514 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.624 / away 0.376

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_SJS_win | p_overtime | goals | shots BOS/SJS | BOS/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.67 | 0.33 | 0.00 | 6.07 | 27.8/27.8 | 24.9/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.46 | 6.0 | 27.6/27.7 | 24.5/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.66 | 0.34 | 0.00 | 9.42 | 29.2/29.2 | 24.0/22.0 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.080 | 0.68 | 0.32 | 0.00 | 6.04 | 32.3/22.0 | 19.3/27.8 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.55 | 0.45 | 0.48 | 5.97 | 32.9/22.2 | 18.9/29.3 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.061 | 0.74 | 0.26 | 0.00 | 9.21 | 34.3/23.6 | 19.3/26.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tanner Jeannot: 1+ goals YES | 9 | 0.116 | 0.108 | +0.020 | +0.013 | $1.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 67 | 0.738 | 0.699 | +0.052 | +0.013 | $4.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| David Pastrnak: 1+ goals NO | 60 | 0.641 | 0.630 | +0.025 | +0.013 | $3.07 | FUNDED_RESEARCH | $1 | BOS:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 71 | 0.770 | 0.735 | +0.046 | +0.011 | $4.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Tanner Jeannot: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (3.91 vs 0.19 bp); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: BOS offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no; why: higher confidence-adjusted growth (1.82 vs 1.58 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: REINFORCING (phi 0.152); KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: BOS offense succeeds (4+ goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no has the higher standalone adjusted growth (1.82 vs 1.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.152); they share one thesis budget; relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no: REINFORCING (phi 0.152); KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: BOS offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24SJBOS-SJMCELEBRINI71-2|no; why: higher confidence-adjusted growth (1.27 vs 0.07 bp); alternative not eligible: confidence-adjusted EV +0.0019 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:SUPPRESSED (p 0.3089): highest fidelity KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no (same contract)
- thesis SJS:SUPPRESSED (p 0.4392): highest fidelity KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.4872): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3089, phi -0.129)
- KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4872, phi -0.229)
- KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4872, phi -0.251)
- KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3412, phi -0.225)

portfolios: A EV +1.11 (adj +0.42) on $14.80, P(profit) 0.456, adj growth 4.0 bp · B EV +1.03 (adj +0.40) on $13.36, P(profit) 0.459, adj growth 3.8 bp · C EV +1.01 (adj +0.25) on $14.44, P(profit) 0.5682, adj growth 2.3 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6415, adj growth 0.8 bp

## NYR @ OTT  ·  10000 joint draws  ·  444 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.532 / away 0.468

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYR_win | p_overtime | goals | shots OTT/NYR | OTT/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.126 | 0.62 | 0.38 | 0.00 | 5.98 | 32.4/20.8 | 17.9/28.1 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.53 | 0.47 | 0.45 | 5.92 | 32.7/21.1 | 17.9/29.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.54 | 0.46 | 0.00 | 5.99 | 26.9/26.2 | 22.8/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.47 | 5.91 | 27.1/26.6 | 23.4/23.8 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.076 | 0.63 | 0.37 | 0.00 | 9.28 | 34.1/22.4 | 17.3/26.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.54 | 0.46 | 0.00 | 9.24 | 28.6/27.8 | 22.1/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Taylor Raddysh: 1+ goals YES | 8 | 0.120 | 0.106 | +0.034 | +0.021 | $2.11 | FUNDED_RESEARCH | $1 | NYR:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 58 | 0.713 | 0.620 | +0.116 | +0.023 | $7.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Nick Cousins: 1+ goals YES | 8 | 0.108 | 0.096 | +0.023 | +0.011 | $1.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 14 | 0.170 | 0.160 | +0.021 | +0.011 | $1.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (11.84 vs 1.45 bp); relationships: KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT24NYROTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: NYR offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24NYROTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (4.80 vs 0.18 bp); alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT24NYROTT-OTTMAMADIO22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.067); failure: OTT offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24NYROTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (3.44 vs 0.17 bp); despite a smaller raw edge (+0.023 vs +0.071/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT24NYROTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24NYROTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (2.21 vs 0.17 bp); despite a smaller raw edge (+0.021 vs +0.071/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.067); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:SUPPRESSED (p 0.3708): highest fidelity KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.3446): highest fidelity KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4115): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4331, phi -0.162)
- KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4115, phi -0.237)
- KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3708, phi -0.134)
- KXNHLGOAL-26OCT24NYROTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3708, phi -0.187)

portfolios: A EV +2.84 (adj +1.14) on $14.80, P(profit) 0.7796, adj growth 10.7 bp · B EV +2.80 (adj +1.07) on $12.02, P(profit) 0.7796, adj growth 10.0 bp · C EV +2.21 (adj +0.50) on $12.61, P(profit) 0.7129, adj growth 4.6 bp · R EV +0.40 (adj +0.24) on $1.00, P(profit) 0.1196, adj growth 8.6 bp

## NSH @ PIT  ·  10000 joint draws  ·  402 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.532 / away 0.468

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_NSH_win | p_overtime | goals | shots PIT/NSH | PIT/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.62 | 0.38 | 0.00 | 6.06 | 27.9/27.6 | 24.5/23.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.109 | 0.66 | 0.34 | 0.00 | 6.01 | 33.5/21.9 | 19.2/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.59 | 0.41 | 0.00 | 9.41 | 29.5/29.2 | 23.4/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.52 | 0.48 | 0.45 | 5.94 | 27.6/27.2 | 24.1/24.3 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.46 | 0.47 | 5.95 | 33.2/22.1 | 19.0/29.7 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.077 | 0.70 | 0.30 | 0.00 | 9.38 | 35.1/23.4 | 18.7/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 15 | 0.205 | 0.189 | +0.046 | +0.030 | $3.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 34 | 0.412 | 0.393 | +0.057 | +0.037 | $5.95 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 12 | 0.158 | 0.144 | +0.031 | +0.016 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ goals YES | 34 | 0.379 | 0.367 | +0.023 | +0.011 | $1.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (14.09 vs 13.29 bp); despite a smaller raw edge (+0.046 vs +0.057/contract); relationships: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (14.09 vs 13.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (14.09 vs 5.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.027); they share one thesis budget; relationships: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (14.09 vs 1.13 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4828): highest fidelity KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes (same contract)
- KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.212)
- KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 46% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.266)
- KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.186)
- KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.266)

portfolios: A EV +2.83 (adj +1.74) on $14.80, P(profit) 0.6035, adj growth 16.2 bp · B EV +2.44 (adj +1.52) on $12.64, P(profit) 0.6035, adj growth 14.3 bp · C EV +1.53 (adj +0.99) on $5.32, P(profit) 0.2047, adj growth 9.0 bp · R EV +0.32 (adj +0.21) on $2.00, P(profit) 0.4125, adj growth 7.8 bp

## BUF @ WSH  ·  10000 joint draws  ·  466 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_BUF_win | p_overtime | goals | shots WSH/BUF | WSH/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.59 | 0.41 | 0.00 | 5.99 | 27.5/27.7 | 24.6/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.47 | 6.0 | 27.6/27.6 | 24.3/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.56 | 0.44 | 0.00 | 9.42 | 29.1/29.3 | 23.2/22.6 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.079 | 0.48 | 0.52 | 0.00 | 6.04 | 22.0/32.8 | 29.0/18.5 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.48 | 0.52 | 0.48 | 5.96 | 22.1/33.1 | 29.6/19.0 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.058 | 0.61 | 0.39 | 0.00 | 6.02 | 32.4/22.2 | 19.2/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.240 | 0.222 | +0.061 | +0.042 | $4.89 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 15 | 0.197 | 0.179 | +0.038 | +0.020 | $2.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 25 | 0.365 | 0.287 | +0.102 | +0.024 | $2.35 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Rasmus Dahlin: 1+ assists NO | 52 | 0.608 | 0.561 | +0.070 | +0.024 | $5.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (25.31 vs 6.48 bp); despite a smaller raw edge (+0.061 vs +0.102/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (25.31 vs 6.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.144); KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: WSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (25.31 vs 6.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.039); they share one thesis budget; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLGOAL-26OCT24BUFWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.144); KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: WSH offense suppressed (<= 2 goals)
- **Rasmus Dahlin: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no; why: higher confidence-adjusted growth (5.08 vs 2.42 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24BUFWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4409): highest fidelity KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3956): highest fidelity KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.3883): highest fidelity KXNHLGOAL-26OCT24BUFWSH-BUFJZUCKER17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24BUFWSH-BUFJZUCKER17-1|yes (same contract)
- KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3477, phi -0.227)
- KXNHLGOAL-26OCT24BUFWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3477, phi -0.18)
- KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3477, phi -0.279)
- KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3883, phi -0.276)

portfolios: A EV +4.10 (adj +1.79) on $14.80, P(profit) 0.5848, adj growth 16.8 bp · B EV +3.77 (adj +1.85) on $14.75, P(profit) 0.4809, adj growth 17.5 bp · C EV +4.03 (adj +2.32) on $19.65, P(profit) 0.3299, adj growth 21.1 bp · R EV +0.67 (adj +0.46) on $2.00, P(profit) 0.2405, adj growth 16.8 bp

## VGK @ CBJ  ·  10000 joint draws  ·  432 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.447 / away 0.553

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_VGK_win | p_overtime | goals | shots CBJ/VGK | CBJ/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.47 | 0.53 | 0.00 | 6.01 | 27.3/27.4 | 23.8/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.47 | 0.53 | 0.48 | 5.96 | 27.6/27.4 | 24.0/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.43 | 0.57 | 0.00 | 9.26 | 29.2/29.2 | 22.7/23.2 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.071 | 0.38 | 0.62 | 0.00 | 5.99 | 21.6/32.2 | 27.9/18.8 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.065 | 0.53 | 0.47 | 0.00 | 5.95 | 32.3/21.8 | 18.6/28.5 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.52 | 0.48 | 0.48 | 5.89 | 32.3/22.0 | 18.8/28.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 22 | 0.260 | 0.249 | +0.028 | +0.017 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Trevor Connelly: 1+ goals NO | 77 | 0.803 | 0.793 | +0.020 | +0.011 | $5.49 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (3.39 vs 1.18 bp); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24VGKCBJ-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: CBJ offense suppressed (<= 2 goals)
- **Trevor Connelly: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24VGKCBJ-VGKMSTONE61-1|no; why: higher confidence-adjusted growth (1.55 vs 0.25 bp); despite a smaller raw edge (+0.020 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.346): highest fidelity KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.386): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4353, phi -0.253)
- KXNHLGOAL-26OCT24VGKCBJ-VGKTCONNELLY24-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.396, phi -0.182)

portfolios: A EV +0.48 (adj +0.28) on $8.61, P(profit) 0.2599, adj growth 2.6 bp · B EV +0.41 (adj +0.24) on $7.71, P(profit) 0.2599, adj growth 2.2 bp · C EV +0.41 (adj +0.25) on $3.43, P(profit) 0.2599, adj growth 2.3 bp · R EV +0.05 (adj +0.03) on $2.00, P(profit) 0.8028, adj growth 1.0 bp

## CAR @ STL  ·  10000 joint draws  ·  424 bet sides mapped, 15 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.418 / away 0.582

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_CAR_win | p_overtime | goals | shots STL/CAR | STL/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.136 | 0.51 | 0.49 | 0.00 | 6.07 | 21.3/33.2 | 29.4/17.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.50 | 0.50 | 0.49 | 5.92 | 21.2/33.4 | 30.1/18.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.58 | 0.42 | 0.00 | 6.04 | 26.4/27.0 | 23.9/22.4 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.102 | 0.49 | 0.51 | 0.00 | 9.28 | 22.5/34.6 | 27.9/16.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.51 | 0.49 | 0.45 | 5.97 | 26.6/27.3 | 23.9/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.57 | 0.43 | 0.00 | 9.32 | 27.9/28.9 | 23.1/21.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 22 | 0.282 | 0.261 | +0.051 | +0.029 | $3.33 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 65 | 0.741 | 0.693 | +0.075 | +0.027 | $6.23 | FUNDED_RESEARCH | $2 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jimmy Snuggerud: 1+ goals YES | 28 | 0.331 | 0.316 | +0.037 | +0.022 | $2.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24CARSTL-CAR2|no; why: higher confidence-adjusted growth (9.95 vs 7.11 bp); despite a smaller raw edge (+0.051 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT24CARSTL-CAR2|no: REINFORCING (phi 0.158); KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: STL offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (9.95 vs 7.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.158); they share one thesis budget; relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: REINFORCING (phi 0.158); KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: REINFORCING (phi 0.178); failure: CAR wins by 2+
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (9.95 vs 4.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLSPREAD-26OCT24CARSTL-CAR2|no: REINFORCING (phi 0.178); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4291): highest fidelity KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.5285): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS_BY_2PLUS (p 0.3069): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.248)
- KXNHLSPREAD-26OCT24CARSTL-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2595, phi -1.0)
- KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.272)

portfolios: A EV +2.85 (adj +0.88) on $14.80, P(profit) 0.4741, adj growth 8.0 bp · B EV +1.76 (adj +0.86) on $12.23, P(profit) 0.4753, adj growth 8.1 bp · C EV +2.44 (adj +1.11) on $17.08, P(profit) 0.7826, adj growth 10.1 bp · R EV +0.22 (adj +0.08) on $2.00, P(profit) 0.7405, adj growth 3.1 bp

## TOR @ EDM  ·  10000 joint draws  ·  476 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.611 / away 0.389

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_TOR_win | p_overtime | goals | shots EDM/TOR | EDM/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.129 | 0.73 | 0.27 | 0.00 | 6.08 | 35.4/22.9 | 20.4/30.3 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.125 | 0.73 | 0.27 | 0.00 | 9.48 | 37.0/24.1 | 19.6/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.68 | 0.32 | 0.00 | 6.05 | 29.3/28.7 | 25.9/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.69 | 0.31 | 0.00 | 9.58 | 31.4/30.5 | 25.1/23.6 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.57 | 0.43 | 0.45 | 5.99 | 35.4/23.0 | 19.8/31.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.46 | 0.47 | 6.0 | 29.8/29.2 | 25.9/26.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.151 | 0.137 | +0.035 | +0.020 | $2.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 81 | 0.855 | 0.842 | +0.034 | +0.021 | $8.49 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Leon Draisaitl: 1+ assists NO | 37 | 0.485 | 0.407 | +0.099 | +0.021 | $4.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.75) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 27 | 0.312 | 0.301 | +0.029 | +0.017 | $3.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24TOREDM-TORTSTECHER28-1|yes; why: higher confidence-adjusted growth (8.71 vs 0.00 bp); despite a smaller raw edge (+0.035 vs +0.065/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24TOREDM-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (6.95 vs 1.15 bp); despite a smaller raw edge (+0.034 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: TOR offense succeeds (4+ goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT24TOREDM-4|no; why: higher confidence-adjusted growth (4.00 vs 1.05 bp); wins across more scripts (relative breadth 1.077 vs 0.382); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT24TOREDM-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.22); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (3.04 vs 2.64 bp); despite a smaller raw edge (+0.029 vs +0.086/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24TOREDM-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.22); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, EDM shot control · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3474): highest fidelity KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.25): highest fidelity KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.5538): highest fidelity KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4321, phi -0.21)
- KXNHLGOAL-26OCT24TOREDM-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3474, phi -0.188)
- KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5538, phi -0.303)
- KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.25, phi -0.233)

portfolios: A EV +2.72 (adj +0.55) on $14.80, P(profit) 0.5448, adj growth 5.1 bp · B EV +2.40 (adj +1.02) on $17.99, P(profit) 0.6691, adj growth 9.7 bp · C EV +3.64 (adj +1.33) on $19.76, P(profit) 0.5638, adj growth 12.2 bp · R EV +0.12 (adj +0.08) on $3.00, P(profit) 0.8547, adj growth 3.0 bp

## TBL @ UTA  ·  10000 joint draws  ·  428 bet sides mapped, 4 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.564 / away 0.436

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TBL_win | p_overtime | goals | shots UTA/TBL | UTA/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.61 | 0.39 | 0.00 | 6.01 | 27.0/26.9 | 23.9/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.49 | 5.96 | 26.9/26.9 | 23.7/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.63 | 0.37 | 0.00 | 9.29 | 28.5/28.6 | 23.3/21.6 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.077 | 0.69 | 0.31 | 0.00 | 5.98 | 31.2/20.9 | 18.3/26.5 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.067 | 0.55 | 0.45 | 0.00 | 5.99 | 21.4/31.8 | 28.4/17.9 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.48 | 0.52 | 0.45 | 5.91 | 21.5/31.6 | 28.1/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack McBain: 1+ goals YES | 12 | 0.154 | 0.142 | +0.027 | +0.014 | $1.60 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Anthony Cirelli: 1+ goals YES | 18 | 0.217 | 0.206 | +0.027 | +0.016 | $2.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 19 | 0.227 | 0.214 | +0.026 | +0.013 | $1.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (4.05 vs 2.34 bp); relationships: KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: UTA offense suppressed (<= 2 goals)
- **Anthony Cirelli: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24TBUTA-TBACIRELLI71-1|yes; why: higher confidence-adjusted growth (3.65 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.034/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: TBL offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes has the higher standalone adjusted growth (4.05 vs 2.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis UTA:OFFENSE_4PLUS (p 0.453): highest fidelity KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:OFFENSE_4PLUS (p 0.3432): highest fidelity KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes (same contract)
- KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3374, phi -0.179)
- KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.439, phi -0.233)
- KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3374, phi -0.21)

portfolios: A EV +1.60 (adj +0.96) on $8.19, P(profit) 0.5138, adj growth 8.9 bp · B EV +0.84 (adj +0.47) on $5.35, P(profit) 0.4905, adj growth 4.4 bp · C EV +0.96 (adj +0.55) on $5.60, P(profit) 0.3375, adj growth 5.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ CGY  ·  10000 joint draws  ·  444 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.459 / away 0.541

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_DET_win | p_overtime | goals | shots CGY/DET | CGY/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.53 | 0.47 | 0.00 | 5.98 | 28.1/28.4 | 25.0/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.45 | 5.87 | 28.6/28.7 | 25.6/25.3 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.087 | 0.46 | 0.54 | 0.00 | 5.95 | 22.8/34.1 | 30.3/19.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.46 | 0.54 | 0.47 | 5.87 | 22.7/34.2 | 30.7/19.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.50 | 0.50 | 0.00 | 9.22 | 30.2/30.6 | 24.5/23.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.54 | 0.46 | 0.00 | 3.49 | 27.4/27.7 | 25.8/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jonathan Castagna: 1+ goals YES | 10 | 0.149 | 0.127 | +0.043 | +0.021 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 10 | 0.129 | 0.120 | +0.023 | +0.014 | $1.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Justin Faulk: 1+ goals NO | 89 | 0.915 | 0.908 | +0.018 | +0.011 | $8.17 | FUNDED_RESEARCH | $3 | DET:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Lucas Raymond: 1+ goals NO | 72 | 0.758 | 0.746 | +0.024 | +0.012 | $4.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24DETCGY-DET3|no; why: higher confidence-adjusted growth (9.58 vs 0.68 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: CGY offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes has the higher standalone adjusted growth (9.58 vs 4.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CGY offense suppressed (<= 2 goals)
- **Justin Faulk: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no; why: higher confidence-adjusted growth (2.79 vs 2.20 bp); despite a smaller raw edge (+0.018 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.995 vs 0.884); relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: DET offense succeeds (4+ goals)
- **Lucas Raymond: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no; why: Player prop expression KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no selected over broad KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.88 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:OFFENSE_4PLUS (p 0.3555): highest fidelity KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4323): highest fidelity KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no (same contract)
- KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.186)
- KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.174)
- KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3499, phi -0.123)
- KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3499, phi -0.235)
- override: Player prop expression KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no selected over broad KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.88 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.20 (adj +1.02) on $14.80, P(profit) 0.6477, adj growth 9.4 bp · B EV +1.49 (adj +0.79) on $16.39, P(profit) 0.2587, adj growth 7.4 bp · C EV +1.79 (adj +0.76) on $8.94, P(profit) 0.686, adj growth 6.9 bp · R EV +0.06 (adj +0.04) on $3.00, P(profit) 0.9152, adj growth 1.4 bp

## MIN @ SEA  ·  10000 joint draws  ·  406 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.411 / away 0.589

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_MIN_win | p_overtime | goals | shots SEA/MIN | SEA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.54 | 0.46 | 0.00 | 6.0 | 28.4/28.9 | 25.5/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.52 | 0.48 | 0.47 | 5.98 | 28.7/29.0 | 25.7/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.57 | 0.43 | 0.00 | 9.21 | 30.1/30.3 | 24.5/23.7 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.089 | 0.53 | 0.47 | 0.00 | 5.97 | 22.7/34.3 | 30.8/19.2 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.48 | 0.52 | 0.45 | 5.89 | 22.7/34.2 | 30.8/19.5 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.060 | 0.48 | 0.52 | 0.00 | 9.31 | 24.5/36.3 | 29.8/19.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kirill Kaprizov: 1+ goals NO | 54 | 0.625 | 0.602 | +0.067 | +0.045 | $8.49 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 10 | 0.145 | 0.130 | +0.039 | +0.024 | $2.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Mackie Samoskevich: 1+ goals YES | 18 | 0.239 | 0.218 | +0.049 | +0.028 | $3.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Shane Wright: 1+ goals YES | 16 | 0.212 | 0.194 | +0.043 | +0.025 | $2.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: higher confidence-adjusted growth (17.97 vs 9.69 bp); despite a smaller raw edge (+0.067 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.998 vs 0.536); relationships: KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: MIN offense succeeds (4+ goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes; why: higher confidence-adjusted growth (13.04 vs 10.78 bp); despite a smaller raw edge (+0.039 vs +0.049/contract); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: SEA offense suppressed (<= 2 goals)
- **Mackie Samoskevich: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA2|yes; why: higher confidence-adjusted growth (10.78 vs 9.69 bp); despite a smaller raw edge (+0.049 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.902 vs 0.536); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: SEA offense suppressed (<= 2 goals)
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes has the higher standalone adjusted growth (10.78 vs 9.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.41): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.531): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.4111): highest fidelity KXNHLTEAMTOTAL-26OCT24MINSEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-SEA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3649, phi -0.296)
- KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3646, phi -0.169)
- KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3646, phi -0.22)
- KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3646, phi -0.206)

portfolios: A EV +3.03 (adj +0.82) on $14.80, P(profit) 0.4865, adj growth 7.3 bp · B EV +3.54 (adj +2.16) on $17.23, P(profit) 0.4372, adj growth 20.5 bp · C EV +3.83 (adj +2.14) on $21.06, P(profit) 0.7127, adj growth 19.7 bp · R EV +0.36 (adj +0.24) on $3.00, P(profit) 0.6248, adj growth 9.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
