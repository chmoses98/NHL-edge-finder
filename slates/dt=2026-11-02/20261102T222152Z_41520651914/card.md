# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-02T22:21:52Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +16.87 | +7.39 | +11.03 | 0.609 | -42.09 | -48.06 | 63.05 |
| B thesis-diversified (joint) ← optimiser card | 144.28 | +13.58 | +7.38 | +6.13 | 0.596 | -37.50 | -49.27 | 65.36 |
| C best expression per thesis | 90.46 | +10.78 | +4.91 | +9.07 | 0.621 | -29.53 | -41.35 | 43.60 |
| R FUNDED research stakes | 14.00 | +1.12 | +0.66 | +0.05 | 0.608 | -7.69 | -10.02 | 0.00 |

## VGK @ BOS  ·  10000 joint draws  ·  494 bet sides mapped, 5 +EV candidates, 4 on card

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
| Brayden McNabb: 1+ goals YES | 5 | 0.077 | 0.067 | +0.024 | +0.013 | $3.00 | FUNDED_RESEARCH | $1 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| JJ Peterka: 2+ assists NO | 92 | 0.961 | 0.938 | +0.036 | +0.013 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Nikita Zadorov: 1+ goals YES | 4 | 0.059 | 0.053 | +0.016 | +0.010 | $2.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 2+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02VGKBOS-VGKMSTONE61-2|no; why: higher confidence-adjusted growth (8.16 vs 1.16 bp); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLAST-26NOV02VGKBOS-BOSJPETERKA10-2|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV02VGKBOS-BOSNZADOROV91-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: VGK offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV02VGKBOS-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (7.32 vs 0.06 bp); despite a smaller raw edge (+0.024 vs +0.024/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0024 below the 0.010/contract floor; relationships: KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-2|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLAST-26NOV02VGKBOS-BOSJPETERKA10-2|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV02VGKBOS-BOSNZADOROV91-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: VGK offense suppressed (<= 2 goals)
- **JJ Peterka: 2+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02VGKBOS-BOSCMCAVOY73-2|no; why: higher confidence-adjusted growth (5.44 vs 0.67 bp); alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-2|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV02VGKBOS-BOSNZADOROV91-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: BOS offense succeeds (4+ goals)
- **Nikita Zadorov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02VGKBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (5.38 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-2|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV02VGKBOS-BOSJPETERKA10-2|no: MOSTLY_INDEPENDENT (phi -0.025); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.3869): highest fidelity KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-2|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.3987): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis BOS:SUPPRESSED (p 0.3655): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3987, phi -0.253)
- KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3869, phi -0.117)
- KXNHLAST-26NOV02VGKBOS-BOSJPETERKA10-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4201, phi -0.148)
- KXNHLGOAL-26NOV02VGKBOS-BOSNZADOROV91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3655, phi -0.105)

portfolios: A EV +4.63 (adj +2.27) on $42.04, P(profit) 0.212, adj growth 18.7 bp · B EV +4.38 (adj +2.10) on $45.39, P(profit) 0.1317, adj growth 18.8 bp · C EV +1.36 (adj +0.51) on $20.00, P(profit) 0.9072, adj growth 4.9 bp · R EV +0.44 (adj +0.25) on $1.00, P(profit) 0.077, adj growth 8.0 bp

## DET @ FLA  ·  10000 joint draws  ·  418 bet sides mapped, 17 +EV candidates, 4 on card

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
| Sam Reinhart: 1+ goals NO | 63 | 0.700 | 0.681 | +0.053 | +0.035 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.126 | 0.114 | +0.030 | +0.018 | $4.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| J.T. Compher: 1+ goals YES | 11 | 0.146 | 0.134 | +0.029 | +0.018 | $4.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 36 | 0.399 | 0.386 | +0.022 | +0.010 | $3.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | DIRECT (0.60) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02DETFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (11.59 vs 6.79 bp); despite a smaller raw edge (+0.053 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV02DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV02DETFLA-9|yes; why: higher confidence-adjusted growth (8.51 vs 2.96 bp); despite a smaller raw edge (+0.030 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.885 vs 0.368); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV02DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense suppressed (<= 2 goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes; why: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes has the higher standalone adjusted growth (10.21 vs 6.45 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.004); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: DET offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes; why: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.60 vs 0.19 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV02DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.3456): highest fidelity KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3612): highest fidelity KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2844): highest fidelity KXNHLTOTAL-26NOV02DETFLA-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4446, phi -0.262)
- KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3456, phi -0.149)
- KXNHLGOAL-26NOV02DETFLA-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4281, phi -0.186)
- KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 40% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4281, phi -0.323)
- override: override declined: the joint re-optimisation gives KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes less than the minimum stake; KXNHLGOAL-26NOV02DETFLA-DETJCOMPHER37-1|yes kept
- override: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.60 vs 0.19 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +6.51 (adj +2.62) on $42.04, P(profit) 0.4726, adj growth 22.3 bp · B EV +4.49 (adj +2.78) on $33.14, P(profit) 0.4631, adj growth 24.4 bp · C EV +5.10 (adj +2.69) on $31.19, P(profit) 0.3793, adj growth 23.6 bp · R EV +0.41 (adj +0.27) on $5.00, P(profit) 0.6997, adj growth 9.7 bp

## COL @ CHI  ·  10000 joint draws  ·  432 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.333 / away 0.667

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_COL_win | p_overtime | goals | shots CHI/COL | CHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.155 | 0.30 | 0.70 | 0.00 | 6.0 | 21.7/34.5 | 29.6/19.2 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.43 | 0.57 | 0.48 | 5.89 | 21.9/34.5 | 31.1/18.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.117 | 0.27 | 0.73 | 0.00 | 9.34 | 23.2/36.2 | 27.8/18.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.100 | 0.34 | 0.66 | 0.00 | 6.0 | 27.4/28.3 | 23.9/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.33 | 0.67 | 0.00 | 9.31 | 29.1/30.1 | 22.9/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.47 | 0.53 | 0.47 | 5.93 | 27.8/28.7 | 25.4/24.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.261 | 0.247 | +0.039 | +0.025 | $7.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Patrick Kane: 2+ assists NO | 90 | 0.953 | 0.921 | +0.046 | +0.015 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Cole Smith: 1+ goals YES | 7 | 0.093 | 0.085 | +0.019 | +0.011 | $2.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Brock Nelson: 1+ goals NO | 74 | 0.773 | 0.764 | +0.020 | +0.010 | $11.01 | FUNDED_RESEARCH | $3 | COL:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (8.00 vs 0.57 bp); alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLAST-26NOV02COLCHI-CHIPKANE88-2|no: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLGOAL-26NOV02COLCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV02COLCHI-COLBNELSON11-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 2+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (5.98 vs 1.88 bp); despite a smaller raw edge (+0.046 vs +0.061/contract); relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLGOAL-26NOV02COLCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26NOV02COLCHI-COLBNELSON11-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CHI offense succeeds (4+ goals)
- **Cole Smith: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (8.00 vs 3.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV02COLCHI-CHIPKANE88-2|no: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26NOV02COLCHI-COLBNELSON11-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: CHI offense suppressed (<= 2 goals)
- **Brock Nelson: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no; why: Player prop expression KXNHLGOAL-26NOV02COLCHI-COLBNELSON11-1|no selected over player prop KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.91 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26NOV02COLCHI-CHIPKANE88-2|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV02COLCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.12.
- thesis CHI:OFFENSE_4PLUS (p 0.3118): highest fidelity KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.29): highest fidelity KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no (same contract)
- thesis CHI:SUPPRESSED (p 0.4738): highest fidelity KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no (same contract)
- KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4738, phi -0.234)
- KXNHLAST-26NOV02COLCHI-CHIPKANE88-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3118, phi -0.225)
- KXNHLGOAL-26NOV02COLCHI-CHICSMITH22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4738, phi -0.16)
- KXNHLGOAL-26NOV02COLCHI-COLBNELSON11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5045, phi -0.208)
- override: Player prop expression KXNHLGOAL-26NOV02COLCHI-COLBNELSON11-1|no selected over player prop KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.91 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.11 (adj +1.60) on $42.04, P(profit) 0.6584, adj growth 14.5 bp · B EV +3.37 (adj +1.75) on $41.50, P(profit) 0.3232, adj growth 15.5 bp · C EV +4.33 (adj +1.71) on $39.27, P(profit) 0.6527, adj growth 15.1 bp · R EV +0.08 (adj +0.04) on $3.00, P(profit) 0.7735, adj growth 1.4 bp

## CGY @ SJS  ·  10000 joint draws  ·  464 bet sides mapped, 2 +EV candidates, 2 on card

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
| Ivar Stenberg: 1+ goals NO | 78 | 0.820 | 0.808 | +0.028 | +0.016 | $19.75 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Michael Misa: 1+ goals YES | 18 | 0.217 | 0.206 | +0.027 | +0.015 | $4.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02CGYSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (3.30 vs 0.15 bp); despite a smaller raw edge (+0.028 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: SJS offense succeeds (4+ goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (3.30 vs 0.88 bp); alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.3387): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis SJS:OFFENSE_4PLUS (p 0.4491): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4491, phi -0.182)
- KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3387, phi -0.209)

portfolios: A EV +1.61 (adj +0.90) on $23.87, P(profit) 0.2175, adj growth 7.5 bp · B EV +1.35 (adj +0.75) on $24.25, P(profit) 0.8203, adj growth 6.6 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.18 (adj +0.10) on $5.00, P(profit) 0.8203, adj growth 3.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
