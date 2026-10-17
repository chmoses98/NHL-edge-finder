# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T20:51:38Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +23.44 | +5.62 | +22.93 | 0.787 | -13.84 | -23.37 | 51.87 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +18.55 | +9.39 | +16.80 | 0.719 | -19.06 | -28.39 | 89.04 |
| C best expression per thesis | 150.01 | +22.29 | +8.15 | +21.15 | 0.739 | -21.70 | -32.19 | 75.46 |
| R FUNDED research stakes | 21.00 | +2.30 | +1.54 | -0.31 | 0.482 | -6.97 | -8.75 | 0.00 |

## SEA @ FLA  ·  10000 joint draws  ·  418 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.632 / away 0.368

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
| Ben Meyers: 1+ goals YES | 10 | 0.148 | 0.135 | +0.042 | +0.028 | $2.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 63 | 0.709 | 0.688 | +0.062 | +0.041 | $6.25 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 62 | 0.694 | 0.673 | +0.057 | +0.036 | $6.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 14 | 0.193 | 0.173 | +0.044 | +0.025 | $2.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes; why: higher confidence-adjusted growth (17.95 vs 12.66 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (16.50 vs 12.51 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: FLA offense succeeds (4+ goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no has the higher standalone adjusted growth (16.50 vs 12.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: FLA offense succeeds (4+ goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes; why: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes has the higher standalone adjusted growth (12.66 vs 10.45 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.007); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis FLA:SUPPRESSED (p 0.3867): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.3753): highest fidelity KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2633): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes (same contract)
- KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.183)
- KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4008, phi -0.247)
- KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4008, phi -0.229)
- KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.198)

portfolios: A EV +2.61 (adj +0.44) on $14.89, P(profit) 0.6491, adj growth 4.0 bp · B EV +2.95 (adj +1.88) on $17.66, P(profit) 0.6335, adj growth 18.0 bp · C EV +3.06 (adj +1.79) on $17.95, P(profit) 0.7518, adj growth 16.6 bp · R EV +0.19 (adj +0.13) on $2.00, P(profit) 0.7086, adj growth 5.0 bp

## NYI @ TOR  ·  10000 joint draws  ·  458 bet sides mapped, 1 +EV candidates, 1 on card

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
| Auston Matthews: 1+ goals NO | 58 | 0.620 | 0.608 | +0.022 | +0.011 | $2.96 | FUNDED_RESEARCH | $1 | TOR:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NYITOR-TORKMARCHENKO86-1|no; why: higher confidence-adjusted growth (1.17 vs 0.71 bp); despite a smaller raw edge (+0.022 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:SUPPRESSED (p 0.3797): highest fidelity KXNHLGOAL-26OCT17NYITOR-TORAMATTHEWS34-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17NYITOR-TORAMATTHEWS34-1|no (same contract)
- KXNHLGOAL-26OCT17NYITOR-TORAMATTHEWS34-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4002, phi -0.282)

portfolios: A EV +0.16 (adj +0.08) on $4.15, P(profit) 0.6195, adj growth 0.7 bp · B EV +0.11 (adj +0.06) on $2.96, P(profit) 0.6195, adj growth 0.5 bp · C EV +0.16 (adj +0.08) on $4.28, P(profit) 0.6195, adj growth 0.8 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6195, adj growth 0.7 bp

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
| Owen Power: 1+ goals NO | 87 | 0.904 | 0.894 | +0.026 | +0.016 | $8.34 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Ryan McLeod: 1+ goals YES | 15 | 0.183 | 0.172 | +0.024 | +0.013 | $1.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 24 | 0.276 | 0.265 | +0.024 | +0.012 | $1.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ goals NO | 58 | 0.621 | 0.609 | +0.024 | +0.012 | $3.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHL3PTOTAL-26OCT17BUFMTL-2|no; why: higher confidence-adjusted growth (5.47 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 1.003 vs 0.902); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: BUF offense succeeds (4+ goals)
- **Ryan McLeod: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (2.88 vs 1.65 bp); relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: BUF offense suppressed (<= 2 goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17BUFMTL-BUFOPOWER25-1|yes; why: higher confidence-adjusted growth (1.65 vs 1.60 bp); despite a smaller raw edge (+0.024 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: BUF offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17BUFMTL-MTLCKREIDER22-1|no; why: higher confidence-adjusted growth (1.39 vs 0.35 bp); alternative not eligible: confidence-adjusted EV +0.0055 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.3845): highest fidelity KXNHLAST-26OCT17BUFMTL-BUFOPOWER25-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT17BUFMTL-BUFOPOWER25-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3662): highest fidelity KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no (same contract)
- thesis BUF:NET_LOW_VOLUME (p 0.4665): highest fidelity KXNHLSAVE-26OCT17BUFMTL-BUFULUUKKONEN1-26|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT17BUFMTL-BUFULUUKKONEN1-26|no (same contract)
- KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3845, phi -0.132)
- KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.19)
- KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.243)
- KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4184, phi -0.264)

portfolios: A EV +1.94 (adj +0.45) on $14.89, P(profit) 0.5219, adj growth 4.1 bp · B EV +0.76 (adj +0.43) on $14.64, P(profit) 0.7142, adj growth 4.1 bp · C EV +1.41 (adj +0.30) on $11.77, P(profit) 0.552, adj growth 2.8 bp · R EV +0.09 (adj +0.06) on $3.00, P(profit) 0.9039, adj growth 2.1 bp

## SJS @ DET  ·  10000 joint draws  ·  440 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.583 / away 0.417

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
| Nate Danielson: 1+ goals NO | 84 | 0.884 | 0.872 | +0.035 | +0.022 | $6.83 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Macklin Celebrini: 1+ assists NO | 43 | 0.595 | 0.467 | +0.147 | +0.020 | $3.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.77) | CALIBRATION_WARNING | D |
| Ivar Stenberg: 1+ assists NO | 70 | 0.809 | 0.732 | +0.095 | +0.017 | $6.05 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Detroit wins by over 2.5 goals NO | 76 | 0.811 | 0.783 | +0.038 | +0.010 | $4.86 | FUNDED_RESEARCH | $2 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nate Danielson: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no; why: higher confidence-adjusted growth (8.66 vs 1.87 bp); despite a smaller raw edge (+0.035 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.005 vs 0.89); relationships: KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT17SJDET-DET3|no: MOSTLY_INDEPENDENT (phi 0.098); failure: DET offense succeeds (4+ goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17SJDET-SJMCELEBRINI71-2|no; why: higher confidence-adjusted growth (3.61 vs 0.70 bp); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.049); KXNHLSPREAD-26OCT17SJDET-DET3|no: INTENTIONAL_DIVERSIFIER (phi -0.163); failure: SJS offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no; why: second expression of the same thesis: KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no has the higher standalone adjusted growth (3.61 vs 3.13 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.049); they share one thesis budget; relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.049); KXNHLSPREAD-26OCT17SJDET-DET3|no: INTENTIONAL_DIVERSIFIER (phi -0.107); failure: SJS offense succeeds (4+ goals)
- **Detroit wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no; why: Broad expression KXNHLSPREAD-26OCT17SJDET-DET3|no selected over player prop KXNHLAST-26OCT17SJDET-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.98 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.098); KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.163); KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.107); failure: DET wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.4125): highest fidelity KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no (same contract)
- thesis DET:SUPPRESSED (p 0.3918): highest fidelity KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no (same contract)
- thesis SJS:WINS (p 0.4876): highest fidelity KXNHLSPREAD-26OCT17SJDET-DET3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3892, phi -0.152)
- KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.9 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3648, phi -0.285)
- KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.9 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3648, phi -0.212)
- KXNHLSPREAD-26OCT17SJDET-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2983, phi -0.741)
- override: Broad expression KXNHLSPREAD-26OCT17SJDET-DET3|no selected over player prop KXNHLAST-26OCT17SJDET-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.98 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.72 (adj +0.51) on $14.89, P(profit) 0.5485, adj growth 4.8 bp · B EV +2.34 (adj +0.53) on $20.84, P(profit) 0.7972, adj growth 5.1 bp · C EV +2.83 (adj +0.50) on $13.27, P(profit) 0.5053, adj growth 4.6 bp · R EV +0.18 (adj +0.08) on $4.00, P(profit) 0.7289, adj growth 3.0 bp

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
| Drake Batherson: 1+ goals NO | 68 | 0.739 | 0.723 | +0.044 | +0.028 | $7.03 | FUNDED_RESEARCH | $2 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| David Jiricek: 1+ goals NO | 92 | 0.952 | 0.940 | +0.027 | +0.015 | $7.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.98) | EVIDENCE_STRONGER | D |
| Dylan Cozens: 1+ goals NO | 72 | 0.763 | 0.751 | +0.029 | +0.017 | $5.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Drake Batherson: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no; why: higher confidence-adjusted growth (8.05 vs 6.51 bp); despite a smaller raw edge (+0.044 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17OTTPHI-PHIDJIRICEK55-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: OTT offense succeeds (4+ goals)
- **David Jiricek: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17OTTPHI-PHIDJIRICEK55-1|no; why: higher confidence-adjusted growth (7.51 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.056/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: PHI offense succeeds (4+ goals)
- **Dylan Cozens: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no; why: Player prop expression KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.87 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT17OTTPHI-PHIDJIRICEK55-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.4466): highest fidelity KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no — Player prop expression KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.87 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:SUPPRESSED (p 0.4749): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17OTTPHI-OTTDBATHERSON19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3398, phi -0.233)
- KXNHLGOAL-26OCT17OTTPHI-PHIDJIRICEK55-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3027, phi -0.089)
- KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3398, phi -0.223)
- override: Player prop expression KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.87 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.27 (adj +0.51) on $14.89, P(profit) 0.626, adj growth 4.9 bp · B EV +0.88 (adj +0.53) on $20.01, P(profit) 0.5344, adj growth 5.2 bp · C EV +0.76 (adj +0.48) on $12.08, P(profit) 0.7391, adj growth 4.5 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.7391, adj growth 3.1 bp

## NYR @ CBJ  ·  10000 joint draws  ·  418 bet sides mapped, 5 +EV candidates, 4 on card

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
| J.T. Miller: 1+ assists NO | 58 | 0.656 | 0.615 | +0.059 | +0.018 | $3.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Full Game: Over 3.5 goals scored NO | 12 | 0.163 | 0.139 | +0.035 | +0.012 | $1.04 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | DIRECT (0.62) | EVIDENCE_MIXED | D |
| Danton Heinen: 1+ goals YES | 11 | 0.136 | 0.127 | +0.019 | +0.010 | $1.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 69 | 0.728 | 0.716 | +0.023 | +0.011 | $2.29 | FUNDED_RESEARCH | $1 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **J.T. Miller: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT17NYRCBJ-4|no; why: higher confidence-adjusted growth (3.07 vs 2.60 bp); wins across more scripts (relative breadth 0.975 vs 0.35); relationships: KXNHLTOTAL-26OCT17NYRCBJ-4|no: REINFORCING (phi 0.183); KXNHLGOAL-26OCT17NYRCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: REINFORCING (phi 0.209); failure: NYR offense succeeds (4+ goals)
- **Full Game: Over 3.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT17NYRCBJ-5|no; why: higher confidence-adjusted growth (2.60 vs 0.02 bp); alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no: REINFORCING (phi 0.183); KXNHLGOAL-26OCT17NYRCBJ-CBJDHEINEN58-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.099); KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi 0.132); failure: CBJ offense succeeds (4+ goals)
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (2.23 vs 1.28 bp); despite a smaller raw edge (+0.019 vs +0.021/contract); alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLTOTAL-26OCT17NYRCBJ-4|no: INTENTIONAL_DIVERSIFIER (phi -0.099); KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no; why: Player prop expression KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no selected over player prop KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.85 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no: REINFORCING (phi 0.209); KXNHLTOTAL-26OCT17NYRCBJ-4|no: INTENTIONAL_DIVERSIFIER (phi 0.132); KXNHLGOAL-26OCT17NYRCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYR:SUPPRESSED (p 0.4701): highest fidelity KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no — Player prop expression KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no selected over player prop KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.85 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis GAME:LOW_EVENT (p 0.263): highest fidelity KXNHLTOTAL-26OCT17NYRCBJ-4|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT17NYRCBJ-4|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.4038): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT17NYRCBJ-NYRJMILLER8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3121, phi -0.278)
- KXNHLTOTAL-26OCT17NYRCBJ-4|no: FUNDED_RESEARCH; family MIXED; loses 38% of the draws where the thesis happens; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4038, phi -0.363)
- KXNHLGOAL-26OCT17NYRCBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3685, phi -0.165)
- KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3121, phi -0.228)
- override: Player prop expression KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no selected over player prop KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.85 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.44 (adj +0.46) on $14.89, P(profit) 0.474, adj growth 4.2 bp · B EV +0.95 (adj +0.36) on $8.49, P(profit) 0.618, adj growth 3.4 bp · C EV +1.01 (adj +0.32) on $7.67, P(profit) 0.6798, adj growth 3.0 bp · R EV +0.31 (adj +0.11) on $2.00, P(profit) 0.1629, adj growth 3.5 bp

## DAL @ CHI  ·  10000 joint draws  ·  398 bet sides mapped, 17 +EV candidates, 4 on card

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
| Frank Nazar: 2+ goals YES | 2 | 0.034 | 0.033 | +0.013 | +0.012 | $1.17 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.08) | EVIDENCE_STRONGER | D |
| Anton Frondell: 1+ goals YES | 19 | 0.247 | 0.231 | +0.047 | +0.030 | $3.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 24 | 0.295 | 0.280 | +0.042 | +0.027 | $3.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 11 | 0.148 | 0.134 | +0.032 | +0.017 | $1.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Frank Nazar: 2+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes; why: higher confidence-adjusted growth (13.48 vs 11.99 bp); despite a smaller raw edge (+0.013 vs +0.047/contract); relationships: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.025); failure: CHI offense suppressed (<= 2 goals)
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes; why: higher confidence-adjusted growth (11.99 vs 11.44 bp); despite a smaller raw edge (+0.047 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.939 vs 0.536); relationships: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-2|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (11.99 vs 8.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-2|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CHI offense suppressed (<= 2 goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (11.99 vs 6.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-2|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3529): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes (same contract)
- thesis CHI:WINS_BY_2PLUS (p 0.2507): highest fidelity KXNHLSPREAD-26OCT17DALCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.4708): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 92% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.15)
- KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.246)
- KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.259)
- KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.195)

portfolios: A EV +2.90 (adj +0.55) on $14.89, P(profit) 0.6154, adj growth 5.1 bp · B EV +2.60 (adj +1.81) on $10.09, P(profit) 0.5603, adj growth 17.0 bp · C EV +3.81 (adj +1.53) on $15.59, P(profit) 0.4045, adj growth 14.1 bp · R EV +0.60 (adj +0.55) on $1.00, P(profit) 0.0341, adj growth 16.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17DALCHI-DAL|no == KXNHLGAME-26OCT17DALCHI-CHI|yes

## STL @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 4 +EV candidates, 4 on card

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
| Adam Wilsby: 1+ goals YES | 5 | 0.071 | 0.065 | +0.017 | +0.012 | $1.21 | FUNDED_RESEARCH | $1 | NSH:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 24 | 0.284 | 0.272 | +0.031 | +0.019 | $2.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Matthew Wood: 1+ goals YES | 19 | 0.221 | 0.212 | +0.020 | +0.011 | $1.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Jake Neighbours: 1+ assists YES | 24 | 0.308 | 0.264 | +0.056 | +0.011 | $1.18 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT17STLNSH-9|yes; why: higher confidence-adjusted growth (6.21 vs 0.94 bp); despite a smaller raw edge (+0.017 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.912 vs 0.376); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT17STLNSH-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT17STLNSH-STLJNEIGHBOURS63-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: NSH offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17STLNSH-STLJNEIGHBOURS63-1|yes; why: higher confidence-adjusted growth (4.02 vs 1.50 bp); despite a smaller raw edge (+0.031 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT17STLNSH-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT17STLNSH-STLJNEIGHBOURS63-1|yes: MOSTLY_INDEPENDENT (phi 0.101); failure: STL offense suppressed (<= 2 goals)
- **Matthew Wood: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT17STLNSH-9|yes; why: higher confidence-adjusted growth (1.71 vs 0.94 bp); despite a smaller raw edge (+0.020 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.89 vs 0.376); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT17STLNSH-STLJNEIGHBOURS63-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: NSH offense suppressed (<= 2 goals)
- **Jake Neighbours: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (4.02 vs 1.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.101); they share one thesis budget; relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.101); KXNHLGOAL-26OCT17STLNSH-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4049): highest fidelity KXNHLAST-26OCT17STLNSH-STLJNEIGHBOURS63-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.4176): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3659, phi -0.106)
- KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3808, phi -0.248)
- KXNHLGOAL-26OCT17STLNSH-NSHMWOOD71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3659, phi -0.204)
- KXNHLAST-26OCT17STLNSH-STLJNEIGHBOURS63-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3808, phi -0.248)

portfolios: A EV +2.22 (adj +0.89) on $11.85, P(profit) 0.5199, adj growth 7.9 bp · B EV +1.09 (adj +0.59) on $6.21, P(profit) 0.4824, adj growth 5.5 bp · C EV +0.45 (adj +0.27) on $3.66, P(profit) 0.2836, adj growth 2.5 bp · R EV +0.32 (adj +0.23) on $1.00, P(profit) 0.0706, adj growth 7.3 bp

## BOS @ LAK  ·  10000 joint draws  ·  416 bet sides mapped, 3 +EV candidates, 3 on card

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
| Charlie McAvoy: 1+ assists NO | 59 | 0.675 | 0.630 | +0.068 | +0.023 | $6.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 49 | 0.605 | 0.524 | +0.098 | +0.016 | $3.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Hampus Lindholm: 1+ assists YES | 25 | 0.321 | 0.275 | +0.058 | +0.012 | $1.75 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17BOSLA-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (4.81 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.063); failure: BOS offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (2.32 vs 1.01 bp); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: LAK offense succeeds (4+ goals)
- **Hampus Lindholm: 1+ assists YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (1.71 vs 1.29 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BOS:SUPPRESSED (p 0.4519): highest fidelity KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no (same contract)
- thesis LAK:SUPPRESSED (p 0.3978): highest fidelity KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.3292): highest fidelity KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes (same contract)
- KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3292, phi -0.254)
- KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.5 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3926, phi -0.29)
- KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4519, phi -0.271)

portfolios: A EV +2.59 (adj +0.58) on $14.89, P(profit) 0.6063, adj growth 5.2 bp · B EV +1.81 (adj +0.45) on $11.93, P(profit) 0.5613, adj growth 4.2 bp · C EV +2.62 (adj +0.65) on $17.28, P(profit) 0.5613, adj growth 6.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ UTA  ·  10000 joint draws  ·  436 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.554 / away 0.446

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
| Nate Schmidt: 1+ goals YES | 4 | 0.067 | 0.059 | +0.024 | +0.016 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 12 | 0.163 | 0.151 | +0.035 | +0.023 | $2.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 71 | 0.798 | 0.751 | +0.073 | +0.027 | $8.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Zach Hyman: 1+ goals YES | 30 | 0.358 | 0.342 | +0.043 | +0.028 | $4.72 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Nate Schmidt: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (13.17 vs 1.95 bp); relationships: KXNHLGOAL-26OCT17EDMUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: UTA offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (10.50 vs 1.95 bp); relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: UTA offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (8.04 vs 3.60 bp); relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17EDMUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.218); failure: EDM offense succeeds (4+ goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-2|yes; why: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-2|yes because adjusted EV is 1.3 pts higher while thesis capture is 0.51 vs 0.13 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17EDMUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.218); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4295): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes — Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-2|yes because adjusted EV is 1.3 pts higher while thesis capture is 0.51 vs 0.13 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis EDM:SUPPRESSED (p 0.3535): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.4702): highest fidelity KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes (same contract)
- KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3208, phi -0.107)
- KXNHLGOAL-26OCT17EDMUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3208, phi -0.17)
- KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4295, phi -0.328)
- KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3535, phi -0.271)
- override: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-2|yes because adjusted EV is 1.3 pts higher while thesis capture is 0.51 vs 0.13 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +2.48 (adj +0.71) on $14.89, P(profit) 0.5682, adj growth 6.7 bp · B EV +3.05 (adj +1.76) on $17.14, P(profit) 0.4102, adj growth 16.6 bp · C EV +2.55 (adj +1.30) on $21.83, P(profit) 0.6424, adj growth 12.1 bp · R EV +0.28 (adj +0.18) on $2.00, P(profit) 0.358, adj growth 6.3 bp

## PIT @ VGK  ·  10000 joint draws  ·  424 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.642 / away 0.357

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
| Mitch Marner: 1+ goals NO | 68 | 0.734 | 0.720 | +0.039 | +0.024 | $8.34 | FUNDED_RESEARCH | $3 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Evgeni Malkin: 1+ assists NO | 63 | 0.716 | 0.670 | +0.069 | +0.024 | $7.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.084 | 0.075 | +0.020 | +0.011 | $1.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:WINS_BY_2PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Bryan Rust: 1+ goals YES | 24 | 0.286 | 0.272 | +0.033 | +0.019 | $2.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17PITVGK-VGKJEICHEL9-2|no; why: higher confidence-adjusted growth (6.14 vs 1.16 bp); despite a smaller raw edge (+0.039 vs +0.126/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: VGK offense succeeds (4+ goals)
- **Evgeni Malkin: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17PITVGK-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (5.50 vs 0.45 bp); alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: PIT offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK wins by 2+; alternative: KXNHLPTS-26OCT17PITVGK-PITEMALKIN71-1|no; why: higher confidence-adjusted growth (4.54 vs 0.00 bp); despite a smaller raw edge (+0.020 vs +0.064/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: VGK offense suppressed (<= 2 goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17PITVGK-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (4.26 vs 0.86 bp); alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:SUPPRESSED (p 0.4708): highest fidelity KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.3109): highest fidelity KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes (same contract)
- thesis VGK:NET_HIGH_VOLUME (p 0.1594): highest fidelity KXNHLSAVE-26OCT17PITVGK-VGKAHILL33-22|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT17PITVGK-VGKAHILL33-22|yes (same contract)
- KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5155, phi -0.202)
- KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3109, phi -0.225)
- KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2823, phi -0.1)
- KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4708, phi -0.264)

portfolios: A EV +2.11 (adj +0.44) on $14.89, P(profit) 0.649, adj growth 4.2 bp · B EV +2.02 (adj +0.99) on $20.04, P(profit) 0.6713, adj growth 9.4 bp · C EV +3.65 (adj +0.93) on $24.63, P(profit) 0.7021, adj growth 8.6 bp · R EV +0.17 (adj +0.10) on $3.00, P(profit) 0.7344, adj growth 3.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
