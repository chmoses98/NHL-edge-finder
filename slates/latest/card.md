# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-02T23:16:40Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +24.06 | +10.24 | +16.03 | 0.592 | -55.14 | -72.15 | 80.97 |
| B thesis-diversified (joint) ← optimiser card | 137.99 | +18.61 | +10.08 | +13.95 | 0.614 | -42.53 | -57.94 | 88.29 |
| C best expression per thesis | 89.09 | +12.05 | +5.82 | +9.75 | 0.605 | -34.60 | -40.04 | 51.37 |
| R FUNDED research stakes | 14.00 | +1.68 | +1.05 | +0.13 | 0.695 | -7.61 | -7.61 | 0.00 |

## VGK @ BOS  ·  10000 joint draws  ·  524 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.488 / away 0.512

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_VGK_win | p_overtime | goals | shots BOS/VGK | BOS/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.52 | 0.48 | 0.00 | 6.02 | 27.2/27.5 | 24.1/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.47 | 6.0 | 27.3/27.6 | 24.4/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.54 | 0.46 | 0.00 | 9.37 | 28.7/29.0 | 23.0/22.2 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.092 | 0.47 | 0.53 | 0.00 | 6.03 | 21.6/32.5 | 28.7/18.2 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.48 | 0.52 | 0.47 | 5.95 | 21.7/32.8 | 29.3/18.5 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.058 | 0.46 | 0.54 | 0.00 | 9.21 | 23.3/34.3 | 27.7/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 2+ assists NO | 84 | 0.907 | 0.871 | +0.058 | +0.022 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 5 | 0.077 | 0.067 | +0.024 | +0.013 | $3.02 | FUNDED_RESEARCH | $1 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Nikita Zadorov: 1+ goals YES | 4 | 0.059 | 0.053 | +0.016 | +0.010 | $2.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Casey Mittelstadt: 1+ goals YES | 15 | 0.185 | 0.175 | +0.026 | +0.016 | $4.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 2+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (8.16 vs 0.67 bp); despite a smaller raw edge (+0.058 vs +0.102/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26NOV02VGKBOS-BOSNZADOROV91-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV02VGKBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: VGK offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV02VGKBOS-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (7.32 vs 0.06 bp); despite a smaller raw edge (+0.024 vs +0.024/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0024 below the 0.010/contract floor; relationships: KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-2|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26NOV02VGKBOS-BOSNZADOROV91-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV02VGKBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: VGK offense suppressed (<= 2 goals)
- **Nikita Zadorov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02VGKBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (5.38 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-2|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV02VGKBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: BOS offense suppressed (<= 2 goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02VGKBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (4.35 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-2|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV02VGKBOS-BOSNZADOROV91-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.3869): highest fidelity KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-2|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.3987): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis BOS:OFFENSE_4PLUS (p 0.4201): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3987, phi -0.253)
- KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3869, phi -0.117)
- KXNHLGOAL-26NOV02VGKBOS-BOSNZADOROV91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3655, phi -0.105)
- KXNHLGOAL-26NOV02VGKBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3655, phi -0.188)

portfolios: A EV +4.92 (adj +2.62) on $31.20, P(profit) 0.3576, adj growth 21.4 bp · B EV +4.37 (adj +2.30) on $30.03, P(profit) 0.2768, adj growth 20.2 bp · C EV +1.36 (adj +0.51) on $20.00, P(profit) 0.9072, adj growth 4.9 bp · R EV +0.44 (adj +0.25) on $1.00, P(profit) 0.077, adj growth 8.0 bp

## DET @ FLA  ·  10000 joint draws  ·  418 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.620 / away 0.380

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_DET_win | p_overtime | goals | shots FLA/DET | FLA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 6.02 | 26.9/27.0 | 23.9/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.52 | 0.48 | 0.46 | 5.95 | 27.2/27.1 | 23.8/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.61 | 0.39 | 0.00 | 9.41 | 28.6/28.7 | 23.0/21.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.078 | 0.66 | 0.34 | 0.00 | 6.03 | 31.7/21.2 | 18.4/27.3 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.066 | 0.52 | 0.48 | 0.00 | 6.05 | 21.8/31.6 | 27.9/18.5 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.57 | 0.43 | 0.49 | 5.91 | 32.0/22.1 | 18.9/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex DeBrincat: 2+ goals YES | 6 | 0.091 | 0.082 | +0.027 | +0.018 | $4.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 63 | 0.700 | 0.681 | +0.053 | +0.035 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.126 | 0.116 | +0.030 | +0.020 | $5.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 35 | 0.399 | 0.385 | +0.033 | +0.019 | $2.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | DIRECT (0.60) | EVIDENCE_STRONGER | D |
- **Alex DeBrincat: 2+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes; why: higher confidence-adjusted growth (11.74 vs 9.44 bp); despite a smaller raw edge (+0.027 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.805 vs 0.542); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: DUPLICATIVE (phi 0.389); failure: DET offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02DETFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (11.59 vs 6.79 bp); despite a smaller raw edge (+0.053 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV02DETFLA-9|yes; why: higher confidence-adjusted growth (9.69 vs 2.96 bp); despite a smaller raw edge (+0.030 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.885 vs 0.368); relationships: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes; why: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.60 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes: DUPLICATIVE (phi 0.389); KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis DET:OFFENSE_4PLUS (p 0.3612): highest fidelity KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes (same contract)
- thesis FLA:SUPPRESSED (p 0.3456): highest fidelity KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no (same contract)
- thesis GAME:HIGH_EVENT (p 0.2844): highest fidelity KXNHLTOTAL-26NOV02DETFLA-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4281, phi -0.222)
- KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4446, phi -0.262)
- KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3456, phi -0.149)
- KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 40% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4281, phi -0.323)
- override: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.60 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +9.24 (adj +3.46) on $39.60, P(profit) 0.3715, adj growth 24.5 bp · B EV +5.20 (adj +3.41) on $32.04, P(profit) 0.397, adj growth 29.8 bp · C EV +5.16 (adj +2.84) on $29.09, P(profit) 0.7621, adj growth 24.9 bp · R EV +0.41 (adj +0.27) on $5.00, P(profit) 0.6997, adj growth 9.7 bp

## COL @ CHI  ·  10000 joint draws  ·  432 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.333 / away 0.667

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_COL_win | p_overtime | goals | shots CHI/COL | CHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.147 | 0.27 | 0.73 | 0.00 | 5.99 | 21.5/34.2 | 29.3/19.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.41 | 0.58 | 0.48 | 5.92 | 21.9/34.7 | 31.1/18.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.113 | 0.24 | 0.76 | 0.00 | 9.4 | 23.1/36.3 | 27.5/18.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.099 | 0.33 | 0.67 | 0.00 | 6.05 | 27.6/28.4 | 24.1/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.32 | 0.68 | 0.00 | 9.37 | 29.2/30.1 | 22.5/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.49 | 0.51 | 0.48 | 5.9 | 27.7/28.7 | 25.4/24.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.265 | 0.250 | +0.043 | +0.028 | $10.28 | FUNDED_RESEARCH | $3 | CHI:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Cole Smith: 1+ goals YES | 7 | 0.095 | 0.088 | +0.021 | +0.013 | $3.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 62 | 0.703 | 0.654 | +0.066 | +0.017 | $15.38 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Connor Bedard: 1+ assists NO | 54 | 0.623 | 0.574 | +0.065 | +0.016 | $12.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (9.95 vs 1.13 bp); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02COLCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.143); KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.16); failure: CHI offense suppressed (<= 2 goals)
- **Cole Smith: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (9.95 vs 5.27 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.032); KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.054); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (2.87 vs 2.39 bp); relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.143); KXNHLGOAL-26NOV02COLCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.109); failure: CHI offense succeeds (4+ goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no; why: second expression of the same thesis: KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no has the higher standalone adjusted growth (2.87 vs 2.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.109); they share one thesis budget; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.16); KXNHLGOAL-26NOV02COLCHI-CHICSMITH22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.054); KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.109); failure: CHI offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.313): highest fidelity KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.2906): highest fidelity KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no (same contract)
- thesis CHI:SUPPRESSED (p 0.4723): highest fidelity KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4723, phi -0.267)
- KXNHLGOAL-26NOV02COLCHI-CHICSMITH22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4723, phi -0.168)
- KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.313, phi -0.253)
- KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.313, phi -0.287)

portfolios: A EV +5.43 (adj +2.02) on $39.60, P(profit) 0.561, adj growth 17.9 bp · B EV +5.99 (adj +2.69) on $41.37, P(profit) 0.6844, adj growth 23.4 bp · C EV +4.75 (adj +2.00) on $33.77, P(profit) 0.5341, adj growth 17.5 bp · R EV +0.58 (adj +0.38) on $3.00, P(profit) 0.2647, adj growth 12.4 bp

## CGY @ SJS  ·  10000 joint draws  ·  464 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.530 / away 0.470

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_CGY_win | p_overtime | goals | shots SJS/CGY | SJS/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.57 | 0.43 | 0.00 | 6.02 | 28.7/28.5 | 25.3/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.43 | 5.97 | 28.5/28.6 | 25.3/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.60 | 0.40 | 0.00 | 9.31 | 30.3/30.2 | 24.4/23.4 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.075 | 0.65 | 0.35 | 0.00 | 6.03 | 33.7/22.8 | 20.0/28.9 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.52 | 0.48 | 0.45 | 5.93 | 33.7/22.6 | 19.5/30.2 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.062 | 0.53 | 0.47 | 0.00 | 6.0 | 23.1/34.1 | 30.5/19.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 1+ goals NO | 77 | 0.820 | 0.806 | +0.038 | +0.024 | $20.00 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 24 | 0.284 | 0.272 | +0.032 | +0.019 | $5.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Michael Misa: 1+ goals YES | 18 | 0.217 | 0.207 | +0.027 | +0.017 | $4.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Michael Misa: 1+ assists YES | 26 | 0.320 | 0.287 | +0.046 | +0.014 | $4.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02CGYSJ-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (7.52 vs 0.37 bp); despite a smaller raw edge (+0.038 vs +0.108/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.055); failure: SJS offense succeeds (4+ goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes; why: higher confidence-adjusted growth (4.25 vs 2.14 bp); despite a smaller raw edge (+0.032 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes: REINFORCING (phi 0.164); failure: SJS offense suppressed (<= 2 goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes has the higher standalone adjusted growth (4.25 vs 3.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: SJS offense suppressed (<= 2 goals)
- **Michael Misa: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes has the higher standalone adjusted growth (4.25 vs 2.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.164); they share one thesis budget; relationships: KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.055); KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: REINFORCING (phi 0.164); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4491): highest fidelity KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.3387): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4491, phi -0.182)
- KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3387, phi -0.231)
- KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3387, phi -0.209)
- KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3387, phi -0.231)

portfolios: A EV +4.47 (adj +2.14) on $39.60, P(profit) 0.5539, adj growth 17.1 bp · B EV +3.05 (adj +1.68) on $34.55, P(profit) 0.5208, adj growth 14.9 bp · C EV +0.78 (adj +0.47) on $6.23, P(profit) 0.2843, adj growth 4.1 bp · R EV +0.24 (adj +0.15) on $5.00, P(profit) 0.8203, adj growth 5.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
