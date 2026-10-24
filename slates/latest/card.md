# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T20:05:16Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +27.26 | +10.20 | +25.89 | 0.742 | -24.24 | -36.80 | 93.72 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +23.04 | +11.36 | +21.82 | 0.726 | -23.09 | -34.32 | 106.90 |
| C best expression per thesis | 149.99 | +26.41 | +11.49 | +22.87 | 0.680 | -35.16 | -50.56 | 102.47 |
| R FUNDED research stakes | 17.00 | +1.70 | +1.01 | +1.36 | 0.538 | -5.91 | -7.53 | 0.00 |

## SJS @ BOS  ·  10000 joint draws  ·  514 bet sides mapped, 5 +EV candidates, 4 on card

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
| Macklin Celebrini: 2+ assists NO | 83 | 0.906 | 0.863 | +0.066 | +0.023 | $9.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Tanner Jeannot: 1+ goals YES | 9 | 0.116 | 0.108 | +0.020 | +0.013 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 60 | 0.641 | 0.630 | +0.025 | +0.013 | $3.96 | FUNDED_RESEARCH | $1 | BOS:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 21 | 0.242 | 0.232 | +0.021 | +0.010 | $1.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Macklin Celebrini: 2+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (8.67 vs 0.74 bp); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.094); failure: SJS offense succeeds (4+ goals)
- **Tanner Jeannot: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (3.91 vs 0.10 bp); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24SJBOS-SJMCELEBRINI71-2|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: BOS offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no; why: Player prop expression KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.82 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT24SJBOS-SJMCELEBRINI71-2|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: BOS offense succeeds (4+ goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-SJKSHERWOOD44-1|yes; why: higher confidence-adjusted growth (1.31 vs 0.26 bp); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24SJBOS-SJMCELEBRINI71-2|no: INTENTIONAL_DIVERSIFIER (phi -0.094); KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.4392): highest fidelity KXNHLAST-26OCT24SJBOS-SJMCELEBRINI71-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT24SJBOS-SJMCELEBRINI71-2|no (same contract)
- thesis BOS:SUPPRESSED (p 0.3089): highest fidelity KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3412): highest fidelity KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes (same contract)
- KXNHLAST-26OCT24SJBOS-SJMCELEBRINI71-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3412, phi -0.273)
- KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3089, phi -0.129)
- KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4872, phi -0.251)
- KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4392, phi -0.227)
- override: Player prop expression KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.82 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.18 (adj +0.43) on $17.01, P(profit) 0.5534, adj growth 4.1 bp · B EV +1.35 (adj +0.61) on $16.35, P(profit) 0.694, adj growth 5.8 bp · C EV +2.29 (adj +0.77) on $28.93, P(profit) 0.7194, adj growth 7.2 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6415, adj growth 0.8 bp

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
| Taylor Raddysh: 1+ goals YES | 8 | 0.120 | 0.107 | +0.034 | +0.022 | $2.47 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 58 | 0.713 | 0.620 | +0.116 | +0.023 | $7.89 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Nick Cousins: 1+ goals YES | 8 | 0.108 | 0.098 | +0.023 | +0.012 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 14 | 0.170 | 0.160 | +0.021 | +0.011 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (13.28 vs 1.45 bp); relationships: KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT24NYROTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: NYR offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24NYROTT-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (4.80 vs 0.61 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT24NYROTT-OTTMAMADIO22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.067); failure: OTT offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NYROTT-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (4.25 vs 0.02 bp); alternative not eligible: confidence-adjusted EV +0.0012 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT24NYROTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NYROTT-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (2.21 vs 0.02 bp); alternative not eligible: confidence-adjusted EV +0.0012 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.067); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:SUPPRESSED (p 0.3708): highest fidelity KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.3446): highest fidelity KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4115): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4331, phi -0.162)
- KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4115, phi -0.237)
- KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3708, phi -0.134)
- KXNHLGOAL-26OCT24NYROTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3708, phi -0.187)

portfolios: A EV +3.20 (adj +1.33) on $17.01, P(profit) 0.2166, adj growth 12.4 bp · B EV +3.17 (adj +1.28) on $13.45, P(profit) 0.3038, adj growth 12.0 bp · C EV +2.82 (adj +0.64) on $16.08, P(profit) 0.7129, adj growth 5.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ PIT  ·  10000 joint draws  ·  442 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.529 / away 0.471

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
| Connor Dewar: 1+ goals YES | 15 | 0.205 | 0.189 | +0.046 | +0.030 | $3.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 34 | 0.412 | 0.393 | +0.057 | +0.037 | $6.45 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ assists NO | 76 | 0.871 | 0.792 | +0.098 | +0.019 | $9.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Sidney Crosby: 1+ goals YES | 34 | 0.379 | 0.367 | +0.023 | +0.011 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (14.09 vs 13.29 bp); despite a smaller raw edge (+0.046 vs +0.057/contract); relationships: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (14.09 vs 13.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense suppressed (<= 2 goals)
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24NSHPIT-NSH2|no; why: higher confidence-adjusted growth (4.76 vs 0.25 bp); alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NSH offense succeeds (4+ goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes; why: Player prop expression KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.51 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4828): highest fidelity KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes (same contract)
- thesis NSH:SUPPRESSED (p 0.4247): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.212)
- KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 46% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.266)
- KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3654, phi -0.161)
- KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.266)
- override: Player prop expression KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.51 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +3.21 (adj +1.73) on $17.01, P(profit) 0.5673, adj growth 16.3 bp · B EV +3.38 (adj +1.65) on $21.16, P(profit) 0.5056, adj growth 15.6 bp · C EV +1.95 (adj +1.26) on $6.78, P(profit) 0.2047, adj growth 11.2 bp · R EV +0.32 (adj +0.21) on $2.00, P(profit) 0.4125, adj growth 7.8 bp

## BUF @ WSH  ·  10000 joint draws  ·  506 bet sides mapped, 5 +EV candidates, 4 on card

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
| Aliaksei Protas: 1+ goals YES | 17 | 0.240 | 0.222 | +0.061 | +0.042 | $5.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 25 | 0.365 | 0.287 | +0.102 | +0.024 | $2.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Rasmus Dahlin: 1+ assists NO | 52 | 0.608 | 0.561 | +0.070 | +0.024 | $5.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Rasmus Dahlin: 1+ goals NO | 80 | 0.834 | 0.824 | +0.023 | +0.013 | $7.93 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (25.31 vs 6.48 bp); despite a smaller raw edge (+0.061 vs +0.102/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: WSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (25.31 vs 6.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.039); they share one thesis budget; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: WSH offense suppressed (<= 2 goals)
- **Rasmus Dahlin: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no; why: higher confidence-adjusted growth (5.08 vs 2.42 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: BUF offense succeeds (4+ goals)
- **Rasmus Dahlin: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no; why: second expression of the same thesis: KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no has the higher standalone adjusted growth (5.08 vs 2.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4409): highest fidelity KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3956): highest fidelity KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3477, phi -0.227)
- KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3477, phi -0.279)
- KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3883, phi -0.276)
- KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3883, phi -0.2)

portfolios: A EV +3.73 (adj +1.59) on $17.01, P(profit) 0.4929, adj growth 15.0 bp · B EV +3.95 (adj +1.90) on $22.18, P(profit) 0.4031, adj growth 17.8 bp · C EV +4.70 (adj +2.75) on $20.54, P(profit) 0.2405, adj growth 24.3 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.8339, adj growth 1.2 bp

## VGK @ CBJ  ·  10000 joint draws  ·  458 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.444 / away 0.556

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
| Charlie Coyle: 1+ goals YES | 22 | 0.260 | 0.249 | +0.028 | +0.017 | $2.66 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Adam Fantilli: 1+ assists NO | 62 | 0.694 | 0.652 | +0.057 | +0.015 | $5.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (3.39 vs 1.18 bp); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no: INTENTIONAL_DIVERSIFIER (phi -0.103); failure: CBJ offense suppressed (<= 2 goals)
- **Adam Fantilli: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24VGKCBJ-CBJZWERENSKI8-1|no; why: higher confidence-adjusted growth (2.21 vs 0.00 bp); despite a smaller raw edge (+0.057 vs +0.073/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.103); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.346): highest fidelity KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.4353): highest fidelity KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no (same contract)
- KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4353, phi -0.253)
- KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.346, phi -0.274)

portfolios: A EV +0.98 (adj +0.38) on $9.89, P(profit) 0.794, adj growth 3.6 bp · B EV +0.84 (adj +0.33) on $8.49, P(profit) 0.794, adj growth 3.1 bp · C EV +1.51 (adj +0.60) on $15.26, P(profit) 0.794, adj growth 5.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Robert Thomas: 1+ goals YES | 22 | 0.282 | 0.266 | +0.051 | +0.034 | $4.77 | FUNDED_RESEARCH | $2 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Justin Barron: 1+ goals YES | 5 | 0.074 | 0.065 | +0.020 | +0.012 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 28 | 0.331 | 0.317 | +0.037 | +0.023 | $3.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 13 | 0.167 | 0.155 | +0.029 | +0.017 | $2.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT24CARSTL-STL5|yes; why: higher confidence-adjusted growth (13.71 vs 8.24 bp); despite a smaller raw edge (+0.051 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.918 vs 0.572); relationships: KXNHLGOAL-26OCT24CARSTL-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)
- **Justin Barron: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (13.71 vs 5.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (13.71 vs 5.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24CARSTL-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (13.71 vs 5.27 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24CARSTL-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4291): highest fidelity KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.5285): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS_BY_2PLUS (p 0.3069): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.248)
- KXNHLGOAL-26OCT24CARSTL-STLJBARRON72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.099)
- KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.272)
- KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.198)

portfolios: A EV +3.73 (adj +1.21) on $17.01, P(profit) 0.4293, adj growth 10.7 bp · B EV +2.41 (adj +1.51) on $11.70, P(profit) 0.6274, adj growth 14.2 bp · C EV +3.94 (adj +1.89) on $22.14, P(profit) 0.4109, adj growth 16.9 bp · R EV +0.44 (adj +0.29) on $2.00, P(profit) 0.2825, adj growth 10.4 bp

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
| Teddy Blueger: 1+ goals YES | 11 | 0.151 | 0.137 | +0.035 | +0.020 | $2.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 81 | 0.855 | 0.842 | +0.034 | +0.021 | $9.26 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Leon Draisaitl: 1+ assists NO | 37 | 0.485 | 0.407 | +0.099 | +0.021 | $4.59 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.75) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 27 | 0.312 | 0.301 | +0.029 | +0.017 | $3.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24TOREDM-TORTSTECHER28-1|yes; why: higher confidence-adjusted growth (8.71 vs 0.00 bp); despite a smaller raw edge (+0.035 vs +0.075/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24TOREDM-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT24TOREDM-4|no; why: higher confidence-adjusted growth (6.95 vs 1.05 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.007 vs 0.382); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: TOR offense succeeds (4+ goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (4.00 vs 4.00 bp); relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT24TOREDM-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.22); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes; why: Player prop expression KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.42 vs 0.45 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24TOREDM-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.22); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, EDM shot control · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3474): highest fidelity KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.5538): highest fidelity KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.25): highest fidelity KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no (same contract)
- KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4321, phi -0.21)
- KXNHLGOAL-26OCT24TOREDM-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3474, phi -0.188)
- KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5538, phi -0.303)
- KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.25, phi -0.233)
- override: Player prop expression KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT24TOREDM-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.42 vs 0.45 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.82 (adj +0.88) on $17.01, P(profit) 0.5992, adj growth 8.1 bp · B EV +2.62 (adj +1.11) on $19.63, P(profit) 0.6691, adj growth 10.5 bp · C EV +5.02 (adj +1.53) on $16.28, P(profit) 0.7245, adj growth 13.6 bp · R EV +0.12 (adj +0.08) on $3.00, P(profit) 0.8547, adj growth 3.0 bp

## TBL @ UTA  ·  10000 joint draws  ·  446 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.565 / away 0.435

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
| Anthony Cirelli: 1+ goals YES | 18 | 0.223 | 0.211 | +0.033 | +0.021 | $2.81 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 12 | 0.153 | 0.141 | +0.025 | +0.013 | $1.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Anthony Cirelli: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-TBIMIKHEYEV95-1|yes; why: higher confidence-adjusted growth (6.09 vs 0.97 bp); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: TBL offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (3.53 vs 0.13 bp); alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis TBL:OFFENSE_4PLUS (p 0.3395): highest fidelity KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.4504): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.4402, phi -0.224)
- KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3363, phi -0.17)

portfolios: A EV +1.09 (adj +0.64) on $5.93, P(profit) 0.3397, adj growth 5.9 bp · B EV +0.81 (adj +0.48) on $4.43, P(profit) 0.3397, adj growth 4.5 bp · C EV +0.88 (adj +0.56) on $5.11, P(profit) 0.2232, adj growth 5.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ CGY  ·  10000 joint draws  ·  450 bet sides mapped, 5 +EV candidates, 4 on card

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
| Jonathan Castagna: 1+ goals YES | 11 | 0.149 | 0.134 | +0.032 | +0.018 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 10 | 0.129 | 0.120 | +0.023 | +0.014 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 19 | 0.230 | 0.217 | +0.029 | +0.016 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Justin Faulk: 1+ goals NO | 89 | 0.915 | 0.908 | +0.018 | +0.011 | $9.26 | FUNDED_RESEARCH | $3 | DET:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes; why: higher confidence-adjusted growth (6.43 vs 3.65 bp); relationships: KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CGY offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes has the higher standalone adjusted growth (6.43 vs 4.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: CGY offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes has the higher standalone adjusted growth (6.43 vs 3.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CGY offense suppressed (<= 2 goals)
- **Justin Faulk: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no; why: higher confidence-adjusted growth (2.79 vs 2.01 bp); despite a smaller raw edge (+0.018 vs +0.024/contract); relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:OFFENSE_4PLUS (p 0.3555): highest fidelity KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4323): highest fidelity KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no (same contract)
- KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.186)
- KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.174)
- KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.197)
- KXNHLGOAL-26OCT24DETCGY-DETJFAULK72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3499, phi -0.123)

portfolios: A EV +1.99 (adj +1.13) on $15.14, P(profit) 0.4309, adj growth 10.3 bp · B EV +1.47 (adj +0.84) on $15.36, P(profit) 0.4161, adj growth 7.9 bp · C EV +1.38 (adj +0.75) on $14.35, P(profit) 0.7936, adj growth 6.7 bp · R EV +0.06 (adj +0.04) on $3.00, P(profit) 0.9152, adj growth 1.4 bp

## MIN @ SEA  ·  10000 joint draws  ·  438 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.391 / away 0.609

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
| Ben Meyers: 1+ goals YES | 10 | 0.145 | 0.131 | +0.039 | +0.025 | $2.78 | FUNDED_RESEARCH | $1 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Minnesota wins by over 2.5 goals NO | 75 | 0.839 | 0.789 | +0.076 | +0.026 | $9.26 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mackie Samoskevich: 1+ goals YES | 19 | 0.237 | 0.224 | +0.037 | +0.024 | $3.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 12 | 0.160 | 0.146 | +0.033 | +0.019 | $2.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: higher confidence-adjusted growth (13.99 vs 9.23 bp); despite a smaller raw edge (+0.039 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.903 vs 0.457); relationships: KXNHLSPREAD-26OCT24MINSEA-MIN3|no: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: SEA offense suppressed (<= 2 goals)
- **Minnesota wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes has the higher standalone adjusted growth (9.23 vs 8.53 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.216); relationships: KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi 0.102); KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.084); failure: MIN wins by 2+
- **Mackie Samoskevich: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes has the higher standalone adjusted growth (9.23 vs 7.52 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.136); relationships: KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT24MINSEA-MIN3|no: MOSTLY_INDEPENDENT (phi 0.102); KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: SEA offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes has the higher standalone adjusted growth (9.23 vs 7.00 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.127); relationships: KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT24MINSEA-MIN3|no: MOSTLY_INDEPENDENT (phi 0.084); KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4085): highest fidelity KXNHLTEAMTOTAL-26OCT24MINSEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.3094): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN3|no (same contract)
- thesis SEA:WINS (p 0.5307): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN3|no (same contract)
- KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3711, phi -0.169)
- KXNHLSPREAD-26OCT24MINSEA-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2554, phi -0.748)
- KXNHLGOAL-26OCT24MINSEA-SEAMSAMOSKEVICH11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3711, phi -0.203)
- KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3711, phi -0.175)

portfolios: A EV +4.33 (adj +0.88) on $17.01, P(profit) 0.5307, adj growth 7.4 bp · B EV +3.05 (adj +1.65) on $17.25, P(profit) 0.424, adj growth 15.5 bp · C EV +1.90 (adj +0.74) on $4.52, P(profit) 0.196, adj growth 6.6 bp · R EV +0.66 (adj +0.34) on $4.00, P(profit) 0.145, adj growth 12.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT24MINSEA-SEA|yes == KXNHLGAME-26OCT24MINSEA-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
