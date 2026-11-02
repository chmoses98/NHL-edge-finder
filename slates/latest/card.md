# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-02T19:57:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +22.94 | +8.97 | +14.22 | 0.563 | -66.81 | -83.35 | 60.88 |
| B thesis-diversified (joint) ← optimiser card | 90.94 | +14.68 | +8.67 | +3.83 | 0.554 | -40.76 | -50.68 | 74.55 |
| C best expression per thesis | 45.51 | +8.81 | +4.88 | +1.33 | 0.502 | -32.06 | -34.03 | 42.06 |
| R FUNDED research stakes | 14.00 | +1.14 | +0.64 | +3.84 | 0.612 | -6.26 | -7.69 | 0.00 |

## VGK @ BOS  ·  10000 joint draws  ·  462 bet sides mapped, 3 +EV candidates, 3 on card

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
| Brayden McNabb: 1+ goals YES | 5 | 0.077 | 0.065 | +0.024 | +0.012 | $2.62 | FUNDED_RESEARCH | $1 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Braeden Bowman: 1+ goals YES | 14 | 0.171 | 0.162 | +0.023 | +0.014 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Marat Khusnutdinov: 1+ goals YES | 12 | 0.146 | 0.138 | +0.018 | +0.011 | $2.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV02VGKBOS-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (6.01 vs 0.71 bp); despite a smaller raw edge (+0.024 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02VGKBOS-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV02VGKBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: VGK offense suppressed (<= 2 goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV02VGKBOS-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (3.19 vs 0.71 bp); despite a smaller raw edge (+0.023 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV02VGKBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: VGK offense suppressed (<= 2 goals)
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02VGKBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (2.24 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV02VGKBOS-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:OFFENSE_4PLUS (p 0.3987): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis BOS:OFFENSE_4PLUS (p 0.4201): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV02VGKBOS-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3869, phi -0.117)
- KXNHLGOAL-26NOV02VGKBOS-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3869, phi -0.176)
- KXNHLGOAL-26NOV02VGKBOS-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3655, phi -0.187)

portfolios: A EV +4.22 (adj +2.27) on $16.85, P(profit) 0.3451, adj growth 16.7 bp · B EV +2.15 (adj +1.17) on $9.27, P(profit) 0.3451, adj growth 10.1 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.44 (adj +0.22) on $1.00, P(profit) 0.077, adj growth 7.0 bp

## DET @ FLA  ·  10000 joint draws  ·  418 bet sides mapped, 14 +EV candidates, 4 on card

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
| Alex DeBrincat: 2+ goals YES | 5 | 0.091 | 0.079 | +0.038 | +0.026 | $5.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 63 | 0.700 | 0.681 | +0.053 | +0.035 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Ben Chiarot: 1+ goals YES | 3 | 0.052 | 0.045 | +0.020 | +0.013 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.08) | EVIDENCE_STRONGER | D |
| Carter Mazur: 1+ goals YES | 6 | 0.092 | 0.080 | +0.028 | +0.016 | $3.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
- **Alex DeBrincat: 2+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes; why: higher confidence-adjusted growth (28.01 vs 8.89 bp); despite a smaller raw edge (+0.038 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV02DETFLA-DETBCHIAROT8-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV02DETFLA-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: DET offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (11.59 vs 4.91 bp); relationships: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV02DETFLA-DETBCHIAROT8-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV02DETFLA-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: FLA offense succeeds (4+ goals)
- **Ben Chiarot: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes has the higher standalone adjusted growth (28.01 vs 11.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV02DETFLA-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: DET offense suppressed (<= 2 goals)
- **Carter Mazur: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes has the higher standalone adjusted growth (28.01 vs 9.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV02DETFLA-DETBCHIAROT8-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis DET:OFFENSE_4PLUS (p 0.3612): highest fidelity KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes (same contract)
- thesis FLA:SUPPRESSED (p 0.3456): highest fidelity KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no (same contract)
- thesis GAME:HIGH_EVENT (p 0.2844): highest fidelity KXNHLTOTAL-26NOV02DETFLA-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4281, phi -0.222)
- KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4446, phi -0.262)
- KXNHLGOAL-26NOV02DETFLA-DETBCHIAROT8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 92% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4281, phi -0.106)
- KXNHLGOAL-26NOV02DETFLA-DETCMAZUR34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4281, phi -0.142)

portfolios: A EV +10.59 (adj +3.70) on $46.34, P(profit) 0.3715, adj growth 23.4 bp · B EV +8.95 (adj +5.91) on $32.09, P(profit) 0.2172, adj growth 50.4 bp · C EV +6.97 (adj +4.24) on $31.85, P(profit) 0.3468, adj growth 36.4 bp · R EV +0.41 (adj +0.27) on $5.00, P(profit) 0.6997, adj growth 9.7 bp

## COL @ CHI  ·  10000 joint draws  ·  438 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.331 / away 0.669

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_COL_win | p_overtime | goals | shots CHI/COL | CHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.151 | 0.28 | 0.72 | 0.00 | 6.05 | 21.7/34.5 | 29.5/19.3 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.117 | 0.25 | 0.75 | 0.00 | 9.27 | 23.0/36.1 | 27.9/18.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.44 | 0.56 | 0.48 | 5.94 | 22.1/35.0 | 31.5/18.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.31 | 0.69 | 0.00 | 6.08 | 27.5/28.5 | 24.2/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.47 | 0.53 | 0.50 | 5.94 | 27.8/28.9 | 25.4/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.32 | 0.68 | 0.00 | 9.3 | 29.0/30.0 | 22.4/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 22 | 0.261 | 0.248 | +0.029 | +0.016 | $5.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 78 | 0.813 | 0.802 | +0.021 | +0.011 | $11.88 | FUNDED_RESEARCH | $3 | COL:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ assists NO | 41 | 0.477 | 0.439 | +0.050 | +0.012 | $4.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.72) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (3.25 vs 0.40 bp); alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CHI offense suppressed (<= 2 goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (1.48 vs 1.22 bp); despite a smaller raw edge (+0.021 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.128); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (1.22 vs 0.04 bp); alternative not eligible: confidence-adjusted EV +0.0018 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.128); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3062): highest fidelity KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.2878): highest fidelity KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no (same contract)
- KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4752, phi -0.262)
- KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5077, phi -0.174)
- KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 28% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5077, phi -0.302)

portfolios: A EV +3.78 (adj +1.37) on $45.85, P(profit) 0.5351, adj growth 9.3 bp · B EV +1.46 (adj +0.63) on $21.20, P(profit) 0.5654, adj growth 5.5 bp · C EV +1.21 (adj +0.49) on $9.98, P(profit) 0.6111, adj growth 4.3 bp · R EV +0.08 (adj +0.04) on $3.00, P(profit) 0.8134, adj growth 1.4 bp

## CGY @ SJS  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.531 / away 0.469

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
| Ivar Stenberg: 1+ goals NO | 78 | 0.825 | 0.810 | +0.033 | +0.018 | $20.00 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Michael Misa: 1+ goals YES | 18 | 0.217 | 0.205 | +0.027 | +0.015 | $4.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Michael Misa: 1+ assists YES | 26 | 0.320 | 0.285 | +0.046 | +0.011 | $4.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV02CGYSJ-SJMCELEBRINI71-2|no; why: higher confidence-adjusted growth (4.26 vs 0.00 bp); despite a smaller raw edge (+0.033 vs +0.093/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.071); failure: SJS offense succeeds (4+ goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes; why: higher confidence-adjusted growth (3.11 vs 1.45 bp); despite a smaller raw edge (+0.027 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SJS offense suppressed (<= 2 goals)
- **Michael Misa: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (1.45 vs 1.02 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0094 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.071); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4528): highest fidelity KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3413): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4528, phi -0.202)
- KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3413, phi -0.19)
- KXNHLAST-26NOV02CGYSJ-SJMMISA77-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3413, phi -0.256)

portfolios: A EV +4.34 (adj +1.63) on $40.95, P(profit) 0.4435, adj growth 11.6 bp · B EV +2.12 (adj +0.96) on $28.38, P(profit) 0.3892, adj growth 8.5 bp · C EV +0.62 (adj +0.15) on $3.68, P(profit) 0.3199, adj growth 1.3 bp · R EV +0.21 (adj +0.11) on $5.00, P(profit) 0.8248, adj growth 4.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
