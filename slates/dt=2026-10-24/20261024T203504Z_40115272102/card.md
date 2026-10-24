# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T20:35:04Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +27.39 | +9.54 | +25.99 | 0.750 | -22.54 | -35.19 | 87.76 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +25.76 | +12.40 | +23.99 | 0.740 | -22.65 | -35.34 | 116.46 |
| C best expression per thesis | 150.01 | +24.70 | +9.78 | +22.90 | 0.726 | -24.39 | -36.88 | 90.19 |
| R FUNDED research stakes | 12.00 | +1.52 | +1.00 | +0.08 | 0.546 | -5.82 | -6.75 | 0.00 |

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
| Tanner Jeannot: 1+ goals YES | 9 | 0.116 | 0.108 | +0.020 | +0.013 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| James Hagens: 1+ goals NO | 78 | 0.815 | 0.805 | +0.023 | +0.013 | $7.44 | FUNDED_RESEARCH | $2 | BOS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 21 | 0.242 | 0.233 | +0.021 | +0.011 | $1.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 60 | 0.641 | 0.630 | +0.025 | +0.013 | $3.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Tanner Jeannot: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (3.91 vs 0.10 bp); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24SJBOS-BOSJHAGENS44-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: BOS offense suppressed (<= 2 goals)
- **James Hagens: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no; why: KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no has the higher standalone adjusted growth (4.27 vs 2.23 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.062); relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: BOS offense succeeds (4+ goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24SJBOS-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (1.65 vs 0.00 bp); despite a smaller raw edge (+0.021 vs +0.063/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT24SJBOS-BOSJHAGENS44-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: SJS offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no; why: Player prop expression KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.82 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24SJBOS-BOSJHAGENS44-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:SUPPRESSED (p 0.3089): highest fidelity KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3412): highest fidelity KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.4872): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24SJBOS-BOSTJEANNOT84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3089, phi -0.129)
- KXNHLGOAL-26OCT24SJBOS-BOSJHAGENS44-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4872, phi -0.192)
- KXNHLGOAL-26OCT24SJBOS-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4392, phi -0.227)
- KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4872, phi -0.251)
- override: Player prop expression KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.82 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +0.94 (adj +0.42) on $16.08, P(profit) 0.5132, adj growth 3.9 bp · B EV +0.85 (adj +0.49) on $14.57, P(profit) 0.6407, adj growth 4.6 bp · C EV +1.17 (adj +0.43) on $12.72, P(profit) 0.7377, adj growth 4.0 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.8149, adj growth 1.2 bp

## NYR @ OTT  ·  10000 joint draws  ·  460 bet sides mapped, 9 +EV candidates, 4 on card

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
| Taylor Raddysh: 1+ goals YES | 8 | 0.120 | 0.107 | +0.034 | +0.022 | $2.34 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 57 | 0.713 | 0.617 | +0.126 | +0.030 | $9.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Vladislav Gavrikov: 1+ assists YES | 25 | 0.338 | 0.289 | +0.075 | +0.026 | $3.35 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Nick Cousins: 1+ goals YES | 8 | 0.108 | 0.098 | +0.023 | +0.012 | $1.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (13.28 vs 7.61 bp); despite a smaller raw edge (+0.034 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.096); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: NYR offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24NYROTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (7.93 vs 1.43 bp); relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.036); failure: OTT offense succeeds (4+ goals)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NYROTT-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (7.61 vs 1.45 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.096); KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: NYR offense suppressed (<= 2 goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NYROTT-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (4.25 vs 0.02 bp); alternative not eligible: confidence-adjusted EV +0.0012 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:SUPPRESSED (p 0.3708): highest fidelity KXNHLAST-26OCT24NYROTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.3446): highest fidelity KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4115): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4331, phi -0.162)
- KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.8 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4115, phi -0.237)
- KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4331, phi -0.276)
- KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3708, phi -0.134)

portfolios: A EV +3.45 (adj +1.32) on $16.08, P(profit) 0.4028, adj growth 12.4 bp · B EV +4.32 (adj +1.63) on $16.56, P(profit) 0.3965, adj growth 15.3 bp · C EV +4.10 (adj +1.12) on $17.45, P(profit) 0.812, adj growth 10.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ PIT  ·  10000 joint draws  ·  442 bet sides mapped, 6 +EV candidates, 4 on card

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
| Connor Dewar: 1+ goals YES | 15 | 0.205 | 0.189 | +0.046 | +0.030 | $3.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 34 | 0.412 | 0.393 | +0.057 | +0.037 | $6.51 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ assists NO | 75 | 0.871 | 0.789 | +0.108 | +0.026 | $9.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Sidney Crosby: 1+ goals YES | 34 | 0.379 | 0.368 | +0.023 | +0.012 | $2.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (14.09 vs 13.29 bp); despite a smaller raw edge (+0.046 vs +0.057/contract); relationships: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (14.09 vs 13.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense suppressed (<= 2 goals)
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24NSHPIT-NSH2|no; why: higher confidence-adjusted growth (8.17 vs 0.25 bp); alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NSH offense succeeds (4+ goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes; why: Player prop expression KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.51 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4828): highest fidelity KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes (same contract)
- thesis NSH:SUPPRESSED (p 0.4247): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis PIT:SUPPRESSED (p 0.3081): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.212)
- KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 46% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.266)
- KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.6 pts; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3654, phi -0.161)
- KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.266)
- override: Player prop expression KXNHLGOAL-26OCT24NSHPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.51 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +2.42 (adj +1.24) on $16.08, P(profit) 0.5239, adj growth 11.8 bp · B EV +3.56 (adj +1.76) on $21.57, P(profit) 0.5056, adj growth 16.6 bp · C EV +1.46 (adj +0.94) on $5.07, P(profit) 0.2047, adj growth 8.6 bp · R EV +0.32 (adj +0.21) on $2.00, P(profit) 0.4125, adj growth 7.8 bp

## BUF @ WSH  ·  10000 joint draws  ·  506 bet sides mapped, 7 +EV candidates, 4 on card

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
| Aliaksei Protas: 1+ goals YES | 17 | 0.240 | 0.222 | +0.061 | +0.042 | $5.47 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 25 | 0.365 | 0.287 | +0.102 | +0.024 | $3.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Rasmus Dahlin: 1+ assists NO | 52 | 0.608 | 0.561 | +0.070 | +0.024 | $5.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Jordan Kyrou: 1+ assists NO | 65 | 0.725 | 0.682 | +0.059 | +0.016 | $7.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (25.31 vs 6.48 bp); despite a smaller raw edge (+0.061 vs +0.102/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT24BUFWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.048); failure: WSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (25.31 vs 6.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.039); they share one thesis budget; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT24BUFWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.031); failure: WSH offense suppressed (<= 2 goals)
- **Rasmus Dahlin: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no; why: higher confidence-adjusted growth (5.08 vs 2.42 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT24BUFWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: BUF offense succeeds (4+ goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT24BUFWSH-5|no; why: higher confidence-adjusted growth (2.66 vs 0.19 bp); wins across more scripts (relative breadth 1.001 vs 0.39); alternative not eligible: confidence-adjusted EV +0.0035 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4409): highest fidelity KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3956): highest fidelity KXNHLGOAL-26OCT24BUFWSH-BUFRDAHLIN26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:SUPPRESSED (p 0.3477): highest fidelity KXNHLAST-26OCT24BUFWSH-WSHJKYROU25-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24BUFWSH-WSHJKYROU25-1|no (same contract)
- KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3477, phi -0.227)
- KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3477, phi -0.279)
- KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3883, phi -0.276)
- KXNHLAST-26OCT24BUFWSH-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4409, phi -0.225)

portfolios: A EV +3.77 (adj +1.54) on $16.08, P(profit) 0.4777, adj growth 14.6 bp · B EV +4.46 (adj +1.99) on $21.63, P(profit) 0.7011, adj growth 18.7 bp · C EV +4.67 (adj +2.46) on $27.86, P(profit) 0.6029, adj growth 22.5 bp · R EV +0.67 (adj +0.46) on $2.00, P(profit) 0.2405, adj growth 16.8 bp

## VGK @ CBJ  ·  10000 joint draws  ·  458 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.449 / away 0.551

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
| Charlie Coyle: 1+ goals YES | 22 | 0.260 | 0.249 | +0.028 | +0.017 | $2.69 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Adam Fantilli: 1+ assists NO | 62 | 0.694 | 0.652 | +0.057 | +0.015 | $5.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (3.39 vs 1.18 bp); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no: INTENTIONAL_DIVERSIFIER (phi -0.103); failure: CBJ offense suppressed (<= 2 goals)
- **Adam Fantilli: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24VGKCBJ-CBJZWERENSKI8-1|no; why: higher confidence-adjusted growth (2.21 vs 0.00 bp); despite a smaller raw edge (+0.057 vs +0.073/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.103); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.346): highest fidelity KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.4353): highest fidelity KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no (same contract)
- KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4353, phi -0.253)
- KXNHLAST-26OCT24VGKCBJ-CBJAFANTILLI19-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.346, phi -0.274)

portfolios: A EV +0.93 (adj +0.36) on $9.35, P(profit) 0.794, adj growth 3.4 bp · B EV +0.85 (adj +0.33) on $8.56, P(profit) 0.794, adj growth 3.1 bp · C EV +1.13 (adj +0.44) on $11.41, P(profit) 0.794, adj growth 4.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ STL  ·  10000 joint draws  ·  444 bet sides mapped, 15 +EV candidates, 4 on card

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
| Robert Thomas: 1+ goals YES | 22 | 0.282 | 0.264 | +0.051 | +0.032 | $4.61 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Justin Barron: 1+ goals YES | 5 | 0.074 | 0.065 | +0.020 | +0.012 | $1.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 28 | 0.331 | 0.317 | +0.037 | +0.023 | $3.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 13 | 0.167 | 0.155 | +0.029 | +0.017 | $2.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT24CARSTL-STL5|yes; why: higher confidence-adjusted growth (12.71 vs 8.24 bp); despite a smaller raw edge (+0.051 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.918 vs 0.572); relationships: KXNHLGOAL-26OCT24CARSTL-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)
- **Justin Barron: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (12.71 vs 5.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (12.71 vs 5.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24CARSTL-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (12.71 vs 5.27 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24CARSTL-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4291): highest fidelity KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.5285): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS_BY_2PLUS (p 0.3069): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT24CARSTL-STL4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.248)
- KXNHLGOAL-26OCT24CARSTL-STLJBARRON72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.099)
- KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.272)
- KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3598, phi -0.198)

portfolios: A EV +4.15 (adj +1.33) on $16.08, P(profit) 0.4358, adj growth 11.3 bp · B EV +2.39 (adj +1.47) on $11.61, P(profit) 0.6274, adj growth 13.8 bp · C EV +2.93 (adj +1.36) on $19.59, P(profit) 0.4132, adj growth 12.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ EDM  ·  10000 joint draws  ·  502 bet sides mapped, 11 +EV candidates, 4 on card

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
| Teddy Blueger: 1+ goals YES | 11 | 0.151 | 0.136 | +0.035 | +0.019 | $2.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 81 | 0.855 | 0.842 | +0.034 | +0.021 | $9.34 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Leon Draisaitl: 1+ assists NO | 37 | 0.485 | 0.407 | +0.099 | +0.021 | $4.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.75) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 27 | 0.312 | 0.301 | +0.029 | +0.017 | $3.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24TOREDM-TORTSTECHER28-1|yes; why: higher confidence-adjusted growth (7.68 vs 0.00 bp); despite a smaller raw edge (+0.035 vs +0.075/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24TOREDM-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-TORKMARCHENKO86-1|no; why: higher confidence-adjusted growth (6.95 vs 2.77 bp); despite a smaller raw edge (+0.034 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT24TOREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: TOR offense succeeds (4+ goals)
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

portfolios: A EV +3.86 (adj +0.89) on $16.08, P(profit) 0.6931, adj growth 8.3 bp · B EV +2.59 (adj +1.07) on $19.64, P(profit) 0.6619, adj growth 10.1 bp · C EV +4.52 (adj +1.29) on $20.03, P(profit) 0.5937, adj growth 11.9 bp · R EV +0.12 (adj +0.08) on $3.00, P(profit) 0.8547, adj growth 3.0 bp

## TBL @ UTA  ·  10000 joint draws  ·  446 bet sides mapped, 3 +EV candidates, 3 on card

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
| Jack McBain: 1+ goals YES | 12 | 0.153 | 0.141 | +0.025 | +0.013 | $1.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 67 | 0.778 | 0.701 | +0.093 | +0.016 | $7.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Anthony Cirelli: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-TBIMIKHEYEV95-1|yes; why: higher confidence-adjusted growth (6.09 vs 0.97 bp); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT24TBUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: TBL offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (3.53 vs 0.13 bp); alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT24TBUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.032); failure: UTA offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT24TBUTA-5|no; why: higher confidence-adjusted growth (2.57 vs 0.32 bp); wins across more scripts (relative breadth 1.007 vs 0.393); alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.032); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis TBL:OFFENSE_4PLUS (p 0.3395): highest fidelity KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3363): highest fidelity KXNHLAST-26OCT24TBUTA-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TBUTA-UTAVTROCHECK16-1|no (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.4504): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.4402, phi -0.224)
- KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3363, phi -0.17)
- KXNHLAST-26OCT24TBUTA-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.8 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4504, phi -0.207)

portfolios: A EV +1.90 (adj +0.75) on $12.03, P(profit) 0.3397, adj growth 7.0 bp · B EV +1.79 (adj +0.65) on $11.65, P(profit) 0.3397, adj growth 6.1 bp · C EV +1.90 (adj +0.63) on $13.03, P(profit) 0.8264, adj growth 5.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ CGY  ·  10000 joint draws  ·  450 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.462 / away 0.538

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
| Jonathan Castagna: 1+ goals YES | 11 | 0.149 | 0.134 | +0.032 | +0.018 | $2.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 10 | 0.129 | 0.120 | +0.023 | +0.014 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 19 | 0.230 | 0.217 | +0.029 | +0.016 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Lucas Raymond: 1+ goals NO | 72 | 0.758 | 0.748 | +0.024 | +0.013 | $5.76 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes; why: higher confidence-adjusted growth (6.43 vs 3.65 bp); relationships: KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: CGY offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes has the higher standalone adjusted growth (6.43 vs 4.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CGY offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes has the higher standalone adjusted growth (6.43 vs 3.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: CGY offense suppressed (<= 2 goals)
- **Lucas Raymond: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24DETCGY-DETVARVIDSSON33-1|no; why: Player prop expression KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no selected over player prop KXNHLAST-26OCT24DETCGY-DETVARVIDSSON33-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.88 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:OFFENSE_4PLUS (p 0.3555): highest fidelity KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4323): highest fidelity KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24DETCGY-DETVARVIDSSON33-1|no — Player prop expression KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no selected over player prop KXNHLAST-26OCT24DETCGY-DETVARVIDSSON33-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.88 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.186)
- KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.174)
- KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.197)
- KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3499, phi -0.235)
- override: Player prop expression KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no selected over player prop KXNHLAST-26OCT24DETCGY-DETVARVIDSSON33-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.88 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.77 (adj +0.82) on $16.08, P(profit) 0.3266, adj growth 7.6 bp · B EV +1.47 (adj +0.84) on $11.89, P(profit) 0.3911, adj growth 7.9 bp · C EV +1.50 (adj +0.60) on $10.40, P(profit) 0.7581, adj growth 5.5 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.7583, adj growth 1.3 bp

## MIN @ SEA  ·  10000 joint draws  ·  438 bet sides mapped, 25 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.391 / away 0.609

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_MIN_win | p_overtime | goals | shots SEA/MIN | SEA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.56 | 0.44 | 0.00 | 6.02 | 28.6/28.9 | 25.6/24.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.47 | 5.95 | 28.5/29.1 | 25.7/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.56 | 0.44 | 0.00 | 9.29 | 30.0/30.6 | 24.9/23.5 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.093 | 0.53 | 0.47 | 0.00 | 5.98 | 22.9/34.5 | 30.8/19.4 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.48 | 0.52 | 0.46 | 5.91 | 23.0/34.3 | 30.8/19.9 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.059 | 0.49 | 0.51 | 0.00 | 9.23 | 24.3/35.9 | 29.0/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Berkly Catton: 1+ goals YES | 16 | 0.217 | 0.199 | +0.048 | +0.030 | $3.88 | FUNDED_RESEARCH | $1 | SEA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 12 | 0.166 | 0.153 | +0.038 | +0.026 | $3.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 10 | 0.145 | 0.129 | +0.039 | +0.023 | $2.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Shane Wright: 1+ goals YES | 17 | 0.214 | 0.200 | +0.034 | +0.021 | $2.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: higher confidence-adjusted growth (13.60 vs 12.08 bp); despite a smaller raw edge (+0.048 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: SEA offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: higher confidence-adjusted growth (12.67 vs 12.08 bp); despite a smaller raw edge (+0.038 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24MINSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: KXNHLSPREAD-26OCT24MINSEA-MIN3|no has the higher standalone adjusted growth (12.08 vs 11.58 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.094); relationships: KXNHLGOAL-26OCT24MINSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: SEA offense suppressed (<= 2 goals)
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: KXNHLSPREAD-26OCT24MINSEA-MIN3|no has the higher standalone adjusted growth (12.08 vs 6.20 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.107); relationships: KXNHLGOAL-26OCT24MINSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4115): highest fidelity KXNHLTEAMTOTAL-26OCT24MINSEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.5346): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN3|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.3116): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN3|no (same contract)
- KXNHLGOAL-26OCT24MINSEA-SEABCATTON27-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3711, phi -0.194)
- KXNHLGOAL-26OCT24MINSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3711, phi -0.184)
- KXNHLGOAL-26OCT24MINSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3711, phi -0.193)
- KXNHLGOAL-26OCT24MINSEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3711, phi -0.2)

portfolios: A EV +4.20 (adj +0.87) on $16.08, P(profit) 0.5346, adj growth 7.4 bp · B EV +3.49 (adj +2.17) on $12.32, P(profit) 0.5622, adj growth 20.3 bp · C EV +1.32 (adj +0.51) on $12.45, P(profit) 0.8441, adj growth 4.9 bp · R EV +0.28 (adj +0.18) on $1.00, P(profit) 0.2173, adj growth 6.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT24MINSEA-SEA|yes == KXNHLGAME-26OCT24MINSEA-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
