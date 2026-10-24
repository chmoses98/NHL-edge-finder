# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T22:52:39Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +27.16 | +8.85 | +25.44 | 0.742 | -24.20 | -36.48 | 80.32 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +22.98 | +11.00 | +21.63 | 0.730 | -22.02 | -32.96 | 103.78 |
| C best expression per thesis | 149.99 | +22.85 | +9.33 | +21.25 | 0.716 | -24.44 | -36.84 | 86.01 |
| R FUNDED research stakes | 22.00 | +1.79 | +0.93 | +0.88 | 0.638 | -5.58 | -7.90 | 0.00 |

## SJS @ BOS  ·  10000 joint draws  ·  514 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.627 / away 0.372

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
| Sam Dickinson: 1+ goals YES | 4 | 0.062 | 0.054 | +0.020 | +0.012 | $1.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 70 | 0.773 | 0.734 | +0.059 | +0.019 | $8.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Hampus Lindholm: 1+ goals YES | 6 | 0.081 | 0.074 | +0.017 | +0.010 | $1.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 59 | 0.641 | 0.626 | +0.035 | +0.019 | $5.44 | FUNDED_RESEARCH | $2 | BOS:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Sam Dickinson: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-SJMMISA77-1|yes; why: higher confidence-adjusted growth (7.09 vs 1.53 bp); despite a smaller raw edge (+0.020 vs +0.021/contract); wins across more scripts (relative breadth 0.975 vs 0.87); alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.04); KXNHLGOAL-26OCT24SJBOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24SJBOS-SJMCELEBRINI71-2|no; why: higher confidence-adjusted growth (4.06 vs 1.45 bp); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24SJBOS-SJSDICKINSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.04); KXNHLGOAL-26OCT24SJBOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: SJS offense succeeds (4+ goals)
- **Hampus Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24SJBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (3.77 vs 0.19 bp); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24SJBOS-SJSDICKINSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: BOS offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no; why: Player prop expression KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.82 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24SJBOS-SJSDICKINSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24SJBOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:SUPPRESSED (p 0.3089): highest fidelity KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no (same contract)
- thesis SJS:SUPPRESSED (p 0.4392): highest fidelity KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3412): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24SJBOS-SJSDICKINSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4392, phi -0.122)
- KXNHLAST-26OCT24SJBOS-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3412, phi -0.219)
- KXNHLGOAL-26OCT24SJBOS-BOSHLINDHOLM27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3089, phi -0.103)
- KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4872, phi -0.251)
- override: Player prop expression KXNHLGOAL-26OCT24SJBOS-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT24SJBOS-BOSJPETERKA10-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.82 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.41 (adj +0.61) on $15.95, P(profit) 0.4582, adj growth 5.8 bp · B EV +1.86 (adj +0.91) on $16.42, P(profit) 0.5678, adj growth 8.5 bp · C EV +1.87 (adj +0.62) on $21.60, P(profit) 0.5705, adj growth 5.8 bp · R EV +0.11 (adj +0.06) on $2.00, P(profit) 0.6415, adj growth 2.3 bp

## NYR @ OTT  ·  10000 joint draws  ·  466 bet sides mapped, 11 +EV candidates, 4 on card

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
| Jake Sanderson: 1+ assists NO | 57 | 0.713 | 0.617 | +0.126 | +0.030 | $8.88 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Michael Amadio: 1+ goals YES | 13 | 0.170 | 0.159 | +0.032 | +0.021 | $2.66 | FUNDED_RESEARCH | $1 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Taylor Raddysh: 1+ goals YES | 8 | 0.108 | 0.099 | +0.023 | +0.013 | $1.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 8 | 0.108 | 0.098 | +0.023 | +0.012 | $1.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24NYROTT-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (7.93 vs 2.64 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT24NYROTT-OTTMAMADIO22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.067); KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.036); failure: OTT offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24NYROTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (7.70 vs 0.00 bp); despite a smaller raw edge (+0.032 vs +0.044/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.067); KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense suppressed (<= 2 goals)
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (4.98 vs 2.06 bp); despite a smaller raw edge (+0.023 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT24NYROTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: NYR offense suppressed (<= 2 goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24NYROTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (4.25 vs 0.00 bp); despite a smaller raw edge (+0.023 vs +0.044/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT24NYROTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:SUPPRESSED (p 0.3708): highest fidelity KXNHLAST-26OCT24NYROTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.4331): highest fidelity KXNHLGOAL-26OCT24NYROTT-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT24NYROTT-NYRPDOROFEYEV16-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.3446): highest fidelity KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT24NYROTT-NYRVGAVRIKOV44-1|yes (same contract)
- KXNHLAST-26OCT24NYROTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.8 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4115, phi -0.237)
- KXNHLGOAL-26OCT24NYROTT-OTTMAMADIO22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3708, phi -0.187)
- KXNHLGOAL-26OCT24NYROTT-NYRTRADDYSH14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4331, phi -0.149)
- KXNHLGOAL-26OCT24NYROTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3708, phi -0.134)

portfolios: A EV +2.09 (adj +0.53) on $15.95, P(profit) 0.5725, adj growth 5.0 bp · B EV +3.31 (adj +1.29) on $14.47, P(profit) 0.8234, adj growth 12.2 bp · C EV +3.44 (adj +0.93) on $23.24, P(profit) 0.5961, adj growth 8.6 bp · R EV +0.23 (adj +0.15) on $1.00, P(profit) 0.1697, adj growth 5.4 bp

## NSH @ PIT  ·  10000 joint draws  ·  442 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.528 / away 0.472

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_NSH_win | p_overtime | goals | shots PIT/NSH | PIT/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.62 | 0.38 | 0.00 | 6.06 | 27.9/27.6 | 24.5/23.7 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.109 | 0.66 | 0.34 | 0.00 | 6.01 | 33.5/21.9 | 19.2/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.59 | 0.41 | 0.00 | 9.41 | 29.5/29.2 | 23.4/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.52 | 0.48 | 0.45 | 5.94 | 27.6/27.2 | 24.0/24.3 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.46 | 0.47 | 5.96 | 33.3/22.1 | 19.0/29.8 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.078 | 0.70 | 0.30 | 0.00 | 9.38 | 35.1/23.4 | 18.7/27.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mavrik Bourque: 1+ assists NO | 74 | 0.866 | 0.781 | +0.113 | +0.028 | $8.88 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Blake Lizotte: 1+ goals YES | 12 | 0.155 | 0.144 | +0.028 | +0.016 | $1.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 14 | 0.188 | 0.166 | +0.039 | +0.017 | $1.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 34 | 0.386 | 0.373 | +0.030 | +0.018 | $3.00 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_STRONGER | D |
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT24NSHPIT-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (8.96 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: NSH offense succeeds (4+ goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (5.15 vs 5.06 bp); despite a smaller raw edge (+0.028 vs +0.039/contract); relationships: KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (5.06 vs 2.98 bp); relationships: KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (5.06 vs 2.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4828): highest fidelity KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes (same contract)
- thesis NSH:SUPPRESSED (p 0.4247): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT24NSHPIT-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.1 pts; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3654, phi -0.166)
- KXNHLGOAL-26OCT24NSHPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.179)
- KXNHLGOAL-26OCT24NSHPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.194)
- KXNHLGOAL-26OCT24NSHPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3081, phi -0.262)

portfolios: A EV +2.72 (adj +1.14) on $15.95, P(profit) 0.5431, adj growth 10.5 bp · B EV +2.51 (adj +0.94) on $15.72, P(profit) 0.519, adj growth 8.9 bp · C EV +0.72 (adj +0.32) on $2.73, P(profit) 0.1875, adj growth 2.9 bp · R EV +0.09 (adj +0.05) on $1.00, P(profit) 0.3862, adj growth 1.8 bp

## BUF @ WSH  ·  10000 joint draws  ·  498 bet sides mapped, 8 +EV candidates, 4 on card

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
| Aliaksei Protas: 1+ goals YES | 17 | 0.240 | 0.222 | +0.061 | +0.042 | $5.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 25 | 0.365 | 0.281 | +0.102 | +0.018 | $2.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Jordan Kyrou: 1+ assists NO | 65 | 0.725 | 0.682 | +0.059 | +0.016 | $6.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ goals NO | 64 | 0.683 | 0.670 | +0.027 | +0.014 | $4.42 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (25.31 vs 3.46 bp); despite a smaller raw edge (+0.061 vs +0.102/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLAST-26OCT24BUFWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.048); KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: WSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (25.31 vs 3.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.039); they share one thesis budget; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLAST-26OCT24BUFWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: WSH offense suppressed (<= 2 goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT24BUFWSH-5|no; why: higher confidence-adjusted growth (2.66 vs 0.19 bp); wins across more scripts (relative breadth 1.001 vs 0.39); alternative not eligible: confidence-adjusted EV +0.0035 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: WSH offense succeeds (4+ goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no; why: Player prop expression KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.84 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT24BUFWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4409): highest fidelity KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3956): highest fidelity KXNHLAST-26OCT24BUFWSH-BUFJZUCKER17-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no — Player prop expression KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.84 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WSH:SUPPRESSED (p 0.3477): highest fidelity KXNHLAST-26OCT24BUFWSH-WSHJKYROU25-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24BUFWSH-WSHJKYROU25-1|no (same contract)
- KXNHLGOAL-26OCT24BUFWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3477, phi -0.227)
- KXNHLAST-26OCT24BUFWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.1 pts; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3477, phi -0.279)
- KXNHLAST-26OCT24BUFWSH-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4409, phi -0.225)
- KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3883, phi -0.248)
- override: Player prop expression KXNHLGOAL-26OCT24BUFWSH-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT24BUFWSH-BUFRDAHLIN26-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.84 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.72 (adj +1.42) on $15.95, P(profit) 0.4771, adj growth 13.4 bp · B EV +3.35 (adj +1.62) on $18.49, P(profit) 0.3726, adj growth 15.2 bp · C EV +4.10 (adj +2.19) on $23.14, P(profit) 0.5784, adj growth 20.1 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.6833, adj growth 1.5 bp

## VGK @ CBJ  ·  10000 joint draws  ·  464 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.452 / away 0.548

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_VGK_win | p_overtime | goals | shots CBJ/VGK | CBJ/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.45 | 0.55 | 0.00 | 5.99 | 27.2/27.3 | 23.4/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.47 | 0.53 | 0.46 | 5.9 | 27.8/27.7 | 24.5/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.43 | 0.57 | 0.00 | 9.19 | 28.7/28.8 | 22.5/23.0 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.072 | 0.37 | 0.63 | 0.00 | 5.97 | 21.8/32.2 | 28.0/18.9 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.063 | 0.49 | 0.51 | 0.00 | 5.97 | 32.2/22.0 | 18.6/28.4 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.55 | 0.45 | 0.48 | 5.93 | 32.7/22.4 | 19.3/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivan Barbashev: 1+ goals YES | 20 | 0.238 | 0.227 | +0.026 | +0.016 | $2.48 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 15 | 0.192 | 0.171 | +0.033 | +0.012 | $1.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 22 | 0.257 | 0.246 | +0.025 | +0.014 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ assists NO | 43 | 0.559 | 0.459 | +0.112 | +0.011 | $3.13 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.76) | CALIBRATION_WARNING | D |
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT24VGKCBJ-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (3.24 vs 0.00 bp); despite a smaller raw edge (+0.026 vs +0.032/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no: INTENTIONAL_DIVERSIFIER (phi -0.212); failure: VGK offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (2.45 vs 2.43 bp); relationships: KXNHLGOAL-26OCT24VGKCBJ-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (2.45 vs 2.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT24VGKCBJ-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Jack Eichel: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT24VGKCBJ-VGKJEICHEL9-2|no; why: higher confidence-adjusted growth (1.13 vs 0.84 bp); alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24VGKCBJ-VGKIBARBASHEV49-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.212); KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis VGK:OFFENSE_4PLUS (p 0.3993): highest fidelity KXNHLGOAL-26OCT24VGKCBJ-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24VGKCBJ-VGKIBARBASHEV49-1|yes (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.3388): highest fidelity KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes (same contract)
- thesis CBJ:NET_LOW_VOLUME (p 0.4021): highest fidelity KXNHLSAVE-26OCT24VGKCBJ-CBJCTALBOT33-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT24VGKCBJ-CBJCTALBOT33-27|no (same contract)
- KXNHLGOAL-26OCT24VGKCBJ-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3832, phi -0.22)
- KXNHLGOAL-26OCT24VGKCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4396, phi -0.216)
- KXNHLGOAL-26OCT24VGKCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4396, phi -0.25)
- KXNHLAST-26OCT24VGKCBJ-VGKJEICHEL9-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 24% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.4 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3993, phi -0.3)

portfolios: A EV +3.34 (adj +0.64) on $15.95, P(profit) 0.6016, adj growth 5.8 bp · B EV +1.60 (adj +0.49) on $9.00, P(profit) 0.4822, adj growth 4.7 bp · C EV +2.96 (adj +0.62) on $14.73, P(profit) 0.617, adj growth 5.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ STL  ·  10000 joint draws  ·  446 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.420 / away 0.580

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_CAR_win | p_overtime | goals | shots STL/CAR | STL/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.132 | 0.49 | 0.51 | 0.00 | 5.99 | 20.9/33.0 | 29.2/17.6 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.45 | 0.55 | 0.43 | 5.97 | 21.1/33.3 | 29.7/18.0 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.102 | 0.51 | 0.49 | 0.00 | 9.26 | 22.4/34.9 | 28.4/16.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.101 | 0.55 | 0.45 | 0.00 | 6.03 | 26.7/27.4 | 24.0/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.55 | 0.45 | 0.44 | 5.96 | 26.6/27.5 | 24.4/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.58 | 0.42 | 0.00 | 9.37 | 28.1/29.0 | 23.0/21.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 22 | 0.294 | 0.270 | +0.062 | +0.038 | $5.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 27 | 0.334 | 0.317 | +0.050 | +0.033 | $4.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 12 | 0.163 | 0.151 | +0.036 | +0.024 | $2.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 74 | 0.786 | 0.773 | +0.033 | +0.020 | $8.62 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (17.73 vs 11.38 bp); relationships: KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT24CARSTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (17.73 vs 11.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT24CARSTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (17.73 vs 10.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT24CARSTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: STL offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24CARSTL-STL2|yes; why: KXNHLSPREAD-26OCT24CARSTL-STL2|yes has the higher standalone adjusted growth (7.24 vs 4.75 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.149); relationships: KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, CAR shot control · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4248): highest fidelity KXNHLTEAMTOTAL-26OCT24CARSTL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.5244): highest fidelity KXNHLSPREAD-26OCT24CARSTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS_BY_2PLUS (p 0.3093): highest fidelity KXNHLSPREAD-26OCT24CARSTL-STL2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT24CARSTL-STL5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24CARSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3566, phi -0.258)
- KXNHLGOAL-26OCT24CARSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3566, phi -0.258)
- KXNHLGOAL-26OCT24CARSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3566, phi -0.166)
- KXNHLGOAL-26OCT24CARSTL-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3874, phi -0.217)

portfolios: A EV +3.86 (adj +1.24) on $15.95, P(profit) 0.4696, adj growth 10.3 bp · B EV +3.35 (adj +2.14) on $21.24, P(profit) 0.5645, adj growth 20.1 bp · C EV +3.56 (adj +2.04) on $14.81, P(profit) 0.5267, adj growth 18.7 bp · R EV +0.13 (adj +0.08) on $3.00, P(profit) 0.7863, adj growth 3.0 bp

## TOR @ EDM  ·  10000 joint draws  ·  504 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.576 / away 0.424

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_TOR_win | p_overtime | goals | shots EDM/TOR | EDM/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.132 | 0.74 | 0.26 | 0.00 | 6.06 | 35.2/22.5 | 20.0/30.1 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.115 | 0.72 | 0.28 | 0.00 | 9.5 | 37.0/24.3 | 19.6/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.112 | 0.67 | 0.33 | 0.00 | 9.63 | 31.6/30.6 | 25.2/24.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.70 | 0.30 | 0.00 | 6.05 | 29.7/28.9 | 26.2/25.1 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.58 | 0.42 | 0.47 | 5.95 | 35.4/23.1 | 19.9/31.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.54 | 0.46 | 0.46 | 6.03 | 29.6/28.7 | 25.5/26.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.149 | 0.136 | +0.033 | +0.019 | $2.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ assists YES | 33 | 0.407 | 0.366 | +0.061 | +0.020 | $3.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 27 | 0.314 | 0.302 | +0.030 | +0.018 | $2.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ goals NO | 60 | 0.644 | 0.632 | +0.028 | +0.015 | $4.60 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24TOREDM-TORTSTECHER28-1|yes; why: higher confidence-adjusted growth (7.49 vs 0.00 bp); despite a smaller raw edge (+0.033 vs +0.057/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT24TOREDM-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: TOR offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (4.00 vs 3.54 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT24TOREDM-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (4.00 vs 3.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.026); they share one thesis budget; relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT24TOREDM-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: EDM offense suppressed (<= 2 goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TOREDM-TORGMCKENNA92-1|no; why: Player prop expression KXNHLGOAL-26OCT24TOREDM-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT24TOREDM-TORGMCKENNA92-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.81 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, EDM shot control · high event (8+) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.351): highest fidelity KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.4337): highest fidelity KXNHLTEAMTOTAL-26OCT24TOREDM-TOR4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT24TOREDM-TORGMCKENNA92-1|no — Player prop expression KXNHLGOAL-26OCT24TOREDM-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT24TOREDM-TORGMCKENNA92-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.81 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis EDM:OFFENSE_4PLUS (p 0.5509): highest fidelity KXNHLAST-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes (same contract)
- KXNHLGOAL-26OCT24TOREDM-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4337, phi -0.211)
- KXNHLAST-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2516, phi -0.255)
- KXNHLGOAL-26OCT24TOREDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2516, phi -0.211)
- KXNHLGOAL-26OCT24TOREDM-TORAMATTHEWS34-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.351, phi -0.296)
- override: Player prop expression KXNHLGOAL-26OCT24TOREDM-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT24TOREDM-TORGMCKENNA92-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.81 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.97 (adj +0.51) on $15.95, P(profit) 0.609, adj growth 4.8 bp · B EV +1.70 (adj +0.84) on $12.82, P(profit) 0.5153, adj growth 7.9 bp · C EV +3.27 (adj +1.15) on $23.54, P(profit) 0.42, adj growth 10.6 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.6445, adj growth 1.8 bp

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
| Jack McBain: 1+ goals YES | 11 | 0.153 | 0.138 | +0.036 | +0.021 | $2.41 | FUNDED_RESEARCH | $1 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Anthony Cirelli: 1+ goals YES | 18 | 0.223 | 0.211 | +0.033 | +0.021 | $2.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (9.61 vs 0.41 bp); alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: UTA offense suppressed (<= 2 goals)
- **Anthony Cirelli: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-TBIMIKHEYEV95-1|yes; why: higher confidence-adjusted growth (6.09 vs 0.97 bp); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: TBL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis TBL:OFFENSE_4PLUS (p 0.3395): highest fidelity KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.4504): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3363, phi -0.17)
- KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.4402, phi -0.224)

portfolios: A EV +1.56 (adj +0.95) on $6.48, P(profit) 0.3397, adj growth 8.8 bp · B EV +1.20 (adj +0.74) on $5.08, P(profit) 0.3397, adj growth 6.9 bp · C EV +0.64 (adj +0.41) on $3.71, P(profit) 0.2232, adj growth 3.7 bp · R EV +0.31 (adj +0.18) on $1.00, P(profit) 0.1528, adj growth 6.6 bp

## DET @ CGY  ·  10000 joint draws  ·  450 bet sides mapped, 7 +EV candidates, 4 on card

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
| Moritz Seider: 1+ goals NO | 86 | 0.906 | 0.893 | +0.037 | +0.025 | $8.88 | FUNDED_RESEARCH | $3 | DET:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 11 | 0.149 | 0.134 | +0.032 | +0.018 | $2.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 10 | 0.129 | 0.120 | +0.023 | +0.014 | $1.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 19 | 0.230 | 0.216 | +0.029 | +0.015 | $2.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Moritz Seider: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no; why: higher confidence-adjusted growth (11.74 vs 2.01 bp); relationships: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: DET offense succeeds (4+ goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes; why: higher confidence-adjusted growth (6.43 vs 3.12 bp); relationships: KXNHLGOAL-26OCT24DETCGY-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: CGY offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes has the higher standalone adjusted growth (6.43 vs 4.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: CGY offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes has the higher standalone adjusted growth (6.43 vs 3.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:OFFENSE_4PLUS (p 0.3555): highest fidelity KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4323): highest fidelity KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT24DETCGY-DETLRAYMOND23-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT24DETCGY-DETMSEIDER53-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3499, phi -0.155)
- KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.186)
- KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.174)
- KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.197)

portfolios: A EV +1.68 (adj +0.82) on $15.95, P(profit) 0.3344, adj growth 7.6 bp · B EV +1.58 (adj +0.93) on $14.57, P(profit) 0.415, adj growth 8.8 bp · C EV +1.00 (adj +0.55) on $10.41, P(profit) 0.7936, adj growth 5.0 bp · R EV +0.13 (adj +0.08) on $3.00, P(profit) 0.9056, adj growth 3.3 bp

## MIN @ SEA  ·  10000 joint draws  ·  440 bet sides mapped, 22 +EV candidates, 4 on card

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
| Minnesota wins by over 2.5 goals NO | 75 | 0.844 | 0.794 | +0.081 | +0.031 | $8.17 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Berkly Catton: 1+ goals YES | 16 | 0.217 | 0.197 | +0.048 | +0.027 | $2.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 2+ goals NO | 88 | 0.919 | 0.908 | +0.032 | +0.021 | $8.17 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Minnesota wins by over 1.5 goals NO | 61 | 0.747 | 0.655 | +0.120 | +0.028 | $3.16 | FUNDED_RESEARCH | $1 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: higher confidence-adjusted growth (12.08 vs 8.79 bp); wins across more scripts (relative breadth 1.025 vs 0.467); relationships: KXNHLGOAL-26OCT24MINSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.097); KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: REINFORCING (phi 0.177); KXNHLSPREAD-26OCT24MINSEA-MIN2|no: DUPLICATIVE (phi 0.738); failure: MIN wins by 2+
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24MINSEA-MIN3|no has the higher standalone adjusted growth (12.08 vs 11.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.097); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24MINSEA-MIN3|no: MOSTLY_INDEPENDENT (phi 0.097); KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLSPREAD-26OCT24MINSEA-MIN2|no: MOSTLY_INDEPENDENT (phi 0.113); failure: SEA offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 2+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24MINSEA-MIN3|no has the higher standalone adjusted growth (12.08 vs 9.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.177); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24MINSEA-MIN3|no: REINFORCING (phi 0.177); KXNHLGOAL-26OCT24MINSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLSPREAD-26OCT24MINSEA-MIN2|no: REINFORCING (phi 0.202); failure: MIN offense succeeds (4+ goals)
- **Minnesota wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-MIN3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT24MINSEA-MIN3|no has the higher standalone adjusted growth (12.08 vs 7.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.738); they share one thesis budget; relationships: KXNHLSPREAD-26OCT24MINSEA-MIN3|no: DUPLICATIVE (phi 0.738); KXNHLGOAL-26OCT24MINSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.113); KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: REINFORCING (phi 0.202); failure: MIN wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:WINS (p 0.5346): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN3|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.4115): highest fidelity KXNHLTEAMTOTAL-26OCT24MINSEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4218): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN3|no (same contract)
- KXNHLSPREAD-26OCT24MINSEA-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2531, phi -0.738)
- KXNHLGOAL-26OCT24MINSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3711, phi -0.194)
- KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3593, phi -0.248)
- KXNHLSPREAD-26OCT24MINSEA-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.2 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2531, phi -1.0)

portfolios: A EV +4.81 (adj +0.99) on $15.95, P(profit) 0.579, adj growth 8.2 bp · B EV +2.53 (adj +1.10) on $22.19, P(profit) 0.7494, adj growth 10.5 bp · C EV +1.28 (adj +0.50) on $12.08, P(profit) 0.8441, adj growth 4.8 bp · R EV +0.62 (adj +0.24) on $7.00, P(profit) 0.7932, adj growth 9.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT24MINSEA-MIN|no == KXNHLGAME-26OCT24MINSEA-SEA|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
