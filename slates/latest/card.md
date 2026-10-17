# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T21:38:41Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.97 | +22.87 | +5.23 | +22.85 | 0.795 | -12.35 | -21.70 | 48.73 |
| B thesis-diversified (joint) ← optimiser card | 149.01 | +16.37 | +8.38 | +15.05 | 0.719 | -17.51 | -26.57 | 79.92 |
| C best expression per thesis | 150.00 | +20.62 | +7.32 | +19.85 | 0.751 | -17.19 | -27.45 | 68.88 |
| R FUNDED research stakes | 17.00 | +1.49 | +0.98 | +0.68 | 0.543 | -5.29 | -6.97 | 0.00 |

## SEA @ FLA  ·  10000 joint draws  ·  418 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.629 / away 0.371

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_SEA_win | p_overtime | goals | shots FLA/SEA | FLA/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.50 | 0.50 | 0.00 | 6.02 | 27.2/26.9 | 23.2/23.7 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.108 | 0.58 | 0.42 | 0.00 | 6.0 | 32.9/21.5 | 18.5/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.49 | 5.94 | 27.5/27.1 | 23.7/24.2 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.55 | 0.45 | 0.49 | 5.91 | 33.0/21.6 | 18.5/29.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.57 | 0.43 | 0.00 | 9.4 | 29.3/28.8 | 23.2/22.8 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.071 | 0.57 | 0.43 | 0.00 | 9.29 | 34.9/23.1 | 17.8/27.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 10 | 0.148 | 0.135 | +0.042 | +0.028 | $2.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 63 | 0.709 | 0.688 | +0.062 | +0.041 | $7.29 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 11 | 0.155 | 0.142 | +0.038 | +0.025 | $2.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 15 | 0.193 | 0.178 | +0.034 | +0.019 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes; why: higher confidence-adjusted growth (17.95 vs 12.66 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (16.50 vs 13.39 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: FLA offense succeeds (4+ goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes; why: higher confidence-adjusted growth (12.66 vs 7.37 bp); despite a smaller raw edge (+0.038 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.906 vs 0.535); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes has the higher standalone adjusted growth (12.66 vs 6.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis FLA:SUPPRESSED (p 0.3867): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.3753): highest fidelity KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2633): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes (same contract)
- KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.183)
- KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4008, phi -0.247)
- KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.205)
- KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.198)

portfolios: A EV +2.16 (adj +0.35) on $13.75, P(profit) 0.6281, adj growth 3.1 bp · B EV +2.84 (adj +1.85) on $13.97, P(profit) 0.3767, adj growth 17.6 bp · C EV +2.60 (adj +1.52) on $15.29, P(profit) 0.7518, adj growth 14.3 bp · R EV +0.19 (adj +0.13) on $2.00, P(profit) 0.7086, adj growth 5.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17SEAFLA-SEA|yes == KXNHLGAME-26OCT17SEAFLA-FLA|no

## NYI @ TOR  ·  10000 joint draws  ·  458 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.554 / away 0.446

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
| Jean-Gabriel Pageau: 1+ goals YES | 14 | 0.166 | 0.159 | +0.018 | +0.010 | $1.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ assists NO | 71 | 0.768 | 0.737 | +0.044 | +0.012 | $4.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Ilya Sorokin: 26+ saves NO | 54 | 0.692 | 0.571 | +0.135 | +0.013 | $3.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYI:NET_LOW_VOLUME | STRUCTURAL (1.00) | CALIBRATION_WARNING | D |
| Auston Matthews: 1+ goals NO | 58 | 0.620 | 0.608 | +0.022 | +0.011 | $2.43 | FUNDED_RESEARCH | $1 | TOR:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17NYITOR-TOR2|no; why: higher confidence-adjusted growth (1.76 vs 0.14 bp); despite a smaller raw edge (+0.018 vs +0.028/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSAVE-26OCT17NYITOR-NYIISOROKIN30-26|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26OCT17NYITOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: NYI offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17NYITOR-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (1.66 vs 1.17 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT17NYITOR-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSAVE-26OCT17NYITOR-NYIISOROKIN30-26|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT17NYITOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.113); failure: TOR offense succeeds (4+ goals)
- **Ilya Sorokin: 26+ saves NO** — thesis: NYI net faces light volume (<= 25 shots; TOR suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT17NYITOR-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT17NYITOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.047); failure: NYI net faces heavy volume (33+ shots; TOR pressure)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no; why: second expression of the same thesis: KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no has the higher standalone adjusted growth (1.66 vs 1.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.113); they share one thesis budget; relationships: KXNHLGOAL-26OCT17NYITOR-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLSAVE-26OCT17NYITOR-NYIISOROKIN30-26|no: MOSTLY_INDEPENDENT (phi -0.047); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:SUPPRESSED (p 0.3797): highest fidelity KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no (same contract)
- thesis NYI:NET_LOW_VOLUME (p 0.4762): highest fidelity KXNHLSAVE-26OCT17NYITOR-NYIISOROKIN30-26|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT17NYITOR-NYIISOROKIN30-26|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3878): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17NYITOR-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3934, phi -0.184)
- KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4002, phi -0.222)
- KXNHLSAVE-26OCT17NYITOR-NYIISOROKIN30-26|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.2 pts; fragile player expression; opposing: failure thesis NYI:NET_HIGH_VOLUME (p 0.1335, phi -0.52)
- KXNHLGOAL-26OCT17NYITOR-TORAMATTHEWS34-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4002, phi -0.282)

portfolios: A EV +1.68 (adj +0.33) on $13.75, P(profit) 0.6688, adj growth 3.1 bp · B EV +1.29 (adj +0.27) on $11.04, P(profit) 0.6036, adj growth 2.6 bp · C EV +1.47 (adj +0.21) on $10.90, P(profit) 0.5255, adj growth 2.0 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6195, adj growth 0.7 bp

## BUF @ MTL  ·  10000 joint draws  ·  414 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.557 / away 0.443

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
| Owen Power: 1+ goals NO | 87 | 0.904 | 0.894 | +0.026 | +0.016 | $7.29 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Ryan McLeod: 1+ goals YES | 15 | 0.183 | 0.172 | +0.024 | +0.013 | $1.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 24 | 0.276 | 0.266 | +0.024 | +0.013 | $1.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ goals NO | 58 | 0.621 | 0.609 | +0.024 | +0.012 | $2.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFTTHOMPSON72-2|no; why: higher confidence-adjusted growth (5.47 vs 0.12 bp); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: BUF offense succeeds (4+ goals)
- **Ryan McLeod: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (2.88 vs 2.01 bp); relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: BUF offense suppressed (<= 2 goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17BUFMTL-BUFOPOWER25-1|yes; why: higher confidence-adjusted growth (2.01 vs 1.60 bp); despite a smaller raw edge (+0.024 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: BUF offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BUFMTL-MTLCKREIDER22-1|no; why: higher confidence-adjusted growth (1.39 vs 1.14 bp); despite a smaller raw edge (+0.024 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.3845): highest fidelity KXNHLAST-26OCT17BUFMTL-BUFOPOWER25-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT17BUFMTL-BUFOPOWER25-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3662): highest fidelity KXNHLAST-26OCT17BUFMTL-MTLCKREIDER22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3882): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3845, phi -0.132)
- KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.19)
- KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.243)
- KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4184, phi -0.264)

portfolios: A EV +1.14 (adj +0.39) on $13.75, P(profit) 0.5263, adj growth 3.7 bp · B EV +0.68 (adj +0.39) on $12.96, P(profit) 0.3862, adj growth 3.7 bp · C EV +0.36 (adj +0.20) on $6.17, P(profit) 0.7247, adj growth 1.8 bp · R EV +0.06 (adj +0.04) on $2.00, P(profit) 0.9039, adj growth 1.4 bp

## SJS @ DET  ·  10000 joint draws  ·  440 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.578 / away 0.422

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
| Nate Danielson: 1+ goals NO | 84 | 0.884 | 0.872 | +0.035 | +0.022 | $6.42 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 70 | 0.809 | 0.732 | +0.095 | +0.017 | $5.49 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Luca Cagnoni: 1+ assists NO | 70 | 0.761 | 0.728 | +0.047 | +0.013 | $3.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Dylan Larkin: 1+ goals NO | 64 | 0.679 | 0.668 | +0.022 | +0.012 | $2.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Nate Danielson: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no; why: higher confidence-adjusted growth (8.66 vs 1.87 bp); despite a smaller raw edge (+0.035 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.005 vs 0.89); relationships: KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT17SJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: DET offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no; why: KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no has the higher standalone adjusted growth (4.62 vs 3.13 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.049); relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26OCT17SJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: SJS offense succeeds (4+ goals)
- **Luca Cagnoni: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no; why: Player prop expression KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no selected over player prop KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.88 vs 0.77 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26OCT17SJDET-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: SJS offense succeeds (4+ goals)
- **Dylan Larkin: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no; why: Player prop expression KXNHLGOAL-26OCT17SJDET-DETDLARKIN71-1|no selected over broad KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.4125): highest fidelity KXNHLPTS-26OCT17SJDET-SJMCELEBRINI71-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no — Player prop expression KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no selected over player prop KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.88 vs 0.77 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)
- thesis DET:SUPPRESSED (p 0.3918): highest fidelity KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no (same contract)
- thesis SJS:WINS (p 0.4876): highest fidelity KXNHLSPREAD-26OCT17SJDET-DET3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3892, phi -0.152)
- KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.9 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3648, phi -0.212)
- KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3648, phi -0.22)
- KXNHLGOAL-26OCT17SJDET-DETDLARKIN71-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3892, phi -0.26)
- override: Player prop expression KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no selected over player prop KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.88 vs 0.77 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT17SJDET-DETDLARKIN71-1|no selected over broad KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.65 (adj +0.42) on $13.75, P(profit) 0.6359, adj growth 4.0 bp · B EV +1.32 (adj +0.42) on $18.23, P(profit) 0.6661, adj growth 4.0 bp · C EV +2.60 (adj +0.45) on $14.38, P(profit) 0.4672, adj growth 4.2 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.884, adj growth 2.1 bp

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
| Drake Batherson: 1+ goals NO | 68 | 0.739 | 0.723 | +0.044 | +0.028 | $6.17 | FUNDED_RESEARCH | $2 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 78 | 0.822 | 0.810 | +0.030 | +0.018 | $6.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Dylan Cozens: 1+ goals NO | 72 | 0.763 | 0.751 | +0.029 | +0.017 | $4.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Drake Batherson: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no; why: higher confidence-adjusted growth (8.05 vs 5.52 bp); despite a smaller raw edge (+0.044 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: OTT offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-PHIPMARTONE94-1|no; why: higher confidence-adjusted growth (4.60 vs 0.04 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0017 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense succeeds (4+ goals)
- **Dylan Cozens: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no; why: Player prop expression KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.87 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.4466): highest fidelity KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no — Player prop expression KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.87 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:SUPPRESSED (p 0.4749): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3398, phi -0.233)
- KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3027, phi -0.183)
- KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3398, phi -0.223)
- override: Player prop expression KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.87 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.04 (adj +0.46) on $13.75, P(profit) 0.626, adj growth 4.5 bp · B EV +0.83 (adj +0.51) on $17.51, P(profit) 0.4643, adj growth 4.9 bp · C EV +0.65 (adj +0.41) on $10.29, P(profit) 0.7391, adj growth 3.9 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.7391, adj growth 3.1 bp

## NYR @ CBJ  ·  10000 joint draws  ·  418 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.548 / away 0.452

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
| Danton Heinen: 1+ goals YES | 11 | 0.136 | 0.127 | +0.019 | +0.010 | $1.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Will Cuylle: 1+ goals NO | 78 | 0.813 | 0.803 | +0.021 | +0.011 | $5.12 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 17 | 0.201 | 0.191 | +0.021 | +0.011 | $1.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 69 | 0.728 | 0.716 | +0.023 | +0.011 | $3.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (2.23 vs 1.65 bp); despite a smaller raw edge (+0.019 vs +0.021/contract); relationships: KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Will Cuylle: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no; why: Player prop expression KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no selected over player prop KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.90 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17NYRCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: NYR offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17NYRCBJ-CBJKJOHNSON91-1|yes; why: higher confidence-adjusted growth (1.65 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT17NYRCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CBJ offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no; why: Player prop expression KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no selected over player prop KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.85 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17NYRCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYR:SUPPRESSED (p 0.4701): highest fidelity KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no — Player prop expression KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no selected over player prop KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.90 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis GAME:LOW_EVENT (p 0.263): highest fidelity KXNHLTOTAL-26OCT17NYRCBJ-4|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT17NYRCBJ-4|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.4038): highest fidelity KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes (same contract)
- KXNHLGOAL-26OCT17NYRCBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3685, phi -0.165)
- KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3121, phi -0.215)
- KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3685, phi -0.21)
- KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3121, phi -0.228)
- override: Player prop expression KXNHLGOAL-26OCT17NYRCBJ-NYRWCUYLLE50-1|no selected over player prop KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.90 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no selected over player prop KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.85 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.38 (adj +0.45) on $13.75, P(profit) 0.474, adj growth 4.2 bp · B EV +0.54 (adj +0.28) on $10.64, P(profit) 0.7015, adj growth 2.7 bp · C EV +1.09 (adj +0.38) on $8.28, P(profit) 0.7451, adj growth 3.6 bp · R EV +0.05 (adj +0.03) on $2.00, P(profit) 0.8126, adj growth 1.1 bp

## DAL @ CHI  ·  10000 joint draws  ·  422 bet sides mapped, 20 +EV candidates, 4 on card

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
| Anton Frondell: 1+ goals YES | 19 | 0.247 | 0.231 | +0.047 | +0.030 | $3.12 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Frank Nazar: 1+ goals YES | 19 | 0.241 | 0.227 | +0.041 | +0.027 | $2.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 24 | 0.295 | 0.280 | +0.042 | +0.027 | $3.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 11 | 0.148 | 0.135 | +0.032 | +0.018 | $1.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
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

portfolios: A EV +2.61 (adj +0.56) on $13.75, P(profit) 0.5739, adj growth 5.0 bp · B EV +2.27 (adj +1.44) on $10.77, P(profit) 0.6549, adj growth 13.7 bp · C EV +3.23 (adj +1.18) on $13.93, P(profit) 0.8146, adj growth 11.0 bp · R EV +0.23 (adj +0.15) on $1.00, P(profit) 0.2475, adj growth 5.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17DALCHI-DAL|no == KXNHLGAME-26OCT17DALCHI-CHI|yes

## STL @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

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
| Adam Wilsby: 1+ goals YES | 5 | 0.071 | 0.065 | +0.017 | +0.012 | $1.07 | FUNDED_RESEARCH | $1 | NSH:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 24 | 0.284 | 0.272 | +0.031 | +0.019 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 27 | 0.313 | 0.301 | +0.029 | +0.017 | $2.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Matthew Wood: 1+ goals YES | 19 | 0.221 | 0.212 | +0.020 | +0.011 | $1.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (6.21 vs 3.12 bp); despite a smaller raw edge (+0.017 vs +0.029/contract); relationships: KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17STLNSH-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: NSH offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17STLNSH-STLJNEIGHBOURS63-1|yes; why: higher confidence-adjusted growth (4.02 vs 1.50 bp); despite a smaller raw edge (+0.031 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17STLNSH-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: STL offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT17STLNSH-9|yes; why: higher confidence-adjusted growth (3.12 vs 0.94 bp); despite a smaller raw edge (+0.029 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.931 vs 0.376); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17STLNSH-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: NSH offense suppressed (<= 2 goals)
- **Matthew Wood: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes has the higher standalone adjusted growth (3.12 vs 1.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4049): highest fidelity KXNHLAST-26OCT17STLNSH-STLJNEIGHBOURS63-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.4176): highest fidelity KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes (same contract)
- KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3659, phi -0.106)
- KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3808, phi -0.248)
- KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3659, phi -0.249)
- KXNHLGOAL-26OCT17STLNSH-NSHMWOOD71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3659, phi -0.204)

portfolios: A EV +1.93 (adj +0.70) on $12.47, P(profit) 0.4219, adj growth 6.3 bp · B EV +0.96 (adj +0.61) on $6.67, P(profit) 0.5432, adj growth 5.8 bp · C EV +0.69 (adj +0.41) on $6.10, P(profit) 0.5078, adj growth 3.8 bp · R EV +0.32 (adj +0.23) on $1.00, P(profit) 0.0706, adj growth 7.3 bp

## BOS @ LAK  ·  10000 joint draws  ·  416 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.553 / away 0.447

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
| Charlie McAvoy: 1+ assists NO | 59 | 0.675 | 0.627 | +0.068 | +0.020 | $5.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Artemi Panarin: 2+ assists NO | 84 | 0.908 | 0.864 | +0.058 | +0.015 | $7.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Hampus Lindholm: 1+ assists YES | 25 | 0.321 | 0.278 | +0.058 | +0.015 | $1.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| Elias Lindholm: 1+ goals YES | 20 | 0.233 | 0.222 | +0.022 | +0.011 | $1.50 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17BOSLA-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (3.81 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.173); failure: BOS offense succeeds (4+ goals)
- **Artemi Panarin: 2+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (3.63 vs 2.32 bp); despite a smaller raw edge (+0.058 vs +0.098/contract); relationships: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: LAK offense succeeds (4+ goals)
- **Hampus Lindholm: 1+ assists YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (2.47 vs 1.64 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.082); failure: BOS offense suppressed (<= 2 goals)
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes has the higher standalone adjusted growth (2.47 vs 1.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.082); they share one thesis budget; relationships: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.173); KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi 0.082); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BOS:SUPPRESSED (p 0.4519): highest fidelity KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no (same contract)
- thesis LAK:SUPPRESSED (p 0.3978): highest fidelity KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.3292): highest fidelity KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes (same contract)
- KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3292, phi -0.254)
- KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3926, phi -0.25)
- KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4519, phi -0.271)
- KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4519, phi -0.24)

portfolios: A EV +2.04 (adj +0.42) on $13.75, P(profit) 0.5992, adj growth 3.9 bp · B EV +1.67 (adj +0.49) on $16.29, P(profit) 0.6621, adj growth 4.7 bp · C EV +2.47 (adj +0.63) on $21.89, P(profit) 0.6545, adj growth 6.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ UTA  ·  10000 joint draws  ·  436 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.559 / away 0.441

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
| Nate Schmidt: 1+ goals YES | 4 | 0.067 | 0.059 | +0.024 | +0.016 | $1.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 71 | 0.798 | 0.751 | +0.073 | +0.027 | $7.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Zach Hyman: 1+ goals YES | 30 | 0.358 | 0.342 | +0.043 | +0.028 | $4.22 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 8 | 0.110 | 0.101 | +0.025 | +0.016 | $1.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Nate Schmidt: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (13.17 vs 1.95 bp); relationships: KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: UTA offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (8.04 vs 3.60 bp); relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.218); KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.106); failure: EDM offense succeeds (4+ goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (7.66 vs 6.98 bp); despite a smaller raw edge (+0.043 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.218); KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes has the higher standalone adjusted growth (7.66 vs 7.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:SUPPRESSED (p 0.3535): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.4295): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.4702): highest fidelity KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes (same contract)
- KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3208, phi -0.107)
- KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4295, phi -0.328)
- KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3535, phi -0.271)
- KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3535, phi -0.149)

portfolios: A EV +2.43 (adj +0.74) on $13.75, P(profit) 0.5682, adj growth 7.1 bp · B EV +2.51 (adj +1.43) on $14.40, P(profit) 0.3772, adj growth 13.6 bp · C EV +2.25 (adj +1.10) on $22.78, P(profit) 0.468, adj growth 10.4 bp · R EV +0.28 (adj +0.18) on $2.00, P(profit) 0.358, adj growth 6.3 bp

## PIT @ VGK  ·  10000 joint draws  ·  424 bet sides mapped, 10 +EV candidates, 3 on card

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
| Mitch Marner: 1+ goals NO | 68 | 0.734 | 0.720 | +0.039 | +0.024 | $7.29 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Evgeni Malkin: 1+ assists NO | 63 | 0.716 | 0.670 | +0.069 | +0.024 | $6.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Bryan Rust: 1+ goals YES | 24 | 0.286 | 0.272 | +0.033 | +0.019 | $2.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17PITVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (6.14 vs 2.03 bp); despite a smaller raw edge (+0.039 vs +0.125/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: VGK offense succeeds (4+ goals)
- **Evgeni Malkin: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17PITVGK-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (5.50 vs 0.45 bp); alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: PIT offense succeeds (4+ goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17PITVGK-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (4.26 vs 0.86 bp); alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.044); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:SUPPRESSED (p 0.4708): highest fidelity KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.3109): highest fidelity KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.2823): highest fidelity KXNHLPTS-26OCT17PITVGK-VGKJEICHEL9-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17PITVGK-VGKJEICHEL9-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5155, phi -0.202)
- KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3109, phi -0.225)
- KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4708, phi -0.264)

portfolios: A EV +2.81 (adj +0.41) on $13.75, P(profit) 0.6271, adj growth 3.8 bp · B EV +1.46 (adj +0.69) on $16.53, P(profit) 0.6441, adj growth 6.6 bp · C EV +3.20 (adj +0.83) on $19.99, P(profit) 0.7052, adj growth 7.8 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.7344, adj growth 2.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
