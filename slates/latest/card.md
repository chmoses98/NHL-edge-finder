# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-02T19:03:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +22.39 | +9.96 | +11.82 | 0.562 | -63.21 | -79.15 | 74.09 |
| B thesis-diversified (joint) ← optimiser card | 124.70 | +16.20 | +9.44 | +8.98 | 0.609 | -40.55 | -54.10 | 82.07 |
| C best expression per thesis | 50.24 | +9.25 | +4.95 | +9.02 | 0.539 | -30.67 | -42.35 | 42.87 |
| R FUNDED research stakes | 15.00 | +1.23 | +0.74 | +4.18 | 0.508 | -7.26 | -9.95 | 0.00 |

## VGK @ BOS  ·  10000 joint draws  ·  462 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.481 / away 0.519

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
| Brayden McNabb: 1+ goals YES | 5 | 0.077 | 0.067 | +0.024 | +0.013 | $2.93 | FUNDED_RESEARCH | $1 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Casey Mittelstadt: 1+ goals YES | 15 | 0.185 | 0.175 | +0.026 | +0.016 | $4.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Braeden Bowman: 1+ goals YES | 14 | 0.171 | 0.162 | +0.023 | +0.014 | $3.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV02VGKBOS-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (7.32 vs 0.71 bp); despite a smaller raw edge (+0.024 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02VGKBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV02VGKBOS-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: VGK offense suppressed (<= 2 goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02VGKBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (4.35 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV02VGKBOS-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: BOS offense suppressed (<= 2 goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV02VGKBOS-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (3.19 vs 0.71 bp); despite a smaller raw edge (+0.023 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV02VGKBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:OFFENSE_4PLUS (p 0.3987): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis BOS:OFFENSE_4PLUS (p 0.4201): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3869, phi -0.117)
- KXNHLGOAL-26NOV02VGKBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3655, phi -0.188)
- KXNHLGOAL-26NOV02VGKBOS-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3869, phi -0.176)

portfolios: A EV +4.53 (adj +2.64) on $18.45, P(profit) 0.3765, adj growth 20.2 bp · B EV +2.65 (adj +1.55) on $11.34, P(profit) 0.3765, adj growth 13.3 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.44 (adj +0.25) on $1.00, P(profit) 0.077, adj growth 8.0 bp

## DET @ FLA  ·  10000 joint draws  ·  418 bet sides mapped, 15 +EV candidates, 4 on card

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
| Ben Chiarot: 1+ goals YES | 3 | 0.052 | 0.045 | +0.020 | +0.013 | $2.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.08) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.126 | 0.113 | +0.030 | +0.017 | $4.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 35 | 0.398 | 0.385 | +0.032 | +0.019 | $7.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (11.59 vs 4.91 bp); relationships: KXNHLGOAL-26NOV02DETFLA-DETBCHIAROT8-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: FLA offense succeeds (4+ goals)
- **Ben Chiarot: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes; why: higher confidence-adjusted growth (11.51 vs 8.89 bp); despite a smaller raw edge (+0.020 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.878 vs 0.738); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: DET offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV02DETFLA-8|yes; why: higher confidence-adjusted growth (7.41 vs 1.80 bp); despite a smaller raw edge (+0.030 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.885 vs 0.336); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV02DETFLA-DETBCHIAROT8-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes; why: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26NOV02DETFLA-DETCMAZUR34-1|yes because adjusted EV is 0.3 pts higher while thesis capture is 0.59 vs 0.15 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV02DETFLA-DETBCHIAROT8-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.3456): highest fidelity KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3612): highest fidelity KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2844): highest fidelity KXNHLTOTAL-26NOV02DETFLA-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4446, phi -0.262)
- KXNHLGOAL-26NOV02DETFLA-DETBCHIAROT8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 92% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4281, phi -0.106)
- KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3456, phi -0.149)
- KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4281, phi -0.322)
- override: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26NOV02DETFLA-DETCMAZUR34-1|yes because adjusted EV is 0.3 pts higher while thesis capture is 0.59 vs 0.15 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +9.89 (adj +3.37) on $44.41, P(profit) 0.3715, adj growth 21.2 bp · B EV +5.43 (adj +3.41) on $34.66, P(profit) 0.406, adj growth 29.7 bp · C EV +4.19 (adj +2.00) on $30.30, P(profit) 0.7774, adj growth 17.8 bp · R EV +0.41 (adj +0.27) on $5.00, P(profit) 0.6997, adj growth 9.7 bp

## COL @ CHI  ·  10000 joint draws  ·  438 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.331 / away 0.669

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_COL_win | p_overtime | goals | shots CHI/COL | CHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.146 | 0.28 | 0.72 | 0.00 | 6.08 | 21.6/34.7 | 29.7/19.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.43 | 0.56 | 0.46 | 5.97 | 22.0/34.7 | 31.1/18.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.109 | 0.24 | 0.76 | 0.00 | 9.3 | 22.9/36.2 | 28.0/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.34 | 0.66 | 0.00 | 6.01 | 27.6/28.5 | 24.1/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.30 | 0.70 | 0.00 | 9.36 | 29.0/30.2 | 22.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.45 | 0.56 | 0.45 | 5.96 | 27.5/28.4 | 24.9/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Patrick Kane: 2+ assists NO | 90 | 0.953 | 0.922 | +0.047 | +0.015 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 22 | 0.269 | 0.253 | +0.037 | +0.021 | $6.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 78 | 0.815 | 0.804 | +0.023 | +0.012 | $13.94 | FUNDED_RESEARCH | $4 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ assists NO | 41 | 0.477 | 0.439 | +0.050 | +0.012 | $4.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
- **Patrick Kane: 2+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (6.22 vs 0.49 bp); despite a smaller raw edge (+0.047 vs +0.051/contract); alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.098); KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: CHI offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02COLCHI-CHI2|yes; why: higher confidence-adjusted growth (5.45 vs 0.25 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLAST-26NOV02COLCHI-CHIPKANE88-2|no: INTENTIONAL_DIVERSIFIER (phi -0.098); KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (1.93 vs 1.22 bp); despite a smaller raw edge (+0.023 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV02COLCHI-CHIPKANE88-2|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.116); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV02COLCHI-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (1.22 vs 0.00 bp); despite a smaller raw edge (+0.050 vs +0.058/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV02COLCHI-CHIPKANE88-2|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.116); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3109): highest fidelity KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.2817): highest fidelity KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no (same contract)
- thesis CHI:SUPPRESSED (p 0.4673): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV02COLCHI-CHIPKANE88-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3109, phi -0.188)
- KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4673, phi -0.254)
- KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5117, phi -0.167)
- KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5117, phi -0.3)

portfolios: A EV +3.65 (adj +1.41) on $44.41, P(profit) 0.5584, adj growth 11.8 bp · B EV +3.05 (adj +1.29) on $45.03, P(profit) 0.5572, adj growth 11.6 bp · C EV +1.64 (adj +0.73) on $11.56, P(profit) 0.6178, adj growth 6.4 bp · R EV +0.12 (adj +0.06) on $4.00, P(profit) 0.8154, adj growth 2.1 bp

## CGY @ SJS  ·  10000 joint draws  ·  444 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.532 / away 0.468

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_CGY_win | p_overtime | goals | shots SJS/CGY | SJS/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.59 | 0.41 | 0.00 | 6.02 | 28.7/28.6 | 25.4/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.43 | 5.98 | 28.6/28.6 | 25.2/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.58 | 0.42 | 0.00 | 9.26 | 30.2/30.0 | 24.4/23.6 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.073 | 0.64 | 0.36 | 0.00 | 6.01 | 33.4/22.8 | 19.9/28.9 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.55 | 0.45 | 0.47 | 5.94 | 33.8/22.8 | 19.7/30.2 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.061 | 0.54 | 0.46 | 0.00 | 6.05 | 22.7/33.8 | 30.1/19.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zach Whitecloud: 1+ goals YES | 2 | 0.041 | 0.035 | +0.020 | +0.013 | $2.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ goals NO | 77 | 0.823 | 0.807 | +0.040 | +0.025 | $20.00 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Michael Misa: 1+ goals YES | 18 | 0.223 | 0.210 | +0.033 | +0.020 | $5.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 24 | 0.282 | 0.269 | +0.030 | +0.017 | $5.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Zach Whitecloud: 1+ goals YES** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: CGY offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV02CGYSJ-SJMCELEBRINI71-2|no; why: higher confidence-adjusted growth (7.92 vs 0.00 bp); despite a smaller raw edge (+0.040 vs +0.068/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV02CGYSJ-CGYZWHITECLOUD28-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: SJS offense succeeds (4+ goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (5.38 vs 3.18 bp); relationships: KXNHLGOAL-26NOV02CGYSJ-CGYZWHITECLOUD28-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: SJS offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes has the higher standalone adjusted growth (5.38 vs 3.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26NOV02CGYSJ-CGYZWHITECLOUD28-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4443): highest fidelity KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.3391): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV02CGYSJ-CGYZWHITECLOUD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4199, phi -0.09)
- KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4443, phi -0.181)
- KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3391, phi -0.207)
- KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3391, phi -0.213)

portfolios: A EV +4.32 (adj +2.54) on $42.74, P(profit) 0.5277, adj growth 20.9 bp · B EV +5.07 (adj +3.19) on $33.67, P(profit) 0.4017, adj growth 27.5 bp · C EV +3.42 (adj +2.22) on $8.38, P(profit) 0.2557, adj growth 18.6 bp · R EV +0.26 (adj +0.16) on $5.00, P(profit) 0.8228, adj growth 5.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
