# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T18:51:13Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +26.97 | +10.14 | +25.87 | 0.757 | -20.01 | -31.70 | 94.31 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +24.48 | +12.67 | +22.69 | 0.739 | -21.95 | -33.94 | 119.75 |
| C best expression per thesis | 149.99 | +26.26 | +12.60 | +23.92 | 0.711 | -29.26 | -42.62 | 116.08 |
| R FUNDED research stakes | 23.00 | +2.14 | +1.33 | +1.85 | 0.575 | -6.31 | -8.69 | 0.00 |

## LAK @ NJD  ·  10000 joint draws  ·  422 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.633 / away 0.366

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
| Luke Evangelista: 1+ assists NO | 60 | 0.790 | 0.660 | +0.173 | +0.043 | $6.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Timo Meier: 1+ goals NO | 73 | 0.789 | 0.773 | +0.046 | +0.030 | $6.36 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 2.5 goals NO | 73 | 0.796 | 0.761 | +0.052 | +0.017 | $4.33 | FUNDED_RESEARCH | $2 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Alex Laferriere: 1+ goals YES | 24 | 0.277 | 0.265 | +0.024 | +0.012 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no; why: higher confidence-adjusted growth (17.45 vs 10.13 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no: REINFORCING (phi 0.226); KXNHLSPREAD-26OCT24LANJ-NJ3|no: REINFORCING (phi 0.16); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: NJD offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no has the higher standalone adjusted growth (17.45 vs 10.13 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.226); they share one thesis budget; relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.226); KXNHLSPREAD-26OCT24LANJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins by over 2.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT24LANJ-NJ2|no; why: KXNHLTEAMTOTAL-26OCT24LANJ-NJ2|no has the higher standalone adjusted growth (3.94 vs 3.28 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.247); relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.16); KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.136); failure: NJD wins by 2+
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24LANJ-NJ3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24LANJ-NJ3|no has the higher standalone adjusted growth (3.28 vs 1.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.136); they share one thesis budget; relationships: KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT24LANJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.136); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.11.
- thesis NJD:SUPPRESSED (p 0.4092): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS (p 0.4551): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT24LANJ-NJLEVANGELISTA77-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.303): highest fidelity KXNHLSPREAD-26OCT24LANJ-NJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT24LANJ-NJ3|no (same contract)
- KXNHLAST-26OCT24LANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.0 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3736, phi -0.219)
- KXNHLGOAL-26OCT24LANJ-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3736, phi -0.196)
- KXNHLSPREAD-26OCT24LANJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.32, phi -0.737)
- KXNHLGOAL-26OCT24LANJ-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.474, phi -0.251)

portfolios: A EV +2.81 (adj +0.59) on $15.50, P(profit) 0.7185, adj growth 5.6 bp · B EV +2.61 (adj +0.86) on $18.35, P(profit) 0.7179, adj growth 8.3 bp · C EV +4.31 (adj +1.15) on $20.46, P(profit) 0.6555, adj growth 10.9 bp · R EV +0.26 (adj +0.12) on $4.00, P(profit) 0.6527, adj growth 4.8 bp

## SJS @ BOS  ·  10000 joint draws  ·  480 bet sides mapped, 5 +EV candidates, 4 on card

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
| Tanner Jeannot: 1+ goals YES | 9 | 0.116 | 0.108 | +0.020 | +0.013 | $1.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Michael Misa: 1+ goals YES | 16 | 0.190 | 0.180 | +0.020 | +0.010 | $1.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 60 | 0.641 | 0.630 | +0.025 | +0.013 | $3.69 | FUNDED_RESEARCH | $1 | BOS:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 71 | 0.770 | 0.735 | +0.046 | +0.011 | $5.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Tanner Jeannot: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (3.91 vs 0.10 bp); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24SJBOS-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: BOS offense suppressed (<= 2 goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (1.64 vs 1.01 bp); despite a smaller raw edge (+0.020 vs +0.021/contract); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.132); failure: SJS offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no; why: Player prop expression KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.82 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24SJBOS-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: BOS offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24SJBOS-SJMCELEBRINI71-2|no; why: despite a smaller raw edge (+0.046 vs +0.047/contract); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT24SJBOS-SJMMISA77-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.132); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:SUPPRESSED (p 0.3089): highest fidelity KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3412): highest fidelity KXNHLGOAL-26OCT24SJBOS-SJMMISA77-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24SJBOS-SJMMISA77-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.4392): highest fidelity KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no (same contract)
- KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3089, phi -0.129)
- KXNHLGOAL-26OCT24SJBOS-SJMMISA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4392, phi -0.204)
- KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4872, phi -0.251)
- KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3412, phi -0.225)
- override: Player prop expression KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.82 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.16 (adj +0.44) on $15.50, P(profit) 0.456, adj growth 4.2 bp · B EV +0.94 (adj +0.42) on $11.76, P(profit) 0.6305, adj growth 4.0 bp · C EV +1.25 (adj +0.37) on $16.48, P(profit) 0.6484, adj growth 3.4 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6415, adj growth 0.8 bp

## NYR @ OTT  ·  10000 joint draws  ·  448 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.535 / away 0.465

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
| Taylor Raddysh: 1+ goals YES | 8 | 0.120 | 0.105 | +0.034 | +0.019 | $1.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 58 | 0.713 | 0.620 | +0.116 | +0.023 | $6.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Nick Cousins: 1+ goals YES | 8 | 0.108 | 0.096 | +0.023 | +0.011 | $1.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Tim Stutzle: 1+ goals NO | 65 | 0.696 | 0.682 | +0.030 | +0.016 | $4.47 | FUNDED_RESEARCH | $2 | OTT:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (10.47 vs 1.45 bp); relationships: KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT24NYROTT-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NYR offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24NYROTT-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (4.80 vs 2.64 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT24NYROTT-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.105); failure: OTT offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24NYROTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (3.44 vs 0.17 bp); despite a smaller raw edge (+0.023 vs +0.071/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT24NYROTT-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense suppressed (<= 2 goals)
- **Tim Stutzle: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no has the higher standalone adjusted growth (4.80 vs 2.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.105); they share one thesis budget; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.105); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense succeeds (4+ goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:SUPPRESSED (p 0.3708): highest fidelity KXNHLAST-26OCT24NYROTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.3446): highest fidelity KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4115): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4331, phi -0.162)
- KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4115, phi -0.237)
- KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3708, phi -0.134)
- KXNHLGOAL-26OCT24NYROTT-OTTTSTUTZLE18-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4115, phi -0.254)

portfolios: A EV +2.16 (adj +0.83) on $15.50, P(profit) 0.4959, adj growth 7.8 bp · B EV +2.59 (adj +0.97) on $14.13, P(profit) 0.6267, adj growth 9.1 bp · C EV +2.05 (adj +0.47) on $11.69, P(profit) 0.7129, adj growth 4.3 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.6964, adj growth 1.8 bp

## NSH @ PIT  ·  10000 joint draws  ·  420 bet sides mapped, 5 +EV candidates, 4 on card

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
| Connor Dewar: 1+ goals YES | 15 | 0.205 | 0.189 | +0.046 | +0.030 | $3.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 35 | 0.412 | 0.394 | +0.047 | +0.028 | $4.56 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ assists NO | 76 | 0.871 | 0.792 | +0.098 | +0.019 | $8.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Sidney Crosby: 1+ goals YES | 34 | 0.379 | 0.367 | +0.023 | +0.011 | $1.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (14.09 vs 7.60 bp); despite a smaller raw edge (+0.046 vs +0.047/contract); relationships: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (14.09 vs 7.60 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense suppressed (<= 2 goals)
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT24NSHPIT-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (4.76 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NSH offense succeeds (4+ goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes; why: Player prop expression KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.51 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4828): highest fidelity KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes — Player prop expression KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.51 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis NSH:SUPPRESSED (p 0.4247): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.212)
- KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 46% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.266)
- KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3654, phi -0.161)
- KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.266)
- override: Player prop expression KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.51 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +2.79 (adj +1.45) on $15.50, P(profit) 0.5673, adj growth 13.6 bp · B EV +2.74 (adj +1.25) on $18.06, P(profit) 0.4902, adj growth 11.8 bp · C EV +1.42 (adj +0.92) on $4.93, P(profit) 0.2047, adj growth 8.4 bp · R EV +0.25 (adj +0.16) on $2.00, P(profit) 0.4125, adj growth 5.6 bp

## BUF @ WSH  ·  10000 joint draws  ·  442 bet sides mapped, 7 +EV candidates, 4 on card

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
| Aliaksei Protas: 1+ goals YES | 17 | 0.240 | 0.222 | +0.061 | +0.042 | $4.88 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
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

portfolios: A EV +4.30 (adj +1.88) on $15.50, P(profit) 0.5848, adj growth 17.6 bp · B EV +3.77 (adj +1.85) on $14.74, P(profit) 0.4809, adj growth 17.4 bp · C EV +3.74 (adj +2.15) on $18.22, P(profit) 0.3299, adj growth 19.7 bp · R EV +0.67 (adj +0.46) on $2.00, P(profit) 0.2405, adj growth 16.8 bp

## VGK @ CBJ  ·  10000 joint draws  ·  430 bet sides mapped, 1 +EV candidates, 1 on card

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
| Charlie Coyle: 1+ goals YES | 22 | 0.260 | 0.249 | +0.028 | +0.017 | $2.23 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (3.39 vs 1.18 bp); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.346): highest fidelity KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes (same contract)
- KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4353, phi -0.253)

portfolios: A EV +0.34 (adj +0.20) on $2.81, P(profit) 0.2599, adj growth 1.9 bp · B EV +0.27 (adj +0.16) on $2.23, P(profit) 0.2599, adj growth 1.5 bp · C EV +0.38 (adj +0.23) on $3.18, P(profit) 0.2599, adj growth 2.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ STL  ·  10000 joint draws  ·  444 bet sides mapped, 17 +EV candidates, 4 on card

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
| Robert Thomas: 1+ goals YES | 21 | 0.282 | 0.261 | +0.061 | +0.039 | $4.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 13 | 0.167 | 0.155 | +0.029 | +0.017 | $1.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 28 | 0.331 | 0.316 | +0.037 | +0.022 | $3.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 68 | 0.729 | 0.714 | +0.034 | +0.019 | $6.76 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24CARSTL-CAR2|no; why: higher confidence-adjusted growth (19.02 vs 7.11 bp); despite a smaller raw edge (+0.061 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (19.02 vs 5.27 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (19.02 vs 4.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: STL offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24CARSTL-CAR2|no; why: Player prop expression KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no selected over player prop KXNHLAST-26OCT24CARSTL-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.85 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4291): highest fidelity KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.5285): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.389): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24CARSTL-CAR2|no — Player prop expression KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no selected over player prop KXNHLAST-26OCT24CARSTL-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.85 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.248)
- KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.198)
- KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.272)
- KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3852, phi -0.239)
- override: Player prop expression KXNHLGOAL-26OCT24CARSTL-CARSAHO20-1|no selected over player prop KXNHLAST-26OCT24CARSTL-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.85 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.46 (adj +0.77) on $15.50, P(profit) 0.6121, adj growth 7.3 bp · B EV +2.45 (adj +1.51) on $16.60, P(profit) 0.5218, adj growth 14.2 bp · C EV +2.95 (adj +1.57) on $16.83, P(profit) 0.2825, adj growth 14.4 bp · R EV +0.10 (adj +0.05) on $2.00, P(profit) 0.7287, adj growth 2.0 bp

## TOR @ EDM  ·  10000 joint draws  ·  502 bet sides mapped, 8 +EV candidates, 4 on card

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
| Teddy Blueger: 1+ goals YES | 10 | 0.151 | 0.135 | +0.045 | +0.029 | $2.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 81 | 0.855 | 0.842 | +0.034 | +0.021 | $8.48 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 16 | 0.193 | 0.184 | +0.024 | +0.014 | $1.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 27 | 0.312 | 0.301 | +0.029 | +0.017 | $2.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24TOREDM-TORTSTECHER28-1|yes; why: higher confidence-adjusted growth (18.20 vs 0.00 bp); despite a smaller raw edge (+0.045 vs +0.065/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24TOREDM-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT24TOREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (6.95 vs 1.72 bp); despite a smaller raw edge (+0.034 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT24TOREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: TOR offense succeeds (4+ goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (3.19 vs 3.04 bp); despite a smaller raw edge (+0.024 vs +0.029/contract); relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT24TOREDM-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (3.04 vs 1.63 bp); despite a smaller raw edge (+0.029 vs +0.086/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24TOREDM-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT24TOREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, EDM shot control · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3474): highest fidelity KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.5538): highest fidelity KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.4321): highest fidelity KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TOREDM-TORAMATTHEWS34-1|no (same contract)
- KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4321, phi -0.21)
- KXNHLGOAL-26OCT24TOREDM-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3474, phi -0.188)
- KXNHLGOAL-26OCT24TOREDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.25, phi -0.152)
- KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.25, phi -0.233)

portfolios: A EV +3.19 (adj +1.09) on $15.50, P(profit) 0.4416, adj growth 10.1 bp · B EV +2.10 (adj +1.31) on $15.53, P(profit) 0.4829, adj growth 12.4 bp · C EV +2.69 (adj +1.48) on $13.35, P(profit) 0.323, adj growth 13.6 bp · R EV +0.12 (adj +0.08) on $3.00, P(profit) 0.8547, adj growth 3.0 bp

## TBL @ UTA  ·  10000 joint draws  ·  428 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.564 / away 0.436

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TBL_win | p_overtime | goals | shots UTA/TBL | UTA/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.63 | 0.37 | 0.00 | 6.05 | 26.8/26.7 | 23.6/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.48 | 5.95 | 26.9/27.1 | 23.8/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.63 | 0.37 | 0.00 | 9.31 | 28.4/28.4 | 23.3/21.4 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 6.02 | 31.8/21.3 | 18.5/27.3 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.065 | 0.54 | 0.46 | 0.00 | 6.05 | 21.3/31.3 | 27.9/17.8 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.55 | 0.45 | 0.46 | 5.91 | 31.8/21.5 | 18.4/28.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anthony Cirelli: 1+ goals YES | 18 | 0.223 | 0.211 | +0.033 | +0.021 | $2.57 | FUNDED_RESEARCH | $1 | TBL:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 12 | 0.153 | 0.141 | +0.025 | +0.013 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 19 | 0.224 | 0.212 | +0.023 | +0.011 | $1.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Anthony Cirelli: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-TBIMIKHEYEV95-1|yes; why: higher confidence-adjusted growth (6.09 vs 0.24 bp); alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: TBL offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (3.53 vs 1.66 bp); relationships: KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: UTA offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-UTAALEE72-1|yes; why: higher confidence-adjusted growth (1.66 vs 0.03 bp); alternative not eligible: confidence-adjusted EV +0.0015 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis TBL:OFFENSE_4PLUS (p 0.3395): highest fidelity KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.4504): highest fidelity KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes (same contract)
- KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.4402, phi -0.224)
- KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3363, phi -0.17)
- KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3363, phi -0.21)

portfolios: A EV +1.26 (adj +0.71) on $7.67, P(profit) 0.4875, adj growth 6.5 bp · B EV +0.90 (adj +0.51) on $5.44, P(profit) 0.4875, adj growth 4.8 bp · C EV +0.87 (adj +0.52) on $5.71, P(profit) 0.3972, adj growth 4.7 bp · R EV +0.17 (adj +0.11) on $1.00, P(profit) 0.2232, adj growth 4.0 bp

## DET @ CGY  ·  10000 joint draws  ·  442 bet sides mapped, 6 +EV candidates, 4 on card

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
| Jonathan Castagna: 1+ goals YES | 10 | 0.149 | 0.134 | +0.043 | +0.028 | $2.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 18 | 0.230 | 0.213 | +0.039 | +0.023 | $2.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 10 | 0.129 | 0.120 | +0.023 | +0.014 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Justin Faulk: 1+ goals NO | 89 | 0.915 | 0.908 | +0.018 | +0.011 | $8.48 | FUNDED_RESEARCH | $3 | DET:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes; why: higher confidence-adjusted growth (17.70 vs 7.50 bp); relationships: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CGY offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes has the higher standalone adjusted growth (17.70 vs 7.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CGY offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes has the higher standalone adjusted growth (17.70 vs 4.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: CGY offense suppressed (<= 2 goals)
- **Justin Faulk: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no; why: higher confidence-adjusted growth (2.79 vs 2.20 bp); despite a smaller raw edge (+0.018 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.995 vs 0.884); relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:OFFENSE_4PLUS (p 0.3555): highest fidelity KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4323): highest fidelity KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no (same contract)
- KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.186)
- KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.197)
- KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.174)
- KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3499, phi -0.123)

portfolios: A EV +2.37 (adj +1.34) on $15.50, P(profit) 0.3177, adj growth 12.5 bp · B EV +2.30 (adj +1.45) on $15.89, P(profit) 0.4094, adj growth 13.6 bp · C EV +2.16 (adj +1.24) on $9.38, P(profit) 0.1492, adj growth 11.4 bp · R EV +0.06 (adj +0.04) on $3.00, P(profit) 0.9152, adj growth 1.4 bp

## MIN @ SEA  ·  10000 joint draws  ·  426 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.407 / away 0.593

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_MIN_win | p_overtime | goals | shots SEA/MIN | SEA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.56 | 0.44 | 0.00 | 6.04 | 28.4/28.9 | 25.6/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.54 | 0.46 | 0.48 | 5.92 | 28.6/29.0 | 25.7/25.3 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.094 | 0.51 | 0.49 | 0.00 | 5.99 | 22.8/34.1 | 30.4/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.59 | 0.41 | 0.00 | 9.26 | 30.0/30.4 | 24.8/23.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.44 | 0.56 | 0.45 | 5.9 | 22.8/34.7 | 31.1/19.8 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.063 | 0.45 | 0.55 | 0.00 | 9.24 | 24.3/35.9 | 28.6/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kirill Kaprizov: 1+ goals NO | 54 | 0.625 | 0.602 | +0.067 | +0.045 | $8.48 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Mackie Samoskevich: 1+ goals YES | 17 | 0.237 | 0.214 | +0.058 | +0.035 | $4.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 10 | 0.145 | 0.130 | +0.039 | +0.024 | $2.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 12 | 0.160 | 0.148 | +0.033 | +0.020 | $2.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: higher confidence-adjusted growth (17.91 vs 10.23 bp); despite a smaller raw edge (+0.067 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: MIN offense succeeds (4+ goals)
- **Mackie Samoskevich: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: higher confidence-adjusted growth (17.34 vs 10.23 bp); despite a smaller raw edge (+0.058 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes has the higher standalone adjusted growth (17.34 vs 12.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: SEA offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes has the higher standalone adjusted growth (17.34 vs 7.95 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.4146): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.5307): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.4085): highest fidelity KXNHLTEAMTOTAL-26OCT24MINSEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3704, phi -0.322)
- KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3711, phi -0.203)
- KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3711, phi -0.169)
- KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3711, phi -0.175)

portfolios: A EV +4.15 (adj +0.84) on $15.50, P(profit) 0.6158, adj growth 7.2 bp · B EV +3.81 (adj +2.38) on $17.28, P(profit) 0.4543, adj growth 22.5 bp · C EV +4.44 (adj +2.50) on $29.76, P(profit) 0.663, adj growth 23.2 bp · R EV +0.36 (adj +0.24) on $3.00, P(profit) 0.6247, adj growth 9.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT24MINSEA-SEA|yes == KXNHLGAME-26OCT24MINSEA-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
