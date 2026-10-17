# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T22:25:52Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +25.02 | +5.75 | +24.66 | 0.800 | -12.21 | -22.68 | 53.16 |
| B thesis-diversified (joint) ← optimiser card | 149.03 | +15.94 | +7.59 | +14.68 | 0.710 | -17.69 | -26.54 | 72.19 |
| C best expression per thesis | 150.01 | +23.34 | +7.11 | +22.65 | 0.770 | -16.17 | -27.17 | 66.08 |
| R FUNDED research stakes | 15.00 | +1.22 | +0.80 | +0.32 | 0.580 | -4.91 | -5.43 | 0.00 |

## NYI @ TOR  ·  10000 joint draws  ·  458 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.551 / away 0.449

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYI_win | p_overtime | goals | shots TOR/NYI | TOR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.53 | 0.47 | 0.00 | 6.0 | 28.1/28.5 | 25.1/24.5 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.106 | 0.46 | 0.54 | 0.00 | 5.95 | 22.0/34.1 | 30.3/18.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.47 | 5.98 | 28.0/28.6 | 25.4/24.6 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.50 | 0.50 | 0.49 | 5.95 | 22.1/34.2 | 30.9/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.54 | 0.46 | 0.00 | 9.28 | 29.4/30.3 | 24.5/23.2 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.075 | 0.48 | 0.52 | 0.00 | 9.2 | 24.0/36.2 | 29.8/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Pelech: 1+ goals YES | 4 | 0.060 | 0.055 | +0.017 | +0.012 | $1.13 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 10 | 0.131 | 0.122 | +0.025 | +0.016 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ assists NO | 71 | 0.768 | 0.737 | +0.044 | +0.012 | $4.89 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Ilya Sorokin: 26+ saves NO | 54 | 0.692 | 0.571 | +0.135 | +0.013 | $3.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYI:NET_LOW_VOLUME | STRUCTURAL (1.00) | CALIBRATION_WARNING | D |
- **Adam Pelech: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17NYITOR-TOR2|no; why: higher confidence-adjusted growth (7.95 vs 0.14 bp); despite a smaller raw edge (+0.017 vs +0.028/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17NYITOR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSAVE-26OCT17NYITOR-NYIISOROKIN30-26|no: MOSTLY_INDEPENDENT (phi 0.004); failure: NYI offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17NYITOR-TOR2|no; why: higher confidence-adjusted growth (5.54 vs 0.14 bp); despite a smaller raw edge (+0.025 vs +0.028/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17NYITOR-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSAVE-26OCT17NYITOR-NYIISOROKIN30-26|no: MOSTLY_INDEPENDENT (phi -0.007); failure: NYI offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NYITOR-TORDRADDYSH43-1|no; why: higher confidence-adjusted growth (1.66 vs 0.73 bp); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17NYITOR-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17NYITOR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSAVE-26OCT17NYITOR-NYIISOROKIN30-26|no: MOSTLY_INDEPENDENT (phi -0.033); failure: TOR offense succeeds (4+ goals)
- **Ilya Sorokin: 26+ saves NO** — thesis: NYI net faces light volume (<= 25 shots; TOR suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT17NYITOR-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT17NYITOR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.033); failure: NYI net faces heavy volume (33+ shots; TOR pressure)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:SUPPRESSED (p 0.3797): highest fidelity KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no (same contract)
- thesis NYI:NET_LOW_VOLUME (p 0.4762): highest fidelity KXNHLSAVE-26OCT17NYITOR-NYIISOROKIN30-26|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT17NYITOR-NYIISOROKIN30-26|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3878): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17NYITOR-NYIAPELECH3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3934, phi -0.1)
- KXNHLGOAL-26OCT17NYITOR-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3934, phi -0.162)
- KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4002, phi -0.222)
- KXNHLSAVE-26OCT17NYITOR-NYIISOROKIN30-26|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.2 pts; fragile player expression; opposing: failure thesis NYI:NET_HIGH_VOLUME (p 0.1335, phi -0.52)

portfolios: A EV +2.40 (adj +0.63) on $15.14, P(profit) 0.6528, adj growth 5.9 bp · B EV +1.96 (adj +0.73) on $11.05, P(profit) 0.6141, adj growth 6.9 bp · C EV +1.66 (adj +0.24) on $12.30, P(profit) 0.5255, adj growth 2.3 bp · R EV +0.41 (adj +0.29) on $1.00, P(profit) 0.0601, adj growth 9.3 bp

## BUF @ MTL  ·  10000 joint draws  ·  414 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.559 / away 0.441

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_BUF_win | p_overtime | goals | shots MTL/BUF | MTL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.55 | 0.45 | 0.00 | 6.03 | 27.3/27.6 | 24.2/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.47 | 5.98 | 27.4/27.8 | 24.6/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.55 | 0.45 | 0.00 | 9.28 | 28.7/29.1 | 23.5/22.2 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.086 | 0.49 | 0.51 | 0.00 | 6.07 | 21.7/32.7 | 28.9/18.3 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.50 | 0.50 | 0.43 | 5.91 | 21.6/32.5 | 29.0/18.4 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.063 | 0.45 | 0.55 | 0.00 | 9.21 | 23.3/34.7 | 27.9/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Owen Power: 1+ goals NO | 87 | 0.904 | 0.894 | +0.026 | +0.016 | $7.85 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Ryan McLeod: 1+ goals YES | 15 | 0.183 | 0.172 | +0.024 | +0.013 | $1.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ assists YES | 33 | 0.398 | 0.361 | +0.052 | +0.016 | $2.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
| Zach Benson: 1+ goals YES | 24 | 0.276 | 0.266 | +0.024 | +0.013 | $1.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFTTHOMPSON72-2|no; why: higher confidence-adjusted growth (5.47 vs 0.12 bp); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.057); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: BUF offense succeeds (4+ goals)
- **Ryan McLeod: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (2.88 vs 2.48 bp); despite a smaller raw edge (+0.024 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.058); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: BUF offense suppressed (<= 2 goals)
- **Zach Benson: 1+ assists YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (2.48 vs 2.01 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.057); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.058); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: BUF offense suppressed (<= 2 goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes has the higher standalone adjusted growth (2.48 vs 2.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.3845): highest fidelity KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3662): highest fidelity KXNHLAST-26OCT17BUFMTL-MTLCKREIDER22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3882): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3845, phi -0.132)
- KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.19)
- KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.299)
- KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.243)

portfolios: A EV +1.34 (adj +0.49) on $15.14, P(profit) 0.4868, adj growth 4.6 bp · B EV +0.94 (adj +0.46) on $13.20, P(profit) 0.5902, adj growth 4.4 bp · C EV +0.70 (adj +0.25) on $7.95, P(profit) 0.398, adj growth 2.3 bp · R EV +0.06 (adj +0.04) on $2.00, P(profit) 0.9039, adj growth 1.4 bp

## SJS @ DET  ·  10000 joint draws  ·  440 bet sides mapped, 14 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.581 / away 0.419

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_SJS_win | p_overtime | goals | shots DET/SJS | DET/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.52 | 0.48 | 0.00 | 5.99 | 27.6/27.3 | 23.9/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.47 | 0.53 | 0.48 | 5.92 | 27.8/27.4 | 24.1/24.6 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.104 | 0.58 | 0.42 | 0.00 | 5.98 | 32.9/21.6 | 18.5/28.8 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.51 | 0.49 | 0.48 | 5.85 | 33.1/22.0 | 18.8/29.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.52 | 0.48 | 0.00 | 9.26 | 29.0/28.8 | 22.9/22.9 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.062 | 0.58 | 0.42 | 0.00 | 9.21 | 34.5/23.4 | 18.4/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nate Danielson: 1+ goals NO | 84 | 0.884 | 0.872 | +0.035 | +0.022 | $7.39 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 69 | 0.809 | 0.729 | +0.104 | +0.024 | $7.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Luca Cagnoni: 1+ assists NO | 69 | 0.761 | 0.721 | +0.056 | +0.016 | $4.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Nate Danielson: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no; why: higher confidence-adjusted growth (8.66 vs 1.87 bp); despite a smaller raw edge (+0.035 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.005 vs 0.89); relationships: KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: DET offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (5.86 vs 4.62 bp); despite a smaller raw edge (+0.104 vs +0.157/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi 0.049); failure: SJS offense succeeds (4+ goals)
- **Luca Cagnoni: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no; why: Player prop expression KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no selected over player prop KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.77 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.049); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.4125): highest fidelity KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no — Player prop expression KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no selected over player prop KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.77 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)
- thesis SJS:OFFENSE_4PLUS (p 0.3648): highest fidelity KXNHLSPREAD-26OCT17SJDET-DET3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17SJDET-SJMMARCHMENT27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.3918): highest fidelity KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no (same contract)
- KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3892, phi -0.152)
- KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.4 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3648, phi -0.212)
- KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3648, phi -0.22)
- override: Player prop expression KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no selected over player prop KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.77 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +3.49 (adj +0.53) on $15.14, P(profit) 0.7452, adj growth 4.9 bp · B EV +1.73 (adj +0.54) on $19.17, P(profit) 0.5525, adj growth 5.2 bp · C EV +3.02 (adj +0.61) on $13.73, P(profit) 0.6648, adj growth 5.6 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.884, adj growth 2.1 bp

## OTT @ PHI  ·  10000 joint draws  ·  460 bet sides mapped, 10 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.416 / away 0.584

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_OTT_win | p_overtime | goals | shots PHI/OTT | PHI/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.49 | 0.51 | 0.00 | 5.99 | 25.6/26.1 | 22.5/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.47 | 5.93 | 25.6/26.2 | 22.9/22.3 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.099 | 0.40 | 0.60 | 0.00 | 5.95 | 20.5/31.4 | 27.2/17.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.45 | 0.55 | 0.49 | 5.8 | 20.7/31.5 | 28.1/17.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.066 | 0.50 | 0.50 | 0.00 | 3.41 | 24.5/25.0 | 23.0/22.7 | even strength |
| OTT shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.49 | 0.51 | 0.49 | 2.76 | 19.0/29.7 | 28.2/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drake Batherson: 1+ goals NO | 68 | 0.739 | 0.723 | +0.044 | +0.028 | $6.64 | FUNDED_RESEARCH | $2 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 78 | 0.822 | 0.810 | +0.030 | +0.018 | $7.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Dylan Cozens: 1+ goals NO | 72 | 0.763 | 0.751 | +0.029 | +0.017 | $5.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Drake Batherson: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no; why: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no has the higher standalone adjusted growth (8.32 vs 8.05 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.205); relationships: KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: OTT offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-PHIPMARTONE94-1|no; why: higher confidence-adjusted growth (4.60 vs 0.04 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0017 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense succeeds (4+ goals)
- **Dylan Cozens: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no; why: Player prop expression KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.87 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.4466): highest fidelity KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no — Player prop expression KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.87 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:SUPPRESSED (p 0.4749): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis PHI:OFFENSE_4PLUS (p 0.3027): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3398, phi -0.233)
- KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3027, phi -0.183)
- KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3398, phi -0.223)
- override: Player prop expression KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.87 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.31 (adj +0.57) on $15.14, P(profit) 0.626, adj growth 5.5 bp · B EV +0.89 (adj +0.55) on $18.86, P(profit) 0.4643, adj growth 5.3 bp · C EV +0.93 (adj +0.30) on $11.62, P(profit) 0.9176, adj growth 2.9 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.7391, adj growth 3.1 bp

## NYR @ CBJ  ·  10000 joint draws  ·  418 bet sides mapped, 8 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.551 / away 0.449

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_NYR_win | p_overtime | goals | shots CBJ/NYR | CBJ/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.62 | 0.38 | 0.00 | 6.01 | 26.8/26.2 | 23.2/22.7 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.109 | 0.66 | 0.34 | 0.00 | 5.96 | 32.1/20.9 | 18.1/27.8 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.55 | 0.45 | 0.49 | 5.87 | 32.5/21.3 | 18.1/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.51 | 0.49 | 0.49 | 5.92 | 26.9/26.5 | 23.3/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.56 | 0.44 | 0.00 | 9.15 | 28.2/27.7 | 22.2/22.0 | even strength |
| CBJ shot control · high event (8+) · decided (2+) | 0.069 | 0.66 | 0.34 | 0.00 | 9.18 | 33.7/22.2 | 17.6/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Danton Heinen: 1+ goals YES | 11 | 0.136 | 0.127 | +0.019 | +0.010 | $1.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Will Cuylle: 1+ goals NO | 78 | 0.813 | 0.803 | +0.021 | +0.011 | $5.54 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 69 | 0.728 | 0.716 | +0.023 | +0.011 | $3.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (2.23 vs 1.65 bp); despite a smaller raw edge (+0.019 vs +0.021/contract); relationships: KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Will Cuylle: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no; why: Player prop expression KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no selected over player prop KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.90 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17NYRCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: NYR offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no; why: Player prop expression KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no selected over player prop KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.85 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17NYRCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYR:SUPPRESSED (p 0.4701): highest fidelity KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no — Player prop expression KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no selected over player prop KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.90 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis GAME:LOW_EVENT (p 0.263): highest fidelity KXNHLTOTAL-26OCT17NYRCBJ-4|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT17NYRCBJ-4|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.4038): highest fidelity KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes (same contract)
- KXNHLGOAL-26OCT17NYRCBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3685, phi -0.165)
- KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3121, phi -0.215)
- KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3121, phi -0.228)
- override: Player prop expression KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no selected over player prop KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.90 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no selected over player prop KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.85 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.52 (adj +0.50) on $15.14, P(profit) 0.474, adj growth 4.5 bp · B EV +0.45 (adj +0.23) on $10.37, P(profit) 0.6422, adj growth 2.2 bp · C EV +2.02 (adj +0.98) on $11.39, P(profit) 0.3837, adj growth 9.0 bp · R EV +0.05 (adj +0.03) on $2.00, P(profit) 0.8126, adj growth 1.1 bp

## DAL @ CHI  ·  10000 joint draws  ·  428 bet sides mapped, 25 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.344 / away 0.656

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_DAL_win | p_overtime | goals | shots CHI/DAL | CHI/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.48 | 0.52 | 0.00 | 5.98 | 25.6/26.0 | 22.5/22.2 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.109 | 0.39 | 0.61 | 0.00 | 5.99 | 20.0/30.8 | 26.5/17.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.47 | 0.53 | 0.46 | 5.91 | 25.7/26.2 | 22.8/22.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.46 | 0.54 | 0.47 | 5.91 | 20.3/31.2 | 27.9/17.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.49 | 0.51 | 0.00 | 9.32 | 27.2/27.7 | 21.7/21.4 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.064 | 0.36 | 0.64 | 0.00 | 9.13 | 21.5/32.5 | 25.5/16.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anton Frondell: 1+ goals YES | 19 | 0.247 | 0.231 | +0.047 | +0.030 | $3.36 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Frank Nazar: 1+ goals YES | 19 | 0.241 | 0.227 | +0.041 | +0.027 | $3.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 24 | 0.295 | 0.280 | +0.042 | +0.027 | $3.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 11 | 0.148 | 0.135 | +0.032 | +0.018 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes; why: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes has the higher standalone adjusted growth (13.24 vs 11.99 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.212); relationships: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: CHI offense suppressed (<= 2 goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes; why: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes has the higher standalone adjusted growth (13.24 vs 9.54 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.219); relationships: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes; why: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes has the higher standalone adjusted growth (13.24 vs 8.52 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.232); relationships: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CHI offense suppressed (<= 2 goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes; why: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes has the higher standalone adjusted growth (13.24 vs 6.91 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.186); relationships: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3529): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.2507): highest fidelity KXNHLSPREAD-26OCT17DALCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes (same contract)
- thesis CHI:WINS (p 0.4708): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.246)
- KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.247)
- KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.259)
- KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.195)

portfolios: A EV +3.03 (adj +0.57) on $15.14, P(profit) 0.6154, adj growth 5.3 bp · B EV +2.45 (adj +1.55) on $11.59, P(profit) 0.6549, adj growth 14.7 bp · C EV +5.17 (adj +1.66) on $23.46, P(profit) 0.606, adj growth 15.4 bp · R EV +0.23 (adj +0.15) on $1.00, P(profit) 0.2475, adj growth 5.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17DALCHI-DAL|no == KXNHLGAME-26OCT17DALCHI-CHI|yes

## STL @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.497 / away 0.503

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_STL_win | p_overtime | goals | shots NSH/STL | NSH/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.48 | 0.52 | 0.00 | 6.04 | 27.3/27.5 | 23.7/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.49 | 5.97 | 27.5/27.5 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.50 | 0.50 | 0.00 | 9.39 | 29.1/29.0 | 22.9/22.8 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.068 | 0.47 | 0.53 | 0.00 | 6.0 | 21.6/31.9 | 27.9/18.4 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.068 | 0.59 | 0.41 | 0.00 | 5.98 | 32.2/21.8 | 18.7/28.2 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.57 | 0.43 | 0.46 | 5.92 | 32.3/22.0 | 18.7/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Wilsby: 1+ goals YES | 5 | 0.071 | 0.065 | +0.017 | +0.012 | $1.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 24 | 0.284 | 0.272 | +0.031 | +0.019 | $2.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 27 | 0.313 | 0.301 | +0.029 | +0.017 | $2.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Dalibor Dvorsky: 1+ goals NO | 82 | 0.849 | 0.841 | +0.019 | +0.011 | $6.49 | FUNDED_RESEARCH | $2 | STL:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (6.21 vs 3.12 bp); despite a smaller raw edge (+0.017 vs +0.029/contract); relationships: KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17STLNSH-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: NSH offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17STLNSH-STLJNEIGHBOURS63-1|yes; why: higher confidence-adjusted growth (4.02 vs 1.50 bp); despite a smaller raw edge (+0.031 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17STLNSH-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: STL offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT17STLNSH-9|yes; why: higher confidence-adjusted growth (3.12 vs 0.94 bp); despite a smaller raw edge (+0.029 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.931 vs 0.376); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17STLNSH-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NSH offense suppressed (<= 2 goals)
- **Dalibor Dvorsky: 1+ goals NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17STLNSH-STLMMCTAVISH83-1|no; why: higher confidence-adjusted growth (1.71 vs 0.33 bp); despite a smaller raw edge (+0.019 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4049): highest fidelity KXNHLAST-26OCT17STLNSH-STLJNEIGHBOURS63-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.4176): highest fidelity KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes (same contract)
- thesis STL:SUPPRESSED (p 0.3808): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3659, phi -0.106)
- KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3808, phi -0.248)
- KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3659, phi -0.249)
- KXNHLGOAL-26OCT17STLNSH-STLDDVORSKY15-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4049, phi -0.177)

portfolios: A EV +2.12 (adj +0.78) on $13.73, P(profit) 0.4219, adj growth 6.8 bp · B EV +1.05 (adj +0.66) on $12.33, P(profit) 0.4843, adj growth 6.2 bp · C EV +0.77 (adj +0.46) on $6.89, P(profit) 0.5078, adj growth 4.3 bp · R EV +0.05 (adj +0.03) on $2.00, P(profit) 0.8494, adj growth 0.9 bp

## BOS @ LAK  ·  10000 joint draws  ·  416 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.555 / away 0.445

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BOS_win | p_overtime | goals | shots LAK/BOS | LAK/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.55 | 0.45 | 0.00 | 5.96 | 28.1/27.5 | 24.1/24.4 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.111 | 0.63 | 0.37 | 0.00 | 5.93 | 33.3/21.8 | 19.0/29.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.47 | 5.92 | 28.1/27.7 | 24.5/24.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.53 | 0.47 | 0.42 | 5.84 | 33.5/22.0 | 18.7/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.55 | 0.45 | 0.00 | 9.18 | 29.3/29.0 | 23.3/22.9 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.062 | 0.64 | 0.36 | 0.00 | 9.19 | 34.9/23.4 | 18.5/27.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Artemi Panarin: 1+ assists NO | 48 | 0.605 | 0.520 | +0.108 | +0.023 | $3.45 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Charlie McAvoy: 1+ assists NO | 59 | 0.675 | 0.627 | +0.068 | +0.020 | $6.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Artemi Panarin: 2+ assists NO | 84 | 0.908 | 0.864 | +0.058 | +0.015 | $7.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Elias Lindholm: 1+ goals YES | 20 | 0.233 | 0.222 | +0.022 | +0.011 | $1.72 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (4.65 vs 3.63 bp); relationships: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no: DUPLICATIVE (phi 0.394); KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: LAK offense succeeds (4+ goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17BOSLA-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (3.81 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.173); failure: BOS offense succeeds (4+ goals)
- **Artemi Panarin: 2+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no; why: second expression of the same thesis: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no has the higher standalone adjusted growth (4.65 vs 3.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.394); they share one thesis budget; relationships: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no: DUPLICATIVE (phi 0.394); KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: LAK offense succeeds (4+ goals)
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes; why: KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes has the higher standalone adjusted growth (1.71 vs 1.64 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.082); relationships: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.173); KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi 0.017); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis LAK:SUPPRESSED (p 0.3978): highest fidelity KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.4519): highest fidelity KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.3292): highest fidelity KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes (same contract)
- KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.0 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3926, phi -0.29)
- KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3292, phi -0.254)
- KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3926, phi -0.25)
- KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4519, phi -0.24)

portfolios: A EV +2.33 (adj +0.54) on $15.14, P(profit) 0.5959, adj growth 5.1 bp · B EV +2.14 (adj +0.59) on $19.08, P(profit) 0.68, adj growth 5.6 bp · C EV +2.93 (adj +0.71) on $17.53, P(profit) 0.5613, adj growth 6.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ UTA  ·  10000 joint draws  ·  436 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.561 / away 0.439

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_EDM_win | p_overtime | goals | shots UTA/EDM | UTA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.53 | 0.47 | 0.00 | 6.05 | 27.4/27.3 | 23.9/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.118 | 0.54 | 0.46 | 0.00 | 9.51 | 29.2/29.1 | 23.2/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.47 | 6.04 | 27.8/27.7 | 24.3/24.3 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.075 | 0.59 | 0.41 | 0.00 | 6.09 | 32.6/21.8 | 18.7/28.0 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.064 | 0.62 | 0.38 | 0.00 | 9.52 | 34.0/23.2 | 18.0/26.3 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.53 | 0.47 | 0.49 | 6.05 | 32.7/22.0 | 18.7/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nate Schmidt: 1+ goals YES | 4 | 0.067 | 0.059 | +0.024 | +0.016 | $1.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 71 | 0.798 | 0.751 | +0.073 | +0.027 | $7.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ goals YES | 8 | 0.110 | 0.101 | +0.025 | +0.016 | $1.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Zach Hyman: 1+ goals YES | 31 | 0.358 | 0.345 | +0.033 | +0.020 | $3.54 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Nate Schmidt: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (13.17 vs 1.95 bp); relationships: KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: UTA offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (8.04 vs 1.32 bp); relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.218); failure: EDM offense succeeds (4+ goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (7.00 vs 5.23 bp); despite a smaller raw edge (+0.025 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: EDM offense suppressed (<= 2 goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes; why: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.51 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.218); KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:SUPPRESSED (p 0.3535): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.4295): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes — Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.51 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis UTA:OFFENSE_4PLUS (p 0.4702): highest fidelity KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes (same contract)
- KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3208, phi -0.107)
- KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4295, phi -0.328)
- KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3535, phi -0.149)
- KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3535, phi -0.271)
- override: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.51 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +3.37 (adj +0.71) on $15.14, P(profit) 0.5682, adj growth 6.6 bp · B EV +2.43 (adj +1.35) on $14.50, P(profit) 0.3772, adj growth 12.8 bp · C EV +2.71 (adj +1.01) on $23.56, P(profit) 0.7383, adj growth 9.5 bp · R EV +0.10 (adj +0.06) on $1.00, P(profit) 0.358, adj growth 2.3 bp

## PIT @ VGK  ·  10000 joint draws  ·  424 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.643 / away 0.357

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_PIT_win | p_overtime | goals | shots VGK/PIT | VGK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.69 | 0.31 | 0.00 | 6.04 | 27.7/27.5 | 24.8/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.71 | 0.29 | 0.00 | 9.35 | 29.1/28.8 | 23.9/21.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.55 | 0.45 | 0.46 | 6.0 | 27.6/27.4 | 24.1/24.2 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.094 | 0.74 | 0.26 | 0.00 | 6.02 | 32.4/21.6 | 19.2/27.6 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.56 | 0.44 | 0.48 | 5.93 | 32.3/21.7 | 18.6/28.7 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.067 | 0.77 | 0.23 | 0.00 | 9.33 | 34.2/23.0 | 18.8/25.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 68 | 0.734 | 0.720 | +0.039 | +0.024 | $7.85 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Evgeni Malkin: 1+ assists NO | 63 | 0.716 | 0.670 | +0.069 | +0.024 | $7.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.084 | 0.075 | +0.020 | +0.011 | $1.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:WINS_BY_2PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Bryan Rust: 1+ goals YES | 24 | 0.286 | 0.272 | +0.033 | +0.019 | $2.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17PITVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (6.14 vs 2.03 bp); despite a smaller raw edge (+0.039 vs +0.125/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: VGK offense succeeds (4+ goals)
- **Evgeni Malkin: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17PITVGK-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (5.50 vs 1.87 bp); relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: PIT offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK wins by 2+; alternative: KXNHLPTS-26OCT17PITVGK-PITEMALKIN71-1|no; why: higher confidence-adjusted growth (4.54 vs 0.00 bp); despite a smaller raw edge (+0.020 vs +0.064/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: VGK offense suppressed (<= 2 goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17PITVGK-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (4.26 vs 0.86 bp); alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:SUPPRESSED (p 0.4708): highest fidelity KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.3109): highest fidelity KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.2823): highest fidelity KXNHLPTS-26OCT17PITVGK-VGKJEICHEL9-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17PITVGK-VGKJEICHEL9-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5155, phi -0.202)
- KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3109, phi -0.225)
- KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2823, phi -0.1)
- KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4708, phi -0.264)

portfolios: A EV +3.10 (adj +0.43) on $15.14, P(profit) 0.6271, adj growth 4.0 bp · B EV +1.90 (adj +0.93) on $18.88, P(profit) 0.6713, adj growth 8.9 bp · C EV +3.42 (adj +0.89) on $21.58, P(profit) 0.7052, adj growth 8.3 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.7344, adj growth 2.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
