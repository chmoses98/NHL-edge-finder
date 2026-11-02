# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-02T20:51:56Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +18.10 | +8.81 | +13.13 | 0.575 | -42.34 | -58.64 | 74.31 |
| B thesis-diversified (joint) ← optimiser card | 143.65 | +16.32 | +9.25 | +6.95 | 0.578 | -35.07 | -50.11 | 81.48 |
| C best expression per thesis | 75.28 | +9.29 | +4.56 | +0.28 | 0.719 | -31.14 | -31.14 | 40.68 |
| R FUNDED research stakes | 16.00 | +1.41 | +0.85 | +4.56 | 0.516 | -8.14 | -9.69 | 0.00 |

## VGK @ BOS  ·  10000 joint draws  ·  462 bet sides mapped, 5 +EV candidates, 4 on card

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
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV02VGKBOS-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (7.32 vs 0.71 bp); despite a smaller raw edge (+0.024 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLAST-26NOV02VGKBOS-VGKMMARNER93-2|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLAST-26NOV02VGKBOS-BOSJPETERKA10-2|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV02VGKBOS-BOSNZADOROV91-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: VGK offense suppressed (<= 2 goals)
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

portfolios: A EV +4.51 (adj +2.21) on $40.95, P(profit) 0.212, adj growth 18.4 bp · B EV +4.38 (adj +2.10) on $45.39, P(profit) 0.1317, adj growth 18.8 bp · C EV +1.36 (adj +0.51) on $20.00, P(profit) 0.9072, adj growth 4.9 bp · R EV +0.44 (adj +0.25) on $1.00, P(profit) 0.077, adj growth 8.0 bp

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
| Sam Reinhart: 1+ goals NO | 62 | 0.700 | 0.678 | +0.063 | +0.042 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Ben Chiarot: 1+ goals YES | 3 | 0.052 | 0.045 | +0.020 | +0.013 | $2.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Carter Mazur: 1+ goals YES | 6 | 0.092 | 0.081 | +0.028 | +0.017 | $3.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 36 | 0.399 | 0.386 | +0.022 | +0.010 | $3.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | DIRECT (0.60) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (16.81 vs 4.91 bp); relationships: KXNHLGOAL-26NOV02DETFLA-DETBCHIAROT8-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV02DETFLA-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: FLA offense succeeds (4+ goals)
- **Ben Chiarot: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes; why: higher confidence-adjusted growth (12.03 vs 10.21 bp); despite a smaller raw edge (+0.020 vs +0.027/contract); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV02DETFLA-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: DET offense suppressed (<= 2 goals)
- **Carter Mazur: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes; why: higher confidence-adjusted growth (10.56 vs 10.21 bp); wins across more scripts (relative breadth 0.924 vs 0.805); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV02DETFLA-DETBCHIAROT8-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: DET offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes; why: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.60 vs 0.19 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV02DETFLA-DETBCHIAROT8-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV02DETFLA-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.3456): highest fidelity KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3612): highest fidelity KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2844): highest fidelity KXNHLTOTAL-26NOV02DETFLA-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4446, phi -0.262)
- KXNHLGOAL-26NOV02DETFLA-DETBCHIAROT8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4281, phi -0.108)
- KXNHLGOAL-26NOV02DETFLA-DETCMAZUR34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4281, phi -0.144)
- KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 40% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4281, phi -0.323)
- override: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.60 vs 0.19 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +6.33 (adj +2.54) on $40.95, P(profit) 0.4726, adj growth 21.8 bp · B EV +5.71 (adj +3.67) on $30.74, P(profit) 0.739, adj growth 32.1 bp · C EV +5.43 (adj +2.93) on $31.20, P(profit) 0.7834, adj growth 26.1 bp · R EV +0.50 (adj +0.33) on $5.00, P(profit) 0.6997, adj growth 12.2 bp

## COL @ CHI  ·  10000 joint draws  ·  432 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.331 / away 0.669

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
| Cale Makar: 1+ goals NO | 77 | 0.823 | 0.807 | +0.041 | +0.025 | $18.08 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.261 | 0.247 | +0.039 | +0.025 | $7.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Cole Smith: 1+ goals YES | 7 | 0.093 | 0.086 | +0.019 | +0.012 | $2.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 2+ assists NO | 78 | 0.847 | 0.803 | +0.055 | +0.011 | $11.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (8.02 vs 1.70 bp); despite a smaller raw edge (+0.041 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV02COLCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no: MOSTLY_INDEPENDENT (phi 0.113); failure: COL offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (8.00 vs 0.37 bp); alternative not eligible: confidence-adjusted EV +0.0051 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV02COLCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no: MOSTLY_INDEPENDENT (phi -0.004); failure: CHI offense suppressed (<= 2 goals)
- **Cole Smith: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (8.00 vs 4.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CHI offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 2+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02COLCHI-COLBNELSON11-1|no; why: higher confidence-adjusted growth (1.70 vs 0.05 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0020 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV02COLCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.12.
- thesis CHI:OFFENSE_4PLUS (p 0.3118): highest fidelity KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.29): highest fidelity KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no (same contract)
- KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5045, phi -0.161)
- KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4738, phi -0.234)
- KXNHLGOAL-26NOV02COLCHI-CHICSMITH22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4738, phi -0.16)
- KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5045, phi -0.285)

portfolios: A EV +4.22 (adj +2.25) on $40.95, P(profit) 0.3186, adj growth 19.4 bp · B EV +3.84 (adj +2.07) on $40.53, P(profit) 0.3157, adj growth 18.3 bp · C EV +2.50 (adj +1.12) on $24.08, P(profit) 0.2608, adj growth 9.7 bp · R EV +0.26 (adj +0.16) on $5.00, P(profit) 0.823, adj growth 5.9 bp

## CGY @ SJS  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.530 / away 0.470

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_CGY_win | p_overtime | goals | shots SJS/CGY | SJS/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.59 | 0.41 | 0.00 | 6.04 | 28.7/28.7 | 25.5/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.45 | 6.04 | 28.6/28.6 | 25.3/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.59 | 0.41 | 0.00 | 9.35 | 30.2/30.2 | 24.7/23.3 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.077 | 0.63 | 0.37 | 0.00 | 6.03 | 33.6/22.5 | 19.6/29.1 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.45 | 5.95 | 34.1/22.9 | 19.7/30.7 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.059 | 0.54 | 0.46 | 0.00 | 5.98 | 22.7/33.4 | 29.9/19.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Dickinson: 1+ goals YES | 5 | 0.072 | 0.065 | +0.019 | +0.012 | $2.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ goals NO | 78 | 0.825 | 0.810 | +0.033 | +0.018 | $20.00 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Michael Misa: 1+ goals YES | 18 | 0.217 | 0.205 | +0.027 | +0.015 | $4.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Sam Dickinson: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes; why: higher confidence-adjusted growth (6.09 vs 0.89 bp); despite a smaller raw edge (+0.019 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02CGYSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (4.26 vs 0.06 bp); despite a smaller raw edge (+0.033 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0024 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02CGYSJ-SJSDICKINSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SJS offense succeeds (4+ goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes; why: higher confidence-adjusted growth (3.11 vs 0.89 bp); despite a smaller raw edge (+0.027 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02CGYSJ-SJSDICKINSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4528): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis SJS:SUPPRESSED (p 0.3413): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV02CGYSJ-SJSDICKINSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3413, phi -0.11)
- KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4528, phi -0.202)
- KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3413, phi -0.19)

portfolios: A EV +3.05 (adj +1.81) on $27.16, P(profit) 0.2706, adj growth 14.8 bp · B EV +2.40 (adj +1.41) on $26.99, P(profit) 0.2381, adj growth 12.3 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.21 (adj +0.11) on $5.00, P(profit) 0.8248, adj growth 4.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
